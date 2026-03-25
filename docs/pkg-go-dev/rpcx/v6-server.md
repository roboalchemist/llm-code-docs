### Index ¶

- Constants

- Variables

- 
        func HTTPRequest2RpcxRequest(r *http.Request) (*protocol.Message, error)

- 
        func RegisterMakeListener(network string, ml MakeListener)

- 
          type CORSOptions

- 

  - 
            func AllowAllCORSOptions() *CORSOptions

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
          type Server

- 

  - 
            func NewServer(options ...OptionFn) *Server

- 

  - 
            func (s *Server) ActiveClientConn() []net.Conn

  - 
            func (s *Server) Address() net.Addr

  - 
            func (s *Server) Close() error

  - 
            func (s *Server) EnableFileTransfer(serviceName string, fileTransfer *FileTransfer)

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
            func (s *Server) SetCORS(options *CORSOptions)

  - 
            func (s *Server) Shutdown(ctx context.Context) error

  - 
            func (s *Server) UnregisterAll() error

- 
          type VersionTag

- 

  - 
            func (VersionTag) MarshalJSON() ([]byte, error)

  - 
            func (VersionTag) UnmarshalJSON(data []byte) error

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
	//CodeInvalidjsonrpcRequest is used when the JSON sent is not a valid jsonrpcRequest object.
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
var ErrServerClosed = errors.New("http: Server closed")
```

    
  

ErrServerClosed is returned by the Server's Serve, ListenAndServe after a call to Shutdown or Close.

    
      View Source
      

```
var UsePool bool
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
      type CORSOptions ¶
  
    
  

    
    
      

```
type CORSOptions struct {
	// AllowedOrigins is a list of origins a cross-domain request can be executed from.
	// If the special "*" value is present in the list, all origins will be allowed.
	// An origin may contain a wildcard (*) to replace 0 or more characters
	// (i.e.: http://*.domain.com). Usage of wildcards implies a small performance penalty.
	// Only one wildcard can be used per origin.
	// Default value is ["*"]
	AllowedOrigins []string
	// AllowOriginFunc is a custom function to validate the origin. It take the origin
	// as argument and returns true if allowed or false otherwise. If this option is
	// set, the content of AllowedOrigins is ignored.
	AllowOriginFunc func(origin string) bool
	// AllowOriginFunc is a custom function to validate the origin. It takes the HTTP Request object and the origin as
	// argument and returns true if allowed or false otherwise. If this option is set, the content of `AllowedOrigins`
	// and `AllowOriginFunc` is ignored.
	AllowOriginRequestFunc func(r *http.Request, origin string) bool
	// AllowedMethods is a list of methods the client is allowed to use with
	// cross-domain requests. Default value is simple methods (HEAD, GET and POST).
	AllowedMethods []string
	// AllowedHeaders is list of non simple headers the client is allowed to use with
	// cross-domain requests.
	// If the special "*" value is present in the list, all headers will be allowed.
	// Default value is [] but "Origin" is always appended to the list.
	AllowedHeaders []string
	// ExposedHeaders indicates which headers are safe to expose to the API of a CORS
	// API specification
	ExposedHeaders []string
	// MaxAge indicates how long (in seconds) the results of a preflight request
	// can be cached
	MaxAge int
	// AllowCredentials indicates whether the request can include user credentials like
	// cookies, HTTP authentication or client side SSL certificates.
	AllowCredentials bool
	// OptionsPassthrough instructs preflight to let other potential next handlers to
	// process the OPTIONS method. Turn this on if your application handles OPTIONS.
	OptionsPassthrough bool
	// Debugging flag adds additional output to debug server side CORS issues
	Debug bool
}
```

    
  

    
  
  
    
#### 
      func AllowAllCORSOptions ¶
  
    
  

    
    
      

```
func AllowAllCORSOptions() *CORSOptions
```

    
  

AllowAllCORSOptions returns a option that allows access.