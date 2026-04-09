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

graphql.execution.reactive

## Class CompletionStageMappingPublisher<D,U>

- java.lang.Object

- 

  - graphql.execution.reactive.CompletionStageMappingPublisher<D,U>

- 

Type Parameters:
`D` - the down stream type
`U` - the up stream type to be mapped to

All Implemented Interfaces:
org.reactivestreams.Publisher<D>

---

```
public class CompletionStageMappingPublisher<D,U>
extends java.lang.Object
implements org.reactivestreams.Publisher<D>
```

A reactive Publisher that bridges over another Publisher of `D` and maps the results
 to type `U` via a CompletionStage, handling errors in that stage

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`CompletionStageMappingPublisher(org.reactivestreams.Publisher<U> upstreamPublisher,
                               java.util.function.Function<U,java.util.concurrent.CompletionStage<D>> mapper)`
You need the following :

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`void`
`subscribe(org.reactivestreams.Subscriber<? super D> downstreamSubscriber)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### CompletionStageMappingPublisher

```
public CompletionStageMappingPublisher(org.reactivestreams.Publisher<U> upstreamPublisher,
                                       java.util.function.Function<U,java.util.concurrent.CompletionStage<D>> mapper)
```

You need the following :

Parameters:
`upstreamPublisher` - an upstream source of data
`mapper` - a mapper function that turns upstream data into a promise of mapped D downstream data

  - 

### Method Detail

    - 

#### subscribe

```
public void subscribe(org.reactivestreams.Subscriber<? super D> downstreamSubscriber)
```

Specified by:
`subscribe` in interface `org.reactivestreams.Publisher<D>`

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