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

org.bouncycastle.asn1.x500.style

## Class AbstractX500NameStyle

- java.lang.Object

- 

  - org.bouncycastle.asn1.x500.style.AbstractX500NameStyle

- 

All Implemented Interfaces:
X500NameStyle

Direct Known Subclasses:
BCStyle, RFC4519Style

---

```
public abstract class AbstractX500NameStyle
extends java.lang.Object
implements X500NameStyle
```

This class provides some default behavior and common implementation for a
 X500NameStyle. It should be easily extendable to support implementing the
 desired X500NameStyle.

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AbstractX500NameStyle()` 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`areEqual(X500Name name1,
        X500Name name2)`
Return true if the two names are equal.

`int`
`calculateHashCode(X500Name name)`
Calculate a hashCode for the passed in name.

`static java.util.Hashtable`
`copyHashTable(java.util.Hashtable paramsMap)`
Tool function to shallow copy a Hashtable.

`protected ASN1Encodable`
`encodeStringValue(ASN1ObjectIdentifier oid,
                 java.lang.String value)`
Encoded every value into a UTF8String.

`protected boolean`
`rdnAreEqual(RDN rdn1,
           RDN rdn2)` 

`ASN1Encodable`
`stringToValue(ASN1ObjectIdentifier oid,
             java.lang.String value)`
For all string values starting with '#' is assumed, that these are
 already valid ASN.1 objects encoded in hex.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface org.bouncycastle.asn1.x500.X500NameStyle

`attrNameToOID, fromString, oidToAttrNames, oidToDisplayName, toString`

- 

  - 

### Constructor Detail

    - 

#### AbstractX500NameStyle

```
public AbstractX500NameStyle()
```

  - 

### Method Detail

    - 

#### copyHashTable

```
public static java.util.Hashtable copyHashTable(java.util.Hashtable paramsMap)
```

Tool function to shallow copy a Hashtable.

Parameters:
`paramsMap` - table to copy
Returns:
the copy of the table

    - 

#### calculateHashCode

```
public int calculateHashCode(X500Name name)
```

Description copied from interface: `X500NameStyle`
Calculate a hashCode for the passed in name.

Specified by:
`calculateHashCode` in interface `X500NameStyle`
Parameters:
`name` - the name the hashCode is required for.
Returns:
the calculated hashCode.

    - 

#### stringToValue

```
public ASN1Encodable stringToValue(ASN1ObjectIdentifier oid,
                                   java.lang.String value)
```

For all string values starting with '#' is assumed, that these are
 already valid ASN.1 objects encoded in hex.
 

 All other string values are send to
 `encodeStringValue(ASN1ObjectIdentifier, String)`.
 
 Subclasses should overwrite
 `encodeStringValue(ASN1ObjectIdentifier, String)`
 to change the encoding of specific types.

Specified by:
`stringToValue` in interface `X500NameStyle`
Parameters:
`oid` - the DN name of the value.
`value` - the String representation of the value.
Returns:
the ASN.1 equivalent for the value.

    - 

#### encodeStringValue

```
protected ASN1Encodable encodeStringValue(ASN1ObjectIdentifier oid,
                                          java.lang.String value)
```

Encoded every value into a UTF8String.
 

 Subclasses should overwrite
 this method to change the encoding of specific types.
 

Parameters:
`oid` - the DN oid of the value
`value` - the String representation of the value
Returns:
a the value encoded into a ASN.1 object. Never returns `null`.

    - 

#### areEqual

```
public boolean areEqual(X500Name name1,
                        X500Name name2)
```

Description copied from interface: `X500NameStyle`
Return true if the two names are equal.

Specified by:
`areEqual` in interface `X500NameStyle`
Parameters:
`name1` - first name for comparison.
`name2` - second name for comparison.
Returns:
true if name1 = name 2, false otherwise.

    - 

#### rdnAreEqual

```
protected boolean rdnAreEqual(RDN rdn1,
                              RDN rdn2)
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