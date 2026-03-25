# Source: https://ebean.io/docs/features/json

Title: Documentation / Features / JSON Marshalling

URL Source: https://ebean.io/docs/features/json

Markdown Content:
Overview
--------

Ebean has built in support for marshalling and unmarshalling entity beans to and from JSON. Ebean uses `Jackson core` to do this. The reason Ebean does this is treat JSON as a first class feature with built in support for `Partial objects` and `cyclical relationships` which are both common in ORM. In additional all supported types including `Joda types`, `Java8 types` and [`JSON database mapping types`](https://ebean.io/docs/features/json-in-db) work out of the box.

> JSON marshalling/unmarshalling should be painless, performant and work out of the box.

JsonContext
-----------

Obtain a `JsonContext` from Database via the `json()` method. This JsonContext then provides various methods for marshalling/unmarshalling JSON to and from entity beans.

String jsonWithUnknown = "{\"id\":42, \"unknownProp\":\"foo\", \"name\":\"rob\", \"version\":1}";

Customer customer = DB.json().toBean(Customer.class, jsonWithUnknown);
assertEquals(Integer.valueOf(42), customer.getId());
assertEquals("rob", customer.getName());
