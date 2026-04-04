# Source: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.md

<a id="schema-evolution-and-compatibility"></a>

# Schema Evolution and Compatibility for Schema Registry on Confluent Platform

<!-- WARNING: THIS IS A SHARED FILE AND THE SOURCE IS LOCATED IN DOCS-COMMON. DO NOT ADD TO ANY OTHER REPO. -->

## Schema evolution

When using serdes formats such as Avro, JSON Schema, and Protobuf, keep in mind the importance of managing the schemas and consider how these
schemas should evolve. [Confluent Schema Registry](../index.md#schemaregistry-intro) is built for exactly that purpose.
Schema compatibility checking is implemented in Schema Registry by versioning every single schema.
The compatibility type determines how Schema Registry compares the new schema with previous versions of a schema, for a given subject.
When a schema is first created for a subject, it gets a unique id and it gets a version number, i.e., version 1.
When the schema is updated (if it passes compatibility checks), it gets a new unique id and it gets an incremented version number, i.e., version 2.

To learn more about serdes for supported schema formats, see âFormats, Serializers, and Deserializersâ in either the
[Confluent Cloud documentation](/cloud/current/sr/fundamentals/serdes-develop/index.html)
or in the [Confluent Platform documentation](/platform/current/schema-registry/fundamentals/serdes-develop/index.html)

<a id="sr-compatibility-types"></a>

## Compatibility types

### Summary

The following table summarizes the compatibility rules for the different schema formats: **Avro**, **Protobuf**, and **JSON Schema** policies for a given subject.
The Confluent Schema Registry default compatibility type is `BACKWARD`. All the compatibility types are described in more detail in the sections that follow the table.
Note that the allowed changes are dependent on how fields are originally defined. For example, as described under [Backward compatibility](#avro-backward-compatibility),
the ability to delete a field and keep the schema compatible requires that the field was either specified as optional or provided a default value in the original version.
To learn more, see [Configuration Options](/platform/current/schema-registry/connect.html#configuration-options) on connectors to self-managed Schema Registry that provide further control over compatibility requirements.

|                            |    |    |      |    |    |      |    |    | **Avro**   | **Protobuf**   | **JSON Schema (lenient policy)**   | **JSON Schema (strict policy)**   |
|----------------------------|----|----|------|----|----|------|----|----|------------|----------------|------------------------------------|-----------------------------------|
| Allowed changes            | BW | FW | Full | BW | FW | Full | BW | FW | Full       | BW             | FW                                 | Full                              |
| Add optional field         | â  | â  | â    | â  | â  | â    | â  | â  | â          | Closed         | Open                               | Partial                           |
| Remove optional field      | â  | â  | â    | â  | â  | â    | â  | â  | â          | Open           | Closed                             | Partial                           |
| Add required field         |    | â  |      |    |    |      |    | â  |            |                | Open                               |                                   |
| Remove required field      | â  |    |      |    |    |      | â  |    |            | Open           |                                    |                                   |
| Add union/oneof variant    | â  |    |      | â  |    |      | â  |    |            | â              |                                    |                                   |
| Remove union/oneof variant |    | â  |      |    | â  |      |    | â  |            |                | â                                  |                                   |
| Widen a scalar type        | â  |    |      | â  | â  | â    | â  |    |            | â              |                                    |                                   |
| Narrow a scalar type       |    | â  |      | â  | â  | â    |    | â  |            |                | â                                  |                                   |

Table Legend:

- â  = **Compatible** operation for the given schema format and compatibility type
- Blank space = **Incompatible** operation for the given schema format and compatibility type
- **BW** = Backward compatible
- **FW** = Forward compatible
- **Full** = Fully compatible (both backward and forward)
- **Closed** = Closed content model
- **Open** = Open content model
- **Partial** = Partially open content model

#### NOTE
- A REST API call to compatibility mode is global meaning it overrides any compatibility parameters set
  in schema registry properties files. This is discussed in [Using compatibility types](#using-compatibility-types-examples) below and
  shown in the API usage examples in [Confluent Cloud: Schema Compatibility (V1) API Usage Examples](/cloud/current/sr/sr-rest-apis.html#schema-compatibility-v1-api-usage-examples)
  and on [Confluent Platform: Update compatibility requirements globally](/platform/current/schema-registry/develop/using.html#update-compatibility-requirements-globally).
- Schema Registry supports a global configuration context using the special context name `:.__GLOBAL:`. When looking up compatibility settings with `defaultToGlobal`,
  the lookup proceeds from the subject to the context, and then to the global context. For contexts without global configuration, compatibility is handled per context.
  To learn more about contexts, see [Contexts](../schema-linking-cp.md#schema-contexts).

### Avro, Protobuf, and JSON Schema have different compatibility rules

Schema evolution and compatibility rules vary somewhat based on schema format. The scenarios and source code examples
given on this page are geared for [Avro](https://avro.apache.org/docs/), which was the first serializer / deserializer that
Confluent supported. Avro was developed with schema evolution in mind, and its specification clearly states the rules for
backward compatibility; whereas the rules and grammar for [JSON Schema](https://json-schema.org) and [Protobuf](https://protobuf.dev) can be more nuanced.

Although the general concepts apply to all formats, the details on how
compatibility is implemented will differ depending on whether you are using
Avro, JSON Schema, or Protobuf. For more in-depth explanations and specific
examples on the newer formats, see the following blog posts and documentation:

**Protobuf**

- Blog post: [Understanding Protobuf Compatibility](https://yokota.blog/2021/08/26/understanding-protobuf-compatibility/)
- Confluent Cloud documentation: [Protobuf compatibility rules](/cloud/current/sr/fundamentals/serdes-develop/serdes-protobuf.html#protobuf-schema-compatibility-rules)
- Confluent Platform documentation: [Protobuf compatibility rules](/platform/current/schema-registry/fundamentals/serdes-develop/serdes-protobuf.html#protobuf-schema-compatibility-rules)

Note that best practice for Protobuf is to use BACKWARD_TRANSITIVE, as adding new message types is not forward compatible.

**JSON Schema**

- Blog post: [Understanding JSON Schema Compatibility](https://yokota.blog/2021/03/29/understanding-json-schema-compatibility/)
- Confluent Cloud documentation: [JSON Schema compatibility rules](/cloud/current/sr/fundamentals/serdes-develop/serdes-json.html#json-schema-compatibility-rules)
- Confluent Platform documentation: [Protobuf compatibility rules](/platform/current/schema-registry/fundamentals/serdes-develop/serdes-json.html#json-schema-compatibility-rules)
  [Compatibility checks](/platform/current/schema-registry/fundamentals/serdes-develop/index.html#compatibility-checks)

<a id="avro-backward-compatibility"></a>

### Backward compatibility

`BACKWARD` compatibility means that consumers using the new schema can read data produced with the last schema.
For example, if there are three schemas for a subject that change in order X-2, X-1, and X then `BACKWARD` compatibility ensures that consumers using the new schema X can process data written by producers using schema X or X-1, but not necessarily X-2.
If the consumer using the new schema needs to be able to process data written by all registered schemas, not just the last two schemas, then use `BACKWARD_TRANSITIVE` instead of `BACKWARD`.
For example, if there are three schemas for a subject that change in order X-2, X-1, and X then `BACKWARD_TRANSITIVE` compatibility ensures that consumers using the new schema X can process data written by producers using schema X, X-1, or X-2.

* `BACKWARD`: consumer using schema X can process data produced with schema X or X-1
* `BACKWARD_TRANSITIVE`: consumer using schema X can process data produced with schema X, X-1, or X-2

#### IMPORTANT
- The Confluent Schema Registry default compatibility type is `BACKWARD`, not `BACKWARD_TRANSITIVE`. The main reason that
  `BACKWARD` compatibility mode is the default, and preferred for Kafka, is so that you can rewind consumers to
  the beginning of the topic.  With `FORWARD` compatibility mode, you arenât guaranteed the ability to read old messages.
  Also, `FORWARD` compatibility mode is harder to work with. In a sense, you need to anticipate all future changes.
  For example, in `FORWARD` compatibility mode with Protobuf, you cannot add new message types to a schema.
- For Kafka Streams, only BACKWARD compatibility is supported. To learn more, see the [note about Kafka Streams under Order of Upgrading Clients](#kstreams-backward-compatibility).
- To understand how Avro uses a newer backward-compatible schema to decode (deserialize) data that was encoded (serialized) with an older schema,
  see [ResolvingDecoder](https://github.com/apache/avro/blob/release-1.7.7/lang/java/avro/src/main/java/org/apache/avro/io/ResolvingDecoder.java)
  in the Apache Avro project.

An example of a backward compatible change is a removal of a field. A consumer that was developed to process events without this field will be able to process events written with the old schema and contain the field â the consumer will just ignore that field.

Consider the case where all of the data in Kafka is also loaded into HDFS, and you want to run SQL queries (for example, using
Apache Hive) over all the data. Here, it is important that the same SQL queries continue to work even as the data is
undergoing changes over time.  To support this kind of use case, you can evolve the schemas in a backward compatible way.
All [Formats, Serializers, and Deserializers](https://docs.confluent.io/platform/current/schema-registry/serdes-develop/index.html) have rules as to what changes are allowed
in the new schema for it to be backward compatible. For example, here are the [Avro rules for compatibility](https://avro.apache.org/docs/1.7.7/spec.html#Schema+Resolution)
If all schemas are evolved in a backward compatible way, we can always use the latest schema to query all the data uniformly.

For example, an application can evolve the
[user schema from the previous section](#schema-evolution-and-compatibility) to the following by adding a new field
`favorite_color`:

```json
{"namespace": "example.avro",
 "type": "record",
 "name": "user",
 "fields": [
     {"name": "name", "type": "string"},
     {"name": "favorite_number",  "type": "int"},
     {"name": "favorite_color", "type": "string", "default": "green"}
 ]
}
```

Note that the new field `favorite_color` has the default value âgreenâ. This allows data encoded with the old schema
to be read with the new one. The default value specified in the new schema will be used for the missing field when
deserializing the data encoded with the old schema.  Had the default value been omitted in the new field, the new
schema would not be backward compatible with the old one since itâs not clear what value should be assigned to the new
field, which is missing in the old data.

<a id="avro-forward-compatibility"></a>

### Forward compatibility

`FORWARD` compatibility means that data produced with a new schema can be read by consumers using the last schema, even though they may not be able to use the full capabilities of the new schema.
For example, if there are three schemas for a subject that change in order X-2, X-1, and X then `FORWARD` compatibility ensures that data written by producers using the new schema X can be processed by consumers using schema X or X-1, but not necessarily X-2.
If data produced with a new schema needs to be read by consumers using all registered schemas, not just the last two schemas, then use `FORWARD_TRANSITIVE` instead of `FORWARD`.
For example, if there are three schemas for a subject that change in order X-2, X-1, and X then `FORWARD_TRANSITIVE` compatibility ensures that data written by producers using the new schema X can be processed by consumers using schema X, X-1, or X-2.

* `FORWARD`: data produced using schema X can be read by consumers with schema X or X-1
* `FORWARD_TRANSITIVE`: data produced using schema X can be read by consumers with schema X, X-1, or X-2

An example of a forward compatible schema modification is adding a new field. In most data formats, consumers that were written to process events without the new field will be able to continue doing so even when they receive new events that contain the new field.

Consider a use case where a consumer has application logic tied to a particular version of the schema. When the schema
evolves, the application logic may not be updated immediately. Therefore, you need to be able to project data with newer
schemas onto the (older) schema that the application understands. To support this use case, you can evolve the schemas
in a forward compatible way: data encoded with the new schema can be read with the old schema.  For example, the new
user schema shown in the previous section on [backward compatibility](#avro-backward-compatibility) is also
forward compatible with the old one.  When projecting data written with the new schema to the old one, the new field is
simply dropped.  Had the new schema dropped the original field `favorite_number` (number, not color), it would not be
forward compatible with the original user schema since consumers wouldnât know how to fill in the value for `favorite_number`
for the new data because the original schema did not specify a default value for that field.

<a id="avro-full-compatibility"></a>

### Full compatibility

`FULL` compatibility means schemas are both backward **and** forward compatible.
Schemas evolve in a fully compatible way: old data can be read with the new schema, and new data can also be read with the last schema.
For example, if there are three schemas for a subject that change in order X-2, X-1, and X then `FULL` compatibility ensures that consumers using the new schema X can process data written by producers using schema X or X-1, but not necessarily X-2, and that data written by producers using the new schema X can be processed by consumers using schema X or X-1, but not necessarily X-2.
If the new schema needs to be forward and backward compatible with all registered schemas, not just the last two schemas, then use `FULL_TRANSITIVE` instead of `FULL`.
For example, if there are three schemas for a subject that change in order X-2, X-1, and X then `FULL_TRANSITIVE` compatibility ensures that consumers using the new schema X can process data written by producers using schema X, X-1, or X-2, and that data written by producers using the new schema X can be processed by consumers using schema X, X-1, or X-2.

* `FULL`: backward and forward compatible between schemas X and X-1
* `FULL_TRANSITIVE`: backward and forward compatible between schemas X, X-1, and X-2

In **Avro** and **Protobuf**, you can define fields with default values. In that case, adding or removing a field with a default value is a fully compatible change.

In **Avro**, a field is made nullable (and therefore âoptionalâ at the schema level) by using a union type that includes `"null"` (for example, `["null", "string"]`).
Providing a default value is not required for nullability itself, but it is important for schema evolution when adding a new field so that existing data can still be read.
Avro requires that the default value conform to the first branch of the union, so it is common to put `"null"` first and use `"default": null` for fields that are intended
to be optional for schema evolution. Note that Avro does not have a built-in `optional` keyword like Protobuf; instead, the union-with-null pattern serves this purpose.

Compatibility rules for supported schema types are described in [Compatibility checks](serdes-develop/index.md#sr-serdes-schemas-compatibility-checks).

JSON Schema does not explicitly define compatibility rules, so this blog post further explains how [JSON Schema compatibility](https://yokota.blog/2021/03/29/understanding-json-schema-compatibility/) works, including full compatibility.

<a id="avro-none-compatibility"></a>

### No compatibility checking

`NONE` compatibility type means schema compatibility checks are disabled.

Sometimes we make incompatible changes.
For example, modifying a field type from `Number` to `String`.
In this case, you will either need to upgrade all producers and consumers to the new schema version at the same time, or more likely â create a brand-new topic and start migrating applications to use the new topic and new schema, avoiding the need to handle two incompatible versions in the same topic.

## Transitive property

<!-- WARNING: THIS IS A SHARED FILE AND THE SOURCE IS LOCATED IN DOCS-COMMON. DO NOT ADD TO ANY OTHER REPO. -->
<!-- transitive -->

Transitive compatibility checking is important once you have more than two versions of a schema for a given subject.
If compatibility is configured as transitive, then it checks compatibility of a new schema against all previously registered schemas; otherwise, it checks compatibility of a new schema only against the latest schema.

For example, if there are three schemas for a subject that change in order X-2, X-1, and X then:

* transitive: ensures compatibility between X-2 <==> X-1 and X-1 <==> X and X-2 <==> X
* non-transitive: ensures compatibility between X-2 <==> X-1 and X-1 <==> X, but not necessarily X-2 <==> X

Refer to an [example of schema changes](https://github.com/confluentinc/schema-registry/issues/209) which are incrementally compatible, but not transitively so.

The Confluent Schema Registry default compatibility type `BACKWARD` is non-transitive, which means that itâs not `BACKWARD_TRANSITIVE`.
As a result, new schemas are checked for compatibility only against the latest schema.

## Order of upgrading clients

The configured compatibility type has an implication on the order for upgrading client applications, i.e., the producers using schemas to write events to Kafka and the consumers using schemas to read events from Kafka.
Depending on the compatibility type:

* `BACKWARD` or `BACKWARD_TRANSITIVE`: there is no assurance that consumers using older schemas can read data produced using the new schema. Therefore, upgrade all consumers before you start producing new events.
* `FORWARD` or `FORWARD_TRANSITIVE`: there is no assurance that consumers using the new schema can read data produced using older schemas. Therefore, first upgrade all producers to using the new schema and make sure the data already produced using the older schemas are not available to consumers, then upgrade the consumers.
* `FULL` or `FULL_TRANSITIVE`: there are assurances that consumers using older schemas can read data produced using the new schema and that consumers using the new schema can read data produced using older schemas. Therefore, you can upgrade the producers and consumers independently.
* `NONE`: compatibility checks are disabled. Therefore, you need to be cautious about when to upgrade clients.

<a id="kstreams-backward-compatibility"></a>

#### IMPORTANT
- For Kafka Streams only FULL, TRANSITIVE, and BACKWARD compatibility is supported.
  For a plain consumer, it is safe to upgrade the consumer to the new schema after
  the producer is upgraded because a plain consumer reads only from the input topic.
  For Kafka Streams, the scenario is different. When you upgrade Kafka Streams, it also can read from
  the input topic (that now contains data with the new schema). However, in contrast to a
  plain consumer, Kafka Streams must also be able to read the old schema (from the state/changelog);
  therefore, only `BACKWARD` compatibility is supported. The Kafka Streams apps must be upgraded first,
  then it safe to upgrade the upstream producer that writes into the input topic.
  `FULL`, `FULL_TRANSITIVE`, and `BACKWARD_TRANSITIVE` compatibilities are always supported for Kafka Streams, as they include backward compatibility
  and so are, in effect, âstrongerâ settings than `BACKWARD`.
- With Confluent Cloud for Apache FlinkÂ®, `FULL`, `FULL_TRANSITIVE`, and `BACKWARD_TRANSITIVE` compatibility types are supported. For more information, see [Schema and Statement Evolution with Flink](/cloud/current/flink/concepts/schema-statement-evolution.html).

## Specify schema compatibility requirements per subject

You can configure and update schema compatibility requirements globally or on a per-subject basis.
To learn more, see [Compatibility](/platform/current/schema-registry/develop/api.html#sr-api-compatibility) in the Schema Registry API Reference and the following topics in the Schema Registry API Usage Examples and Reference docs:

On Confluent Cloud:

- [Get compatibility level on a subject](/cloud/current/sr/sr-rest-apis.html#get-the-compatibility-level-on-a-subject)
- [Update compatibility level on a subject](/cloud/current/sr/sr-rest-apis.html#update-the-subject-compatibility-level)

On Confluent Platform:

- [Get compatibility requirements on a subject](/platform/current/schema-registry/develop/using.html#get-compatibility-requirements-on-a-subject)
- [Update compatibility requirements on a subject](/platform/current/schema-registry/develop/using.html#update-compatibility-requirements-on-a-subject)

## Examples

Each of the sections above has an example of the compatibility type.
An additional reference for Avro is [Avro compatibility test suite](https://github.com/confluentinc/schema-registry/blob/master/core/src/test/java/io/confluent/kafka/schemaregistry/avro/AvroCompatibilityTest.java),
which presents multiple test cases with two schemas and the respective result of the compatibility test between them.

<a id="using-compatibility-types-examples"></a>

## Using compatibility types

Compatibility rules and references for all supported schema types are described in [Compatibility checks](serdes-develop/index.md#sr-serdes-schemas-compatibility-checks) in [Formats, Serializers, and Deserializers](https://docs.confluent.io/platform/current/schema-registry/serdes-develop/index.html),
and in [Schema Evolution and Compatibility](/cloud/current/sr/fundamentals/schema-evolution.html) (on Confluent Cloud) and [Schema Evolution and Compatibility](/platform/current/schema-registry/fundamentals/schema-evolution.html) (on Confluent Platform).

You can find out the details on how to use Schema Registry to store schemas and enforce certain compatibility rules during schema evolution by looking at the REST API usage examples and references for Confluent Cloud and Confluent Platform:

- For Confluent Cloud, see [Confluent Cloud Schema Registry REST API Usage Examples](/cloud/current/sr/sr-rest-apis.html) and Cloud REST API reference: [Schemas (V1)](https://docs.confluent.io/cloud/current/api.html#tag/Schemas-(v1)) and [Subjects (v1)](https://docs.confluent.io/cloud/current/api.html#tag/Subjects-(v1))
- For Confluent Platform, see [Confluent Platform Schema Registry API Usage Examples](/platform/current/schema-registry/develop/using.html) and [Schema Registry API Reference](/platform/current/schema-registry/develop/api.html#schemaregistry-api)

Here are some tips to get you started.

### To check the currently configured global compatibility type

On Confluent Cloud:

- Use the REST API to [Show global compatibility level in currently effect](/cloud/current/sr/sr-rest-apis.html#get-the-global-compatibility-level)
- Use the Confluent Cloud Console to [View Global Compatibility Settings on Schemas](/cloud/current/get-started/schema-registry.html#view-and-edit-global-compatibility-settings-on-schemas)

On Confluent Platform:

- Use the REST API to [Get the top level config](/platform/current/schema-registry/develop/using.html#get-the-top-level-config).

### To set the global or per schema compatibility level

You can configure schema compatibility in the following ways:

On Confluent Cloud:

- Use the API to [Update global compatibility level](/cloud/current/sr/sr-rest-apis.html#update-the-global-compatibility-level)
- Use the API to [Update the subject compatibility level](/cloud/current/sr/sr-rest-apis.html#update-the-subject-compatibility-level)
- Use the Confluent Cloud Console to [View and Edit Global Compatibility Settings on Schemas](/cloud/current/get-started/schema-registry.html#view-and-edit-global-compatibility-settings-on-schemas)
- Use the Confluent Cloud Console as described in [Changing subject level (per topic) compatibility mode of a schema](/cloud/current/sr/schemas-manage.html#changing-subject-level-per-topic-compatibility-mode-of-a-schema)

On Confluent Platform:

- Update compatibility [in your client application](/platform/current/schema-registry/installation/config.html#avro-compatibility-level)
- Use the API to [Update global compatibility](/platform/current/schema-registry/develop/using.html#update-compatibility-requirements-globally)
- Use the API to [Update subject compatibility](/platform/current/schema-registry/develop/using.html#update-compatibility-requirements-on-a-subject)
- Use the Control Center Edit Schema feature, as described in [Manage Schemas for Topics in the Control Center](/platform/current/control-center/topics/schema.html#topicschema).

#### NOTE
A REST API call to compatibility mode is global on Confluent Platform meaning it overrides any compatibility parameters set in Schema Registry properties files, as shown in the API usage example
[Update compatibility requirements globally](/platform/current/schema-registry/develop/using.html#updating-compatibility-requirements-globally).

### To validate the compatibility of a given schema

You can validate the compatibility of a schema as follows:

- [Use the Schema Registry Maven Plugin](../develop/maven-plugin.md#schema-registry-test-compatibility)
- On Confluent Cloud, [Get compatibility level on a subject](/cloud/current/sr/sr-rest-apis.html#get-the-compatibility-level-on-a-subject)
- On Confluent Platform, [Get compatibility requirements on a subject](/platform/current/schema-registry/develop/using.html#get-compatibility-requirements-on-a-subject)

Also, refer to the Confluent Schema Registry Tutorials which show examples of checking schema compatibility:

- [Confluent Cloud Schema Registry Tutorial](/cloud/current/sr/schema_registry_ccloud_tutorial.html)
- [On-Premises Schema Registry Tutorial](/platform/current/schema-registry/schema_registry_onprem_tutorial.html)

## Format-specific compatibility rules for primitive types, objects, enums, arrays, and unions

Compatibility rules for each schema format are described in their related sections:

- [Avro schema compatibility rules](serdes-develop/serdes-avro.md#sr-avro-schema-compatibility)
- [JSON Schema compatibility rules](serdes-develop/serdes-json.md#sr-json-schema-compatibility)
- [Protobuf schema compatibility rules](serdes-develop/serdes-protobuf.md#sr-protobuf-schema-compatibility)

## Related content

### Confluent Cloud documentation

- [Formats, Serializers, and Deserializers](/cloud/current/sr/fundamentals/serdes-develop/index.html)
- [Compatibility checks](/cloud/current/sr/fundamentals/serdes-develop/index.html#compatibility-checks)

### Confluent Platform documentation

- [Formats, Serializers, and Deserializers](/platform/current/schema-registry/fundamentals/serdes-develop/index.html)
- [Compatibility checks](/platform/current/schema-registry/fundamentals/serdes-develop/index.html#compatibility-checks)
