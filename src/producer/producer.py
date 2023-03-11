from kafka import KafkaProducer
from json import dumps
import pandas as pd
import os
from time import sleep
from sys import argv

producer = KafkaProducer(bootstrap_servers=[
                         '0.0.0.0:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))


def run():
    if (argv[1] == 'comments'):
        path = os.path.join(os.path.dirname(__file__),
                            'Youtube-Stats/comments.csv')

    if (argv[1] == 'video-stats'):
        path = os.path.join(os.path.dirname(__file__),
                            'Youtube-Stats/video-stats.csv')
    df = pd.read_csv(path)
    for _, row in df.iterrows():
        producer.send(argv[1], value=row.to_dict())
        sleep(1)


if __name__ == '__main__':
    run()
