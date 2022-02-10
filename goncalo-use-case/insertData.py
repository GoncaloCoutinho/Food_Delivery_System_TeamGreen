import pandas as pd
import utils_redis


df = pd.read_csv('/mnt/c/Users/Westbrook/Documents/srh_masters/data_engineering_1/drivers_locations.csv', 
                names = ['date', 'latitude', 'longitude', 'driver_id'])

for index, row in df.iterrows():
    utils_redis.insert_coordinates(row['date'], row['longitude'], row['latitude'], row['driver_id'])

utils_redis.r.bgsave()