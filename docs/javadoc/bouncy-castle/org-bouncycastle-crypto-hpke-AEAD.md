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

org.bouncycastle.crypto.hpke

## Class AEAD

- java.lang.Object

- 

  - org.bouncycastle.crypto.hpke.AEAD

- 

---

```
public class AEAD
extends java.lang.Object
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AEAD(short aeadId,
    byte[] key,
    byte[] baseNonce)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`byte[]`
`open(byte[] aad,
    byte[] ct)` 

`byte[]`
`open(byte[] aad,
    byte[] ct,
    int ctOffset,
    int ctLength)` 

`byte[]`
`seal(byte[] aad,
    byte[] pt)` 

`byte[]`
`seal(byte[] aad,
    byte[] pt,
    int ptOffset,
    int ptLength)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AEAD

```
public AEAD(short aeadId,
            byte[] key,
            byte[] baseNonce)
```

  - 

### Method Detail

    - 

#### seal

```
public byte[] seal(byte[] aad,
                   byte[] pt)
            throws InvalidCipherTextException
```

Throws:
`InvalidCipherTextException`

    - 

#### seal

```
public byte[] seal(byte[] aad,
                   byte[] pt,
                   int ptOffset,
                   int ptLength)
            throws InvalidCipherTextException
```

Throws:
`InvalidCipherTextException`

    - 

#### open

```
public byte[] open(byte[] aad,
                   byte[] ct)
            throws InvalidCipherTextException
```

Throws:
`InvalidCipherTextException`

    - 

#### open

```
public byte[] open(byte[] aad,
                   byte[] ct,
                   int ctOffset,
                   int ctLength)
            throws InvalidCipherTextException
```

Throws:
`InvalidCipherTextException`

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