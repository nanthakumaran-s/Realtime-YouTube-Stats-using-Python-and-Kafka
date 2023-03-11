from kafka import KafkaConsumer
from json import dump, loads
from sys import argv
from uuid import uuid4 as v4
from s3fs import S3FileSystem

consumer = KafkaConsumer(argv[1], bootstrap_servers=[
                         '0.0.0.0:9092'], value_deserializer=lambda x: loads(x.decode('utf-8')), auto_offset_reset='earliest')

if __name__ == "__main__":
    for message in consumer:
        print(message)
        s3 = S3FileSystem()
        file = ""
        if (argv[1] == 'comments'):
            file = argv[1] + '/comments-stat-' + str(v4())
        else:
            file = argv[1] + '/video-stat-' + str(v4())
        with s3.open("s3://youtube-stats-kafka/{}".format(file), 'w') as f:
            dump(message, f)
