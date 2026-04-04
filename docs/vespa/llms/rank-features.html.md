# Source: https://docs.vespa.ai/en/reference/ranking/rank-features.html.md

# Rank Feature Reference

 

This is the list of the rank features in Vespa. These features are available during document ranking for combination into a complete rank score by a[ranking expression](ranking-expressions.html). The features are a combination of coarse grained features suitable for handwritten expressions, and finer grained features suitable for machine learning.

See also [the overview of the ranking framework](../../basics/ranking.html), and[rank feature configuration parameters](rank-feature-configuration.html). Notes:

- Types: All rank feature values are floats. Integers are converted to exact whole value floats. String values are converted to exact whole value floats using a hash function. String literals in ranking expressions are converted using the same hash function, to enable equality tests on string values. 
- Features which are _normalized_ are between 0 and 1, where 0 is always the minimum and 1 the maximum. Normalized features should normally be preferred because they are more easily combined by [ranking expressions](ranking-expressions.html) into a complete normalized score. 
- A query may override _any_ rank feature value by submitting that value as a feature with the query. 
- Some features have parameters. It is always allowed to quote parameters with _"_. Nested quotes are not allowed and must be escaped using _\_. Parameters that can be parsed as feature names may be left unquoted. Examples: _foo(bar(baz(5.5)))_, _foo("bar(\"baz(\\\"5.5\\\")\")")_, _foo("need quote")_

## Feature list

| |
| 
### Query features
 |
| Feature name | Default | Description |
| --- | --- | --- |
| query(_value_) | 0 | 

