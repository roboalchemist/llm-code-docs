# Source: https://firebase.google.com/docs/firestore/pipelines/stages/transformation/replace-with.md.txt

> [!WARNING]
> **Preview:** **Firestore in Native mode (with Pipeline operations) for Enterprise
> edition** is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific
> Terms](https://cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage
> descriptions](https://cloud.google.com/products#product-launch-stages).

**Description:**

Replaces fields in the existing document with the fields in a given expression.
The expression can either be a literal map or an expression that evaluates to a
map. If a given expression does not evaluate to a map, this stage returns an
error.

**Syntax:**

    Mode: {full_replace | merge_overwrite_existing | merge_keep_existing}

    replace_with(map: Expr, mode: Mode)

**Mode Behaviour:**

- `full_replace`: Replaces the entire document with the result of the given expression, omitting fields that don't appear in it.
- `merge_overwrite_existing`: Merges the expression with the existing document, overwriting field values in the document with values in the expression
- `merge_keep_existing`: Merges the expression with the existing document, only adding field values when one does not exist in the document.

**Examples:**

Create a <var translate="no">cities</var> collection with the following documents:

### Node.js

    await db.collection('cities').doc('SF').set({name: 'San Francisco', population: 800000, location: {country: 'USA', state: 'California'}});
    await db.collection('cities').doc('TO').set({name: 'Toronto', population:  3000000, province: 'ON', location: {country: 'Canada', province: 'Ontario'}});
    await db.collection('cities').doc('NY').set({name: 'New York', location: {country: 'USA', state: 'New York'}});
    await db.collection('cities').cov('AT').set({name: 'Atlantis', population: null});

#### Using the full_replace mode to get a mutated version of the document

Extract the nested <var translate="no">location</var> field, discarding all other data:

##### Node.js

```javascript
  const names = await db.pipeline()
    .collection("/cities")
    .replace_with(Field.of("location"), "full_replace")
    .execute();
    
```

##### Java

```java
Pipeline.Snapshot names =
    firestore.pipeline().collection("cities").replaceWith(field("location")).execute().get();
```

Which produces the following documents:

    {country: 'USA', state: 'California'},
    {country: 'Canada', province: 'Ontario'},
    {country: 'USA', state: 'New York'},
    {}

#### Using the merge_overwrite_existing mode to set fields

Set the <var translate="no">population</var> field of all documents to 0, overwriting existing
values:

##### Node.js

```javascript
  const censoredResults = await db.pipeline()
    .collection("/cities")
    .replace_with(map("population", 0), "merge_overwrite_existing")
    .execute();
    
```

Which produces the following documents:

    {name: 'San Francisco', population: 0, location: {country: 'USA', state: 'California'}},
    {name: 'Toronto', population: 0, province: 'ON', location: {country: 'Canada', province: 'Ontario'}},
    {name: 'New York', population: 0, location: {country: 'USA', state: 'New York'}},
    {name: 'Atlantis', population: 0}

#### Using the merge_keep_existing mode to add a default value

Setting a default value for <var translate="no">location</var> when it doesn't appear in a
document:

##### Node.js

```javascript
  const defaultedResults = await db.pipeline()
    .collection("/cities")
    .replace_with(map("location", "unknown"), "merge_keep_existing")
    .execute();
    
```

Which produces the following documents:

    {name: 'San Francisco', population: 800000, location: {country: 'USA', state: 'California'}},
    {name: 'Toronto', province: 'ON', population: 3000000, location: {country: 'Canada', province: 'Ontario'}},
    {name: 'New York', location: {country: 'USA', state: 'New York'}},
    {name: 'Atlantis', population: null, location: "unknown"}