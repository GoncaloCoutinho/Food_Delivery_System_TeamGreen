import pandas as pd
import utils_redis

# Inserting Data into Redis
# from csv
df = pd.read_csv('/mnt/c/Users/Westbrook/Documents/srh_masters/data_engineering_1/drivers_locations.csv', 
                names = ['date', 'latitude', 'longitude', 'driver_id'])

for index, row in df.iterrows():
    utils_redis.insert_coordinates(row['date'], row['longitude'], row['latitude'], row['driver_id'])

# insert one row
utils_redis.insert_coordinates('2022-02-11 11:06:38', 19.693450000, 60.12700000, 0)

utils_redis.r.bgsave()