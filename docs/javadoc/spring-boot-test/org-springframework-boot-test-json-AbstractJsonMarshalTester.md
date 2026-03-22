# Class AbstractJsonMarshalTester<T>

java.lang.Object
org.springframework.boot.test.json.AbstractJsonMarshalTester<T>

Type Parameters:
`T` - the type under test

Direct Known Subclasses:
`GsonTester, Jackson2Tester, JacksonTester, JsonbTester`

---

public abstract class AbstractJsonMarshalTester<T>
extends Object
Base class for AssertJ based JSON marshal testers. Exposes specific Asserts following a
`read`, `write` or `parse` of JSON content. Typically used in
combination with an AssertJ `assertThat` call. For example:

```

public class ExampleObjectJsonTests {

    private AbstractJsonTester<ExampleObject> json = //...

    @Test
    public void testWriteJson() {
        ExampleObject object = //...
        assertThat(json.write(object)).isEqualToJson("expected.json");
        assertThat(json.read("expected.json")).isEqualTo(object);
    }

}

```

For a complete list of supported assertions see `JsonContentAssert` and
`ObjectContentAssert`.

To use this library JSONAssert must be on the test classpath.

Since:
1.4.0
See Also:

- `JsonContentAssert`

- `ObjectContentAssert`

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`protected static class `
`AbstractJsonMarshalTester.FieldInitializer<M>`

Utility class used to support field initialization.

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`AbstractJsonMarshalTester()`

Create a new uninitialized `AbstractJsonMarshalTester` instance.

` `
`AbstractJsonMarshalTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type)`

Create a new `AbstractJsonMarshalTester` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`protected JsonContent<T>`
`getJsonContent(String json)`

Factory method used to get a `JsonContent` instance from a source JSON
string.

`protected final @Nullable Class<?>`
`getResourceLoadClass()`

Return class used to load relative resources.

`protected final @Nullable org.springframework.core.ResolvableType`
`getType()`

Return the type under test.

`protected final void`
`initialize(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type)`

Initialize the marshal tester for use.

`ObjectContent<T>`
`parse(byte[] jsonBytes)`

Return `ObjectContent` from parsing the specific JSON bytes.

`ObjectContent<T>`
`parse(String jsonString)`

Return `ObjectContent` from parsing the specific JSON String.

`T`
`parseObject(byte[] jsonBytes)`

Return the object created from parsing the specific JSON bytes.

`T`
`parseObject(String jsonString)`

Return the object created from parsing the specific JSON String.

`ObjectContent<T>`
`read(File file)`

Return `ObjectContent` from reading from the specified file.

`ObjectContent<T>`
`read(InputStream inputStream)`

Return `ObjectContent` from reading from the specified input stream.

`ObjectContent<T>`
`read(Reader reader)`

Return `ObjectContent` from reading from the specified reader.

`ObjectContent<T>`
`read(String resourcePath)`

Return `ObjectContent` from reading from the specified classpath resource.

`ObjectContent<T>`
`read(org.springframework.core.io.Resource resource)`

Return `ObjectContent` from reading from the specified resource.

`T`
`readObject(File file)`

Return the object created from reading from the specified file.

`T`
`readObject(InputStream inputStream)`

Return the object created from reading from the specified input stream.

`protected T`
`readObject(InputStream inputStream,
 org.springframework.core.ResolvableType type)`

Read from the specified input stream to create an object of the specified type.

`T`
`readObject(Reader reader)`

Return the object created from reading from the specified reader.

`protected abstract T`
`readObject(Reader reader,
 org.springframework.core.ResolvableType type)`

Read from the specified reader to create an object of the specified type.

`T`
`readObject(String resourcePath)`

Return the object created from reading from the specified classpath resource.

`T`
`readObject(org.springframework.core.io.Resource resource)`

Return the object created from reading from the specified resource.

`JsonContent<T>`
`write(T value)`

Return `JsonContent` from writing the specific value.

`protected abstract String`
`writeObject(T value,
 org.springframework.core.ResolvableType type)`

Write the specified object to a JSON string.

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### AbstractJsonMarshalTester

protected AbstractJsonMarshalTester()
Create a new uninitialized `AbstractJsonMarshalTester` instance.

  - 

### AbstractJsonMarshalTester

public AbstractJsonMarshalTester(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type)
Create a new `AbstractJsonMarshalTester` instance.

Parameters:
`resourceLoadClass` - the source class used when loading relative classpath
resources
`type` - the type under test

- 

## Method Details

  - 

### initialize

protected final void initialize(Class<?> resourceLoadClass,
 org.springframework.core.ResolvableType type)
Initialize the marshal tester for use.

Parameters:
`resourceLoadClass` - the source class used when loading relative classpath
resources
`type` - the type under test

  - 

### getType

protected final @Nullable org.springframework.core.ResolvableType getType()
Return the type under test.

Returns:
the type under test

  - 

### getResourceLoadClass

protected final @Nullable Class<?> getResourceLoadClass()
Return class used to load relative resources.

Returns:
the resource load class

  - 

### write

public JsonContent<T> write(T value)
                     throws IOException
Return `JsonContent` from writing the specific value.

