import os, sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, size

# Increase Driver memory to prevent OutOfMemoryError
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Funnel") \
    .config("spark.driver.memory", "4g") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

# Read session data
sess = spark.read.json("data/sessions_*.json")

# Stage 1: View
views = sess.filter(size(col("viewed_products")) > 0).select("session_id").distinct()

# Stage 2: Cart (cart_contents is STRUCT, check isNotNull)
carts = sess.filter(col("cart_contents").isNotNull()).select("session_id").distinct()

# Stage 3: Purchase
purchases = sess.filter(col("conversion_status").like("%purchas%")).select("session_id").distinct()

# Count
v_count = views.count()
c_count = carts.join(views, "session_id").count()
p_count = purchases.join(carts, "session_id").count()

print(f"Funnel Results -> View: {v_count} | Cart: {c_count} | Purchase: {p_count}")

# Save to CSV (add limit to prevent toPandas from exhausting driver memory)
funnel_data = [("View", v_count), ("Cart", c_count), ("Purchase", p_count)]
df_funnel = spark.createDataFrame(funnel_data, ["Stage", "Count"])
df_funnel.limit(10).toPandas().to_csv("visualizations/funnel.csv", index=False)

print("Funnel saved to visualizations/funnel.csv")
spark.stop()