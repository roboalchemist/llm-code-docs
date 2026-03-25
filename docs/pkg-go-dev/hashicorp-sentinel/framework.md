### Overview ¶

Package framework contains a high-level framework for implementing
Sentinel plugins with Go.

The direct sdk.Plugin interface is a low-level interface that is
tediuos, clunky, and difficult to implement correctly. The
interface is this way to assist in the performance of plugins
while executing Sentinel policies. This package provides a
high-level API that eases plugin implementation while still
supporting the performance-sensitive interface underneath.

Plugins are generally activated in this framework by serving the
plugin with the root namespace embedded in Plugin:

```
package main

import (
    "github.com/hashicorp/sentinel-sdk"
    "github.com/hashicorp/sentinel-sdk/rpc"
)

func main() {
    rpc.Serve(&rpc.ServeOpts{
        PluginFunc: func() sdk.Plugin {
            return &framework.Plugin{Root: &root{}}
        },
    })
}

```

The plugin framework is based around the concept of namespaces.
Root is the entrypoint namespace and must be implemented as a
minimum. From there, nested access may be delegated to other
Namespace implementations.

Namespaces outside of the root must at least implement the
Namespace interface. All namespaces, including the root, may
implement the optional Call or Map interfaces, to support function
calls or selective memoization calls, respectively.

Root namespaces are generally global, that is, for the lifetime of
the execution of Sentinel, one single plugin Root namespace state
will be shared by all policies that need to be executed. Take care
when storing state in the Root namespace. If you require state
in the Root namespace that must be unique across policy
executions, implement the NamespaceCreator interface.

The Root namespace (or the NamespaceCreator interface, which
embeds Root) may optionally implement the New interface, which
allows for the construction of namespaces via the handling of
arbitrary object data. New is ignored for namespaces past the
root.

Non-primitive plugin return data is normally memoized, including
for namespaces. This prevents expensive calls over the plugin RPC.
Memoization can be controlled by a couple of methods:

* Implementing the Map interface allows for the explicit return of
a map of values, sidestepping struct memoization. Normally, this
is combined with the MapFromKeys function which will call Get for
each defined key and add the return values to the map. Note that
multi-key plugin calls always bypass memoization - so if foo.bar
is a namespace that implements Map but foo.bar.baz is looked up in
a single expression, it does not matter if baz is excluded from
Map.

* Struct memoization is implicit otherwise. Only exported fields
are acted on - fields are lower and snake cased where applicable.
To control this behavior, you can use the "sentinel" struct tag.
sentinel:"NAME" will alter the field to have the name indicated by
NAME, while an empty string will exclude the field.

Additionally, there are a couple of nuances that the plugin author
should be cognizant of:

* nil values within slices, maps, and structs are converted to
nulls in the return object.

* Returning a nil from a Get call is undefined, not null.

The author can alter this behavior explicitly by assigning or
returning the sdk.Null and sdk.Undefined values.

    
### Index ¶

- 
        func MapFromKeys(ns Namespace, keys []string) (map[string]interface{}, error)

- 
          type Call

- 
          type List

- 
          type Map

- 
          type Namespace

- 
          type NamespaceCreator

- 
          type New

- 
          type Plugin

- 

  - 
            func (m *Plugin) Configure(raw map[string]interface{}) error

  - 
            func (m *Plugin) Get(reqs []*sdk.GetReq) ([]*sdk.GetResult, error)

- 
          type Root

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func MapFromKeys ¶
  
    
  

    
    
      

```
func MapFromKeys(ns Namespace, keys []string) (map[string]interface{}, error)
```

    
  

MapFromKeys creates a map[string]interface{} for a Namespace from the
given set of keys. This is a useful helper for implementing the Map
interface.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type Call ¶
  
    
  

    
    
      

```
type Call interface {
	Namespace

	// Func returns a function to call for the given string. The function
	// must take some number of arguments and return (interface{}, error).
	// The argument types may be Go types and the framework will handle
	// conversion and validation automatically.
	//
	// The returned function may also return only interface{}. In this case,
	// it is assumed an error scenario is impossible. Any other number of
	// return values will result in an error.
	//
	// This should return nil if the key doesn't support being called.
	Func(string) interface{}
}
```

    
  

Call is a Namespace that supports call expressions. For example, "time.now()"
would invoke the Func function for "now".

  

    
      
  
  
    
#### 
      type List ¶
  
    
      added in
      v0.5.0
    
  

    
    
      

