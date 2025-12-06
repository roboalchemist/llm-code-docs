# Nomic Documentation

Source: https://docs.nomic.ai/reference/python-api/map-resources

Atlas generates a variety of useful resources from your data, such as embeddings, 2D projections, and topic labels, which you can use for analysis and integration into your applications.

## Dataset​

Your Atlas Dataset is the collection of data you upload to Atlas, from which all other resources are generated.

You can access the dataset corresponding to an Atlas Map with atlas_map.data.

```
atlas_map.data
```

```
from nomic import AtlasDatasetdataset = AtlasDataset('my-dataset')atlas_map = dataset.maps[0]df = atlas_map.data.df # use atlas_map.data.tb to load as an Arrow table
```

### AtlasMapData API Reference​

```
class AtlasMapData()
```

Atlas Map Data (Metadata) State. This is how you can access text and other associated metadata columns
you uploaded with your project.

### df​

```
@propertydef df() -> pd.DataFrame
```

A pandas DataFrame associating each datapoint on your map to their metadata.
Converting to pandas DataFrame may materialize a large amount of data into memory.

### tb​

```
@propertydef tb() -> pa.Table
```

Pyarrow table associating each datapoint on the map to their metadata columns.
This table is memmapped from the underlying files and is the most efficient way to
access metadata information.

## Embeddings​

Access your datasets embeddings with atlas_map.embeddings.

```
atlas_map.embeddings
```

atlas_map.embeddings.latent contains the high-dimensional embeddings produced by a Nomic Embedding Model.

```
atlas_map.embeddings.latent
```

atlas_map.embeddings.projected contains the 2D reduced version. These are the positions you see on your Atlas Map in the web browser.

```
atlas_map.embeddings.projected
```

This example shows how to access high- and low-dimensional embeddings of your data generated and stored by Atlas.

```
from nomic import AtlasDatasetdataset = AtlasDataset('my-dataset')atlas_map = dataset.maps[0]# projected embeddings are your 2D embeddingsprojected_embeddings = atlas_map.embeddings.projected# latent embeddings are your high-dim vectorslatent_embeddings = atlas_map.embeddings.latent
```

### AtlasMapEmbeddings API Reference​

```
class AtlasMapEmbeddings()
```

Atlas Embeddings State

Access latent (high-dimensional) and projected (two-dimensional) embeddings of your datapoints.

## Topics​

Directly access your Atlas-generated topics with atlas_map.topics.df. This dataframe include depth-unique ids and human interpretable descriptions for your datasets topics.

```
atlas_map.topics.df
```

Atlas topic models are hierarchical. As you zoom in and out in the Atlas in-browser data map explorer, you will see topics appear and disappear at different zoom levels.

The topics which the Atlas system generates behind the scenes is directly accessible via Python. Information is available about topic hierarchy and topic density. Topic information can be used for downstream pipelines like visualization, analyses, and predictions.

Your embedding information can be accessed in the map.topics attribute of the AtlasDataset:

```
map.topics
```

```
AtlasDataset
```

```
from nomic import AtlasDatasetmap = AtlasDataset('my-dataset').maps[0]
```

```
# Pandas df of your data with columns ID, topic_depth_n, topic_depth_n+1, etc.print(map.topics.df)
```

```
id_    topic_depth_1          topic_depth_2             topic_depth_30    +Bw    Baby, Ray, Sunglasses  Apparel                   T-Shirts (2)1    fHM    Phone Protector        Music Genre               Blues Music  2    9Ts    Lighting Replacement   Years                     Hyundai Engines3    6mU    Women's Fashion (3)    Footwear (14)             Women's Sandals4    8j8    Women's Fashion (3)    Tops, Shirts, Shirt       Women's Tops (2)...  ...    ...                    ...                       ...117238 GRs  Electronics (5)        Smartphones (3)           Computer Peripherals117239 AULT Electronics (5)        Computer Hardware (2)     Computer Upgrades117240 P0U  Electronics (5)        Computer Hardware (2)     Computer Hardware  117241 AWnV Electronics (5)        Computer Hardware (2)     Computer Hardware117242 5Vg  Electronics (5)        Computer Hardware (2)     Computer Hardware[117243 rows × 4 columns]
```

