# (y_patches + 6, 128)
pooled_by_columns = torch.cat([pooled_by_columns, image_embedding[~mask]])

```

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#upload-to-qdrant) Upload to Qdrant

The upload process is trivial; the only thing to pay attention to is the compute cost for ColPali and ColQwen2 models.
In low-resource environments, it’s recommended to use a smaller batch size for embedding and mean pooling.

Full version of the upload code is available in the [tutorial notebook](https://githubtocolab.com/qdrant/examples/blob/master/pdf-retrieval-at-scale/ColPali_ColQwen2_Tutorial.ipynb)

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/pdf-retrieval-at-scale/\#querying-pdfs) Querying PDFs

After indexing PDF documents, we can move on to querying them using our two-stage retrieval approach.

```python
query = "Lee Harvey Oswald's involvement in the JFK assassination"
processed_queries = model_processor.process_queries([query]).to(model.device)