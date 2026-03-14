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
          type Breaker

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
            func (c *Client) Connect(network, address string) error

  - 
            func (client *Client) Go(ctx context.Context, servicePath, serviceMethod string, args interface{}, ...) *Call

  - 
            func (client *Client) IsClosing() bool

  - 
            func (client *Client) IsShutdown() bool

  - 
            func (client *Client) RegisterServerMessageChan(ch chan<- *protocol.Message)

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
          type ConsulDiscovery

- 

  - 
            func (d *ConsulDiscovery) Clone(servicePath string) (ServiceDiscovery, error)

  - 
            func (d *ConsulDiscovery) Close()

  - 
            func (d *ConsulDiscovery) GetServices() []*KVPair

  - 
            func (d *ConsulDiscovery) RemoveWatcher(ch chan []*KVPair)

  - 
            func (d *ConsulDiscovery) SetFilter(filter ServiceDiscoveryFilter)

  - 
            func (d *ConsulDiscovery) WatchService() chan []*KVPair

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
          type NacosDiscovery

- 

  - 
            func (d *NacosDiscovery) Clone(servicePath string) (ServiceDiscovery, error)

  - 
            func (d *NacosDiscovery) Close()

  - 
            func (d *NacosDiscovery) GetServices() []*KVPair

  - 
            func (d *NacosDiscovery) RemoveWatcher(ch chan []*KVPair)

  - 
            func (d *NacosDiscovery) SetFilter(filter ServiceDiscoveryFilter)

  - 
            func (d *NacosDiscovery) WatchService() chan []*KVPair

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
          type OneClientPool

- 

  - 
            func NewBidirectionalOneClientPool(count int, failMode FailMode, selectMode SelectMode, ...) *OneClientPool

  - 
            func NewOneClientPool(count int, failMode FailMode, selectMode SelectMode, ...) *OneClientPool

- 

  - 
            func (c *OneClientPool) Auth(auth string)

  - 
            func (p OneClientPool) Close()

  - 
            func (p *OneClientPool) Get() *OneClient

- 
          type OpenCensusPlugin

- 

  - 
            func (p *OpenCensusPlugin) PostCall(ctx context.Context, servicePath, serviceMethod string, args interface{}, ...) error

  - 
            func (p *OpenCensusPlugin) PreCall(ctx context.Context, servicePath, serviceMethod string, args interface{}) error

- 
          type OpenTracingPlugin

- 

  - 
            func (p *OpenTracingPlugin) PostCall(ctx context.Context, servicePath, serviceMethod string, args interface{}, ...) error

  - 
            func (p *OpenTracingPlugin) PreCall(ctx context.Context, servicePath, serviceMethod string, args interface{}) error

- 
          type Option

- 
          type Peer2PeerDiscovery

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
          type RedisDiscovery

