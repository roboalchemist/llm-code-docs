# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md

Title: Miscellaneous — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html

Published Time: Fri, 18 Jul 2025 19:26:27 GMT

Markdown Content:
Miscellaneous[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#miscellaneous "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo_curator.Sequential(_modules:list[BaseModule]_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.Sequential "Link to this definition")@nemo_curator.utils.decorators.batched[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.utils.decorators.batched "Link to this definition")
Marks a function as accepting a pandas series of elements instead of a single element

Parameters:
**function** – The function that accepts a batch of elements

_class_ nemo_curator.AddId(_id\_field:str_,_id\_prefix:str='doc\_id'_,_start\_index:int|None=None_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.AddId "Link to this definition")call(_dataset:[DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo\_curator.datasets.DocumentDataset "nemo\_curator.datasets.doc\_dataset.DocumentDataset")_,)→[DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo_curator.datasets.DocumentDataset "nemo_curator.datasets.doc_dataset.DocumentDataset")[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.AddId.call "Link to this definition")
Performs an arbitrary operation on a dataset

Parameters:
**dataset** ([_DocumentDataset_](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo_curator.datasets.DocumentDataset "nemo_curator.datasets.DocumentDataset")) – The dataset to operate on

_class_ nemo_curator.blend_datasets(_target\_size:int_,_datasets:list[[DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo\_curator.datasets.DocumentDataset "nemo\_curator.datasets.doc\_dataset.DocumentDataset")]_,_sampling\_weights:list[float]_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.blend_datasets "Link to this definition")
Combines multiple datasets into one with different amounts of each dataset. :param target_size: The number of documents the resulting dataset should have.

> The actual size of the dataset may be slightly larger if the normalized weights do not allow for even mixtures of the datasets.

Parameters:
*   **datasets** – A list of all datasets to combine together

*   **sampling_weights** – A list of weights to assign to each dataset in the input. Weights will be normalized across the whole list as a part of the sampling process. For example, if the normalized sampling weight for dataset 1 is 0.02, 2% ofthe total samples will be sampled from dataset 1. There are guaranteed to be math.ceil(normalized_weight_i * target_size) elements from dataset i in the final blend.

_class_ nemo_curator.Shuffle(_seed:int|None=None,npartitions:int|None=None,partition\_to\_filename:~collections.abc.Callable[[int],str]=<function default\_filename>,filename\_col:str='file\_name'_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.Shuffle "Link to this definition")call(_dataset:[DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo\_curator.datasets.DocumentDataset "nemo\_curator.datasets.doc\_dataset.DocumentDataset")_,)→[DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo_curator.datasets.DocumentDataset "nemo_curator.datasets.doc_dataset.DocumentDataset")[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.Shuffle.call "Link to this definition")
Performs an arbitrary operation on a dataset

Parameters:
**dataset** ([_DocumentDataset_](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo_curator.datasets.DocumentDataset "nemo_curator.datasets.DocumentDataset")) – The dataset to operate on

_class_ nemo_curator.DocumentSplitter(_separator:str_,_text\_field:str='text'_,_segment\_id\_field:str='segment\_id'_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.DocumentSplitter "Link to this definition")
Splits documents into segments based on a separator. Each segment is a new document with an additional column indicating the segment id.

To restore the original document, ensure that each document has a unique id prior to splitting.

call(_dataset:[DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo\_curator.datasets.DocumentDataset "nemo\_curator.datasets.doc\_dataset.DocumentDataset")_,)→[DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo_curator.datasets.DocumentDataset "nemo_curator.datasets.doc_dataset.DocumentDataset")[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.DocumentSplitter.call "Link to this definition")
Splits the documents into segments based on the separator and adds a column indicating the segment id.

_class_ nemo_curator.DocumentJoiner(_separator:str_,_text\_field:str='text'_,_segment\_id\_field:str='segment\_id'_,_document\_id\_field:str='id'_,_drop\_segment\_id\_field:bool=True_,_max\_length:int|None=None_,_length\_field:str|None=None_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.DocumentJoiner "Link to this definition")
Joins documents that have a common id back into a single document. The order of the documents is dictated by an additional segment_id column. A maximum length can be specified to limit the size of the joined documents.

The joined documents are joined by a separator.

call(_dataset:[DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo\_curator.datasets.DocumentDataset "nemo\_curator.datasets.doc\_dataset.DocumentDataset")_,)→[DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo_curator.datasets.DocumentDataset "nemo_curator.datasets.doc_dataset.DocumentDataset")[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.DocumentJoiner.call "Link to this definition")
Joins the documents back into a single document while preserving all the original fields.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/misc.html.md#nemo_curator.DocumentJoiner.call)
- [DocumentDataset](https://docs.nvidia.com/nemo-framework/user-guide/latest/datacuration/api/datasets.html.md#nemo_curator.datasets.DocumentDataset)
