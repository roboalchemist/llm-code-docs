# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/guides/organize-and-search-images

Nomic Atlas natively supports image datasets, allowing users to interactively explore large image collections.

Atlas automatically organizes your image collections into clusters that group images with similar visual & semantic contents near each other in the map.

For example, you can explore hundreds of thousands of images of artworks from the Metropolitan Museum of Art in this data map in Atlas, which groups similar artworks into different neighborhoods of the map based on their visual content.

## Upload Images​

Currently, image datasets must be uploaded programatically via the Nomic Python SDK.

You can upload images as URLS, filepaths, or bytes.

Supported file types are .png, .jpg, and .webp.

```
.png
```

```
.jpg
```

```
.webp
```

Pass a list of filepaths, URLs, bytes, or PIL.Image objects to the blobs parameter when adding data to your dataset.

```
blobs
```

```
from nomic import AtlasDatasetdataset = AtlasDataset(your_dataset_name)dataset.add_data(    blobs=your_images,     data=your_metadata # Optional metadata for each image)atlas_map = dataset.create_index()
```

After upload images, Atlas will automatically embed your images using Nomic Embed Vision.

### Upload Custom Image Embeddings​

You can also bring your own image embeddings to Atlas:

For custom pre-computed image embeddings, use:

```
from nomic import AtlasDatasetdataset = AtlasDataset(your_dataset_name)# embeddings is a np.array of shape (n_embeddings, embedding_dim)dataset.add_data(    embeddings=your_image_embeddings,     data=your_metadata # Optional metadata for each image)atlas_map = dataset.create_index()
```

Developers can see more examples of uploading image datasets in the API reference for data upload functionality in the Nomic Python SDK here.

## Nomic Embed Vision​

Image support in Atlas is supported by our Apache 2.0-licensed image embedding model Nomic Embed Vision. You can read our release announcement for this model here on our blog. Developers looking to use the model programatically can read the API reference for the model here.

## Multimodality​

Atlas enables multimodal interation with your image data, e.g. searching over your image datasets with text queries to find images that depict content visually related to your queries.

For example, searching for animals over the Metropolitan Museum of Art map returns images of artwork that depicts animals.

```
animals
```

You can read more about multimodality in Atlas in our multimodality guide.

- Upload ImagesUpload Custom Image Embeddings
- Upload Custom Image Embeddings
- Nomic Embed Vision
- Multimodality
