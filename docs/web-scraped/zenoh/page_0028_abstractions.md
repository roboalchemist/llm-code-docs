# Abstractions · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/manual/abstractions

# Source: https://zenoh.io/docs/manual/abstractions

# Abstractions
Zenoh is adistributed serviceto define, manage and operate onkey/valuespaces.
The main abstractions at the core of Zenoh are the following:

## Key
Zenoh operates onkey/valuepairs. The most important thing to know about Zenoh keys is that/is the hierarchical separator, just like in unix filesystems.
While you could set up your own hierarchy using other separators, your Zenoh exchanges would benefit from better performance using/, as it will let Zenoh do clever optimisations (users have informed us in the past that switching from.to/as their hierarchy-separator almost divided their CPU usage by 2).
However, you will much more often interact withkey expressions, which provide a small regular language to match sets of keys.
There are a few restrictions on what may be a key:
- It is a/-joined list of non-empty UTF-8 chunks. This implies that leading and trailing/are forbidden, as well as the//pattern.
- An individual key may not contain the characters*,$,?,#.
A typical Zenoh key would look something like:organizationA/building8/room275/sensor3/temperature

## Key Expression
A key expression denotes a set of keys.
It is declared usingKey Expression Language, a small regular language, where:
- *matches any set of characters in a key, except'/'. It can only be surrounded by/.
For example, subscribing toorganizationA/building8/room275/*/temperaturewill ensure that any temperature message from any device in room 275 of building 8 will be routed to your subscriber.Note however that this expression wouldn’t matchorganizationA/building8/room275/temperature.
- $*is like*except it may be surrounded by any other characters.
For example, subscribing toorganizationA/building8/room275/thermometer$*/temperaturewill get the temperature readings from all thermometers in the room.
- **is equivalent to.*in regular expression syntax: it will match absolutely anything, including nothing. They may appear at the beginning of a key expression or after a/, and/is the only allowed character after a**For example, subscribing toorganizationA/**/temperaturewill ensure that any temperature message from ALL devices in organization A.
This language is designed to ensure that two key expressions addressing the same set of keysmustbe the same string.
To ensure that, only acanonform is allowed for key expressions:
- **/**must always be replaced by**
- **/*must always be replaced by*/**
- $*$*must always be replaced by$*
- $*must be replaced by*if alone in a chunk.

### Notes on key-space design
Here are some rules of thumb to make Zenoh more comfortable to work with, and more resource-efficient:
- $*is slower than*, design your key-space to avoid needing it. The need for$*usually stems from mixing different discriminants within a chunk. Preferrobot/12andpc/18torobot12andpc18.
- A strict hierarchy, where you ensure thata/keyexpr/that/ends/with/*always yields data from a single type, will save you the hassle of filtering out data that’s not of the right type, while saving the network bandwidth.

## Selector
A selector (specification) is an extension of thekey expressionsyntax, and is made of two parts:
- The key expression, which is the part of the selector that routers will consider when routing a Zenoh message.
- Optionally, separated from the key expression by a?, the parameters.
Here’s what a selector concretely looks like:
```
path/**/something?arg1=val1;arg2=value%202
^               ^ ^                      ^
|Key Expression-| |----- parameters -----|
```

Which deserializes to:
```
{
  key_expr: "path/**/something",
  parameters: {arg1: "val1", arg2: "value 2"}
}
```

The selector’sparameterssection functions just like query parameters:
- It’s separated from the path (Key Expr) by a?.
- It’s a?list of key-value pairs.
- The first=in a key-value pair separates the key from the value.
- If no=is found, the value is an empty string:hello=there;kenobiis interpreted as{"hello": "there", "kenobi": ""}.
- The selector is assumed to be url-encoded: any character can be escaped using%<charCode>.
There are however some additional conventions:
- Duplicate keys are considered Undefined Behaviour; but the recommended behaviour (implemented by the tools we provide for selector interpretation) is to check for duplicates of the interpreted keys, returning errors when they arise.
- The Zenoh Team considers any key that does not start with an ASCII alphabetic character reserved, intending to standardize some parameters to facilitate working with diverse queryables.
- Since Zenoh operations may be distributed over diverse networks, we encourage queryable developers to use some prefix in their custom keys to avoid collisions.
- When interpreting a key-value pair as a boolean, the absence of the key-value pair, or the value being"false"are the only “falsey” values: in the previous examples, the bothhelloandkenobiwould be considered truthy if interpreted as boolean.
The list of standardized parameters, as well as their usage, is documented in theselector specification.

## Value
A user provided data item along with itsencoding.

## Encoding
A description of thevalueformat, allowing Zenoh (or your application) to know how to encode/decode the value to/from a bytes buffer.
By default, Zenoh is able to transport and store any format of data as long as it’s serializable as a bytes buffer.
But for advanced features such as content filtering (usingselector) or to automatically deserialize the data into a concrete type in the client APIs, Zenoh requires a description of the data encoding.
Some noteworthy supported encodings are:
- TextPlain: the value is a UTF-8 string
- AppJsonorTextJson: the value is a JSON string
- AppProperties: the value is a string representing a list of keys/values separated by';'(e.g."k1=v1;k2=v2..."), where both key and value are string-typed.
- AppInteger: the value is an integer
- AppFloat: the value is a float
You may refer toZenoh’s Rust API documentationto get more information on the supported encodings.
You may also write your own encodings by either suffixing an existing one, or by suffixing theEMPTYencoding, if you wish to use encodings that are unknown to Zenoh. While Zenoh will not be able to deserialize these encodings, it will expose them to your application so that it may be informed on how it should deserialize any received value.

## Timestamp
When avalueis put into Zenoh, the first Zenoh router receiving this value automatically
associates it with a timestamp.This timestamp is made of 2 items:
- Atimegenerated by aHybrid Logical Clock (HLC).
This time is a 64-bit time with a similar structure than a NTP timestamp (but with a different epoch):The higher 32-bit part is the number of seconds since midnight, January 1, 1970 UTC
(implying a rollover in 2106).The lower 32-bit part is a fraction of second, but with the 4 last bits replaced by a counter.This time gives a theoretical resolution of (0xF * 10^9 / 2^32) = 3.5 nanoseconds.The counter guarantees that the same time cannot be generated twice and that thehappened-beforerelationship is preserved.
- The higher 32-bit part is the number of seconds since midnight, January 1, 1970 UTC
(implying a rollover in 2106).
- The lower 32-bit part is a fraction of second, but with the 4 last bits replaced by a counter.
- TheUUIDof the Zenoh router that generated the time.
Such a timestamp allows Zenoh to guarantee that each value introduced into the system has a unique timestamp, and that those timestamps (and therefore the values) can be ordered in the same way at any point of the system, without the need of any consensus algorithm.

## Subscriber
An entity registering interest for any change (put or delete) to a value associated with a key matching the specifiedkey expression.

## Publisher
An entity declaring that it will be updating the key/value with keys matching a givenkey expression.

## Queryable
A computation registered at a specifickey expression.
This computation can be triggered by agetoperation on aselectormatching this key expression.
The computation function will receive the selector as parameters.

## Storage
Storagesare both a queryable and subscriber. They
- subscribe tokey expression;
- upon receiving publications matching their subscription, they store the associated values;
- when queried with a selector matching their subscription, they return the latest values for each matching key.
zenohd, the reference implementation of a Zenoh node, supports storages through thestoragesplugin.
Since there exist many ways to implement the storing part of the process, thestoragesplugin relies on dynamically loadedvolumesto do the actual value-storing. Each volume has its own tradeoffs, as well as potential uses besides acting as a database forzenohd.

## Admin space
The key space of Zenoh dedicated to administering a Zenoh router and its plugins.
It is accessible via regular GET/PUT on Zenoh, under the@/router/<router-id>prefix, where<router-id>is the UUID of a Zenoh router.
When using the REST API, you can replace the<router-id>with thelocalkeyword,
meaning the operation addresses the Zenoh router the HTTP client is connected to.
For instance, the following keys can be used:
- @/<router-id>/router(read-only):Returns a JSON with the status information about the router.
- @/<router-id>/router/**(write-only):Allows you to edit the configuration of the router at runtime.
Some plugins may extend the admin space, such asStorages, which will add the following keys:
- @/<router-id>/router/status/plugins/storage_manager/volumes/<volume-name>(read-only):Returning information about the selected backend in JSON format
- @/<router-id>/router/status/plugins/storage_manager/storages/<storage-name>(read-only):Returning information about the selected storage in JSON format