Pandas dataframe where each row corresponds to a unique topic. Metadata associated with each topic includes:

- topic depth
- a human-readable topic description (topic label)
- identifying keywords that differentiate the topic from other topics
```
# Returns a Pandas dfprint(map.topics.metadata)
```

```
depth  topic_id  topic_depth_1           topic_description                                 topic_short_description  topic_depth_2  topic_depth_30     1     0         Women's Fashion (3)      women/tops/dress/sandals/womens/casual/shoes/p...  Women's Fashion (3)     NaN           NaN1     1     1         Electronics (5)          USB/Bluetooth/iPhone/charging/Intel/cable/HDMI...  Electronics (5)         NaN           NaN2     1     2         Jewelry Collection (2)   jewelry/IceCarats/Jewelry/Type/ICECARATS/Sterl... Jewelry Collection (2)   NaN           NaN3     1     3         Phone Protector         phone/Galaxy/Samsung/dogs/Watch/protector/scre...   Phone Protector         NaN           NaN4     1     4         Pool Supplies           Pool/pool/Floats/chair/Brand/Amazon/Lathe/floa...   Pool Supplies           NaN           NaN...   ...   ...       ...                     ...                                                 ...                      ...           ...605   3     507       Lighting Replacement    hose/garden/Garden/watering/Hose/ft/plants/Jet...   Garden Hose             Plumbing S... Garden Hose606   3     508       Lighting Replacement    Rate/9930/gallons/207/months/38℃/125PSI/GPM/34...   Water Pump              Plumbing S... Water Pump607   3     509       Lighting Replacement    NPT/¼/½/PSI/Pump/Straight/tire/pump/12V/Connec...   Tire Pump               Plumbing S... Tire Pump608   3     510       Lighting Replacement    drain/Drain/sink/pipe/Sink/stopper/steel/toile...   Plumbing Fixtures       Plumbing S... Plumbing Fixtures609   3     511       Lighting Replacement    shower/water/Shower/filter/solar/fountain/head...    Bathroom Essentials     Plumbing S... Bathroom Essentials610 rows × 7 columns
```

The topic hierarchy brances from the most general topics down to sub-topics at different depths.

```
# map.topics.hierarchy is a dicthierarchy = map.topics.hierarchyprint(f'Your depth 1 (most general) topics are: {hierarchy.keys()}')
```

```
Your depth 1 (most general) topics are: dict_keys([  ("Women's Fashion (3)", 1),   ('Electronics (5)', 1),   ('Jewelry Collection (2)', 1),   ...])
```

You can use higher-level topic keys to access lower-level topics in your hierarchy.

```
import random# List the subtopics in a random top-level topicrandom_topic_1 = random.choice(list(hierarchy.keys()))print(f'The general topic {random_topic_1} contains subtopics {hierarchy[random_topic_1]}')
```

```
The general topic ('Footwear (14)', 2) contains subtopics [  'Shoes (3)', 'Sandal', 'Sneaker Culture', ..., "Women's Sandals"]
```

By providing a specific level of the topic hierarchy, you get a list of dictionaries where each item is a distinct topic at that level.

Keys for that topic include subtopics, subtopic_ids, topic_id, topic_short_description, topic_long_description, and datum_ids.

```
subtopics
```

```
subtopic_ids
```

```
topic_id
```

```
topic_short_description
```

```
topic_long_description
```

```
datum_ids
```

```
your_depth_level = 2print(map.topics.group_by_topic(your_depth_level)[0])
```

```
{  'subtopics': ['Miscellaneous (3)'],   'subtopic_ids': [87],   'topic_id': 16,   'topic_short_description': 'Audio Equipment (3)',   'topic_long_description': 'Bluetooth/speaker/Speaker/music/CarPlay/MP3/prevention/bluetooth/stereo/sound/karaoke/Loss/Radio/⭐/radio',   'datum_ids': {'61c', '/WM', 'Rsw', 'q6I', ...,  'AVjU'}}
```

### AtlasMapTopics API Reference​

```
class AtlasMapTopics()
```

Atlas Topics State

### df​

```
@propertydef df() -> pd.DataFrame
```

