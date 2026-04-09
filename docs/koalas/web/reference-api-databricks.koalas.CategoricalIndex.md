# databricks.koalas.CategoricalIndex

*class *`databricks.koalas.``CategoricalIndex`

Index based on an underlying Categorical.

CategoricalIndex can only take on a limited,
and usually fixed, number of possible values (categories). Also,
it might have an order, but numerical operations
(additions, divisions, …) are not possible.

Parameters

**data**array-like (1-dimensional)

The values of the categorical. If categories are given, values not in
categories will be replaced with NaN.

**categories**index-like, optional

The categories for the categorical. Items need to be unique.
If the categories are not given here (and also not in dtype), they
will be inferred from the data.

**ordered**bool, optional

Whether or not this categorical is treated as an ordered
categorical. If not given here or in dtype, the resulting
categorical will be unordered.

**dtype**CategoricalDtype or “category”, optional

If `CategoricalDtype`, cannot be used together with
categories or ordered.

**copy**bool, default False

Make a copy of input ndarray.

**name**object, optional

Name to be stored in the index.

See also

`Index`

The base Koalas Index type.