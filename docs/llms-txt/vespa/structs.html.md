# Source: https://docs.vespa.ai/en/schemas/structs.html.md

# Structs

 

This document explains how to use structs in Vespa documents.

## Structs

A [struct](../reference/schemas/schemas.html#struct)is contained in a document and groups one or more fields into a composite type that can be accessed like a single field.

Example:
```
struct email {
        field sender type string {}
        field recipient type string {}
        field subject type string {}
        field content type string {}
    }

    field emails type array<email> {}
```

In this example the struct is part of an[array](../reference/schemas/schemas.html#array). A struct can also be used in a [map](../reference/schemas/schemas.html#map).

## Struct fields

A [struct-field](../reference/schemas/schemas.html#struct-field)defines how a given field in a struct should be indexed and searched.

Note that though a struct-field refers to a field in a struct, the struct-field itself is defined inside a field.

Using the _email_ struct defined previously (see [struct](../reference/schemas/schemas.html#struct)), we can define indexing for a specific field, like _content_:

```
field emails type array<email> {
        indexing: summary
        struct-field content {
            indexing: attribute
            attribute: fast-search
        }
    }
```

The equivalent code (including the struct definition) in Pyvespa is as follows:

```
email_struct = Struct(name="email", fields=[
      Field(name="sender", type="string"),
      Field(name="recipient", type="string"),
      Field(name="subject", type="string"),
      Field(name="content", type="string"),
    ])
    emails_field = Field(name="emails",
                    type="array<email>",
                    indexing=["summary"],
                    struct_fields=[StructField(name="content", indexing=["attribute"], attribute=["fast-search"])]
    )
    schema = Schema(name="schema", document=Document())
    schema.add_fields(emails_field)
    schema.document.add_structs(email_struct)
```

 Copyright © 2026 - [Cookie Preferences](#)

