# Java · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/migration_1.0/java

# Source: https://zenoh.io/docs/migration_1.0/java

# Java

# Java API migration guide for 1.0.0
The API has been extensively modified with the following goals in mind:
- Match the API rework done through the Rust Zenoh API.
- Abstracting users from the underlying native mechanisms.
- Making the API more idiomatic, more “imperative”.

## Remotion of the builder patterns and options parameters
Throughout the 0.11.0 API, we were exposing builders, for instance:
```
session.put(keyExpr, value)
  .congestionControl(CongestionControl.BLOCK)
  .priority(Priority.REALTIME)
  .res()
```

This seemed odd, because “put” is an imperative statement. This could lead to confusions
since it’s not evident that instead of performing the put operation, that function returns
a builder that must be built with a ‘res()’ (from resolve) function.
After some deliberation, we opted for the following approach:
- Making theputoperation actually imperative, meaning that calling that function actually performs the put operation. No need for the.res()call anymore.
- Provide configuration options with an optional parameter, in this case aPutOptionsparameter:Example:varputOptions=newPutOptions();putOptions.setCongestionControl(CongestionControl.BLOCK);putOptions.setPriority(Priority.REALTIME);//...session.put(keyExpr,payload,putOptions);// triggers the putIf not provided, the default configuration is used:session.put(keyExpr, payload);
```
var putOptions = new PutOptions();
putOptions.setCongestionControl(CongestionControl.BLOCK);
putOptions.setPriority(Priority.REALTIME);
//...
session.put(keyExpr, payload, putOptions); // triggers the put
```

## Session opening
Session.open(config: Config)has now been replaced withZenoh.open(config: Config).

## Encoding rework
TheEncodingclass has been modified. In 0.11.0. it had the signature
```
class Encoding(val knownEncoding: KnownEncoding, val suffix: String = "")
```

whereKnownEncodingwas an enum.
In 0.11.0. an encoding instance would be created as follows:
```
var encoding = new Encoding(KnownEncoding.TEXT_JSON)
```

In 1.0.0. we have implemented the following changes:
- KnownEncodingenum is removed, instead we provide staticEncodinginstances containing an ID and a description.
- Custom encodings can be created
- The list of pre-defined encodings has been expanded.
In 1.0.0. the previous example would instead now become:
```
var encoding = Encoding.TEXT_JSON
```

## Session-managed declarations
Up until 0.11.0, it was up to the user to keep track of their variable declarations to keep them alive, because once the variable declarations were garbage collected, the declarations were closed. This was because each Kotlin variable declaration is associated with a native Rust instance, and in order to avoid leaking the memory of that Rust instance, it was necessary to free it upon dropping the declaration instance. However, this behavior could be counterintuitive, as users were expecting the declaration to keep running despite losing track of the reference to it.
In this release we introduce a change in which any session declaration is internally associated to the session from which it was declared. Users may want to keep a reference to the declaration in case they want to undeclare it earlier before the session is closed, otherwise, the declaration is kept alive.
For instance:
```
var keyExprA = KeyExp::tryFrom("A/B/C");
var subscriber = session.declareSubscriber(keyExprA, { sample -> System.out.println("Receiving sample on 'A/B/C': " + sample.getPayload() + ")") });

var keyExprB = KeyExpr::tryFrom("A/C/D");
session.declareSubscriber(keyExprB, { sample -> System.out.println("Receiving sample on 'A/C/D': " + sample.getPayload() + ")") }); // No variable is associated to the declared session, on 0.11.0 it would have been instantly dropped
```

