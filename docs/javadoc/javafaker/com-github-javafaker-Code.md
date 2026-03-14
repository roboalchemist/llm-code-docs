Package com.github.javafaker

## Class Code

- java.lang.Object

- 

  - com.github.javafaker.Code

- 

---

```
public class Code
extends java.lang.Object
```

ISBN Rules : https://en.wikipedia.org/wiki/International_Standard_Book_Number

- 

  - 

### Constructor Summary

Constructors 

Modifier
Constructor
Description

`protected `
`Code​(Faker faker)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`java.lang.String`
`asin()`
 

`java.lang.String`
`ean13()`
 

`java.lang.String`
`ean8()`
 

`java.lang.String`
`gtin13()`
 

`java.lang.String`
`gtin8()`
 

`java.lang.String`
`imei()`
 

`java.lang.String`
`isbn10()`
 

`java.lang.String`
`isbn10​(boolean separator)`
 

`java.lang.String`
`isbn13()`
 

`java.lang.String`
`isbn13​(boolean separator)`
 

`java.lang.String`
`isbnGroup()`

This can be overridden by specifying
 `
     code:
       isbn_group: "some expression"
 `
 in the appropriate yml file.

`java.lang.String`
`isbnGs1()`

This can be overridden by specifying
 `
     code:
       isbn_gs1: "some expression"
 `
 in the appropriate yml file.

`java.lang.String`
`isbnRegistrant()`

This can be overridden by specifying
 `
     code:
       isbn_registrant: "some expression"
 `
 in the appropriate yml file.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Code

```
protected Code​(Faker faker)
```

  - 

### Method Detail

    - 

#### isbnGs1

```
public java.lang.String isbnGs1()
```

This can be overridden by specifying
 `
     code:
       isbn_gs1: "some expression"
 `
 in the appropriate yml file.

Returns:
a GS1 code for an ISBN13, currently is only 978 and 979

    - 

#### isbnGroup

```
public java.lang.String isbnGroup()
```

This can be overridden by specifying
 `
     code:
       isbn_group: "some expression"
 `
 in the appropriate yml file.

Returns:
an ISBN group number

    - 

#### isbnRegistrant

```
public java.lang.String isbnRegistrant()
```

This can be overridden by specifying
 `
     code:
       isbn_registrant: "some expression"
 `
 in the appropriate yml file.

Returns:
an ISBN registrant 'element' with separator

    - 

#### isbn10

```
public java.lang.String isbn10()
```

Returns:
a valid ISBN10 number with no separators (ex. 9604250590)

    - 

#### isbn10

```
public java.lang.String isbn10​(boolean separator)
```

Parameters:
`separator` - true if you want separators returned, false otherwise
Returns:
a valid ISBN10 number with or without separators (ex. 9604250590, 960-425-059-0)

    - 

#### isbn13

```
public java.lang.String isbn13()
```

Returns:
a valid ISBN13 number with no separators (ex. 9789604250590)

    - 

#### isbn13

```
public java.lang.String isbn13​(boolean separator)
```

Parameters:
`separator` - true if you want separators returned, false otherwise
Returns:
a valid ISBN13 number with or without separators (ex. 9789604250590, 978-960-425-059-0)

    - 

#### asin

```
public java.lang.String asin()
```

    - 

#### imei

```
public java.lang.String imei()
```

    - 

#### ean8

```
public java.lang.String ean8()
```

    - 

#### gtin8

```
public java.lang.String gtin8()
```

    - 

#### ean13

```
public java.lang.String ean13()
```

    - 

#### gtin13

```
public java.lang.String gtin13()
```