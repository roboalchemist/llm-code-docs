# Source: https://docs.vespa.ai/en/schemas/parent-child.html.md

# Parent/Child

 

Using [document references](../reference/schemas/schemas.html#reference), documents can have parent/child relationships. Use this to join data by [importing](../reference/schemas/schemas.html#import-field) fields from parent documents. Features:

- simplify document operations - one write to update one value
- no de-normalization needed - simplifies data updates and atomic update into all children
- search child documents based on properties from parent documents
- search parent documents only
- use imported fields as part of [visiting](../writing/visiting.html) and [garbage collection](documents.html#document-expiry) with [document selection](../reference/writing/document-selector-language.html#using-imported-fields-in-selections) expressions

Parent/child relationships are not supported in [streaming search](../performance/streaming-search.html#differences-in-streaming-search).

An alternative to parent documents is using arrays or maps of struct fields - this guide covers both.

Common use cases are applications with structured data like commerce (e.g. products with multiple sellers), advertising (advertisers with campaigns with ads, that have budgets that need realtime updates).

High-level overview of documents, imported fields and array fields:

 ![Parent/child and global documents](/assets/img/parent-child.svg)
## Parent documents

Model parent-child relationships by using [references](../reference/schemas/schemas.html#reference) to [global documents](../reference/applications/services/content.html#document). This is like foreign keys in a relational database. Parents can have parents. A document can have references to multiple parents - the parents can be of same or different types.

Using a _reference_, [attribute](../content/attributes.html) fields can be [imported](../reference/schemas/schemas.html#import-field) from parent types into the child's [schema](../basics/schemas.html) and used for matching, ranking, grouping and sorting. A reference is a special attribute with the parent's [document ID](documents.html#document-ids) as value. References are hence weak:

- no cascade delete
- a referenced document can be non-existent - imported fields do not have values in this case

When using parent-child relationships, data does not have to be denormalized as fields from parents are imported into children. Use this to update parent fields to limit number of updates if a field's value is shared between many documents. This also limits the resources (memory / disk) required to store and handle documents on content nodes.

At cluster changes, global documents are merged to new nodes before regular documents. For consistency, a content node is not serving queries before all global documents are synchronized - refer to [content cluster elasticity](../content/elasticity.html).

 **Important:** Cyclic or self [references](../reference/schemas/schemas.html#reference) are not allowed.

Performance notes:

- As parent documents are global, a write executes on all content nodes - see [examples](../performance/sizing-feeding.html#parent-child)
- Node capacity will limit the number of parent documents - there should normally be an order of magnitude fewer parent documents than child documents
- Memory usage grows accordingly. A global document is otherwise equal to a regular document, but each content node must be sized to hold all global documents plus its share of regular documents
- Reference fields add a memory indirection and does not impact query performance much
- [Search performance notes](../performance/feature-tuning.html#parent-child-and-search-performance)
- [Partial updates](../writing/partial-updates.html) to a reference field requires a read-modify-write to the document store and limits throughput.

## Multivalue fields

A document can have [fields](../basics/schemas.html#document-fields) that are arrays or maps of struct. Structs and documents are similar - a set of field name/value pairs. One-to-many mappings can therefore be implemented this way, as an alternative to using parent/child, when each document has a set of properties that belongs to that document.

Refer to [multivalue fields](../searching-multi-valued-fields) for more information.

## Parent or multivalue?

As a rule of thumb, model the items _searched for_ as the document - example products for sale. Shared properties, like vendor, can be model using a parent document, importing a vendor name field - assuming a vendor has many products, and the vendor list is limited. Use arrays or maps of structs for properties documents might have, like shoe size or screen resolution - one can then have a struct field for property name and another for property value, giving a flexible structure for products with an unlimited set of possible properties.

## Parent/child example

In services.xml:

```
```
<content id="mycluster" version="1.0">
    <documents>
        <document type="advertiser" mode="index" global="true" />
        <document type="campaign" mode="index" global="true" />
        <document type="salesperson" mode="index" global="true" />
        <document type="ad" mode="index" />
    </documents>
```
```

Schemas and data:

```
schema advertiser {
    document advertiser {
        field name type string {
            indexing : attribute
        }
    }
}
```

```
```
{
    "put": "id:test:advertiser::cool",
    "fields": {
        "name": "cool"
    }
}
```
```

```
schema campaign {
    document campaign {
        field advertiser_ref typereference\<advertiser\>{
            indexing: attribute
        }
        field budget type int {
            indexing : attribute
        }
    }import field advertiser\_ref.name as advertiser\_name{}
}
```

```
```
[{
    "put": "id:test:campaign::thebest",
    "fields": {
        "advertiser_ref": "id:test:advertiser::cool",
        "budget": 20
    }
},
{
    "put": "id:test:campaign::nextbest",
    "fields": {
        "advertiser_ref": "id:test:advertiser::cool",
        "budget": 10
    }
}]
```
```

```
schema salesperson {
    document salesperson {
        field name type string {
            indexing: attribute
        }
    }
}
```

```
```
{
    "put": "id:test:salesperson::johndoe",
    "fields": {
        "name": "John Doe"
    }
}
```
```

```
schema ad {
    document ad {
        field campaign_ref typereference\<campaign\>{
            indexing: attribute
        }
        field other_campaign_ref type reference<campaign> {
            indexing: attribute
        }
        field salesperson_ref type reference<salesperson> {
            indexing: attribute
        }
    }import field campaign\_ref.budget as budget{}
    import field salesperson_ref.name as salesperson_name {}
    import field campaign_ref.advertiser_name as advertiser_name {}

    document-summary my_summary {
        summary budget {}
        summary salesperson_name {}
        summary advertiser_name {}
    }
}
```

```
```
{
    "put": "id:test:ad::1",
    "fields": {
        "campaign_ref": "id:test:campaign::thebest",
        "other_campaign_ref": "id:test:campaign::nextbest",
        "salesperson_ref": "id:test:salesperson::johndoe"
    }
}
```
```

Document type _ad_ has two references to _campaign_ (via _campaign\_ref_ and _other\_campaign\_ref_) and one reference to _salesperson_ (via _salesperson\_ref_). The _budget_ field from _campaign_ is imported into the _ad_ schema (via _campaign\_ref_) and given the name _budget_. Similarly, the _name_ of _salesperson_ is imported as _salesperson\_name_.

Document type _campaign_ has a reference to _advertiser_ and imports the field _name_ as _advertiser\_name_. This is also imported into _ad_ via _campaign\_ref_ from its grandparent _advertiser_. To use the imported fields in summary, define a document summary _my\_summary_ containing these fields.

 Copyright © 2026 - [Cookie Preferences](#)

