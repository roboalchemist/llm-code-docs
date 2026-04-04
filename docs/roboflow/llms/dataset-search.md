# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/manage-datasets/dataset-search.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/manage-datasets/dataset-search.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/manage-datasets/dataset-search.md

# Source: https://docs.roboflow.com/datasets/manage-datasets/dataset-search.md

# Search a Dataset

You can search for image files in Roboflow by file name, a search query, and mix and match queries and filters to find specific images and better understand your data.

* **Images in a split with a certain tag:**\
  `tag:factory split:train`\
  This uses a tag filter and a split filter
* **Find missing labels by using semantic search and a class filter**:\
  `person -class:helmet`\
  This uses semantic search and an inverted filter on a class filter
* **If all images with a class need a certain filter:**\
  `class:helmet AND NOT (tag:v1 OR tag:v2)`\
  This uses a class filter, boolean logic, and tag filters
* **Find wide images with a low number of annotations:**\
  `min-width:1000 max-annotations:1`\
  This uses a minimum width filter and a max annotation count filter

See the full list of [search filters](#search-filters), as well as examples below

{% hint style="info" %}
You can combine all of these search filters and queries together
{% endhint %}

### Semantic Search

You can search for images by describing them. These queries will search for images most closely related to your search terms and can help you find images even when objects are not currently labeled.

Semantic search happens when you enter a text query without any filter selectors (ex: `filename:`)

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-252e7735b8f04fdeb7b567c8a73c783ba42c7ba0%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Search by File Name

You can search for file names using the `filename:` filter or the file name textbox, which will create the query for you.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-007ef7663b94243be3a88de95df3a6fe6345bf5f%2Fimage.png?alt=media" alt="" width="192"><figcaption></figcaption></figure>

### Search by Dataset Split

Search images by the dataset split (train, valid, test)

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-42804a6e68a1551a7f23c0fe1746da8231fb5b02%2Fimage.png?alt=media" alt="" width="257"><figcaption></figcaption></figure>

## Search Filters

Here are the filters available:

* `like-image:<IMAGE_ID>`: Semantic search based on image content
* `tag` : Filter by user-provided tags.
* `filename` : Runs a search for file names that match the provided file name. Use \* at the beginning and end of a query to run a partial match.
* `split` : Filters by split (train, test, valid).
* `job:<JOB_ID>` : Shows images with the provided job ID.
* `min-width:X` : Shows images with a width greater than X.
* `max-width:X` : Shows images with a width less than X.
* `min-height:X` : Shows images with a height greater than X.
* `max-height:X` : Shows images with a height less than X.
* `min-annotations:X` : Filters images with more than the specified number of annotations.
* `max-annotations:X` : Shows images with fewer than the specified number of annotations.
* `class:CLASS`: Shows images that have at least 1 annotation with the provided label.

### Boolean Logic

Use AND, OR, NOT, and parentheses to combine multiple filters to form complex queries.

`class:helmet AND NOT (tag:v1 OR tag:v2)`

### Inverted Filters

Add a minus sign before the filter to exclude images matching the filter.

`class:helmet -class:vest`

### Numeric Class Filters

Filter by the number of labeled items in an image.

`class:helmet=3 class:vest>=4`

## API

You can also search your dataset and images on Roboflow via our [Search API](https://docs.roboflow.com/api-reference/images/search#rest-api).