An application specific feature submitted with the query, see [using the query feature](../../ranking/ranking-expressions-features.html#using-query-variables).

 |
| term(_n_).significance | 0 | 

A normalized number (between 0.0 and 1.0) describing the significance of the term; used as a multiplier or weighting factor by many other text matching rank features.

This should ideally be set by a searcher in the container for global correctness as each node will estimate the significance values from the local corpus. Use the [Java API for significance](https://javadoc.io/doc/com.yahoo.vespa/container-search/latest/com/yahoo/prelude/query/TaggableItem.html#setSignificance(double)) or [YQL annotation for significance](../querying/yql.html#significance).

As a fallback, a significance based on Robertson-Sparck-Jones term weighting is used; it is logarithmic from 1.0 for rare terms down to 0.5 for common terms (those occurring in every document seen).

Note that "rare" is defined as a frequency of 0.000001 or less. This is the term document frequency (how many documents contain the term out of all documents that can be observed), so you cannot get 1.0 as the fallback until you actually have a large number of documents (minimum 1 million) in the same search process.

See [numTerms](rank-feature-configuration.html#term) config.

 |
| term(_n_).weight | 100 | 

The importance of matching this query term given in the query

 |
| term(_n_).connectedness | 0.1 | 

The normalized strength with which this term is connected to the previous term in the query. Must be assigned to query terms in a [searcher](../../applications/searchers.html) using the [Java API for connectivity](https://javadoc.io/doc/com.yahoo.vespa/container-search/latest/com/yahoo/prelude/query/TaggableItem.html#setConnectivity(com.yahoo.prelude.query.Item,double)) or [YQL annotation for connectivity](../querying/yql.html#connectivity).

 |
| queryTermCount | 0 | 

The total number of terms in this query, including both user and synthetic terms in all fields.

 |
| |
| 
### Document features
 |
| Feature name | Default | Description |
| --- | --- | --- |
| fieldLength(_name_) | 1000000 | 

The number of terms in this field if one or more query term matched the field, 1000000 if no query term matched the field.

 |
| attribute(_name_) | null | 

The value of a [tensor](../schemas/schemas.html#tensor) or single value _numeric_ attribute or null/NaN if not set. Use _isNan()_ to check if value is not defined. Using undefined values in ranking expressions leads to undefined behavior.

 |
| attribute(_name_,_n_) | 0 | 

The value at index n (base 0) of a _numeric_ array attribute with the given name. Note that the index number must be explicit, it cannot be the output of an [expression function](../schemas/schemas.html#function-rank). The order of the items in an array attribute is the same as the order they have in the input feed. If items are added using partial updates they are added to the end of the existing items list.

 |
| attribute(_name_,_key_).weight | 0 | 

The weight found at a given key in a weighted set attribute

 |
| attribute(_name_,_key_).contains | 0 | 

1 if the given key is present in a weighted set attribute, 0 otherwise

 |
| attribute(_name_).count | 0 | 

The number of elements in the attribute with the given name.

 |
| tensorFromWeightedSet(_source_,_dimension_) | empty tensor | 

Creates a `tensor<double>` with one mapped dimension from the given integer or string weighted set attribute. The attribute is specified as the full feature name, `attribute(name)`. The _dimension_ parameter is optional. If omitted the dimension name will be the attribute name.

Example: Given the weighted set:

```
{key1:0, key2:1, key3:2.5}
```

_tensorFromWeightedSet(attribute(myField), dim)_ produces:

```
tensor<double>(dim{}):{ {dim:key1}:0.0, {dim:key2}:1.0, {dim:key3}:2.5} }
```

 **Note:** This creates a temporary tensor, and has build cost and extra memory is touched. Tensor evaluation is most effective when the cell types of all tensors are equal - use [cell\_cast](ranking-expressions.html#cell_cast) to enable optimizations. Also, duplicating the field in the schema to a native tensor instead of creating from a set can increase performance.
 |
| tensorFromLabels(_attribute_,_dimension_) | empty tensor | 

Creates a `tensor<double>` with one mapped dimension from the given single value or array attribute. The value(s) must be integers or strings. The attribute is specified as the full feature name, `attribute(name)`. The _dimension_ parameter is optional. If omitted the dimension name will be the attribute name.

Example: Given an attribute field `myField` containing the array value:

```
[v1, v2, v3]
```

_tensorFromLabels(attribute(myField), dim)_ produces:

```
tensor<double>(dim{}):{ {dim:v1}:1.0, {dim:v2}:1.0, {dim:v3}:1.0} }
```

See _tensorFromWeightedSet_ for performance notes.

 |
| tensorFromStructs(_attribute_,_key_,_value_,_type_) | empty tensor | 

Creates a `tensor<type>` with one mapped dimension from the given `array<struct>` attribute. Keys are taken from the struct field _key_ and values from the struct field _value_. The resulting tensor will have one mapped dimension named after the _key_ field. The _type_ parameter is required and must be `float` or `double`. The function takes exactly four arguments.

Example: Given an `array<struct>` attribute `items` with fields `name` (string) and `price` (float):

```
tensorFromStructs(attribute(items), name, price, float)
```

```
tensor<float>(name{}):{ {name:apple}:1.5, {name:banana}:0.75, {name:cherry}:2.25 }
```

Example: Integer keys and float values:

```
tensorFromStructs(attribute(ids), id, score, double)
```

```
tensor(id{}):{ {id:100}:10.5, {id:200}:20.75, {id:300}:30.25 }
```

_Details:_ Empty or missing arrays yield an empty tensor of the requested type. The first argument must be an `attribute(...)` source.

See _tensorFromWeightedSet_ for performance notes.

 |
| |
| 
### Field match features - normalized
 |
| fieldMatch features provide a good measure of the degree to which a query matches the text of a field, but are expensive to calculate and therefore often only suitable for [second-phase](../../ranking/phased-ranking.html) ranking expressions. See the [string segment match](string-segment-match.html) document for details on the algorithm computing this rank-feature set. Note that even using a fine-grained sub features like fieldMatch(_name_).absoluteOccurrence will have the same complexity and cost as using the general top level fieldMatch(_name_) feature. |
| Feature name | Default | Description |
| --- | --- | --- |
| fieldMatch(_name_) | 0 | 

A normalized measure of the degree to which this query and field matched (default, the long name of this is `match`). Use this if you do not want to create your own combination function of more fine-grained fieldmatch features.

 |
| fieldMatch(_name_).proximity | 0 | 

Normalized proximity - a value which is close to 1 when matched terms are close _inside each segment_, and close to zero when they are far apart inside segments. Relatively more connected terms influence this value more. This is absoluteProximity/average connectedness for the query terms for this field.

Note that if all the terms are far apart, the proximity will be 1, but the number of segments will be high. Proximity is only concerned with closeness within segments, a total score must also take the number of segments into account.

 |
| fieldMatch(_name_).completeness | 0 | 

The normalized total completeness, where field completeness is more important:

`queryCompleteness *
        ( 1 - fieldCompletenessImportance )
        + fieldCompletenessImportance * fieldCompleteness`

 |
| fieldMatch(_name_).queryCompleteness | 0 | 

The normalized ratio of query tokens matched in the field:

`matches/query terms searching this field` |
| fieldMatch(_name_).fieldCompleteness | 0 | 

The normalized ratio of query tokens which was matched in the field:

`matches/fieldLength` |
| fieldMatch(_name_).orderness | 0 | 

A normalized metric of how well the order of the terms agrees in the chosen segments:

`1-outOfOrder/pairs`

 |
| fieldMatch(_name_).relatedness | 0 | 

A normalized measure of the degree to which different terms are related (occurring in the same segment):

`1-(segments-1)/(matches-1)`

 |
| fieldMatch(_name_).earliness | 0 | 

A normalized measure of how early the first segment occurs in this field.

 |
| fieldMatch(_name_).longestSequenceRatio | 0 | 

A normalized metric of the relative size of the longest sequence:

`longestSequence/matches`

 |
| fieldMatch(_name_).segmentProximity | 0 | 

A normalized metric of the closeness (inverse of spread) of segments in the field:

`1-segmentDistance/fieldLength`

 |
| fieldMatch(_name_).unweightedProximity | 0 | 

The normalized proximity of the matched terms, not taking term connectedness into account. This number is close to 1 if all the matched terms are following each other in sequence, and close to 0 if they are far from each other or out of order.

 |
| fieldMatch(_name_).absoluteProximity | 0 | 

Returns the normalized proximity of the matched terms, weighted by the connectedness of the query terms. This number is 0.1 if all the matched terms are and have default or lower connectedness, close to 1 if they are following in sequence and have a high connectedness, and close to 0 if they are far from each other in the segments or out of order.

 |
| fieldMatch(_name_).occurrence | 0 | 

Returns a normalized measure of the number of occurrences of the terms of the query. This is 1 if there are many occurrences of the query terms _in absolute terms, or relative to the total content of the field_, and 0 if there are none.

This is suitable for occurrence in fields containing regular text.

 |
| fieldMatch(_name_).absoluteOccurrence | 0 | 

Returns a normalized measure of the number of occurrence of the terms of the query:

$$\frac{\sum\_{\text{all query terms}}(min(\text{number of occurrences of the term},maxOccurrences))}{(\text{query term count} × 100)}$$

This is 1 if there are many occurrences of the query terms, and 0 if there are none.

This number is not relative to the field length, so it is suitable for uses of occurrence to denote relative importance between matched terms (i.e. fields containing keywords, not normal text).

 |
| fieldMatch(_name_).weightedOccurrence | 0 | 

Returns a normalized measure of the number of occurrence of the terms of the query, weighted by term weight. This number is close to 1 if there are many occurrences of highly weighted query terms, in absolute terms, or relative to the total content of the field, and 0 if there are none.

 |
| fieldMatch(_name_).weightedAbsoluteOccurrence | 0 | 

Returns a normalized measure of the number of occurrence of the terms of the query, taking weights into account so that occurrences of higher weighted query terms has more impact than lower weighted terms.

This is 1 if there are many occurrences of the highly weighted terms, and 0 if there are none.

This number is not relative to the field length, so it is suitable for uses of occurrence to denote relative importance between matched terms (i.e. fields containing keywords, not normal text).

 |
| fieldMatch(_name_).significantOccurrence | 0 | 

Returns a normalized measure of the number of occurrence of the terms of the query _in absolute terms, or relative to the total content of the field_, weighted by term significance.

This number is 1 if there are many occurrences of the highly significant terms, and 0 if there are none.

 |
| |
| 
### Field match features - normalized and relative to the whole query
 |
| Feature name | Default | Description |
| --- | --- | --- |
| fieldMatch(_name_).weight | 0 | 

The normalized weight of this match relative to the whole query: The sum of the weights of all _matched_ terms/the sum of the weights of all _query_ terms. If all the query terms were matched, this is 1. If no terms were matched, or these matches has weight zero this is 0.

As the sum of this number over all the terms of the query is always 1, sums over all fields of normalized rank features for each field multiplied by this number for the same field will produce a normalized number.

Note that this scales with the number of matched query terms in the field. If you want a component which does not, divide by matches.

 |
| fieldMatch(_name_).significance | 0 | 

Returns the normalized term significance of the terms of this match relative to the whole query: The sum of the significance of all _matched_ terms/the sum of the significance of all _query_ terms. If all the query terms were matched, this is 1. If no terms were matched, or if the significance of all the matched terms is zero, this number is zero.

This metric has the same properties as weight.

See the [term(n).significance](#term(n).significance) feature for how the significance for a single term is calculated.

 |
| fieldMatch(_name_).importance | 0 | 

Returns the average of significance and weight. This has the same properties as those metrics.

 |
| |
| 
### Field match features - not normalized
 |
| Feature name | Default | Description |
| --- | --- | --- |
| fieldMatch(_name_).segments | 0 | 

The number of field text segments which are needed to match the query as completely as possible

 |
| fieldMatch(_name_).matches | 0 | 

The total number of query terms which was matched in this field

 |
| fieldMatch(_name_).degradedMatches | 0 | 

The number of degraded query terms which was matched in this field. A degraded term is a term where no occurrence information is available during calculation. The number of degraded matches is less than or equal to the total number of matches.

 |
| fieldMatch(_name_).outOfOrder | 0 | 

The total number of out of order token sequences _within_ matched field segments

 |
| fieldMatch(_name_).gaps | 0 | 

The total number of position jumps (backward or forward) within field segments

 |
| fieldMatch(_name_).gapLength | 0 | 

The summed length of all gaps within segments

 |
| fieldMatch(_name_).longestSequence | 0 | 

The size of the longest matched continuous, in-order sequence in the field

 |
| fieldMatch(_name_).head | 0 | 

The number of tokens in the field preceding the start of the first matched segment

 |
| fieldMatch(_name_).tail | 0 | 

The number of tokens in the field following the end of the last matched segment

 |
| fieldMatch(_name_).segmentDistance | 0 | 

The sum of the distance between all segments making up a match to the query, measured as the sum of the number of token positions separating the _start_ of each _field_ adjacent segment.

 |
| |
| 
### Query and field similarity
 |
| Normalized feature set measuring the approximate _similarity_ between a field and the query. These features are suitable in cases where the query is as large as the field (i.e. is a document) such that we are interested in the similarity between the query and the entire field. They are cheap to compute even if the query is large. |
| Feature name | Default | Description |
| --- | --- | --- |
| textSimilarity(_name_) | 0 | 

A weighted sum of the individual similarity measures.

 |
| textSimilarity(_name_).proximity | 0 | 

A measure of how close together the query terms appear in the field.

 |
| textSimilarity(_name_).order | 0 | 

A measure of the order in which the query terms appear in the field compared to the query.

 |
| textSimilarity(_name_).queryCoverage | 0 | 

A measure of how much of the query the field covers when a single term from the field can only cover a single term in the query. Query term weights are used during normalization.

 |
| textSimilarity(_name_).fieldCoverage | 0 | 

A measure of how much of the field the query covers when a single term from the query can only cover a single term in the field.

 |
| |
| 
### Query term and field match features
 |
| Feature name | Default | Description |
| --- | --- | --- |
| fieldTermMatch(_name_,_n_).firstPosition | 1000000 | 

The position of the first occurrence of this query term in this index field. [numTerms](rank-feature-configuration.html#fieldTermMatch) configuration

 |
| fieldTermMatch(_name_,_n_).occurrences | 0 | 

The number of occurrences of this query term in this index field

 |
| matchCount(_name_) | 0 | 

Returns number of times any term in the query matches this index/attribute field.

 |
| matches(_name_) | 0 | 

Returns 1 if the index/attribute field with the given name is matched by the query.

 |
| matches(_name_,_n_) | 0 | 

Returns 1 if the index/attribute field with the given name is matched by the query term with position _n_.

 |
| termDistance(_name_,_x_,_y_).forward | 1000000 | 

The minimum distance between the occurrences of term _x_ and term _y_ in this index field. Term _x_ occurs before term _y_.

 |
| termDistance(_name_,_x_,_y_).forwardTermPosition | 1000000 | 

The position of the occurrence of term _x_ in this index field used for the forward distance.

 |
| termDistance(_name_,_x_,_y_).reverse | 1000000 | 

The minimum distance between the occurrences of term _y_ and term _x_ in this index field. Term _y_ occurs before term _x_.

 |
| termDistance(_name_,_x_,_y_).reverseTermPosition | 1000000 | 

The position of the occurrence of term _y_ in this index field used for the reverse distance.

 |
| |
| 
### Features for indexed multivalue string fields
 |
| Feature name | Default | Description |
| --- | --- | --- |
| elementCompleteness(_name_).completeness | 0 | 

A weighted combination of fieldCompleteness and queryCompleteness for the element in the field that produces the highest value for this output after the elements weight is factored in. The weighting can be adjusted using [elementCompleteness(name).fieldCompletenessImportance](rank-feature-configuration.html#elementCompleteness).

 |
| elementCompleteness(_name_).fieldCompleteness | 0 | 

The field completeness of the best matching element. This is calculated as:

`max( (number of query terms matched in the element) /
      (element size), 1.0)`.

 |
| elementCompleteness(_name_).queryCompleteness | 0 | 

The query completeness of the best matching element. This is calculated as:

`(sum of weight for query terms matched in the element) /
      (sum of weight for query terms searching the field)`.

 |
| elementCompleteness(_name_).elementWeight | 0 | 

The weight of the best matching element, starting from the default - i.e., negative weights will return 0.

 |
| elementSimilarity(_name_) | 0 | 

Aggregated similarity between the query and individual field elements. The same sub-scores used by the `textSimilarity` feature are calculated for each individual element in the field. The final output is calculated as the maximum of the combined element similarity measures (similarity measures are combined the same way as the default output of the `textSimilarity` feature) multiplied with the element weight which is 1 for arrays, and the supplied weights for indexed weighted sets.

This is a flexible feature; how sub-scores are combined for each element and how element scores are aggregated may be configured. You may also add additional outputs if you want to capture multiple signals from a single field. Use [elementSimilarity](rank-feature-configuration.html#elementSimilarity) to customize this feature.

 |
| |
| 
### Attribute match features - normalized
 |
| Feature name | Default | Description |
| --- | --- | --- |
| attributeMatch(_name_) | 0 | 

A normalized measure of the degree to which this query and field matched. This is currently the same as completeness. Note that depending on what the attribute is used for, this may or may not be a suitable metric. If the attribute is a weighted set representing counts of items (like tags), `normalizedWeight` is probably a better metric.

 |
| attributeMatch(_name_).completeness | 0 | 

The normalized total completeness, where field completeness is more important:

`queryCompleteness * ( 1 - fieldCompletenessImportance +
       fieldCompletenessImportance * fieldCompleteness )`

 |
| attributeMatch(_name_).queryCompleteness | 0 | 

The query completeness for this attribute:

`matches/the number of query terms searching this attribute`

 |
| attributeMatch(_name_).fieldCompleteness | 0 | 

The normalized ratio of query tokens which was matched in the field. For arrays: `matches/array length` For weighted sets: `sum of weight of matched terms/sum of weights of entire set`. This is relatively expensive to calculate for large weighted sets.

 |
| attributeMatch(_name_).normalizedWeight | 0 | 

A number which is close to 1 if the attribute weights of most matches in a weighted set are high (relative to [maxWeight](rank-feature-configuration.html#attributeMatch)), 0 otherwise

 |
| attributeMatch(_name_).normalizedWeightedWeight | 0 | 

A number which is close to 1 if the attribute weights of most matches in a weighted set are high (relative to [maxWeight](rank-feature-configuration.html#attributeMatch)), and where highly weighted query terms has more impact, 0 otherwise

 |
| closeness(_dimension_,_name_) | 0 | 

Used with the [nearestNeighbor](../querying/yql.html#nearestneighbor) query operator. A number which is close to 1 when a point vector in the document is close to a matching point vector in the query. The document vectors and the query vector must be the same tensor type, with one indexed dimension of size N, representing a point in an N-dimensional space.

- _dimension_: Specifies the dimension of _name_. This must be either the string `field` or the string `label`. 

- _name_: The value of the field name or label. 

 **Note:**`closeness()` is calculated **only** based on the vectors matched with nearestNeighbor operator. This means that the value of `closeness()` is not necessarily calculated based on the same vector returned by `closest()` rank feature if nearestNeighbor search is approximate, as `closest()` will be calculated based on _all_ specified document vectors.

The output value is $$ closeness(dimension,name) = \frac{1.0}{1.0 + distance(dimension,name)}$$

When the tensor field stores multiple vectors per document, the minimum distance between the vectors of a document and the query vector is used in the calculation above.

 |
| freshness(_name_) | 0 | 

A number which is close to 1 if the timestamp in attribute _name_ is recent compared to the current time compared to [maxAge](rank-feature-configuration.html#freshness):

`max( 1-age(name)/maxAge , 0 )`

Scales linearly with age, see [freshness plot](#freshness).

 |
| freshness(_name_).logscale | 0 | 

A logarithmic-shaped freshness; also goes from 1 to 0, but looks like [freshness plot](#freshness). The function is based on `-log(age(name) + scale)` and is calculated as:

$$\frac{log(maxAge + scale) - log(age(name) + scale)}{log(maxAge + scale) - log(scale)}$$

where scale is defined using [halfResponse and maxAge](rank-feature-configuration.html#freshness):

$$\frac{-halfResponse^2}{2 × halfResponse - maxAge}$$

When `age(name) == halfResponse` the function output is 0.5.

 |
| |
| 
### Attribute match features - normalized and relative to the whole query
 |
| Feature name | Default | Description |
| --- | --- | --- |
| attributeMatch(_name_).weight | 0 | 

This has the same semantics as fieldMatch(_name_).weight.

 |
| attributeMatch(_name_).significance | 0 | 

This has the same semantics as fieldMatch(_name_).significance.

 |
| attributeMatch(_name_).importance | 0 | 

Returns the average of significance and weight. This has the same properties as those metrics.

 |
| |
| 
### Attribute match features - not normalized
 |
| Feature name | Default | Description |
| --- | --- | --- |
| attributeMatch(_name_).matches | 0 | 

The number of query terms which was matched in this attribute

 |
| attributeMatch(_name_).totalWeight | 0 | 

The sum of the weights of the attribute keys matched in a weighted set attribute

 |
| attributeMatch(_name_).averageWeight | 0 | 

totalWeight/matches

 |
| attributeMatch(_name_).maxWeight | 0 | 

The maximum weight of the attribute keys matched in a weighted set attribute

 |
| closest(_name_) | {} | 

Used with the [nearestNeighbor](../querying/yql.html#nearestneighbor) query operator and a tensor field attribute _name_ storing multiple vectors per document. This feature returns a tensor with one or more mapped dimensions and one point with a value of 1.0, where the label of that point indicates which document vector was closest to the query vector in the nearest neighbor search.

Given a tensor field with type `tensor<float>(m{},x[3])` used with the _nearestNeighbor_ operator, an example output of this feature is:

```
tensor<float>(m{}):{ 3: 1.0 }
```

In this example, the document vector with label _3_ in the mapped _m_ dimension was closest to the query vector.

 |
| closest(_name_,_label_) | {} | 

Used with the [nearestNeighbor](../querying/yql.html#nearestneighbor) query operator tagged with a [label](../../ranking/multivalue-query-operators.html#raw-scores-and-query-item-labeling) _label_ and a tensor field attribute _name_ storing multiple vectors per document.

See [closest(name)](#closest(name)) for details.

 |
| distance(_dimension_,_name_) | max double value | 

Used with the [nearestNeighbor](../querying/yql.html#nearestneighbor) query operator. A number which is close to 0 when a point vector in the document is close to a matching point vector in the query. The document vectors and the query vector must be the same tensor type, with one indexed dimension of size N, representing a point in an N-dimensional space.

- _dimension_: Specifies the dimension of _name_. This must be either the string `field` or the string `label`. 

- _name_: The value of the field name or label. 

The output value depends on the [distance metric](../schemas/schemas.html#distance-metric) used. The default is the Euclidean distance between the "n"-dimensional query point "d" and the point "d" in the document tensor field: $$ distance = \sqrt{\sum\_{i=1}^n (q\_i - d\_i)^2} $$

When the tensor field stores multiple vectors per document, the minimum distance between the vectors of a document and the query vector is used in the calculation above.

 |
| age(_name_) | 10B | 

The document age in seconds relative to the unit time value stored in the attribute having this name

 |
| |
| 
### Features combining multiple fields and attributes
 |
| Feature name | Default | Description |
| --- | --- | --- |
| match | 0 | 

A normalized average of the fieldMatch and attributeMatch scores of all the searched fields and attributes, where the contribution of each field and attribute is weighted by its _weight_ setting.

 |
| match.totalWeight | 0 | 

The sum of the weight settings of all the field and attributes searched by the query

 |
| match.weight._name_ | 100 | 

The (schema) weight setting of a field or attribute

 |
| |
| 
### Rank scores
 |
| Feature name | Default | Description |
| --- | --- | --- |
| bm25(field) | 0 | 

Calculates the [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25) ranking function over the given [indexed string field](../schemas/schemas.html#indexing-index). This feature is cheap to compute, about 3-4 times faster than nativeRank, while still providing a good rank score quality wise. This feature is a good candidate for usage in a first phase ranking function when ranking text documents. Note that the field must be enabled to be used with the bm25 feature; set the _enable-bm25_ flag in the [index](../schemas/schemas.html#index) section of the field definition. See the [BM25 Reference](../../ranking/bm25.html) for more detailed information.

 |
| elementwise(bm25(field),dimension,cell\_type) | `tensor<cell_type>(dimension{}):{}` | 

Calculates the [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25) ranking function over each element in the given _multi-valued_ [indexed string field](../schemas/schemas.html#indexing-index) and creates a tensor with a single mapped dimension containing the bm25 score for each matching element. The element indexes (starting at 0) are used as dimension labels. This feature is more expensive than [bm25](#bm25), does not need the _enable-bm25_ flag and can be tuned with [rank properties](rank-feature-configuration.html#elementwise-bm25).

The _cell\_type_ parameter can be omitted (the default value is `double`) except when setting rank properties.

Example: If the `content` field is of type `array<string>` where query terms are found in elements 2 and 5 then the feature `elementwise(bm25(content),x,float)` as a summary feature might be shown as:

```
"elementwise(bm25(content),x,float)": {
  "type": "tensor(x{})", "cells": { "2": 0.5112776, "5": 0.1021805 } }
```
 |
| nativeRank | 0 | 

A reasonably good rank score which is computed cheaply by Vespa. This value only is a good candidate first phase ranking function, and is the default used in the default rank profile. The value computed by this function may change between Vespa versions. See the [native rank reference](nativerank.html) for more information.

 |
| nativeRank(field,...) | 0 | 

Same as _nativeRank_, but only the given set of fields are used in the calculation.

 |
| nativeFieldMatch | 0 | 

Captures how well query terms match in index fields. Used by _nativeRank_. See the [native rank reference](nativerank.html) for more information.

 |
| nativeFieldMatch(field,...) | 0 | 

Same as _nativeFieldMatch_, but only the given set of index fields are used in the calculation.

 |
| nativeProximity | 0 | 

Captures how near matched query terms occur in index fields. Used by _nativeRank_. See the [native rank reference](nativerank.html) for more information.

 |
| nativeProximity(field,...) | 0 | 

Same as _nativeProximity_, but only the given set of index fields are used in the calculation.

 |
| nativeAttributeMatch | 0 | 

Captures how well query terms match in attribute fields. Used by _nativeRank_. See the [native rank reference](nativerank.html) for more information.

 |
| nativeAttributeMatch(field,...) | 0 | 

Same as _nativeAttributeMatch_, but only the given set of attribute fields are used in the calculation.

 |
| nativeDotProduct(field) | 0 | 

Calculates the sparse dot product between query term weights and match weights for the given field. Example: A weighted set string field X:

```
"X": {
    "x": 10,
    "y": 20,
    "z": 30
}
```

For the query (x!2 OR y!4), the nativeDotProduct(X) feature will have the value 100 (10\*2+20\*4) for that document.

 **Note:**`nativeDotProduct` and `nativeDotProduct(field)` is less optimal for computing the dot product - consider using [dotProduct(name,vector)](#dotProduct(name,vector)).
 |
| nativeDotProduct | 0 | 

Calculates the sparse dot product between query term weights and match weights as above, but for all term/field combinations.

 |
| firstPhase | 0 | 

The value of the rank score calculated in the first phase (unavailable in first phase ranking expressions)

 |
| secondPhase | 0 | 

The value of the rank score calculated in the second phase (unavailable in first phase and second phase ranking expressions)

 |
| firstPhaseRank | max double value | 

The rank of the document after first phase within the content node when selecting which documents to rerank in second phase. The best document after first phase has rank 1, the second best 2, etc. The feature returns the default value for documents not selected for second phase ranking and for unsupported cases ([streaming search](../../performance/streaming-search.html#differences-in-streaming-search), [summary features](../schemas/schemas.html#summary-features), first phase expressions). Multiple documents can have the same _firstPhaseRank_ value in multi-node configurations.

 |
| relevanceScore | - | 

The value of the rank score calculated either in the first or (when defined) in the second phase (unavailable in first phase and second phase ranking expressions) (since 8.559.30).

 |
| |
| 
### Global features
 |
| Feature name | Default | Description |
| --- | --- | --- |
| globalSequence | n/a | 

A global sequence number computed as (1 \<\< 48) - (LocalDocumentId \<\< 16 || [distribution-key](../applications/services/content.html#node)). This will give a global sequence to documents. This is a cheap way of having stable ordering of documents. Note the large range of this value. Also note that if the system is not stable, e.g. if documents move around due to new nodes coming in, or nodes being removed, it will no longer be stable as documents might be found in a different replica. If you need true global ordering we suggest assigning a unique numeric id to your documents as an [attribute](../schemas/schemas.html#attribute) field and use the [attribute(name)](#attribute(name)) feature.

 |
| now | n/a | 

Time at which the query is executed in unix-time (seconds since epoch)

 |
| random | n/a | 

A pseudorandom number in the range [0,1\> which is drawn once per document during rank evaluation. By default, the current time in microseconds is used as a seed value. Users can specify a seed value by setting [random.seed](rank-feature-configuration.html#random) in the rank profile. If you need several independent random numbers the feature can be named like this: `random(foo)`, `random(bar)`.

 |
| random.match | n/a | 

A pseudorandom number in the range [0,1\> that is stable for a given hit. This means that a hit will always receive the same random score (on a single node). If it is required that the scores be different between different queries, specify a seed value dependent upon the query. By default, the seed value is 1024. Users can specify a seed value by adding the query parameter [rankproperty.random.match.seed=\<value\>](../api/query.html#ranking.properties). If you need several independent random numbers the feature can be named like this: `random(foo).match`, `random(bar).match`.

 |
| randomNormal(_mean_,_stddev_) | 0.0,1.0 | 

Same as [random](#random), except the random number is drawn from the Gaussian distribution using the supplied mean and stddev parameters. Can be called without parameters; default values are assumed. Seed is set similarly as _random_. If you need several independent random numbers with the same parameters, the feature can be named like this: `randomNormal(0.0,1.0,foo)`, `randomNormal(0.0,1.0,bar)`. If the parameters to _randomNormal_ are not the same, you do not need to supply an additional name, e.g. `randomNormal(0.0, 0.1)` and `randomNormal(0.0, 0.5)` results in two independent values.

 |
| randomNormalStable(_mean_,_stddev_) | 0.0,1.0 | 

Same as [randomNormal](#randomNormal(mean,stddev)), except that the generated number is stable for a given hit, similar to [random.match](#random.match).

 |
| constant(_name_) | n/a | 

Returns the [constant](../schemas/schemas.html#constant) tensor value.

 |
| |
| 
### Match operator scores
 |
| See [Raw scores and query item labeling](../../ranking/multivalue-query-operators.html#raw-scores-and-query-item-labeling) |
| Feature name | Default | Description |
| --- | --- | --- |
| rawScore(_field_) | 0 | 

The sum of all raw scores produced by match operators for this field.

 |
| itemRawScore(_label_) | 0 | 

The raw score produced by the query item with the given label.

 |
| |
| 
### Geo search
 |
| These features are for ranking on the distances between geographical coordinates, i.e. points on the surface of the earth defined by latitude/longitude pairs. See the main documentation for [Geo Search](../../querying/geo-search.html). 
 **Note:** Some of these features have the same names as features used with the [nearestNeighbor](../querying/yql.html#nearestneighbor) query operator. Take care not to get them mixed up!
 |
| Feature name | Default | Description |
| --- | --- | --- |
| closeness(_name_) | 0 | 

A number which is close to 1 if the position in attribute _name_ is close to the query position compared to [maxDistance](rank-feature-configuration.html#closeness):

`max(1-distance(name)/maxDistance , 0)`

Scales linearly with distance, see [closeness plot](#closeness).

 |
| closeness(_name_).logscale | 0 | 

A logarithmic-shaped closeness; like normal closeness it goes from 1 to 0, but looks like [closeness plot](#closeness). The function is a logarithmic fall-off based on `log(distance + scale)` and is calculated as:

$$closeness(name).logscale = \frac{log(maxDistance + scale) - log(distance(name) + scale))}{(log(maxDistance + scale) - log(scale))}$$

where scale is defined using [halfResponse and maxDistance](rank-feature-configuration.html#closeness):

$$scale = \frac{halfResponse^2}{(maxDistance - 2 × halfResponse)}$$

When `distance(name) == halfResponse` the function output is 0.5; halfResponse should be less than `maxDistance/2` since that means adding a certain distance when you are close matters more than adding the same distance when you're already far away.

 |
| distance(_name_) | 6400M | 

The Euclidean distance from the query position to the given position attribute in millionths of degrees (about 10 cm). If there are multiple positions in the query, items that actually search in _name_ is preferred. Also: if multiple query items search in _name_, or _name_ is an array of positions, or both, the closest distance found is returned.

 |
| distance(_name_).km | 711648.5 | 

As above, but scaled, so it uses the kilometer as unit of distance, instead of "micro-degrees".

 |
| distance(_name_).index | -1 | 

The array index of the closest position found. Useful when _name_ is of `array<position>` type.

 |
| distance(_name_).latitude | 90 | 

The latitude (geographical north-south coordinate) of the closest position found. In range from -90.0 (South Pole) to +90.0 (North Pole). Useful when _name_ is of `array<position>` type.

 |
| distance(_name_).longitude | -180 | 

The latitude (geographical east-west coordinate) of the closest position found. In range from -180.0 (extreme west) to +180.0 (extreme east). Useful when _name_ is of `array<position>` type.

 |
| distanceToPath(_name_).distance | 6400M | 

The Euclidean distance from a path through 2d space given in the query to the given position attribute in millionths of degrees. This is useful e.g. for finding the closest locations to a given road. The query path is set in the [rankproperty.distanceToPath(_name_).path](../api/query.html#ranking.properties) query parameter, using syntax `"(x1,y1,x2,y2,..)"` also in millionth of degrees, see the [distance to path](../../querying/geo-search.html#distance-to-path) example. The closest point along the path is referred to as the _intersection_.

 **Note:** For documents with multiple locations, only the closest location is used for ranking purposes.
 |
| distanceToPath(_name_).traveled | 1 | 

The normalized distance along the query path traveled before intersection (0.0 indicates start of path, 0.5 is middle, and 1.0 is end of path).

 |
| distanceToPath(_name_).product | 0 | 

The cross-product of the intersected path segment and the intersection-to-document vector. Given that the document was found to lie closest to the path element `A->B`, the intersected path segment vector is `[B.x - A.x, B.y - A.y]`. Furthermore, given that the intersection of that path element occurred at point `I` for document location `D`, the intersection-to-document vector is `[I.x - D.x, I.y - D.y]`. This is useful e.g. for finding what side of a path a document exists by looking at the sign of this value.

 |
| |
| 
### Utility features
 |
| Feature name | Default | Description |
| --- | --- | --- |
| foreach(_dimension_, _variable_, _feature_, _condition_, _operation_) | n/a | 

_foreach_ iterates over a set of feature output values and performs an operation on them. Only the values where the condition evaluates to true are considered for the operation. The result of this operation is returned.

- _dimension_: Specifies what to iterate over. This can be: 
  - _terms_: All query term indices, from 0 and up to [maxTerms](rank-feature-configuration.html#foreach). 
  - _fields_: All index field names. 
  - _attributes_: All attribute field names. 

- _variable_: The name of the variable 'storing' each of the items you are iterating over. 
- _feature_: The name of the feature you want to use the output value from. Use the _variable_ as part of the feature name, and for each item you iterate over this _variable_ is replaced with the actual item. Note that the variable replacement is a simple string replace, so you should use a variable name that is not in conflict with the feature name. 
- _condition_: The condition used on each feature output value to find out if the value should be considered by the operation. The condition can be: 
  - _\>a_: Use feature output if greater than number a. 
  - _\<a_: Use feature output if less than number a. 
  - _true_: Use all feature output values. 

- _operation_: The operation you want to perform on the feature output values. This can be: 
  - _sum_: Calculate the sum of the values. 
  - _product_: Calculate the product of the values. 
  - _average_: Calculate the average of the values. 
  - _max_: Find the max of the values. 
  - _min_: Find the min of the values. 
  - _count_: Count the number of values. 

Let's say you want to calculate the average score of the _fieldMatch_ feature for all index fields, but only consider the scores larger than 0. Then you can use the following setup of the _foreach_ feature:

`foreach(fields,N,fieldMatch(N), ">0", average)`.

Note that when using the conditions _\>a_ and _\<a_ the arguments must be quoted.

You can also specify a ranking expression in the _foreach_ feature by using the _rankingExpression_ feature. The _rankingExpression_ feature takes the expression as the first and only parameter and outputs the result of evaluating this expression. Let's say you want to calculate the average score of the squared _fieldMatch_ feature score for all index fields. Then you can use the following setup of the _foreach_ feature:

`foreach(fields, N, rankingExpression("fieldMatch(N)*fieldMatch(N)"), true, average)`

Note that you must quote the expression passed in to the _rankingExpression_ feature.

 |
| dotProduct(_name_,_vector_) | 0 | 

 **Note:** Most dot product use cases are better solved using [tensors](../../ranking/tensor-user-guide.html).

The sparse dot product of the vector represented by the given weighted set attribute and the vector sent down with the query.

You can also do an ordinary full dotproduct by using arrays instead of weighted sets. This will be a lot faster when you have full vectors in the document with more than 5-10% non-zero values. You are also then not limited to integer weights. All the numeric datatypes can be used with arrays, so you have full floating point support. The 32 bit floating point type yields the fastest execution.

- _name_: The name of the weighted set string/integer or array of numeric attribute. 
- _vector_: The name of the vector sent down with the query. 

Each unique string/integer in the weighted set corresponds to a dimension and the belonging weight is the vector component for that dimension. The query vector is set in the [rankproperty.dotProduct._vector_](../api/query.html#ranking.properties) query parameter, using syntax `{d1:c1,d2:c2,…}` where _d1_ and _d2_ are dimensions matching the strings/integers in the weighted set and _c1_ and _c2_ are the vector components (floating point numbers). The number of dimensions in the weighted set and the query vector do not need to be the same. When calculating the dot product we only use the dimensions present in both the weighted set and the query vector.

When using an array the dimensions is a positive integer starting at 0. If the query is sparse all non given dimensions are zero. That also goes for dimensions that outside of the array size in each document.

Assume a weighted set string attribute X with:

```
"X": {
    "x": 10,
    "y": 20
}
```

for a particular document. The result of using the feature dotProduct(X,Y) with the query vector rankproperty.dotProduct.Y={x:2,y:4} will then be 100 (10\*2+20\*4) for this document.

Arrays can be passed down as `[w1 w2 w3 …]` or on sparse form `{d1:c1,d2:c2,…}` as is already supported for weighted sets.

 **Note:** When the query vector ends up being the same as the query, it is better to annotate the query terms with weights (see [term weight](../querying/simple-query-language.html#term-weight)) and use the nativeDotProduct feature instead. This will run more efficiently and improve the correlation between results produced by the WAND operator and the final relevance score.

 **Note:** When using the dotProduct feature, [fast-search](../../content/attributes.html#fast-search) is not needed, unless also used for searching. When using the dotProduct query operator, use fast-search.
 |
| tokenInputIds(_length_, _input\_1_, _input\_2_, _..._) | n/a | 

Convenience function for generating token sequence input to Transformer models. Creates a tensor with dimensions `d0[1], d1[length]`, where `d0` is the batch dimension and `d1` is the maximum length of the token sequence. Assumes the inputs are zero-padded tensors representing token sequences. The result is the token sequence:

`CLS + input_1 + SEP + input_2 + SEP + ... + 0's`

- _length_: The maximum length of the token sequence
- _input\_N_: Where to retrieve input from. At least one is required.

The inputs are typically retrieved from the query, document attributes or constants. For instance, `tokenInputIds(128, query(my_input), attribute(my_field))` where input types are:

- `query(my_input): tensor(d0[32])`
- `attribute(my_field): tensor(d0[128])`

will create a tensor of type `d0[1],d1[128]` consisting of the CLS token `101`, the tokens from the query, the SEP token `102`, the tokens from the document field, the SEP token `102`, and 0's for the rest of the tensor.

 |
| customTokenInputIds(_start\_sequence\_id_, _sep\_sequence\_id__length_, _input\_1_, _input\_2_, _..._) | n/a | 

Convenience function for generating token sequence input to Transformer models. Creates a tensor with dimensions `d0[1], d1[length]`, where `d0` is the batch dimension and `d1` is the maximum length of the token sequence. Assumes the inputs are zero-padded tensors representing token sequences. The result is the token sequence:

`start_sequence_id + input_1 + sep_sequence_id + input_2 + sep_sequence_id + ... + 0's`

- _start\_sequence\_id_The start sequence id, typically _1_
- _sep\_sequence\_id_The separator sequence id, typically _2_
- _length_: The maximum length of the token sequence
- _input\_N_: Where to retrieve input from. At least one is required.

The inputs are typically retrieved from the query, document attributes or constants. For instance, `customTokenInputIds(1,2,128, query(my_input), attribute(my_field))` where input types are:

- `query(my_input): tensor(d0[32])`
- `attribute(my_field): tensor(d0[128])`

 |
| tokenTypeIds(_length_, _input\_1_, _input\_2_, _..._) | n/a | 

Convenience function for generating token sequence input to Transformer models. Similar to the `tokenInputIds`, creates a tensor of type `d0[1],d1[length]` which represents a mask with zeros for the first input including CLS and SEP token, ones for the rest of the inputs (up to and including the final SEP token), and 0's for the rest of the tensor.

 |
| tokenAttentionMask(_length_, _input\_1_, _input\_2_, _..._) | n/a | 

Convenience function for generating token sequence input to Transformer models. Similar to the `tokenInputIds`, creates a tensor of type `d0[1],d1[length]` which represents a mask with ones for all tokens that are set (CLS and SEP and all inputs), and zeros for the rest.

 |

## Graphs for selected ranking functions

### closeness
 ![Closeness logscale plot](/assets/img/relevance/closeness-logscale.png)

The plot above shows the possible outputs from the closeness distance rank feature using the default maxDistance of 1000 km. The _linear(x)_ graph shows the default closeness output while the other graphs are logscale output for various values of the scaleDistance parameter: 9013.305 (1 km), 45066.525 (5 km - the default value), and 901330.5 (100 km). These values correspond to the following values of the halfResponse parameter: 276154.903 (30.64 km), 593861.739 (65.89 km), and 2088044.581 (231.66 km).

### freshness
 ![Freshness logscale plot](/assets/img/relevance/freshness-logscale.png)

The plot above shows the possible outputs from the freshness rank feature using the default maxAge of 7776000s (90 days). The _linear(x)_ graph shows the default freshness output while the other graphs are logscale output for various values of the halfResponse parameter: 172800s (2 days), 604800s (7 days - the default value), 1209600s (14 days).

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [Feature list](#feature-list)
- [Query features](#query-features)
- [Document features](#document-features)
- [Field match features - normalized](#field-match-features-normalized)
- [Field match features - normalized and relative to the whole query](#field-match-features-normalized-and-relative-to-the-whole-query)
- [Field match features - not normalized](#field-match-features-not-normalized)
- [Query and field similarity](#query-and-field-similarity)
- [Query term and field match features](#query-term-and-field-match-features)
- [Features for indexed multivalue string fields](#features-for-indexed-multivalue-string-fields)
- [Attribute match features - normalized](#attribute-match-features-normalized)
- [Attribute match features - normalized and relative to the whole query](#attribute-match-features-normalized-and-relative-to-the-whole-query)
- [Attribute match features - not normalized](#attribute-match-features-not-normalized)
- [Features combining multiple fields and attributes](#features-combining-multiple-fields-and-attributes)
- [Rank scores](#rank-scores)
- [Global features](#global-features)
- [Match operator scores](#match-operator-scores)
- [Geo search](#geo-search)
- [Utility features](#utility-features)
- [Graphs for selected ranking functions](#graphs)
- [closeness](#closeness)
- [freshness](#freshness)

