# Package org.springframework.boot.test.json

---

@NullMarked
package org.springframework.boot.test.json

Support for testing JSON.

- 

Classes

Class
Description
AbstractJsonMarshalTester<T>

Base class for AssertJ based JSON marshal testers.

AbstractJsonMarshalTester.FieldInitializer<M>

Utility class used to support field initialization.

BasicJsonTester

AssertJ based JSON tester that works with basic JSON strings.

GsonTester<T>

AssertJ based JSON tester backed by Gson.

Jackson2Tester<T>
Deprecated, for removal: This API element is subject to removal in a future version.
since 4.0.0 for removal in 4.3.0 in favor of Jackson 3.

JacksonTester<T>

AssertJ based JSON tester backed by Jackson.

JsonbTester<T>

AssertJ based JSON tester backed by Jsonb.

JsonContent<T>

JSON content usually created from a JSON tester.

JsonContentAssert

AssertJ `Assert` for `JsonContent`.

ObjectContent<T>

Object content usually created from `AbstractJsonMarshalTester`.

ObjectContentAssert<A>

AssertJ `Assert` for `ObjectContent`.