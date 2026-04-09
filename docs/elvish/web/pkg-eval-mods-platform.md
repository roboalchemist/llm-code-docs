### Overview ¶

Package platform exposes variables and functions that deal with the
specific platform being run on, such as the OS name and CPU architecture.

### Index ¶

- Variables

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var Ns = eval.NsBuilder{
 "arch":       vars.NewReadOnly(runtime.GOARCH),
 "os":         vars.NewReadOnly(runtime.GOOS),
 "is-unix":    vars.NewReadOnly(isUnix),
 "is-windows": vars.NewReadOnly(isWindows),
}.AddGoFns("platform:", map[string]interface{}{
 "hostname": hostname,
}).Ns()
```

### Functions ¶

This section is empty.

### Types ¶

This section is empty.
