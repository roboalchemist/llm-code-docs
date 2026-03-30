Package com.github.javafaker

## Class Internet

- java.lang.Object

- 

  - com.github.javafaker.Internet

- 

---

```
public class Internet
extends java.lang.Object
```

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class
Description

`static class `
`Internet.UserAgent`
 

  - 

### Constructor Summary

Constructors 

Modifier
Constructor
Description

`protected `
`Internet​(Faker faker)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`java.lang.String`
`avatar()`

Generates a random avatar url based on a collection of profile pictures of real people.

`java.lang.String`
`domainName()`
 

`java.lang.String`
`domainSuffix()`
 

`java.lang.String`
`domainWord()`
 

`java.lang.String`
`emailAddress()`
 

`java.lang.String`
`emailAddress​(java.lang.String localPart)`
 

`java.lang.String`
`image()`

Generates a random image url based on the lorempixel service.

`java.lang.String`
`image​(java.lang.Integer width,
     java.lang.Integer height,
     java.lang.Boolean gray,
     java.lang.String text)`

Same as image() but allows client code to choose a few image characteristics

`java.lang.String`
`ipV4Address()`

returns an IPv4 address in dot separated octets.

`java.lang.String`
`ipV4Cidr()`
 

`java.lang.String`
`ipV6Address()`

Returns an IPv6 address in hh:hh:hh:hh:hh:hh:hh:hh format.

`java.lang.String`
`ipV6Cidr()`
 

`java.lang.String`
`macAddress()`
 

`java.lang.String`
`macAddress​(java.lang.String prefix)`

Returns a MAC address in the following format: 6-bytes in MM:MM:MM:SS:SS:SS format.

`java.lang.String`
`password()`
 

`java.lang.String`
`password​(boolean includeDigit)`
 

`java.lang.String`
`password​(int minimumLength,
        int maximumLength)`
 

`java.lang.String`
`password​(int minimumLength,
        int maximumLength,
        boolean includeUppercase)`
 

`java.lang.String`
`password​(int minimumLength,
        int maximumLength,
        boolean includeUppercase,
        boolean includeSpecial)`
 

`java.lang.String`
`password​(int minimumLength,
        int maximumLength,
        boolean includeUppercase,
        boolean includeSpecial,
        boolean includeDigit)`
 

`java.lang.String`
`privateIpV4Address()`
 

`java.lang.String`
`publicIpV4Address()`
 

`java.lang.String`
`safeEmailAddress()`
 

`java.lang.String`
`safeEmailAddress​(java.lang.String localPart)`
 

`java.lang.String`
`slug()`
 

`java.lang.String`
`slug​(java.util.List<java.lang.String> wordsOrNull,
    java.lang.String glueOrNull)`
 

`java.lang.String`
`url()`
 

`java.lang.String`
`userAgent​(Internet.UserAgent userAgent)`
 

`java.lang.String`
`userAgentAny()`
 

`java.lang.String`
`uuid()`

Returns a UUID (type 4) as String.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Internet

```
protected Internet​(Faker faker)
```

  - 

### Method Detail

    - 

#### emailAddress

```
public java.lang.String emailAddress()
```

    - 

#### emailAddress

```
public java.lang.String emailAddress​(java.lang.String localPart)
```

    - 

#### safeEmailAddress

```
public java.lang.String safeEmailAddress()
```

    - 

#### safeEmailAddress

```
public java.lang.String safeEmailAddress​(java.lang.String localPart)
```

    - 

#### domainName

```
public java.lang.String domainName()
```

    - 

#### domainWord

```
public java.lang.String domainWord()
```

    - 

#### domainSuffix

```
public java.lang.String domainSuffix()
```

    - 

#### url

```
public java.lang.String url()
```

    - 

#### avatar

```
public java.lang.String avatar()
```

Generates a random avatar url based on a collection of profile pictures of real people. All this avatar have been
 authorized by its awesome users to be used on live websites (not just mockups). For more information, please
 visit: http://uifaces.com/authorized

Returns:
an url to a random avatar image.
See Also:
Authorized UI Faces

    - 

#### image

```
public java.lang.String image()
```

Generates a random image url based on the lorempixel service. All the images provided by this service are released
 under the creative commons license (CC BY-SA). For more information, please visit: http://lorempixel.com/

Returns:
an url to a random image.
See Also:
lorempixel - Placeholder Images for every case

    - 

#### image

```
public java.lang.String image​(java.lang.Integer width,
                              java.lang.Integer height,
                              java.lang.Boolean gray,
                              java.lang.String text)
