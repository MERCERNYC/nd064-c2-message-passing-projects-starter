import grpc
import services_pb2
import services_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5003", options=(('grpc.enable_http_proxy', 0),))
stub = services_pb2_grpc.PersonServiceStub(channel)

# Update this with desired payload
item = services_pb2.PersonMessage(
    id=321,
    first_name="first_name",
    last_name="last_name",
    company_name="company_name"
)


response = stub.Create(item)
print('show response',response);
