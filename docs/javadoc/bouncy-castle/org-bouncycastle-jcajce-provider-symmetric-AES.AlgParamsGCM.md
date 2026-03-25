JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

**Bouncy Castle Cryptography Library 1.83**

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

org.bouncycastle.jcajce.provider.symmetric

## Class AES.AlgParamsGCM

- java.lang.Object

- 

  - java.security.AlgorithmParametersSpi

  - 

    - org.bouncycastle.jcajce.provider.symmetric.util.BaseAlgorithmParameters

    - 

      - org.bouncycastle.jcajce.provider.symmetric.AES.AlgParamsGCM

- 

Enclosing class:
AES

---

```
public static class AES.AlgParamsGCM
extends BaseAlgorithmParameters
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AlgParamsGCM()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`protected byte[]`
`engineGetEncoded()` 

`protected byte[]`
`engineGetEncoded(java.lang.String format)` 

`protected void`
`engineInit(java.security.spec.AlgorithmParameterSpec paramSpec)` 

`protected void`
`engineInit(byte[] params)` 

`protected void`
`engineInit(byte[] params,
          java.lang.String format)` 

`protected java.lang.String`
`engineToString()` 

`protected java.security.spec.AlgorithmParameterSpec`
`localEngineGetParameterSpec(java.lang.Class paramSpec)` 

    - 

### Methods inherited from class org.bouncycastle.jcajce.provider.symmetric.util.BaseAlgorithmParameters

`engineGetParameterSpec, isASN1FormatString`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AlgParamsGCM

```
public AlgParamsGCM()
```

  - 

### Method Detail

    - 

#### engineInit

```
protected void engineInit(java.security.spec.AlgorithmParameterSpec paramSpec)
                   throws java.security.spec.InvalidParameterSpecException
```

Specified by:
`engineInit` in class `java.security.AlgorithmParametersSpi`
Throws:
`java.security.spec.InvalidParameterSpecException`

    - 

#### engineInit

```
protected void engineInit(byte[] params)
                   throws java.io.IOException
```

Specified by:
`engineInit` in class `java.security.AlgorithmParametersSpi`
Throws:
`java.io.IOException`

    - 

#### engineInit

```
protected void engineInit(byte[] params,
                          java.lang.String format)
                   throws java.io.IOException
```

Specified by:
`engineInit` in class `java.security.AlgorithmParametersSpi`
Throws:
`java.io.IOException`

    - 

#### engineGetEncoded

```
protected byte[] engineGetEncoded()
                           throws java.io.IOException
```

Specified by:
`engineGetEncoded` in class `java.security.AlgorithmParametersSpi`
Throws:
`java.io.IOException`

    - 

#### engineGetEncoded

```
protected byte[] engineGetEncoded(java.lang.String format)
                           throws java.io.IOException
```

Specified by:
`engineGetEncoded` in class `java.security.AlgorithmParametersSpi`
Throws:
`java.io.IOException`

    - 

#### engineToString

```
protected java.lang.String engineToString()
```

Specified by:
`engineToString` in class `java.security.AlgorithmParametersSpi`

    - 

#### localEngineGetParameterSpec

```
protected java.security.spec.AlgorithmParameterSpec localEngineGetParameterSpec(java.lang.Class paramSpec)
                                                                         throws java.security.spec.InvalidParameterSpecException
```

Specified by:
`localEngineGetParameterSpec` in class `BaseAlgorithmParameters`
Throws:
`java.security.spec.InvalidParameterSpecException`

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

**Bouncy Castle Cryptography Library 1.83**

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