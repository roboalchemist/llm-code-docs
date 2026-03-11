# RDF/JS Dataset

**Source**: https://rdf.js.org/dataset-spec/

**Description**: Specification for the RDF/JS Dataset interface, providing a standard way to work with RDF quads in JavaScript.

---

RDF/JS: Dataset specification 1.0


Abstract
--------

The scope of this specification is to provide a way to store multiple quads, as defined in the [RDF/JS: Data model specification](http://rdf.js.org/data-model-spec/#quad-interface), in a so-called dataset.
Similar to the [RDF/JS: Data model specification](http://rdf.js.org/data-model-spec/), this is a low-level specification that provides only essential methods for working with multiple quads.
High-level interfaces that work with quads can and should be using libraries that implement this interface.

The specification itself consists of a core-part that is the base for all other functions defined.

Low-level methods are using explicit parameters that cannot be omitted.

Additional high-level interfaces are outside of the scope of this specification and should be defined elsewhere.

Data interfaces
---------------

### DatasetCore interface

```
    [Exposed=(Window,Worker)]
    interface DatasetCore {
      readonly attribute unsigned long  size;
      Dataset                           add (Quad quad);
      Dataset                           delete (Quad quad);
      boolean                           has (Quad quad);
      Dataset                           match (optional Term? subject, optional Term? predicate, optional Term? _object, optional Term? graph);

      iterable<Quad>;
    };
```

### Attributes

size

A non-negative integer that specifies the number of quads in the set.

### Methods

add

Adds the specified `quad` to the dataset.

This method returns the dataset instance it was called on.

Existing quads, as defined in `Quad.equals`, will be ignored.

delete

Removes the specified `quad` from the dataset.

This method returns the dataset instance it was called on.

has

Determines whether a dataset includes a certain quad, returning true or false as appropriate.

match

This method returns a new dataset that is comprised of all quads in the current instance matching the given arguments.
The logic described in [Quad Matching](#quad-matching) is applied for each quad in this dataset to check if it should be included in the output dataset.

Note: This method always returns a new DatasetCore, even if that dataset contains no quads.

Note: Since a DatasetCore is an unordered set, the order of the quads within the returned sequence is arbitrary.

### DatasetCoreFactory interface

```
    [Exposed=(Window,Worker)]
    interface DatasetCoreFactory {
      DatasetCore dataset (optional sequence<Quad> quads);
    };
```

`DatasetCoreFactory` provides a `dataset` method to create instances of `DatasetCore`.

dataset

Returns a new dataset and imports all quads, if given.

The given sequence must be treated as immutable (do not `.pop()`, `.splice()`, `.shift()`, etc).

The following interfaces are experimental and will change in future versions of this document:

`Dataset`, `DatasetFactory`, `QuadFilterIteratee`, `QuadMapIteratee`, `QuadReduceIteratee`, `QuadRunIteratee`

### Dataset interface

```
    [Exposed=(Window,Worker)]
    interface Dataset : DatasetCore {
      Dataset                           addAll ((Dataset or sequence<Quad>) quads);
      boolean                           contains (Dataset other);
      Dataset                           deleteMatches (optional Term subject, optional Term predicate, optional Term _object, optional Term graph);
      Dataset                           difference (Dataset other);
      boolean                           equals (Dataset other);
      boolean                           every (QuadFilterIteratee iteratee);
      Dataset                           filter (QuadFilterIteratee iteratee);
      undefined                         forEach (QuadRunIteratee iteratee);
      Promise<Dataset>                  import (Stream stream);
      Dataset                           intersection (Dataset other);
      Dataset                           map (QuadMapIteratee iteratee);
      any                               reduce (QuadReduceIteratee iteratee, optional any initialValue);
      boolean                           some (QuadFilterIteratee iteratee);
      DOMString                         toCanonical ();
      Stream                            toStream ();
      Dataset                           union (Dataset quads);
    };
```

A DatasetCore implementation may already implement part of the Dataset interface.
If a Dataset implementation acts as a wrapper for a DatasetCore, the wrapped dataset methods should be used.

**`toString`**

Returns an N-Quads string representation of the dataset.

No prior normalization is required, therefore the results for the same quads may vary depending on the Dataset implementation.

### Attributes

### Methods

addAll

Imports the `quads` into this dataset.

This method returns the dataset instance it was called on.

This method differs from Dataset.union in that it adds all `quads` to the current instance, rather than combining `quads` and the current instance to create a new instance.

The given sequence must be treated as immutable (do not `.pop()`, `.splice()`, `.shift()`, etc).

contains

Returns true if the current instance is a superset of the given dataset; differently put: if the given dataset is a subset of, is contained in the current dataset.

Blank Nodes will be normalized.

The given dataset and its content must be treated as immutable (do not cause mutations by calling e.g. `.add()` or `.delete()` on it, do not modify the quads you get out of it).

deleteMatches

This method removes the quads in the current instance that match the given arguments.
The logic described in [Quad Matching](#quad-matching) is applied for each quad in this dataset to select the quads which will be deleted.

This method returns the dataset instance it was called on.

difference

Returns a new dataset that contains alls quads from the current dataset, not included in the given dataset.

The given dataset and its content must be treated as immutable (do not cause mutations by calling e.g. `.add()` or `.delete()` on it, do not modify the quads you get out of it).

equals

Returns true if the current instance contains the same graph structure as the given dataset.

Blank Nodes will be normalized.

The given dataset and its content must be treated as immutable (do not cause mutations by calling e.g. `.add()` or `.delete()` on it, do not modify the quads you get out of it).

every

Universal quantification method, tests whether every quad in the dataset passes the test implemented by the provided `iteratee`.

This method immediately returns boolean false once a quad that does not pass the test is found.

This method always returns boolean true on an empty dataset.

Note: This method is aligned with Array.prototype.every() in ECMAScript-262.

filter

Creates a new dataset with all the quads that pass the test implemented by the provided `iteratee`.

Note: This method is aligned with Array.prototype.filter() in ECMAScript-262.

forEach

Executes the provided `iteratee` once on each quad in the dataset.

Note: This method is aligned with Array.prototype.forEach() in ECMAScript-262.

import

Imports all quads from the given stream into the dataset.

The stream events `end` and `error` are wrapped in a Promise.

intersection

Returns a new dataset containing alls quads from the current dataset that are also included in the given dataset.

The given dataset and its content must be treated as immutable (do not cause mutations by calling e.g. `.add()` or `.delete()` on it, do not modify the quads you get out of it).

map

Returns a new dataset containing all quads returned by applying `iteratee` to each quad in the current dataset.

reduce

This method calls the `iteratee` on each `quad` of the DatasetCore.
The first time the `iteratee` is called, the `accumulator` value is the `initialValue` or, if not given, equals to the first quad of the Dataset.
The return value of the `iteratee` is used as `accumulator` value for the next calls.

This method returns the return value of the last `iteratee` call.

Note: This method is aligned with Array.prototype.reduce() in ECMAScript-262.

some

Existential quantification method, tests whether some quads in the dataset pass the test implemented by the provided `iteratee`.

This method immediately returns boolean true once a quad that passes the test is found.

Note: This method is aligned with Array.prototype.some() in ECMAScript-262.

toCanonical

Returns an N-Quads string representation of the dataset, preprocessed with [RDF Dataset Normalization](https://json-ld.github.io/normalization/spec/) algorithm.

toStream

Returns a stream that contains all quads of the dataset.

union

Returns a new Dataset that is a concatenation of this dataset and the `quads` given as an argument.

The given dataset and its content must be treated as immutable (do not cause mutations by calling e.g. `.add()` or `.delete()` on it, do not modify the quads you get out of it).

### DatasetFactory interface

```
    [Exposed=(Window,Worker)]
    interface DatasetFactory : DataFactory {
      Dataset dataset (optional (Dataset or sequence<Quad>) quads);
    };
```

dataset

Returns a new dataset and imports all quads, if given.

### QuadFilterIteratee interface

```
    [Exposed=(Window,Worker)]
    interface QuadFilterIteratee {
      boolean test (Quad quad, Dataset dataset);
    };
```

test

A callable function that returns true if the input quad passes the test this function implements.

### QuadMapIteratee interface

```
    [Exposed=(Window,Worker)]
    interface QuadMapIteratee {
      Quad map (Quad quad, Dataset dataset);
    };
```

map

A callable function that can be executed on a quad and returns a quad.

The returned quad can be the given quad or a new one.

### QuadReduceIteratee interface

```
    [Exposed=(Window,Worker)]
    interface QuadReduceIteratee {
      any run (any accumulator, Quad quad, Dataset dataset);
    };
```

run

A callable function that can be executed on an accumulator and quad and returns a new accumulator.

### QuadRunIteratee interface

```
    [Exposed=(Window,Worker)]
    interface QuadRunIteratee {
      undefined run (Quad quad, Dataset dataset);
    };
```

run

A callable function that can be executed on a quad.

Runtime Semantics
-----------------

### Quad Matching

The methods `match` and `deleteMatches` select each quad for which the following logic is true:

* calling `quad.subject.equals` with the specified subject as argument returns true, or the subject argument is null, AND
* calling `quad.predicate.equals` with the specified predicate as argument returns true, or the predicate argument is null, AND
* calling `quad.object.equals` with the specified object as argument returns true, or the object argument is null, AND
* calling `quad.graph.equals` with the specified graph as argument returns true, or the graph argument is null

Only quads matching all of the given non-null arguments will be selected.

Acknowledgements
----------------

The authors would like to thank the authors of the [RDF Interfaces](https://www.w3.org/TR/rdf-interfaces/) specification.
Many concepts and definitions were adopted from that specification.

WebIDL references
-----------------

The interfaces in this spec make use of the
DataFactory,
Quad, and
Term
interfaces from the [RDF/JS Data model specification](https://rdf.js.org/data-model-spec/).

The interfaces in this spec make use of the
Stream
interface from the [Node.js API](https://nodejs.org/api/).
