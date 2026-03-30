# Class JsonbTester<T>

java.lang.Object
org.springframework.boot.test.json.AbstractJsonMarshalTester<T>
org.springframework.boot.test.json.JsonbTester<T>

Type Parameters:
`T` - the type under test

---

public class JsonbTester<T>
extends AbstractJsonMarshalTester<T>
AssertJ based JSON tester backed by Jsonb. Usually instantiated via
`initFields(Object, Jsonb)`, for example: 

```

public class ExampleObjectJsonTests {

        private JsonbTester<ExampleObject> json;

        @Before
        public void setup() {
                Jsonb jsonb = JsonbBuilder.create();
                JsonbTester.initFields(this, jsonb);
        }

        @Test
        public void testWriteJson() throws IOException {
                ExampleObject object = // ...
                assertThat(json.write(object)).isEqualToJson("expected.json");
        }

}

```

See `AbstractJsonMarshalTester` for more details.

Since:
2.0.0

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
`JsonbTester(jakarta.json.bind.Jsonb jsonb)`

Create a new uninitialized `JsonbTester` instance.

` `
`JsonbTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 jakarta.json.bind.Jsonb jsonb)`

Create a new `JsonbTester` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`static void`
`initFields(Object testInstance,
 jakarta.json.bind.Jsonb jsonb)`

Utility method to initialize `JsonbTester` fields.

`static void`
`initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<jakarta.json.bind.Jsonb> jsonb)`

Utility method to initialize `JsonbTester` fields.

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

### JsonbTester

protected JsonbTester(jakarta.json.bind.Jsonb jsonb)
Create a new uninitialized `JsonbTester` instance.

Parameters:
`jsonb` - the Jsonb instance

  - 

### JsonbTester

public JsonbTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type,
 jakarta.json.bind.Jsonb jsonb)
Create a new `JsonbTester` instance.

Parameters:
`resourceLoadClass` - the source class used to load resources
`type` - the type under test
`jsonb` - the Jsonb instance
See Also:

    - `initFields(Object, Jsonb)`

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
 jakarta.json.bind.Jsonb jsonb)
Utility method to initialize `JsonbTester` fields. See `class-level documentation` for example usage.

Parameters:
`testInstance` - the test instance
`jsonb` - the Jsonb instance

  - 

### initFields

public static void initFields(Object testInstance,
 org.springframework.beans.factory.ObjectFactory<jakarta.json.bind.Jsonb> jsonb)
Utility method to initialize `JsonbTester` fields. See `class-level documentation` for example usage.

Parameters:
`testInstance` - the test instance
`jsonb` - an object factory to create the Jsonb instance