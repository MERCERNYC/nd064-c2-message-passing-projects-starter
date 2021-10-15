from __future__ import annotations
from kafka import KafkaConsumer
from dataclasses import dataclass
from datetime import datetime
import logging
logger = logging.getLogger(__name__)
import json
import ast
from services_pb2 import PersonMessage
import services_pb2
import services_pb2_grpc
import grpc


def create_person(req):
    channel = grpc.insecure_channel("192.168.0.113:30033", options=(('grpc.enable_http_proxy', 0),))
    stub = services_pb2_grpc.UdaConnectServiceStub(channel)
    person = PersonMessage(first_name=req["first_name"] , last_name=req["last_name"], company_name=req["company_name"])
    stub.createPerson(person)

consumer = KafkaConsumer('test',
     bootstrap_servers=['my-release-kafka-0.my-release-kafka-headless.default.svc.cluster.local:9092'],
     value_deserializer=lambda m: json.dumps(m.decode('utf-8')))
#ds
for message in consumer:
    resp=eval(json.loads((message.value)))
    logger.warning("consumer value %s", resp);
    create_person(resp)