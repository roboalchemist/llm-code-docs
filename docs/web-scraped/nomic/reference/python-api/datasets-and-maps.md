# Nomic Documentation

Source: https://docs.nomic.ai/reference/python-api/datasets-and-maps

This guide walks you through uploading data and creating data maps using the Atlas Python SDK.

To connect an external dataset with Atlas, read our Integrations.

Read our Atlas Dataset docs to learn how to prepare your own data that will work with Atlas.

## Setup​

Make sure you have the nomic package installed:

```
nomic
```

```
pip install nomic
```

Then login with your API key at a terminal / command line:

```
nomic login nk-...
```

## Using Atlas Datasets​

When you create an Atlas Dataset, you

- set up an empty initial dataset
set up an empty initial dataset

- add data to the dataset
add data to the dataset

- create an Atlas Map from the dataset
create an Atlas Map from the dataset

with users typically repeating steps 2 and 3 as they collect more data and make their maps reflects the most complete picture of their data.

Your dataset can be downloaded like this:

```
from nomic import AtlasDatasetdataset = AtlasDataset('my-dataset')atlas_map = dataset.maps[0]df = atlas_map.data.df
```

## Upload Text​

For text data, use:

```
from nomic import AtlasDatasetdataset = AtlasDataset(your_dataset_name)# data is a DataFrame or list of dictionariesdataset.add_data(your_data) # indexed_field contains text to embedatlas_map = dataset.create_index(    indexed_field=your_text_field)
```

For example, this will upload text to Atlas and embed it with Nomic Embed Text, and create a map of the points in the dataset clustered by the content of the text.

```
from nomic import AtlasDatasetimport pandas as pddataset = AtlasDataset("text-dataset-airline-reviews")df = pd.read_csv('https://docs.nomic.ai/singapore_airlines_reviews.csv')dataset.add_data(df)atlas_map = dataset.create_index(indexed_field='text')
```

## Upload Images​

For image data, use:

```
from nomic import AtlasDatasetdataset = AtlasDataset(your_dataset_name)# blobs is a list of URLS, filepaths, bytes, or PIL imagesdataset.add_data(    blobs=your_images,     data=your_metadata # Optional metadata for each image)# indexed_field is automatically inferred as your image blobsatlas_map = dataset.create_index()
```

For example, this will create a map of the CIFAR10 dataset. Each image will be embedded using Nomic Embed Vision.

```
from nomic import AtlasDatasetfrom datasets import load_datasetdataset = AtlasDataset("image-dataset-CIFAR10")cifar = load_dataset('cifar10', split="train")images = cifar["img"]metadata = [{"label": label} for label in cifar["label"]]dataset.add_data(blobs=images, data=metadata)atlas_map = dataset.create_index()
```

## Upload Embeddings​

For pre-computed embeddings, use:

```
from nomic import AtlasDatasetdataset = AtlasDataset(your_dataset_name) # embeddings is a np.array of shape (n_embeddings, embedding_dim)dataset.add_data(    embeddings=your_embeddings,     data=your_metadata # Optional metadata for each embedding)atlas_map = dataset.create_index()
```

This example will create a map of the same data we used to create a map of text, except instead of uploading text to Atlas and having Atlas generate the embeddings, we will first generate the embeddings ourselves in Python and then upload those embedding vectors directly.

We will use NomicTopicOptions to configure topic labels for our embeddings dataset. Topics are generated automatically when you create a text dataset, but when you create an embeddings dataset you need to specify which features to use for map topic labels. Learn about how to fetch your topics here.

```
NomicTopicOptions
```

```
from nomic import AtlasDataset, embedfrom nomic.data_inference import NomicTopicOptionsimport pandas as pddataset = AtlasDataset('embeddings-dataset-airline-reviews')df = pd.read_csv('https://docs.nomic.ai/singapore_airlines_reviews.csv')embeddings = embed.text(    texts=df.text.values,    model='nomic-embed-text-v1.5',)['embeddings']dataset.add_data(df, embeddings=embeddings)atlas_map = dataset.create_index(    topic_model=NomicTopicOptions(        build_topic_model=True,         topic_label_field='text'    ))
```

### Customizing the Embedding Model​

You can choose one of the models available in Atlas to generate text and image embeddings.