A pandas DataFrame associating each datapoint on your map to their topics as each topic depth.

### tb​

```
@propertydef tb() -> pa.Table
```

Pyarrow table associating each datapoint on the map to their Atlas assigned topics.
This table is memmapped from the underlying files and is the most efficient way to
access topic information.

### metadata​

```
@propertydef metadata() -> pd.DataFrame
```

Pandas DataFrame where each row gives metadata all map topics including:

- topic id
- a human readable topic description (topic label)
- identifying keywords that differentiate the topic from other topics
### hierarchy​

```
@propertydef hierarchy() -> Dict
```

A dictionary that allows iteration of the topic hierarchy. Each key is of (topic label, topic depth)
to its direct sub-topics.
If topic is not a key in the hierarchy, it is leaf in the topic hierarchy.

### group_by_topic​

```
def group_by_topic(topic_depth: int = 1) -> List[Dict]
```

Associates topics at a given depth in the topic hierarchy to the identifiers of their contained datapoints.

Arguments:

- topic_depth - Topic depth to group datums by.
```
topic_depth
```

Returns:

List of dictionaries where each dictionary contains next depth
subtopics, subtopic ids, topic_id, topic_short_description,
topic_long_description, and list of datum_ids.

### get_topic_density​

```
def get_topic_density(time_field: str, start: datetime, end: datetime)
```

Computes the density/frequency of topics in a given interval of a timestamp field.

Useful for answering questions such as:

- What topics increased in prevalence between December and January?
Arguments:

- time_field - Your metadata field containing isoformat timestamps
```
time_field
```

- start - A datetime object for the window start
```
start
```

- end - A datetime object for the window end
```
end
```

Returns:

A list of {topic, count} dictionaries, sorted from largest count to smallest count.

```
{topic, count}
```

### vector_search_topics​

```
def vector_search_topics(queries: np.ndarray,                         k: int = 32,                         depth: int = 3) -> Dict
```

Given an embedding, returns a normalized distribution over topics.

Useful for answering the questions such as:

- What topic does my new datapoint belong to?
- Does by datapoint belong to the "Dog" topic or the "Cat" topic.
Arguments:

- queries - a 2d NumPy array where each row corresponds to a query vector
```
queries
```

- k - (Default 32) the number of neighbors to use when estimating the posterior
```
k
```

- depth - (Default 3) the topic depth at which you want to search
```
depth
```

Returns:

A dict mapping {topic: posterior probability} for each query.

```
{topic: posterior probability}
```

## Duplicate Detection​

Duplicate detection is enabled by default when creating an Atlas map using the Nomic Atlas Python SDK:

```
from nomic import AtlasDatasetdataset_identifier = "my-dataset" # for my-dataset in the organization connected to your Nomic API key# dataset_identifier = "<ORG_NAME>/my-dataset" # for my-dataset in other organizations you are a member ofatlas_dataset = AtlasDataset(dataset_identifier)atlas_dataset.add_data(my_data)# Duplicate detection runs by defaultatlas_dataset.create_index(indexed_field="text")
```

While duplicate detection runs by default, you can fine-tune its behavior by providing NomicDuplicatesOptions to the create_index method. The main parameter you might adjust is the duplicate_cutoff threshold. Smaller thresholds result in duplicate clusters containing datapoints that are closer to exact matches. The default threshold is 0.1.

```
NomicDuplicatesOptions
```

```
create_index
```

```
duplicate_cutoff
```

```
0.1
```

```
from nomic import AtlasDataset, NomicDuplicatesOptions# ... (Dataset creation and data addition as above) ...atlas_dataset.create_index(        indexed_field="text",        duplicate_detection=NomicDuplicatesOptions(                tag_duplicates=True,                duplicate_cutoff=0.2, # Adjust the similarity threshold    ))
```

Directly access your Atlas-detected duplicate datapoint clusters with atlas_map.duplicates.df.

```
atlas_map.duplicates.df
```

Every datapoint is assigned a duplicate cluster_id. Two points share a cluster_id if Atlas identified them
to be semantic duplicates based of latent space properties.

```
cluster_id
```

```
cluster_id
```

