JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

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

com.sun.mail.smtp

## Class DigestMD5

- java.lang.Object

- 

  - com.sun.mail.smtp.DigestMD5

- 

---

```
public class DigestMD5
extends Object
```

DIGEST-MD5 authentication support.

Author:
Dean Gibson, Bill Shannon

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`DigestMD5(MailLogger logger)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`byte[]`
`authClient(String host,
          String user,
          String passwd,
          String realm,
          String serverChallenge)`
Return client's authentication response to server's challenge.

`boolean`
`authServer(String serverResponse)`
Allow the client to authenticate the server based on its
 response.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### DigestMD5

```
public DigestMD5(MailLogger logger)
```

  - 

### Method Detail

    - 

#### authClient

```
public byte[] authClient(String host,
                         String user,
                         String passwd,
                         String realm,
                         String serverChallenge)
                  throws IOException
```

Return client's authentication response to server's challenge.

Parameters:
`host` - the host name
`user` - the user name
`passwd` - the user's password
`realm` - the security realm
`serverChallenge` - the challenge from the server
Returns:
byte array with client's response
Throws:
`IOException` - for I/O errors

    - 

#### authServer

```
public boolean authServer(String serverResponse)
                   throws IOException
```

Allow the client to authenticate the server based on its
 response.

Parameters:
`serverResponse` - the response that was received from the server
Returns:
true if server is authenticated
Throws:
`IOException` - for character conversion failures

Skip navigation links

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

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

Copyright © 2018 Oracle. All rights reserved.