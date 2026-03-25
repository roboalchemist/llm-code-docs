### Overview ¶

Package loadtest implements load testing for pubsub,
following the interface defined in https://github.com/GoogleCloudPlatform/pubsub/tree/master/load-test-framework/ .

This package is experimental.

    
### Index ¶

- 
          type PubServer

- 

  - 
            func (l *PubServer) Start(ctx context.Context, req *pb.StartRequest) (*pb.StartResponse, error)

- 
          type SubServer

- 

  - 
            func (s *SubServer) Start(ctx context.Context, req *pb.StartRequest) (*pb.StartResponse, error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type PubServer ¶
  
    
  

    
    
      

```
type PubServer struct {
	ID string

	pb.UnimplementedLoadtestWorkerServer
	// contains filtered or unexported fields
}
```

    
  

PubServer is a dummy Pub/Sub server for load testing.

    
  
  
    
#### 
      func (*PubServer) Start ¶
  
    
  

    
    
      

```
func (l *PubServer) Start(ctx context.Context, req *pb.StartRequest) (*pb.StartResponse, error)
```

    
  

Start starts the server.