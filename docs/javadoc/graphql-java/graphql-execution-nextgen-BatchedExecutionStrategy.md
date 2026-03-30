JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

graphql.execution.nextgen

## Class BatchedExecutionStrategy

- java.lang.Object

- 

  - graphql.execution.nextgen.BatchedExecutionStrategy

- 

All Implemented Interfaces:
ExecutionStrategy

---

```
public class BatchedExecutionStrategy
extends java.lang.Object
implements ExecutionStrategy
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`BatchedExecutionStrategy()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`java.util.concurrent.CompletableFuture<ExecutionResult>`
`execute(ExecutionContext context)` 

`java.util.concurrent.CompletableFuture<RootExecutionResultNode>`
`executeImpl(ExecutionContext executionContext,
           FieldSubSelection fieldSubSelection)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BatchedExecutionStrategy

```
public BatchedExecutionStrategy()
```

  - 

### Method Detail

    - 

#### execute

```
public java.util.concurrent.CompletableFuture<ExecutionResult> execute(ExecutionContext context)
```

Specified by:
`execute` in interface `ExecutionStrategy`

    - 

#### executeImpl

```
public java.util.concurrent.CompletableFuture<RootExecutionResultNode> executeImpl(ExecutionContext executionContext,
                                                                                   FieldSubSelection fieldSubSelection)
```

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method