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

org.bouncycastle.crypto.modes

## Interface AEADBlockCipher

- 

All Superinterfaces:
AEADCipher

All Known Subinterfaces:
CCMModeCipher, GCMModeCipher

All Known Implementing Classes:
CCMBlockCipher, EAXBlockCipher, GCMBlockCipher, GCMSIVBlockCipher, KCCMBlockCipher, KGCMBlockCipher, OCBBlockCipher

---

```
public interface AEADBlockCipher
extends AEADCipher
```

An `AEADCipher` based on a `BlockCipher`.

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

`BlockCipher`
`getUnderlyingCipher()`
return the `BlockCipher` this object wraps.

    - 

### Methods inherited from interface org.bouncycastle.crypto.modes.AEADCipher

`doFinal, getAlgorithmName, getMac, getOutputSize, getUpdateOutputSize, init, processAADByte, processAADBytes, processByte, processBytes, reset`

- 

  - 

### Method Detail

    - 

#### getUnderlyingCipher

```
BlockCipher getUnderlyingCipher()
```

return the `BlockCipher` this object wraps.

Returns:
the `BlockCipher` this object wraps.

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