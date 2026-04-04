# Source: https://docs.vespa.ai/en/writing/indexing.html.md

# Indexing

 

Refer to the [overview](../learn/overview.html). The primary index configuration is the [schema](../basics/schemas.html).

[services.xml](../reference/applications/services/services.html) configures how indexing is distributed to the nodes, see [multinode-HA](https://github.com/vespa-engine/sample-apps/blob/master/examples/operations/multinode-HA/services.xml) for a full example:

```
```
<container id="feed" version="1.0">
    <document-api />
    <document-processing />
    <nodes count="2" />
</container>
```
```

It is important to configure both `document-api` and `document-processing` to run the document processing on the same nodes as the document API endpoint, to avoid network hops to other nodes (for better throughput). Normally, one will run the indexing preprocessing on these nodes, too, see the [document-processing reference](../reference/applications/services/content.html#document-processing) for a full example.

## Date indexing

Vespa does not have a "date" field type. Best practise is using a [long](../reference/schemas/schemas.html#long) field. If the date is a string in the source data, one can use [to\_epoch\_second](../reference/writing/indexing-language.html#to_epoch_second) to transform into a long-field:

```
schema docs {

    document docs {
        field date_string type string {
            indexing: summary
        }
    }

    field date type long {
        indexing: input date_string | to_epoch_second | attribute | summary
    }

    field last_modified type long {
        indexing: now | attribute | summary
    }
}
```

The synthetic `date` field can be used in queries and [grouping](../querying/grouping.html):

```
```
"fields": {
    "last_modified": 1695995429,
    "date": 1703437243,
    "date_string": "2023-12-24T17:00:43.000Z"
}
```
```

 **Note:** The `date` and `last_modified` fields above are placedoutside the `document` section, as their content is generated from the document input. Use `vespa visit --field-set "[all]"` to dump all fields

Note how [now](../reference/writing/indexing-language.html#now) is used to get current time.

## Execution value example

Accessing the execution value (the value passed into this expression) explicitly is useful when it is to be used as part of an expression such as concatenation. In this example we have a document with a title and an array of sentences, and we prepend each sentence by the document title (and a space), before converting it to a set of embedding vectors (represented by a 2d mixed tensor).

```
input mySentenceArray | for_each { input title . " " . _ } | embed | attribute my2dTensor | index my2dTensor
```

## Choice (||) example

The choice expression is used to provide alternatives if an expression may return null.

```
(input myField1 || "") . " " . (input myField2 || "") | embed | attribute | index
```

In this example two fields are concatenated, but if one of the fields is empty, the empty string is used instead. If the empty string alternatives are not provided, no embedding will be produced if either input field is missing.

## select\_input example

The `select_input` expression is used to choose a statement to execute based on which fields are non-empty in the input document:

```
select_input {
    CX: input CX | set_var CX;
    CA: input CA . " " . input CB | set_var CX;
}
```

This statement executes `input CX | set_var CX;` unless CX is empty. If so, it will execute `input CA . " " . input CB | set_var CX;` unless CA is empty.

## Switch example

The switch-expression behaves similarly to the switch-statement in other programming languages. Each case in the switch-expression consists of a string and a statement. The execution value is compared to each string, and if there is a match, the corresponding statement is executed. An optional default operation (designated by `default:`) can be added to the end of the switch:

```
input mt | switch {
    case "audio": input fa | index;
    case "video": input fv | index;
    default: 0 | index;
};
```

## Indexing statements example

Using indexing statements, multiple document fields can be used to produce one index structure field. For example, the index statement:

```
input field1 . input field2 | attribute field2;
```

combines _field1_ and _field2_ into the attribute named _field2_. When partially updating documents which contains indexing statement which combines multiple fields the following rules apply:

- Only attributes where _all_ the source values are available in the source document update will be updated
- The document update will fail when indexed (only) if _no_ attributes end up being updated when applying the rule above

Example: If a schema has the indexing statements

```
input field1 | attribute field1;
input field1 . input field2 | attribute field2;
```

the following will happen for the different partial updates:

| Partial update contains | Result |
| --- | --- |
| field1 | field1 is updated |
| field2 | The update fails |
| field1 and field2 | field1 and field2 are updated |

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Date indexing](#date-indexing)
- [Execution value example](#execution-value-example)
- [Choice (||) example](#choice-example)
- [select\_input example](#select-input-example)
- [Switch example](#switch-example)
- [Indexing statements example](#combine-values-in-indexing-statements)

