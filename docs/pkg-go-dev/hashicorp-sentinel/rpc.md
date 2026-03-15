### Overview ¶

Package rpc contains the API that can be used to serve Sentinel
plugins over an RPC interface. Sentinel supports consuming plugins
across RPC with the requirement that the RPC must happen over a completely
reliable network (effectively a local network).

## Object Plugins

Object plugins allow Sentinel values to be served over a plugin interface.
This implements the object.External interface exported by lang/object.

There are limitations to the types of values that can be returned when
this is served over a plugin:

  
- 

All Go primitives and collections that the External interface
allows may be returned, including structs.

  
- 

All primitive and collection Object implementations may be returned.

  
- 

ExternalObj, External may not yet be returned. We plan to allow this.

    
### Index ¶

- Constants

- Variables

- 
        func Serve(opts *ServeOpts)

- 
          type Plugin

- 

  - 
            func (p *Plugin) GRPCClient(_ context.Context, _ *goplugin.GRPCBroker, c *grpc.ClientConn) (interface{}, error)

  - 
            func (p *Plugin) GRPCServer(_ *goplugin.GRPCBroker, s *grpc.Server) error

- 
          type PluginFunc

- 
          type PluginGRPCClient

- 

  - 
            func (m *PluginGRPCClient) Close() error

  - 
            func (m *PluginGRPCClient) Configure(config map[string]interface{}) error

  - 
            func (m *PluginGRPCClient) Get(rawReqs []*sdk.GetReq) ([]*sdk.GetResult, error)

- 
          type PluginGRPCServer

- 

  - 
            func (m *PluginGRPCServer) Close(ctx context.Context, v *proto.Close_Request) (*proto.Empty, error)

  - 
            func (m *PluginGRPCServer) Configure(ctx context.Context, v *proto.Configure_Request) (*proto.Configure_Response, error)

  - 
            func (m *PluginGRPCServer) Get(ctx context.Context, v *proto.Get_MultiRequest) (*proto.Get_MultiResponse, error)

- 
          type ServeOpts

### Constants ¶

  
    
      View Source
      

```
const (
	PluginName = "import"
)
```

    
  

The constants below are the names of the plugins that can be dispensed
from the plugin server.

  
### Variables ¶

  
    
      View Source
      

```
var Handshake = goplugin.HandshakeConfig{

	ProtocolVersion: 3,

	MagicCookieKey:   "SENTINEL_PLUGIN_MAGIC_COOKIE",
	MagicCookieValue: "2b7847b7b705781d7cf21a05e9c1bb37cbf078aea103bc3edcc6aca52ab65453",
}
```

    
  

Handshake is the HandshakeConfig used to configure clients and servers.

    
      View Source
      

```
var PluginMap = map[string]goplugin.Plugin{
	PluginName: &Plugin{},
}
```

    
  

PluginMap should be used by clients for the map of plugins.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Serve ¶
  
    
  

    
    
      

```
func Serve(opts *ServeOpts)
```

    
  

Serve serves a plugin. This function never returns and should be the final
function called in the main function of the plugin.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type Plugin ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
type Plugin struct {
	goplugin.NetRPCUnsupportedPlugin

	F func() sdk.Plugin
}
```

    
  

Plugin is the goplugin.Plugin implementation to serve sdk.Plugin.

    
  
  
    
#### 
      func (*Plugin) GRPCClient ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
func (p *Plugin) GRPCClient(_ context.Context, _ *goplugin.GRPCBroker, c *grpc.ClientConn) (interface{}, error)
```