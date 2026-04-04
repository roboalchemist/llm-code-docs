# Source: https://firebase.google.com/docs/reference/rules/rules.firestore.Resource.md.txt

# Interface: Resource

# [rules](https://firebase.google.com/docs/reference/rules/rules).[firestore](https://firebase.google.com/docs/reference/rules/rules.firestore).Resource

interface static

The firestore document being read or written.

## Properties

### __name__

non-null [rules.Path](https://firebase.google.com/docs/reference/rules/rules.Path)

The full document name, as a path.

#### Example

    // Check 'name' field from the document
    resource['__name__'] == /databases/(default)/documents/collection/document

### data

non-null [rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map)

Map of the document data.

#### Example

    // Check 'name' field from the document
    resource.data.name == 'John Doe'

### id

non-null [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)

String of the document's key

#### Example

    resource['__name__'] ==
      /databases/(default)/documents/collection/$(resource.id)