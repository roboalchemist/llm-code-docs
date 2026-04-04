# Source: https://firebase.google.com/docs/ai-logic/count-tokens.md.txt

<br />

Geminimodels process input and output in units called*tokens*.

Tokens can be single characters like`z`or whole words like`cat`. Long words are broken up into several tokens. The set of all tokens used by the model is called the vocabulary, and the process of splitting text into tokens is called*tokenization*.

ForGeminimodels, a token is equivalent to about 4 characters. 100 tokens is equal to about 60-80 English words.

Each model has a[maximum number of tokens](https://firebase.google.com/docs/ai-logic/models#specs-and-limitations-comparison)that it can handle in a prompt and response. Knowing the token count of your prompt lets you know if you've exceeded this limit. Additionally, the cost of a request is determined in part by the number of input and output tokens, so knowing how to count tokens can be helpful.
| **Tip:** To control the number of tokens used for generating a response (and thus control costs), you can set the[thinking budget](https://firebase.google.com/docs/ai-logic/thinking)(forGemini3 models andGemini2.5 models only) and the`maxOutputTokens`(allGeminimodels) in the[model's configuration](https://firebase.google.com/docs/ai-logic/model-parameters#gemini).

### Supported models

- `gemini-3-pro-preview`
- `gemini-3-flash-preview`
- `gemini-3-pro-image-preview`
- `gemini-2.5-pro`
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`
- `gemini-2.0-flash-001`(and its auto-updated alias`gemini-2.0-flash`)
- `gemini-2.0-flash-lite-001`(and its auto-updated alias`gemini-2.0-flash-lite`)

| **Note** : Although all generative models process input and output as tokens, this page and its token counting options are specific only to the*Gemini* models listed above.
|
| ForImagenmodels, pricing and limits aren't based on tokens.

## Options for counting tokens

All input and output for theGemini APIis tokenized, including text, image files, and other non-text modalities. Here are the options for counting tokens:

Check the token count for your*requests only*(before sending them to the model).
:   Call**`countTokens`** with the input of the request*before* sending it to the model. This returns:

    - `total_tokens`: token count of the*input only*

Check the token count for*both your requests and responses*.
:   Access the**`usageMetadata`** attribute on the response object. This includes:

    - `prompt_token_count`: token count of the input only
    - `candidates_token_count`: token count of the output only (does not include thinking tokens)
    - `thoughts_token_count`: token count of any thinking tokens used to generate the response
    - `total_token_count`: total count of tokens for*both*the input and the output (includes any thinking tokens)

    When streaming output, the`usageMetadata`attribute only appears on the last chunk of the stream. It's`nil`for intermediate chunks.

Note the following points about the options above:

- They will*not* count the number of input images or the number of seconds in video or audio input files. However, the token count for each of these modalities will*correlate*with these values.
- The input token count includes the prompt (text and any input files) as well as any system instructions and tools.
- The output token count does not include any thinking tokens; those are provided in a separate field.
- Review the[additional information specific to each type of request](https://firebase.google.com/docs/ai-logic/count-tokens#additional-information)later on this page.
- Gemini Live APImodels do*not* support`countTokens`. Also,Firebase AI Logicdoes*not yet* support that`usageMetadata`attribute in the response fromLive APImodels, but it's coming soon!

### Pricing for these options

- Calling`countTokens`: There's no charge for calling`countTokens`(the Count Tokens API). The maximum quota for the Count Tokens API is 3000 requests per minute (RPM).

- Using the`usageMetadata`attribute: This attribute is always returned as part of the response and doesn't incur any tokens or charge itself.

## Additional information

Here's some additional information when working with specific types of requests.

### Count text input tokens

No additional information.

### Count multi-turn (chat) tokens

Note the following for calling`countTokens`when using chat:

- If you call`countTokens`with the chat history, it returns the total token count from both roles in the chat (`total_tokens`).
- To understand how big your next conversational turn will be, you need to append it to the history when you call`countTokens`.

### Count multimodal input tokens

Note the following points about counting tokens with multimodal input:

- You can optionally call`countTokens`on the text and the file separately.
- For both token counting options, you'll get the same token count whether you provide the file as inline data or using its URL.

#### Image input files

Image input files are converted to tokens based on their dimensions:

- Image inputs with*both*dimensions less than or equal to 384 pixels: each image is counted as 258 tokens.
- Image inputs that are larger in one or both dimensions: each image is cropped and scaled as needed into tiles of 768x768 pixels, and then each tile is counted as 258 tokens.

#### Video and audio input files

Video and audio input files are converted to tokens at the following fixed rates:

- Video: 263 tokens per second
- Audio: 32 tokens per second

#### Document (like PDFs) input files

PDF input files are treated as images, so each page of a PDF is tokenized in the same way as an image.