```
from nomic import AtlasDatasetatlas_dataset = AtlasDataset(dataset_identifier)atlas_map = atlas_dataset.maps[0]duplicate_info_df = atlas_map.duplicates.dfprint(duplicate_info_df)
```

```
index      duplicate_class  cluster_id0      100001            singleton       164921      100011            singleton       160172      100016            singleton        78263      100020            singleton        50444      100030  retention candidate         412...       ...                  ...         ...19995   99721            singleton        921819996   99730   deletion candidate         37119997   99918            singleton       1331119998   99926            singleton       1372519999    9997            singleton        3866...       ...                  ...         ...
```

You can use your deletion candidates from the duplicate detection results and curate a new dataset without them.

```
# Get your old dataframeold_df = atlas_map.data.df# Get a list of IDs for datapoints marked as deletion candidates# We will keep only singletons and retention candidatesids_to_remove = atlas_map.duplicates.deletion_candidates()if ids_to_remove:    new_df = old_df[~old_df['id'].isin(ids_to_remove)]    new_identifier = dataset_identifier + "-without-duplicates"    new_dataset = AtlasDataset(        new_identifier,        description=f'Map of {dataset_identifier} without duplicates',    )    new_dataset.add_data(new_df)    new_dataset.create_index(        indexed_field="text"    )
```

### AtlasMapDuplicates API Reference​

```
class AtlasMapDuplicates()
```

Atlas Duplicate Clusters State. Atlas can automatically group embeddings that are sufficiently close into semantic clusters.
You can use these clusters for semantic duplicate detection allowing you to quickly deduplicate
your data.

### df​

```
@propertydef df() -> pd.DataFrame
```

Pandas DataFrame mapping each data point to its cluster of semantically similar points.

### tb​

```
@propertydef tb() -> pa.Table
```

Pyarrow table with information about duplicate clusters and candidates.
This table is memmapped from the underlying files and is the most efficient way to
access duplicate information.

### deletion_candidates​

```
def deletion_candidates() -> List[str]
```

Returns:

The ids for all data points which are semantic duplicates and are candidates for being deleted from the dataset. If you remove these data points from your dataset, your dataset will be semantically deduplicated.

## Tags​

Users can tag data in Atlas for workflows like data cleaning or curating training data for a classification model.

From python, to get the data that has been given a tag, use atlas_map.tags.get_datums_in_tag(tag_name).

```
atlas_map.tags.get_datums_in_tag(tag_name)
```

For example, here is how to get a map's data that has been tagged 'sports':

```
from nomic import AtlasDatasetdataset = AtlasDataset('my-dataset')atlas_map = dataset.maps[0]sports_ids = atlas_map.tags.get_datums_in_tag('sports')sports_data = dataset.get_data(sports_ids)
```

Here is how to get all existing map tags and the number of points in each with atlas_map.tags.get_tags():

```
atlas_map.tags.get_tags()
```

```
from nomic import AtlasDatasetdataset = AtlasDataset('my-dataset')atlas_map = dataset.maps[0]tags = atlas_map.tags.get_tags()for tag in tags:    tag_ids = atlas_map.tags.get_datums_in_tag(tag['tag_name'])    print(tag['tag_name'], "Count:", len(tag_ids))
```

For more on using tags in a pipeline, check out the data curation walkthrough.

### AtlasMapTags API Reference​

```
class AtlasMapTags()
```

Atlas Map Tag State. You can manipulate tags by filtering over
the associated pandas DataFrame.

### df​

```
@propertydef df(overwrite: bool = False) -> pd.DataFrame
```

Pandas DataFrame mapping each data point to its tags.

### get_tags​

```
def get_tags() -> List[Dict[str, str]]
```

Retrieves back all tags made in the web browser for a specific map.
Each tag is a dictionary containing tag_name, tag_id, and metadata.

Returns:

A list of tags a user has created for projection.

### get_datums_in_tag​

```
def get_datums_in_tag(tag_name: str, overwrite: bool = False)
```

Returns the datum ids in a given tag.

Arguments:

- overwrite - If True, re-downloads the tag. Otherwise, checks to see if up
to date tag already exists.
```
overwrite
```

Returns:

List of datum ids.

- Dataset
- Embeddings
- Topics
- Duplicate Detection
- Tags