- 

  - 
            func (d *RedisDiscovery) Clone(servicePath string) (ServiceDiscovery, error)

  - 
            func (d *RedisDiscovery) Close()

  - 
            func (d *RedisDiscovery) GetServices() []*KVPair

  - 
            func (d *RedisDiscovery) RemoveWatcher(ch chan []*KVPair)

  - 
            func (d *RedisDiscovery) SetFilter(filter ServiceDiscoveryFilter)

  - 
            func (d *RedisDiscovery) WatchService() chan []*KVPair

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
            func NewConsulDiscovery(basePath, servicePath string, consulAddr []string, options *store.Config) (ServiceDiscovery, error)

  - 
            func NewConsulDiscoveryStore(basePath string, kv store.Store) (ServiceDiscovery, error)

  - 
            func NewConsulDiscoveryTemplate(basePath string, consulAddr []string, options *store.Config) (ServiceDiscovery, error)

  - 
            func NewMDNSDiscovery(service string, timeout time.Duration, watchInterval time.Duration, ...) (ServiceDiscovery, error)

  - 
            func NewMDNSDiscoveryTemplate(timeout time.Duration, watchInterval time.Duration, domain string) (ServiceDiscovery, error)

  - 
            func NewMultipleServersDiscovery(pairs []*KVPair) (ServiceDiscovery, error)

  - 
            func NewMultipleServersDiscoveryTemplate(pairs []*KVPair) (ServiceDiscovery, error)

  - 
            func NewNacosDiscovery(servicePath string, cluster string, clientConfig constant.ClientConfig, ...) (ServiceDiscovery, error)

  - 
            func NewNacosDiscoveryTemplate(cluster string, clientConfig constant.ClientConfig, ...) ServiceDiscovery

  - 
            func NewNacosDiscoveryWithClient(servicePath string, cluster string, namingClient naming_client.INamingClient) ServiceDiscovery

  - 
            func NewPeer2PeerDiscovery(server, metadata string) (ServiceDiscovery, error)

  - 
            func NewRedisDiscovery(basePath string, servicePath string, etcdAddr []string, options *store.Config) (ServiceDiscovery, error)

  - 
            func NewRedisDiscoveryStore(basePath string, kv store.Store) (ServiceDiscovery, error)

  - 
            func NewRedisDiscoveryTemplate(basePath string, etcdAddr []string, options *store.Config) (ServiceDiscovery, error)

  - 
            func NewZookeeperDiscovery(basePath string, servicePath string, zkAddr []string, options *store.Config) (ServiceDiscovery, error)

  - 
            func NewZookeeperDiscoveryTemplate(basePath string, zkAddr []string, options *store.Config) (ServiceDiscovery, error)

  - 
            func NewZookeeperDiscoveryWithStore(basePath string, kv store.Store) (ServiceDiscovery, error)

- 
          type ServiceDiscoveryFilter

- 
          type ServiceError

- 

  - 
            func (e ServiceError) Error() string

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

- 
          type ZookeeperDiscovery

- 

  - 
            func (d *ZookeeperDiscovery) Clone(servicePath string) (ServiceDiscovery, error)

  - 
            func (d *ZookeeperDiscovery) Close()

  - 
            func (d *ZookeeperDiscovery) GetServices() []*KVPair

  - 
            func (d *ZookeeperDiscovery) RemoveWatcher(ch chan []*KVPair)

  - 
            func (d *ZookeeperDiscovery) SetFilter(filter ServiceDiscoveryFilter)

  - 
            func (d *ZookeeperDiscovery) WatchService() chan []*KVPair

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
	ErrServerUnavailable = errors.New("selected server is unavilable")
)
```

    
  

    
      View Source
      

```
var ConnFactories = map[string]ConnFactoryFn{
	"http": newDirectHTTPConn,
	"kcp":  newDirectKCPConn,
	"quic": newDirectQuicConn,
	"unix": newDirectConn,
}
```

    
  

    
      View Source
      

```
var DefaultOption = Option{
	Retries:             3,
	RPCPath:             share.DefaultRPCPath,
	ConnectTimeout:      10 * time.Second,
	SerializeType:       protocol.MsgPack,
	CompressType:        protocol.None,
	BackupLatency:       10 * time.Millisecond,
	MaxWaitForHeartbeat: 30 * time.Second,
	TCPKeepAlivePeriod:  time.Minute,
}
```

    
  

DefaultOption is a common option configuration for client.

  
### Functions ¶

  
	  
  
  
    
#### 
      func CalculateWeight ¶
  
    
  

    
    
      

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
  
    
  

    
    
      

```
func Ping(host string) (rtt int, err error)
```

    
  

Ping gets network traffic by ICMP

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type Breaker ¶
  
    
  

    
    
      

```
type Breaker interface {
	Call(func() error, time.Duration) error
	Fail()
	Success()
	Ready() bool
}
```

    
  

Breaker is a CircuitBreaker interface.

    
      

```
var CircuitBreaker Breaker = circuit.NewRateBreaker(0.95, 100)
```

    
  

CircuitBreaker is a default circuit breaker (RateBreaker(0.95, 100)).