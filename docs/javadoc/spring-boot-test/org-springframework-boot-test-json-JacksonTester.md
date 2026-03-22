# Class JacksonTester<T>

java.lang.Object
org.springframework.boot.test.json.AbstractJsonMarshalTester<T>
org.springframework.boot.test.json.JacksonTester<T>

Type Parameters:
`T` - the type under test

---

public class JacksonTester<T>
extends AbstractJsonMarshalTester<T>
AssertJ based JSON tester backed by Jackson. Usually instantiated via
`initFields(Object, JsonMapper)`, for example: 

```

public class ExampleObjectJsonTests {

    private JacksonTester<ExampleObject> json;

    @Before
    public void setup() {
        JsonMapper jsonMapper = new JsonMapper();
        JacksonTester.initFields(this, jsonMapper);
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
1.4.0

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
` `
`JacksonTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 tools.jackson.databind.json.JsonMapper jsonMapper)`

Create a new `JacksonTester` instance.

` `
`JacksonTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 tools.jackson.databind.json.JsonMapper jsonMapper,
 @Nullable Class<?> view)`

Create a new `JacksonTester` instance.

`protected `
`JacksonTester(tools.jackson.databind.json.JsonMapper jsonMapper)`

Create a new `JacksonTester` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`JacksonTester<T>`
`forView(Class<?> view)`

Returns a new instance of `JacksonTester` with the view that should be used
for json serialization/deserialization.

`protected JsonContent<T>`
`getJsonContent(String json)`

Factory method used to get a `JsonContent` instance from a source JSON
string.

`static void`
`initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<tools.jackson.databind.json.JsonMapper> jsonMapperFactory)`

Utility method to initialize `JacksonTester` fields.

`static void`
`initFields(Object testInstance,
 tools.jackson.databind.json.JsonMapper jsonMapper)`

Utility method to initialize `JacksonTester` fields.

`protected T`
`readObject(InputStream inputStream,
 org.springframework.core.ResolvableType type)`

Read from the specified input stream to create an object of the specified type.

`protected T`
`readObject(Reader reader,
 org.springframework.core.ResolvableType type)`

Read from the specified reader to create an object of the specified type.

`protected String`
`writeObject(T value,
 org.springframework.core.ResolvableType type)`

Write the specified object to a JSON string.

### Methods inherited from class AbstractJsonMarshalTester

`getResourceLoadClass, getType, initialize, parse, parse, parseObject, parseObject, read, read, read, read, read, readObject, readObject, readObject, readObject, readObject, write`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### JacksonTester

protected JacksonTester(tools.jackson.databind.json.JsonMapper jsonMapper)
Create a new `JacksonTester` instance.

Parameters:
`jsonMapper` - the Jackson JSON mapper
Since:
4.0.0

  - 

### JacksonTester

public JacksonTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 tools.jackson.databind.json.JsonMapper jsonMapper)
Create a new `JacksonTester` instance.

Parameters:
`resourceLoadClass` - the source class used to load resources
`type` - the type under test
`jsonMapper` - the Jackson JSON mapper
Since:
4.0.0

  - 

### JacksonTester

public JacksonTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 tools.jackson.databind.json.JsonMapper jsonMapper,
 @Nullable Class<?> view)
Create a new `JacksonTester` instance.

Parameters:
`resourceLoadClass` - the source class used to load resources
`type` - the type under test
`jsonMapper` - the Jackson JSON mapper
`view` - the JSON view
Since:
4.0.0

- 

## Method Details

  - 

### getJsonContent

protected JsonContent<T> getJsonContent(String json)
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
 tools.jackson.databind.json.JsonMapper jsonMapper)
Utility method to initialize `JacksonTester` fields. See `class-level documentation` for example usage.

Parameters:
`testInstance` - the test instance
`jsonMapper` - the JSON mapper
Since:
4.0.0
See Also:

    - `initFields(Object, JsonMapper)`

  - 

### initFields

public static void initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<tools.jackson.databind.json.JsonMapper> jsonMapperFactory)
Utility method to initialize `JacksonTester` fields. See `class-level documentation` for example usage.

Parameters:
`testInstance` - the test instance
`jsonMapperFactory` - a factory to create the JSON mapper
Since:
4.0.0
See Also:

    - `initFields(Object, JsonMapper)`

  - 

### forView

public JacksonTester<T> forView(Class<?> view)
Returns a new instance of `JacksonTester` with the view that should be used
for json serialization/deserialization.

Parameters:
`view` - the view class
Returns:
the new instance