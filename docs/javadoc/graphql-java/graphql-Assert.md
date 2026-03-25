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

graphql

## Class Assert

- java.lang.Object

- 

  - graphql.Assert

- 

---

```
public class Assert
extends java.lang.Object
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`Assert()` 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description

`static void`
`assertFalse(boolean condition)` 

`static void`
`assertFalse(boolean condition,
           java.util.function.Supplier<java.lang.String> msg)` 

`static <T> T`
`assertNeverCalled()` 

`static <T> java.util.Collection<T>`
`assertNotEmpty(java.util.Collection<T> collection)` 

`static <T> java.util.Collection<T>`
`assertNotEmpty(java.util.Collection<T> collection,
              java.util.function.Supplier<java.lang.String> msg)` 

`static <T> T`
`assertNotNull(T object)` 

`static <T> T`
`assertNotNull(T object,
             java.util.function.Supplier<java.lang.String> msg)` 

`static <T> T`
`assertNotNullWithNPE(T object,
                    java.util.function.Supplier<java.lang.String> msg)` 

`static <T> void`
`assertNull(T object)` 

`static <T> void`
`assertNull(T object,
          java.util.function.Supplier<java.lang.String> msg)` 

`static <T> T`
`assertShouldNeverHappen()` 

`static <T> T`
`assertShouldNeverHappen(java.lang.String format,
                       java.lang.Object... args)` 

`static void`
`assertTrue(boolean condition)` 

`static void`
`assertTrue(boolean condition,
          java.util.function.Supplier<java.lang.String> msg)` 

`static java.lang.String`
`assertValidName(java.lang.String name)`
Validates that the Lexical token name matches the current spec.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Assert

```
public Assert()
```

  - 

### Method Detail

    - 

#### assertNotNull

```
public static <T> T assertNotNull(T object,
                                  java.util.function.Supplier<java.lang.String> msg)
```

    - 

#### assertNotNullWithNPE

```
public static <T> T assertNotNullWithNPE(T object,
                                         java.util.function.Supplier<java.lang.String> msg)
```

    - 

#### assertNotNull

```
public static <T> T assertNotNull(T object)
```

    - 

#### assertNull

```
public static <T> void assertNull(T object,
                                  java.util.function.Supplier<java.lang.String> msg)
```

    - 

#### assertNull

```
public static <T> void assertNull(T object)
```

    - 

#### assertNeverCalled

```
public static <T> T assertNeverCalled()
```

    - 

#### assertShouldNeverHappen

```
public static <T> T assertShouldNeverHappen(java.lang.String format,
                                            java.lang.Object... args)
```

    - 

#### assertShouldNeverHappen

```
public static <T> T assertShouldNeverHappen()
```

    - 

#### assertNotEmpty

```
public static <T> java.util.Collection<T> assertNotEmpty(java.util.Collection<T> collection)
```

    - 

#### assertNotEmpty

```
public static <T> java.util.Collection<T> assertNotEmpty(java.util.Collection<T> collection,
                                                         java.util.function.Supplier<java.lang.String> msg)
```

    - 

#### assertTrue

```
public static void assertTrue(boolean condition,
                              java.util.function.Supplier<java.lang.String> msg)
```

    - 

#### assertTrue

```
public static void assertTrue(boolean condition)
```

    - 

#### assertFalse

```
public static void assertFalse(boolean condition,
                               java.util.function.Supplier<java.lang.String> msg)
```

    - 

#### assertFalse

```
public static void assertFalse(boolean condition)
```

    - 

#### assertValidName

```
public static java.lang.String assertValidName(java.lang.String name)
```

Validates that the Lexical token name matches the current spec.
 currently non null, non empty,

Parameters:
`name` - - the name to be validated.
Returns:
the name if valid, or AssertException if invalid.

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