# Source: https://docs.vespa.ai/en/schemas/inheritance-in-schemas.html.md

# Inheritance in schemas

 

Both document types and full schemas can be inherited to make it easy to design a structured application package with little duplication. Document type inheritance defines a type hierarchy which is also useful for applications that[federate queries](../querying/federation.html)as queries can be written to the common supertype. This guide covers the different elements in the schema that supports inheritance:

1. Schemas
2. Document types
3. Rank profiles
4. Document summaries

 ![Schema elements that support inheritance](/assets/img/inheritance-overview.svg)
 **Note:** Inheritance is not to be confused with [parent/child](parent-child.html), which is a feature to import field values at query time.

## Schema inheritance

A schema that inherits another gets all the content of the parent schema as if it was defined inside the inheriting schema. A schema that inherits another must also (explicitly) inherit its document type:

```
schema booksinherits items{
    document booksinherits items{
        field author type string {
            indexing: summary | index
        }
    }
}
```

## Document type inheritance

A document type can inherit another document type. This will include all fields, also fields declared outside the document block in the schema, rank-profiles defined in the super-schema can then be inherited in the schema of this document, see [Rank profile inheritance](#rank-profile-inheritance) below.

Both schemas _music_ and _books_ have the _title_ field through inheritance:

`my-app/schemas/items.sd`:
```
document items {
    field title type string {
        indexing: summary | index
    }
}
```
`my-app/schemas/books.sd`:
```
schema books {
    document booksinherits items{
        field author type string {
            indexing: summary | index
        }
    }
}
```
`my-app/schemas/music.sd`:
```
schema music {
    document musicinherits items{
        field artist type string {
            indexing: summary | index
        }
    }
}
```

This is equivalent to:

`my-app/schemas/books.sd`:
```
schema books {
    document books {
        field title type string {
            indexing: summary | index
        }
        field author type string {
            indexing: summary | index
        }
    }
}
```
`my-app/schemas/music.sd`:
```
schema music {
    document music {
        field title type string {
            indexing: summary | index
        }
        field artist type string {
            indexing: summary | index
        }
    }
}
```

Notes:

- Multiple inheritance and multiple levels of inheritance is supported.
- Inheriting a document type defined in another content cluster is allowed.
- Overriding fields defined in supertypes is not allowed.
- [Imported fields](../reference/schemas/schemas.html#import-field) defined in supertypes are not inherited.

## Rank profile inheritance

Where fields define the document types, rank profiles define the computations over the documents. Rank profiles can be inherited from rank-profiles defined in the same schema, or defined in another schema when this document inherits the document defined in the schema where the rank profile is defined:

`my-app/schemas/items.sd`:
```
schema items {
    document items {
        field title type string {
            indexing: summary | index
        }
    }

    rank-profile items_ranking_base {
        function title_score() {
            expression: fieldLength(title)
        }
        first-phase {
            expression: title_score
        }
        summary-features {
            title_score
        }
    }
}
```
`my-app/schemas/books.sd`:
```
schema books {
    document booksinherits items{
        field author type string {
            indexing: summary | index
        }
    }

    rank-profile items_rankinginherits items\_ranking\_base{}

    rank-profile items_subschema_rankinginherits items\_ranking\_base{
        first-phase {
            expression: title_score + fieldMatch(author)
        }
        summary-featuresinherits items\_ranking\_base{
            fieldMatch(author)
        }
    }
}
```
`my-app/schemas/music.sd`:
```
schema music {
    document musicinherits items{
        field artist type string {
            indexing: summary | index
        }
    }

    rank-profile items_rankinginherits items\_ranking\_base{}

    rank-profile items_subschema_rankinginherits items\_ranking\_base{
        first-phase {
            expression: title_score + fieldMatch(artist)
        }
        summary-featuresinherits items\_ranking\_base{
            fieldMatch(artist)
        }
    }
}
```

_items\_ranking_ can be considered the "base" ranking. Pro-tip: Set this as the _default_ rank profile by modifying the default [query profile](../querying/query-profiles.html):

`my-app/search/query-profiles/default.xml`:
```
<query-profile id="default">
    <field name="ranking.profile">items_ranking</field>
</query-profile>
```

Queries using _ranking.profile=default_ will then use the first-phase ranking defined in _items.sd_.

Another way to inherit behavior is to override the first-phase ranking in the sub-schemas, still using functions defined in the super-schema (e.g. _title\_score_).

### Summary features

[Summary-features](../reference/schemas/schemas.html#summary-features) and[match-features](../reference/schemas/schemas.html#match-features)are rank features computed during ranking, to be included in [results](../reference/querying/default-result-format.html). These features can be inherited from parent rank profiles - the above example uses `inherits` to include scores from features in super- and sub-schema - example result:

```
```
"summaryfeatures": {
    "fieldMatch(author)": 0,
    "rankingExpression(title_score)": 4
}
```
```

In the examples above, both _books_ and _music_ schemas implement rank profiles with same names (e.g. _items\_subschema\_ranking_), so they can be used in queries spanning both. If a query's rank profile can not be found in a given schema, Vespa's default rank profile [nativerank](../ranking/nativerank.html) is used.

[Inputs](../reference/schemas/schemas.html#inputs) to a rank profile are automatically inherited from the parent rank profile. If a new inputs block is defined in a child rank profile, those inputs will be added cumulatively to those defined in the parent.

## Document summary inheritance

[Document summaries](../querying/document-summaries.html) can inherit others defined in the same or an inherited schema.

`my-app/schemas/books.sd`:
```
schema books {
    document books {
        field title type string {
            indexing: summary | index
        }
        field author type string {
            indexing: summary | index
        }
    }

    document-summary items_summary_tiny {
        summary title {}
    }

    document-summary items_summary_fullinherits items\_summary\_tiny{
        summary author {}
    }
}
```

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Schema inheritance](#schema-inheritance)
- [Document type inheritance](#document-type-inheritance)
- [Rank profile inheritance](#rank-profile-inheritance)
- [Summary features](#summary-features)
- [Document summary inheritance](#document-summary-inheritance)

