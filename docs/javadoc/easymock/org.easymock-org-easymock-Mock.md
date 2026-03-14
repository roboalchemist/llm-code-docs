Module org.easymock
Package org.easymock

## Annotation Type Mock

- 

---

```
@Target({FIELD,ANNOTATION_TYPE})
@Retention(RUNTIME)
@Documented
public @interface Mock
```

Annotation to set on a field so that `EasyMockRunner`, `EasyMockRule` or `EasyMockSupport.injectMocks(Object)`
 will inject a mock to it.
 

 Doing

 `@Mock private MyClass mock;`

 is strictly identical to doing

 `private MyClass mock = createMock(MyClass.class);`

Since:
3.2
Author:
Henri Tremblay

- 

  - 

### Optional Element Summary

Optional Elements 

Modifier and Type
Optional Element
Description

`String`
`fieldName`

Name of the test subject field to which this mock will be assigned.

`String`
`name`
 

`MockType`
`type`
 

`MockType`
`value`
 

- 

  - 

### Element Detail

    - 

#### value

```
MockType value
```

Returns:
type of mock to create. It is an alias of `type()`
Since:
3.5

Default:
org.easymock.MockType.DEFAULT

  - 

    - 

#### type

```
MockType type
```

Returns:
type of mock to create

Default:
org.easymock.MockType.DEFAULT

  - 

    - 

#### name

```
String name
```

Returns:
name of the mock to be created. By default, it is the "EasyMock for field TypeName.fieldName

Default:
""

  - 

    - 

#### fieldName

```
String fieldName
```

Name of the test subject field to which this mock will be assigned. Use to disambiguate the case where a mock may be assigned to multiple fields of the same type.
 When set, this mock will be assigned to the given field name in any test subject with a matching field name.
 If not set, injection is to all type-compatible fields in all test subjects.
 A given field name may only be used once, and there must be a matching field in at least one test subject.

Returns:
name of the field to inject to

Default:
""