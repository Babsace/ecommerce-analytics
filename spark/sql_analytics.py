from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("SQLAnalytics").getOrCreate()

# Load data
txn = spark.read.parquet("data/processed/transactions")
prod = spark.read.json("data/products.json")

txn.createOrReplaceTempView("txn")
prod.createOrReplaceTempView("prod")

print("--- Category Revenue ---")
result = spark.sql("""
    SELECT p.category_id, SUM(t.total) AS revenue
    FROM txn t
    JOIN prod p ON t.items[0].product_id = p.product_id
    GROUP BY p.category_id 
    ORDER BY revenue DESC
""")
result.show()
spark.stop()