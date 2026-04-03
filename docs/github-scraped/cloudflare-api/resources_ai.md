# AI | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai

[API Reference]
# AI

##### [Execute AI model]
POST/accounts/{account_id}/ai/run/{model_name}
##### ModelsExpand Collapse
AIRunResponse = array of  { label, score }  or string or  { audio }  or 12 more
An array of classification results for the input text
One of the following:TextClassification = array of  { label, score }
An array of classification results for the input text
label: optional string
The classification label assigned to the text (e.g., ‘POSITIVE’ or ‘NEGATIVE’)
[]score: optional number
Confidence score indicating the likelihood that the text belongs to the specified label
[][]TextToImage = string
The generated image in PNG format
[]Audio  { audio } audio: optional string
The generated audio in MP3 format, base64-encoded
[][]string
The generated audio in MP3 format
[]TextEmbeddings  { data, shape } data: optional array of array of number
Embeddings of the requested text values
[]shape: optional array of number[][]AutomaticSpeechRecognition  { text, vtt, word_count, words } text: string
The transcription
[]vtt: optional string[]word_count: optional number[]words: optional array of  { end, start, word } end: optional number
The ending second when the word completes
[]start: optional number
The second this word begins in the recording
[]word: optional string[][][]ImageClassification = array of  { label, score } label: optional string
The predicted category or class for the input image based on analysis
[]score: optional number
A confidence value, between 0 and 1, indicating how certain the model is about the predicted label
[][]ObjectDetection = array of  { box, label, score }
An array of detected objects within the input image
box: optional  { xmax, xmin, ymax, ymin }
Coordinates defining the bounding box around the detected object
xmax: optional number
The x-coordinate of the bottom-right corner of the bounding box
[]xmin: optional number
The x-coordinate of the top-left corner of the bounding box
[]ymax: optional number
The y-coordinate of the bottom-right corner of the bounding box
[]ymin: optional number
The y-coordinate of the top-left corner of the bounding box
[][]label: optional string
The class label or name of the detected object
[]score: optional number
Confidence score indicating the likelihood that the detection is correct
[][] { response, tool_calls, usage } response: string
The generated text response from the model
[]tool_calls: optional array of  { arguments, name }
An array of tool calls requests made during the response generation
arguments: optional unknown
The arguments passed to be passed to the tool call request
[]name: optional string
The name of the tool to be called
[][]usage: optional  { completion_tokens, prompt_tokens, total_tokens }
Usage statistics for the inference request
completion_tokens: optional number
Total number of tokens in output
[]prompt_tokens: optional number
Total number of tokens in input
[]total_tokens: optional number
Total number of input and output tokens
[][][]string[]Translation  { translated_text } translated_text: optional string
The translated text in the target language
[][]Summarization  { summary } summary: optional string
The summarized version of the input text
[][]ImageToText  { description } description: optional string[][]ImageTextToText  { description } description: optional string[][]MultimodalEmbeddings  { data, shape } data: optional array of array of number[]shape: optional array of number[][][]
#### AIFinetunes

##### [List Finetunes]
GET/accounts/{account_id}/ai/finetunes
##### [Create a new Finetune]
POST/accounts/{account_id}/ai/finetunes
##### ModelsExpand Collapse
FinetuneListResponse  { id, created_at, model, 3 more } id: stringformatuuid[]created_at: stringformatdate-time[]model: string[]modified_at: stringformatdate-time[]name: string[]description: optional string[][]FinetuneCreateResponse  { id, created_at, model, 4 more } id: stringformatuuid[]created_at: stringformatdate-time[]model: string[]modified_at: stringformatdate-time[]name: string[]public: boolean[]description: optional string[][]
#### AIFinetunesAssets

##### [Upload a Finetune Asset]
POST/accounts/{account_id}/ai/finetunes/{finetune_id}/finetune-assets
##### ModelsExpand Collapse
AssetCreateResponse  { success } success: boolean[][]
#### AIFinetunesPublic

##### [List Public Finetunes]
GET/accounts/{account_id}/ai/finetunes/public
##### ModelsExpand Collapse
PublicListResponse  { id, created_at, model, 4 more } id: stringformatuuid[]created_at: stringformatdate-time[]model: string[]modified_at: stringformatdate-time[]name: string[]public: boolean[]description: optional string[][]
#### AIAuthors

##### [Author Search]
GET/accounts/{account_id}/ai/authors/search
##### ModelsExpand Collapse
AuthorListResponse = unknown[]
#### AITasks

##### [Task Search]
GET/accounts/{account_id}/ai/tasks/search
##### ModelsExpand Collapse
TaskListResponse = unknown[]
#### AIModels

##### [Model Search]
GET/accounts/{account_id}/ai/models/search
##### ModelsExpand Collapse
ModelListResponse = unknown[]
#### AIModelsSchema

##### [Get Model Schema]
GET/accounts/{account_id}/ai/models/schema
##### ModelsExpand Collapse
SchemaGetResponse  { input, output } input:  { additionalProperties, description, type } additionalProperties: boolean[]description: string[]type: string[][]output:  { additionalProperties, description, type } additionalProperties: boolean[]description: string[]type: string[][][]
#### AITo Markdown

##### [Convert Files into Markdown]
POST/accounts/{account_id}/ai/tomarkdown
##### [Get all converted formats supported]
GET/accounts/{account_id}/ai/tomarkdown/supported
##### ModelsExpand Collapse
ToMarkdownTransformResponse  { data, format, mimeType, 2 more } data: string[]format: string[]mimeType: string[]name: string[]tokens: string[][]ToMarkdownSupportedResponse  { extension, mimeType } extension: string[]mimeType: string[][]