```

Same as image() but allows client code to choose a few image characteristics

Parameters:
`width` - the image width
`height` - the image height
`gray` - true for gray image and false for color image
`text` - optional custom text on the selected picture
Returns:
an url to a random image with the given characteristics.

    - 

#### password

```
public java.lang.String password()
```

    - 

#### password

```
public java.lang.String password​(boolean includeDigit)
```

    - 

#### password

```
public java.lang.String password​(int minimumLength,
                                 int maximumLength)
```

    - 

#### password

```
public java.lang.String password​(int minimumLength,
                                 int maximumLength,
                                 boolean includeUppercase)
```

    - 

#### password

```
public java.lang.String password​(int minimumLength,
                                 int maximumLength,
                                 boolean includeUppercase,
                                 boolean includeSpecial)
```

    - 

#### password

```
public java.lang.String password​(int minimumLength,
                                 int maximumLength,
                                 boolean includeUppercase,
                                 boolean includeSpecial,
                                 boolean includeDigit)
```

    - 

#### macAddress

```
public java.lang.String macAddress​(java.lang.String prefix)
```

Returns a MAC address in the following format: 6-bytes in MM:MM:MM:SS:SS:SS format.

Parameters:
`prefix` - a prefix to put on the front of the address
Returns:
a correctly formatted MAC address

    - 

#### macAddress

```
public java.lang.String macAddress()
```

See Also:
`macAddress(String)`

    - 

#### ipV4Address

```
public java.lang.String ipV4Address()
```

returns an IPv4 address in dot separated octets.

Returns:
a correctly formatted IPv4 address.

    - 

#### privateIpV4Address

```
public java.lang.String privateIpV4Address()
```

Returns:
a valid private IPV4 address in dot notation

    - 

#### publicIpV4Address

```
public java.lang.String publicIpV4Address()
```

Returns:
a valid public IPV4 address in dot notation

    - 

#### ipV4Cidr

```
public java.lang.String ipV4Cidr()
```

Returns:
a valid IPV4 CIDR

    - 

#### ipV6Address

```
public java.lang.String ipV6Address()
```

Returns an IPv6 address in hh:hh:hh:hh:hh:hh:hh:hh format.

Returns:
a correctly formatted IPv6 address.

    - 

#### ipV6Cidr

```
public java.lang.String ipV6Cidr()
```

Returns:
a valid IPV6 CIDR

    - 

#### slug

```
public java.lang.String slug()
```

Returns:
a slug using '_' as the word separator and two `Lorem` words as the values

    - 

#### slug

```
public java.lang.String slug​(java.util.List<java.lang.String> wordsOrNull,
                             java.lang.String glueOrNull)
```

Parameters:
`wordsOrNull` - if null, then 2 `Lorem` words
`glueOrNull` - if null, "_"
Returns:
a slug string combining wordsOrNull with glueOrNull (ex. x_y)

    - 

#### uuid

```
public java.lang.String uuid()
```

Returns a UUID (type 4) as String.

Returns:
A UUID as String.

    - 

#### userAgent

```
public java.lang.String userAgent​(Internet.UserAgent userAgent)
```

    - 

#### userAgentAny

```
public java.lang.String userAgentAny()
```