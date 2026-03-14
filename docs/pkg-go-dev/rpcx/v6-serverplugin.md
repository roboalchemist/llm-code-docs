### Index ¶

- Variables

- 
        func InfluxDB(r metrics.Registry, d time.Duration, url, database, username, password string)

- 
        func InfluxDBWithTags(r metrics.Registry, d time.Duration, url, database, username, password string, ...)

- 
          type AliasPlugin

- 

  - 
            func NewAliasPlugin() *AliasPlugin

- 

  - 
            func (p *AliasPlugin) Alias(aliasServicePath, aliasServiceMethod string, servicePath, serviceMethod string)

  - 
            func (p *AliasPlugin) PostReadRequest(ctx context.Context, r *protocol.Message, e error) error

  - 
            func (p *AliasPlugin) PreWriteResponse(ctx context.Context, r *protocol.Message, res *protocol.Message) error

- 
          type BlacklistPlugin

- 

  - 
            func (plugin *BlacklistPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

- 
          type ConsulRegisterPlugin

- 

  - 
            func (p *ConsulRegisterPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

  - 
            func (p *ConsulRegisterPlugin) PreCall(_ context.Context, _, _ string, args interface{}) (interface{}, error)

  - 
            func (p *ConsulRegisterPlugin) Register(name string, rcvr interface{}, metadata string) (err error)

  - 
            func (p *ConsulRegisterPlugin) RegisterFunction(serviceName, fname string, fn interface{}, metadata string) error

  - 
            func (p *ConsulRegisterPlugin) Start() error

  - 
            func (p *ConsulRegisterPlugin) Stop() error

  - 
            func (p *ConsulRegisterPlugin) Unregister(name string) (err error)

- 
          type MDNSRegisterPlugin

- 

  - 
            func NewMDNSRegisterPlugin(serviceAddress string, port int, m metrics.Registry, ...) *MDNSRegisterPlugin

- 

  - 
            func (p *MDNSRegisterPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

  - 
            func (p *MDNSRegisterPlugin) PreCall(_ context.Context, _, _ string, args interface{}) (interface{}, error)

  - 
            func (p *MDNSRegisterPlugin) Register(name string, rcvr interface{}, metadata string) (err error)

  - 
            func (p *MDNSRegisterPlugin) RegisterFunction(serviceName, fname string, fn interface{}, metadata string) error

  - 
            func (p *MDNSRegisterPlugin) Start() error

  - 
            func (p *MDNSRegisterPlugin) Stop() error

  - 
            func (p *MDNSRegisterPlugin) Unregister(name string) (err error)

- 
          type MetricsPlugin

- 

  - 
            func NewMetricsPlugin(registry metrics.Registry) *MetricsPlugin

- 

  - 
            func (p *MetricsPlugin) Exp()

  - 
            func (p *MetricsPlugin) Graphite(freq time.Duration, prefix string, addr *net.TCPAddr)

  - 
            func (p *MetricsPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

  - 
            func (p *MetricsPlugin) InfluxDB(freq time.Duration, url, database, username, password string)

  - 
            func (p *MetricsPlugin) InfluxDBWithTags(freq time.Duration, url, database, username, password string, ...)

  - 
            func (p *MetricsPlugin) Log(freq time.Duration, l metrics.Logger)

  - 
            func (p *MetricsPlugin) PostReadRequest(ctx context.Context, r *protocol.Message, e error) error

  - 
            func (p *MetricsPlugin) PostWriteResponse(ctx context.Context, req *protocol.Message, res *protocol.Message, e error) error

  - 
            func (p *MetricsPlugin) PreReadRequest(ctx context.Context) error

  - 
            func (p *MetricsPlugin) Register(name string, rcvr interface{}, metadata string) error

- 
          type NacosRegisterPlugin

- 

  - 
            func (p *NacosRegisterPlugin) Register(name string, rcvr interface{}, metadata string) (err error)

  - 
            func (p *NacosRegisterPlugin) RegisterFunction(serviceName, fname string, fn interface{}, metadata string) error

  - 
            func (p *NacosRegisterPlugin) Start() error

  - 
            func (p *NacosRegisterPlugin) Stop() error

  - 
            func (p *NacosRegisterPlugin) Unregister(name string) (err error)

- 
          type OpenCensusPlugin

- 

  - 
            func (p OpenCensusPlugin) PostConnAccept(conn net.Conn) (net.Conn, bool)

  - 
            func (p OpenCensusPlugin) PostWriteResponse(ctx context.Context, req *protocol.Message, res *protocol.Message, err error) error

  - 
            func (p OpenCensusPlugin) PreHandleRequest(ctx context.Context, r *protocol.Message) error

  - 
            func (p OpenCensusPlugin) Register(name string, rcvr interface{}, metadata string) error

  - 
            func (p OpenCensusPlugin) RegisterFunction(serviceName, fname string, fn interface{}, metadata string) error

- 
          type OpenTracingPlugin

- 

  - 
            func (p OpenTracingPlugin) PostConnAccept(conn net.Conn) (net.Conn, bool)

  - 
            func (p OpenTracingPlugin) PostWriteResponse(ctx context.Context, req *protocol.Message, res *protocol.Message, err error) error

  - 
            func (p OpenTracingPlugin) PreHandleRequest(ctx context.Context, r *protocol.Message) error

  - 
            func (p OpenTracingPlugin) Register(name string, rcvr interface{}, metadata string) error

  - 
            func (p OpenTracingPlugin) RegisterFunction(serviceName, fname string, fn interface{}, metadata string) error

- 
          type RateLimitingPlugin

- 

  - 
            func NewRateLimitingPlugin(fillInterval time.Duration, capacity int64) *RateLimitingPlugin

- 

  - 
            func (plugin *RateLimitingPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

- 
          type RedisRegisterPlugin

- 

  - 
            func (p *RedisRegisterPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

  - 
            func (p *RedisRegisterPlugin) PreCall(_ context.Context, _, _ string, args interface{}) (interface{}, error)

  - 
            func (p *RedisRegisterPlugin) Register(name string, rcvr interface{}, metadata string) (err error)

  - 
            func (p *RedisRegisterPlugin) Start() error

  - 
            func (p *RedisRegisterPlugin) Stop() error

  - 
            func (p *RedisRegisterPlugin) Unregister(name string) (err error)

- 
          type ReqRateLimitingPlugin

- 

  - 
            func NewReqRateLimitingPlugin(fillInterval time.Duration, capacity int64, block bool) *ReqRateLimitingPlugin

- 

  - 
            func (plugin *ReqRateLimitingPlugin) PreReadRequest(ctx context.Context) error

- 
          type TeeConnPlugin

- 

  - 
            func NewTeeConnPlugin(w io.Writer) *TeeConnPlugin

- 

  - 
            func (plugin *TeeConnPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

  - 
            func (plugin *TeeConnPlugin) Update(w io.Writer)

- 
          type WhitelistPlugin

- 

  - 
            func (plugin *WhitelistPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

- 
          type ZooKeeperRegisterPlugin

- 

  - 
            func (p *ZooKeeperRegisterPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

  - 
            func (p *ZooKeeperRegisterPlugin) PreCall(_ context.Context, _, _ string, args interface{}) (interface{}, error)

  - 
            func (p *ZooKeeperRegisterPlugin) Register(name string, rcvr interface{}, metadata string) (err error)

  - 
            func (p *ZooKeeperRegisterPlugin) RegisterFunction(serviceName, fname string, fn interface{}, metadata string) error

  - 
            func (p *ZooKeeperRegisterPlugin) Start() error

  - 
            func (p *ZooKeeperRegisterPlugin) Stop() error

  - 
            func (p *ZooKeeperRegisterPlugin) Unregister(name string) (err error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  
    
      View Source
      

```
var ErrReqReachLimit = errors.New("request reached rate limit")
```

    
  

  
### Functions ¶

  
	  
  
  
    
#### 
      func InfluxDB ¶
  
    
  

    
    
      

```
func InfluxDB(r metrics.Registry, d time.Duration, url, database, username, password string)
```

    
  

InfluxDB starts a InfluxDB reporter which will post the metrics from the given registry at each d interval.

  

        
	  
  
  
    
#### 
      func InfluxDBWithTags ¶
  
    
  

    
    
      

```
func InfluxDBWithTags(r metrics.Registry, d time.Duration, url, database, username, password string, tags map[string]string)
```

    
  

InfluxDBWithTags starts a InfluxDB reporter which will post the metrics from the given registry at each d interval with the specified tags

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type AliasPlugin ¶
  
    
  

    
    
      

```
type AliasPlugin struct {
	Aliases          map[string]*aliasPair
	ReseverseAliases map[string]*aliasPair
}
```

    
  

AliasPlugin can be used to set aliases for services

    
  
  
    
#### 
      func NewAliasPlugin ¶
  
    
  

    
    
      

```
func NewAliasPlugin() *AliasPlugin
```

    
  

NewAliasPlugin creates a new NewAliasPlugin

  

  
    
  
  
    
#### 
      func (*AliasPlugin) Alias ¶
  
    
  

    
    
      

```
func (p *AliasPlugin) Alias(aliasServicePath, aliasServiceMethod string, servicePath, serviceMethod string)
```

    
  

Alias sets a alias for the serviceMethod.
For example Alias("anewpath&method", "Arith.mul")

  

  
    
  
  
    
#### 
      func (*AliasPlugin) PostReadRequest ¶
  
    
  

    
    
      

```
func (p *AliasPlugin) PostReadRequest(ctx context.Context, r *protocol.Message, e error) error
```

    
  

PostReadRequest converts the alias of this service.

  

  
    
  
  
    
#### 
      func (*AliasPlugin) PreWriteResponse ¶
  
    
  

    
    
      

```
func (p *AliasPlugin) PreWriteResponse(ctx context.Context, r *protocol.Message, res *protocol.Message) error
```

    
  

PreWriteResponse restore servicePath and serviceMethod.