Therfore, when receiving a ‘hello’ message onA/**we would still see:
```
>> Receiving sample on 'A/B/C': hello
>> Receiving sample on 'A/C/D': hello
```

since both declarations are still alive.
Now the question is, for how long? What happens first, either when:
- you callundeclare()orclose()to the declaration
- the session is closed, then all the associated declarations are automatically undeclared.

## Key Expression rework
KeyExpr instances are not bound to a native key expression anymore, unless they are declared from a session. It is safe to drop the reference to the key expression instance, but the memory management associated to a key expression will differ:
- If the KeyExpr was not declared from a session, then the garbage collector simply claims back the memory.
- If it was declared from a session, then the session keeps track of it and frees the native memory upon closing the session.
Declaring a KeyExpr on a session results in better performance, since the session is informed that we intend to use a key expression repeatedly.
We also associate a native key expression to a Kotlin key expression instance, avoiding copies.

## Config loading
When opening a session, it’s now mandatory to provide a configuration to the session, even for a default config:
```
var config = Config.loadDefault();
var session = Zenoh.open(config);
```

TheConfigclass has been modified
- Config.loadDefault(): Config: returns the default config
- Config.fromFile(file: File): Config: allows to load a config file.
- Config.fromPath(path: Path): Config: allows to load a config file from a path.
- Config.fromJson(json: String): Config: loads the config from a string literal with json format
- Config.fromJson5(json5: String): Config: loads the config from a string literal with json5 format
- Config.fromYaml(yaml: String): Config: loads the config from a string literal with yaml format
- Config.fromJsonElement(jsonElement: JsonElement): Config: loads the config from a kotlin JsonElement.
In case of failure loading the config, an exception is thrown.

## Packages rework
The package structure of the API is now aligned with Zenoh Rust package structure.
Changes:
- Removing the “prelude” package
- QoS package now contains:CongestionCOntrolPriorityReliabilityQoS
- CongestionCOntrol
- Priority
- Reliability
- QoS
- Bytes package is created with:ZBytes,IntoZBytes,Encoding
- ZBytes,IntoZBytes,Encoding
- Config package:Config,ZenohId
- Config,ZenohId
- Session package:SessionInfo
- SessionInfo
- Query package:containsQueryandQueryableremoving queryable package
- containsQueryandQueryable
- removing queryable package

## Reliability
TheReliabilityconfig parameter used on when declaring a subscriber, has been moved. It now must be specified when declaring aPublisheror when performing aPutor aDeleteoperation.

## Logging
There are two main changes regarding logging, the interface and the mechanism.
Lets look at the following example, where we want to run the ZPub example with debug logging. On 1.0.0 we’ll do:
```
RUST_LOG=debug gradle ZPub
```

If we wanted to enable debug logging and tracing for some specific package, for instancezenoh::net::routing, we’d do:
```
RUST_LOG=debug,zenoh::net::routing=trace gradle ZPub
```

However, this is not enabled by default.
In order to enable logging, one of these newly provided functions must be called:
```
Zenoh.tryInitLogFromEnv();
```

and
```
Zenoh.initLogFromEnvOr(fallbackFilter: String);
```

This last function allows to programmatically specify the logs configuration if not provided as an environment variable.

## ZBytes serialization / deserialization & replacement of Value
We have created a new abstraction with the name ofZBytes. This class represents the bytes received through the Zenoh network. This new approach has the following implications:
- Attachmentclass is replaced byZBytes.
- Valueis replaced by the combination ofZBytesandEncoding.
- ReplacingByteArrayto represent payloads
WithZByteswe have also introduced a Serialization and Deserialization for convenient conversion betweenZBytesand Kotlin types.

### Serialization & Deserialization
We can serialize primitive types into aZBytesinstance, that is, converting the data into bytes processed by the zenoh network.
We’ll see that for serialization and deserialization, we need to create instances ofZSerializerandZDeserializerrespectively.

#### Primitive types
(De)Serialization is supported by the following primitive types:
- Numeric:Byte,Short,Integer,Long,Float, andDouble
- String
- ByteArray
For instance:
```
Integer input = 123456;
ZSerializer<Integer> serializer = new ZSerializer<>() {};
ZBytes zbytes = serializer.serialize(input);

ZDeserializer<Integer> deserializer = new ZDeserializer<>() {};
Integer output = deserializer.deserialize(zbytes);
assert input.equals(output);
```

This approach works as well for the other aforementioned types.
For serialization,StringandByteArraythe functionsZBytes::from(string: String)andZBytes::from(bytes: ByteArray)can be used respectively. Analogously, deserialization,ZBytes::toString()andZBytes::toByteArray()can be used.
For instance:
```
var exampleString = "example string";
var zbytes = ZBytes.from(exampleString);
var output = zbytes.toString();
assert exampleString.equals(output);
```

#### Lists
Lists are supported, but they must be either:
- List of numeric types : (Byte,Short,Int,Long,Float,Double)
- List ofString
- List ofByteArray
- List of another supported type
The serialize syntax must be used:
```
List<Integer> input = List.of(1, 2, 3, 4, 5);
ZSerializer<List<Integer>> serializer = new ZSerializer<>() {};
ZBytes zbytes = serializer.serialize(input);

ZDeserializer<List<Integer>> deserializer = new ZDeserializer<>() {};
List<Integer> output = deserializer.deserialize(zbytes);
assert input.equals(output);
```

#### Maps
Maps are supported as well, with the restriction that their inner types must supported primitives:
- Numeric types
- String
- ByteArray
- Map of another supported types
```
Map<String, Integer> input = Map.of("one", 1, "two", 2, "three", 3);
ZSerializer<Map<String, Integer>> serializer = new ZSerializer<>() {};
ZBytes zbytes = serializer.serialize(input);

ZDeserializer<Map<String, Integer>> deserializer = new ZDeserializer<>() {};
Map<String, Integer> output = deserializer.deserialize(zbytes);
assert input.equals(output);
```

#### Parameterized types combinations
Combinations of all the above types is supported. For instance:
- List of lists
```
List<List<Integer>> input = List.of(List.of(1, 2, 3));
ZSerializer<List<List<Integer>>> serializer = new ZSerializer<>() {};
ZBytes zbytes = serializer.serialize(input);

ZDeserializer<List<List<Integer>>> deserializer = new ZDeserializer<>() {};
List<List<Integer>> output = deserializer.deserialize(zbytes18);
assert input.equals(output);
```

- List of maps
```
List<Map<String, Integer>> input = List.of(Map.of("a", 1, "b", 2));
ZSerializer<List<Map<String, Integer>>> serializer = new ZSerializer<>() {};
ZBytes zbytes = serializer.serialize(input);

ZDeserializer<List<Map<String, Integer>>> deserializer = new ZDeserializer<>() {};
List<Map<String, Integer>> output = deserializer.deserialize(zbytes);
assert input.equals(output);
```