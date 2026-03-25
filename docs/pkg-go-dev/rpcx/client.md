### Index ¶

- Constants

- Variables

- 
        func CalculateWeight(rtt int) int

- 
        func Hash(key uint64, buckets int32) int32

- 
        func HashString(s string) uint64

- 
        func JumpConsistentHash(len int, options ...interface{}) int

- 
        func Ping(host string) (rtt int, err error)

- 
        func RegisterCacheClientBuilder(network string, builder CacheClientBuilder)

- 
          type Breaker

- 
          type CacheClientBuilder

- 
          type Call

- 
          type Client

- 

  - 
            func NewClient(option Option) *Client

- 

  - 
            func (client *Client) Call(ctx context.Context, servicePath, serviceMethod string, args interface{}, ...) error

  - 
            func (client *Client) Close() error

  - 
            func (client *Client) Connect(network, address string) error

  - 
            func (client *Client) GetConn() net.Conn

  - 
            func (client *Client) Go(ctx context.Context, servicePath, serviceMethod string, args interface{}, ...) *Call

  - 
            func (client *Client) IsClosing() bool

  - 
            func (client *Client) IsShutdown() bool

  - 
            func (client *Client) RegisterServerMessageChan(ch chan<- *protocol.Message)

  - 
            func (client *Client) RemoteAddr() string

  - 
            func (client *Client) SendRaw(ctx context.Context, r *protocol.Message) (map[string]string, []byte, error)

  - 
            func (client *Client) UnregisterServerMessageChan()

- 
          type ClientAfterDecodePlugin

- 
          type ClientBeforeEncodePlugin

- 
          type ClientConnectedPlugin

- 
          type ClientConnectionClosePlugin

- 
          type ConnCreateFailedPlugin

- 
          type ConnCreatedPlugin

- 
          type ConnFactoryFn

- 
          type ConsecCircuitBreaker

- 

  - 
            func NewConsecCircuitBreaker(failureThreshold uint64, window time.Duration) *ConsecCircuitBreaker

- 

  - 
            func (cb *ConsecCircuitBreaker) Call(fn func() error, d time.Duration) error

  - 
            func (cb *ConsecCircuitBreaker) Fail()

  - 
            func (cb *ConsecCircuitBreaker) Ready() bool

  - 
            func (cb *ConsecCircuitBreaker) Success()

- 
          type ConsistentAddrStrFunction

- 
          type DNSDiscovery

- 

  - 
            func NewDNSDiscovery(domain string, network string, port int, d time.Duration) (*DNSDiscovery, error)

- 

  - 
            func (d *DNSDiscovery) Clone(servicePath string) (ServiceDiscovery, error)

  - 
            func (d *DNSDiscovery) Close()

  - 
            func (d *DNSDiscovery) GetServices() []*KVPair

  - 
            func (d *DNSDiscovery) RemoveWatcher(ch chan []*KVPair)

  - 
            func (d *DNSDiscovery) SetFilter(filter ServiceDiscoveryFilter)

  - 
            func (d *DNSDiscovery) WatchService() chan []*KVPair

- 
          type FailMode

- 

  - 
            func FailModeString(s string) (FailMode, error)

  - 
            func FailModeValues() []FailMode

- 

  - 
            func (i FailMode) IsAFailMode() bool

  - 
            func (i FailMode) String() string

- 
          type HashServiceAndArgs

- 
          type KVPair

- 
          type MDNSDiscovery

- 

  - 
            func NewMDNSDiscovery(service string, timeout time.Duration, watchInterval time.Duration, ...) (*MDNSDiscovery, error)

- 

  - 
            func (d *MDNSDiscovery) Clone(servicePath string) (ServiceDiscovery, error)

  - 
            func (d *MDNSDiscovery) Close()

  - 
            func (d *MDNSDiscovery) GetServices() []*KVPair

  - 
            func (d *MDNSDiscovery) RemoveWatcher(ch chan []*KVPair)

  - 
            func (d *MDNSDiscovery) SetFilter(filter ServiceDiscoveryFilter)

  - 
            func (d *MDNSDiscovery) WatchService() chan []*KVPair

- 
          type MultipleServersDiscovery

- 

  - 
            func NewMultipleServersDiscovery(pairs []*KVPair) (*MultipleServersDiscovery, error)

