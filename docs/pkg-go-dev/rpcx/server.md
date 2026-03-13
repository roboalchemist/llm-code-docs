### Index ¶

- Constants

- Variables

- 
        func HTTPRequest2RpcxRequest(r *http.Request) (*protocol.Message, error)

- 
        func RegisterMakeListener(network string, ml MakeListener)

- 
          type CMuxPlugin

- 
          type CORSOptions

- 

  - 
            func AllowAllCORSOptions() *CORSOptions

- 
          type Context

- 

  - 
            func NewContext(ctx *share.Context, conn net.Conn, req *protocol.Message, async bool) *Context

- 

  - 
            func (ctx *Context) Bind(v interface{}) error

  - 
            func (ctx *Context) DeleteKey(key interface{})

  - 
            func (ctx *Context) Get(key interface{}) interface{}

  - 
            func (ctx *Context) Metadata() map[string]string

  - 
            func (ctx *Context) Payload() []byte

  - 
            func (ctx *Context) ServiceMethod() string

  - 
            func (ctx *Context) ServicePath() string

  - 
            func (ctx *Context) SetValue(key, val interface{})

  - 
            func (ctx *Context) Write(v interface{}) error

  - 
            func (ctx *Context) WriteError(err error) error

- 
          type DownloadFileHandler

- 
          type FileTransfer

- 

  - 
            func NewFileTransfer(addr string, handler FileTransferHandler, ...) *FileTransfer

- 

  - 
            func (s *FileTransfer) Start() error

  - 
            func (s *FileTransfer) Stop() error

- 
          type FileTransferHandler

- 
          type FileTransferService

- 

  - 
            func (s *FileTransferService) DownloadFile(ctx context.Context, args *share.DownloadFileArgs, ...) error

  - 
            func (s *FileTransferService) TransferFile(ctx context.Context, args *share.FileTransferArgs, ...) error

- 
          type Handler

- 
          type HeartbeatPlugin

- 
          type ID

- 

  - 
            func (id *ID) MarshalJSON() ([]byte, error)

  - 
            func (id *ID) String() string

  - 
            func (id *ID) UnmarshalJSON(data []byte) error

- 
          type JSONRPCError

- 

  - 
            func (err *JSONRPCError) JSONRPCError() string

- 
          type MakeListener

- 
          type OptionFn

- 

  - 
            func WithAsyncWrite() OptionFn

  - 
            func WithCustomPool(pool WorkerPool) OptionFn

  - 
            func WithPool(maxWorkers, maxCapacity int, options ...pond.Option) OptionFn

  - 
            func WithReadTimeout(readTimeout time.Duration) OptionFn

  - 
            func WithTCPKeepAlivePeriod(period time.Duration) OptionFn

  - 
            func WithTLSConfig(cfg *tls.Config) OptionFn

  - 
            func WithWriteTimeout(writeTimeout time.Duration) OptionFn

- 
          type Plugin

- 
          type PluginContainer

- 
          type PostCallPlugin

- 
          type PostConnAcceptPlugin

- 
          type PostConnClosePlugin

- 
          type PostHTTPRequestPlugin

- 
          type PostReadRequestPlugin

- 
          type PostWriteRequestPlugin

- 
          type PostWriteResponsePlugin

- 
          type PreCallPlugin

- 
          type PreHandleRequestPlugin

- 
          type PreReadRequestPlugin

- 
          type PreWriteRequestPlugin

- 
          type PreWriteResponsePlugin

- 
          type RegisterFunctionPlugin

- 
          type RegisterPlugin

- 
          type Reset

- 
          type RpcServiceInternalError

- 

  - 
            func (e RpcServiceInternalError) Error() string

  - 
            func (e RpcServiceInternalError) String() string

- 
          type Server

- 

  - 
            func NewServer(options ...OptionFn) *Server

- 

  - 
            func (s *Server) ActiveClientConn() []net.Conn

  - 
            func (s *Server) AddHandler(servicePath, serviceMethod string, handler func(*Context) error)

  - 
            func (s *Server) Address() net.Addr

  - 
            func (s *Server) Close() error

  - 
            func (s *Server) EnableFileTransfer(serviceName string, fileTransfer *FileTransfer)

  - 
            func (s *Server) EnableStreamService(serviceName string, streamService *StreamService)

  - 
            func (s *Server) ListServices() []string

  - 
            func (s *Server) Register(rcvr interface{}, metadata string) error

  - 
            func (s *Server) RegisterFunction(servicePath string, fn interface{}, metadata string) error

  - 
            func (s *Server) RegisterFunctionName(servicePath string, name string, fn interface{}, metadata string) error

  - 
            func (s *Server) RegisterName(name string, rcvr interface{}, metadata string) error

  - 
            func (s *Server) RegisterOnRestart(f func(s *Server))

  - 
            func (s *Server) RegisterOnShutdown(f func(s *Server))

  - 
            func (s *Server) Restart(ctx context.Context) error

  - 
            func (s *Server) SendMessage(conn net.Conn, servicePath, serviceMethod string, metadata map[string]string, ...) error

  - 
            func (s *Server) Serve(network, address string) (err error)

  - 
            func (s *Server) ServeHTTP(w http.ResponseWriter, req *http.Request)

  - 
            func (s *Server) ServeListener(network string, ln net.Listener) (err error)

  - 
            func (s *Server) ServeWS(conn *websocket.Conn)

  - 
            func (s *Server) SetCORS(options *CORSOptions)

  - 
            func (s *Server) Shutdown(ctx context.Context) error

  - 
            func (s *Server) UnregisterAll() error

  - 
            func (s *Server) UpdateHandler(router map[string]Handler)

