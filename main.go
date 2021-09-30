package main

import (
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"log"
	"net"
	pb "server/proto"
)


type server struct{

}

func (s *server)Compute(ctx context.Context, x *pb.DataRequest)(*pb.DataResponse, error){
	y:=2*x.X+1
	log.Print("Received value of x: ", x.X)
	log.Print("The Y value is: ", y)
	return &pb.DataResponse{Y:y}, nil
}

const(
	port=":50001"
)

func main(){
	print("Salut !")
	lis, err:=net.Listen("tcp", port)
	if err!=nil{
		log.Fatalf("Error !")
	}
	s:=grpc.NewServer()
	pb.RegisterComputeFunctionServer(s, &server{})
	log.Printf("Starting gRPC listener on port " + port)

	if err=s.Serve(lis); err!=nil{
		log.Fatalf("Fatal to serve: %v", err)
	}
}
