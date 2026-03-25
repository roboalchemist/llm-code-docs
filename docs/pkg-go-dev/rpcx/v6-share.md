### Index ¶

- Constants

- Variables

- 
        func GetOpencensusSpanContextFromContext(ctx context.Context) (*trace.SpanContext, error)

- 
        func GetSpanContextFromContext(ctx context.Context) (opentracing.SpanContext, error)

- 
        func RegisterCodec(t protocol.SerializeType, c codec.Codec)

- 
          type Context

- 

  - 
            func NewContext(ctx context.Context) *Context

  - 
            func WithLocalValue(ctx *Context, key, val interface{}) *Context

  - 
            func WithValue(parent context.Context, key, val interface{}) *Context

- 

  - 
            func (c *Context) SetValue(key, val interface{})

  - 
            func (c *Context) String() string

  - 
            func (c *Context) Value(key interface{}) interface{}

- 
          type ContextKey

- 
          type DownloadFileArgs

- 
          type FileTransferArgs

- 
          type FileTransferReply

### Constants ¶

  
    
      View Source
      

```
const (
	// DefaultRPCPath is used by ServeHTTP.
	DefaultRPCPath = "/_rpcx_"

	// AuthKey is used in metadata.
	AuthKey = "__AUTH"

	// ServerAddress is used to get address of the server by client
	ServerAddress = "__ServerAddress"

	// ServerTimeout timeout value passed from client to control timeout of server
	ServerTimeout = "__ServerTimeout"

	// OpentracingSpanServerKey key in service context
	OpentracingSpanServerKey = "opentracing_span_server_key"
	// OpentracingSpanClientKey key in client context
	OpentracingSpanClientKey = "opentracing_span_client_key"

	// OpencensusSpanServerKey key in service context
	OpencensusSpanServerKey = "opencensus_span_server_key"
	// OpencensusSpanClientKey key in client context
	OpencensusSpanClientKey = "opencensus_span_client_key"
	// OpencensusSpanRequestKey span key in request meta
	OpencensusSpanRequestKey = "opencensus_span_request_key"

	// SendFileServiceName file transfer service.
	SendFileServiceName = "_filetransfer"
)
```

    
  

  
### Variables ¶

  
    
      View Source
      

```
var (
	// Codecs are codecs supported by rpcx. You can add customized codecs in Codecs.
	Codecs = map[protocol.SerializeType]codec.Codec{
		protocol.SerializeNone: &codec.ByteCodec{},
		protocol.JSON:          &codec.JSONCodec{},
		protocol.ProtoBuffer:   &codec.PBCodec{},
		protocol.MsgPack:       &codec.MsgpackCodec{},
		protocol.Thrift:        &codec.ThriftCodec{},
	}
)
```

    
  

    
      View Source
      

```
var ReqMetaDataKey = ContextKey("__req_metadata")
```

    
  

ReqMetaDataKey is used to set metatdata in context of requests.

    
      View Source
      

```
var ResMetaDataKey = ContextKey("__res_metadata")
```

    
  

ResMetaDataKey is used to set metatdata in context of responses.

  
### Functions ¶

  
	  
  
  
    
#### 
      func GetOpencensusSpanContextFromContext ¶
  
    
  

    
    
      

```
func GetOpencensusSpanContextFromContext(ctx context.Context) (*trace.SpanContext, error)
```

    
  

GetOpencensusSpanContextFromContext get opencensus.trace.SpanContext from context.Context.

  

        
	  
  
  
    
#### 
      func GetSpanContextFromContext ¶
  
    
  

    
    
      

```
func GetSpanContextFromContext(ctx context.Context) (opentracing.SpanContext, error)
```

    
  

GetSpanContextFromContext get opentracing.SpanContext from context.Context.

  

        
	  
  
  
    
#### 
      func RegisterCodec ¶
  
    
  

    
    
      

```
func RegisterCodec(t protocol.SerializeType, c codec.Codec)
```

    
  

RegisterCodec register customized codec.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type Context ¶
  
    
  

    
    
      

```
type Context struct {
	context.Context
	// contains filtered or unexported fields
}
```

    
  

Context is a rpcx customized Context that can contains multiple values.

    
  
  
    
#### 
      func NewContext ¶
  
    
  

    
    
      

```
func NewContext(ctx context.Context) *Context
```