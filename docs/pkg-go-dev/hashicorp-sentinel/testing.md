### Overview ¶

Package testing provides support for automated testing for plugins.

    
### Index ¶

- 
        func Clean()

- 
        func PluginPath(dir string) (string, error)

- 
        func TestPlugin(t testing.T, c TestPluginCase)

- 
        func TestPluginDir(t testing.T, path string, customize func(*TestPluginCase))

- 
          type TestPluginCase

- 

  - 
            func LoadTestPluginCase(t testing.T, path string) TestPluginCase

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Clean ¶
  
    
  

    
    
      

```
func Clean()
```

    
  

Clean cleans any temporary files created. This should always be called
at the end of any set of plugin tests.

  

        
	  
  
  
    
#### 
      func PluginPath ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
func PluginPath(dir string) (string, error)
```

    
  

PluginPath attempts to infer the plugin path based on the GOPATH
environment variable and the directory.

  

        
	  
  
  
    
#### 
      func TestPlugin ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
func TestPlugin(t testing.T, c TestPluginCase)
```

    
  

TestPlugin tests that a sdk.Plugin implementation works as expected.

  

        
	  
  
  
    
#### 
      func TestPluginDir ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
func TestPluginDir(t testing.T, path string, customize func(*TestPluginCase))
```

    
  

TestPluginDir iterates over files in a directory, calls
LoadTestPluginCase on each file suffixed with ".sentinel", and executes all
of the plugin tests.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type TestPluginCase ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
type TestPluginCase struct {
	// Source is a policy to execute. This should be a full program ending
	// in `main = ` and an assignment. For example `main = subject.foo`.
	Source string

	// This is the configuration that will be sent to the plugin. This
	// must serialize to JSON since the JSON will be used to pass the
	// configuration.
	Config map[string]interface{}

	// This is extra data to inject into the global scope of the policy
	// execution
	Global map[string]interface{}

	// Mock is mocked plugin data
	Mock map[string]map[string]interface{}

	// PluginPath is the path to a Go package on your GOPATH containing
	// the plugin to test. If this is blank, the test case uses heuristics
	// to extract the GOPATH and use the current package for testing.
	// This package is expected to expose a "New" function which adheres to
	// the sdk/rpc.PluginFunc signature.
	//
	// This should usually be blank. This maximizes portability of the
	// plugin if it were to be forked or moved.
	//
	// For a given plugin path, the test binary will be built exactly once
	// per test run.
	PluginPath string

	// PluginName allows passing a custom name for the plugin to be used in
	// test cases. By default, the plugin is simply named "subject". The
	// plugin name is what is used within this policy's source to access
	// functionality provided by the plugin.
	PluginName string

	// A string containing any expected runtime error during evaluation. If
	// this field is non-empty, a runtime error is expected to occur, and
	// the Sentinel output is searched for the string given here. If the
	// output contains the string, the test passes. If it does not contain
	// the string, the test will fail.
	//
	// More advanced matches can be done with regular expression patterns.
	// If the Error string is delimited by slashes (/), the string is
	// compiled as a regular expression and the Sentinel output is matched
	// against the resulting pattern. If a match is found, the test passes.
	// If it does not match, the tests will fail.
	Error string
}
```

    
  

TestPluginCase is a single test case for configuring TestPlugin.

    
  
  
    
#### 
      func LoadTestPluginCase ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
func LoadTestPluginCase(t testing.T, path string) TestPluginCase
```

    
  

LoadTestPluginCase is used to load a TestPluginCase from a Sentinel policy
file. Certain test case pragmas are supported in the top-most comment body.
The following is a completely valid example:

```
//config: {"option1": "value1"}
//error: failed to do the thing
main = rule { true }

```

The above would load a TestPlugin case using the specified options. The
config is loaded as a JSON string and unmarshaled into the Config field.
The error field is loaded as a string into the Error field. Pragmas *must*
be at the very top of the file, starting at line one. When a non-pragma
line is encountered, parsing will end and any further pragmas are discarded.

This makes boilerplate very simple for a large number of Sentinel tests,
and allows an entire test to be captured neatly into a single file which
also happens to be the policy being tested.