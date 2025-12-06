# Source: https://docs.voyageai.com/docs/tokenization

## GET STARTED 

- [[[Introduction]]](/docs/introduction)
- [[[API Key and Python Client]]](/docs/api-key-and-installation)
- [[[Quickstart Tutorial]]](/docs/quickstart-tutorial)

## CAPABILITIES 

- [[[Text Embeddings]]](/docs/embeddings)
- [[[Contextualized Chunk Embeddings]]](/docs/contextualized-chunk-embeddings)
- [[[Multimodal Embeddings]]](/docs/multimodal-embeddings)
- [[[Rerankers]]](/docs/reranker)

## GUIDES 

- [[[Tokenization]]](/docs/tokenization)
- [[[Flexible Dimensions and Quantization]]](/docs/flexible-dimensions-and-quantization)
- [[[Batch Inference]]](/docs/batch-inference)
- [[[Error Codes]]](/docs/error-codes)
- [[[Rate Limits]]](/docs/rate-limits)
- [[[Pricing]]](/docs/pricing)
- [[[Organizations and Projects]]](/docs/organizations-and-projects)
- [[[Service Level Objectives]]](/docs/service-level-objectives)

## DEPLOYMENT ON VPC 

- [[AWS Marketplace Model Package]]
  - [[[MongoDB Voyage AI Models in AWS]]](/docs/aws-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in AWS]]](/docs/aws-marketplace-voyage)
- [[Azure Marketplace Managed Application]]
  - [[[MongoDB Voyage AI Models in Azure]]](/docs/azure-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in Azure]]](/docs/azure-marketplace-voyage)

## ACCESS VIA DATA PLATFORMS 

- [[[Snowflake]]](/docs/snowflake)

## Community 

- [[[Integrations]]](/docs/integrations-and-other-libraries)
- [[[Community SDKs]]](/docs/community-sdks)

## HELP 

- [[[FAQ]]](/docs/faq)
- [[[Contact Email]]](/docs/contact-email)
- [[[Discord]]](/docs/discord)

