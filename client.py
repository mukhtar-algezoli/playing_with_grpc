# Client Code
# replace [PROTO_FILE_NAME] with Proto filename
# replace [GRPC_SERVICE_NAME] with the service name (name after service command)
# replace [GRPC_METHOD_NAME] with the method name (name after rpc command)
# replace [GRPC_SERVICE_input_TYPE] with the input type that was declared in a message
import grpc
import test_pb2_grpc
import test_pb2
def run():
    with grpc.insecure_channel("10.128.0.5:50051") as channel:
        print("runing client request")
        stub = test_pb2_grpc.RoutingStub(channel)
        # calling function from Server
        # feature = stub.GetDirMeth(test_pb2.point(lang=35, lat=22))
        feature = stub.getRoute(test_pb2.point(lat=35, lang=22))
        # do something with the returned output
        print(feature)



if __name__ == "__main__":
    run()