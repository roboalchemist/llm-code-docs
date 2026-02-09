# Source: https://upstash.com/docs/vector/features/similarityfunctions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vector Similarity Functions

When creating a vector index in Upstash Vector, you have the flexibility to choose from different vector similarity functions.
Each function yields distinct query results, catering to specific use cases. Here are the three supported similarity functions:

<Note>
  The score returned from query requests is a normalized value between 0 and 1,
  where 1 indicates the highest similarity and 0 the lowest regardless of the
  similarity function used.
</Note>

#### Cosine Similarity

Cosine similarity measures the cosine of the angle between two vectors. It is particularly useful when the magnitude of the vectors is not essential, and the focus is on the orientation.

**Use Cases:**

* **Natural Language Processing (NLP):** Ideal for comparing document embeddings or word vectors, as it captures semantic similarity irrespective of vector magnitude.
* **Recommendation Systems:** Effective in recommending items based on user preferences or content similarities.

**Score calculation:**
` (1 + cosine_similarity(v1, v2)) / 2;`

<Frame>
  <img className="block h-32 dark:hidden" src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity.svg?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=8cf075d97fdf99a8e2c8403e6c543fe2" data-og-width="264" width="264" data-og-height="39" height="39" data-path="img/vector/cosine_similarity.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity.svg?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=fc9c55f0c2ef40319c067f0c0140e763 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity.svg?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=b9ea803a48a5292e96c7e724369e841a 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity.svg?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=ac427776c3faa8f2f2810aa7d7525220 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity.svg?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=0a599eb292d63b7d2e11f76be7ce13d8 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity.svg?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=404858ef18bb054d8738a7a76eccc8cd 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity.svg?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=c7cad49ae65f9a5edcc84a666dbd04da 2500w" />

  <img className="hidden h-32 dark:block" src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity_dark.svg?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=23f03f96f01b2d805ec8f6fd58030379" data-og-width="264" width="264" data-og-height="39" height="39" data-path="img/vector/cosine_similarity_dark.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity_dark.svg?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=a15381d917323dc84b0624b65c012d51 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity_dark.svg?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=8af75547873d319b3b1f3981d4ecfa24 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity_dark.svg?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=4e2d899566e38cbcfd7ac9f9e556be9a 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity_dark.svg?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=a9d2bf461b2432bb7f5d86a47e0ac61a 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity_dark.svg?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=6212d67189ad29dd726b8b04f282883b 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/cosine_similarity_dark.svg?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=749c46c7c0d8f80f2e4ba1442019972c 2500w" />
</Frame>

#### Euclidean Distance

Euclidean distance calculates the straight-line distance between two vectors in a multi-dimensional space. It is well-suited for scenarios where the magnitude of vectors is crucial, providing a measure of their spatial separation.

**Use Cases:**

* **Computer Vision:** Useful in image processing tasks, such as image recognition or object detection, where the spatial arrangement of features is significant.
* **Anomaly Detection:** Valuable for detecting anomalies in datasets, as it considers both the direction and magnitude of differences between vectors.

**Score calculation:**
`1 / (1 + squared_distance(v1, v2))`

<Frame>
  <img className="block h-32 dark:hidden" src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance.svg?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=782afbe41e09f96b97b241cae539e398" data-og-width="248" width="248" data-og-height="52" height="52" data-path="img/vector/squared_distance.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance.svg?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=090f5f6527896ecc0f23798cdfeaba62 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance.svg?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=98d871d3ce08641a13143d3dd1a9233a 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance.svg?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=c6dba07d3d3ab3eda1c04ee9455764e0 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance.svg?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=c520f8847b53f4710e4b920ca34bebe7 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance.svg?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=db74ae03fb53ff3515a79ca3b0c7b4c1 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance.svg?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=daadb06cb259ef8acba628d02988a5c4 2500w" />

  <img className="hidden h-32 dark:block" src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance_dark.svg?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=f540c058c1caee45ea45d79f759acb95" data-og-width="248" width="248" data-og-height="52" height="52" data-path="img/vector/squared_distance_dark.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance_dark.svg?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=545ef97a82e1c287792c3505e42906a3 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance_dark.svg?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=8ce578734f1ca31eb5790f399380d98a 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance_dark.svg?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=b3a09be6a9a328f7c1fd6378d9a67754 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance_dark.svg?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=0b2f49ba96a5713ac1fda54fe6baa221 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance_dark.svg?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=82b2ff2edff62b041376d303cbb34e79 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/squared_distance_dark.svg?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=c3f1014519582c08b34443aebfc72c59 2500w" />
</Frame>

#### Dot Product

The dot product measures the similarity by multiplying the corresponding components of two vectors and summing the results. It provides a measure of alignment between vectors.
Note that to use dot product, the vectors needs to be normalized to be of unit length.

**Use Cases:**

* **Machine Learning Models:** Commonly used in machine learning for tasks like sentiment analysis or classification, where feature alignment is critical.
* **Collaborative Filtering:** Effective in collaborative filtering scenarios, such as recommending items based on user behavior or preferences.

**Score calculation:**
` (1 + dot_product(v1, v2)) / 2`

<Frame>
  <img className="block h-32 dark:hidden" src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product.svg?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=3653225a6b17f76ae995316f8fa414d1" data-og-width="172" width="172" data-og-height="52" height="52" data-path="img/vector/dot_product.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product.svg?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=d44c8bca574c139b1fa58ca65df5da70 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product.svg?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=f18b611ba2a8663bb24688fe35fabbd4 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product.svg?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=a718830873df76c2e7f0de7af31e68d0 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product.svg?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=2ba62dfa3f53beabe2dc123263f7c7c4 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product.svg?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=4e0e51eab3ec519c57071129972f5bab 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product.svg?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=8a90dee80fe1a3712eb3d5f13cb984ba 2500w" />

  <img className="hidden h-32 dark:block" src="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product_dark.svg?fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=6f5375475124b8c2ffe6db5c1052d0f8" data-og-width="172" width="172" data-og-height="52" height="52" data-path="img/vector/dot_product_dark.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product_dark.svg?w=280&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=3cfe09c3f8b784ef820f79f8f2da27b0 280w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product_dark.svg?w=560&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=848249d0f130138b27e01f4fb92306d2 560w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product_dark.svg?w=840&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=9cd18d2d67215e24fc08843b482461ee 840w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product_dark.svg?w=1100&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=c28f0db887d2b9e34e915c3fee0ad2d8 1100w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product_dark.svg?w=1650&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=1c9c29c2098e9a5c0315d7be64b72130 1650w, https://mintcdn.com/upstash/EFJsv57gEAWfBXNv/img/vector/dot_product_dark.svg?w=2500&fit=max&auto=format&n=EFJsv57gEAWfBXNv&q=85&s=2cc637a916fedaf4bafc156d023f4d11 2500w" />
</Frame>
