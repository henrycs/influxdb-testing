from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "my-bucket"

client = InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org")

delete_api = client.delete_api()
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

start = "1970-01-01T00:00:00Z"
stop = "2022-05-07T00:00:00Z"
delete_api.delete(start, stop, '_measurement="my_measurement"', bucket='my-bucket', org='my-org')

# 2022-05-06T03:15:33.749328477Z   1546300800000  1651815312
#p = Point("my_measurement").tag("location", "Wuhan").tag("Sum", "100").field("temperature", 29.3).field("humidity", 0.61).time('2022-05-06T05:40:05.00Z')
#p = Point("my_measurement").tag("location", "Beijing").field("temperature", 29.3).field("humidity", 0.61).time(1651815312000000, write_precision=WritePrecision.NS)
#write_api.write(bucket=bucket, record=p)

## using Table structure
#tables = query_api.query('from(bucket:"my-bucket") |> range(start: 0) |> filter(fn: (r) => r._measurement == "my_measurement")')
tables = query_api.query('from(bucket:"my-bucket") |> range(start: 0) |> filter(fn: (r) => r._measurement == "security_list")')

for table in tables:
    print('----',table)
    for row in table.records:
        print (row.values)

print('-----')

## using csv library
csv_result = query_api.query_csv('from(bucket:"my-bucket") |> range(start: -10m)')
print(csv_result)
val_count = 0
for row in csv_result:
    print(row)
    for cell in row:
        #print(cell)
        val_count += 1