You can upload any embedding vectors from any embedding model to Atlas. Features like our vector search API are available as long as you use the same embedding model for query and document embeddings.

## Customizing the Projection​

By default, Atlas uses:

- UMAP for datasets with fewer than 50,000 points
- Nomic Project for datasets with 50,000 or more points
You can explicitly specify which projection algorithm to use and configure its parameters:

```
from nomic import AtlasDatasetfrom nomic.data_inference import ProjectionOptionsimport pandas as pddataset = AtlasDataset("airline-reviews-custom-projection")# Load the reviews dataframedf = pd.read_csv('https://docs.nomic.ai/singapore_airlines_reviews.csv')dataset.add_data(df)atlas_map = dataset.create_index(    indexed_field='text',     projection=ProjectionOptions(        model="umap",        n_neighbors=5,         min_dist=0.05,        n_epochs=30    ))
```

## Upload in Batches​

If you have a large dataset of images, you can additionally successively add images to the dataset using the add_data method.

This example creates a map of the Imagenette dataset.

```
from nomic import atlasfrom datasets import load_datasetfrom tqdm import tqdmid2label = {   "0": "tench",   "1": "English springer",   "2": "cassette player",   "3": "chain saw",   "4": "church",   "5": "French horn",   "6": "garbage truck",   "7": "gas pump",   "8": "golf ball",   "9": "parachute"}image_dataset = load_dataset('frgfm/imagenette', '160px')['train'].shuffle(seed=42)images = image_dataset["image"]labels = image_dataset["label"]metadata = [{"label": id2label[str(label)]} for label in tqdm(labels, desc="Creating metadata")]dataset = AtlasDataset('image-dataset-imagenette10k')for i, record in enumerate(metadata):    metadata[i]["id"] = ifor i in range(0, len(images), 1000):    dataset.add_data(blobs=images[i:i+1000],                   data=metadata[i:i+1000],                   )atlas_map = dataset.create_index(    topic_model={"build_topic_model": False},     embedding_model="nomic-embed-vision-v1.5")
```

## API Reference​

### AtlasDataset​

AtlasDataset is the main class for creating and managing datasets in Atlas.

```
class AtlasDataset(AtlasClass)
```

### __init__​

```
def __init__(identifier: Optional[str] = None,             description: Optional[str] = "A description for your map.",             unique_id_field: Optional[str] = None,             is_public: bool = True,             dataset_id=None,             organization_name=None)
```

Creates or loads an AtlasDataset.
AtlasDataset's store data (text, embeddings, etc) that you can organize by building indices.
If the organization already contains a dataset with this name, it will be returned instead.

Parameters:

- identifier - The dataset identifier in the form dataset or organization/dataset. If no organization is passed, the organization tied to the API key you logged in to Nomic with will be used.
```
dataset
```

```
organization/dataset
```

- description - A description for the dataset.
- unique_id_field - A field that uniquely identifies each data point.
- is_public - Should this dataset be publicly accessible for viewing (read only). If False, only members of your Nomic organization can view.
- dataset_id - An alternative way to load a dataset is by passing the dataset_id directly. This only works if a dataset exists.
### delete​

```
def delete()
```

Deletes an atlas dataset with all associated metadata.

### id​

```
@propertydef id() -> str
```

The ID of the dataset.

### id_field​

```
@propertydef id_field() -> str
```

The unique_id_field of the dataset.

### total_datums​

```
@propertydef total_datums() -> int
```

The total number of data points in the dataset.

### name​

```
@propertydef name() -> str
```

The customizable name of the dataset.

### slug​

```
@propertydef slug() -> str
```

The URL-safe identifier for this dataset.

### identifier​

```
@propertydef identifier() -> str
```

The Atlas globally unique, URL-safe identifier for this dataset

### is_accepting_data​

```
@propertydef is_accepting_data() -> bool
```

Checks if the dataset can accept data. Datasets cannot accept data when they are being indexed.

Returns:

True if dataset is unlocked for data additions, false otherwise.

### wait_for_dataset_lock​

```
@contextmanagerdef wait_for_dataset_lock()
```

Blocks thread execution until dataset is in a state where it can ingest data.

### get_map​

