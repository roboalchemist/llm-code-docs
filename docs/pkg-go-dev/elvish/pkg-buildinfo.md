### Overview ¶

Package buildinfo contains build information.

Build information should be set during compilation by passing
-ldflags "-X github.com/elves/elvish/pkg/buildinfo.Var=value" to "go build" or
"go get".

### Index ¶

- Variables

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var (
 Version      = "unknown"
 Reproducible = "false"
)
```

Build information.

      View Source
      

```
var Program prog.Program = program{}
```

Program is the buildinfo subprogram.

### Functions ¶

This section is empty.

### Types ¶

This section is empty.
