# Source: https://docs.unstructured.io/ui/enriching/image-descriptions.md

# Image descriptions

<iframe width="560" height="315" src="https://www.youtube.com/embed/pMQm9ymM3N8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

After partitioning, you can have Unstructured generate text-based summaries of detected images.

This summarization is done by using models offered through various model providers.

Here is an example of the output of a detected image using GPT-4o. Note specifically the `text` field that is added.
Line breaks have been inserted here for readability. The output will not contain these line breaks.

```json  theme={null}
{
    "type": "Image",
    "element_id": "3303aa13098f5a26b9845bd18ee8c881",
    "text": "{\n  \"type\": \"graph\",\n  \"description\": \"The graph shows 
        the relationship between Potential (V) and Current Density (A/cm2). 
        The x-axis is labeled 'Current Density (A/cm2)' and ranges from 
        0.0000001 to 0.1. The y-axis is labeled 'Potential (V)' and ranges 
        from -2.5 to 1.5. There are six different data series represented 
        by different colors: blue (10g), red (4g), green (6g), purple (2g), 
        orange (Control), and light blue (8g). The data points for each series 
        show how the potential changes with varying current density.\"\n}",
    "metadata": {
        "filetype": "application/pdf",
        "languages": [
            "eng"
        ],
        "page_number": 1,
        "image_base64": "/9j...<full results omitted for brevity>...Q==",
        "image_mime_type": "image/jpeg",
        "filename": "7f239e1d4ef3556cc867a4bd321bbc41.pdf",
        "data_source": {}
    }
}
```

<Note>
  The `image_base64` field is generated only for documents or PDF pages that are [partitioned](/ui/partitioning) by using the High Res strategy. This field is not generated for
  documents or PDF pages that are partitioned by using the Fast or VLM strategy.
</Note>

For workflows that use [chunking](/ui/chunking), note the following changes:

* Each `Image` element is replaced by a `CompositeElement` element.
* This `CompositeElement` element will contain the image's summary description as part of the element's `text` field.
* This `CompositeElement` element will not contain an `image_base64` field.

Here are three examples of the descriptions for detected images. These descriptions are generated with GPT-4o by OpenAI:

<img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/enriching/Image-Description-1.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=8a0b06395070f17ab506d0fcaf16215a" alt="Description of an image showing a scatter plot graph" data-og-width="2970" width="2970" data-og-height="458" height="458" data-path="img/enriching/Image-Description-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/enriching/Image-Description-1.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=2259f59c869211cbbb5e6769d6f43962 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/enriching/Image-Description-1.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=88d07f255d81c05c441e83c5dc772c2a 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/enriching/Image-Description-1.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=8f5ebefe720961bebbf7349ff73a0f69 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/enriching/Image-Description-1.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=71f10d3cf8948e9a3a546149f33c1277 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/enriching/Image-Description-1.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=853e08bbe6845220c8dc0381e4c0f15b 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/enriching/Image-Description-1.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=dfda06da7c7701d66863fd9ab25bcd6e 2500w" />

<img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-2.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=267621de3b05f57c3c028dedb956d627" alt="Description of an image showing the Matthews Correlation Coefficient for different VQA datasets" data-og-width="2970" width="2970" data-og-height="442" height="442" data-path="img/enriching/Image-Description-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-2.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=3e7007067f76ff4b8d07b336fe49a7ac 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-2.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=262bb14e2df8f968662f2e0e3f370d54 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-2.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=ba99980d6cbd1d3d7170fb5c136968e1 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-2.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=da7930915a560295d588f0726e19a517 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-2.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=93d92082e3589c83085dfc988e1aed28 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-2.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=50a968b980b7b0ef45c6170b8f979c2d 2500w" />

<img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-3.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=c79e8f0ac5f35e1712ae4518d0b5636e" alt="Description of an image showing three scatter plots" data-og-width="2982" width="2982" data-og-height="374" height="374" data-path="img/enriching/Image-Description-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-3.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=006c177dfac538612bb3d580e22d446f 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-3.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=60d9df431bcf556b432314608f249979 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-3.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=266a91b667d5a82755b7f3a29355ac14 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-3.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=95b6bf5e8e1edd48065b6aa22c9415ed 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-3.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=804f527e7d42487fd5390add70483c7a 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Image-Description-3.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=e94315d34545a4be2936bd6b107fbb3e 2500w" />

Any embeddings that are produced after these summaries are generated will be based on the `text` field's contents.

## Generate image descriptions

To generate image descriptions, in an **Enrichment** node in a workflow, select **Image**, and then choose one of the available provider (and model) combinations that are shown.

<Note>
  You can change a workflow's image description settings only through [Custom](/ui/workflows#create-a-custom-workflow) workflow settings.

  For workflows that use [chunking](/ui/chunking), the **Chunker** node should be placed after all **Enrichment** nodes. Placing the
  **Chunker** node before an image descriptions **Enrichment** node could cause incomplete or no image descriptions to be generated.
</Note>

<Warning>
  The following models are no longer available as of the following dates:

  * Amazon Bedrock Claude Sonnet 3.5: October 22, 2025
  * Anthropic Claude Sonnet 3.5: October 22, 2025

  Unstructured recommends the following actions:

  * For new workflows, do not use any of these models.
  * For any workflow that uses any of these models, update that workflow as soon as possible to use a different model.

  Workflows that attempt to use any of these models on or after its associated date will return errors.
</Warning>

<Warning>
  Unstructured can potentially generate image summary descriptions only for workflows that are configured as follows:

  * With a **Partitioner** node set to use the **Auto** or **High Res** partitioning strategy, and an image summary description node is added.
  * With a **Partitioner** node set to use the **VLM** partitioning strategy. No image summary description node is needed (or allowed).

  Even with these configurations, Unstructured actually generates image summary descriptions only for files that contain images and are also eligible
  for processing with the following partitioning strategies:

  * **High Res**, when the workflow's **Partitioner** node is set to use **Auto** or **High Res**.
  * **VLM** or **High Res**, when the workflow's **Partitioner** node is set to use **VLM**.

  Unstructured never generates image summary descriptions for workflows that are configured as follows:

  * With a **Partitioner** node set to use the **Fast** partitioning strategy.
  * With a **Partitioner** node set to use the **Auto**, **High Res**, or **VLM** partitioning strategy, for all files that Unstructured encounters that do not contain images.
</Warning>
