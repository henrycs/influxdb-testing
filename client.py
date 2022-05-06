from influxdb_client import InfluxDBClient, Point

client = InfluxDBClient.from_config_file("config.ini")