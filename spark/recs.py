from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, count

spark = SparkSession.builder.master("local[*]").appName("Recs").getOrCreate()
df = spark.read.parquet("data/processed/transactions")

# "Bought X also bought Y" (Simple co-occurrence)
items_df = df.select("transaction_id", explode("items").alias("item"))
co_occur = items_df.alias("a").join(items_df.alias("b"), "transaction_id") \
    .filter(col("a.item.product_id") != col("b.item.product_id")) \
    .groupBy(col("a.item.product_id").alias("product_A"), col("b.item.product_id").alias("product_B")) \
    .agg(count("*").alias("frequency")) \
    .orderBy(col("frequency").desc())

co_occur.limit(100).toPandas().to_csv("visualizations/recs.csv", index=False)
print("Recommendations saved to visualizations/recs.csv")
spark.stop()