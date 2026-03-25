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

org.bouncycastle.crypto.params

## Class AEADParameters

- java.lang.Object

- 

  - org.bouncycastle.crypto.params.AEADParameters

- 

All Implemented Interfaces:
CipherParameters

Direct Known Subclasses:
CCMParameters

---

```
public class AEADParameters
extends java.lang.Object
implements CipherParameters
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AEADParameters(KeyParameter key,
              int macSize,
              byte[] nonce)`
Base constructor.

`AEADParameters(KeyParameter key,
              int macSize,
              byte[] nonce,
              byte[] associatedText)`
Base constructor.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`byte[]`
`getAssociatedText()` 

`KeyParameter`
`getKey()` 

`int`
`getMacSize()` 

`byte[]`
`getNonce()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AEADParameters

```
public AEADParameters(KeyParameter key,
                      int macSize,
                      byte[] nonce)
```

Base constructor.

Parameters:
`key` - key to be used by underlying cipher
`macSize` - macSize in bits
`nonce` - nonce to be used

    - 

#### AEADParameters

```
public AEADParameters(KeyParameter key,
                      int macSize,
                      byte[] nonce,
                      byte[] associatedText)
```

Base constructor.

Parameters:
`key` - key to be used by underlying cipher
`macSize` - macSize in bits
`nonce` - nonce to be used
`associatedText` - initial associated text, if any

  - 

### Method Detail

    - 

#### getKey

```
public KeyParameter getKey()
```

    - 

#### getMacSize

```
public int getMacSize()
```

    - 

#### getAssociatedText

```
public byte[] getAssociatedText()
```

    - 

#### getNonce

```
public byte[] getNonce()
```

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