```
def get_map(name: Optional[str] = None,            atlas_index_id: Optional[str] = None,            projection_id: Optional[str] = None) -> AtlasProjection
```

Retrieves a map.

Arguments:

- name - The name of your map. This defaults to your dataset name but can be different if you build multiple maps in your dataset.
```
name
```

- atlas_index_id - If specified, will only return a map if there is one built under the index with the id atlas_index_id.
```
atlas_index_id
```

- projection_id - If projection_id is specified, will only return a map if there is one built under the index with id projection_id.
```
projection_id
```

Returns:

The map or a ValueError.

### create_index​

```
def create_index(    name: Optional[str] = None,    indexed_field: Optional[str] = None,    modality: Optional[str] = None,    projection: Union[Dict, ProjectionOptions, None] = None,    topic_model: Union[bool, Dict, NomicTopicOptions] = True,    duplicate_detection: Union[bool, Dict, NomicDuplicatesOptions] = True,    embedding_model: Optional[Union[str, Dict, NomicEmbedOptions]] = None,    reuse_embeddings_from_index: Optional[str] = None) -> Optional[AtlasProjection]
```

Creates an index in the specified dataset.

Arguments:

- name - The name of the index and the map.
```
name
```

- indexed_field - For text datasets, name the data field corresponding to the text to be mapped.
```
indexed_field
```

- reuse_embeddings_from_index - the name of the index to reuse embeddings from.
```
reuse_embeddings_from_index
```

- modality - The data modality of this index. Currently, Atlas supports either text, image, or embedding indices.
```
modality
```

```
text
```

```
image
```

```
embedding
```

- projection - Options for configuring the 2D projection algorithm or None to let cloud decide
```
projection
```

- topic_model - Options for configuring the topic model
```
topic_model
```

- duplicate_detection - Options for configuring semantic duplicate detection
```
duplicate_detection
```

- embedding_model - Options for configuring the embedding model
```
embedding_model
```

Returns:

The projection this index has built.

### get_data​

```
def get_data(ids: List[str]) -> List[Dict]
```

Retrieve the contents of the data given ids.

Arguments:

- ids - a list of datum ids
```
ids
```

Returns:

A list of dictionaries corresponding to the data.

### delete_data​

```
def delete_data(ids: List[str]) -> bool
```

Deletes the specified datapoints from the dataset.

.. deprecated:: 3.4.0

Arguments:

- ids - A list of data ids to delete
```
ids
```

Returns:

True if data deleted successfully.

### add_data​

```
def add_data(data=Union[DataFrame, List[Dict], pa.Table],             embeddings: Optional[np.ndarray] = None,             blobs: Optional[List[Union[str, bytes, Image.Image]]] = None,             pbar=None)
```

Adds data of varying modality to an Atlas dataset.

Arguments:

- data - A pandas DataFrame, list of dictionaries, or pyarrow Table matching the dataset schema.
```
data
```

- embeddings - A numpy array of embeddings: each row corresponds to a row in the table. Use if you already have embeddings for your datapoints.
```
embeddings
```

- blobs - A list of image paths, bytes, or PIL Images. Use if you want to create an AtlasDataset using image embeddings over your images. Note: Blobs are stored locally only.
```
blobs
```

- pbar - (Optional). A tqdm progress bar to update.
```
pbar
```

### update_maps​

```
def update_maps(data: List[Dict],                embeddings: Optional[np.ndarray] = None,                num_workers: int = 10)
```

Utility method to update a project's maps by adding the given data.

.. deprecated:: 3.3.1

Arguments:

- data - An [N,] element list of dictionaries containing metadata for each embedding.
```
data
```

- embeddings - An [N, d] matrix of embeddings for updating embedding dataset. Leave as None to update text dataset.
```
embeddings
```

- shard_size - Data is uploaded in parallel by many threads. Adjust the number of datums to upload by each worker.
```
shard_size
```

- num_workers - The number of workers to use when sending data.
```
num_workers
```

### update_indices​

```
def update_indices(rebuild_topic_models: bool = False)
```

Rebuilds all maps in a dataset with the latest state dataset data state. Maps will not be rebuilt to
reflect the additions, deletions or updates you have made to your data until this method is called.

.. deprecated:: 3.3.1

Arguments:

