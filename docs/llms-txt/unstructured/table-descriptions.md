# Source: https://docs.unstructured.io/ui/enriching/table-descriptions.md

# Table descriptions

<iframe width="560" height="315" src="https://www.youtube.com/embed/3UIW5PDck74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

After partitioning, you can have Unstructured generate text-based summaries of detected tables.

This summarization is done by using models offered through various model providers.

Here is an example of the output of a detected table using GPT-4o. Note specifically the `text` field that is added.
Line breaks have been inserted here for readability. The output will not contain these line breaks.

```json  theme={null}
{
    "type": "Table",
    "element_id": "5713c0e90194ac7f0f2c60dd614bd24d",
    "text": "The table consists of 6 rows and 7 columns. The columns represent 
        inhibitor concentration (g), bc (V/dec), ba (V/dec), Ecorr (V), icorr 
        (A/cm\u00b2), polarization resistance (\u03a9), and corrosion rate 
        (mm/year). As the inhibitor concentration increases, the corrosion 
        rate generally decreases, indicating the effectiveness of the 
        inhibitor. Notably, the polarization resistance increases with higher 
        inhibitor concentrations, peaking at 6 grams before slightly 
        decreasing. This suggests that the inhibitor is most effective at 
        6 grams, significantly reducing the corrosion rate and increasing 
        polarization resistance. The data provides valuable insights into the 
        optimal concentration of the inhibitor for corrosion prevention.",
    "metadata": {
        "text_as_html": "<table>...<full results omitted for brevity>...</table>",
        "filetype": "application/pdf",
        "languages": [
            "eng"
        ],
        "page_number": 1,
        "image_base64": "/9j...<full results omitted for brevity>...//Z",
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

Here are two examples of the descriptions for detected tables. These descriptions are generated with GPT-4o by OpenAI:

<img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-1.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=35d5ed3a55a463deb9450e6841e15a89" alt="Description of a table with information about endoscopic datasets" data-og-width="2978" width="2978" data-og-height="562" height="562" data-path="img/enriching/Table-Description-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-1.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=e1c7018844513570205cd2b4cb8e110e 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-1.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=51ffc6fa2fae9fa04cc91535e1511226 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-1.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=60a0bb92bd07061da28e7b5fbdcedaf7 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-1.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=563fc53f4ab297c7cd1739d72e13f20c 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-1.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=ecb939c4695dff39a073c2398bc3ecc1 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-1.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=80882b18948d17aa503d01834ac9049d 2500w" />

<img src="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-2.png?fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=69356d0e8ff919facc848645ca04e2df" alt="Description of a table with information about potentiodynamic polarization of stainless steel" data-og-width="3108" width="3108" data-og-height="544" height="544" data-path="img/enriching/Table-Description-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-2.png?w=280&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=f5359c7b6d9540046f92e328d242a984 280w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-2.png?w=560&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=a864dce3563c09ac1fb5bc82595e416b 560w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-2.png?w=840&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=bbc57d51163dbd6f14b4137c71f82e6a 840w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-2.png?w=1100&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=e521ed67f0cf40341c70791e4ef00e23 1100w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-2.png?w=1650&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=b112071b4a3942dda5c42331ae958725 1650w, https://mintcdn.com/unstructured-53/ognmPfo7rw6i-YTz/img/enriching/Table-Description-2.png?w=2500&fit=max&auto=format&n=ognmPfo7rw6i-YTz&q=85&s=1f2d75d2dc56aadf43301ed82dd0ad3a 2500w" />

The generated table's summary will overwrite any text that Unstructured had previously extracted from that table into the `text` field.
The table's original content is available in the `image_base64` field.

<Note>
  The `image_base64` field is generated only for documents or PDF pages that are [partitioned](/ui/partitioning) by using the High Res strategy. This field is not generated for
  documents or PDF pages that are partitioned by using the Fast or VLM strategy.
</Note>

For workflows that use [chunking](/ui/chunking), note the following changes:

* If a `Table` element must be chunked, the `Table` element is replaced by a set of related `TableChunk` elements.
* Each of these `TableChunk` elements will contain a summary description only for its own element, as part of the element's `text` field.
* These `TableChunk` elements will not contain an `image_base64` field.

Any embeddings that are produced after these summaries are generated will be based on the new `text` field's contents.

## Generate table descriptions

To generate table descriptions, in an **Enrichment** node in a workflow, select **Table**, and then choose one of the available provider (and model) combinations that are shown.

Make sure after you choose the provider and model, that **Table Description** is also displayed. If **Table Description** and **Table to HTML** are both
displayed, be sure to select **Table Description**.

<Note>
  You can change a workflow's table description settings only through [Custom](/ui/workflows#create-a-custom-workflow) workflow settings.

  For workflows that use [chunking](/ui/chunking), the **Chunker** node should be placed after all **Enrichment** nodes. Placing the
  **Chunker** node before a table descriptions **Enrichment** node could cause incomplete or no table descriptions to be generated.
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
  Unstructured can potentially generate table summary descriptions only for workflows that are configured as follows:

  * With a **Partitioner** node set to use the **Auto** or **High Res** partitioning strategy, and a table summary description node is added.
  * With a **Partitioner** node set to use the **VLM** partitioning strategy. No table summary description node is needed (or allowed).

  Even with these configurations, Unstructured actually generates table summary descriptions only for files that contain tables and are also eligible
  for processing with the following partitioning strategies:

  * **High Res**, when the workflow's **Partitioner** node is set to use **Auto** or **High Res**.
  * **VLM** or **High Res**, when the workflow's **Partitioner** node is set to use **VLM**.

  Unstructured never generates table summary descriptions for workflows that are configured as follows:

  * With a **Partitioner** node set to use the **Fast** partitioning strategy.
  * With a **Partitioner** node set to use the **Auto**, **High Res**, or **VLM** partitioning strategy, for all files that Unstructured encounters that do not contain tables.
</Warning>

## Learn more

* <Icon icon="video" />  [How to Extract Data from Complex Tables](https://unstructured.io/events/how-to-extract-data-from-complex-tables)
