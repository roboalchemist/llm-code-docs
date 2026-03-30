### Overview ¶

Package daemon implements a service for mediating access to the data store,
and its client.

Most RPCs exposed by the service correspond to the methods of Store in the
store package and are not documented here.

### Index ¶

- Constants

- Variables

-
        func Serve(sockpath, dbpath string)

-
        func Spawn(cfg *SpawnConfig) error

-
          type Client

-

-
            func NewClient(sockPath string) Client

-
          type SpawnConfig

### Constants ¶

      View Source
      

```
const Version = -93
```

Version is the API version. It should be bumped any time the API changes.

### Variables ¶

      View Source
      

```
var (
 // ErrDaemonUnreachable is returned when the daemon cannot be reached after
 // several retries.
 ErrDaemonUnreachable = errors.New("daemon offline")
)
```

      View Source
      

```
var Program prog.Program = program{}
```

Program is the daemon subprogram.

### Functions ¶

####

      func Serve ¶
  
    
  

    
    
      

```
func Serve(sockpath, dbpath string)
```

Serve runs the daemon service, listening on the socket specified by sockpath
and serving data from dbpath. It quits upon receiving SIGTERM, SIGINT or when
all active clients have disconnected.

####

      func Spawn ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func Spawn(cfg *SpawnConfig) error
```

Spawn spawns a daemon process in the background by invoking BinPath, passing
BinPath, DbPath and SockPath as command-line arguments after resolving them
to absolute paths. The daemon log file is created in RunDir, and the stdout
and stderr of the daemon is redirected to the log file.

A suitable ProcAttr is chosen depending on the OS and makes sure that the
daemon is detached from the current terminal, so that it is not affected by
I/O or signals in the current terminal and keeps running after the current
process quits.

### Types ¶

####

      type Client ¶
  
    
  

    
    
      

```
type Client interface {
 store.Store

 ResetConn() error
 Close() error

 Pid() (int, error)
 SockPath() string
 Version() (int, error)
}
```

Client represents a daemon client.

####

      func NewClient ¶
  
    
  

    
    
      

```
func NewClient(sockPath string) Client
```

NewClient creates a new Client instance that talks to the socket. Connection
creation is deferred to the first request.
