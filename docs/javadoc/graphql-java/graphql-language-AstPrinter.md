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

## Class AstPrinter

- java.lang.Object

- 

  - graphql.language.AstPrinter

- 

---

```
@PublicApi
public class AstPrinter
extends java.lang.Object
```

This can take graphql language AST and print it out as a string

- 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description

`static java.lang.String`
`printAst(Node node)`
This will pretty print the AST node in graphql language format

`static void`
`printAst(java.io.Writer writer,
        Node node)`
This will pretty print the AST node in graphql language format

`static java.lang.String`
`printAstCompact(Node node)`
This will print the Ast node in graphql language format in a compact manner, with no new lines
 and comments stripped out of the text.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Method Detail

    - 

#### printAst

```
public static java.lang.String printAst(Node node)
```

This will pretty print the AST node in graphql language format

Parameters:
`node` - the AST node to print
Returns:
the printed node in graphql language format

    - 

#### printAst

```
public static void printAst(java.io.Writer writer,
                            Node node)
```

This will pretty print the AST node in graphql language format

Parameters:
`writer` - the place to put the output
`node` - the AST node to print

    - 

#### printAstCompact

```
public static java.lang.String printAstCompact(Node node)
```

This will print the Ast node in graphql language format in a compact manner, with no new lines
 and comments stripped out of the text.

Parameters:
`node` - the AST node to print
Returns:
the printed node in a compact graphql language format

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