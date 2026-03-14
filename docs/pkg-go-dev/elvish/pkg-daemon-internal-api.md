### Overview ¶

Package api defines types and constants useful for the API between the daemon
service and client.

### Index ¶

- Constants

-
          type AddCmdRequest

-
          type AddCmdResponse

-
          type AddDirRequest

-
          type AddDirResponse

-
          type CmdRequest

-
          type CmdResponse

-
          type CmdsRequest

-
          type CmdsResponse

-
          type CmdsWithSeqRequest

-
          type CmdsWithSeqResponse

-
          type DelCmdRequest

-
          type DelCmdResponse

-
          type DelDirRequest

-
          type DelDirResponse

-
          type DelSharedVarRequest

-
          type DelSharedVarResponse

-
          type DirsRequest

-
          type DirsResponse

-
          type NextCmdRequest

-
          type NextCmdResponse

-
          type NextCmdSeqRequest

-
          type NextCmdSeqResponse

-
          type PidRequest

-
          type PidResponse

-
          type PrevCmdRequest

-
          type PrevCmdResponse

-
          type SetSharedVarRequest

-
          type SetSharedVarResponse

-
          type SharedVarRequest

-
          type SharedVarResponse

-
          type VersionRequest

-
          type VersionResponse

### Constants ¶

      View Source
      

```
const ServiceName = "Daemon"
```

ServiceName is the name of the RPC service exposed by the daemon.

### Variables ¶

This section is empty.

### Functions ¶

This section is empty.

### Types ¶

####

      type AddCmdRequest ¶
  
    
  

    
    
      

```
type AddCmdRequest struct {
 Text string
}
```
