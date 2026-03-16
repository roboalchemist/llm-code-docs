# Class Jackson2Tester<T>

java.lang.Object
org.springframework.boot.test.json.AbstractJsonMarshalTester<T>
org.springframework.boot.test.json.Jackson2Tester<T>

Type Parameters:
`T` - the type under test

---

@Deprecated(since="4.0.0",
            forRemoval=true)
public class Jackson2Tester<T>
extends AbstractJsonMarshalTester<T>
Deprecated, for removal: This API element is subject to removal in a future version.
since 4.0.0 for removal in 4.3.0 in favor of Jackson 3.

AssertJ based JSON tester backed by Jackson 2. Usually instantiated via
`initFields(Object, ObjectMapper)`, for example: 

```

public class ExampleObjectJsonTests {

    private Jackson2Tester<ExampleObject> json;

    @Before
    public void setup() {
        ObjectMapper objectMapper = new ObjectMapper();
        Jackson2Tester.initFields(this, objectMapper);
    }

    @Test
    public void testWriteJson() throws IOException {
        ExampleObject object = //...
        assertThat(json.write(object)).isEqualToJson("expected.json");
    }

}

```

See `AbstractJsonMarshalTester` for more details.

Since:
4.0.0

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class AbstractJsonMarshalTester

`AbstractJsonMarshalTester.FieldInitializer<M>`

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`Jackson2Tester(com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Deprecated, for removal: This API element is subject to removal in a future version.
Create a new `Jackson2Tester` instance.

` `
`Jackson2Tester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Deprecated, for removal: This API element is subject to removal in a future version.
Create a new `Jackson2Tester` instance.

` `
`Jackson2Tester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 com.fasterxml.jackson.databind.ObjectMapper objectMapper,
 @Nullable Class<?> view)`

Deprecated, for removal: This API element is subject to removal in a future version.
Create a new `Jackson2Tester` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`Jackson2Tester<T>`
`forView(Class<?> view)`

Deprecated, for removal: This API element is subject to removal in a future version.
Returns a new instance of `Jackson2Tester` with the view that should be used
for json serialization/deserialization.

`protected JsonContent<T>`
`getJsonContent(String json)`

Deprecated, for removal: This API element is subject to removal in a future version.
Factory method used to get a `JsonContent` instance from a source JSON
string.

