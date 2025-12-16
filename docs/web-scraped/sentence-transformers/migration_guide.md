# Source: https://www.sbert.net/docs/migration_guide.html

# Migration Guide[ïƒ?](#migration-guide "Link to this heading")

## Migrating from v4.x to v5.x[ïƒ?](#migrating-from-v4-x-to-v5-x "Link to this heading")

The v5 Sentence Transformers release introduced [[`SparseEncoder`]](package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder") embedding models (see the [Sparse Encoder Usage](sparse_encoder/usage/usage.html) for more details on them) alongside an extensive training suite for them, including [[`SparseEncoderTrainer`]](package_reference/sparse_encoder/trainer.html#sentence_transformers.sparse_encoder.SparseEncoderTrainer "sentence_transformers.sparse_encoder.trainer.SparseEncoderTrainer") and [[`SparseEncoderTrainingArguments`]](package_reference/sparse_encoder/training_args.html#sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments "sentence_transformers.sparse_encoder.training_args.SparseEncoderTrainingArguments"). Unlike with v3 (updated [[`SentenceTransformer`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer")) and v4 (updated [[`CrossEncoder`]](package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder")), this update does not deprecate any training methods.

### Migration for model.encode[ïƒ?](#migration-for-model-encode "Link to this heading")

We introduce two new methods, [[`encode_query()`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query") and [[`encode_document()`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document"), which are recommended to use instead of the [[`encode()`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") method when working with information retrieval tasks. These methods are specialized version of [[`encode()`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") that differs in exactly two ways:

1.  If no [`prompt_name`] or [`prompt`] is provided, it uses a predefined â€œqueryâ€? prompt, if available in the modelâ€™s [`prompts`] dictionary.

2.  It sets the [`task`] to â€œqueryâ€?. If the model has a [[`Router`]](package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, it will use the â€œqueryâ€? task type to route the input through the appropriate submodules.

The same methods apply to the [[`SparseEncoder`]](package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder") models.

+-----------------------------------------------------------------------+---------------------------------------------------------------------------+
| v4.x                                                                  | v5.x (recommended)                                                        |
+=======================================================================+===========================================================================+
| ::::                                  | ::::                                      |
| ::: highlight                                                         | ::: highlight                                                             |
|     from sentence_transformers import SentenceTransformer             |     from sentence_transformers import SentenceTransformer                 |
|                                                                       |                                                                           |
|     model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1") |     model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")     |
|     query = "What is the capital of France?"                          |     query = "What is the capital of France?"                              |
|     document = "Paris is the capital of France."                      |     document = "Paris is the capital of France."                          |
|                                                                       |                                                                           |
|     # Use the prompt with the name "query" for the query              |     # The new encode_query and encode_document methods call encode,       |
|     query_embedding = model.encode(query, prompt_name="query")        |     # but with the prompt name set to "query" or "document" if the        |
|     document_embedding = model.encode(document)                       |     # model has prompts saved, and the task set to "query" or "document", |
|                                                                       |     # if the model has a Router module.                                   |
|     print(query_embedding.shape, document_embedding.shape)            |     query_embedding = model.encode_query(query)                           |
|     # => (1, 768) (1, 768)                                            |     document_embedding = model.encode_document(document)                  |
| :::                                                                   |                                                                           |
| ::::                                                                  |     print(query_embedding.shape, document_embedding.shape)                |
|                                                                       |     # => (1, 768) (1, 768)                                                |
|                                                                       | :::                                                                       |
|                                                                       | ::::                                                                      |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------+

: [encode_query and encode_document][ïƒ?](#id1 "Link to this table") 

We also deprecated the [[`encode_multi_process()`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_multi_process "sentence_transformers.SentenceTransformer.encode_multi_process") method, which was used to encode large datasets in parallel using multiple processes. This method has now been subsumed by the [[`encode()`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode "sentence_transformers.SentenceTransformer.encode") method with the [`device`], [`pool`], and [`chunk_size`] arguments. Provide a list of devices to the [`device`] argument to use multiple processes, or a single device to use a single process. The [`pool`] argument can be used to pass a multiprocessing pool that gets reused across calls, and the [`chunk_size`] argument can be used to control the size of the chunks that are sent to each process in parallel.

+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| v4.x                                                                         | v5.x (recommended)                                                                            |
+==============================================================================+===============================================================================================+
| ::::                                         | ::::                                                          |
| ::: highlight                                                                | ::: highlight                                                                                 |
|     from sentence_transformers import SentenceTransformer                    |     from sentence_transformers import SentenceTransformer                                     |
|                                                                              |                                                                                               |
|     def main():                                                              |     def main():                                                                               |
|         model = SentenceTransformer("all-mpnet-base-v2")                     |         model = SentenceTransformer("all-mpnet-base-v2")                                      |
|         texts = ["The weather is so nice!", "It's so sunny outside.", ...]   |         texts = ["The weather is so nice!", "It's so sunny outside.", ...]                    |
|                                                                              |                                                                                               |
|         pool = model.start_multi_process_pool(["cpu", "cpu", "cpu", "cpu"])  |         embeddings = model.encode(texts, device=["cpu", "cpu", "cpu", "cpu"], chunk_size=512) |
|         embeddings = model.encode_multi_process(texts, pool, chunk_size=512) |                                                                                               |
|         model.stop_multi_process_pool(pool)                                  |         print(embeddings.shape)                                                               |
|                                                                              |         # => (4000, 768)                                                                      |
|         print(embeddings.shape)                                              |                                                                                               |
|         # => (4000, 768)                                                     |     if __name__ == "__main__":                                                                |
|                                                                              |         main()                                                                                |
|     if __name__ == "__main__":                                               | :::                                                                                           |
|         main()                                                               | ::::                                                                                          |
| :::                                                                          |                                                                                               |
| ::::                                                                         |                                                                                               |
+------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

: [encode_multi_process deprecation -\> encode][ïƒ?](#id2 "Link to this table") 

The [`truncate_dim`] parameter allows you to reduce the dimensionality of embeddings by truncating them. This is useful for optimizing storage and retrieval while maintaining most of the semantic information. Research has shown that the first dimensions often contain most of the important information in transformer embeddings.

+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| v4.x                                                                          | v5.x (recommended)                                                                    |
+===============================================================================+=======================================================================================+
| ::::                                          | ::::                                                  |
| ::: highlight                                                                 | ::: highlight                                                                         |
|     from sentence_transformers import SentenceTransformer                     |     from sentence_transformers import SentenceTransformer                             |
|                                                                               |                                                                                       |
|     # To truncate embeddings to a specific dimension,                         |     # Now you can either specify the dimension when loading the model...              |
|     # you had to specify the dimension when loading                           |     model = SentenceTransformer(                                                      |
|     model = SentenceTransformer(                                              |        "mixedbread-ai/mxbai-embed-large-v1",                                          |
|        "mixedbread-ai/mxbai-embed-large-v1",                                  |        truncate_dim=384,                                                              |
|        truncate_dim=384,                                                      |     )                                                                                 |
|     )                                                                         |     sentences = ["This is an example sentence", "Each sentence is converted"]         |
|     sentences = ["This is an example sentence", "Each sentence is converted"] |                                                                                       |
|                                                                               |     # ... or you can specify it when encoding                                         |
|     embeddings = model.encode(sentences)                                      |     embeddings = model.encode(sentences, truncate_dim=256)                            |
|     print(embeddings.shape)                                                   |     print(embeddings.shape)                                                           |
|     # => (2, 384)                                                             |     # => (2, 256)                                                                     |
| :::                                                                           |                                                                                       |
| ::::                                                                          |     # The encode parameter has priority, but otherwise the model truncate_dim is used |
|                                                                               |     embeddings = model.encode(sentences)                                              |
|                                                                               |     print(embeddings.shape)                                                           |
|                                                                               |     # => (2, 384)                                                                     |
|                                                                               | :::                                                                                   |
|                                                                               | ::::                                                                                  |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

: [Add truncate_dim to encode][ïƒ?](#id3 "Link to this table") 

### Migration for Asym to Router[ïƒ?](#migration-for-asym-to-router "Link to this heading")

The [`Asym`] module has been renamed and updated to the new [[`Router`]](package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module, which provides the same functionality but with a more consistent API and additional features. The new [[`Router`]](package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module allows for more flexible routing of different tasks, such as query and document embeddings, and is recommended when working with asymmetric models that require different processing for different tasks, notably queries and documents.

The [[`encode_query()`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_query "sentence_transformers.SentenceTransformer.encode_query") and [[`encode_document()`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode_document "sentence_transformers.SentenceTransformer.encode_document") methods automatically set the [`task`] parameter that is used by the [[`Router`]](package_reference/sentence_transformer/models.html#sentence_transformers.models.Router "sentence_transformers.models.Router") module to route the input to the query or document submodules, respectively.

Asym -\> Router

+----------------------------------------------------------------------+-------------------------------------------------------------------+
| v4.x                                                                 | v5.x (recommended)                                                |
+======================================================================+===================================================================+
| ::::                                 | ::::                              |
| ::: highlight                                                        | ::: highlight                                                     |
|     from sentence_transformers import SentenceTransformer, models    |     from sentence_transformers import SentenceTransformer, models |
|                                                                      |                                                                   |
|     # Load a Sentence Transformer model and add an asymmetric router |     # Load a Sentence Transformer model and add a router          |
|     # for different query and document post-processing               |     # for different query and document post-processing            |
|     model = SentenceTransformer("microsoft/mpnet-base")              |     model = SentenceTransformer("microsoft/mpnet-base")           |
|     dim = model.get_sentence_embedding_dimension()                   |     dim = model.get_sentence_embedding_dimension()                |
|     asym_model = models.Asym()                                                               |     })                                                            |
|     model.add_module("asym", asym_model)                             |     model.add_module("router", router_model)                      |
| :::                                                                  | :::                                                               |
| ::::                                                                 | ::::                                                              |
+----------------------------------------------------------------------+-------------------------------------------------------------------+

Asym -\> Router for queries and documents

+----------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| v4.x                                                                                   | v5.x (recommended)                                                                 |
+========================================================================================+====================================================================================+
| ::::                                                   | ::::                                               |
| ::: highlight                                                                          | ::: highlight                                                                      |
|     from sentence_transformers import SentenceTransformer                              |     from sentence_transformers import SentenceTransformer                          |
|     from sentence_transformers.models import Router, Normalize                         |     from sentence_transformers.models import Router, Normalize                     |
|                                                                                        |                                                                                    |
|     # Use a regular SentenceTransformer for the document embeddings,                   |     # Use a regular SentenceTransformer for the document embeddings,               |
|     # and a static embedding model for the query embeddings                            |     # and a static embedding model for the query embeddings                        |
|     document_embedder = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")      |     document_embedder = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")  |
|     query_embedder = SentenceTransformer("static-retrieval-mrl-en-v1")                 |     query_embedder = SentenceTransformer("static-retrieval-mrl-en-v1")             |
|     asym = Asym()                                                                                 |     )                                                                              |
|     normalize = Normalize()                                                            |     normalize = Normalize()                                                        |
|                                                                                        |                                                                                    |
|     # Create an asymmetric model with different encoders for queries and documents     |     # Create an asymmetric model with different encoders for queries and documents |
|     model = SentenceTransformer(                                                       |     model = SentenceTransformer(                                                   |
|         modules=[asym, normalize],                                                     |         modules=[router, normalize],                                               |
|     )                                                                                  |     )                                                                              |
|                                                                                        |                                                                                    |
|     # ... requires more training to align the vector spaces                            |     # ... requires more training to align the vector spaces                        |
|                                                                                        |                                                                                    |
|     # Use the query & document routes                                                  |     # Use the query & document routes                                              |
|     query_embedding = model.encode()        |     query_embedding = model.encode_query("What is the capital of France?")         |
|     document_embedding = model.encode() |     document_embedding = model.encode_document("Paris is the capital of France.")  |
| :::                                                                                    | :::                                                                                |
| ::::                                                                                   | ::::                                                                               |
+----------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

Asym inference -\> Router inference

+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| v4.x                                                                              | v5.x (recommended)                                                                          |
+===================================================================================+=============================================================================================+
| ::::                                              | ::::                                                        |
| ::: highlight                                                                     | ::: highlight                                                                               |
|     ...                                                                           |     ...                                                                                     |
|                                                                                   |                                                                                             |
|     # Use the query & document routes as keys in dictionaries                     |     # Use the query & document routes with encode_query/encode_document                     |
|     query_embedding = model.encode([]) |     query_embedding = model.encode_query(["What is the capital of France?"])                |
|     document_embedding = model.encode([                                           |     document_embedding = model.encode_document([                                            |
|         ,                          |         "Paris is the capital of France.",                                                  |
|         ,                        |         "Berlin is the capital of Germany.",                                                |
|     ])                                                                            |     ])                                                                                      |
|     class_embedding = model.encode(                                               |                                                                                             |
|         [],                       |     # When using routes other than "query" and "document", you can use the `task` parameter |
|     )                                                                             |     # on model.encode                                                                       |
| :::                                                                               |     class_embedding = model.encode(                                                         |
| ::::                                                                              |         ["S&P500 is down 2.1% today."],                                                     |
|                                                                                   |         task="classification"  # or any other task defined in the model Router              |
|                                                                                   |     )                                                                                       |
|                                                                                   | :::                                                                                         |
|                                                                                   | ::::                                                                                        |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

Asym training -\> Router training

+--------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| v4.x                                                                                 | v5.x (recommended)                                                                    |
+======================================================================================+=======================================================================================+
| ::::                                                 | ::::                                                  |
| ::: highlight                                                                        | ::: highlight                                                                         |
|     ...                                                                              |     ...                                                                               |
|                                                                                      |                                                                                       |
|     # Prepare a training dataset for an Asym model with "query" and "document" keys  |     # Prepare a training dataset for a Router model with "query" and "document" keys  |
|     train_dataset = Dataset.from_dict()                                                                               |     })                                                                                |
|                                                                                      |     train_dataset = train_dataset.map(mapper)                                         |
|     # This mapper turns normal texts into a dictionary mapping Asym keys to the text |     print(train_dataset[0])                                                           |
|     def mapper(sample):                                                              |     """                                                                               |
|         return ,                               |         "question": "is toprol xl the same as metoprolol?",                           |
|             "answer": ,                                |         "answer": "Metoprolol succinate is also known by the brand name Toprol XL."   |
|         }                                                                            |     }                                                                                 |
|                                                                                      |     """                                                                               |
|     train_dataset = train_dataset.map(mapper)                                        |                                                                                       |
|     print(train_dataset[0])                                                          |     args = SentenceTransformerTrainingArguments(  # Or SparseEncoderTrainingArguments |
|     """                                                                              |         # Map dataset columns to the Router keys                                      |
|     ,               |             "question": "query",                                                      |
|         "answer":       |             "answer": "document",                                                     |
|     }                                                                                |         }                                                                             |
|     """                                                                              |     )                                                                                 |
|                                                                                      |                                                                                       |
|     trainer = SentenceTransformerTrainer(  # Or SparseEncoderTrainer                 |     trainer = SentenceTransformerTrainer(  # Or SparseEncoderTrainer                  |
|         model=model,                                                                 |         model=model,                                                                  |
|         args=training_args,                                                          |         args=training_args,                                                           |
|         train_dataset=train_dataset,                                                 |         train_dataset=train_dataset,                                                  |
|         ...                                                                          |         ...                                                                           |
|     )                                                                                |     )                                                                                 |
| :::                                                                                  | :::                                                                                   |
| ::::                                                                                 | ::::                                                                                  |
+--------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

\

### Migration of advanced usage[ïƒ?](#migration-of-advanced-usage "Link to this heading")

Module and InputModule convenience superclasses

+-----------------------------------------------------------+-------------------------------------------------------------------------------+
| v4.x                                                      | v5.x (recommended)                                                            |
+===========================================================+===============================================================================+
| ::::                      | ::::                                          |
| ::: highlight                                             | ::: highlight                                                                 |
|     from sentence_transformers import SentenceTransformer |     from sentence_transformers import SentenceTransformer                     |
|     import torch                                          |     from sentence_transformers.models import Module, InputModule              |
|                                                           |                                                                               |
|     class MyModule(torch.nn.Module):                      |     # The new Module and InputModule superclasses provide convenience methods |
|         def __init__(self):                               |     # like 'load', 'load_file_path', 'load_dir_path', 'load_torch_weights',   |
|             super().__init__()                            |     # 'save_config', 'save_torch_weights', 'get_config_dict'                  |
|             # Custom code here                            |     # InputModule is meant to be used as the first module, is requires the    |
|                                                           |     # 'tokenize' method to be implemented                                     |
|     model = SentenceTransformer(modules=[MyModule()])     |     class MyModule(Module):                                                   |
| :::                                                       |         def __init__(self):                                                   |
| ::::                                                      |             super().__init__()                                                |
|                                                           |             # Custom initialization code here                                 |
|                                                           |                                                                               |
|                                                           |     model = SentenceTransformer(modules=[MyModule()])                         |
|                                                           | :::                                                                           |
|                                                           | ::::                                                                          |
+-----------------------------------------------------------+-------------------------------------------------------------------------------+

Custom batch samplers via class or function

+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| v4.x                                                                                  | v5.x (recommended)                                                                                 |
+=======================================================================================+====================================================================================================+
| ::::                                                  | ::::                                                               |
| ::: highlight                                                                         | ::: highlight                                                                                      |
|     from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer |     from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer              |
|                                                                                       |     from sentence_transformers.sampler import DefaultBatchSampler                                  |
|     class CustomSentenceTransformerTrainer(SentenceTransformerTrainer):               |     import torch                                                                                   |
|         # Custom batch samplers require subclassing the Trainer                       |                                                                                                    |
|         def get_batch_sampler(                                                        |     class CustomBatchSampler(DefaultBatchSampler):                                                 |
|             self,                                                                     |         def __init__(                                                                              |
|             dataset,                                                                  |             self,                                                                                  |
|             batch_size,                                                               |             dataset: Dataset,                                                                      |
|             drop_last,                                                                |             batch_size: int,                                                                       |
|             valid_label_columns=None,                                                 |             drop_last: bool,                                                                       |
|             generator=None,                                                           |             valid_label_columns: list[str] | None = None,                                          |
|             seed=0,                                                                   |             generator: torch.Generator | None = None,                                              |
|         ):                                                                            |             seed: int = 0,                                                                         |
|             # Custom batch sampler logic here                                         |         ):                                                                                         |
|             return ...                                                                |             super().__init__(dataset, batch_size, drop_last, valid_label_columns, generator, seed) |
|                                                                                       |             # Custom batch sampler logic here                                                      |
|     ...                                                                               |                                                                                                    |
|                                                                                       |     args = SentenceTransformerTrainingArguments(                                                   |
|     trainer = CustomSentenceTransformerTrainer(                                       |         # Other training arguments                                                                 |
|         model=model,                                                                  |         batch_sampler=CustomBatchSampler,  # Use the custom batch sampler class                    |
|         args=args,                                                                    |     )                                                                                              |
|         train_dataset=train_dataset,                                                  |     trainer = SentenceTransformerTrainer(                                                          |
|         ...                                                                           |         model=model,                                                                               |
|     )                                                                                 |         args=args,                                                                                 |
|     trainer.train()                                                                   |         train_dataset=train_dataset,                                                               |
| :::                                                                                   |         ...                                                                                        |
| ::::                                                                                  |     )                                                                                              |
|                                                                                       |     trainer.train()                                                                                |
|                                                                                       |                                                                                                    |
|                                                                                       |     # Or, use a function to initialize the batch sampler                                           |
|                                                                                       |     def custom_batch_sampler(                                                                      |
|                                                                                       |         dataset: Dataset,                                                                          |
|                                                                                       |         batch_size: int,                                                                           |
|                                                                                       |         drop_last: bool,                                                                           |
|                                                                                       |         valid_label_columns: list[str] | None = None,                                              |
|                                                                                       |         generator: torch.Generator | None = None,                                                  |
|                                                                                       |         seed: int = 0,                                                                             |
|                                                                                       |     ):                                                                                             |
|                                                                                       |         # Custom batch sampler logic here                                                          |
|                                                                                       |         return ...                                                                                 |
|                                                                                       |                                                                                                    |
|                                                                                       |     args = SentenceTransformerTrainingArguments(                                                   |
|                                                                                       |         # Other training arguments                                                                 |
|                                                                                       |         batch_sampler=custom_batch_sampler,  # Use the custom batch sampler function               |
|                                                                                       |     )                                                                                              |
|                                                                                       |     trainer = SentenceTransformerTrainer(                                                          |
|                                                                                       |         model=model,                                                                               |
|                                                                                       |         args=args,                                                                                 |
|                                                                                       |         train_dataset=train_dataset,                                                               |
|                                                                                       |         ...                                                                                        |
|                                                                                       |     )                                                                                              |
|                                                                                       |     trainer.train()                                                                                |
|                                                                                       | :::                                                                                                |
|                                                                                       | ::::                                                                                               |
+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

Custom multi-dataset batch samplers via class or function

+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| v4.x                                                                                  | v5.x (recommended)                                                                                   |
+=======================================================================================+======================================================================================================+
| ::::                                                  | ::::                                                                 |
| ::: highlight                                                                         | ::: highlight                                                                                        |
|     from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer |     from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer                |
|                                                                                       |     from sentence_transformers.sampler import MultiDatasetDefaultBatchSampler                        |
|     class CustomSentenceTransformerTrainer(SentenceTransformerTrainer):               |     import torch                                                                                     |
|         def get_multi_dataset_batch_sampler(                                          |                                                                                                      |
|             self,                                                                     |     class CustomMultiDatasetBatchSampler(MultiDatasetDefaultBatchSampler):                           |
|             dataset: ConcatDataset,                                                   |         def __init__(                                                                                |
|             batch_samplers: list[BatchSampler],                                       |             self,                                                                                    |
|             generator: torch.Generator | None = None,                                 |             dataset: ConcatDataset,                                                                  |
|             seed: int | None = 0,                                                     |             batch_samplers: list[BatchSampler],                                                      |
|         ):                                                                            |             generator: torch.Generator | None = None,                                                |
|             # Custom multi-dataset batch sampler logic here                           |             seed: int = 0,                                                                           |
|             return ...                                                                |         ):                                                                                           |
|                                                                                       |             super().__init__(dataset, batch_samplers=batch_samplers, generator=generator, seed=seed) |
|     ...                                                                               |             # Custom multi-dataset batch sampler logic here                                          |
|                                                                                       |                                                                                                      |
|     trainer = CustomSentenceTransformerTrainer(                                       |     args = SentenceTransformerTrainingArguments(                                                     |
|         model=model,                                                                  |         # Other training arguments                                                                   |
|         args=args,                                                                    |         multi_dataset_batch_sampler=CustomMultiDatasetBatchSampler,                                  |
|         train_dataset=train_dataset,                                                  |     )                                                                                                |
|         ...                                                                           |     trainer = SentenceTransformerTrainer(                                                            |
|     )                                                                                 |         model=model,                                                                                 |
|     trainer.train()                                                                   |         args=args,                                                                                   |
| :::                                                                                   |         train_dataset=train_dataset,                                                                 |
| ::::                                                                                  |         ...                                                                                          |
|                                                                                       |     )                                                                                                |
|                                                                                       |     trainer.train()                                                                                  |
|                                                                                       |                                                                                                      |
|                                                                                       |     # Or, use a function to initialize the batch sampler                                             |
|                                                                                       |     def custom_batch_sampler(                                                                        |
|                                                                                       |         dataset: ConcatDataset,                                                                      |
|                                                                                       |         batch_samplers: list[BatchSampler],                                                          |
|                                                                                       |         generator: torch.Generator | None = None,                                                    |
|                                                                                       |         seed: int = 0,                                                                               |
|                                                                                       |     ):                                                                                               |
|                                                                                       |         # Custom multi-dataset batch sampler logic here                                              |
|                                                                                       |         return ...                                                                                   |
|                                                                                       |                                                                                                      |
|                                                                                       |     args = SentenceTransformerTrainingArguments(                                                     |
|                                                                                       |         # Other training arguments                                                                   |
|                                                                                       |         multi_dataset_batch_sampler=custom_batch_sampler,  # Use the custom batch sampler function   |
|                                                                                       |     )                                                                                                |
|                                                                                       |     trainer = SentenceTransformerTrainer(                                                            |
|                                                                                       |         model=model,                                                                                 |
|                                                                                       |         args=args,                                                                                   |
|                                                                                       |         train_dataset=train_dataset,                                                                 |
|                                                                                       |         ...                                                                                          |
|                                                                                       |     )                                                                                                |
|                                                                                       |     trainer.train()                                                                                  |
|                                                                                       | :::                                                                                                  |
|                                                                                       | ::::                                                                                                 |
+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

Custom learning rate for sections

+-------------------------------------------------------------+---------------------------------------------------------------------------------------+
| v4.x                                                        | v5.x (recommended)                                                                    |
+=============================================================+=======================================================================================+
| ::::                        | ::::                                                  |
| ::: highlight                                               | ::: highlight                                                                         |
|     # A bunch of hacky code to set different learning rates |     from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer |
|     # for different sections of the model                   |                                                                                       |
| :::                                                         |     # Custom learning rate for each section of the model,                             |
| ::::                                                        |     # mapping regular expressions of parameter names to learning rates                |
|                                                             |     # Matching is done with 'search', not just 'match' or 'fullmatch'                 |
|                                                             |     learning_rate_mapping =                                                                                  |
|                                                             |                                                                                       |
|                                                             |     args = SentenceTransformerTrainingArguments(                                      |
|                                                             |         ...,                                                                          |
|                                                             |         learning_rate=1e-5,  # Default learning rate                                  |
|                                                             |         learning_rate_mapping=learning_rate_mapping,                                  |
|                                                             |     )                                                                                 |
|                                                             |                                                                                       |
|                                                             |     trainer = SentenceTransformerTrainer(                                             |
|                                                             |         model=model,                                                                  |
|                                                             |         args=args,                                                                    |
|                                                             |         train_dataset=train_dataset,                                                  |
|                                                             |         ...                                                                           |
|                                                             |     )                                                                                 |
|                                                             |     trainer.train()                                                                   |
|                                                             | :::                                                                                   |
|                                                             | ::::                                                                                  |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------+

Training with composite losses

+---------------------------------------------------------------------------+------------------------------------------------------------------------------+
| v4.x                                                                      | v5.x (recommended)                                                           |
+===========================================================================+==============================================================================+
| ::::                                      | ::::                                         |
| ::: highlight                                                             | ::: highlight                                                                |
|     class CustomLoss(torch.nn.Module):                                    |     class CustomLoss(torch.nn.Module):                                       |
|         def __init__(self, model, ...):                                   |         def __init__(self, model, ...):                                      |
|             super().__init__()                                            |             super().__init__()                                               |
|             # Custom loss initialization code here                        |             # Custom loss initialization code here                           |
|                                                                           |                                                                              |
|         def forward(self, features, labels):                              |         def forward(self, features, labels):                                 |
|             loss_component_one = self.compute_loss_one(features, labels)  |             loss_component_one = self.compute_loss_one(features, labels)     |
|             loss_component_two = self.compute_loss_two(features, labels)  |             loss_component_two = self.compute_loss_two(features, labels)     |
|                                                                           |                                                                              |
|             loss = loss_component_one * alpha + loss_component_two * beta |             # You can now return a dictionary of loss components.            |
|             return loss                                                   |             # The trainer considers the full loss as the sum of all          |
|                                                                           |             # components, but each component will also be logged separately. |
|      loss = CustomLoss(model, ...)                                        |             return                                                                 |
|                                                                           |                                                                              |
|                                                                           |     loss = CustomLoss(model, ...)                                            |
|                                                                           | :::                                                                          |
|                                                                           | ::::                                                                         |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------+

Accessing the underlying Transformer model

+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| v4.x                                                                          | v5.x (recommended)                                                                 |
+===============================================================================+====================================================================================+
| ::::                                          | ::::                                               |
| ::: highlight                                                                 | ::: highlight                                                                      |
|     from sentence_transformers import SentenceTransformer                     |     from sentence_transformers import SentenceTransformer                          |
|                                                                               |                                                                                    |
|     # Sometimes, for one reason or another, you need to access the underlying |     # Now, you can just use the `transformers_model` attribute on the model itself |
|     # Transformer directly. This was previously commonly done by accessing    |     # even if your model has non-standard modules.                                 |
|     # the first module, often 'Transformer', and then accessing the           |     model = SentenceTransformer("all-MiniLM-L6-v2")                                |
|     # `auto_model` attribute.                                                 |     print(model.transformers_model)                                                |
|     model = SentenceTransformer("all-MiniLM-L6-v2")                           |     # BertModel(                                                                   |
|     print(model[0].auto_model)                                                |     #   (embeddings): BertEmbeddings(                                              |
|     # BertModel(                                                              |     # ...                                                                          |
|     #   (embeddings): BertEmbeddings(                                         | :::                                                                                |
|     # ...                                                                     | ::::                                                                               |
| :::                                                                           |                                                                                    |
| ::::                                                                          |                                                                                    |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

\

## Migrating from v3.x to v4.x[ïƒ?](#migrating-from-v3-x-to-v4-x "Link to this heading")

The v4 Sentence Transformers release refactored the training of [[`CrossEncoder`]](package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") reranker/pair classification models, replacing [[`CrossEncoder.fit`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.fit "sentence_transformers.SentenceTransformer.fit") with a [[`CrossEncoderTrainer`]](package_reference/cross_encoder/trainer.html#sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer "sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer") and [`CrossEncoderTrainingArguments`]. Like with v3 and [[`SentenceTransformer`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") models, this update softly deprecated [[`CrossEncoder.fit`]](package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.fit "sentence_transformers.cross_encoder.CrossEncoder.fit"), meaning that it still works, but itâ€™s recommended to switch to the new v4.x training format. Behind the scenes, this method now uses the new trainer.

Warning

If you donâ€™t have code that uses [[`CrossEncoder.fit`]](package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.fit "sentence_transformers.cross_encoder.CrossEncoder.fit"), then you will not have to make any changes to your code to update from v3.x to v4.x.

If you do, your code still works, but it is recommended to switch to the new v4.x training format, as it allows more training arguments and functionality. See the [Training Overview](cross_encoder/training_overview.html) for more details.

+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| v3.x                                                                                 | v4.x (recommended)                                                                                    |
+======================================================================================+=======================================================================================================+
| ::::                                                | ::::                                                                 |
| ::: highlight                                                                        | ::: highlight                                                                                         |
|     from sentence_transformers import CrossEncoder, InputExample                     |     from datasets import load_dataset                                                                 |
|     from torch.utils.data import DataLoader                                          |     from sentence_transformers import CrossEncoder, CrossEncoderTrainer                               |
|                                                                                      |     from sentence_transformers.cross_encoder.losses import BinaryCrossEntropyLoss                     |
|     # 1. Define the model. Either from scratch of by loading a pre-trained model     |                                                                                                       |
|     model = CrossEncoder("microsoft/mpnet-base")                                     |     # 1. Define the model. Either from scratch of by loading a pre-trained model                      |
|                                                                                      |     model = CrossEncoder("microsoft/mpnet-base")                                                      |
|     # 2. Define your train examples. You need more than just two examples...         |                                                                                                       |
|     train_examples = [                                                               |     # 2. Load a dataset to finetune on, convert to required format                                    |
|         InputExample(texts=["What are pandas?", "The giant panda ..."], label=1),    |     dataset = load_dataset("sentence-transformers/hotpotqa", "triplet", split="train")                |
|         InputExample(texts=["What's a panda?", "Mount Vesuvius is a ..."], label=0), |                                                                                                       |
|     ]                                                                                |     def triplet_to_labeled_pair(batch):                                                               |
|     train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)       |         anchors = batch["anchor"]                                                                     |
|                                                                                      |         positives = batch["positive"]                                                                 |
|     # 3. Finetune the model                                                          |         negatives = batch["negative"]                                                                 |
|     model.fit(train_dataloader=train_dataloader, epochs=1, warmup_steps=100)         |         return                                                                                              |
|                                                                                      |                                                                                                       |
|                                                                                      |     dataset = dataset.map(triplet_to_labeled_pair, batched=True, remove_columns=dataset.column_names) |
|                                                                                      |     train_dataset = dataset.select(range(10_000))                                                     |
|                                                                                      |     eval_dataset = dataset.select(range(10_000, 11_000))                                              |
|                                                                                      |                                                                                                       |
|                                                                                      |     # 3. Define a loss function                                                                       |
|                                                                                      |     loss = BinaryCrossEntropyLoss(model)                                                              |
|                                                                                      |                                                                                                       |
|                                                                                      |     # 4. Create a trainer & train                                                                     |
|                                                                                      |     trainer = CrossEncoderTrainer(                                                                    |
|                                                                                      |         model=model,                                                                                  |
|                                                                                      |         train_dataset=train_dataset,                                                                  |
|                                                                                      |         eval_dataset=eval_dataset,                                                                    |
|                                                                                      |         loss=loss,                                                                                    |
|                                                                                      |     )                                                                                                 |
|                                                                                      |     trainer.train()                                                                                   |
|                                                                                      |                                                                                                       |
|                                                                                      |     # 5. Save the trained model                                                                       |
|                                                                                      |     model.save_pretrained("models/mpnet-base-hotpotqa")                                               |
|                                                                                      |     # model.push_to_hub("mpnet-base-hotpotqa")                                                        |
|                                                                                      | :::                                                                                                   |
|                                                                                      | ::::                                                                                                  |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

: [Old and new training flow][ïƒ?](#id4 "Link to this table") 

### Migration for parameters on [`CrossEncoder`] initialization and methods[ïƒ?](#migration-for-parameters-on-crossencoder-initialization-and-methods "Link to this heading")

+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v3.x                                                                                     | v4.x (recommended)                                                                                                                                                                            |
+==========================================================================================+===============================================================================================================================================================================================+
| [`CrossEncoder(model_name=...)`]                  | Renamed to [`CrossEncoder(model_name_or_path=...)`]                                                                                                    |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder(automodel_args=...)`]              | Renamed to [`CrossEncoder(model_kwargs=...)`]                                                                                                          |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder(tokenizer_args=...)`]              | Renamed to [`CrossEncoder(tokenizer_kwargs=...)`]                                                                                                      |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder(config_args=...)`]                 | Renamed to [`CrossEncoder(config_kwargs=...)`]                                                                                                         |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder(cache_dir=...)`]                   | Renamed to [`CrossEncoder(cache_folder=...)`]                                                                                                          |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder(default_activation_function=...)`] | Renamed to [`CrossEncoder(activation_fn=...)`]                                                                                                         |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder(classifier_dropout=...)`]          | Use [`CrossEncoder(config_kwargs=]` `[`...})`] instead. |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder.predict(activation_fct=...)`]      | Renamed to [`CrossEncoder.predict(activation_fn=...)`]                                                                                                 |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder.rank(activation_fct=...)`]         | Renamed to [`CrossEncoder.rank(activation_fn=...)`]                                                                                                    |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder.predict(num_workers=...)`]         | Fully deprecated, no longer has any effect.                                                                                                                                                   |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CrossEncoder.rank(num_workers=...)`]            | Fully deprecated, no longer has any effect.                                                                                                                                                   |
+------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note

The old keyword arguments still work, but they will emit a warning recommending you to use the new names instead.

### Migration for specific parameters from [`CrossEncoder.fit`][ïƒ?](#migration-for-specific-parameters-from-crossencoder-fit "Link to this heading")

CrossEncoder.fit(train_dataloader)

+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| v3.x                                                                                 | v4.x (recommended)                                                                  |
+======================================================================================+=====================================================================================+
| ::::                                                 | ::::                                                |
| ::: highlight                                                                        | ::: highlight                                                                       |
|     from sentence_transformers import CrossEncoder, InputExample                     |     from datasets import Dataset                                                    |
|     from torch.utils.data import DataLoader                                          |     from sentence_transformers import CrossEncoder, CrossEncoderTrainer             |
|                                                                                      |     from sentence_transformers.cross_encoder.losses import BinaryCrossEntropyLoss   |
|     # 1. Define the model. Either from scratch of by loading a pre-trained model     |                                                                                     |
|     model = CrossEncoder("microsoft/mpnet-base")                                     |     # Define a training dataset                                                     |
|                                                                                      |     train_examples = [                                                              |
|     # 2. Define your train examples. You need more than just two examples...         |         ,                                                                          |
|     train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)       |         ,                                                                          |
| ::::                                                                                 |     ]                                                                               |
|                                                                                      |     train_dataset = Dataset.from_list(train_examples)                               |
|                                                                                      |                                                                                     |
|                                                                                      |     # Define a loss function                                                        |
|                                                                                      |     loss = BinaryCrossEntropyLoss(model)                                            |
|                                                                                      |                                                                                     |
|                                                                                      |     # Finetune the model                                                            |
|                                                                                      |     trainer = CrossEncoderTrainer(                                                  |
|                                                                                      |         model=model,                                                                |
|                                                                                      |         train_dataset=train_dataset,                                                |
|                                                                                      |         loss=loss,                                                                  |
|                                                                                      |     )                                                                               |
|                                                                                      |     trainer.train()                                                                 |
|                                                                                      | :::                                                                                 |
|                                                                                      | ::::                                                                                |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

CrossEncoder.fit(loss_fct)

+--------------------------------------------+---------------------------------------------------------------------------------------+
| v3.x                                       | v4.x (recommended)                                                                    |
+============================================+=======================================================================================+
| ::::       | ::::                                                  |
| ::: highlight                              | ::: highlight                                                                         |
|     ...                                    |     from sentence_transformers.cross_encoder.losses import MSELoss                    |
|                                            |                                                                                       |
|     # Finetune the model                   |     ...                                                                               |
|     model.fit(                             |                                                                                       |
|         train_dataloader=train_dataloader, |     # Prepare the loss function                                                       |
|         loss_fct=torch.nn.MSELoss(),       |     # See all valid losses in https://sbert.net/docs/cross_encoder/loss_overview.html |
|     )                                      |     loss = MSELoss(model)                                                             |
| :::                                        |                                                                                       |
| ::::                                       |     # Finetune the model                                                              |
|                                            |     trainer = CrossEncoderTrainer(                                                    |
|                                            |         model=model,                                                                  |
|                                            |         args=args,                                                                    |
|                                            |         train_dataset=train_dataset,                                                  |
|                                            |         loss=loss,                                                                    |
|                                            |     )                                                                                 |
|                                            |     trainer.train()                                                                   |
|                                            | :::                                                                                   |
|                                            | ::::                                                                                  |
+--------------------------------------------+---------------------------------------------------------------------------------------+

CrossEncoder.fit(evaluator)

+-------------------------------------------------+-------------------------------------------------+
| v3.x                                            | v4.x (recommended)                              |
+=================================================+=================================================+
| ::::            | ::::            |
| ::: highlight                                   | ::: highlight                                   |
|     ...                                         |     # Load an evaluator                         |
|                                                 |     evaluator = CrossEncoderNanoBEIREvaluator() |
|     # Load an evaluator                         |                                                 |
|     evaluator = CrossEncoderNanoBEIREvaluator() |     # Finetune with an evaluator                |
|                                                 |     trainer = CrossEncoderTrainer(              |
|     # Finetune with an evaluator                |         model=model,                            |
|     model.fit(                                  |         train_dataset=train_dataset,            |
|         train_dataloader=train_dataloader,      |         eval_dataset=eval_dataset,              |
|         evaluator=evaluator,                    |         loss=loss,                              |
|     )                                           |         evaluator=evaluator,                    |
| :::                                             |     )                                           |
| ::::                                            |     trainer.train()                             |
|                                                 | :::                                             |
|                                                 | ::::                                            |
+-------------------------------------------------+-------------------------------------------------+

CrossEncoder.fit(epochs)

+--------------------------------------------+-------------------------------------------+
| v3.x                                       | v4.x (recommended)                        |
+============================================+===========================================+
| ::::       | ::::      |
| ::: highlight                              | ::: highlight                             |
|     ...                                    |     ...                                   |
|                                            |                                           |
|     # Finetune the model                   |     # Prepare the Training Arguments      |
|     model.fit(                             |     args = CrossEncoderTrainingArguments( |
|         train_dataloader=train_dataloader, |         num_train_epochs=1,               |
|         epochs=1,                          |     )                                     |
|     )                                      |                                           |
| :::                                        |     # Finetune the model                  |
| ::::                                       |     trainer = CrossEncoderTrainer(        |
|                                            |         model=model,                      |
|                                            |         args=args,                        |
|                                            |         train_dataset=train_dataset,      |
|                                            |         loss=loss,                        |
|                                            |     )                                     |
|                                            |     trainer.train()                       |
|                                            | :::                                       |
|                                            | ::::                                      |
+--------------------------------------------+-------------------------------------------+

CrossEncoder.fit(activation_fct)

+--------------------------------------------+-------------------------------------------------------------+
| v3.x                                       | v4.x (recommended)                                          |
+============================================+=============================================================+
| ::::       | ::::                        |
| ::: highlight                              | ::: highlight                                               |
|     ...                                    |     ...                                                     |
|                                            |                                                             |
|     # Finetune the model                   |     # Prepare the loss function                             |
|     model.fit(                             |     loss = MSELoss(model, activation_fn=torch.nn.Sigmoid()) |
|         train_dataloader=train_dataloader, |                                                             |
|         activation_fct=torch.nn.Sigmoid(), |     # Finetune the model                                    |
|     )                                      |     trainer = CrossEncoderTrainer(                          |
| :::                                        |         model=model,                                        |
| ::::                                       |         args=args,                                          |
|                                            |         train_dataset=train_dataset,                        |
|                                            |         loss=loss,                                          |
|                                            |     )                                                       |
|                                            |     trainer.train()                                         |
|                                            | :::                                                         |
|                                            | ::::                                                        |
+--------------------------------------------+-------------------------------------------------------------+

CrossEncoder.fit(scheduler)

+--------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| v3.x                                       | v4.x (recommended)                                                                                                 |
+============================================+====================================================================================================================+
| ::::       | ::::                                                                               |
| ::: highlight                              | ::: highlight                                                                                                      |
|     ...                                    |     ...                                                                                                            |
|                                            |                                                                                                                    |
|     # Finetune the model                   |     # Prepare the Training Arguments                                                                               |
|     model.fit(                             |     args = CrossEncoderTrainingArguments(                                                                          |
|         train_dataloader=train_dataloader, |         # See https://huggingface.co/docs/transformers/main_classes/optimizer_schedules#transformers.SchedulerType |
|         scheduler="WarmupLinear",          |         lr_scheduler_type="linear"                                                                                 |
|     )                                      |     )                                                                                                              |
| :::                                        |                                                                                                                    |
| ::::                                       |     # Finetune the model                                                                                           |
|                                            |     trainer = CrossEncoderTrainer(                                                                                 |
|                                            |         model=model,                                                                                               |
|                                            |         args=args,                                                                                                 |
|                                            |         train_dataset=train_dataset,                                                                               |
|                                            |         loss=loss,                                                                                                 |
|                                            |     )                                                                                                              |
|                                            |     trainer.train()                                                                                                |
|                                            | :::                                                                                                                |
|                                            | ::::                                                                                                               |
+--------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

CrossEncoder.fit(warmup_steps)

+--------------------------------------------+-------------------------------------------+
| v3.x                                       | v4.x (recommended)                        |
+============================================+===========================================+
| ::::       | ::::      |
| ::: highlight                              | ::: highlight                             |
|     ...                                    |     ...                                   |
|                                            |                                           |
|     # Finetune the model                   |     # Prepare the Training Arguments      |
|     model.fit(                             |     args = CrossEncoderTrainingArguments( |
|         train_dataloader=train_dataloader, |         warmup_steps=1000,                |
|         warmup_steps=1000,                 |     )                                     |
|     )                                      |                                           |
| :::                                        |     # Finetune the model                  |
| ::::                                       |     trainer = CrossEncoderTrainer(        |
|                                            |         model=model,                      |
|                                            |         args=args,                        |
|                                            |         train_dataset=train_dataset,      |
|                                            |         loss=loss,                        |
|                                            |     )                                     |
|                                            |     trainer.train()                       |
|                                            | :::                                       |
|                                            | ::::                                      |
+--------------------------------------------+-------------------------------------------+

CrossEncoder.fit(optimizer_class, optimizer_params)

+--------------------------------------------+-------------------------------------------------------------------------------------------------------+
| v3.x                                       | v4.x (recommended)                                                                                    |
+============================================+=======================================================================================================+
| ::::       | ::::                                                                  |
| ::: highlight                              | ::: highlight                                                                                         |
|     ...                                    |     ...                                                                                               |
|                                            |                                                                                                       |
|     # Finetune the model                   |     # Prepare the Training Arguments                                                                  |
|     model.fit(                             |     args = CrossEncoderTrainingArguments(                                                             |
|         train_dataloader=train_dataloader, |         # See https://github.com/huggingface/transformers/blob/main/src/transformers/training_args.py |
|         optimizer_class=torch.optim.AdamW, |         optim="adamw_torch",                                                                          |
|         optimizer_params=,    |         optim_args=,                                                                     |
|     )                                      |     )                                                                                                 |
| :::                                        |                                                                                                       |
| ::::                                       |     # Finetune the model                                                                              |
|                                            |     trainer = CrossEncoderTrainer(                                                                    |
|                                            |         model=model,                                                                                  |
|                                            |         args=args,                                                                                    |
|                                            |         train_dataset=train_dataset,                                                                  |
|                                            |         loss=loss,                                                                                    |
|                                            |     )                                                                                                 |
|                                            |     trainer.train()                                                                                   |
|                                            | :::                                                                                                   |
|                                            | ::::                                                                                                  |
+--------------------------------------------+-------------------------------------------------------------------------------------------------------+

CrossEncoder.fit(weight_decay)

+--------------------------------------------+-------------------------------------------+
| v3.x                                       | v4.x (recommended)                        |
+============================================+===========================================+
| ::::       | ::::      |
| ::: highlight                              | ::: highlight                             |
|     ...                                    |     ...                                   |
|                                            |                                           |
|     # Finetune the model                   |     # Prepare the Training Arguments      |
|     model.fit(                             |     args = CrossEncoderTrainingArguments( |
|         train_dataloader=train_dataloader, |         weight_decay=0.02,                |
|         weight_decay=0.02,                 |     )                                     |
|     )                                      |                                           |
| :::                                        |     # Finetune the model                  |
| ::::                                       |     trainer = CrossEncoderTrainer(        |
|                                            |         model=model,                      |
|                                            |         args=args,                        |
|                                            |         train_dataset=train_dataset,      |
|                                            |         loss=loss,                        |
|                                            |     )                                     |
|                                            |     trainer.train()                       |
|                                            | :::                                       |
|                                            | ::::                                      |
+--------------------------------------------+-------------------------------------------+

CrossEncoder.fit(evaluation_steps)

+--------------------------------------------+-------------------------------------------------------------------+
| v3.x                                       | v4.x (recommended)                                                |
+============================================+===================================================================+
| ::::       | ::::                              |
| ::: highlight                              | ::: highlight                                                     |
|     ...                                    |     ...                                                           |
|                                            |                                                                   |
|     # Finetune the model                   |     # Prepare the Training Arguments                              |
|     model.fit(                             |     args = CrossEncoderTrainingArguments(                         |
|         train_dataloader=train_dataloader, |         eval_strategy="steps",                                    |
|         evaluator=evaluator,               |         eval_steps=1000,                                          |
|         evaluation_steps=1000,             |     )                                                             |
|     )                                      |                                                                   |
| :::                                        |     # Finetune the model                                          |
| ::::                                       |     # Note: You need an eval_dataset and/or evaluator to evaluate |
|                                            |     trainer = CrossEncoderTrainer(                                |
|                                            |         model=model,                                              |
|                                            |         args=args,                                                |
|                                            |         train_dataset=train_dataset,                              |
|                                            |         eval_dataset=eval_dataset,                                |
|                                            |         loss=loss,                                                |
|                                            |         evaluator=evaluator,                                      |
|                                            |     )                                                             |
|                                            |     trainer.train()                                               |
|                                            | :::                                                               |
|                                            | ::::                                                              |
+--------------------------------------------+-------------------------------------------------------------------+

CrossEncoder.fit(output_path, save_best_model)

+--------------------------------------------+-------------------------------------------------------------------------------------+
| v3.x                                       | v4.x (recommended)                                                                  |
+============================================+=====================================================================================+
| ::::       | ::::                                                |
| ::: highlight                              | ::: highlight                                                                       |
|     ...                                    |     ...                                                                             |
|                                            |                                                                                     |
|     # Finetune the model                   |     # Prepare the Training Arguments                                                |
|     model.fit(                             |     args = CrossEncoderTrainingArguments(                                           |
|         train_dataloader=train_dataloader, |         load_best_model_at_end=True,                                                |
|         evaluator=evaluator,               |         metric_for_best_model="hotpotqa_ndcg@10", # E.g. `evaluator.primary_metric` |
|         output_path="my/path",             |     )                                                                               |
|         save_best_model=True,              |                                                                                     |
|     )                                      |     # Finetune the model                                                            |
| :::                                        |     trainer = CrossEncoderTrainer(                                                  |
| ::::                                       |         model=model,                                                                |
|                                            |         args=args,                                                                  |
|                                            |         train_dataset=train_dataset,                                                |
|                                            |         loss=loss,                                                                  |
|                                            |     )                                                                               |
|                                            |     trainer.train()                                                                 |
|                                            |                                                                                     |
|                                            |     # Save the best model at my output path                                         |
|                                            |     model.save_pretrained("my/path")                                                |
|                                            | :::                                                                                 |
|                                            | ::::                                                                                |
+--------------------------------------------+-------------------------------------------------------------------------------------+

CrossEncoder.fit(max_grad_norm)

+--------------------------------------------+-------------------------------------------+
| v3.x                                       | v4.x (recommended)                        |
+============================================+===========================================+
| ::::       | ::::      |
| ::: highlight                              | ::: highlight                             |
|     ...                                    |     ...                                   |
|                                            |                                           |
|     # Finetune the model                   |     # Prepare the Training Arguments      |
|     model.fit(                             |     args = CrossEncoderTrainingArguments( |
|         train_dataloader=train_dataloader, |         max_grad_norm=1,                  |
|         max_grad_norm=1,                   |     )                                     |
|     )                                      |                                           |
| :::                                        |     # Finetune the model                  |
| ::::                                       |     trainer = CrossEncoderTrainer(        |
|                                            |         model=model,                      |
|                                            |         args=args,                        |
|                                            |         train_dataset=train_dataset,      |
|                                            |         loss=loss,                        |
|                                            |     )                                     |
|                                            |     trainer.train()                       |
|                                            | :::                                       |
|                                            | ::::                                      |
+--------------------------------------------+-------------------------------------------+

CrossEncoder.fit(use_amp)

+--------------------------------------------+------------------------------------------------------------------------------+
| v3.x                                       | v4.x (recommended)                                                           |
+============================================+==============================================================================+
| ::::       | ::::                                         |
| ::: highlight                              | ::: highlight                                                                |
|     ...                                    |     ...                                                                      |
|                                            |                                                                              |
|     # Finetune the model                   |     # Prepare the Training Arguments                                         |
|     model.fit(                             |     args = CrossEncoderTrainingArguments(                                    |
|         train_dataloader=train_dataloader, |         fp16=True,                                                           |
|         use_amp=True,                      |         bf16=False, # If your GPU supports it, you can also use bf16 instead |
|     )                                      |     )                                                                        |
| :::                                        |                                                                              |
| ::::                                       |     # Finetune the model                                                     |
|                                            |     trainer = CrossEncoderTrainer(                                           |
|                                            |         model=model,                                                         |
|                                            |         args=args,                                                           |
|                                            |         train_dataset=train_dataset,                                         |
|                                            |         loss=loss,                                                           |
|                                            |     )                                                                        |
|                                            |     trainer.train()                                                          |
|                                            | :::                                                                          |
|                                            | ::::                                                                         |
+--------------------------------------------+------------------------------------------------------------------------------+

CrossEncoder.fit(callback)

+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| v3.x                                                                    | v4.x (recommended)                                                                                                             |
+=========================================================================+================================================================================================================================+
| ::::                                    | ::::                                                                                           |
| ::: highlight                                                           | ::: highlight                                                                                                                  |
|     ...                                                                 |     from transformers import TrainerCallback                                                                                   |
|                                                                         |                                                                                                                                |
|     def printer_callback(score, epoch, steps):                          |     ...                                                                                                                        |
|         print(f"Score:  at epoch , step ") |                                                                                                                                |
|                                                                         |     class PrinterCallback(TrainerCallback):                                                                                    |
|     # Finetune the model                                                |         # Subclass any method from https://huggingface.co/docs/transformers/main_classes/callback#transformers.TrainerCallback |
|     model.fit(                                                          |         def on_evaluate(self, args, state, control, metrics=None, **kwargs):                                                   |
|         train_dataloader=train_dataloader,                              |             print(f"Metrics:  at epoch , step ")                                  |
|         callback=printer_callback,                                      |                                                                                                                                |
|     )                                                                   |     printer_callback = PrinterCallback()                                                                                       |
| :::                                                                     |                                                                                                                                |
| ::::                                                                    |     # Finetune the model                                                                                                       |
|                                                                         |     trainer = CrossEncoderTrainer(                                                                                             |
|                                                                         |         model=model,                                                                                                           |
|                                                                         |         train_dataset=train_dataset,                                                                                           |
|                                                                         |         loss=loss,                                                                                                             |
|                                                                         |         callbacks=[printer_callback],                                                                                          |
|                                                                         |     )                                                                                                                          |
|                                                                         |     trainer.train()                                                                                                            |
|                                                                         | :::                                                                                                                            |
|                                                                         | ::::                                                                                                                           |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

CrossEncoder.fit(show_progress_bar)

+--------------------------------------------+-------------------------------------------+
| v3.x                                       | v4.x (recommended)                        |
+============================================+===========================================+
| ::::       | ::::      |
| ::: highlight                              | ::: highlight                             |
|     ...                                    |     ...                                   |
|                                            |                                           |
|     # Finetune the model                   |     # Prepare the Training Arguments      |
|     model.fit(                             |     args = CrossEncoderTrainingArguments( |
|         train_dataloader=train_dataloader, |         disable_tqdm=False,               |
|         show_progress_bar=True,            |     )                                     |
|     )                                      |                                           |
| :::                                        |     # Finetune the model                  |
| ::::                                       |     trainer = CrossEncoderTrainer(        |
|                                            |         model=model,                      |
|                                            |         args=args,                        |
|                                            |         train_dataset=train_dataset,      |
|                                            |         loss=loss,                        |
|                                            |     )                                     |
|                                            |     trainer.train()                       |
|                                            | :::                                       |
|                                            | ::::                                      |
+--------------------------------------------+-------------------------------------------+

\

Note

The old [[`CrossEncoder.fit`]](package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.fit "sentence_transformers.cross_encoder.CrossEncoder.fit") method still works, it was only softly deprecated. It now uses the new [[`CrossEncoderTrainer`]](package_reference/cross_encoder/trainer.html#sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer "sentence_transformers.cross_encoder.trainer.CrossEncoderTrainer") behind the scenes.

### Migration for CrossEncoder evaluators[ïƒ?](#migration-for-crossencoder-evaluators "Link to this heading")

+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v3.x                                                                       | v4.x (recommended)                                                                                                                                                                                                                                                                                                                                                                                                      |
+============================================================================+=========================================================================================================================================================================================================================================================================================================================================================================================================================+
| [`CEBinaryAccuracyEvaluator`]       | Use [[`CrossEncoderClassificationEvaluator`]](package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator"), an encompassed evaluator which uses the same inputs & outputs. |
+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CEBinaryClassificationEvaluator`] | Use [[`CrossEncoderClassificationEvaluator`]](package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator"), an encompassed evaluator which uses the same inputs & outputs. |
+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CECorrelationEvaluator`]          | Use [[`CrossEncoderCorrelationEvaluator`]](package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderCorrelationEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderCorrelationEvaluator"), this evaluator was renamed.                                             |
+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CEF1Evaluator`]                   | Use [[`CrossEncoderClassificationEvaluator`]](package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator"), an encompassed evaluator which uses the same inputs & outputs. |
+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CESoftmaxAccuracyEvaluator`]      | Use [[`CrossEncoderClassificationEvaluator`]](package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderClassificationEvaluator"), an encompassed evaluator which uses the same inputs & outputs. |
+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`CERerankingEvaluator`]            | Renamed to [[`CrossEncoderRerankingEvaluator`]](package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator "sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator"), this evaluator was renamed                                             |
+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note

The old evaluators still work, they will simply warn you to update to the new evaluators.

## Migrating from v2.x to v3.x[ïƒ?](#migrating-from-v2-x-to-v3-x "Link to this heading")

The v3 Sentence Transformers release refactored the training of [[`SentenceTransformer`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") embedding models, replacing [[`SentenceTransformer.fit`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.fit "sentence_transformers.SentenceTransformer.fit") with a [[`SentenceTransformerTrainer`]](package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") and [[`SentenceTransformerTrainingArguments`]](package_reference/sentence_transformer/training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments"). This update softly deprecated [[`SentenceTransformer.fit`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.fit "sentence_transformers.SentenceTransformer.fit"), meaning that it still works, but itâ€™s recommended to switch to the new v3.x training format. Behind the scenes, this method now uses the new trainer.

Warning

If you donâ€™t have code that uses [[`SentenceTransformer.fit`]](package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.fit "sentence_transformers.SentenceTransformer.fit"), then you will not have to make any changes to your code to update from v2.x to v3.x.

If you do, your code still works, but it is recommended to switch to the new v3.x training format, as it allows more training arguments and functionality. See the [Training Overview](sentence_transformer/training_overview.html) for more details.

+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| v2.x                                                                             | v3.x (recommended)                                                                    |
+==================================================================================+=======================================================================================+
| ::::                                            | ::::                                                 |
| ::: highlight                                                                    | ::: highlight                                                                         |
|     from sentence_transformers import SentenceTransformer, InputExample, losses  |     from datasets import load_dataset                                                 |
|     from torch.utils.data import DataLoader                                      |     from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer |
|                                                                                  |     from sentence_transformers.losses import MultipleNegativesRankingLoss             |
|     # 1. Define the model. Either from scratch of by loading a pre-trained model |                                                                                       |
|     model = SentenceTransformer("microsoft/mpnet-base")                          |     # 1. Define the model. Either from scratch of by loading a pre-trained model      |
|                                                                                  |     model = SentenceTransformer("microsoft/mpnet-base")                               |
|     # 2. Define your train examples. You need more than just two examples...     |                                                                                       |
|     train_examples = [                                                           |     # 2. Load a dataset to finetune on                                                |
|         InputExample(texts=[                                                     |     dataset = load_dataset("sentence-transformers/all-nli", "triplet")                |
|             "A person on a horse jumps over a broken down airplane.",            |     train_dataset = dataset["train"].select(range(10_000))                            |
|             "A person is outdoors, on a horse.",                                 |     eval_dataset = dataset["dev"].select(range(1_000))                                |
|             "A person is at a diner, ordering an omelette.",                     |                                                                                       |
|         ]),                                                                      |     # 3. Define a loss function                                                       |
|         InputExample(texts=[                                                     |     loss = MultipleNegativesRankingLoss(model)                                        |
|             "Children smiling and waving at camera",                             |                                                                                       |
|             "There are children present",                                        |     # 4. Create a trainer & train                                                     |
|             "The kids are frowning",                                             |     trainer = SentenceTransformerTrainer(                                             |
|         ]),                                                                      |         model=model,                                                                  |
|     ]                                                                            |         train_dataset=train_dataset,                                                  |
|     train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)   |         eval_dataset=eval_dataset,                                                    |
|                                                                                  |         loss=loss,                                                                    |
|     # 3. Define a loss function                                                  |     )                                                                                 |
|     train_loss = losses.MultipleNegativesRankingLoss(model)                      |     trainer.train()                                                                   |
|                                                                                  |                                                                                       |
|     # 4. Finetune the model                                                      |     # 5. Save the trained model                                                       |
|     model.fit(                                                                   |     model.save_pretrained("models/mpnet-base-all-nli")                                |
|         train_objectives=[(train_dataloader, train_loss)],                       |     # model.push_to_hub("mpnet-base-all-nli")                                         |
|         epochs=1,                                                                | :::                                                                                   |
|         warmup_steps=100,                                                        | ::::                                                                                  |
|     )                                                                            |                                                                                       |
|                                                                                  |                                                                                       |
|     # 5. Save the trained model                                                  |                                                                                       |
|     model.save_pretrained("models/mpnet-base-all-nli")                           |                                                                                       |
| :::                                                                              |                                                                                       |
| ::::                                                                             |                                                                                       |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

: [Old and new training flow][ïƒ?](#id5 "Link to this table") 

### Migration for specific parameters from [`SentenceTransformer.fit`][ïƒ?](#migration-for-specific-parameters-from-sentencetransformer-fit "Link to this heading")

SentenceTransformer.fit(train_objectives)

+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| v2.x                                                                            | v3.x (recommended)                                                                    |
+=================================================================================+=======================================================================================+
| ::::                                            | ::::                                                  |
| ::: highlight                                                                   | ::: highlight                                                                         |
|     from sentence_transformers import SentenceTransformer, InputExample, losses |     from datasets import Dataset                                                      |
|     from torch.utils.data import DataLoader                                     |     from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer |
|                                                                                 |     from sentence_transformers.losses import MultipleNegativesRankingLoss             |
|     # Define a training dataloader                                              |                                                                                       |
|     train_examples = [                                                          |     # Define a training dataset                                                       |
|         InputExample(texts=[                                                    |     train_examples = [                                                                |
|             "A person on a horse jumps over a broken down airplane.",           |         ,                                                                            |
|             "Children smiling and waving at camera",                            |         ,                                                                            |
|     train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)  |     ]                                                                                 |
|                                                                                 |     train_dataset = Dataset.from_list(train_examples)                                 |
|     # Define a loss function                                                    |                                                                                       |
|     train_loss = losses.MultipleNegativesRankingLoss(model)                     |     # Define a loss function                                                          |
|                                                                                 |     loss = MultipleNegativesRankingLoss(model)                                        |
|     # Finetune the model                                                        |                                                                                       |
|     model.fit(train_objectives=[(train_dataloader, train_loss)])                |     # Finetune the model                                                              |
| :::                                                                             |     trainer = SentenceTransformerTrainer(                                             |
| ::::                                                                            |         model=model,                                                                  |
|                                                                                 |         train_dataset=train_dataset,                                                  |
|                                                                                 |         loss=loss,                                                                    |
|                                                                                 |     )                                                                                 |
|                                                                                 |     trainer.train()                                                                   |
|                                                                                 | :::                                                                                   |
|                                                                                 | ::::                                                                                  |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

SentenceTransformer.fit(evaluator)

+------------------------------------------------------------+-------------------------------------------+
| v2.x                                                       | v3.x (recommended)                        |
+============================================================+===========================================+
| ::::                       | ::::      |
| ::: highlight                                              | ::: highlight                             |
|     ...                                                    |     # Load an evaluator                   |
|                                                            |     evaluator = NanoBEIREvaluator()       |
|     # Load an evaluator                                    |                                           |
|     evaluator = NanoBEIREvaluator()                        |     # Finetune with an evaluator          |
|                                                            |     trainer = SentenceTransformerTrainer( |
|     # Finetune with an evaluator                           |         model=model,                      |
|     model.fit(                                             |         train_dataset=train_dataset,      |
|         train_objectives=[(train_dataloader, train_loss)], |         eval_dataset=eval_dataset,        |
|         evaluator=evaluator,                               |         loss=loss,                        |
|     )                                                      |         evaluator=evaluator,              |
| :::                                                        |     )                                     |
| ::::                                                       |     trainer.train()                       |
|                                                            | :::                                       |
|                                                            | ::::                                      |
+------------------------------------------------------------+-------------------------------------------+

SentenceTransformer.fit(epochs)

+------------------------------------------------------------+--------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                               |
+============================================================+==================================================+
| ::::                       | ::::             |
| ::: highlight                                              | ::: highlight                                    |
|     ...                                                    |     ...                                          |
|                                                            |                                                  |
|     # Finetune the model                                   |     # Prepare the Training Arguments             |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments( |
|         train_objectives=[(train_dataloader, train_loss)], |         num_train_epochs=1,                      |
|         epochs=1,                                          |     )                                            |
|     )                                                      |                                                  |
| :::                                                        |     # Finetune the model                         |
| ::::                                                       |     trainer = SentenceTransformerTrainer(        |
|                                                            |         model=model,                             |
|                                                            |         args=args,                               |
|                                                            |         train_dataset=train_dataset,             |
|                                                            |         loss=loss,                               |
|                                                            |     )                                            |
|                                                            |     trainer.train()                              |
|                                                            | :::                                              |
|                                                            | ::::                                             |
+------------------------------------------------------------+--------------------------------------------------+

SentenceTransformer.fit(steps_per_epoch)

+------------------------------------------------------------+-------------------------------------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                                                            |
+============================================================+===============================================================================+
| ::::                       | ::::                                          |
| ::: highlight                                              | ::: highlight                                                                 |
|     ...                                                    |     ...                                                                       |
|                                                            |                                                                               |
|     # Finetune the model                                   |     # Prepare the Training Arguments                                          |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments(                              |
|         train_objectives=[(train_dataloader, train_loss)], |         max_steps=1000, # Note: max_steps is across all epochs, not per epoch |
|         steps_per_epoch=1000,                              |     )                                                                         |
|     )                                                      |                                                                               |
| :::                                                        |     # Finetune the model                                                      |
| ::::                                                       |     trainer = SentenceTransformerTrainer(                                     |
|                                                            |         model=model,                                                          |
|                                                            |         args=args,                                                            |
|                                                            |         train_dataset=train_dataset,                                          |
|                                                            |         loss=loss,                                                            |
|                                                            |     )                                                                         |
|                                                            |     trainer.train()                                                           |
|                                                            | :::                                                                           |
|                                                            | ::::                                                                          |
+------------------------------------------------------------+-------------------------------------------------------------------------------+

SentenceTransformer.fit(scheduler)

+------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                                                                                                 |
+============================================================+====================================================================================================================+
| ::::                       | ::::                                                                               |
| ::: highlight                                              | ::: highlight                                                                                                      |
|     ...                                                    |     ...                                                                                                            |
|                                                            |                                                                                                                    |
|     # Finetune the model                                   |     # Prepare the Training Arguments                                                                               |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments(                                                                   |
|         train_objectives=[(train_dataloader, train_loss)], |         # See https://huggingface.co/docs/transformers/main_classes/optimizer_schedules#transformers.SchedulerType |
|         scheduler="WarmupLinear",                          |         lr_scheduler_type="linear"                                                                                 |
|     )                                                      |     )                                                                                                              |
| :::                                                        |                                                                                                                    |
| ::::                                                       |     # Finetune the model                                                                                           |
|                                                            |     trainer = SentenceTransformerTrainer(                                                                          |
|                                                            |         model=model,                                                                                               |
|                                                            |         args=args,                                                                                                 |
|                                                            |         train_dataset=train_dataset,                                                                               |
|                                                            |         loss=loss,                                                                                                 |
|                                                            |     )                                                                                                              |
|                                                            |     trainer.train()                                                                                                |
|                                                            | :::                                                                                                                |
|                                                            | ::::                                                                                                               |
+------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

SentenceTransformer.fit(warmup_steps)

+------------------------------------------------------------+--------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                               |
+============================================================+==================================================+
| ::::                       | ::::             |
| ::: highlight                                              | ::: highlight                                    |
|     ...                                                    |     ...                                          |
|                                                            |                                                  |
|     # Finetune the model                                   |     # Prepare the Training Arguments             |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments( |
|         train_objectives=[(train_dataloader, train_loss)], |         warmup_steps=1000,                       |
|         warmup_steps=1000,                                 |     )                                            |
|     )                                                      |                                                  |
| :::                                                        |     # Finetune the model                         |
| ::::                                                       |     trainer = SentenceTransformerTrainer(        |
|                                                            |         model=model,                             |
|                                                            |         args=args,                               |
|                                                            |         train_dataset=train_dataset,             |
|                                                            |         loss=loss,                               |
|                                                            |     )                                            |
|                                                            |     trainer.train()                              |
|                                                            | :::                                              |
|                                                            | ::::                                             |
+------------------------------------------------------------+--------------------------------------------------+

SentenceTransformer.fit(optimizer_class, optimizer_params)

+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                                                                                    |
+============================================================+=======================================================================================================+
| ::::                       | ::::                                                                  |
| ::: highlight                                              | ::: highlight                                                                                         |
|     ...                                                    |     ...                                                                                               |
|                                                            |                                                                                                       |
|     # Finetune the model                                   |     # Prepare the Training Arguments                                                                  |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments(                                                      |
|         train_objectives=[(train_dataloader, train_loss)], |         # See https://github.com/huggingface/transformers/blob/main/src/transformers/training_args.py |
|         optimizer_class=torch.optim.AdamW,                 |         optim="adamw_torch",                                                                          |
|         optimizer_params=,                    |         optim_args=,                                                                     |
|     )                                                      |     )                                                                                                 |
| :::                                                        |                                                                                                       |
| ::::                                                       |     # Finetune the model                                                                              |
|                                                            |     trainer = SentenceTransformerTrainer(                                                             |
|                                                            |         model=model,                                                                                  |
|                                                            |         args=args,                                                                                    |
|                                                            |         train_dataset=train_dataset,                                                                  |
|                                                            |         loss=loss,                                                                                    |
|                                                            |     )                                                                                                 |
|                                                            |     trainer.train()                                                                                   |
|                                                            | :::                                                                                                   |
|                                                            | ::::                                                                                                  |
+------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

SentenceTransformer.fit(weight_decay)

+------------------------------------------------------------+--------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                               |
+============================================================+==================================================+
| ::::                       | ::::             |
| ::: highlight                                              | ::: highlight                                    |
|     ...                                                    |     ...                                          |
|                                                            |                                                  |
|     # Finetune the model                                   |     # Prepare the Training Arguments             |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments( |
|         train_objectives=[(train_dataloader, train_loss)], |         weight_decay=0.02,                       |
|         weight_decay=0.02,                                 |     )                                            |
|     )                                                      |                                                  |
| :::                                                        |     # Finetune the model                         |
| ::::                                                       |     trainer = SentenceTransformerTrainer(        |
|                                                            |         model=model,                             |
|                                                            |         args=args,                               |
|                                                            |         train_dataset=train_dataset,             |
|                                                            |         loss=loss,                               |
|                                                            |     )                                            |
|                                                            |     trainer.train()                              |
|                                                            | :::                                              |
|                                                            | ::::                                             |
+------------------------------------------------------------+--------------------------------------------------+

SentenceTransformer.fit(evaluation_steps)

+------------------------------------------------------------+-------------------------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                                                |
+============================================================+===================================================================+
| ::::                       | ::::                              |
| ::: highlight                                              | ::: highlight                                                     |
|     ...                                                    |     ...                                                           |
|                                                            |                                                                   |
|     # Finetune the model                                   |     # Prepare the Training Arguments                              |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments(                  |
|         train_objectives=[(train_dataloader, train_loss)], |         eval_strategy="steps",                                    |
|         evaluator=evaluator,                               |         eval_steps=1000,                                          |
|         evaluation_steps=1000,                             |     )                                                             |
|     )                                                      |                                                                   |
| :::                                                        |     # Finetune the model                                          |
| ::::                                                       |     # Note: You need an eval_dataset and/or evaluator to evaluate |
|                                                            |     trainer = SentenceTransformerTrainer(                         |
|                                                            |         model=model,                                              |
|                                                            |         args=args,                                                |
|                                                            |         train_dataset=train_dataset,                              |
|                                                            |         eval_dataset=eval_dataset,                                |
|                                                            |         loss=loss,                                                |
|                                                            |         evaluator=evaluator,                                      |
|                                                            |     )                                                             |
|                                                            |     trainer.train()                                               |
|                                                            | :::                                                               |
|                                                            | ::::                                                              |
+------------------------------------------------------------+-------------------------------------------------------------------+

SentenceTransformer.fit(output_path, save_best_model)

+------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                                                                         |
+============================================================+============================================================================================+
| ::::                       | ::::                                                       |
| ::: highlight                                              | ::: highlight                                                                              |
|     ...                                                    |     ...                                                                                    |
|                                                            |                                                                                            |
|     # Finetune the model                                   |     # Prepare the Training Arguments                                                       |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments(                                           |
|         train_objectives=[(train_dataloader, train_loss)], |         load_best_model_at_end=True,                                                       |
|         evaluator=evaluator,                               |         metric_for_best_model="all_nli_cosine_accuracy", # E.g. `evaluator.primary_metric` |
|         output_path="my/path",                             |     )                                                                                      |
|         save_best_model=True,                              |                                                                                            |
|     )                                                      |     # Finetune the model                                                                   |
| :::                                                        |     trainer = SentenceTransformerTrainer(                                                  |
| ::::                                                       |         model=model,                                                                       |
|                                                            |         args=args,                                                                         |
|                                                            |         train_dataset=train_dataset,                                                       |
|                                                            |         loss=loss,                                                                         |
|                                                            |     )                                                                                      |
|                                                            |     trainer.train()                                                                        |
|                                                            |                                                                                            |
|                                                            |     # Save the best model at my output path                                                |
|                                                            |     model.save_pretrained("my/path")                                                       |
|                                                            | :::                                                                                        |
|                                                            | ::::                                                                                       |
+------------------------------------------------------------+--------------------------------------------------------------------------------------------+

SentenceTransformer.fit(max_grad_norm)

+------------------------------------------------------------+--------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                               |
+============================================================+==================================================+
| ::::                       | ::::             |
| ::: highlight                                              | ::: highlight                                    |
|     ...                                                    |     ...                                          |
|                                                            |                                                  |
|     # Finetune the model                                   |     # Prepare the Training Arguments             |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments( |
|         train_objectives=[(train_dataloader, train_loss)], |         max_grad_norm=1,                         |
|         max_grad_norm=1,                                   |     )                                            |
|     )                                                      |                                                  |
| :::                                                        |     # Finetune the model                         |
| ::::                                                       |     trainer = SentenceTransformerTrainer(        |
|                                                            |         model=model,                             |
|                                                            |         args=args,                               |
|                                                            |         train_dataset=train_dataset,             |
|                                                            |         loss=loss,                               |
|                                                            |     )                                            |
|                                                            |     trainer.train()                              |
|                                                            | :::                                              |
|                                                            | ::::                                             |
+------------------------------------------------------------+--------------------------------------------------+

SentenceTransformer.fit(use_amp)

+------------------------------------------------------------+------------------------------------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                                                           |
+============================================================+==============================================================================+
| ::::                       | ::::                                         |
| ::: highlight                                              | ::: highlight                                                                |
|     ...                                                    |     ...                                                                      |
|                                                            |                                                                              |
|     # Finetune the model                                   |     # Prepare the Training Arguments                                         |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments(                             |
|         train_objectives=[(train_dataloader, train_loss)], |         fp16=True,                                                           |
|         use_amp=True,                                      |         bf16=False, # If your GPU supports it, you can also use bf16 instead |
|     )                                                      |     )                                                                        |
| :::                                                        |                                                                              |
| ::::                                                       |     # Finetune the model                                                     |
|                                                            |     trainer = SentenceTransformerTrainer(                                    |
|                                                            |         model=model,                                                         |
|                                                            |         args=args,                                                           |
|                                                            |         train_dataset=train_dataset,                                         |
|                                                            |         loss=loss,                                                           |
|                                                            |     )                                                                        |
|                                                            |     trainer.train()                                                          |
|                                                            | :::                                                                          |
|                                                            | ::::                                                                         |
+------------------------------------------------------------+------------------------------------------------------------------------------+

SentenceTransformer.fit(callback)

+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| v2.x                                                                    | v3.x (recommended)                                                                                                             |
+=========================================================================+================================================================================================================================+
| ::::                                    | ::::                                                                                           |
| ::: highlight                                                           | ::: highlight                                                                                                                  |
|     ...                                                                 |     from transformers import TrainerCallback                                                                                   |
|                                                                         |                                                                                                                                |
|     def printer_callback(score, epoch, steps):                          |     ...                                                                                                                        |
|         print(f"Score:  at epoch , step ") |                                                                                                                                |
|                                                                         |     class PrinterCallback(TrainerCallback):                                                                                    |
|     # Finetune the model                                                |         # Subclass any method from https://huggingface.co/docs/transformers/main_classes/callback#transformers.TrainerCallback |
|     model.fit(                                                          |         def on_evaluate(self, args, state, control, metrics=None, **kwargs):                                                   |
|         train_objectives=[(train_dataloader, train_loss)],              |             print(f"Metrics:  at epoch , step ")                                  |
|         callback=printer_callback,                                      |                                                                                                                                |
|     )                                                                   |     printer_callback = PrinterCallback()                                                                                       |
| :::                                                                     |                                                                                                                                |
| ::::                                                                    |     # Finetune the model                                                                                                       |
|                                                                         |     trainer = SentenceTransformerTrainer(                                                                                      |
|                                                                         |         model=model,                                                                                                           |
|                                                                         |         train_dataset=train_dataset,                                                                                           |
|                                                                         |         loss=loss,                                                                                                             |
|                                                                         |         callbacks=[printer_callback],                                                                                          |
|                                                                         |     )                                                                                                                          |
|                                                                         |     trainer.train()                                                                                                            |
|                                                                         | :::                                                                                                                            |
|                                                                         | ::::                                                                                                                           |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

SentenceTransformer.fit(show_progress_bar)

+------------------------------------------------------------+--------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                               |
+============================================================+==================================================+
| ::::                       | ::::             |
| ::: highlight                                              | ::: highlight                                    |
|     ...                                                    |     ...                                          |
|                                                            |                                                  |
|     # Finetune the model                                   |     # Prepare the Training Arguments             |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments( |
|         train_objectives=[(train_dataloader, train_loss)], |         disable_tqdm=False,                      |
|         show_progress_bar=True,                            |     )                                            |
|     )                                                      |                                                  |
| :::                                                        |     # Finetune the model                         |
| ::::                                                       |     trainer = SentenceTransformerTrainer(        |
|                                                            |         model=model,                             |
|                                                            |         args=args,                               |
|                                                            |         train_dataset=train_dataset,             |
|                                                            |         loss=loss,                               |
|                                                            |     )                                            |
|                                                            |     trainer.train()                              |
|                                                            | :::                                              |
|                                                            | ::::                                             |
+------------------------------------------------------------+--------------------------------------------------+

SentenceTransformer.fit(checkpoint_path, checkpoint_save_steps, checkpoint_save_total_limit)

+------------------------------------------------------------+---------------------------------------------------------------------+
| v2.x                                                       | v3.x (recommended)                                                  |
+============================================================+=====================================================================+
| ::::                       | ::::                                |
| ::: highlight                                              | ::: highlight                                                       |
|     ...                                                    |     ...                                                             |
|                                                            |                                                                     |
|     # Finetune the model                                   |     # Prepare the Training Arguments                                |
|     model.fit(                                             |     args = SentenceTransformerTrainingArguments(                    |
|         train_objectives=[(train_dataloader, train_loss)], |         eval_strategy="steps",                                      |
|         checkpoint_path="checkpoints",                     |         eval_steps=5000,                                            |
|         checkpoint_save_steps=5000,                        |         save_strategy="steps",                                      |
|         checkpoint_save_total_limit=2,                     |         save_steps=5000,                                            |
|     )                                                      |         save_total_limit=2,                                         |
| :::                                                        |     )                                                               |
| ::::                                                       |                                                                     |
|                                                            |     # Finetune the model                                            |
|                                                            |     # Note: You need an eval_dataset and/or evaluator to checkpoint |
|                                                            |     trainer = SentenceTransformerTrainer(                           |
|                                                            |         model=model,                                                |
|                                                            |         args=args,                                                  |
|                                                            |         train_dataset=train_dataset,                                |
|                                                            |         eval_dataset=eval_dataset,                                  |
|                                                            |         loss=loss,                                                  |
|                                                            |     )                                                               |
|                                                            |     trainer.train()                                                 |
|                                                            | :::                                                                 |
|                                                            | ::::                                                                |
+------------------------------------------------------------+---------------------------------------------------------------------+

\

### Migration for custom Datasets and DataLoaders used in [`SentenceTransformer.fit`][ïƒ?](#migration-for-custom-datasets-and-dataloaders-used-in-sentencetransformer-fit "Link to this heading")

+------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v2.x                                                                   | v3.x (recommended)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+========================================================================+===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| [`ParallelSentencesDataset`]    | Manually creating a [[`Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") and adding a [`label`] column for embeddings. Alternatively, consider loading one of our pre-provided [Parallel Sentences Datasets](https://huggingface.co/collections/sentence-transformers/parallel-sentences-datasets-6644d644123d31ba5b1c8785).                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`SentenceLabelDataset`]        | Loading or creating a [[`Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") and using [`SentenceTransformerTrainingArguments(batch_sampler=BatchSamplers.GROUP_BY_LABEL)`] (uses the [[`GroupByLabelBatchSampler`]](package_reference/sentence_transformer/sampler.html#sentence_transformers.sampler.GroupByLabelBatchSampler "sentence_transformers.sampler.GroupByLabelBatchSampler")). Recommended for the BatchTripletLosses.                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`DenoisingAutoEncoderDataset`] | Manually adding a column with noisy text to a [[`Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") with texts, e.g. with [`Dataset.map`].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`NoDuplicatesDataLoader`]      | Loading or creating a [[`Dataset`]](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset "(in datasets vmain)") and using [`SentenceTransformerTrainingArguments(batch_sampler=BatchSamplers.NO_DUPLICATES)`] (uses the [[`NoDuplicatesBatchSampler`]](package_reference/sentence_transformer/sampler.html#sentence_transformers.sampler.NoDuplicatesBatchSampler "sentence_transformers.sampler.NoDuplicatesBatchSampler")). Recommended for [[`MultipleNegativesRankingLoss`]](package_reference/sentence_transformer/losses.html#sentence_transformers.losses.MultipleNegativesRankingLoss "sentence_transformers.losses.MultipleNegativesRankingLoss"). |
+------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+