```
type List interface {
	Namespace

	List() ([]interface{}, error)
}
```

    
  

List is a Namespace that supports returning a list of data.

  

    
      
  
  
    
#### 
      type Map ¶
  
    
  

    
    
      

```
type Map interface {
	Namespace

	// Map returns the entire map for this value. The return value
	// must only contain values convertable by lang/object.ToObject. It
	// cannot contain functions or other framework interface implementations.
	Map() (map[string]interface{}, error)
}
```

    
  

Map is a Namespace that supports returning the entire map of data.
For example, if "time.pst" implemented this, then the writer of a policy
may request "time.pst" and get the entire value back as a map.

  

    
      
  
  
    
#### 
      type Namespace ¶
  
    
  

    
    
      

```
type Namespace interface {
	// Get requests the value for a specific key. This must return a value
	// convertable by lang/object.ToObject or another Interface value.
	//
	// If the value doesn't exist, nil should be returned. This will turn
	// into "undefined" eventually in the Sentinel policy. If you want to
	// return an explicit "null" value, please return object.Null directly.
	//
	// If an Interface implementation is returned, this is treated like
	// a namespace. For example, "time.pst" may return an Interface since
	// the value itself expects further keys such as ".hour".
	Get(string) (interface{}, error)
}
```

    
  

Namespace represents a namespace of attributes that can be requested
by key. For example in "time.pst.hour, time.pst.minute", "time.pst" would
be a namespace.

Namespaces are either represented or returned by the Root implementation.
Root is the top-level implementation for a plugin. See Plugin and Root
for more details.

A Namespace on its own doesn't allow accessing the full mapping of
keys and values. Map may be optionally implemented to support this.
Following the example in the first paragraph of this documentation,
"time.pst" itself wouldn't be allowed for a Namespace on its own. If
the implementation also implements Map, then "time.pst" would return
a complete mapping.

  

    
      
  
  
    
#### 
      type NamespaceCreator ¶
  
    
  

    
    
      

```
type NamespaceCreator interface {
	Root

	// Namespace is called to return the root namespace for accessing keys.
	//
	// This will be called once for each policy execution. If data and access
	// is shared by all policy executions (such as static data), then you
	// can return a singleton value.
	//
	// If each policy execution should maintain its own state, then this
	// should return a new value.
	Namespace() Namespace
}
```

    
  

NamespaceCreator is an interface only used in conjunction with the
Root interface. It allows the Root implementation to create a unique
Namespace implementation for each policy execution.

This is useful for plugins that maintain state per policy execution.
For example for the "time" package, it may be useful for the state to
be the current time so that all access returns a singular view of time
for a policy execution.

If your plugin doesn't require per-execution state, Root should
implement Namespace directly instead.

  

    
      
  
  
    
#### 
      type New ¶
  
    
      added in
      v0.3.0
    
  

    
    
      

```
type New interface {
	Namespace

	// New is called to construct new namespaces based on arbitrary
	// receiver data.
	//
	// The format of the object and the kinds of namespaces returned by
	// the constructor are up to the plugin author.
	//
	// Namespaces returned by this function must implement
	// framework.Map, or else errors will be returned on
	// post-processing of the receiver.
	//
	// New should return an error if there are issues instantiating the
	// namespace. This includes if the namespace cannot be determined
	// from the receiver data. Returning nil from this function will
	// return undefined to the caller.
	New(map[string]interface{}) (Namespace, error)
}
```

    
  

New is an interface indicating that the namespace supports object
construction via the handling of arbitrary object data. New is
only supported on root namespaces, so either created through
Root or NamespaceCreator.

The format of the object and the kinds of namespaces returned by
the constructor are up to the plugin author.

  

    
      
  
  
    
#### 
      type Plugin ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
type Plugin struct {
	// Root is the implementation of the plugin that the user of the
	// framework should implement. It represents the minimum necessary
	// implementation for a plugin. See the docs for Root for more details.
	Root Root
	// contains filtered or unexported fields
}
```

    
  

Plugin implements sdk.Plugin. Configure and return this structure
to simplify implementation of sdk.Plugin.

    
  
  
    
#### 
      func (*Plugin) Configure ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
func (m *Plugin) Configure(raw map[string]interface{}) error
```

    
  

plugin.Plugin impl.

  

  
    
  
  
    
#### 
      func (*Plugin) Get ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
func (m *Plugin) Get(reqs []*sdk.GetReq) ([]*sdk.GetResult, error)
```

    
  

plugin.Plugin impl.