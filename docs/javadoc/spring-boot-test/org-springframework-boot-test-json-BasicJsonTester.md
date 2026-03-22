# Class BasicJsonTester

java.lang.Object
org.springframework.boot.test.json.BasicJsonTester

---

public class BasicJsonTester
extends Object
AssertJ based JSON tester that works with basic JSON strings. Allows testing of JSON
payloads created from any source, for example:

```

public class ExampleObjectJsonTests {

    private BasicJsonTester json = new BasicJsonTester(getClass());

    @Test
    public void testWriteJson() throws IOException {
        assertThat(json.from("example.json")).extractingJsonPathStringValue("@.name")
                        .isEqualTo("Spring");
    }

}

```

See `AbstractJsonMarshalTester` for more details.

Since:
1.4.0

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`BasicJsonTester()`

Create a new uninitialized `BasicJsonTester` instance.

` `
`BasicJsonTester(Class<?> resourceLoadClass)`

Create a new `BasicJsonTester` instance that will load resources as UTF-8.

` `
`BasicJsonTester(Class<?> resourceLoadClass,
 @Nullable Charset charset)`

Create a new `BasicJsonTester` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`JsonContent<Object>`
`from(byte[] source)`

Create JSON content from the specified JSON bytes.

`JsonContent<Object>`
`from(File source)`

Create JSON content from the specified JSON file.

`JsonContent<Object>`
`from(InputStream source)`

Create JSON content from the specified JSON input stream.

`JsonContent<Object>`
`from(CharSequence source)`

Create JSON content from the specified String source.

`JsonContent<Object>`
`from(String path,
 Class<?> resourceLoadClass)`

Create JSON content from the specified resource path.

`JsonContent<Object>`
`from(org.springframework.core.io.Resource source)`

Create JSON content from the specified JSON resource.

`protected final void`
`initialize(Class<?> resourceLoadClass)`

Initialize the marshal tester for use, configuring it to load JSON resources as
UTF-8.

`protected final void`
`initialize(Class<?> resourceLoadClass,
 @Nullable Charset charset)`

Initialize the marshal tester for use.

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### BasicJsonTester

protected BasicJsonTester()
Create a new uninitialized `BasicJsonTester` instance.

  - 

### BasicJsonTester

public BasicJsonTester(Class<?> resourceLoadClass)
Create a new `BasicJsonTester` instance that will load resources as UTF-8.

Parameters:
`resourceLoadClass` - the source class used to load resources

  - 

### BasicJsonTester

public BasicJsonTester(Class<?> resourceLoadClass,
 @Nullable Charset charset)
Create a new `BasicJsonTester` instance.

Parameters:
`resourceLoadClass` - the source class used to load resources
`charset` - the charset used to load resources
Since:
1.4.1

- 

## Method Details

  - 

### initialize

protected final void initialize(Class<?> resourceLoadClass)
Initialize the marshal tester for use, configuring it to load JSON resources as
UTF-8.

Parameters:
`resourceLoadClass` - the source class used when loading relative classpath
resources

  - 

### initialize

protected final void initialize(Class<?> resourceLoadClass,
 @Nullable Charset charset)
Initialize the marshal tester for use.

Parameters:
`resourceLoadClass` - the source class used when loading relative classpath
resources
`charset` - the charset used when loading relative classpath resources
Since:
1.4.1

  - 

### from

public JsonContent<Object> from(CharSequence source)
Create JSON content from the specified String source. The source can contain the
JSON itself or, if it ends with `.json`, the name of a resource to be loaded
using `resourceLoadClass`.

Parameters:
`source` - the JSON content or a `.json` resource name
Returns:
the JSON content

  - 

### from

public JsonContent<Object> from(String path,
 Class<?> resourceLoadClass)
Create JSON content from the specified resource path.

Parameters:
`path` - the path of the resource to load
`resourceLoadClass` - the source class used to load the resource
Returns:
the JSON content

  - 

### from

public JsonContent<Object> from(byte[] source)
Create JSON content from the specified JSON bytes.

Parameters:
`source` - the bytes of JSON
Returns:
the JSON content

  - 

### from

public JsonContent<Object> from(File source)
Create JSON content from the specified JSON file.

Parameters:
`source` - the file containing JSON
Returns:
the JSON content

  - 

### from

public JsonContent<Object> from(InputStream source)
Create JSON content from the specified JSON input stream.

Parameters:
`source` - the input stream containing JSON
Returns:
the JSON content

  - 

### from

public JsonContent<Object> from(org.springframework.core.io.Resource source)
Create JSON content from the specified JSON resource.

Parameters:
`source` - the resource containing JSON
Returns:
the JSON content