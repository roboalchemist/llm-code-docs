# RDF/JS Stream

**Source**: https://rdf.js.org/stream-spec/

**Description**: Specification for RDF/JS Stream interfaces, enabling efficient streaming of RDF quads in JavaScript.

---

RDF/JS: Stream interfaces

This document provides a specification of a low level interface definition representing RDF data
independent of a serialized format in a JavaScript environment. The task force which defines
this interface was formed by RDF JavaScript library developers with the wish to make existing
and future libraries interoperable. This definition strives to provide the minimal necessary
interface to enable interoperability of libraries such as serializers, parsers and higher level
accessors and manipulators.

## Stream interfaces

Streams are used only in a readable manner. This requires only a single queue per stream, which
simplifies implementations and doesn't have performance drawbacks, compared to writeable
streams.

The interfaces introduces in this spec make use of the Term and DataFactory interfaces from the [RDF/JS Data model specification](https://rdf.js.org/data-model-spec/)

![UML data interface diagram](img/stream_diagram.svg)

### Stream interface

```typescript
      [Exposed=(Window,Worker)]
      interface Stream : EventEmitter {
        any read();
        attribute Event readable;
        attribute Event end;
        attribute Event error;
        attribute Event data;
        attribute Event prefix;
      };
```

A Stream handles a sequence of data as chunks which are emitted or manually pulled over time.
The type of the chunks must be consistent.
Typical types are Buffer or String for serialized data or Quad for RDF data.

The EventEmitter and Event types originate from [Node.JS](https://nodejs.org/docs/latest-v17.x/api/)

This specification uses the following notation, for a known type `T` of a Stream:

```typescript
Stream<T>
```

read()
This method pulls a chunk of data out of the internal buffer and returns it.
If there is no chunk available, then it will return null.

readable When a chunk can be read from the stream, it will emit this event.

end This event fires when there will be no more chunks to read.

error `error(Error error)` This event fires if any error occurs. The `message` describes the error.

data `data(any chunk)` This event is emitted for every chunk that can be read from the stream. The `chunk` is the content of the data.

#### Optional Events

These events are not required, but if an implementation wishes to support such events, they should conform to these definitions:

prefix `prefix(string prefix, NamedNode iri)` This event is emitted every time a prefix is mapped to some IRI.

### ConstructorOptions interface

```typescript
      [Exposed=(Window,Worker)]
      interface ConstructorOptions {
        attribute DataFactory? dataFactory;
        attribute DOMString? baseIRI;
      };
```

Constructors of all other interfaces defined in this spec accept options parameter. While we define this parameter as optional as well as all its attributes as optional, specific implementations may choose to require them. All implementations SHOULD provide documentation of the constructors and their options.

dataFactory DataFactory implementation that created instance implementing the interface will use to create all the Data Model instances.

baseIRI Base IRI that created instance implementing the interface will use to resolve or create relative IRIs.

### Source interface

```typescript
      [Exposed=(Window,Worker)]
      interface Source {
        constructor();
        constructor(ConstructorOptions options);
        Stream match(optional Term? subject, optional Term? predicate, optional Term? _object, optional Term? graph);
      };
```

A Source is an object that emits quads. It can contain quads but also generate them on the
fly. For example, parsers and transformations which generate quads can implement the Source
interface.

match() Returns a stream of `Quad`s that processes all quads matching the pattern.

When matching with `graph` set to `undefined` or `null`
it MUST match all the graphs (sometimes called *the union graph*). To match only *the default graph*
set `graph` to a `DefaultGraph`

### Sink interface

```typescript
      [Exposed=(Window,Worker)]
      interface Sink {
        constructor();
        constructor(ConstructorOptions options);
        EventEmitter import(Stream stream);
      };
```

A Sink is an object that consumes data from different kinds of streams. It can store the
content of the stream or do some further processing. For example parsers, serializers,
transformations and stores can implement the Sink interface.

import() Consumes the given stream. The `end` and `error`
events are used like described in the `Stream` interface. Depending on the use
case, subtypes of `EventEmitter` or `Stream` are used.

#### Typical use cases

* **Parser:**

```typescript
  Stream<Quad> import(Stream stream)
```

* **Serializer**

```typescript
  Stream import(Stream<Quad> stream)
```

* **Transformation**

```typescript
  Stream<Quad> import(Stream<Quad> stream)
```

* **Store**

```typescript
  EventEmitter .import(Stream<Quad> stream)
```

### Store interface

```typescript
      [Exposed=(Window,Worker)]
      interface Store { // Extends Source and Sink
        constructor();
        constructor(ConstructorOptions options);
        EventEmitter remove(Stream stream);
        EventEmitter removeMatches(optional Term? subject, optional Term? predicate, optional Term? _object, optional Term? graph);
        EventEmitter deleteGraph((Term or DOMString) graph);
      };
```

A Store is an object that usually used to persist quads. The interface allows removing quads,
beside read and write access. The quads can be stored locally or remotely. Access to stores
LDP or SPARQL endpoints can be implemented with a Store inteface.

remove() Removes all streamed `Quad`s. The `end` and `error`
events are used like described in the `Stream` interface.

removeMatches() All quads matching the pattern will be removed. The
`end` and `error` events are used like described in the
`Stream` interface.

deleteGraph() Deletes the given named graph. The `end` and
`error` events are used like described in the `Stream` interface.
