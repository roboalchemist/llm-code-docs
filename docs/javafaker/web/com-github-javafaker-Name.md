Package com.github.javafaker

## Class Name

- java.lang.Object

- 

  - com.github.javafaker.Name

- 

---

```
public class Name
extends java.lang.Object
```

- 

  - 

### Constructor Summary

Constructors 

Modifier
Constructor
Description

`protected `
`Name​(Faker faker)`

Internal constructor, not to be used by clients.

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`java.lang.String`
`bloodGroup()`

Returns a blood group such as Oâ, O+, A-, A+, B-, B+, AB-, AB+

`java.lang.String`
`firstName()`

Returns a random 'given' name such as Aaliyah, Aaron, Abagail or Abbey

`java.lang.String`
`fullName()`

Returns the same value as `name()`

`java.lang.String`
`lastName()`

Returns a random last name such as Smith, Jones or Baldwin

`java.lang.String`
`name()`

      A multipart name composed of an optional prefix, a firstname and a lastname
      or other possible variances based on locale.

`java.lang.String`
`nameWithMiddle()`

      A multipart name composed of an optional prefix, a given and family name,
      another 'firstname' for the middle name and an optional suffix such as Jr.

`java.lang.String`
`prefix()`

Returns a name prefix such as Mr., Mrs., Ms., Miss, or Dr.

`java.lang.String`
`suffix()`

Returns a name suffix such as Jr., Sr., I, II, III, IV, V, MD, DDS, PhD or DVM

`java.lang.String`
`title()`

     A three part title composed of a descriptor level and job.

`java.lang.String`
`username()`

     A lowercase username composed of the first_name and last_name joined with a '.'.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Name

```
protected Name​(Faker faker)
```

Internal constructor, not to be used by clients.  Instances of `Name` should be accessed via 
 `Faker.name()`.

  - 

### Method Detail

    - 

#### name

```
public java.lang.String name()
```

      A multipart name composed of an optional prefix, a firstname and a lastname
      or other possible variances based on locale.  Examples:
      

          
      - James Jones Jr.
          
      - Julie Johnson
      

 

Returns:
a random name with given and family names and an optional suffix.

    - 

#### nameWithMiddle

```
public java.lang.String nameWithMiddle()
```

      A multipart name composed of an optional prefix, a given and family name,
      another 'firstname' for the middle name and an optional suffix such as Jr. 
      Examples:
      

          
      - Mrs. Ella Geraldine Fitzgerald
          
      - Jason Tom Sawyer Jr.
          
      - Helen Jessica Troy
      

 

Returns:
a random name with a middle name component with optional prefix and suffix

    - 

#### fullName

```
public java.lang.String fullName()
```

Returns the same value as `name()`

See Also:
`name()`

    - 

#### firstName

```
public java.lang.String firstName()
```

Returns a random 'given' name such as Aaliyah, Aaron, Abagail or Abbey

Returns:
a 'given' name such as Aaliyah, Aaron, Abagail or Abbey

    - 

#### lastName

```
public java.lang.String lastName()
```

Returns a random last name such as Smith, Jones or Baldwin

Returns:
a random last name such as Smith, Jones or Baldwin

    - 

#### prefix

```
public java.lang.String prefix()
```

Returns a name prefix such as Mr., Mrs., Ms., Miss, or Dr.

Returns:
a name prefix such as Mr., Mrs., Ms., Miss, or Dr.

    - 

#### suffix

```
public java.lang.String suffix()
```

Returns a name suffix such as Jr., Sr., I, II, III, IV, V, MD, DDS, PhD or DVM

Returns:
a name suffix such as Jr., Sr., I, II, III, IV, V, MD, DDS, PhD or DVM

    - 

#### title

```
public java.lang.String title()
```

     A three part title composed of a descriptor level and job.  Some examples are :
     

         
      - (template) {descriptor} {level} {job}
         
      - Lead Solutions Specialist
         
      - National Marketing Manager
         
      - Central Response Liaison
     

 

Returns:
a random three part job title

    - 

#### username

```
public java.lang.String username()
```

     A lowercase username composed of the first_name and last_name joined with a '.'. Some examples are:
     

         
      - (template) `firstName()`.`lastName()`
         
      - jim.jones
         
      - jason.leigh
         
      - tracy.jordan
     

 

Returns:
a random two part user name.
See Also:
`firstName()`, 
`lastName()`

    - 

#### bloodGroup

```
public java.lang.String bloodGroup()
```

Returns a blood group such as Oâ, O+, A-, A+, B-, B+, AB-, AB+

Returns:
a blood group such as Oâ, O+, A-, A+, B-, B+, AB-, AB+