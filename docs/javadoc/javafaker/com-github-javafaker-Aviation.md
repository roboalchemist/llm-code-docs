Package com.github.javafaker

## Class Aviation

- java.lang.Object

- 

  - com.github.javafaker.Aviation

- 

---

```
public class Aviation
extends java.lang.Object
```

Generates aviation related strings.

- 

  - 

### Constructor Summary

Constructors 

Modifier
Constructor
Description

`protected `
`Aviation​(Faker faker)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`java.lang.String`
`aircraft()`
 

`java.lang.String`
`airport()`

Returns an airport ICAO code.

`java.lang.String`
`METAR()`

Provides a METAR weather report.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Aviation

```
protected Aviation​(Faker faker)
```

  - 

### Method Detail

    - 

#### aircraft

```
public java.lang.String aircraft()
```

Returns:
some aircraft name/model/make e.g. "An-2".

    - 

#### airport

```
public java.lang.String airport()
```

Returns an airport ICAO code.
 See also: https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_A

    - 

#### METAR

```
public java.lang.String METAR()
```

Provides a METAR weather report.
 Have a look at https://en.wikipedia.org/wiki/METAR