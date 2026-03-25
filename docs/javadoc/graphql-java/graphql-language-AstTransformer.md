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

graphql.language

## Class AstTransformer

- java.lang.Object

- 

  - graphql.language.AstTransformer

- 

---

```
@PublicApi
public class AstTransformer
extends java.lang.Object
```

Allows for an easy way to "manipulate" the immutable Ast by changing specific nodes and getting back a new Ast
 containing the changed nodes while everything else is the same.

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AstTransformer()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Node`
`transform(Node root,
         NodeVisitor nodeVisitor)` 

`Node`
`transformParallel(Node root,
                 NodeVisitor nodeVisitor)` 

`Node`
`transformParallel(Node root,
                 NodeVisitor nodeVisitor,
                 java.util.concurrent.ForkJoinPool forkJoinPool)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AstTransformer

```
public AstTransformer()
```

  - 

### Method Detail

    - 

#### transform

```
public Node transform(Node root,
                      NodeVisitor nodeVisitor)
```

    - 

#### transformParallel

```
public Node transformParallel(Node root,
                              NodeVisitor nodeVisitor)
```

    - 

#### transformParallel

```
public Node transformParallel(Node root,
                              NodeVisitor nodeVisitor,
                              java.util.concurrent.ForkJoinPool forkJoinPool)
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