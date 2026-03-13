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

org.bouncycastle.jcajce.provider.keystore.util

## Class AdaptingKeyStoreSpi

- java.lang.Object

- 

  - java.security.KeyStoreSpi

  - 

    - org.bouncycastle.jcajce.provider.keystore.util.AdaptingKeyStoreSpi

- 

Direct Known Subclasses:
PKCS12KeyStoreSpi.BCPKCS12KeyStore, PKCS12KeyStoreSpi.BCPKCS12KeyStore3DES, PKCS12KeyStoreSpi.BCPKCS12KeyStoreAES256, PKCS12KeyStoreSpi.BCPKCS12KeyStoreAES256GCM, PKCS12KeyStoreSpi.DefPKCS12KeyStore, PKCS12KeyStoreSpi.DefPKCS12KeyStore3DES, PKCS12KeyStoreSpi.DefPKCS12KeyStoreAES256, PKCS12KeyStoreSpi.DefPKCS12KeyStoreAES256GCM

---

```
public class AdaptingKeyStoreSpi
extends java.security.KeyStoreSpi
```

Implements a certificate only JKS key store.

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static java.lang.String`
`COMPAT_OVERRIDE` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AdaptingKeyStoreSpi(JcaJceHelper helper,
                   java.security.KeyStoreSpi primaryStore)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`java.util.Enumeration<java.lang.String>`
`engineAliases()` 

`boolean`
`engineContainsAlias(java.lang.String alias)` 

`void`
`engineDeleteEntry(java.lang.String alias)` 

`java.security.cert.Certificate`
`engineGetCertificate(java.lang.String alias)` 

`java.lang.String`
`engineGetCertificateAlias(java.security.cert.Certificate cert)` 

`java.security.cert.Certificate[]`
`engineGetCertificateChain(java.lang.String alias)` 

`java.util.Date`
`engineGetCreationDate(java.lang.String alias)` 

`java.security.Key`
`engineGetKey(java.lang.String alias,
            char[] password)` 

`boolean`
`engineIsCertificateEntry(java.lang.String alias)` 

`boolean`
`engineIsKeyEntry(java.lang.String alias)` 

`void`
`engineLoad(java.io.InputStream stream,
          char[] password)` 

`void`
`engineLoad(java.security.KeyStore.LoadStoreParameter parameter)` 

`boolean`
`engineProbe(java.io.InputStream stream)` 

`void`
`engineSetCertificateEntry(java.lang.String alias,
                         java.security.cert.Certificate cert)` 

`void`
`engineSetKeyEntry(java.lang.String alias,
                 byte[] key,
                 java.security.cert.Certificate[] chain)` 

`void`
`engineSetKeyEntry(java.lang.String alias,
                 java.security.Key key,
                 char[] password,
                 java.security.cert.Certificate[] chain)` 

`int`
`engineSize()` 

`void`
`engineStore(java.security.KeyStore.LoadStoreParameter parameter)` 

`void`
`engineStore(java.io.OutputStream stream,
           char[] password)` 

    - 

### Methods inherited from class java.security.KeyStoreSpi

`engineEntryInstanceOf, engineGetEntry, engineSetEntry`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### COMPAT_OVERRIDE

```
public static final java.lang.String COMPAT_OVERRIDE
```

See Also:
Constant Field Values

  - 

### Constructor Detail

    - 

#### AdaptingKeyStoreSpi

```
public AdaptingKeyStoreSpi(JcaJceHelper helper,
                           java.security.KeyStoreSpi primaryStore)
```

  - 

### Method Detail

    - 

#### engineProbe

```
public boolean engineProbe(java.io.InputStream stream)
                    throws java.io.IOException
```

Throws:
`java.io.IOException`

    - 

#### engineGetKey

```
public java.security.Key engineGetKey(java.lang.String alias,
                                      char[] password)
                               throws java.security.NoSuchAlgorithmException,
                                      java.security.UnrecoverableKeyException
```

Specified by:
`engineGetKey` in class `java.security.KeyStoreSpi`
Throws:
`java.security.NoSuchAlgorithmException`
`java.security.UnrecoverableKeyException`

    - 

#### engineGetCertificateChain

```
public java.security.cert.Certificate[] engineGetCertificateChain(java.lang.String alias)
```

Specified by:
`engineGetCertificateChain` in class `java.security.KeyStoreSpi`

    - 

#### engineGetCertificate

```
public java.security.cert.Certificate engineGetCertificate(java.lang.String alias)
```

Specified by:
`engineGetCertificate` in class `java.security.KeyStoreSpi`

    - 

#### engineGetCreationDate

```
public java.util.Date engineGetCreationDate(java.lang.String alias)
```

Specified by:
`engineGetCreationDate` in class `java.security.KeyStoreSpi`

    - 

#### engineSetKeyEntry

```
public void engineSetKeyEntry(java.lang.String alias,
                              java.security.Key key,
                              char[] password,
                              java.security.cert.Certificate[] chain)
                       throws java.security.KeyStoreException
