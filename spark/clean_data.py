from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

spark = SparkSession.builder.master("local[*]").appName("CleanData").getOrCreate()

# Read all JSON files (transactions and sessions)
df_txn = spark.read.json("data/transactions.json")
df_sess = spark.read.json("data/sessions_*.json")

# Clean Transactions
df_txn_clean = df_txn.withColumn("timestamp", to_timestamp("timestamp")).dropna(subset=["user_id"])
df_txn_clean.write.mode("overwrite").parquet("data/processed/transactions")

# Clean Sessions
df_sess_clean = df_sess.withColumn("start_time", to_timestamp("start_time")).dropna(subset=["user_id"])
df_sess_clean.write.mode("overwrite").parquet("data/processed/sessions")

print("Data cleaned and written to Parquet!")
spark.stop()