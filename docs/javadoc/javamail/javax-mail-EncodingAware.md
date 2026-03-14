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

javax.mail

## Interface EncodingAware

- 

---

```
public interface EncodingAware
```

A `DataSource` that also implements
 `EncodingAware` may specify the Content-Transfer-Encoding
 to use for its data.  Valid Content-Transfer-Encoding values specified
 by RFC 2045 are "7bit", "8bit", "quoted-printable", "base64", and "binary".
 

 For example, a `FileDataSource`
 could be created that forces all files to be base64 encoded:
 

```

  public class Base64FileDataSource extends FileDataSource
                                        implements EncodingAware {
        public Base64FileDataSource(File file) {
            super(file);
        }

        // implements EncodingAware.getEncoding()
        public String getEncoding() {
            return "base64";
        }
  }
 
```

Since:
JavaMail 1.5
Author:
Bill Shannon

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

`String`
`getEncoding()`
Return the MIME Content-Transfer-Encoding to use for this data,
 or null to indicate that an appropriate value should be chosen
 by the caller.

- 

  - 

### Method Detail

    - 

#### getEncoding

```
String getEncoding()
```

Return the MIME Content-Transfer-Encoding to use for this data,
 or null to indicate that an appropriate value should be chosen
 by the caller.

Returns:
the Content-Transfer-Encoding value, or null

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