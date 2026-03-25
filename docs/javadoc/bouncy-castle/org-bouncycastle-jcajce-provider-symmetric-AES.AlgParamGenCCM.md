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

## Class AES.AlgParamGenCCM

- java.lang.Object

- 

  - java.security.AlgorithmParameterGeneratorSpi

  - 

    - org.bouncycastle.jcajce.provider.symmetric.util.BaseAlgorithmParameterGenerator

    - 

      - org.bouncycastle.jcajce.provider.symmetric.AES.AlgParamGenCCM

- 

Enclosing class:
AES

---

```
public static class AES.AlgParamGenCCM
extends BaseAlgorithmParameterGenerator
```

- 

  - 

### Field Summary

    - 

### Fields inherited from class org.bouncycastle.jcajce.provider.symmetric.util.BaseAlgorithmParameterGenerator

`random, strength`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AlgParamGenCCM()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`protected java.security.AlgorithmParameters`
`engineGenerateParameters()` 

`protected void`
`engineInit(java.security.spec.AlgorithmParameterSpec genParamSpec,
          java.security.SecureRandom random)` 

    - 

### Methods inherited from class org.bouncycastle.jcajce.provider.symmetric.util.BaseAlgorithmParameterGenerator

`createParametersInstance, engineInit`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AlgParamGenCCM

```
public AlgParamGenCCM()
```

  - 

### Method Detail

    - 

#### engineInit

```
protected void engineInit(java.security.spec.AlgorithmParameterSpec genParamSpec,
                          java.security.SecureRandom random)
                   throws java.security.InvalidAlgorithmParameterException
```

Specified by:
`engineInit` in class `java.security.AlgorithmParameterGeneratorSpi`
Throws:
`java.security.InvalidAlgorithmParameterException`

    - 

#### engineGenerateParameters

```
protected java.security.AlgorithmParameters engineGenerateParameters()
```

Specified by:
`engineGenerateParameters` in class `java.security.AlgorithmParameterGeneratorSpi`

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