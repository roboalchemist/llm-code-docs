# Source: https://docs.unstructured.io/ui/enriching/generative-ocr.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Generative OCR optimization

After partitioning, you can have a vision language model (VLM) optimize the fidelity of text blocks that Unstructured
initially processed during its partitioning phase.

Here are a few examples of Unstructured's output of text blocks that were initially processed, and the more accurate
version of these text blocks that were optimized by using Claude Sonnet 4. Irrelevant lines of output have been omitted here for brevity.

Example 1: Vertical watermarked text

<img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-watermark.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=7b0f23e8446dd7ce620e7651c50edeea" alt="Vertical watermarked text example" data-og-width="143" width="143" data-og-height="626" height="626" data-path="img/ui/enriching/generative-ocr-watermark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-watermark.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=15e47c50df569cbb2fe69924355c0c81 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-watermark.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=62218af951eb0ffaa3db8cad0ac60ad7 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-watermark.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=b1ea9bf9adc17b1b822445eccd16753b 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-watermark.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=7de690d74c56300e08f4caa282dd0e83 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-watermark.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=c4a2b211e386c3c091bb1b0490c52e22 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-watermark.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=9fe7a85cdf4b6b92d8cf8791f8af9163 2500w" />

Before (vertical watermarked text, represented incorrectly):

```json  theme={null}
{
    "...": "...",
    "text": "3 2 0 2 t c O 9 2 ] V C . s c [ 2 v 9 0 8 6 1 . 0 1 3 2 : v i X r",
    "...": "..."
}
```

After (vertical watermarked text, now represented correctly from the original content):

```json  theme={null}
{
    "...": "...",
    "text": "arXiv:2310.16809v2 [cs.CV] 29 Oct 2023",
    "...": "..."
}
```

Example 2: Hyperlink

<img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-hyperlink.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=b6839365e38048b688ad2e110198cb14" alt="Hyperlinked text example" data-og-width="507" width="507" data-og-height="188" height="188" data-path="img/ui/enriching/generative-ocr-hyperlink.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-hyperlink.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=7676f083d0aae46beae3730507fea500 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-hyperlink.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=72123904e13ff21a48fc7dfbe9d1b9c2 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-hyperlink.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=3c45a6ad472957fce954c320e8a866c4 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-hyperlink.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=dec0c975b72e6d5b00d60082d05fdcb3 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-hyperlink.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=ff0c0b77aef00bb4add76ba19b7c3ae0 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-hyperlink.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=4e03fb162af79f94c482d061f346ccf9 2500w" />

Before (hyperlink, represented incorrectly):

```json  theme={null}
{
    "...": "...",
    "text": "con/Yuliang-Liu/MultinodalOCR|",
    "...": "..."
}
```

After (hyperlink, now represented correctly from the original content):

```json  theme={null}
{
    "...": "...",
    "text": "https://github.com/Yuliang-Liu/MultimodalOCR",
    "...": "..."
}
```

Example 3: Chinese characters

<img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-image.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=d7c523324999fc3da8752920d5fb3795" alt="Chinese characters example" data-og-width="269" width="269" data-og-height="200" height="200" data-path="img/ui/enriching/generative-ocr-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-image.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=f134ff22d50f41c8394b9d6edbda3f3d 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-image.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=b00d4d697ece67fe41c24a03cf5cf048 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-image.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=160372e44d78bbe97e7ccbbfbf542e45 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-image.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=5a08bd9af73e30dc858c6e8d1eaa1a44 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-image.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=e3c54125e96cbef101f10b65ca93e696 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/enriching/generative-ocr-image.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=996c067c1840b4b82eb0f5d25a7d70c6 2500w" />

Before (Chinese characters, represented incorrectly):

```json  theme={null}
{
    "...": "...",
    "text": "GT SHE GPT4-V: EHES",
    "...": "..."
}
```

After (Chinese characters, now represented correctly from the original content, expressed as Unicode):

```json  theme={null}
{
    "...": "...",
    "text": "GT : \u91d1\u724c\u70e7\u814a GPT4-V: \u6587\u9759\u5019\u9e1f",
    "...": "..."
}
```

## Improve text fidelity with generative OCR

To produce generative OCR optimizations, in an **Enrichment** node in a workflow, click the following
in the node's settings pane's **Details** tab:

* **Image** under **Input Type**.

* One of the following providers and models:

  * **Anthropic** under **Provider** and any choice under **Model**
  * **OpenAI** under **Provider** and any choice under **Model**

* **Generative OCR** under **Task**.

<Warning>
  Generative OCR does not process any text blocks by default. You must also explicitly specify which document element
  types containing text that you want generative OCR to process. To do this, in the workflow editor for your workflow:

  1. Click the **Partitioner** node.
  2. In the node's settings pane, scroll down to and then click a blank area inside of the **Extract Image Block Types** list.
  3. Select each [document element types](/ui/document-elements#element-type) that you want generative OCR to process. For this
     walkthrough, select only **NarrativeText**.

  Generative OCR does not process the text of any `Image` or `Table` elements if they have already been processed by
  [image description](#image-description-task) or [table description](#table-description-task) enrichments, respectively. Do
  not remove the **Image** or **Table** document elements types from this **Extract Image Block Types** list, or else
  the image description and table description enrichments in your workflow might produce unexepcted results or might not work at all.
</Warning>

<Note>
  The **Generative OCR** enrichment appears under the **Input Type** of **Image**, even though this is not an image-related enrichment.
  This is a known issue and will be addressed in a future release.
</Note>

<Note>
  You can change a workflow's image description settings only through [Custom](/ui/workflows#create-a-custom-workflow) workflow settings.

  For workflows that use [chunking](/ui/chunking), the **Chunker** node should be placed after all **Enrichment** nodes. Placing the
  **Chunker** node before an image descriptions **Enrichment** node could cause incomplete or no image descriptions to be generated.
</Note>

<Warning>
  Unstructured can produce generative OCR optimizations for workflows that are configured as follows:

  * With a **Partitioner** node set to use the **Auto** or **High Res** partitioning strategy, and a generative OCR optimizations node is added.
  * With a **Partitioner** node set to use the **VLM** partitioning strategy. No generative OCR optimization node is needed (or allowed).

  Unstructured never produces generative OCR optimizations for workflows with a **Partitioner** node set to use the **Fast** partitioning strategy.
</Warning>
