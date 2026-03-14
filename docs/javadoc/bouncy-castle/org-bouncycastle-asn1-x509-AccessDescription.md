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

org.bouncycastle.asn1.x509

## Class AccessDescription

- java.lang.Object

- 

  - org.bouncycastle.asn1.ASN1Object

  - 

    - org.bouncycastle.asn1.x509.AccessDescription

- 

All Implemented Interfaces:
ASN1Encodable, Encodable

---

```
public class AccessDescription
extends ASN1Object
```

The AccessDescription object.
 

```

 AccessDescription  ::=  SEQUENCE {
       accessMethod          OBJECT IDENTIFIER,
       accessLocation        GeneralName  }
 
```

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static ASN1ObjectIdentifier`
`id_ad_caIssuers` 

`static ASN1ObjectIdentifier`
`id_ad_ocsp` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AccessDescription(ASN1ObjectIdentifier oid,
                 GeneralName location)`
create an AccessDescription with the oid and location provided.

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`GeneralName`
`getAccessLocation()` 

`ASN1ObjectIdentifier`
`getAccessMethod()` 

`static AccessDescription`
`getInstance(java.lang.Object obj)` 

`ASN1Primitive`
`toASN1Primitive()`
Method providing a primitive representation of this object suitable for encoding.

`java.lang.String`
`toString()` 

    - 

### Methods inherited from class org.bouncycastle.asn1.ASN1Object

`encodeTo, encodeTo, equals, getEncoded, getEncoded, hasEncodedTagValue, hashCode`

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### id_ad_caIssuers

```
public static final ASN1ObjectIdentifier id_ad_caIssuers
```

    - 

#### id_ad_ocsp

```
public static final ASN1ObjectIdentifier id_ad_ocsp
```

  - 

### Constructor Detail

    - 

#### AccessDescription

```
public AccessDescription(ASN1ObjectIdentifier oid,
                         GeneralName location)
```

create an AccessDescription with the oid and location provided.

  - 

### Method Detail

    - 

#### getInstance

```
public static AccessDescription getInstance(java.lang.Object obj)
```

    - 

#### getAccessMethod

```
public ASN1ObjectIdentifier getAccessMethod()
```

Returns:
the access method.

    - 

#### getAccessLocation

```
public GeneralName getAccessLocation()
```

Returns:
the access location

    - 

#### toASN1Primitive

```
public ASN1Primitive toASN1Primitive()
```

Description copied from class: `ASN1Object`
Method providing a primitive representation of this object suitable for encoding.

Specified by:
`toASN1Primitive` in interface `ASN1Encodable`
Specified by:
`toASN1Primitive` in class `ASN1Object`
Returns:
a primitive representation of this object.

    - 

#### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`

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