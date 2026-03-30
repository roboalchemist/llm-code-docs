# Source: https://nmslib.github.io/nmslib/api.html

Title: API Reference — nmslib 2.0.5 documentation

URL Source: https://nmslib.github.io/nmslib/api.html

Markdown Content:
[nmslib](https://nmslib.github.io/nmslib/index.html)

Information on the search methods (and their parameters) and spaces, can be found [on this page](https://github.com/nmslib/nmslib/tree/master/manual/README.md).

nmslib.init[¶](https://nmslib.github.io/nmslib/api.html#nmslib-init "Permalink to this headline")
-------------------------------------------------------------------------------------------------

This function acts act the main entry point into NMS lib. This function should be called first before calling any other method.

`nmslib.``init`(_space: str='cosinesimil'_, _space\_params: object=None_, _method: str='hnsw'_, _data\_type: nmslib.DataType=DataType.DENSE\_VECTOR_, _dtype: nmslib.DistType=DistType.FLOAT_) → object[¶](https://nmslib.github.io/nmslib/api.html#nmslib.init "Permalink to this definition")
This function initializes a new NMSLIB index

| Parameters: | * **space** (_str optional_) – The metric space to create for this index * **space_params** (_dict optional_) – Parameters for configuring the space * **method** (_str optional_) – The index method to use * **data_type** (_nmslib.DataType optional_) – The type of data to index (dense/sparse/string vectors) |
| --- |
| Returns: |  |
| Return type: | A new NMSLIB Index. |
_class_`nmslib.``DistType`[¶](https://nmslib.github.io/nmslib/api.html#nmslib.DistType "Permalink to this definition")`FLOAT`[¶](https://nmslib.github.io/nmslib/api.html#nmslib.DistType.FLOAT "Permalink to this definition")`INT`[¶](https://nmslib.github.io/nmslib/api.html#nmslib.DistType.INT "Permalink to this definition")_class_`nmslib.``DataType`[¶](https://nmslib.github.io/nmslib/api.html#nmslib.DataType "Permalink to this definition")`DENSE_VECTOR`[¶](https://nmslib.github.io/nmslib/api.html#nmslib.DataType.DENSE_VECTOR "Permalink to this definition")`OBJECT_AS_STRING`[¶](https://nmslib.github.io/nmslib/api.html#nmslib.DataType.OBJECT_AS_STRING "Permalink to this definition")`SPARSE_VECTOR`[¶](https://nmslib.github.io/nmslib/api.html#nmslib.DataType.SPARSE_VECTOR "Permalink to this definition")

nmslib.FloatIndex[¶](https://nmslib.github.io/nmslib/api.html#nmslib-floatindex "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------

nmslib.dist.FloatIndex

_class_`nmslib.dist.``FloatIndex`[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex "Permalink to this definition")`addDataPoint`(_self: nmslib.dist.FloatIndex_, _id: int_, _data: object_) → int[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex.addDataPoint "Permalink to this definition")
Adds a single datapoint to the index

| Parameters: | * **id** (_int_) – The id of the object to add * **data** (_object_) – The object to add to the index. |
| --- |
| Returns: | The position the item was added at |
| Return type: | int |
`addDataPointBatch`(_self: nmslib.dist.FloatIndex_, _data: object_, _ids: object=None_) → int[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex.addDataPointBatch "Permalink to this definition")
Adds multiple datapoints to the index

| Parameters: | * **data** (_object_) – The objects to add to the index. * **ids** (_array\_like optional_) – The ids of the object being inserted. If not set will default to the row id of each object in the dataset |
| --- |
| Returns: | The number of items added |
| Return type: | int |
`createIndex`(_self: nmslib.dist.FloatIndex_, _index\_params: object=None_, _print\_progress: bool=False_) → None[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex.createIndex "Permalink to this definition")
Creates the index, and makes it available for querying

| Parameters: | * **index_params** (_dict optional_) – Dictionary of optional parameters to use in indexing * **print_progress** (_bool optional_) – Whether or not to display progress bar when creating index |
| --- |
`getDistance`(_self: nmslib.dist.FloatIndex_, _arg0: int_, _arg1: int_) → float[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex.getDistance "Permalink to this definition")`knnQuery`(_self: nmslib.dist.FloatIndex_, _vector: object_, _k: int=10_) → object[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex.knnQuery "Permalink to this definition")
Finds the approximate K nearest neighbours of a vector in the index

| Parameters: | * **vector** (_array\_like_) – A 1D vector to query for. * **k** (_int optional_) – The number of neighbours to return |
| --- |
| Returns: | * **ids** (_array\_like._) – A 1D vector of the ids of each nearest neighbour. * **distances** (_array\_like._) – A 1D vector of the distance to each nearest neigbhour. |
`knnQueryBatch`(_self: nmslib.dist.FloatIndex_, _queries: object_, _k: int=10_, _num\_threads: int=0_) → object[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex.knnQueryBatch "Permalink to this definition")
Performs multiple queries on the index, distributing the work over a thread pool

| Parameters: | * **input** (_list_) – A list of queries to query for * **k** (_int optional_) – The number of neighbours to return * **num_threads** (_int optional_) – The number of threads to use |
| --- |
| Returns: | A list of tuples of (ids, distances) |
| Return type: | list |
`loadIndex`(_self: nmslib.dist.FloatIndex_, _filename: str_, _load\_data: bool=False_) → None[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex.loadIndex "Permalink to this definition")
Loads the index from disk

| Parameters: | * **filename** (_str_) – The filename to read from * **load_data** (_bool optional_) – Whether or not to load previously saved data. |
| --- |
`saveIndex`(_self: nmslib.dist.FloatIndex_, _filename: str_, _save\_data: bool=False_) → None[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex.saveIndex "Permalink to this definition")
Saves the index and/or data to disk

| Parameters: | * **filename** (_str_) – The filename to save to * **save_data** (_bool optional_) – Whether or not to save data |
| --- |
`setQueryTimeParams`(_self: nmslib.dist.FloatIndex_, _params: object=None_) → None[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.FloatIndex.setQueryTimeParams "Permalink to this definition")
Sets parameters used in knnQuery.

| Parameters: | **params** (_dict_) – A dictionary of params to use in querying. Setting params to None will reset |
| --- |

nmslib.IntIndex[¶](https://nmslib.github.io/nmslib/api.html#nmslib-intindex "Permalink to this headline")
---------------------------------------------------------------------------------------------------------

nmslib.dist.IntIndex

_class_`nmslib.dist.``IntIndex`[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex "Permalink to this definition")`addDataPoint`(_self: nmslib.dist.IntIndex_, _id: int_, _data: object_) → int[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex.addDataPoint "Permalink to this definition")
Adds a single datapoint to the index

| Parameters: | * **id** (_int_) – The id of the object to add * **data** (_object_) – The object to add to the index. |
| --- |
| Returns: | The position the item was added at |
| Return type: | int |
`addDataPointBatch`(_self: nmslib.dist.IntIndex_, _data: object_, _ids: object=None_) → int[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex.addDataPointBatch "Permalink to this definition")
Adds multiple datapoints to the index

| Parameters: | * **data** (_object_) – The objects to add to the index. * **ids** (_array\_like optional_) – The ids of the object being inserted. If not set will default to the row id of each object in the dataset |
| --- |
| Returns: | The number of items added |
| Return type: | int |
`createIndex`(_self: nmslib.dist.IntIndex_, _index\_params: object=None_, _print\_progress: bool=False_) → None[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex.createIndex "Permalink to this definition")
Creates the index, and makes it available for querying

| Parameters: | * **index_params** (_dict optional_) – Dictionary of optional parameters to use in indexing * **print_progress** (_bool optional_) – Whether or not to display progress bar when creating index |
| --- |
`getDistance`(_self: nmslib.dist.IntIndex_, _arg0: int_, _arg1: int_) → int[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex.getDistance "Permalink to this definition")`knnQuery`(_self: nmslib.dist.IntIndex_, _vector: object_, _k: int=10_) → object[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex.knnQuery "Permalink to this definition")
Finds the approximate K nearest neighbours of a vector in the index

| Parameters: | * **vector** (_array\_like_) – A 1D vector to query for. * **k** (_int optional_) – The number of neighbours to return |
| --- |
| Returns: | * **ids** (_array\_like._) – A 1D vector of the ids of each nearest neighbour. * **distances** (_array\_like._) – A 1D vector of the distance to each nearest neigbhour. |
`knnQueryBatch`(_self: nmslib.dist.IntIndex_, _queries: object_, _k: int=10_, _num\_threads: int=0_) → object[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex.knnQueryBatch "Permalink to this definition")
Performs multiple queries on the index, distributing the work over a thread pool

| Parameters: | * **input** (_list_) – A list of queries to query for * **k** (_int optional_) – The number of neighbours to return * **num_threads** (_int optional_) – The number of threads to use |
| --- |
| Returns: | A list of tuples of (ids, distances) |
| Return type: | list |
`loadIndex`(_self: nmslib.dist.IntIndex_, _filename: str_, _load\_data: bool=False_) → None[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex.loadIndex "Permalink to this definition")
Loads the index from disk

| Parameters: | * **filename** (_str_) – The filename to read from * **load_data** (_bool optional_) – Whether or not to load previously saved data. |
| --- |
`saveIndex`(_self: nmslib.dist.IntIndex_, _filename: str_, _save\_data: bool=False_) → None[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex.saveIndex "Permalink to this definition")
Saves the index and/or data to disk

| Parameters: | * **filename** (_str_) – The filename to save to * **save_data** (_bool optional_) – Whether or not to save data |
| --- |
`setQueryTimeParams`(_self: nmslib.dist.IntIndex_, _params: object=None_) → None[¶](https://nmslib.github.io/nmslib/api.html#nmslib.dist.IntIndex.setQueryTimeParams "Permalink to this definition")
Sets parameters used in knnQuery.

| Parameters: | **params** (_dict_) – A dictionary of params to use in querying. Setting params to None will reset |
| --- |