Parameters:
`value` - the value to write
Returns:
the `JsonContent`
Throws:
`IOException` - on write error

  - 

### getJsonContent

protected JsonContent<T> getJsonContent(String json)
Factory method used to get a `JsonContent` instance from a source JSON
string.

Parameters:
`json` - the source JSON
Returns:
a new `JsonContent` instance
Since:
2.1.5

  - 

### parseObject

public T parseObject(byte[] jsonBytes)
              throws IOException
Return the object created from parsing the specific JSON bytes.

Parameters:
`jsonBytes` - the source JSON bytes
Returns:
the resulting object
Throws:
`IOException` - on parse error

  - 

### parse

public ObjectContent<T> parse(byte[] jsonBytes)
                       throws IOException
Return `ObjectContent` from parsing the specific JSON bytes.

Parameters:
`jsonBytes` - the source JSON bytes
Returns:
the `ObjectContent`
Throws:
`IOException` - on parse error

  - 

### parseObject

public T parseObject(String jsonString)
              throws IOException
Return the object created from parsing the specific JSON String.

Parameters:
`jsonString` - the source JSON string
Returns:
the resulting object
Throws:
`IOException` - on parse error

  - 

### parse

public ObjectContent<T> parse(String jsonString)
                       throws IOException
Return `ObjectContent` from parsing the specific JSON String.

Parameters:
`jsonString` - the source JSON string
Returns:
the `ObjectContent`
Throws:
`IOException` - on parse error

  - 

### readObject

public T readObject(String resourcePath)
             throws IOException
Return the object created from reading from the specified classpath resource.

Parameters:
`resourcePath` - the source resource path. May be a full path or a path relative
to the `resourceLoadClass` passed to the constructor
Returns:
the resulting object
Throws:
`IOException` - on read error

  - 

### read

public ObjectContent<T> read(String resourcePath)
                      throws IOException
Return `ObjectContent` from reading from the specified classpath resource.

Parameters:
`resourcePath` - the source resource path. May be a full path or a path relative
to the `resourceLoadClass` passed to the constructor
Returns:
the `ObjectContent`
Throws:
`IOException` - on read error

  - 

### readObject

public T readObject(File file)
             throws IOException
Return the object created from reading from the specified file.

Parameters:
`file` - the source file
Returns:
the resulting object
Throws:
`IOException` - on read error

  - 

### read

public ObjectContent<T> read(File file)
                      throws IOException
Return `ObjectContent` from reading from the specified file.

Parameters:
`file` - the source file
Returns:
the `ObjectContent`
Throws:
`IOException` - on read error

  - 

### readObject

public T readObject(InputStream inputStream)
             throws IOException
Return the object created from reading from the specified input stream.

Parameters:
`inputStream` - the source input stream
Returns:
the resulting object
Throws:
`IOException` - on read error

  - 

### read

public ObjectContent<T> read(InputStream inputStream)
                      throws IOException
Return `ObjectContent` from reading from the specified input stream.

Parameters:
`inputStream` - the source input stream
Returns:
the `ObjectContent`
Throws:
`IOException` - on read error

  - 

### readObject

public T readObject(org.springframework.core.io.Resource resource)
             throws IOException
Return the object created from reading from the specified resource.

Parameters:
`resource` - the source resource
Returns:
the resulting object
Throws:
`IOException` - on read error

  - 

### read

public ObjectContent<T> read(org.springframework.core.io.Resource resource)
                      throws IOException
Return `ObjectContent` from reading from the specified resource.

Parameters:
`resource` - the source resource
Returns:
the `ObjectContent`
Throws:
`IOException` - on read error

  - 

### readObject

public T readObject(Reader reader)
             throws IOException
Return the object created from reading from the specified reader.

Parameters:
`reader` - the source reader
Returns:
the resulting object
Throws:
`IOException` - on read error

  - 

### read

public ObjectContent<T> read(Reader reader)
                      throws IOException
Return `ObjectContent` from reading from the specified reader.

Parameters:
`reader` - the source reader
Returns:
the `ObjectContent`
Throws:
`IOException` - on read error

  - 

### writeObject

protected abstract String writeObject(T value,
 org.springframework.core.ResolvableType type)
                               throws IOException
Write the specified object to a JSON string.

Parameters:
`value` - the source value (never `null`)
`type` - the resulting type (never `null`)
Returns:
the JSON string
Throws:
`IOException` - on write error

  - 

### readObject

protected T readObject(InputStream inputStream,
 org.springframework.core.ResolvableType type)
                throws IOException
Read from the specified input stream to create an object of the specified type. The
default implementation delegates to `readObject(Reader, ResolvableType)`.

Parameters:
`inputStream` - the source input stream (never `null`)
`type` - the resulting type (never `null`)
Returns:
the resulting object
Throws:
`IOException` - on read error

  - 

### readObject

protected abstract T readObject(Reader reader,
 org.springframework.core.ResolvableType type)
                         throws IOException
Read from the specified reader to create an object of the specified type.

Parameters:
`reader` - the source reader (never `null`)
`type` - the resulting type (never `null`)
Returns:
the resulting object
Throws:
`IOException` - on read error