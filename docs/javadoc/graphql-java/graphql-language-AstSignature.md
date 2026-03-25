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

## Class AstSignature

- java.lang.Object

- 

  - graphql.language.AstSignature

- 

---

```
@PublicApi
public class AstSignature
extends java.lang.Object
```

This will produce signature query documents that can be used say for logging.

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AstSignature()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Document`
`signatureQuery(Document document,
              java.lang.String operationName)`
This can produce a "signature" canonical AST that conforms to the algorithm as outlined
  here
 which removes excess operations, removes any field aliases, hides literal values and sorts the result into a canonical
 query

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AstSignature

```
public AstSignature()
```

  - 

### Method Detail

    - 

#### signatureQuery

```
public Document signatureQuery(Document document,
                               java.lang.String operationName)
```

This can produce a "signature" canonical AST that conforms to the algorithm as outlined
  here
 which removes excess operations, removes any field aliases, hides literal values and sorts the result into a canonical
 query

Parameters:
`document` - the document to make a signature query from
`operationName` - the name of the operation to do it for (since only one query can be run at a time)
Returns:
the signature query in document form

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