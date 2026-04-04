# Source: https://docs.unstructured.io/ui/enriching/image-descriptions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Image descriptions

<iframe width="560" height="315" src="https://www.youtube.com/embed/pMQm9ymM3N8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

After partitioning, you can have Unstructured generate text-based summaries of detected images.

This summarization is done by using models offered through various model providers.

Here is an example of the output of a detected image using GPT-4o. Note specifically the `text` field that is added.
In this `text` field, `type` indicates the kind of image that was detected (in this case, a `diagram`), and `description` is a summary of the image.
Line breaks have been inserted here for readability. The output will not contain these line breaks.

<img src="https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Diagram-Example.png?fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=16c8e1ac1fcbd00932c9f2b4ebfa2005" alt="Example of a diagram" data-og-width="1112" width="1112" data-og-height="842" height="842" data-path="img/enriching/Diagram-Example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Diagram-Example.png?w=280&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=7a41102ba0d5a1d7824838935e7e0a69 280w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Diagram-Example.png?w=560&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=1f0ed45c549623d0f5edab66e1fa4d7e 560w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Diagram-Example.png?w=840&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=06b0dab8f7ba8be41463acc962957b77 840w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Diagram-Example.png?w=1100&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=0523313f67193a0169705a9737f6cfc0 1100w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Diagram-Example.png?w=1650&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=9cc970b99319944f0bf87e370080e9e9 1650w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Diagram-Example.png?w=2500&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=e4d21ad523642bb60aac78be8b98e89d 2500w" />

```json  theme={null}
{
  "type": "Image",
  "element_id": "dd1fb72db7937725c9a781906098e6f8",
  "text": "{\n    
    \"type\": \"diagram\",\n    
    \"description\": \"User uploads a flowchart image via a Web Browser, which is then 
      converted to a Base64 Encoded Image. This image is sent to the Back-end System 
      (Node.js) where it is processed by the AI Model Adapter. The output undergoes 
      Validation and Rendering, resulting in Normalized Mermaid Code. AI Assisted 
      Editing is available through an AI Assistant, which allows for the Regenerated 
      Flowchart Image to be viewed again in the Web Browser.\\n\\n
      Text in the image:\\n
        - User\\n
        - Upload flowchart image\\n
        - Web Browser\\n
        - Base64 Encoded Image\\n
        - Back-end System (Node.js)\\n
        - AI Model Adapter\\n
        - Validation and Rendering\\n
        - Normalized Mermaid Code\\n
        - AI Assisted Editing\\n
        - AI Assistant\\n
        - Regenerated Flowchart Image\"\n
  }",
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

For technical drawings, the `text` field will contain a `type` of `technical drawing`; `description` with `texts` containing text strings found in the drawing,
`tables` containing HTML representations of tables found in the drawing, and a `description` containing a summary of the drawing.
Here is an example. Line breaks have been inserted here for readability. The output will not contain these line breaks.

<img src="https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Technical-Drawing-Example.png?fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=e4d3fb249208b3166b0e79a9d54b4cdf" alt="Example of a technical drawing" data-og-width="1468" width="1468" data-og-height="782" height="782" data-path="img/enriching/Technical-Drawing-Example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Technical-Drawing-Example.png?w=280&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=1dc71713c55e51adc75a04a4cb2f379e 280w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Technical-Drawing-Example.png?w=560&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=45d530c526f19e4a297853089bccbc9f 560w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Technical-Drawing-Example.png?w=840&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=1f7b15ac7c1927436daa9232be2a8944 840w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Technical-Drawing-Example.png?w=1100&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=f610544e6d84ce84e88402549b66eca8 1100w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Technical-Drawing-Example.png?w=1650&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=3137b95737ca36bf07f989c3f95b0cd7 1650w, https://mintcdn.com/unstructured-53/8osKRiNz_JLtvBTP/img/enriching/Technical-Drawing-Example.png?w=2500&fit=max&auto=format&n=8osKRiNz_JLtvBTP&q=85&s=53d8f2bd14dfff5c2c95dbd56994f7be 2500w" />

```json  theme={null}
{
  "type": "Image",
  "element_id": "7877acdd762f2afc65b193fa89d8ef46",
  "text": "{\n  
    \"type\": \"technical drawing\",\n  
    \"description\": {\n    
      \"texts\": [\n
        \"RTD 1\",\n      
        \"RTD 2\",\n      
        \"01\",\n      
        \"18.50\\\" Cable Length\",\n      
        \"02\",\n      
        \"1/4\\\" Heat Shrink\",\n      
        \"6X Strip wires 0.100\\\" - 0.115\\\" before crimping\",\n      
        \"2X 1.50\",\n      
        \"22.25\\\" Cable Length\"\n    
      ],\n    
      \"tables\": "<table>
        <thead>
          <tr>
            <th>Item</th>
            <th>Quantity</th>
            <th>Part Number</th>
            <th>Description</th>
            <th>Supplier</th>
            <th>Supplier PN</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>6</td>
            <td>002622</td>
            <td>Conn Socket 20-24AWG Gold</td>
            <td>Digikey</td>
            <td>WM7082CT-ND</td>
          </tr>
          <tr>
            <td>2</td>
            <td>1</td>
            <td>002647</td>
            <td>Conn Recept 16pos 3mm Dual Row</td>
            <td>Digikey</td>
            <td>WM2490-ND</td>
          </tr>
          <tr>
              <td>3</td>
              <td>2</td>
              <td>102961-01</td>
              <td>M12 Q/D Cable, Elbow, 4-Pole, 5m</td>
              <td>Automation Direct</td>
              <td>EVT222</td>
          </tr>
        </tbody>
      </table>",\n    
      \"description\": \"The technical drawing depicts a wiring setup involving two 
          RTDs (Resistance Temperature Detectors) labeled RTD 1 and RTD 2. Each RTD 
          is connected via cables with specified lengths: RTD 1 has an 18.50-inch 
          cable length, and RTD 2 has a 22.25-inch cable length. The drawing 
          includes annotations for stripping wires, indicating that six wires should 
          be stripped to a length between 0.100 inches and 0.115 inches before 
          crimping. There is a section labeled '1/4\\\" Heat Shrink' and a dimension 
          marked '2X 1.50'. The drawing uses numbered circles to reference specific 
          parts or steps in the process.\"\n  
      }\n
  }",
  "metadata": {
    "filetype": "application/pdf",
    "languages": [
      "eng"
    ],
    "page_number": 1,
    "image_base64": "/9j...<full results omitted for brevity>...Q==",
    "image_mime_type": "image/jpeg",
    "filename": "Material-Callouts-c4655c0c.pDF",
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
