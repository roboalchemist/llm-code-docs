# Source: https://docs.aporia.com/api-reference/custom-segment-syntax.md

# Custom Segment Syntax

In Aporia, [custom segments](https://docs.aporia.com/core-concepts/tracking-data-segments) are defined using SQL-based syntax.

The definition is written as a condition that will be passed to a WHERE clause. The condition should be based only on fields within your model version schema.

The following SQL operators are supported:

```sql
>, <, <=, >=, !=, &, |, =, is, not, or, and
```

{% hint style="warning" %}
Categorical fields are ingested as strings.\
If your segment includes a comparison of a categorical field and a constant value, remember to quote the constant value.
{% endhint %}

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2Fc2Ew2i6ljDCtGexD1CCh%2Fimage.png?alt=media&#x26;token=a811d003-06d8-4619-8501-332e72f8a384" alt=""><figcaption><p>Custom Segments Creation</p></figcaption></figure>

## Examples

1. Assume we have a numeric field "age" and a boolean field "is\_customer" in our schema, we can create a segment based on these fields as follows:

```sql
--Segment of customers above age 23
age > 23 and is_customer = True
```

2. Assume we have a categorical field "partner\_type" and categorical field "deal\_step" in our schema, we can create a segment based on these fields as follows:

```sql
--Segment of all 'Gold' partners with missing deal stage
partner_type = 'Gold' and deal_stage is null
```

3. Assume we have a categorical field "region\_code" in our schema, we can create a segment based on this field as follows:

```sql
--Segment of all data with region_code different than '123'
region_code != '123'
```
