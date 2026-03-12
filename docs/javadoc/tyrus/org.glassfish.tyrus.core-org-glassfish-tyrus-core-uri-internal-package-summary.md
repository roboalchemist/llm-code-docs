Module org.glassfish.tyrus.core

# Package org.glassfish.tyrus.core.uri.internal

---

package org.glassfish.tyrus.core.uri.internal

Common classes that provide support for URI templates,
 encoding/decoding of URI components and multivalued collections.

 Taken from Jersey 2 - org.glassfish.jersey.uri.

-

Related Packages

Package
Description
org.glassfish.tyrus.core.uri

URI matching.

-

Class
Description
AbstractMultivaluedMap<K,V>

Abstract skeleton implementation of a `MultivaluedMap` that is backed
 by a [key, multi-value] store represented as a `Map<K, List<V>>`.

MultivaluedHashMap<K,V>

A hash table based implementation of `MultivaluedMap` interface.

MultivaluedMap<K,V>

A map of key-values pairs.

MultivaluedStringMap

An implementation of `MultivaluedMap` where keys and values are
 instances of String.

PathPattern

A path pattern that is a regular expression generated from a URI path template.

PathPattern.RightHandPath

The set of right hand path patterns that may be appended to a path pattern.

PathSegment

Represents a URI path segment and any associated matrix parameters.

PathTemplate

A URI template for a URI path.

PatternWithGroups

A pattern for matching a string against a regular expression and returning capturing group values for any capturing
 groups present in the expression.

UriComponent

Utility class for validating, encoding and decoding components
 of a URI.

UriComponent.Type

The URI component type.

UriTemplate

A URI template.

UriTemplateParser

A URI template parser that parses JAX-RS specific URI templates.
