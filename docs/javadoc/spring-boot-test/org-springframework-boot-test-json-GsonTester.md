# Class GsonTester<T>

java.lang.Object
org.springframework.boot.test.json.AbstractJsonMarshalTester<T>
org.springframework.boot.test.json.GsonTester<T>

Type Parameters:
`T` - the type under test

---

public class GsonTester<T>
extends AbstractJsonMarshalTester<T>
AssertJ based JSON tester backed by Gson. Usually instantiated via
`initFields(Object, Gson)`, for example: 

```

public class ExampleObjectJsonTests {

    private GsonTester<ExampleObject> json;

    @Before
    public void setup() {
        Gson gson = new GsonBuilder().create();
        GsonTester.initFields(this, gson);
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
`protected `
`GsonTester(com.google.gson.Gson gson)`

Create a new uninitialized `GsonTester` instance.

` `
`GsonTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 com.google.gson.Gson gson)`

Create a new `GsonTester` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`static void`
`initFields(Object testInstance,
 com.google.gson.Gson gson)`

Utility method to initialize `GsonTester` fields.

`static void`
`initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<com.google.gson.Gson> gson)`

Utility method to initialize `GsonTester` fields.

`protected T`
`readObject(Reader reader,
 org.springframework.core.ResolvableType type)`

Read from the specified reader to create an object of the specified type.

`protected String`
`writeObject(T value,
 org.springframework.core.ResolvableType type)`

Write the specified object to a JSON string.

### Methods inherited from class AbstractJsonMarshalTester

`getJsonContent, getResourceLoadClass, getType, initialize, parse, parse, parseObject, parseObject, read, read, read, read, read, readObject, readObject, readObject, readObject, readObject, readObject, write`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### GsonTester

protected GsonTester(com.google.gson.Gson gson)
Create a new uninitialized `GsonTester` instance.

Parameters:
`gson` - the Gson instance

  - 

### GsonTester

public GsonTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 com.google.gson.Gson gson)
Create a new `GsonTester` instance.

Parameters:
`resourceLoadClass` - the source class used to load resources
`type` - the type under test
`gson` - the Gson instance
See Also:

    - `initFields(Object, Gson)`

- 

## Method Details

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

### initFields

public static void initFields(Object testInstance,
 com.google.gson.Gson gson)
Utility method to initialize `GsonTester` fields. See `class-level documentation` for example usage.

Parameters:
`testInstance` - the test instance
`gson` - the Gson instance

  - 

### initFields

public static void initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<com.google.gson.Gson> gson)
Utility method to initialize `GsonTester` fields. See `class-level documentation` for example usage.

Parameters:
`testInstance` - the test instance
`gson` - an object factory to create the Gson instance