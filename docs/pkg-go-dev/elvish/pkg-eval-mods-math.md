### Overview ¶

Package math exposes functionality from Go's math package as an elvish
module.

### Index ¶

- Variables

### Constants ¶

This section is empty.

### Variables ¶

      View Source
      

```
var Ns = eval.NsBuilder{
 "e":  vars.NewReadOnly(math.E),
 "pi": vars.NewReadOnly(math.Pi),
}.AddGoFns("math:", fns).Ns()
```

Ns is the namespace for the math: module.

### Functions ¶

This section is empty.

### Types ¶

This section is empty.
