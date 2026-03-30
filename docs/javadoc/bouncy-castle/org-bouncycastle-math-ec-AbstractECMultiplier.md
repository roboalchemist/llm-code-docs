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

org.bouncycastle.math.ec

## Class AbstractECMultiplier

- java.lang.Object

- 

  - org.bouncycastle.math.ec.AbstractECMultiplier

- 

All Implemented Interfaces:
ECMultiplier

Direct Known Subclasses:
FixedPointCombMultiplier, GLVMultiplier, WNafL2RMultiplier, WTauNafMultiplier

---

```
public abstract class AbstractECMultiplier
extends java.lang.Object
implements ECMultiplier
```

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AbstractECMultiplier()` 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods Concrete Methods 

Modifier and Type
Method and Description

`protected ECPoint`
`checkResult(ECPoint p)` 

`ECPoint`
`multiply(ECPoint p,
        java.math.BigInteger k)`
Multiplies the `ECPoint p` by `k`, i.e.

`protected abstract ECPoint`
`multiplyPositive(ECPoint p,
                java.math.BigInteger k)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AbstractECMultiplier

```
public AbstractECMultiplier()
```

  - 

### Method Detail

    - 

#### multiply

```
public ECPoint multiply(ECPoint p,
                        java.math.BigInteger k)
```

Description copied from interface: `ECMultiplier`
Multiplies the `ECPoint p` by `k`, i.e.
 `p` is added `k` times to itself.

Specified by:
`multiply` in interface `ECMultiplier`
Parameters:
`p` - The `ECPoint` to be multiplied.
`k` - The factor by which `p` is multiplied.
Returns:
`p` multiplied by `k`.

    - 

#### multiplyPositive

```
protected abstract ECPoint multiplyPositive(ECPoint p,
                                            java.math.BigInteger k)
```

    - 

#### checkResult

```
protected ECPoint checkResult(ECPoint p)
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