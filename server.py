# Server Code
# replace [PROTO_FILE_NAME] with Proto filename
# replace [GRPC_SERVICE_NAME] with the service name (name after service command)
# replace [GRPC_METHOD_NAME] with the method name (name after rpc command)
# replace [GRPC_SERVICE_RETURN_TYPE] with the return type that was declared in a message
import grpc
import test_pb2
import test_pb2_grpc
from concurrent import futures

class RoutingServicer(test_pb2_grpc.RoutingServicer):
    def getRoute(self, request, context):
        print("I am here")
        print(request.lat)
        print(request.lang)
        return test_pb2.direction(dir="North")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_RoutingServicer_to_server(
        RoutingServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()