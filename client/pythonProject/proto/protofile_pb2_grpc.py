# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import protofile_pb2 as proto_dot_protofile__pb2


class ComputeFunctionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.compute = channel.unary_unary(
                '/ComputeFunction/compute',
                request_serializer=proto_dot_protofile__pb2.DataRequest.SerializeToString,
                response_deserializer=proto_dot_protofile__pb2.DataResponse.FromString,
                )


class ComputeFunctionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def compute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComputeFunctionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'compute': grpc.unary_unary_rpc_method_handler(
                    servicer.compute,
                    request_deserializer=proto_dot_protofile__pb2.DataRequest.FromString,
                    response_serializer=proto_dot_protofile__pb2.DataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ComputeFunction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ComputeFunction(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def compute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ComputeFunction/compute',
            proto_dot_protofile__pb2.DataRequest.SerializeToString,
            proto_dot_protofile__pb2.DataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
