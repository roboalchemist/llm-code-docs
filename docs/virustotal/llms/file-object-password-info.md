# Source: https://virustotal.readme.io/reference/file-object-password-info.md

# password_info

Information from password protected files

`password_info` returns hashcat data from Microsoft Office files. It contains the following attributes:

* `type`: <*string*> type of returned value. It can only be "hashcat".
* `value`: <*string*> hashcat value.

```json password information
{
  "data": {
        ...
    "attributes" : {
      ...
      "password_info": {
        "type": "<string>",
        "value": "<string>"
      }
    }
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "password_info": {
        "type": "hashcat",
        "value": "$office$*2007*20*128*16*56c7195598b191101f3721dbf1ebe367*131bf49e0b5315f0c2c387d1a62c3360*e820170b1338525454b1ee95ddf9f2c40ae5111d"
      }
    }
  }
}
```