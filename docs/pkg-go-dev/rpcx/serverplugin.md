### Index ¶

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
          type RateLimitingPlugin

- 

  - 
            func NewRateLimitingPlugin(fillInterval time.Duration, capacity int64) *RateLimitingPlugin

- 

  - 
            func (plugin *RateLimitingPlugin) HandleConnAccept(conn net.Conn) (net.Conn, bool)

- 
          type RedisRateLimitingPlugin

- 

  - 
            func NewRedisRateLimitingPlugin(addrs []string, rate int, burst int, period time.Duration) *RedisRateLimitingPlugin

- 

  - 
            func (plugin *RedisRateLimitingPlugin) PostReadRequest(ctx context.Context, r *protocol.Message, e error) error

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
            func (plugin *ReqRateLimitingPlugin) PostReadRequest(ctx context.Context, r *protocol.Message, e error) error

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

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
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