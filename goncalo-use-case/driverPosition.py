from utils_redis import get_driver_position

# Request most up-to-date drivers position
data = get_driver_position('Goncalo')

print(data)