- 

  - 
            func (d *MultipleServersDiscovery) Clone(servicePath string) (ServiceDiscovery, error)

  - 
            func (d *MultipleServersDiscovery) Close()

  - 
            func (d *MultipleServersDiscovery) GetServices() []*KVPair

  - 
            func (d *MultipleServersDiscovery) RemoveWatcher(ch chan []*KVPair)

  - 
            func (d *MultipleServersDiscovery) SetFilter(filter ServiceDiscoveryFilter)

  - 
            func (d *MultipleServersDiscovery) Update(pairs []*KVPair)

  - 
            func (d *MultipleServersDiscovery) WatchService() chan []*KVPair

- 
          type OneClient

- 

  - 
            func NewBidirectionalOneClient(failMode FailMode, selectMode SelectMode, discovery ServiceDiscovery, ...) *OneClient

  - 
            func NewOneClient(failMode FailMode, selectMode SelectMode, discovery ServiceDiscovery, ...) *OneClient

- 

  - 
            func (c *OneClient) Auth(auth string)

  - 
            func (c *OneClient) Broadcast(ctx context.Context, servicePath string, serviceMethod string, ...) error

  - 
            func (c *OneClient) Call(ctx context.Context, servicePath string, serviceMethod string, ...) error

  - 
            func (c *OneClient) Close() error

  - 
            func (c *OneClient) ConfigGeoSelector(latitude, longitude float64)

  - 
            func (c *OneClient) DownloadFile(ctx context.Context, requestFileName string, saveTo io.Writer, ...) error

  - 
            func (c *OneClient) Fork(ctx context.Context, servicePath string, serviceMethod string, ...) error

  - 
            func (c *OneClient) GetPlugins() PluginContainer

  - 
            func (c *OneClient) Go(ctx context.Context, servicePath string, serviceMethod string, ...) (*Call, error)

  - 
            func (c *OneClient) SendFile(ctx context.Context, fileName string, rateInBytesPerSecond int64, ...) error

  - 
            func (c *OneClient) SendRaw(ctx context.Context, r *protocol.Message) (map[string]string, []byte, error)

  - 
            func (c *OneClient) SetPlugins(plugins PluginContainer)

  - 
            func (c *OneClient) SetSelector(servicePath string, s Selector)

  - 
            func (c *OneClient) Stream(ctx context.Context, meta map[string]string) (net.Conn, error)

- 
          type OneClientPool

- 

  - 
            func NewBidirectionalOneClientPool(count int, failMode FailMode, selectMode SelectMode, ...) *OneClientPool

  - 
            func NewOneClientPool(count int, failMode FailMode, selectMode SelectMode, ...) *OneClientPool

- 

  - 
            func (p *OneClientPool) Auth(auth string)

  - 
            func (p *OneClientPool) Close()

  - 
            func (p *OneClientPool) Get() *OneClient

- 
          type Option

- 
          type Peer2PeerDiscovery

- 

  - 
            func NewPeer2PeerDiscovery(server, metadata string) (*Peer2PeerDiscovery, error)

- 

  - 
            func (d *Peer2PeerDiscovery) Clone(servicePath string) (ServiceDiscovery, error)

  - 
            func (d *Peer2PeerDiscovery) Close()

  - 
            func (d *Peer2PeerDiscovery) GetServices() []*KVPair

  - 
            func (d *Peer2PeerDiscovery) RemoveWatcher(ch chan []*KVPair)

  - 
            func (d *Peer2PeerDiscovery) SetFilter(filter ServiceDiscoveryFilter)

  - 
            func (d *Peer2PeerDiscovery) WatchService() chan []*KVPair

- 
          type Plugin

- 
          type PluginContainer

- 

  - 
            func NewPluginContainer() PluginContainer

- 
          type PostCallPlugin

- 
          type PreCallPlugin

- 
          type RPCClient

- 
          type Receipt

- 
          type SelectFunc

- 
          type SelectMode

- 

  - 
            func SelectModeString(s string) (SelectMode, error)

  - 
            func SelectModeValues() []SelectMode

- 

  - 
            func (i SelectMode) IsASelectMode() bool

  - 
            func (i SelectMode) String() string

- 
          type SelectNodePlugin

- 
          type Selector

- 
          type ServiceDiscovery

- 

  - 
            func CacheDiscovery(threshold int, cachedFile string, discovery ServiceDiscovery) ServiceDiscovery

- 
          type ServiceDiscoveryFilter

- 
          type ServiceError

- 

  - 
            func NewServiceError(s string) ServiceError

- 
          type Weighted

- 
          type XClient

- 

  - 
            func NewBidirectionalXClient(servicePath string, failMode FailMode, selectMode SelectMode, ...) XClient

  - 
            func NewXClient(servicePath string, failMode FailMode, selectMode SelectMode, ...) XClient

