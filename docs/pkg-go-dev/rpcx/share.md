### Index ¶

- Constants

- Variables

- 
        func IsShareContext(ctx context.Context) bool

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
            func (c *Context) DeleteKey(key interface{})

  - 
            func (c *Context) Lock()

  - 
            func (c *Context) SetValue(key, val interface{})

  - 
            func (c *Context) String() string

  - 
            func (c *Context) Unlock()

  - 
            func (c *Context) Value(key interface{}) interface{}

- 
          type ContextKey

- 
          type DownloadFileArgs

- 

  - 
            func (args DownloadFileArgs) Clone() *DownloadFileArgs

- 
          type FileTransferArgs

- 

  - 
            func (args FileTransferArgs) Clone() *FileTransferArgs

- 
          type FileTransferReply

- 
          type StreamServiceArgs

- 
          type StreamServiceReply

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

	// SendFileServiceName is name of the file transfer service.
	SendFileServiceName = "_filetransfer"

	// StreamServiceName is name of the stream service.
	StreamServiceName = "_streamservice"

	// ContextTagsLock is name of the Context TagsLock.
	ContextTagsLock = "_tagsLock"
)
```

    
  

  
### Variables ¶

  
    
      View Source
      

```
var Codecs = map[protocol.SerializeType]codec.Codec{
	protocol.SerializeNone: &codec.ByteCodec{},
	protocol.JSON:          &codec.JSONCodec{},
	protocol.ProtoBuffer:   &codec.PBCodec{},
	protocol.MsgPack:       &codec.MsgpackCodec{},
	protocol.Thrift:        &codec.ThriftCodec{},
}
```

    
  

Codecs are codecs supported by rpcx. You can add customized codecs in Codecs.

    
      View Source
      

```
var ReqMetaDataKey = ContextKey("__req_metadata")
```

    
  

ReqMetaDataKey is used to set metadata in context of requests.

    
      View Source
      

```
var ResMetaDataKey = ContextKey("__res_metadata")
```

    
  

ResMetaDataKey is used to set metadata in context of responses.

    
      View Source
      

```
var Trace bool
```

    
  

Trace is a flag to write a trace log or not.
You should not enable this flag for product environment and enable it only for test.
It writes trace log with logger Debug level.

  
### Functions ¶

  
	  
  
  
    
#### 
      func IsShareContext ¶
  
    
      added in
      v1.7.5
    
  

    
    
      

```
func IsShareContext(ctx context.Context) bool
```

    
  

IsShareContext checks whether a context is share.Context.

  

        
	  
  
  
    
#### 
      func RegisterCodec ¶
  
    
  

    
    
      

```
func RegisterCodec(t protocol.SerializeType, c codec.Codec)
```

    
  

RegisterCodec register customized codec.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type Context ¶
  
    
      added in
      v1.4.1
    
  

    
    
      

```
type Context struct {
	context.Context
	// contains filtered or unexported fields
}
```

    
  

Context is a rpcx customized Context that can contains multiple values.

    
  
  
    
#### 
      func NewContext ¶
  
    
      added in
      v1.4.1
    
  

    
    
      

```
func NewContext(ctx context.Context) *Context
```