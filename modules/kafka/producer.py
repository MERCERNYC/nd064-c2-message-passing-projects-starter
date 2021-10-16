from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=' my-release-kafka-0.my-release-kafka-headless.default.svc.cluster.local:9092, api_version=(2, 0, 2)')
msg1=dict({'first_name':'Juliana','last_name':'Lola','company_name':'Udacity'})
producer.send('test', bytes(str(msg1), 'utf-8'))
producer.flush()