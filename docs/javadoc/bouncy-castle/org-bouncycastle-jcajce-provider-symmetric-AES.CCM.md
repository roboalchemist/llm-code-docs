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

## Class AES.CCM

- java.lang.Object

- 

  - javax.crypto.CipherSpi

  - 

    - org.bouncycastle.jcajce.provider.symmetric.util.BaseWrapCipher

    - 

      - org.bouncycastle.jcajce.provider.symmetric.util.BaseBlockCipher

      - 

        - org.bouncycastle.jcajce.provider.symmetric.AES.CCM

- 

All Implemented Interfaces:
PBE

Enclosing class:
AES

---

```
public static class AES.CCM
extends BaseBlockCipher
```

- 

  - 

### Nested Class Summary

    - 

### Nested classes/interfaces inherited from class org.bouncycastle.jcajce.provider.symmetric.util.BaseWrapCipher

`BaseWrapCipher.ErasableOutputStream, BaseWrapCipher.InvalidKeyOrParametersException`

    - 

### Nested classes/interfaces inherited from interface org.bouncycastle.jcajce.provider.symmetric.util.PBE

`PBE.Util`

  - 

### Field Summary

    - 

### Fields inherited from class org.bouncycastle.jcajce.provider.symmetric.util.BaseWrapCipher

`engineParams, pbeHash, pbeIvSize, pbeKeySize, pbeType, wrapEngine`

    - 

### Fields inherited from interface org.bouncycastle.jcajce.provider.symmetric.util.PBE

`GOST3411, MD2, MD5, OPENSSL, PKCS12, PKCS5S1, PKCS5S1_UTF8, PKCS5S2, PKCS5S2_UTF8, RIPEMD160, SHA1, SHA224, SHA256, SHA3_224, SHA3_256, SHA3_384, SHA3_512, SHA384, SHA512, SHA512_224, SHA512_256, SM3, TIGER`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`CCM()` 

  - 

### Method Summary

    - 

### Methods inherited from class org.bouncycastle.jcajce.provider.symmetric.util.BaseBlockCipher

`engineDoFinal, engineDoFinal, engineGetBlockSize, engineGetIV, engineGetKeySize, engineGetOutputSize, engineGetParameters, engineInit, engineInit, engineInit, engineSetMode, engineSetPadding, engineUpdate, engineUpdate, engineUpdateAAD, engineUpdateAAD`

    - 

### Methods inherited from class org.bouncycastle.jcajce.provider.symmetric.util.BaseWrapCipher

`createParametersInstance, engineUnwrap, engineWrap`

    - 

### Methods inherited from class javax.crypto.CipherSpi

`engineDoFinal, engineUpdate`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### CCM

```
public CCM()
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