```

Specified by:
`engineSetKeyEntry` in class `java.security.KeyStoreSpi`
Throws:
`java.security.KeyStoreException`

    - 

#### engineSetKeyEntry

```
public void engineSetKeyEntry(java.lang.String alias,
                              byte[] key,
                              java.security.cert.Certificate[] chain)
                       throws java.security.KeyStoreException
```

Specified by:
`engineSetKeyEntry` in class `java.security.KeyStoreSpi`
Throws:
`java.security.KeyStoreException`

    - 

#### engineSetCertificateEntry

```
public void engineSetCertificateEntry(java.lang.String alias,
                                      java.security.cert.Certificate cert)
                               throws java.security.KeyStoreException
```

Specified by:
`engineSetCertificateEntry` in class `java.security.KeyStoreSpi`
Throws:
`java.security.KeyStoreException`

    - 

#### engineDeleteEntry

```
public void engineDeleteEntry(java.lang.String alias)
                       throws java.security.KeyStoreException
```

Specified by:
`engineDeleteEntry` in class `java.security.KeyStoreSpi`
Throws:
`java.security.KeyStoreException`

    - 

#### engineAliases

```
public java.util.Enumeration<java.lang.String> engineAliases()
```

Specified by:
`engineAliases` in class `java.security.KeyStoreSpi`

    - 

#### engineContainsAlias

```
public boolean engineContainsAlias(java.lang.String alias)
```

Specified by:
`engineContainsAlias` in class `java.security.KeyStoreSpi`

    - 

#### engineSize

```
public int engineSize()
```

Specified by:
`engineSize` in class `java.security.KeyStoreSpi`

    - 

#### engineIsKeyEntry

```
public boolean engineIsKeyEntry(java.lang.String alias)
```

Specified by:
`engineIsKeyEntry` in class `java.security.KeyStoreSpi`

    - 

#### engineIsCertificateEntry

```
public boolean engineIsCertificateEntry(java.lang.String alias)
```

Specified by:
`engineIsCertificateEntry` in class `java.security.KeyStoreSpi`

    - 

#### engineGetCertificateAlias

```
public java.lang.String engineGetCertificateAlias(java.security.cert.Certificate cert)
```

Specified by:
`engineGetCertificateAlias` in class `java.security.KeyStoreSpi`

    - 

#### engineStore

```
public void engineStore(java.io.OutputStream stream,
                        char[] password)
                 throws java.io.IOException,
                        java.security.NoSuchAlgorithmException,
                        java.security.cert.CertificateException
```

Specified by:
`engineStore` in class `java.security.KeyStoreSpi`
Throws:
`java.io.IOException`
`java.security.NoSuchAlgorithmException`
`java.security.cert.CertificateException`

    - 

#### engineStore

```
public void engineStore(java.security.KeyStore.LoadStoreParameter parameter)
                 throws java.io.IOException,
                        java.security.NoSuchAlgorithmException,
                        java.security.cert.CertificateException
```

Overrides:
`engineStore` in class `java.security.KeyStoreSpi`
Throws:
`java.io.IOException`
`java.security.NoSuchAlgorithmException`
`java.security.cert.CertificateException`

    - 

#### engineLoad

```
public void engineLoad(java.io.InputStream stream,
                       char[] password)
                throws java.io.IOException,
                       java.security.NoSuchAlgorithmException,
                       java.security.cert.CertificateException
```

Specified by:
`engineLoad` in class `java.security.KeyStoreSpi`
Throws:
`java.io.IOException`
`java.security.NoSuchAlgorithmException`
`java.security.cert.CertificateException`

    - 

#### engineLoad

```
public void engineLoad(java.security.KeyStore.LoadStoreParameter parameter)
                throws java.io.IOException,
                       java.security.NoSuchAlgorithmException,
                       java.security.cert.CertificateException
```

Overrides:
`engineLoad` in class `java.security.KeyStoreSpi`
Throws:
`java.io.IOException`
`java.security.NoSuchAlgorithmException`
`java.security.cert.CertificateException`

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