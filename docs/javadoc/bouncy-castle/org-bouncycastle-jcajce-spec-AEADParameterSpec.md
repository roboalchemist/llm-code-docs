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

org.bouncycastle.jcajce.spec

## Class AEADParameterSpec

- java.lang.Object

- 

  - javax.crypto.spec.IvParameterSpec

  - 

    - org.bouncycastle.jcajce.spec.AEADParameterSpec

- 

All Implemented Interfaces:
java.security.spec.AlgorithmParameterSpec

---

```
public class AEADParameterSpec
extends javax.crypto.spec.IvParameterSpec
```

ParameterSpec for AEAD modes which allows associated data to be added via an algorithm parameter spec.In normal
 circumstances you would only want to use this if you had to work with the pre-JDK1.7 Cipher class as associated
 data is ignored for the purposes of returning a Cipher's parameters.

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AEADParameterSpec(byte[] nonce,
                 int macSizeInBits)`
Base constructor.

`AEADParameterSpec(byte[] nonce,
                 int macSizeInBits,
                 byte[] associatedData)`
Base constructor with prepended associated data.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`byte[]`
`getAssociatedData()`
Return the associated data associated with this parameter spec.

`int`
`getMacSizeInBits()`
Return the size of the MAC associated with this parameter spec.

`byte[]`
`getNonce()`
Return the nonce (same as IV) associated with this parameter spec.

    - 

### Methods inherited from class javax.crypto.spec.IvParameterSpec

`getIV`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AEADParameterSpec

```
public AEADParameterSpec(byte[] nonce,
                         int macSizeInBits)
```

Base constructor.

Parameters:
`nonce` - nonce/iv to be used
`macSizeInBits` - macSize in bits

    - 

#### AEADParameterSpec

```
public AEADParameterSpec(byte[] nonce,
                         int macSizeInBits,
                         byte[] associatedData)
```

Base constructor with prepended associated data.

Parameters:
`nonce` - nonce/iv to be used
`macSizeInBits` - macSize in bits
`associatedData` - associated data to be prepended to the cipher stream.

  - 

### Method Detail

    - 

#### getMacSizeInBits

```
public int getMacSizeInBits()
```

Return the size of the MAC associated with this parameter spec.

Returns:
the MAC size in bits.

    - 

#### getAssociatedData

```
public byte[] getAssociatedData()
```

Return the associated data associated with this parameter spec.

Returns:
the associated data, null if there isn't any.

    - 

#### getNonce

```
public byte[] getNonce()
```

Return the nonce (same as IV) associated with this parameter spec.

Returns:
the nonce/IV.

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