Powered by [](https://readme.com?ref_src=hub&project=voyage-ai)

# Tokenization

Given an input, the first step of the embedding/reranking process is to dissect it into a list of tokens. This tokenization step is automatically performed on our servers when you call the API. We open-source the tokenizers so that you can preview the tokenized results and verify the number of tokens the API uses.

> [📘]
>
> ###  
>
> ::: 
> :::
>
> ::: heading-text
> Voyage\'s Tokenizers on Hugging Face 🤗
> :::
>
> [](#voyages-tokenizers-on-hugging-face-)
>
> Voyage\'s tokenizers are available on [Hugging Face 🤗](https://huggingface.co/voyageai). You can access the tokenizer associated with a particular model using the following code:
>
> ::::: 
> ::: CodeTabs-toolbar
> Python
> :::
>
> ::: CodeTabs-inner
>     from transformers import AutoTokenizer
>
>     tokenizer = AutoTokenizer.from_pretrained('voyageai/voyage-3.5')
> :::
> :::::
>
> **Update on Voyage tokenizer**
>
> Our earlier models, including embedding models `voyage-01`, `voyage-lite-01`, `voyage-lite-01-instruct`, `voyage-lite-02-instruct`, `voyage-2`, `voyage-large-2`, `voyage-code-2`, `voyage-law-2`, `voyage-large-2-instruct`, and reranking model `rerank-lite-1`, use the same tokenizer as [Llama 2](https://ai.meta.com/llama/). However, our new models have adopted different tokenizers for optimized performance. Therefore, in the future, please specify the model you use when calling the tokenizer.

In our [Python package](/docs/api-key-and-installation#install-voyage-python-package), we provide functions in `voyageai.Client` which allows you to try the tokenizer before calling the API:

> [`voyageai.Client.tokenize`](https://github.com/voyage-ai/voyageai-python/blob/v0.3.1/voyageai/_base.py#L112)`(texts : List[str], model: str)`

**Parameters**

- **texts** (List\[str\]) - A list of texts to be tokenized.

- **model** (str) - Name of the model to be tokenized for. For example, `voyage-3-large`, `voyage-3.5`, `voyage-3.5-lite`, `rerank-2.5`, `rerank-2.5-lite`, `voyage-multimodal-3`.

  *Note*

  The \"model\" parameter was added in June 2024. Our earlier models, including embedding models `voyage-01`, `voyage-lite-01`, `voyage-lite-01-instruct`, `voyage-lite-02-instruct`, `voyage-2`, `voyage-large-2`, `voyage-code-2`, `voyage-law-2`, `voyage-large-2-instruct`, and reranking model `rerank-lite-1`, used the same tokenizer. However, our new models have adopted different tokenizers.

  **Please specify the \"model\" when using this function.** If \"model\" is unspecified, the old tokenizer will be loaded, which may produce mismatched results if you are using our latest models.

**Returns**

- A list of
  `tokenizers.Encoding`, each of which represents the tokenized results of an input text string.

------------------------------------------------------------------------

**Example - Return Tokens**

Python

Output

    import voyageai

    vo = voyageai.Client()
    # This will automatically use the environment variable VOYAGE_API_KEY.
    # Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

    texts = [ 
        "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
        "Photosynthesis in plants converts light energy into glucose and produces essential oxygen."
    ]

    tokenized = vo.tokenize(texts, model="voyage-3.5")
    for i in range(len(texts)):
        print(tokenized[i].tokens)

    ['The', 'ĠMediterranean', 'Ġdiet', 'Ġemphasizes', 'Ġfish', ',', 'Ġolive', 'Ġoil', ',', 'Ġand', 'Ġvegetables', ',', 'Ġbelieved', 'Ġto', 'Ġreduce', 'Ġchronic', 'Ġdiseases', '.']
    ['Photos', 'ynthesis', 'Ġin', 'Ġplants', 'Ġconverts', 'Ġlight', 'Ġenergy', 'Ġinto', 'Ġglucose', 'Ġand', 'Ġproduces', 'Ġessential', 'Ġoxygen', '.']

> [`voyageai.Client.count_tokens`](https://github.com/voyage-ai/voyageai-python/blob/v0.3.1/voyageai/_base.py#L129) `(texts : List[str], model: str)`

**Parameters**

- **texts** (List\[str\]) - A list of texts to count the tokens for.

- **model** (str) - Name of the model to be counted for. For example, `voyage-3-large`, `voyage-3.5`, `voyage-3.5-lite`, `rerank-2.5`, `rerank-2.5-lite`, `voyage-multimodal-3`.

  *Note*

  The \"model\" parameter was added in June 2024. Our earlier models, including embedding models `voyage-01`, `voyage-lite-01`, `voyage-lite-01-instruct`, `voyage-lite-02-instruct`, `voyage-2`, `voyage-large-2`, `voyage-code-2`, `voyage-law-2`, `voyage-large-2-instruct`, and reranking model `rerank-lite-1`, used the same tokenizer. However, our new models have adopted different tokenizers.

  **Please specify the \"model\" when using this function.** If \"model\" is unspecified, the old tokenizer will be loaded, which may produce mismatched results if you are using our latest models.

**Returns**

- The total number of tokens in the input texts, as an integer.

------------------------------------------------------------------------

**Example - Return Count of Tokens**

Python

Output

    import voyageai

    vo = voyageai.Client()
    # This will automatically use the environment variable VOYAGE_API_KEY.
    # Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

    texts = [ 
        "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
        "Photosynthesis in plants converts light energy into glucose and produces essential oxygen."
    ]

    total_tokens = vo.count_tokens(texts, model="voyage-3.5")
    print(total_tokens)

    32

> [`voyageai.Client.count_usage`](https://github.com/voyage-ai/voyageai-python/blob/v0.3.1/voyageai/_base.py#L137) `(inputs : List[dict] or List[List[Union[str, PIL.Image.Image]]] , model: str)`

**Parameters**

- **inputs** (List\[dict\] or List\[List\[Union\[str, PIL.Image.Image\]\]\]) - A list of text and image sequences for which to count text tokens, image pixels, and total tokens. The list elements follow the same format as the
  `inputs` parameter of
  `voyageai.Client.multimodal_embed()`, except that image URLs are not supported. For additional details, refer to the [Python API for Multimodal Embeddings](/docs/multimodal-embeddings#python-api).
- **model** (str) - Name of the model (which affects how inputs are counted). Currently, the only supported model is 
  `voyage-multimodal-3`. For other models that support only text, use the
  `voyageai.Client.count_tokens()` function to calculate token counts.

**Returns**

- A dictionary containing the following attributes:
  - **text_tokens** (int) - The total number of text tokens in the list of inputs.
  - **image_pixels** (int) - The total number of image pixels in the list of inputs.
  - **total_tokens** (int) - The combined total of text and image tokens. Every 560 pixels counts as a token.

------------------------------------------------------------------------

**Example**

Python

Output

    import voyageai
    import PIL

    vo = voyageai.Client()
    # This will automatically use the environment variable VOYAGE_API_KEY.
    # Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

    inputs = [ 
        ["This is a banana.", PIL.Image.open('banana.jpg')]
    ]

    usage = vo.count_usage(inputs, model="voyage-multimodal-3")
    print(usage)

    

Our embedding models have [context length limits](/docs/embeddings#model-choices). If your text exceeds the limit, you would need to truncate the text before calling the API, or specify the `truncation` argument so that we can do it for you.

[]

> [📘]
>
> ###  
>
> ::: 
> :::
>
> ::: heading-text
> Tokens, words, and characters
> :::
>
> [](#tokens-words-and-characters)
>
> Modern NLP models typically convert a text string into a list of tokens. Frequent words, such as \"you\" and \"apple,\" will be tokens by themselves. In contrast, rare or long words will be broken into multiple tokens, e.g., \"uncharacteristically\" is dissected into four tokens, \"▁un\", \"character\", \"ist\", and \"ically\". One word roughly corresponds to 1.2 - 1.5 tokens on average, depending on the complexity of the domain. The tokens produced by our tokenizer have an average of 5 characters, suggesting that you could roughly estimate the number of tokens by dividing the number of characters in the text string by 5. To determine the exact number of tokens, please use the `count_tokens()` function.

> [📘]
>
> ###  
>
> ::: 
> :::
>
> ::: heading-text
> tiktoken
> :::
>
> [](#tiktoken)
>
> `tiktoken` is the open-source version of OpenAI\'s tokenizer. Voyage models use different tokenizers, which can be accessed from [Hugging Face 🤗](https://huggingface.co/voyageai). Therefore, our tokenizer may generate a different list of tokens for a given text compared to `tiktoken`. Statistically, the number of tokens produced by our tokenizer is on average 1.1 - 1.2 times that of `tiktoken`. To determine the exact number of tokens, please use the `count_tokens()` function.

Updated 24 days ago

------------------------------------------------------------------------

[[]](/docs/reranker)

Rerankers

[](/docs/flexible-dimensions-and-quantization)

Flexible Dimensions and Quantization

[]