- rebuild_topic_models - (Default False) - If true, will create new topic models when updating these indices.
```
rebuild_topic_models
```

### ProjectionOptions​

ProjectionOptions is the main class for customizing the projection of a dataset in Atlas.

```
class ProjectionOptions(BaseModel)
```

Generic options for 2D Dimensionality Reduction

Arguments:

- model - The projection model to use.
```
model
```

- n_neighbors - The number of neighbors to use for the projection algorithm.
```
n_neighbors
```

- n_epochs - How many dataset passes to train the projection model.
```
n_epochs
```

- min_dist - Controls how tightly points are packed together.
```
min_dist
```

- spread - Nomic Project specific: Determines how tight together points appear.
```
spread
```

- local_neighborhood_size - Nomic Project v2 specific: Controls the local neighborhood size.
```
local_neighborhood_size
```

- rho - Nomic Project v2 specific: Controls the spread in local structure.
```
rho
```

### NomicTopicOptions​

NomicTopicOptions is the main class for customizing the topic model of a dataset in Atlas.

```
class NomicTopicOptions(BaseModel)
```

Options for Nomic Topic Model

Arguments:

- build_topic_model - If True, builds a topic model over your dataset's embeddings.
```
build_topic_model
```

- topic_label_field - The dataset column (usually the column you embedded) that Atlas will use to assign a human-readable description to each topic.
```
topic_label_field
```

### NomicDuplicatesOptions​

NomicDuplicatesOptions is the main class for customizing duplicate detection in Atlas.

```
class NomicDuplicatesOptions(BaseModel)
```

Options for Duplicate Detection

Arguments:

- tag_duplicates - Should duplicate detection run over your datasets embeddings?
```
tag_duplicates
```

- duplicate_cutoff - A hyperparameter of duplicate detection, smaller values capture more exact duplicates.
```
duplicate_cutoff
```

### map_data​

An additional helper function atlas.map_data exists to create a dataset and map in one step.

```
atlas.map_data
```

```
def map_data(    data: Optional[Union[DataFrame, List[Dict], Table]] = None,    blobs: Optional[List[Union[str, bytes, Image.Image]]] = None,    embeddings: Optional[np.ndarray] = None,    identifier: Optional[str] = None,    description: str = "",    id_field: Optional[str] = None,    is_public: bool = True,    indexed_field: Optional[str] = None,    projection: Optional[Union[Dict, ProjectionOptions]] = None,    topic_model: Union[bool, Dict, NomicTopicOptions] = True,    duplicate_detection: Union[bool, Dict, NomicDuplicatesOptions] = True,    embedding_model: Optional[Union[str, Dict, NomicEmbedOptions]] = None) -> AtlasDataset
```

Arguments:

- data: An ordered collection of the datapoints you are structuring. Can be a list of dictionaries, Pandas Dataframe or PyArrow Table.
```
data
```

- blobs: A list of image paths, bytes, or PIL images to add to your image dataset that are stored locally.
```
blobs
```

- embeddings: An [N,d] numpy array containing the N embeddings to add.
```
embeddings
```

- identifier: A name for your dataset that is used to generate the dataset identifier. A unique name will be chosen if not supplied.
```
identifier
```

- description: The description of your dataset
```
description
```

- id_field: Specify a field that uniquely identifies each datapoint. This field can be up 36 characters in length.
```
id_field
```

- is_public: Should the dataset be accessible outside your Nomic Atlas organization.
```
is_public
```

- indexed_field: The text field from the dataset that will be used to create embeddings, which determines the layout of the data map in Atlas. Required for text data but won't have an impact if uploading embeddings or image blobs.
```
indexed_field
```

- projection: Options for configuring the 2D projection algorithm.
```
projection
```

- topic_model: Options to adjust Nomic Topic - the topic model organizing your dataset.
```
topic_model
```

- duplicate_detection: Options to adjust Nomic Duplicates - the duplicate detection algorithm.
```
duplicate_detection
```

- embedding_model: Options to adjust the embedding model used to embed your dataset.
```
embedding_model
```

- Setup
- Using Atlas Datasets
- Upload Text
- Upload Images
- Upload Embeddings
- Customizing the Projection
- Upload in Batches
- API Reference