- 
          type StreamAcceptor

- 
          type StreamHandler

- 
          type StreamService

- 

  - 
            func NewStreamService(addr string, streamHandler StreamHandler, acceptor StreamAcceptor, waitNum int) *StreamService

- 

  - 
            func (s *StreamService) Start() error

  - 
            func (s *StreamService) Stop() error

  - 
            func (s *StreamService) Stream(ctx context.Context, args *share.StreamServiceArgs, ...) error

- 
          type VersionTag

- 

  - 
            func (VersionTag) MarshalJSON() ([]byte, error)

  - 
            func (VersionTag) UnmarshalJSON(data []byte) error

- 
          type WorkerPool

### Constants ¶

  
    
      View Source
      

```
const (
	XVersion           = "X-RPCX-Version"
	XMessageType       = "X-RPCX-MessageType"
	XHeartbeat         = "X-RPCX-Heartbeat"
	XOneway            = "X-RPCX-Oneway"
	XMessageStatusType = "X-RPCX-MessageStatusType"
	XSerializeType     = "X-RPCX-SerializeType"
	XCompressType      = "X-RPCX-CompressType"
	XMessageID         = "X-RPCX-MessageID"
	XServicePath       = "X-RPCX-ServicePath"
	XServiceMethod     = "X-RPCX-ServiceMethod"
	XMeta              = "X-RPCX-Meta"
	XErrorMessage      = "X-RPCX-ErrorMessage"
)
```

    
  

    
      View Source
      

```
const (
	// CodeUnknownJSONRPCError should be used for all non coded errors.
	CodeUnknownJSONRPCError = -32001
	// CodeParseJSONRPCError is used when invalid JSON was received by the server.
	CodeParseJSONRPCError = -32700
	// CodeInvalidjsonrpcRequest is used when the JSON sent is not a valid jsonrpcRequest object.
	CodeInvalidjsonrpcRequest = -32600
	// CodeMethodNotFound should be returned by the handler when the method does
	// not exist / is not available.
	CodeMethodNotFound = -32601
	// CodeInvalidParams should be returned by the handler when method
	// parameter(s) were invalid.
	CodeInvalidParams = -32602
	// CodeInternalJSONRPCError is not currently returned but defined for completeness.
	CodeInternalJSONRPCError = -32603
)
```

    
  

    
      View Source
      

```
const (
	// ReaderBuffsize is used for bufio reader.
	ReaderBuffsize = 1024
	// WriterBuffsize is used for bufio writer.
	WriterBuffsize = 1024
)
```

    
  

  
### Variables ¶

  
    
      View Source
      

```
var (
	ErrServerClosed  = errors.New("http: Server closed")
	ErrReqReachLimit = errors.New("request reached rate limit")
)
```

    
  

ErrServerClosed is returned by the Server's Serve, ListenAndServe after a call to Shutdown or Close.

    
      View Source
      

```
var (
	// RemoteConnContextKey is a context key. It can be used in
	// services with context.WithValue to access the connection arrived on.
	// The associated value will be of type net.Conn.
	RemoteConnContextKey = &contextKey{"remote-conn"}
	// StartRequestContextKey records the start time
	StartRequestContextKey = &contextKey{"start-parse-request"}
	// StartSendRequestContextKey records the start time
	StartSendRequestContextKey = &contextKey{"start-send-request"}
	// TagContextKey is used to record extra info in handling services. Its value is a map[string]interface{}
	TagContextKey = &contextKey{"service-tag"}
	// HttpConnContextKey is used to store http connection.
	HttpConnContextKey = &contextKey{"http-conn"}
)
```

    
  

    
      View Source
      

```
var ErrNotAccept = errors.New("server refused the connection")
```

    
  

  
### Functions ¶

  
	  
  
  
    
#### 
      func HTTPRequest2RpcxRequest ¶
  
    
  

    
    
      

```
func HTTPRequest2RpcxRequest(r *http.Request) (*protocol.Message, error)
```

    
  

HTTPRequest2RpcxRequest converts a http request to a rpcx request.

  

        
	  
  
  
    
#### 
      func RegisterMakeListener ¶
  
    
  

    
    
      

```
func RegisterMakeListener(network string, ml MakeListener)
```

    
  

RegisterMakeListener registers a MakeListener for network.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type CMuxPlugin ¶
  
    
      added in
      v1.6.3
    
  

    
    
      

```
type CMuxPlugin interface {
	MuxMatch(m cmux.CMux)
}
```