- 
          type XClientPool

- 

  - 
            func NewBidirectionalXClientPool(count int, servicePath string, failMode FailMode, selectMode SelectMode, ...) *XClientPool

  - 
            func NewXClientPool(count int, servicePath string, failMode FailMode, selectMode SelectMode, ...) *XClientPool

- 

  - 
            func (c *XClientPool) Auth(auth string)

  - 
            func (p *XClientPool) Close()

  - 
            func (p *XClientPool) Get() XClient

### Constants ¶

  
    
      View Source
      

```
const (
	XVersion           = "X-RPCX-Version"
	XMessageType       = "X-RPCX-MesssageType"
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
	// ReaderBuffsize is used for bufio reader.
	ReaderBuffsize = 16 * 1024
	// WriterBuffsize is used for bufio writer.
	WriterBuffsize = 16 * 1024
)
```

    
  

    
      View Source
      

```
const (
	FileTransferBufferSize = 1024
)
```

    
  

  
### Variables ¶

  
    
      View Source
      

```
var (
	ErrBreakerOpen    = errors.New("breaker open")
	ErrBreakerTimeout = errors.New("breaker time out")
)
```

    
  

    
      View Source
      

```
var (
	ErrShutdown         = errors.New("connection is shut down")
	ErrUnsupportedCodec = errors.New("unsupported codec")
)
```

    
  

ErrShutdown connection is closed.

    
      View Source
      

```
var (
	// ErrXClientShutdown xclient is shutdown.
	ErrXClientShutdown = errors.New("xClient is shut down")
	// ErrXClientNoServer selector can't found one server.
	ErrXClientNoServer = errors.New("can not found any server")
	// ErrServerUnavailable selected server is unavailable.
	ErrServerUnavailable = errors.New("selected server is unavailable")
)
```

    
  

    
      View Source
      

```
var ClientErrorFunc func(res *protocol.Message, e string) ServiceError
```

    
  

ClientErrorFunc is a function to create a customized error.

    
      View Source
      

```
var ConnFactories = make(map[string]ConnFactoryFn)
```

    
  

    
      View Source
      

```
var DefaultOption = Option{
	Retries:             3,
	RPCPath:             share.DefaultRPCPath,
	ConnectTimeout:      time.Second,
	SerializeType:       protocol.MsgPack,
	CompressType:        protocol.None,
	BackupLatency:       10 * time.Millisecond,
	MaxWaitForHeartbeat: 30 * time.Second,
	TCPKeepAlivePeriod:  time.Minute,
	BidirectionalBlock:  false,
	TimeToDisallow:      time.Minute,
}
```

    
  

DefaultOption is a common option configuration for client.

  
### Functions ¶

  
	  
  
  
    
#### 
      func CalculateWeight ¶
  
    
      added in
      v1.6.2
    
  

    
    
      

```
func CalculateWeight(rtt int) int
```

    
  

CalculateWeight converts the rtt to weighted by:

  
- weight=191 if t <= 10
  
- weight=201 -t if 10 < t <=200
  
- weight=1 if 200 < t < 1000
  
- weight = 0 if t >= 1000

It means servers that ping time t < 10 will be preferred
and servers won't be selected if t > 1000.
It is hard coded based on Ops experience.

  

        
	  
  
  
    
#### 
      func Hash ¶
  
    
  

    
    
      

```
func Hash(key uint64, buckets int32) int32
```

    
  

Hash consistently chooses a hash bucket number in the range [0, numBuckets) for the given key. numBuckets must be >= 1.

  

        
	  
  
  
    
#### 
      func HashString ¶
  
    
  

    
    
      

```
func HashString(s string) uint64
```

    
  

HashString get a hash value of a string

  

        
	  
  
  
    
#### 
      func JumpConsistentHash ¶
  
    
  

    
    
      

```
func JumpConsistentHash(len int, options ...interface{}) int
```

    
  

JumpConsistentHash selects a server by serviceMethod and args

  

        
	  
  
  
    
#### 
      func Ping ¶
  
    
      added in
      v1.6.2
    
  

    
    
      

```
func Ping(host string) (rtt int, err error)
```

    
  

Ping gets network traffic by ICMP

  

        
	  
  
  
    
#### 
      func RegisterCacheClientBuilder ¶
  
    
      added in
      v1.6.3
    
  

    
    
      

```
func RegisterCacheClientBuilder(network string, builder CacheClientBuilder)
```