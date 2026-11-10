from pymongo import MongoClient

db = MongoClient("mongodb://localhost:27017")["ecommerce"]
txns = db.transactions

print("--- Aggregation 1: Top 5 Most Sold Products ---")
pipeline_1 = [
    {"$unwind": "$items"},
    {"$group": {"_id": "$items.product_id", "total_sold": {"$sum": "$items.quantity"}}},
    {"$sort": {"total_sold": -1}},
    {"$limit": 5}
]
for doc in txns.aggregate(pipeline_1):
    print(doc)

print("\n--- Aggregation 2: Revenue by Payment Method ---")
pipeline_2 = [
    {"$group": {"_id": "$payment_method", "total_revenue": {"$sum": "$total"}, "txn_count": {"$sum": 1}}},
    {"$sort": {"total_revenue": -1}}
]
for doc in txns.aggregate(pipeline_2):
    print(doc)