`static void`
`initFields(Object testInstance,
 com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Deprecated, for removal: This API element is subject to removal in a future version.
Utility method to initialize `Jackson2Tester` fields.

`static void`
`initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<com.fasterxml.jackson.databind.ObjectMapper> objectMapperFactory)`

Deprecated, for removal: This API element is subject to removal in a future version.
Utility method to initialize `Jackson2Tester` fields.

`protected T`
`readObject(InputStream inputStream,
 org.springframework.core.ResolvableType type)`

Deprecated, for removal: This API element is subject to removal in a future version.
Read from the specified input stream to create an object of the specified type.

`protected T`
`readObject(Reader reader,
 org.springframework.core.ResolvableType type)`

Deprecated, for removal: This API element is subject to removal in a future version.
Read from the specified reader to create an object of the specified type.

`protected String`
`writeObject(T value,
 org.springframework.core.ResolvableType type)`

Deprecated, for removal: This API element is subject to removal in a future version.
Write the specified object to a JSON string.

### Methods inherited from class AbstractJsonMarshalTester

`getResourceLoadClass, getType, initialize, parse, parse, parseObject, parseObject, read, read, read, read, read, readObject, readObject, readObject, readObject, readObject, write`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Jackson2Tester

protected Jackson2Tester(com.fasterxml.jackson.databind.ObjectMapper objectMapper)
Deprecated, for removal: This API element is subject to removal in a future version.
Create a new `Jackson2Tester` instance.

Parameters:
`objectMapper` - the Jackson object mapper

  - 

### Jackson2Tester

public Jackson2Tester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 com.fasterxml.jackson.databind.ObjectMapper objectMapper)
Deprecated, for removal: This API element is subject to removal in a future version.
Create a new `Jackson2Tester` instance.

Parameters:
`resourceLoadClass` - the source class used to load resources
`type` - the type under test
`objectMapper` - the Jackson object mapper

  - 

### Jackson2Tester

public Jackson2Tester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 com.fasterxml.jackson.databind.ObjectMapper objectMapper,
 @Nullable Class<?> view)
Deprecated, for removal: This API element is subject to removal in a future version.
Create a new `Jackson2Tester` instance.

Parameters:
`resourceLoadClass` - the source class used to load resources
`type` - the type under test
`objectMapper` - the Jackson object mapper
`view` - the JSON view

- 

## Method Details

  - 

### getJsonContent

protected JsonContent<T> getJsonContent(String json)
Deprecated, for removal: This API element is subject to removal in a future version.
Description copied from class: `AbstractJsonMarshalTester`
Factory method used to get a `JsonContent` instance from a source JSON
string.

Overrides:
`getJsonContent` in class `AbstractJsonMarshalTester<T>`
Parameters:
`json` - the source JSON
Returns:
a new `JsonContent` instance

  - 

### readObject

protected T readObject(InputStream inputStream,
 org.springframework.core.ResolvableType type)
                throws IOException
Deprecated, for removal: This API element is subject to removal in a future version.
Description copied from class: `AbstractJsonMarshalTester`
Read from the specified input stream to create an object of the specified type. The
default implementation delegates to `AbstractJsonMarshalTester.readObject(Reader, ResolvableType)`.

Overrides:
`readObject` in class `AbstractJsonMarshalTester<T>`
Parameters:
`inputStream` - the source input stream (never `null`)
`type` - the resulting type (never `null`)
Returns:
the resulting object
Throws:
`IOException` - on read error

  - 

### readObject

protected T readObject(Reader reader,
 org.springframework.core.ResolvableType type)
                throws IOException
Deprecated, for removal: This API element is subject to removal in a future version.
Description copied from class: `AbstractJsonMarshalTester`
Read from the specified reader to create an object of the specified type.

Specified by:
`readObject` in class `AbstractJsonMarshalTester<T>`
Parameters:
`reader` - the source reader (never `null`)
`type` - the resulting type (never `null`)
Returns:
the resulting object
Throws:
`IOException` - on read error

  - 

### writeObject

protected String writeObject(T value,
 org.springframework.core.ResolvableType type)
                      throws IOException
Deprecated, for removal: This API element is subject to removal in a future version.
Description copied from class: `AbstractJsonMarshalTester`
Write the specified object to a JSON string.

Specified by:
`writeObject` in class `AbstractJsonMarshalTester<T>`
Parameters:
`value` - the source value (never `null`)
`type` - the resulting type (never `null`)
Returns:
the JSON string
Throws:
`IOException` - on write error

  - 

### initFields

public static void initFields(Object testInstance,
 com.fasterxml.jackson.databind.ObjectMapper objectMapper)
Deprecated, for removal: This API element is subject to removal in a future version.
Utility method to initialize `Jackson2Tester` fields. See
`class-level documentation` for example usage.

Parameters:
`testInstance` - the test instance
`objectMapper` - the JSON mapper
See Also:

    - `initFields(Object, ObjectMapper)`

  - 

### initFields

public static void initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<com.fasterxml.jackson.databind.ObjectMapper> objectMapperFactory)
Deprecated, for removal: This API element is subject to removal in a future version.
Utility method to initialize `Jackson2Tester` fields. See
`class-level documentation` for example usage.

Parameters:
`testInstance` - the test instance
`objectMapperFactory` - a factory to create the object mapper
See Also:

    - `initFields(Object, ObjectMapper)`

  - 

### forView

public Jackson2Tester<T> forView(Class<?> view)
Deprecated, for removal: This API element is subject to removal in a future version.
Returns a new instance of `Jackson2Tester` with the view that should be used
for json serialization/deserialization.

Parameters:
`view` - the view class
Returns:
the new instance