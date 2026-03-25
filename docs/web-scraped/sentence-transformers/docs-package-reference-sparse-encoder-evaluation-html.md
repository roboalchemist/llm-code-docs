# Source: https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html

Title: Evaluation — Sentence Transformers documentation

URL Source: https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html

Markdown Content:
`sentence_transformers.sparse_encoder.evaluation` defines different classes, that can be used to evaluate the SparseEncoder model during training.

SparseInformationRetrievalEvaluator[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparseinformationretrievalevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.evaluation.SparseInformationRetrievalEvaluator(_queries:dict[str,str]_, _corpus:dict[str,str]_, _relevant\_docs:dict[str,set[str]]_, _corpus\_chunk\_size:int=50000_, _mrr\_at\_k:list[int]=[10]_, _ndcg\_at\_k:list[int]=[10]_, _accuracy\_at\_k:list[int]=[1,3,5,10]_, _precision\_recall\_at\_k:list[int]=[1,3,5,10]_, _map\_at\_k:list[int]=[100]_, _show\_progress\_bar:bool=False_, _batch\_size:int=32_, _name:str=''_, _write\_csv:bool=True_, _max\_active\_dims:int|None=None_, _score\_functions:dict[str,Callable[[[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)"),[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")],[torch.Tensor](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")]]|None=None_, _main\_score\_function:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.SimilarityFunction")|None=None_, _query\_prompt:str|None=None_, _query\_prompt\_name:str|None=None_, _corpus\_prompt:str|None=None_, _corpus\_prompt\_name:str|None=None_, _write\_predictions:bool=False_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/evaluation/SparseInformationRetrievalEvaluator.py#L24-L309)[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseInformationRetrievalEvaluator "Link to this definition")
This evaluator extends [`InformationRetrievalEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator "sentence_transformers.evaluation.InformationRetrievalEvaluator") but is specifically designed for sparse encoder models.

This class evaluates an Information Retrieval (IR) setting.

Given a set of queries and a large corpus set. It will retrieve for each query the top-k most similar document. It measures Mean Reciprocal Rank (MRR), Recall@k, and Normalized Discounted Cumulative Gain (NDCG)

Parameters:
*   **queries** (_Dict_ _[_ _str_ _,_ _str_ _]_) – A dictionary mapping query IDs to queries.

*   **corpus** (_Dict_ _[_ _str_ _,_ _str_ _]_) – A dictionary mapping document IDs to documents.

*   **relevant_docs** (_Dict_ _[_ _str_ _,_ _Set_ _[_ _str_ _]_ _]_) – A dictionary mapping query IDs to a set of relevant document IDs.

*   **corpus_chunk_size** (_int_) – The size of each chunk of the corpus. Defaults to 50000.

*   **mrr_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for MRR calculation. Defaults to [10].

*   **ndcg_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for NDCG calculation. Defaults to [10].

*   **accuracy_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for accuracy calculation. Defaults to [1, 3, 5, 10].

*   **precision_recall_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for precision and recall calculation. Defaults to [1, 3, 5, 10].

*   **map_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for MAP calculation. Defaults to [100].

*   **show_progress_bar** (_bool_) – Whether to show a progress bar during evaluation. Defaults to False.

*   **batch_size** (_int_) – The batch size for evaluation. Defaults to 32.

*   **name** (_str_) – A name for the evaluation. Defaults to “”.

*   **write_csv** (_bool_) – Whether to write the evaluation results to a CSV file. Defaults to True.

*   **max_active_dims** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The maximum number of active dimensions to use. None uses the model’s current max_active_dims. Defaults to None.

*   **score_functions** (_Dict_ _[_ _str_ _,_ _Callable_ _[_ _[_ _Tensor_ _,_ _Tensor_ _]_ _,_ _Tensor_ _]_ _]_) – A dictionary mapping score function names to score functions. Defaults to the `similarity` function from the `model`.

*   **main_score_function** (_Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_ _,_ _optional_) – The main score function to use for evaluation. Defaults to None.

*   **query_prompt** (_str_ _,_ _optional_) – The prompt to be used when encoding the corpus. Defaults to None.

*   **query_prompt_name** (_str_ _,_ _optional_) – The name of the prompt to be used when encoding the corpus. Defaults to None.

*   **corpus_prompt** (_str_ _,_ _optional_) – The prompt to be used when encoding the corpus. Defaults to None.

*   **corpus_prompt_name** (_str_ _,_ _optional_) – The name of the prompt to be used when encoding the corpus. Defaults to None.

*   **write_predictions** (_bool_) – Whether to write the predictions to a JSONL file. Defaults to False. This can be useful for downstream evaluation as it can be used as input to the [`ReciprocalRankFusionEvaluator`](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator") that accept precomputed predictions.

Example

import logging

from datasets import load_dataset

from sentence_transformers import SparseEncoder
from sentence_transformers.sparse_encoder.evaluation import SparseInformationRetrievalEvaluator

logging.basicConfig(format="%(message)s", level=logging.INFO)

# Load a model
model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

# Load the NFcorpus IR dataset (https://huggingface.co/datasets/BeIR/nfcorpus, https://huggingface.co/datasets/BeIR/nfcorpus-qrels)
corpus = load_dataset("BeIR/nfcorpus", "corpus", split="corpus")
queries = load_dataset("BeIR/nfcorpus", "queries", split="queries")
relevant_docs_data = load_dataset("BeIR/nfcorpus-qrels", split="test")

# For this dataset, we want to concatenate the title and texts for the corpus
corpus = corpus.map(lambda x: {"text": x["title"] + " " + x["text"]}, remove_columns=["title"])

# Convert the datasets to dictionaries
corpus = dict(zip(corpus["_id"], corpus["text"]))  # Our corpus (cid => document)
queries = dict(zip(queries["_id"], queries["text"]))  # Our queries (qid => question)
relevant_docs = {}  # Query ID to relevant documents (qid => set([relevant_cids])
for qid, corpus_ids in zip(relevant_docs_data["query-id"], relevant_docs_data["corpus-id"]):
    qid = str(qid)
    corpus_ids = str(corpus_ids)
    if qid not in relevant_docs:
        relevant_docs[qid] = set()
    relevant_docs[qid].add(corpus_ids)

# Given queries, a corpus and a mapping with relevant documents, the SparseInformationRetrievalEvaluator computes different IR metrics.
ir_evaluator = SparseInformationRetrievalEvaluator(
    queries=queries,
    corpus=corpus,
    relevant_docs=relevant_docs,
    name="BeIR-nfcorpus-subset-test",
    show_progress_bar=True,
    batch_size=16,
)

# Run evaluation
results = ir_evaluator(model)
'''
Queries: 323
Corpus: 3269

Score-Function: dot
Accuracy@1: 49.23%
Accuracy@3: 63.47%
Accuracy@5: 66.56%
Accuracy@10: 71.83%
Precision@1: 49.23%
Precision@3: 39.63%
Precision@5: 33.13%
Precision@10: 25.23%
Recall@1: 6.08%
Recall@3: 11.60%
Recall@5: 13.47%
Recall@10: 17.01%
MRR@10: 0.5706
NDCG@10: 0.3530
MAP@100: 0.1778
Model Query Sparsity: Active Dimensions: 40.0, Sparsity Ratio: 0.9987
Model Corpus Sparsity: Active Dimensions: 206.2, Sparsity Ratio: 0.9932
Average FLOPS: 4.66
'''
# Print the results
print(f"Primary metric: {ir_evaluator.primary_metric}")
# => Primary metric: BeIR-nfcorpus-subset-test_dot_ndcg@10
print(f"Primary metric value: {results[ir_evaluator.primary_metric]:.4f}")
# => Primary metric value: 0.3530

SparseNanoBEIREvaluator[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsenanobeirevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.evaluation.SparseNanoBEIREvaluator(_dataset\_names:list[DatasetNameType|str]|None=None,dataset\_id:str='sentence-transformers/NanoBEIR-en',mrr\_at\_k:list[int]=[10],ndcg\_at\_k:list[int]=[10],accuracy\_at\_k:list[int]=[1,3,5,10],precision\_recall\_at\_k:list[int]=[1,3,5,10],map\_at\_k:list[int]=[100],show\_progress\_bar:bool=False,batch\_size:int=32,write\_csv:bool=True,max\_active\_dims:int|None=None,score\_functions:dict[str,Callable[[Tensor,Tensor],Tensor]]|None=None,main\_score\_function:str|SimilarityFunction|None=None,aggregate\_fn:Callable[[list[float]],float]=<function mean>,aggregate\_key:str='mean',query\_prompts:str|dict[str,str]|None=None,corpus\_prompts:str|dict[str,str]|None=None,write\_predictions:bool=False_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/evaluation/SparseNanoBEIREvaluator.py#L28-L332)[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseNanoBEIREvaluator "Link to this definition")
This evaluator extends [`NanoBEIREvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.NanoBEIREvaluator "sentence_transformers.evaluation.NanoBEIREvaluator") but is specifically designed for sparse encoder models.

This class evaluates the performance of a SparseEncoder Model on the NanoBEIR collection of Information Retrieval datasets.

The NanoBEIR collection consists of downsized versions of several BEIR information-retrieval datasets, making it suitable for quickly benchmarking a model’s retrieval performance before running a full-scale BEIR evaluation. The datasets are available on Hugging Face in the Sentence Transformers [NanoBEIR collection](https://huggingface.co/collections/sentence-transformers/nanobeir-datasets), which reformats the [original collection](https://huggingface.co/collections/zeta-alpha-ai/nanobeir) from Zeta Alpha into the default [NanoBEIR-en](https://huggingface.co/datasets/sentence-transformers/NanoBEIR-en) dataset, alongside many translated versions. This evaluator will return the same metrics as the [`SparseInformationRetrievalEvaluator`](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseInformationRetrievalEvaluator "sentence_transformers.sparse_encoder.evaluation.SparseInformationRetrievalEvaluator") (i.e., MRR, nDCG, Recall@k, Sparsity, FLOPS), for each dataset and on average.

Parameters:
*   **dataset_names** (_List_ _[_ _str_ _]_) – The short names of the datasets to evaluate on (e.g., “climatefever”, “msmarco”). If not specified, all predefined NanoBEIR datasets are used. The full list of available datasets is: “climatefever”, “dbpedia”, “fever”, “fiqa2018”, “hotpotqa”, “msmarco”, “nfcorpus”, “nq”, “quoraretrieval”, “scidocs”, “arguana”, “scifact”, and “touche2020”.

*   **dataset_id** (_str_) – The HuggingFace dataset ID to load the datasets from. Defaults to “sentence-transformers/NanoBEIR-en”. The dataset must contain “corpus”, “queries”, and “qrels” subsets for each NanoBEIR dataset, stored under splits named `Nano{DatasetName}` (for example, `NanoMSMARCO` or `NanoNFCorpus`).

*   **mrr_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for MRR calculation. Defaults to [10].

*   **ndcg_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for NDCG calculation. Defaults to [10].

*   **accuracy_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for accuracy calculation. Defaults to [1, 3, 5, 10].

*   **precision_recall_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for precision and recall calculation. Defaults to [1, 3, 5, 10].

*   **map_at_k** (_List_ _[_ _int_ _]_) – A list of integers representing the values of k for MAP calculation. Defaults to [100].

*   **show_progress_bar** (_bool_) – Whether to show a progress bar during evaluation. Defaults to False.

*   **batch_size** (_int_) – The batch size for evaluation. Defaults to 32.

*   **write_csv** (_bool_) – Whether to write the evaluation results to a CSV file. Defaults to True.

*   **max_active_dims** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The maximum number of active dimensions to use. None uses the model’s current max_active_dims. Defaults to None.

*   **score_functions** (_Dict_ _[_ _str_ _,_ _Callable_ _[_ _[_ _Tensor_ _,_ _Tensor_ _]_ _,_ _Tensor_ _]_ _]_) – A dictionary mapping score function names to score functions. Defaults to {SimilarityFunction.COSINE.value: cos_sim, SimilarityFunction.DOT_PRODUCT.value: dot_score}.

*   **main_score_function** (_Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_ _,_ _optional_) – The main score function to use for evaluation. Defaults to None.

*   **aggregate_fn** (_Callable_ _[_ _[_ _list_ _[_ _float_ _]_ _]_ _,_ _float_ _]_) – The function to aggregate the scores. Defaults to np.mean.

*   **aggregate_key** (_str_) – The key to use for the aggregated score. Defaults to “mean”.

*   **query_prompts** (_str_ _|_ _dict_ _[_ _str_ _,_ _str_ _]_ _,_ _optional_) – The prompts to add to the queries. If a string, will add the same prompt to all queries. If a dict, expects that all datasets in dataset_names are keys.

*   **corpus_prompts** (_str_ _|_ _dict_ _[_ _str_ _,_ _str_ _]_ _,_ _optional_) – The prompts to add to the corpus. If a string, will add the same prompt to all corpus. If a dict, expects that all datasets in dataset_names are keys.

*   **write_predictions** (_bool_) – Whether to write the predictions to a JSONL file. Defaults to False. This can be useful for downstream evaluation as it can be used as input to the [`ReciprocalRankFusionEvaluator`](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator") that accept precomputed predictions.

Example

import logging

from sentence_transformers import SparseEncoder
from sentence_transformers.sparse_encoder.evaluation import SparseNanoBEIREvaluator

logging.basicConfig(format="%(message)s", level=logging.INFO)

# Load a model
model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

datasets = ["QuoraRetrieval", "MSMARCO"]

evaluator = SparseNanoBEIREvaluator(
    dataset_names=datasets,
    show_progress_bar=True,
    batch_size=32,
)

# Run evaluation
results = evaluator(model)
'''
Evaluating NanoQuoraRetrieval
Information Retrieval Evaluation of the model on the NanoQuoraRetrieval dataset:
Queries: 50
Corpus: 5046

Score-Function: dot
Accuracy@1: 92.00%
Accuracy@3: 96.00%
Accuracy@5: 98.00%
Accuracy@10: 100.00%
Precision@1: 92.00%
Precision@3: 40.00%
Precision@5: 24.80%
Precision@10: 13.20%
Recall@1: 79.73%
Recall@3: 92.53%
Recall@5: 94.93%
Recall@10: 98.27%
MRR@10: 0.9439
NDCG@10: 0.9339
MAP@100: 0.9070
Model Query Sparsity: Active Dimensions: 59.4, Sparsity Ratio: 0.9981
Model Corpus Sparsity: Active Dimensions: 61.9, Sparsity Ratio: 0.9980
Average FLOPS: 4.10

Information Retrieval Evaluation of the model on the NanoMSMARCO dataset:
Queries: 50
Corpus: 5043

Score-Function: dot
Accuracy@1: 48.00%
Accuracy@3: 74.00%
Accuracy@5: 76.00%
Accuracy@10: 86.00%
Precision@1: 48.00%
Precision@3: 24.67%
Precision@5: 15.20%
Precision@10: 8.60%
Recall@1: 48.00%
Recall@3: 74.00%
Recall@5: 76.00%
Recall@10: 86.00%
MRR@10: 0.6191
NDCG@10: 0.6780
MAP@100: 0.6277
Model Query Sparsity: Active Dimensions: 45.4, Sparsity Ratio: 0.9985
Model Corpus Sparsity: Active Dimensions: 122.6, Sparsity Ratio: 0.9960
Average FLOPS: 2.41

Average Queries: 50.0
Average Corpus: 5044.5
Aggregated for Score Function: dot
Accuracy@1: 70.00%
Accuracy@3: 85.00%
Accuracy@5: 87.00%
Accuracy@10: 93.00%
Precision@1: 70.00%
Recall@1: 63.87%
Precision@3: 32.33%
Recall@3: 83.27%
Precision@5: 20.00%
Recall@5: 85.47%
Precision@10: 10.90%
Recall@10: 92.13%
MRR@10: 0.7815
NDCG@10: 0.8060
MAP@100: 0.7674
Model Query Sparsity: Active Dimensions: 52.4, Sparsity Ratio: 0.9983
Model Corpus Sparsity: Active Dimensions: 92.2, Sparsity Ratio: 0.9970
Average FLOPS: 2.59
'''
# Print the results
print(f"Primary metric: {evaluator.primary_metric}")
# => Primary metric: NanoBEIR_mean_dot_ndcg@10
print(f"Primary metric value: {results[evaluator.primary_metric]:.4f}")
# => Primary metric value: 0.8060

Evaluating on custom/translated datasets:

import logging
from pprint import pprint

from sentence_transformers import SparseEncoder
from sentence_transformers.sparse_encoder.evaluation import SparseNanoBEIREvaluator

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

model = SparseEncoder("opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1")
evaluator = SparseNanoBEIREvaluator(
    dataset_names=["msmarco", "nq"],
    dataset_id="lightonai/NanoBEIR-de",
    batch_size=32,
)
results = evaluator(model)
print(results[evaluator.primary_metric])
pprint({key: value for key, value in results.items() if "ndcg@10" in key})

SparseEmbeddingSimilarityEvaluator[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparseembeddingsimilarityevaluator "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.evaluation.SparseEmbeddingSimilarityEvaluator(_sentences1:list[str]_, _sentences2:list[str]_, _scores:list[float]_, _batch\_size:int=16_, _main\_similarity:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.SimilarityFunction")|None=None_, _similarity\_fn\_names:list[Literal['cosine','euclidean','manhattan','dot']]|None=None_, _name:str=''_, _show\_progress\_bar:bool=False_, _write\_csv:bool=True_, _max\_active\_dims:int|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/evaluation/SparseEmbeddingSimilarityEvaluator.py#L22-L168)[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseEmbeddingSimilarityEvaluator "Link to this definition")
This evaluator extends [`EmbeddingSimilarityEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator") but is specifically designed for sparse encoder models.

Evaluate a model based on the similarity of the embeddings by calculating the Spearman and Pearson rank correlation in comparison to the gold standard labels. The metrics are the cosine similarity as well as euclidean and Manhattan distance The returned score is the Spearman correlation with a specified metric.

Parameters:
*   **sentences1** (_List_ _[_ _str_ _]_) – List with the first sentence in a pair.

*   **sentences2** (_List_ _[_ _str_ _]_) – List with the second sentence in a pair.

*   **scores** (_List_ _[_ _float_ _]_) – Similarity score between sentences1[i] and sentences2[i].

*   **batch_size** (_int_ _,_ _optional_) – The batch size for processing the sentences. Defaults to 16.

*   **main_similarity** (_Optional_ _[_ _Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_ _]_ _,_ _optional_) – The main similarity function to use. Can be a string (e.g. “cosine”, “dot”) or a SimilarityFunction object. Defaults to None.

*   **similarity_fn_names** (_List_ _[_ _str_ _]_ _,_ _optional_) – List of similarity function names to use. If None, the `similarity_fn_name` attribute of the model is used. Defaults to None.

*   **name** (_str_ _,_ _optional_) – The name of the evaluator. Defaults to “”.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Whether to show a progress bar during evaluation. Defaults to False.

*   **write_csv** (_bool_ _,_ _optional_) – Whether to write the evaluation results to a CSV file. Defaults to True.

*   **max_active_dims** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The maximum number of active dimensions to use. None uses the model’s current max_active_dims. Defaults to None.

Example

import logging

from datasets import load_dataset

from sentence_transformers import SparseEncoder, SimilarityFunction
from sentence_transformers.sparse_encoder.evaluation import SparseEmbeddingSimilarityEvaluator

logging.basicConfig(format="%(message)s", level=logging.INFO)

# Load a model
model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

# Load the STSB dataset (https://huggingface.co/datasets/sentence-transformers/stsb)
eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")

# Initialize the evaluator
dev_evaluator = SparseEmbeddingSimilarityEvaluator(
    sentences1=eval_dataset["sentence1"],
    sentences2=eval_dataset["sentence2"],
    scores=eval_dataset["score"],
    main_similarity=SimilarityFunction.COSINE, # even though the model is trained with dot, we need to set it to cosine for evaluation as the score in the dataset is cosine similarity
    name="sts_dev",
)
results = dev_evaluator(model)
'''
EmbeddingSimilarityEvaluator: Evaluating the model on the sts_dev dataset:
Cosine-Similarity: Pearson: 0.8429 Spearman: 0.8366
Model Sparsity: Active Dimensions: 78.3, Sparsity Ratio: 0.9974
'''
# Print the results
print(f"Primary metric: {dev_evaluator.primary_metric}")
# => Primary metric: sts_dev_spearman_cosine
print(f"Primary metric value: {results[dev_evaluator.primary_metric]:.4f}")
# => Primary metric value: 0.8366

SparseBinaryClassificationEvaluator[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsebinaryclassificationevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.evaluation.SparseBinaryClassificationEvaluator(_sentences1:list[str]_, _sentences2:list[str]_, _labels:list[int]_, _name:str=''_, _batch\_size:int=32_, _show\_progress\_bar:bool=False_, _write\_csv:bool=True_, _max\_active\_dims:int|None=None_, _similarity\_fn\_names:list[Literal['cosine','dot','euclidean','manhattan']]|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/evaluation/SparseBinaryClassificationEvaluator.py#L21-L193)[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseBinaryClassificationEvaluator "Link to this definition")
This evaluator extends [`BinaryClassificationEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.BinaryClassificationEvaluator "sentence_transformers.evaluation.BinaryClassificationEvaluator") but is specifically designed for sparse encoder models.

Evaluate a model based on the similarity of the embeddings by calculating the accuracy of identifying similar and dissimilar sentences. The metrics are the cosine similarity, dot score, Euclidean and Manhattan distance The returned score is the accuracy with a specified metric.

The results are written in a CSV. If a CSV already exists, then values are appended.

The labels need to be 0 for dissimilar pairs and 1 for similar pairs.

Parameters:
*   **sentences1** (_List_ _[_ _str_ _]_) – The first column of sentences.

*   **sentences2** (_List_ _[_ _str_ _]_) – The second column of sentences.

*   **labels** (_List_ _[_ _int_ _]_) – labels[i] is the label for the pair (sentences1[i], sentences2[i]). Must be 0 or 1.

*   **name** (_str_ _,_ _optional_) – Name for the output. Defaults to “”.

*   **batch_size** (_int_ _,_ _optional_) – Batch size used to compute embeddings. Defaults to 32.

*   **show_progress_bar** (_bool_ _,_ _optional_) – If true, prints a progress bar. Defaults to False.

*   **write_csv** (_bool_ _,_ _optional_) – Write results to a CSV file. Defaults to True.

*   **max_active_dims** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The maximum number of active dimensions to use. None uses the model’s current max_active_dims. Defaults to None.

*   **similarity_fn_names** (_Optional_ _[_ _List_ _[_ _Literal_ _[_ _"cosine"_ _,_ _"dot"_ _,_ _"euclidean"_ _,_ _"manhattan"_ _]_ _]_ _]_ _,_ _optional_) – The similarity functions to use. If not specified, defaults to the `similarity_fn_name` attribute of the model. Defaults to None.

Example

import logging

from datasets import load_dataset

from sentence_transformers import SparseEncoder
from sentence_transformers.sparse_encoder.evaluation import SparseBinaryClassificationEvaluator

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)

# Initialize the SPLADE model
model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

# Load a dataset with two text columns and a class label column (https://huggingface.co/datasets/sentence-transformers/quora-duplicates)
eval_dataset = load_dataset("sentence-transformers/quora-duplicates", "pair-class", split="train[-1000:]")

# Initialize the evaluator
binary_acc_evaluator = SparseBinaryClassificationEvaluator(
    sentences1=eval_dataset["sentence1"],
    sentences2=eval_dataset["sentence2"],
    labels=eval_dataset["label"],
    name="quora_duplicates_dev",
    show_progress_bar=True,
    similarity_fn_names=["cosine", "dot", "euclidean", "manhattan"],
)
results = binary_acc_evaluator(model)
'''
Accuracy with Cosine-Similarity: 75.00 (Threshold: 0.8668)
F1 with Cosine-Similarity: 67.22 (Threshold: 0.5974)
Precision with Cosine-Similarity: 54.18
Recall with Cosine-Similarity: 88.51
Average Precision with Cosine-Similarity: 67.81
Matthews Correlation with Cosine-Similarity: 49.56

Accuracy with Dot-Product: 76.50 (Threshold: 23.4236)
F1 with Dot-Product: 67.00 (Threshold: 19.0095)
Precision with Dot-Product: 55.93
Recall with Dot-Product: 83.54
Average Precision with Dot-Product: 65.89
Matthews Correlation with Dot-Product: 48.88

Accuracy with Euclidean-Distance: 67.70 (Threshold: -10.0041)
F1 with Euclidean-Distance: 48.60 (Threshold: -0.1876)
Precision with Euclidean-Distance: 32.13
Recall with Euclidean-Distance: 99.69
Average Precision with Euclidean-Distance: 20.52
Matthews Correlation with Euclidean-Distance: -4.59

Accuracy with Manhattan-Distance: 67.70 (Threshold: -103.0263)
F1 with Manhattan-Distance: 48.60 (Threshold: -0.8532)
Precision with Manhattan-Distance: 32.13
Recall with Manhattan-Distance: 99.69
Average Precision with Manhattan-Distance: 21.05
Matthews Correlation with Manhattan-Distance: -4.59

Model Sparsity: Active Dimensions: 61.2, Sparsity Ratio: 0.9980
'''
# Print the results
print(f"Primary metric: {binary_acc_evaluator.primary_metric}")
# => Primary metric: quora_duplicates_dev_max_ap
print(f"Primary metric value: {results[binary_acc_evaluator.primary_metric]:.4f}")
# => Primary metric value: 0.6781

SparseTripletEvaluator[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsetripletevaluator "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator(_anchors:list[str]_, _positives:list[str]_, _negatives:list[str]_, _main\_similarity\_function:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.SimilarityFunction")|None=None_, _margin:float|dict[str,float]|None=None_, _name:str=''_, _batch\_size:int=16_, _show\_progress\_bar:bool=False_, _write\_csv:bool=True_, _max\_active\_dims:int|None=None_, _similarity\_fn\_names:list[Literal['cosine','dot','euclidean','manhattan']]|None=None_, _main\_distance\_function:str|[SimilarityFunction](https://sbert.net/docs/package\_reference/sparse\_encoder/SparseEncoder.html#sentence\_transformers.SimilarityFunction "sentence\_transformers.SimilarityFunction")|None='deprecated'_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/evaluation/SparseTripletEvaluator.py#L23-L191)[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseTripletEvaluator "Link to this definition")
This evaluator extends [`TripletEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator "sentence_transformers.evaluation.TripletEvaluator") but is specifically designed for sparse encoder models.

Evaluate a model based on a triplet: (sentence, positive_example, negative_example). Checks if `similarity(sentence, positive_example) < similarity(sentence, negative_example) + margin`.

Parameters:
*   **anchors** (_List_ _[_ _str_ _]_) – Sentences to check similarity to. (e.g. a query)

*   **positives** (_List_ _[_ _str_ _]_) – List of positive sentences

*   **negatives** (_List_ _[_ _str_ _]_) – List of negative sentences

*   **main_similarity_function** (_Union_ _[_ _str_ _,_[_SimilarityFunction_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.SimilarityFunction "sentence_transformers.SimilarityFunction")_]_ _,_ _optional_) – The similarity function to use. If not specified, use cosine similarity, dot product, Euclidean, and Manhattan similarity. Defaults to None.

*   **margin** (_Union_ _[_ _float_ _,_ _Dict_ _[_ _str_ _,_ _float_ _]_ _]_ _,_ _optional_) – Margins for various similarity metrics. If a float is provided, it will be used as the margin for all similarity metrics. If a dictionary is provided, the keys should be ‘cosine’, ‘dot’, ‘manhattan’, and ‘euclidean’. The value specifies the minimum margin by which the negative sample should be further from the anchor than the positive sample. Defaults to None.

*   **name** (_str_) – Name for the output. Defaults to “”.

*   **batch_size** (_int_) – Batch size used to compute embeddings. Defaults to 16.

*   **show_progress_bar** (_bool_) – If true, prints a progress bar. Defaults to False.

*   **write_csv** (_bool_) – Write results to a CSV file. Defaults to True.

*   **max_active_dims** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The maximum number of active dimensions to use. None uses the model’s current max_active_dims. Defaults to None.

*   **similarity_fn_names** (_List_ _[_ _str_ _]_ _,_ _optional_) – List of similarity function names to evaluate. If not specified, evaluate using the `model.similarity_fn_name`. Defaults to None.

Example

import logging

from datasets import load_dataset

from sentence_transformers import SparseEncoder
from sentence_transformers.sparse_encoder.evaluation import SparseTripletEvaluator

logging.basicConfig(format="%(message)s", level=logging.INFO)

# Load a model
model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

# Load triplets from the AllNLI dataset
# The dataset contains triplets of (anchor, positive, negative) sentences
dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="dev[:1000]")

# Initialize the SparseTripletEvaluator
evaluator = SparseTripletEvaluator(
    anchors=dataset[:1000]["anchor"],
    positives=dataset[:1000]["positive"],
    negatives=dataset[:1000]["negative"],
    name="all_nli_dev",
    batch_size=32,
    show_progress_bar=True,
)

# Run the evaluation
results = evaluator(model)
'''
TripletEvaluator: Evaluating the model on the all_nli_dev dataset:
Accuracy Dot Similarity: 85.40%
Model Anchor Sparsity: Active Dimensions: 103.0, Sparsity Ratio: 0.9966
Model Positive Sparsity: Active Dimensions: 67.4, Sparsity Ratio: 0.9978
Model Negative Sparsity: Active Dimensions: 65.9, Sparsity Ratio: 0.9978
'''
# Print the results
print(f"Primary metric: {evaluator.primary_metric}")
# => Primary metric: all_nli_dev_dot_accuracy
print(f"Primary metric value: {results[evaluator.primary_metric]:.4f}")
# => Primary metric value: 0.8540

SparseRerankingEvaluator[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsererankingevaluator "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.evaluation.SparseRerankingEvaluator(_samples:list[dict[str,str|list[str]]],at\_k:int=10,name:str='',write\_csv:bool=True,similarity\_fct:~collections.abc.Callable[[~torch.Tensor,~torch.Tensor],~torch.Tensor]=<function cos\_sim>,batch\_size:int=64,show\_progress\_bar:bool=False,use\_batched\_encoding:bool=True,max\_active\_dims:int|None=None,mrr\_at\_k:int|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/evaluation/SparseRerankingEvaluator.py#L22-L212)[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseRerankingEvaluator "Link to this definition")
This evaluator extends :class:[`](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#id1)~sentence_transformers.evaluation.RerankingEvaluator’ but is specifically designed for sparse encoder models.

This class evaluates a SparseEncoder model for the task of re-ranking.

Given a query and a list of documents, it computes the score [query, doc_i] for all possible documents and sorts them in decreasing order. Then, [MRR@10](mailto:MRR%4010), [NDCG@10](mailto:NDCG%4010) and MAP is compute to measure the quality of the ranking.

Parameters:
*   **samples** (_list_) –

A list of dictionaries, where each dictionary represents a sample and has the following keys:

    *   ’query’: The search query.

    *   ’positive’: A list of positive (relevant) documents.

    *   ’negative’: A list of negative (irrelevant) documents.

*   **at_k** (_int_ _,_ _optional_) – Only consider the top k most similar documents to each query for the evaluation. Defaults to 10.

*   **name** (_str_ _,_ _optional_) – Name of the evaluator. Defaults to “”.

*   **write_csv** (_bool_ _,_ _optional_) – Write results to CSV file. Defaults to True.

*   **similarity_fct** (_Callable_ _[_ _[_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_,_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_]_ _,_[_torch.Tensor_](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor "(in PyTorch v2.10)")_]_ _,_ _optional_) – Similarity function between sentence embeddings. By default, cosine similarity. Defaults to cos_sim.

*   **batch_size** (_int_ _,_ _optional_) – Batch size to compute sentence embeddings. Defaults to 64.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Show progress bar when computing embeddings. Defaults to False.

*   **use_batched_encoding** (_bool_ _,_ _optional_) – Whether or not to encode queries and documents in batches for greater speed, or 1-by-1 to save memory. Defaults to True.

*   **max_active_dims** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The maximum number of active dimensions to use. None uses the model’s current max_active_dims. Defaults to None.

*   **mrr_at_k** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – Deprecated parameter. Please use at_k instead. Defaults to None.

Example

import logging

from datasets import load_dataset

from sentence_transformers import SparseEncoder
from sentence_transformers.sparse_encoder.evaluation import SparseRerankingEvaluator

logging.basicConfig(format="%(message)s", level=logging.INFO)

# Load a model
model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

# Load a dataset with queries, positives, and negatives
eval_dataset = load_dataset("microsoft/ms_marco", "v1.1", split="validation").select(range(1000))

samples = [
    {
        "query": sample["query"],
        "positive": [
            text
            for is_selected, text in zip(sample["passages"]["is_selected"], sample["passages"]["passage_text"])
            if is_selected
        ],
        "negative": [
            text
            for is_selected, text in zip(sample["passages"]["is_selected"], sample["passages"]["passage_text"])
            if not is_selected
        ],
    }
    for sample in eval_dataset
]

# Now evaluate using only the documents from the 1000 samples
reranking_evaluator = SparseRerankingEvaluator(
    samples=samples,
    name="ms-marco-dev-small",
    show_progress_bar=True,
    batch_size=32,
)

results = reranking_evaluator(model)
'''
RerankingEvaluator: Evaluating the model on the ms-marco-dev-small dataset:
Queries: 967 Positives: Min 1.0, Mean 1.1, Max 3.0 Negatives: Min 1.0, Mean 7.1, Max 9.0
MAP: 53.41
MRR@10: 54.14
NDCG@10: 65.06
Model Query Sparsity: Active Dimensions: 42.2, Sparsity Ratio: 0.9986
Model Corpus Sparsity: Active Dimensions: 126.5, Sparsity Ratio: 0.9959
'''
# Print the results
print(f"Primary metric: {reranking_evaluator.primary_metric}")
# => Primary metric: ms-marco-dev-small_ndcg@10
print(f"Primary metric value: {results[reranking_evaluator.primary_metric]:.4f}")
# => Primary metric value: 0.6506

SparseTranslationEvaluator[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsetranslationevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.evaluation.SparseTranslationEvaluator(_source\_sentences:list[str]_, _target\_sentences:list[str]_, _show\_progress\_bar:bool=False_, _batch\_size:int=16_, _name:str=''_, _print\_wrong\_matches:bool=False_, _write\_csv:bool=True_, _max\_active\_dims:int|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/evaluation/SparseTranslationEvaluator.py#L23-L158)[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseTranslationEvaluator "Link to this definition")
This evaluator extends [`TranslationEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TranslationEvaluator "sentence_transformers.evaluation.TranslationEvaluator") but is specifically designed for sparse encoder models.

Given two sets of sentences in different languages, e.g. (en_1, en_2, en_3…) and (fr_1, fr_2, fr_3, …), and assuming that fr_i is the translation of en_i. Checks if vec(en_i) has the highest similarity to vec(fr_i). Computes the accuracy in both directions

The labels need to indicate the similarity between the sentences.

Parameters:
*   **source_sentences** (_List_ _[_ _str_ _]_) – List of sentences in the source language.

*   **target_sentences** (_List_ _[_ _str_ _]_) – List of sentences in the target language.

*   **show_progress_bar** (_bool_) – Whether to show a progress bar when computing embeddings. Defaults to False.

*   **batch_size** (_int_) – The batch size to compute sentence embeddings. Defaults to 16.

*   **name** (_str_) – The name of the evaluator. Defaults to an empty string.

*   **print_wrong_matches** (_bool_) – Whether to print incorrect matches. Defaults to False.

*   **write_csv** (_bool_) – Whether to write the evaluation results to a CSV file. Defaults to True.

*   **max_active_dims** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The maximum number of active dimensions to use. None uses the model’s current max_active_dims. Defaults to None.

Example

import logging

from datasets import load_dataset

from sentence_transformers import SparseEncoder
from sentence_transformers.sparse_encoder.evaluation import SparseTranslationEvaluator

logging.basicConfig(format="%(message)s", level=logging.INFO)

# Load a model, not mutilingual but hope to see some on the hub soon
model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

# Load a parallel sentences dataset
dataset = load_dataset("sentence-transformers/parallel-sentences-news-commentary", "en-nl", split="train[:1000]")

# Initialize the TranslationEvaluator using the same texts from two languages
translation_evaluator = SparseTranslationEvaluator(
    source_sentences=dataset["english"],
    target_sentences=dataset["non_english"],
    name="news-commentary-en-nl",
)
results = translation_evaluator(model)
'''
Evaluating translation matching Accuracy of the model on the news-commentary-en-nl dataset:
Accuracy src2trg: 41.40
Accuracy trg2src: 47.60
Model Sparsity: Active Dimensions: 112.3, Sparsity Ratio: 0.9963
'''
# Print the results
print(f"Primary metric: {translation_evaluator.primary_metric}")
# => Primary metric: news-commentary-en-nl_mean_accuracy
print(f"Primary metric value: {results[translation_evaluator.primary_metric]:.4f}")
# => Primary metric value: 0.4450

SparseMSEEvaluator[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sparsemseevaluator "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.evaluation.SparseMSEEvaluator(_source\_sentences:list[str]_, _target\_sentences:list[str]_, _teacher\_model=None_, _show\_progress\_bar:bool=False_, _batch\_size:int=32_, _name:str=''_, _write\_csv:bool=True_, _max\_active\_dims:int|None=None_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/evaluation/SparseMSEEvaluator.py#L20-L170)[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.SparseMSEEvaluator "Link to this definition")
This evaluator extends [`MSEEvaluator`](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.MSEEvaluator "sentence_transformers.evaluation.MSEEvaluator") but is specifically designed for sparse encoder models.

Note that this evaluator doesn’t take benefit of the sparse tensor torch representation yet, so memory issues may occur.

Computes the mean squared error (x100) between the computed sentence embedding and some target sentence embedding.

The MSE is computed between `||teacher.encode(source_sentences) - student.encode(target_sentences)||`.

For multilingual knowledge distillation ([https://huggingface.co/papers/2004.09813](https://huggingface.co/papers/2004.09813)), source_sentences are in English and target_sentences are in a different language like German, Chinese, Spanish…

Parameters:
*   **source_sentences** (_List_ _[_ _str_ _]_) – Source sentences to embed with the teacher model.

*   **target_sentences** (_List_ _[_ _str_ _]_) – Target sentences to embed with the student model.

*   **teacher_model** ([_SparseEncoder_](https://sbert.net/docs/package_reference/sparse_encoder/SparseEncoder.html#sentence_transformers.sparse_encoder.SparseEncoder "sentence_transformers.sparse_encoder.SparseEncoder")_,_ _optional_) – The teacher model to compute the source sentence embeddings.

*   **show_progress_bar** (_bool_ _,_ _optional_) – Show progress bar when computing embeddings. Defaults to False.

*   **batch_size** (_int_ _,_ _optional_) – Batch size to compute sentence embeddings. Defaults to 32.

*   **name** (_str_ _,_ _optional_) – Name of the evaluator. Defaults to “”.

*   **write_csv** (_bool_ _,_ _optional_) – Write results to CSV file. Defaults to True.

*   **max_active_dims** (_Optional_ _[_ _int_ _]_ _,_ _optional_) – The maximum number of active dimensions to use. None uses the model’s current max_active_dims. Defaults to None.

Example

import logging

from datasets import load_dataset

from sentence_transformers import SparseEncoder
from sentence_transformers.sparse_encoder.evaluation import SparseMSEEvaluator

logging.basicConfig(format="%(message)s", level=logging.INFO)

# Load a model
student_model = SparseEncoder("prithivida/Splade_PP_en_v1")
teacher_model = SparseEncoder("naver/splade-cocondenser-ensembledistil")

# Load any dataset with some texts
dataset = load_dataset("sentence-transformers/stsb", split="validation")
sentences = dataset["sentence1"] + dataset["sentence2"]

# Given queries, a corpus and a mapping with relevant documents, the SparseMSEEvaluator computes different MSE metrics.
mse_evaluator = SparseMSEEvaluator(
    source_sentences=sentences,
    target_sentences=sentences,
    teacher_model=teacher_model,
    name="stsb-dev",
)
results = mse_evaluator(student_model)
'''
MSE evaluation (lower = better) on the stsb-dev dataset:
MSE (*100): 0.034905
Model Sparsity: Active Dimensions: 54.6, Sparsity Ratio: 0.9982
'''
# Print the results
print(f"Primary metric: {mse_evaluator.primary_metric}")
# => Primary metric: stsb-dev_negative_mse
print(f"Primary metric value: {results[mse_evaluator.primary_metric]:.4f}")
# => Primary metric value: -0.0349

ReciprocalRankFusionEvaluator[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#reciprocalrankfusionevaluator "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator(_dense\_samples:list[dict[str,str|list[str]]]_, _sparse\_samples:list[dict[str,str|list[str]]]_, _at\_k:int=10_, _rrf\_k:int=60_, _name:str=''_, _batch\_size:int=32_, _show\_progress\_bar:bool=False_, _write\_csv:bool=True_, _write\_predictions:bool=False_)[[source]](https://github.com/huggingface/sentence-transformers/blob/main/sentence_transformers/sparse_encoder/evaluation/ReciprocalRankFusionEvaluator.py#L17-L351)[](https://sbert.net/docs/package_reference/sparse_encoder/evaluation.html#sentence_transformers.sparse_encoder.evaluation.ReciprocalRankFusionEvaluator "Link to this definition")
This class evaluates a hybrid search approach using Reciprocal Rank Fusion (RRF).

Given a query and two separate ranked lists of documents from different retrievers (e.g., sparse and dense), it combines them using the RRF formula and computes metrics like MRR@k, NDCG@k, and MAP.

Parameters:
*   **dense_samples** (_list_) – A list of dictionaries for dense retriever results. Each dictionary should have: - ‘query_id’: The ID of the query - ‘query’: The search query text - ‘positive’: A list of relevant documents - ‘documents’: A list of all documents (including positives)

*   **sparse_samples** (_list_) – A list of dictionaries for sparse retriever results with the same format

*   **at_k** (_int_) – Only consider the top k documents for evaluation. Defaults to 10.

*   **rrf_k** (_int_) – Constant in the RRF formula. Defaults to 60.

*   **name** (_str_) – Name of the evaluator. Defaults to “”.

*   **batch_size** (_int_) – Batch size used for the evaluation. Defaults to 32.

*   **show_progress_bar** (_bool_) – Output a progress bar. Defaults to False.

*   **write_csv** (_bool_) – Write results to CSV file. Defaults to True.

*   **write_predictions** (_bool_) – Whether to write the fused predictions to a JSONL file. Defaults to False.

Example

See an example usage [Applications > Retrieve & Rerank](https://sbert.net/examples/sparse_encoder/applications/retrieve_rerank/README.html)
