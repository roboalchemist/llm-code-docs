# Source: https://firebase.google.com/docs/reference/js/ai.md.txt

# ai package

The Firebase AI Web SDK.

## Functions

| Function | Description |
|---|---|
| **function(app, ...)** |   |
| [getAI(app, options)](https://firebase.google.com/docs/reference/js/ai.md#getai_a94a413) | Returns the default [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with the default settings. |
| **function(ai, ...)** |   |
| [getGenerativeModel(ai, modelParams, requestOptions)](https://firebase.google.com/docs/reference/js/ai.md#getgenerativemodel_c63f46a) | Returns a [GenerativeModel](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodel_class) class with methods for inference and other functionality. |
| [getImagenModel(ai, modelParams, requestOptions)](https://firebase.google.com/docs/reference/js/ai.md#getimagenmodel_e1f6645) | Returns an [ImagenModel](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodel_class) class with methods for using Imagen.Only Imagen 3 models (named `imagen-3.0-*`) are supported. |
| [getLiveGenerativeModel(ai, modelParams)](https://firebase.google.com/docs/reference/js/ai.md#getlivegenerativemodel_f2099ac) | ***(Public Preview)*** Returns a [LiveGenerativeModel](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodel_class) class for real-time, bidirectional communication.The Live API is only supported in modern browser windows and Node \>= 22. |
| [getTemplateGenerativeModel(ai, requestOptions)](https://firebase.google.com/docs/reference/js/ai.md#gettemplategenerativemodel_9476bbc) | ***(Public Preview)*** Returns a [TemplateGenerativeModel](https://firebase.google.com/docs/reference/js/ai.templategenerativemodel.md#templategenerativemodel_class) class for executing server-side templates. |
| [getTemplateImagenModel(ai, requestOptions)](https://firebase.google.com/docs/reference/js/ai.md#gettemplateimagenmodel_9476bbc) | ***(Public Preview)*** Returns a [TemplateImagenModel](https://firebase.google.com/docs/reference/js/ai.templateimagenmodel.md#templateimagenmodel_class) class for executing server-side Imagen templates. |
| **function(liveSession, ...)** |   |
| [startAudioConversation(liveSession, options)](https://firebase.google.com/docs/reference/js/ai.md#startaudioconversation_01c8e7f) | ***(Public Preview)*** Starts a real-time, bidirectional audio conversation with the model. This helper function manages the complexities of microphone access, audio recording, playback, and interruptions. |

## Classes

| Class | Description |
|---|---|
| [AIError](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierror_class) | Error class for the Firebase AI SDK. |
| [AIModel](https://firebase.google.com/docs/reference/js/ai.aimodel.md#aimodel_class) | Base class for Firebase AI model APIs.Instances of this class are associated with a specific Firebase AI [Backend](https://firebase.google.com/docs/reference/js/ai.backend.md#backend_class) and provide methods for interacting with the configured generative model. |
| [AnyOfSchema](https://firebase.google.com/docs/reference/js/ai.anyofschema.md#anyofschema_class) | Schema class representing a value that can conform to any of the provided sub-schemas. This is useful when a field can accept multiple distinct types or structures. |
| [ArraySchema](https://firebase.google.com/docs/reference/js/ai.arrayschema.md#arrayschema_class) | Schema class for "array" types. The `items` param should refer to the type of item that can be a member of the array. |
| [Backend](https://firebase.google.com/docs/reference/js/ai.backend.md#backend_class) | Abstract base class representing the configuration for an AI service backend. This class should not be instantiated directly. Use its subclasses; [GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class) for the Gemini Developer API (via [Google AI](https://ai.google/)), and [VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class) for the Vertex AI Gemini API. |
| [BooleanSchema](https://firebase.google.com/docs/reference/js/ai.booleanschema.md#booleanschema_class) | Schema class for "boolean" types. |
| [ChatSession](https://firebase.google.com/docs/reference/js/ai.chatsession.md#chatsession_class) | ChatSession class that enables sending chat messages and stores history of sent and received messages so far. |
| [GenerativeModel](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodel_class) | Class for generative model APIs. |
| [GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class) | Configuration class for the Gemini Developer API.Use this with [AIOptions](https://firebase.google.com/docs/reference/js/ai.aioptions.md#aioptions_interface) when initializing the AI service via [getAI()](https://firebase.google.com/docs/reference/js/ai.md#getai_a94a413) to specify the Gemini Developer API as the backend. |
| [ImagenImageFormat](https://firebase.google.com/docs/reference/js/ai.imagenimageformat.md#imagenimageformat_class) | Defines the image format for images generated by Imagen.Use this class to specify the desired format (JPEG or PNG) and compression quality for images generated by Imagen. This is typically included as part of [ImagenModelParams](https://firebase.google.com/docs/reference/js/ai.imagenmodelparams.md#imagenmodelparams_interface). |
| [ImagenModel](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodel_class) | Class for Imagen model APIs.This class provides methods for generating images using the Imagen model. |
| [IntegerSchema](https://firebase.google.com/docs/reference/js/ai.integerschema.md#integerschema_class) | Schema class for "integer" types. |
| [LiveGenerativeModel](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodel_class) | ***(Public Preview)*** Class for Live generative model APIs. The Live API enables low-latency, two-way multimodal interactions with Gemini.This class should only be instantiated with [getLiveGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#getlivegenerativemodel_f2099ac). |
| [LiveSession](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesession_class) | ***(Public Preview)*** Represents an active, real-time, bidirectional conversation with the model.This class should only be instantiated by calling [LiveGenerativeModel.connect()](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodelconnect). |
| [NumberSchema](https://firebase.google.com/docs/reference/js/ai.numberschema.md#numberschema_class) | Schema class for "number" types. |
| [ObjectSchema](https://firebase.google.com/docs/reference/js/ai.objectschema.md#objectschema_class) | Schema class for "object" types. The `properties` param must be a map of `Schema` objects. |
| [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class) | Parent class encompassing all Schema types, with static methods that allow building specific Schema types. This class can be converted with `JSON.stringify()` into a JSON string accepted by Vertex AI REST endpoints. (This string conversion is automatically done when calling SDK methods.) |
| [StringSchema](https://firebase.google.com/docs/reference/js/ai.stringschema.md#stringschema_class) | Schema class for "string" types. Can be used with or without enum values. |
| [TemplateGenerativeModel](https://firebase.google.com/docs/reference/js/ai.templategenerativemodel.md#templategenerativemodel_class) | ***(Public Preview)*** [GenerativeModel](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodel_class) APIs that execute on a server-side template.This class should only be instantiated with [getTemplateGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#gettemplategenerativemodel_9476bbc). |
| [TemplateImagenModel](https://firebase.google.com/docs/reference/js/ai.templateimagenmodel.md#templateimagenmodel_class) | ***(Public Preview)*** Class for Imagen model APIs that execute on a server-side template.This class should only be instantiated with [getTemplateImagenModel()](https://firebase.google.com/docs/reference/js/ai.md#gettemplateimagenmodel_9476bbc). |
| [VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class) | Configuration class for the Vertex AI Gemini API.Use this with [AIOptions](https://firebase.google.com/docs/reference/js/ai.aioptions.md#aioptions_interface) when initializing the AI service via [getAI()](https://firebase.google.com/docs/reference/js/ai.md#getai_a94a413) to specify the Vertex AI Gemini API as the backend. |

## Interfaces

| Interface | Description |
|---|---|
| [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) | An instance of the Firebase AI SDK.Do not create this instance directly. Instead, use [getAI()](https://firebase.google.com/docs/reference/js/ai.md#getai_a94a413). |
| [AIOptions](https://firebase.google.com/docs/reference/js/ai.aioptions.md#aioptions_interface) | Options for initializing the AI service using [getAI()](https://firebase.google.com/docs/reference/js/ai.md#getai_a94a413). This allows specifying which backend to use (Vertex AI Gemini API or Gemini Developer API) and configuring its specific options (like location for Vertex AI). |
| [AudioConversationController](https://firebase.google.com/docs/reference/js/ai.audioconversationcontroller.md#audioconversationcontroller_interface) | ***(Public Preview)*** A controller for managing an active audio conversation. |
| [AudioTranscriptionConfig](https://firebase.google.com/docs/reference/js/ai.audiotranscriptionconfig.md#audiotranscriptionconfig_interface) | The audio transcription configuration. |
| [BaseParams](https://firebase.google.com/docs/reference/js/ai.baseparams.md#baseparams_interface) | Base parameters for a number of methods. |
| [ChromeAdapter](https://firebase.google.com/docs/reference/js/ai.chromeadapter.md#chromeadapter_interface) | ***(Public Preview)*** Defines an inference "backend" that uses Chrome's on-device model, and encapsulates logic for detecting when on-device inference is possible.These methods should not be called directly by the user. |
| [Citation](https://firebase.google.com/docs/reference/js/ai.citation.md#citation_interface) | A single citation. |
| [CitationMetadata](https://firebase.google.com/docs/reference/js/ai.citationmetadata.md#citationmetadata_interface) | Citation metadata that may be found on a [GenerateContentCandidate](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidate_interface). |
| [CodeExecutionResult](https://firebase.google.com/docs/reference/js/ai.codeexecutionresult.md#codeexecutionresult_interface) | The results of code execution run by the model. |
| [CodeExecutionResultPart](https://firebase.google.com/docs/reference/js/ai.codeexecutionresultpart.md#codeexecutionresultpart_interface) | Represents the code execution result from the model. |
| [CodeExecutionTool](https://firebase.google.com/docs/reference/js/ai.codeexecutiontool.md#codeexecutiontool_interface) | ***(Public Preview)*** A tool that enables the model to use code execution. |
| [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) | Content type for both prompts and response candidates. |
| [CountTokensRequest](https://firebase.google.com/docs/reference/js/ai.counttokensrequest.md#counttokensrequest_interface) | Params for calling [GenerativeModel.countTokens()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelcounttokens) |
| [CountTokensResponse](https://firebase.google.com/docs/reference/js/ai.counttokensresponse.md#counttokensresponse_interface) | Response from calling [GenerativeModel.countTokens()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelcounttokens). |
| [CustomErrorData](https://firebase.google.com/docs/reference/js/ai.customerrordata.md#customerrordata_interface) | Details object that contains data originating from a bad HTTP response. |
| [Date_2](https://firebase.google.com/docs/reference/js/ai.date_2.md#date_2_interface) | Protobuf google.type.Date |
| [EnhancedGenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.enhancedgeneratecontentresponse.md#enhancedgeneratecontentresponse_interface) | Response object wrapped with helper methods. |
| [ErrorDetails](https://firebase.google.com/docs/reference/js/ai.errordetails.md#errordetails_interface) | Details object that may be included in an error response. |
| [ExecutableCode](https://firebase.google.com/docs/reference/js/ai.executablecode.md#executablecode_interface) | An interface for executable code returned by the model. |
| [ExecutableCodePart](https://firebase.google.com/docs/reference/js/ai.executablecodepart.md#executablecodepart_interface) | Represents the code that is executed by the model. |
| [FileData](https://firebase.google.com/docs/reference/js/ai.filedata.md#filedata_interface) | Data pointing to a file uploaded on Google Cloud Storage. |
| [FileDataPart](https://firebase.google.com/docs/reference/js/ai.filedatapart.md#filedatapart_interface) | Content part interface if the part represents [FileData](https://firebase.google.com/docs/reference/js/ai.filedata.md#filedata_interface) |
| [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface) | A predicted [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface) returned from the model that contains a string representing the [FunctionDeclaration.name](https://firebase.google.com/docs/reference/js/ai.functiondeclaration.md#functiondeclarationname) and a structured JSON object containing the parameters and their values. |
| [FunctionCallingConfig](https://firebase.google.com/docs/reference/js/ai.functioncallingconfig.md#functioncallingconfig_interface) |   |
| [FunctionCallPart](https://firebase.google.com/docs/reference/js/ai.functioncallpart.md#functioncallpart_interface) | Content part interface if the part represents a [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface). |
| [FunctionDeclaration](https://firebase.google.com/docs/reference/js/ai.functiondeclaration.md#functiondeclaration_interface) | Structured representation of a function declaration as defined by the [OpenAPI 3.0 specification](https://spec.openapis.org/oas/v3.0.3). Included in this declaration are the function name and parameters. This `FunctionDeclaration` is a representation of a block of code that can be used as a Tool by the model and executed by the client. |
| [FunctionDeclarationsTool](https://firebase.google.com/docs/reference/js/ai.functiondeclarationstool.md#functiondeclarationstool_interface) | A `FunctionDeclarationsTool` is a piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model. |
| [FunctionResponse](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponse_interface) | The result output from a [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface) that contains a string representing the [FunctionDeclaration.name](https://firebase.google.com/docs/reference/js/ai.functiondeclaration.md#functiondeclarationname) and a structured JSON object containing any output from the function is used as context to the model. This should contain the result of a [FunctionCall](https://firebase.google.com/docs/reference/js/ai.functioncall.md#functioncall_interface) made based on model prediction. |
| [FunctionResponsePart](https://firebase.google.com/docs/reference/js/ai.functionresponsepart.md#functionresponsepart_interface) | Content part interface if the part represents [FunctionResponse](https://firebase.google.com/docs/reference/js/ai.functionresponse.md#functionresponse_interface). |
| [GenerateContentCandidate](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidate_interface) | A candidate returned as part of a [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface). |
| [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface) | Request sent through [GenerativeModel.generateContent()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontent) |
| [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface) | Individual response from [GenerativeModel.generateContent()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontent) and [GenerativeModel.generateContentStream()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontentstream). `generateContentStream()` will return one in each chunk until the stream is done. |
| [GenerateContentResult](https://firebase.google.com/docs/reference/js/ai.generatecontentresult.md#generatecontentresult_interface) | Result object returned from [GenerativeModel.generateContent()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontent) call. |
| [GenerateContentStreamResult](https://firebase.google.com/docs/reference/js/ai.generatecontentstreamresult.md#generatecontentstreamresult_interface) | Result object returned from [GenerativeModel.generateContentStream()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelgeneratecontentstream) call. Iterate over `stream` to get chunks as they come in and/or use the `response` promise to get the aggregated response when the stream is done. |
| [GenerationConfig](https://firebase.google.com/docs/reference/js/ai.generationconfig.md#generationconfig_interface) | Config options for content-related requests |
| [GenerativeContentBlob](https://firebase.google.com/docs/reference/js/ai.generativecontentblob.md#generativecontentblob_interface) | Interface for sending an image. |
| [GoogleSearch](https://firebase.google.com/docs/reference/js/ai.googlesearch.md#googlesearch_interface) | Specifies the Google Search configuration. |
| [GoogleSearchTool](https://firebase.google.com/docs/reference/js/ai.googlesearchtool.md#googlesearchtool_interface) | A tool that allows a Gemini model to connect to Google Search to access and incorporate up-to-date information from the web into its responses.Important: If using Grounding with Google Search, you are required to comply with the "Grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms). |
| [GroundingChunk](https://firebase.google.com/docs/reference/js/ai.groundingchunk.md#groundingchunk_interface) | Represents a chunk of retrieved data that supports a claim in the model's response. This is part of the grounding information provided when grounding is enabled. |
| [GroundingMetadata](https://firebase.google.com/docs/reference/js/ai.groundingmetadata.md#groundingmetadata_interface) | Metadata returned when grounding is enabled.Currently, only Grounding with Google Search is supported (see [GoogleSearchTool](https://firebase.google.com/docs/reference/js/ai.googlesearchtool.md#googlesearchtool_interface)).Important: If using Grounding with Google Search, you are required to comply with the "Grounding with Google Search" usage requirements for your chosen API provider: [Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search) or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms) section within the Service Specific Terms). |
| [GroundingSupport](https://firebase.google.com/docs/reference/js/ai.groundingsupport.md#groundingsupport_interface) | Provides information about how a specific segment of the model's response is supported by the retrieved grounding chunks. |
| [HybridParams](https://firebase.google.com/docs/reference/js/ai.hybridparams.md#hybridparams_interface) | ***(Public Preview)*** Configures hybrid inference. |
| [ImagenGCSImage](https://firebase.google.com/docs/reference/js/ai.imagengcsimage.md#imagengcsimage_interface) | An image generated by Imagen, stored in a Cloud Storage for Firebase bucket.This feature is not available yet. |
| [ImagenGenerationConfig](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfig_interface) | Configuration options for generating images with Imagen.See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images-imagen) for more details. |
| [ImagenGenerationResponse](https://firebase.google.com/docs/reference/js/ai.imagengenerationresponse.md#imagengenerationresponse_interface) | The response from a request to generate images with Imagen. |
| [ImagenInlineImage](https://firebase.google.com/docs/reference/js/ai.imageninlineimage.md#imageninlineimage_interface) | An image generated by Imagen, represented as inline data. |
| [ImagenModelParams](https://firebase.google.com/docs/reference/js/ai.imagenmodelparams.md#imagenmodelparams_interface) | Parameters for configuring an [ImagenModel](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodel_class). |
| [ImagenSafetySettings](https://firebase.google.com/docs/reference/js/ai.imagensafetysettings.md#imagensafetysettings_interface) | Settings for controlling the aggressiveness of filtering out sensitive content.See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) for more details. |
| [InlineDataPart](https://firebase.google.com/docs/reference/js/ai.inlinedatapart.md#inlinedatapart_interface) | Content part interface if the part represents an image. |
| [LanguageModelCreateCoreOptions](https://firebase.google.com/docs/reference/js/ai.languagemodelcreatecoreoptions.md#languagemodelcreatecoreoptions_interface) | ***(Public Preview)*** Configures the creation of an on-device language model session. |
| [LanguageModelCreateOptions](https://firebase.google.com/docs/reference/js/ai.languagemodelcreateoptions.md#languagemodelcreateoptions_interface) | ***(Public Preview)*** Configures the creation of an on-device language model session. |
| [LanguageModelExpected](https://firebase.google.com/docs/reference/js/ai.languagemodelexpected.md#languagemodelexpected_interface) | ***(Public Preview)*** Options for the expected inputs for an on-device language model. |
| [LanguageModelMessage](https://firebase.google.com/docs/reference/js/ai.languagemodelmessage.md#languagemodelmessage_interface) | ***(Public Preview)*** An on-device language model message. |
| [LanguageModelMessageContent](https://firebase.google.com/docs/reference/js/ai.languagemodelmessagecontent.md#languagemodelmessagecontent_interface) | ***(Public Preview)*** An on-device language model content object. |
| [LanguageModelPromptOptions](https://firebase.google.com/docs/reference/js/ai.languagemodelpromptoptions.md#languagemodelpromptoptions_interface) | ***(Public Preview)*** Options for an on-device language model prompt. |
| [LiveGenerationConfig](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfig_interface) | ***(Public Preview)*** Configuration parameters used by [LiveGenerativeModel](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodel_class) to control live content generation. |
| [LiveModelParams](https://firebase.google.com/docs/reference/js/ai.livemodelparams.md#livemodelparams_interface) | ***(Public Preview)*** Params passed to [getLiveGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#getlivegenerativemodel_f2099ac). |
| [LiveServerContent](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontent_interface) | ***(Public Preview)*** An incremental content update from the model. |
| [LiveServerGoingAwayNotice](https://firebase.google.com/docs/reference/js/ai.liveservergoingawaynotice.md#liveservergoingawaynotice_interface) | ***(Public Preview)*** Notification that the server will not be able to service the client soon. |
| [LiveServerToolCall](https://firebase.google.com/docs/reference/js/ai.liveservertoolcall.md#liveservertoolcall_interface) | ***(Public Preview)*** A request from the model for the client to execute one or more functions. |
| [LiveServerToolCallCancellation](https://firebase.google.com/docs/reference/js/ai.liveservertoolcallcancellation.md#liveservertoolcallcancellation_interface) | ***(Public Preview)*** Notification to cancel a previous function call triggered by [LiveServerToolCall](https://firebase.google.com/docs/reference/js/ai.liveservertoolcall.md#liveservertoolcall_interface). |
| [ModalityTokenCount](https://firebase.google.com/docs/reference/js/ai.modalitytokencount.md#modalitytokencount_interface) | Represents token counting info for a single modality. |
| [ModelParams](https://firebase.google.com/docs/reference/js/ai.modelparams.md#modelparams_interface) | Params passed to [getGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#getgenerativemodel_c63f46a). |
| [ObjectSchemaRequest](https://firebase.google.com/docs/reference/js/ai.objectschemarequest.md#objectschemarequest_interface) | Interface for JSON parameters in a schema of [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) "object" when not using the `Schema.object()` helper. |
| [OnDeviceParams](https://firebase.google.com/docs/reference/js/ai.ondeviceparams.md#ondeviceparams_interface) | ***(Public Preview)*** Encapsulates configuration for on-device inference. |
| [PrebuiltVoiceConfig](https://firebase.google.com/docs/reference/js/ai.prebuiltvoiceconfig.md#prebuiltvoiceconfig_interface) | ***(Public Preview)*** Configuration for a pre-built voice. |
| [PromptFeedback](https://firebase.google.com/docs/reference/js/ai.promptfeedback.md#promptfeedback_interface) | If the prompt was blocked, this will be populated with `blockReason` and the relevant `safetyRatings`. |
| [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) | Params passed to [getGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#getgenerativemodel_c63f46a). |
| [RetrievedContextAttribution](https://firebase.google.com/docs/reference/js/ai.retrievedcontextattribution.md#retrievedcontextattribution_interface) |   |
| [SafetyRating](https://firebase.google.com/docs/reference/js/ai.safetyrating.md#safetyrating_interface) | A safety rating associated with a [GenerateContentCandidate](https://firebase.google.com/docs/reference/js/ai.generatecontentcandidate.md#generatecontentcandidate_interface) |
| [SafetySetting](https://firebase.google.com/docs/reference/js/ai.safetysetting.md#safetysetting_interface) | Safety setting that can be sent as part of request parameters. |
| [SchemaInterface](https://firebase.google.com/docs/reference/js/ai.schemainterface.md#schemainterface_interface) | Interface for [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class) class. |
| [SchemaParams](https://firebase.google.com/docs/reference/js/ai.schemaparams.md#schemaparams_interface) | Params passed to [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class) static methods to create specific [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class) classes. |
| [SchemaRequest](https://firebase.google.com/docs/reference/js/ai.schemarequest.md#schemarequest_interface) | Final format for [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class) params passed to backend requests. |
| [SchemaShared](https://firebase.google.com/docs/reference/js/ai.schemashared.md#schemashared_interface) | Basic [Schema](https://firebase.google.com/docs/reference/js/ai.schema.md#schema_class) properties shared across several Schema-related types. |
| [SearchEntrypoint](https://firebase.google.com/docs/reference/js/ai.searchentrypoint.md#searchentrypoint_interface) | Google search entry point. |
| [Segment](https://firebase.google.com/docs/reference/js/ai.segment.md#segment_interface) | Represents a specific segment within a [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface) object, often used to pinpoint the exact location of text or data that grounding information refers to. |
| [SingleRequestOptions](https://firebase.google.com/docs/reference/js/ai.singlerequestoptions.md#singlerequestoptions_interface) | Options that can be provided per-request. Extends the base [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) (like `timeout` and `baseUrl`) with request-specific controls like cancellation via `AbortSignal`.Options specified here will override any default [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) configured on a model (for example, [GenerativeModel](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodel_class)). |
| [SpeechConfig](https://firebase.google.com/docs/reference/js/ai.speechconfig.md#speechconfig_interface) | ***(Public Preview)*** Configures speech synthesis. |
| [StartAudioConversationOptions](https://firebase.google.com/docs/reference/js/ai.startaudioconversationoptions.md#startaudioconversationoptions_interface) | ***(Public Preview)*** Options for [startAudioConversation()](https://firebase.google.com/docs/reference/js/ai.md#startaudioconversation_01c8e7f). |
| [StartChatParams](https://firebase.google.com/docs/reference/js/ai.startchatparams.md#startchatparams_interface) | Params for [GenerativeModel.startChat()](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodelstartchat). |
| [TextPart](https://firebase.google.com/docs/reference/js/ai.textpart.md#textpart_interface) | Content part interface if the part represents a text string. |
| [ThinkingConfig](https://firebase.google.com/docs/reference/js/ai.thinkingconfig.md#thinkingconfig_interface) | Configuration for "thinking" behavior of compatible Gemini models.Certain models utilize a thinking process before generating a response. This allows them to reason through complex problems and plan a more coherent and accurate answer. |
| [ToolConfig](https://firebase.google.com/docs/reference/js/ai.toolconfig.md#toolconfig_interface) | Tool config. This config is shared for all tools provided in the request. |
| [Transcription](https://firebase.google.com/docs/reference/js/ai.transcription.md#transcription_interface) | ***(Public Preview)*** Transcription of audio. This can be returned from a [LiveGenerativeModel](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodel_class) if transcription is enabled with the `inputAudioTranscription` or `outputAudioTranscription` properties on the [LiveGenerationConfig](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfig_interface). |
| [URLContext](https://firebase.google.com/docs/reference/js/ai.urlcontext.md#urlcontext_interface) | ***(Public Preview)*** Specifies the URL Context configuration. |
| [URLContextMetadata](https://firebase.google.com/docs/reference/js/ai.urlcontextmetadata.md#urlcontextmetadata_interface) | Metadata related to [URLContextTool](https://firebase.google.com/docs/reference/js/ai.urlcontexttool.md#urlcontexttool_interface). |
| [URLContextTool](https://firebase.google.com/docs/reference/js/ai.urlcontexttool.md#urlcontexttool_interface) | ***(Public Preview)*** A tool that allows you to provide additional context to the models in the form of public web URLs. By including URLs in your request, the Gemini model will access the content from those pages to inform and enhance its response. |
| [URLMetadata](https://firebase.google.com/docs/reference/js/ai.urlmetadata.md#urlmetadata_interface) | Metadata for a single URL retrieved by the [URLContextTool](https://firebase.google.com/docs/reference/js/ai.urlcontexttool.md#urlcontexttool_interface) tool. |
| [UsageMetadata](https://firebase.google.com/docs/reference/js/ai.usagemetadata.md#usagemetadata_interface) | Usage metadata about a [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface). |
| [VideoMetadata](https://firebase.google.com/docs/reference/js/ai.videometadata.md#videometadata_interface) | Describes the input video content. |
| [VoiceConfig](https://firebase.google.com/docs/reference/js/ai.voiceconfig.md#voiceconfig_interface) | ***(Public Preview)*** Configuration for the voice to used in speech synthesis. |
| [WebAttribution](https://firebase.google.com/docs/reference/js/ai.webattribution.md#webattribution_interface) |   |
| [WebGroundingChunk](https://firebase.google.com/docs/reference/js/ai.webgroundingchunk.md#webgroundingchunk_interface) | A grounding chunk from the web.Important: If using Grounding with Google Search, you are required to comply with the [Service Specific Terms](https://cloud.google.com/terms/service-terms) for "Grounding with Google Search". |

## Variables

| Variable | Description |
|---|---|
| [AIErrorCode](https://firebase.google.com/docs/reference/js/ai.md#aierrorcode) | Standardized error codes that [AIError](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierror_class) can have. |
| [BackendType](https://firebase.google.com/docs/reference/js/ai.md#backendtype) | An enum-like object containing constants that represent the supported backends for the Firebase AI SDK. This determines which backend service (Vertex AI Gemini API or Gemini Developer API) the SDK will communicate with.These values are assigned to the `backendType` property within the specific backend configuration objects ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class) or [VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)) to identify which service to target. |
| [BlockReason](https://firebase.google.com/docs/reference/js/ai.md#blockreason) | Reason that a prompt was blocked. |
| [FinishReason](https://firebase.google.com/docs/reference/js/ai.md#finishreason) | Reason that a candidate finished. |
| [FunctionCallingMode](https://firebase.google.com/docs/reference/js/ai.md#functioncallingmode) |   |
| [HarmBlockMethod](https://firebase.google.com/docs/reference/js/ai.md#harmblockmethod) | This property is not supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)). |
| [HarmBlockThreshold](https://firebase.google.com/docs/reference/js/ai.md#harmblockthreshold) | Threshold above which a prompt or candidate will be blocked. |
| [HarmCategory](https://firebase.google.com/docs/reference/js/ai.md#harmcategory) | Harm categories that would cause prompts or candidates to be blocked. |
| [HarmProbability](https://firebase.google.com/docs/reference/js/ai.md#harmprobability) | Probability that a prompt or candidate matches a harm category. |
| [HarmSeverity](https://firebase.google.com/docs/reference/js/ai.md#harmseverity) | Harm severity levels. |
| [ImagenAspectRatio](https://firebase.google.com/docs/reference/js/ai.md#imagenaspectratio) | Aspect ratios for Imagen images.To specify an aspect ratio for generated images, set the `aspectRatio` property in your [ImagenGenerationConfig](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfig_interface).See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) for more details and examples of the supported aspect ratios. |
| [ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/js/ai.md#imagenpersonfilterlevel) | A filter level controlling whether generation of images containing people or faces is allowed.See the [personGeneration](http://firebase.google.com/docs/vertex-ai/generate-images) documentation for more details. |
| [ImagenSafetyFilterLevel](https://firebase.google.com/docs/reference/js/ai.md#imagensafetyfilterlevel) | A filter level controlling how aggressively to filter sensitive content.Text prompts provided as inputs and images (generated or uploaded) through Imagen on Vertex AI are assessed against a list of safety filters, which include 'harmful categories' (for example, `violence`, `sexual`, `derogatory`, and `toxic`). This filter level controls how aggressively to filter out potentially harmful content from responses. See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) and the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-filters) for more details. |
| [InferenceMode](https://firebase.google.com/docs/reference/js/ai.md#inferencemode) | ***(Public Preview)*** Determines whether inference happens on-device or in-cloud. |
| [InferenceSource](https://firebase.google.com/docs/reference/js/ai.md#inferencesource) | ***(Public Preview)*** Indicates whether inference happened on-device or in-cloud. |
| [Language](https://firebase.google.com/docs/reference/js/ai.md#language) | The programming language of the code. |
| [LiveResponseType](https://firebase.google.com/docs/reference/js/ai.md#liveresponsetype) | ***(Public Preview)*** The types of responses that can be returned by [LiveSession.receive()](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionreceive). |
| [Modality](https://firebase.google.com/docs/reference/js/ai.md#modality) | Content part modality. |
| [Outcome](https://firebase.google.com/docs/reference/js/ai.md#outcome) | Represents the result of the code execution. |
| [POSSIBLE_ROLES](https://firebase.google.com/docs/reference/js/ai.md#possible_roles) | Possible roles. |
| [ResponseModality](https://firebase.google.com/docs/reference/js/ai.md#responsemodality) | ***(Public Preview)*** Generation modalities to be returned in generation responses. |
| [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) | Contains the list of OpenAPI data types as defined by the [OpenAPI specification](https://swagger.io/docs/specification/data-models/data-types/) |
| [ThinkingLevel](https://firebase.google.com/docs/reference/js/ai.md#thinkinglevel) | A preset that controls the model's "thinking" process. Use `ThinkingLevel.LOW` for faster responses on less complex tasks, and `ThinkingLevel.HIGH` for better reasoning on more complex tasks. |
| [URLRetrievalStatus](https://firebase.google.com/docs/reference/js/ai.md#urlretrievalstatus) | The status of a URL retrieval. |

## Type Aliases

| Type Alias | Description |
|---|---|
| [AIErrorCode](https://firebase.google.com/docs/reference/js/ai.md#aierrorcode) | Standardized error codes that [AIError](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierror_class) can have. |
| [BackendType](https://firebase.google.com/docs/reference/js/ai.md#backendtype) | Type alias representing valid backend types. It can be either `'VERTEX_AI'` or `'GOOGLE_AI'`. |
| [BlockReason](https://firebase.google.com/docs/reference/js/ai.md#blockreason) | Reason that a prompt was blocked. |
| [FinishReason](https://firebase.google.com/docs/reference/js/ai.md#finishreason) | Reason that a candidate finished. |
| [FunctionCallingMode](https://firebase.google.com/docs/reference/js/ai.md#functioncallingmode) |   |
| [HarmBlockMethod](https://firebase.google.com/docs/reference/js/ai.md#harmblockmethod) | This property is not supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)). |
| [HarmBlockThreshold](https://firebase.google.com/docs/reference/js/ai.md#harmblockthreshold) | Threshold above which a prompt or candidate will be blocked. |
| [HarmCategory](https://firebase.google.com/docs/reference/js/ai.md#harmcategory) | Harm categories that would cause prompts or candidates to be blocked. |
| [HarmProbability](https://firebase.google.com/docs/reference/js/ai.md#harmprobability) | Probability that a prompt or candidate matches a harm category. |
| [HarmSeverity](https://firebase.google.com/docs/reference/js/ai.md#harmseverity) | Harm severity levels. |
| [ImagenAspectRatio](https://firebase.google.com/docs/reference/js/ai.md#imagenaspectratio) | Aspect ratios for Imagen images.To specify an aspect ratio for generated images, set the `aspectRatio` property in your [ImagenGenerationConfig](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfig_interface).See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) for more details and examples of the supported aspect ratios. |
| [ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/js/ai.md#imagenpersonfilterlevel) | A filter level controlling whether generation of images containing people or faces is allowed.See the [personGeneration](http://firebase.google.com/docs/vertex-ai/generate-images) documentation for more details. |
| [ImagenSafetyFilterLevel](https://firebase.google.com/docs/reference/js/ai.md#imagensafetyfilterlevel) | A filter level controlling how aggressively to filter sensitive content.Text prompts provided as inputs and images (generated or uploaded) through Imagen on Vertex AI are assessed against a list of safety filters, which include 'harmful categories' (for example, `violence`, `sexual`, `derogatory`, and `toxic`). This filter level controls how aggressively to filter out potentially harmful content from responses. See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) and the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-filters) for more details. |
| [InferenceMode](https://firebase.google.com/docs/reference/js/ai.md#inferencemode) | ***(Public Preview)*** Determines whether inference happens on-device or in-cloud. |
| [InferenceSource](https://firebase.google.com/docs/reference/js/ai.md#inferencesource) | ***(Public Preview)*** Indicates whether inference happened on-device or in-cloud. |
| [Language](https://firebase.google.com/docs/reference/js/ai.md#language) | The programming language of the code. |
| [LanguageModelMessageContentValue](https://firebase.google.com/docs/reference/js/ai.md#languagemodelmessagecontentvalue) | ***(Public Preview)*** Content formats that can be provided as on-device message content. |
| [LanguageModelMessageRole](https://firebase.google.com/docs/reference/js/ai.md#languagemodelmessagerole) | ***(Public Preview)*** Allowable roles for on-device language model usage. |
| [LanguageModelMessageType](https://firebase.google.com/docs/reference/js/ai.md#languagemodelmessagetype) | ***(Public Preview)*** Allowable types for on-device language model messages. |
| [LiveResponseType](https://firebase.google.com/docs/reference/js/ai.md#liveresponsetype) | ***(Public Preview)*** The types of responses that can be returned by [LiveSession.receive()](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionreceive). This is a property on all messages that can be used for type narrowing. This property is not returned by the server, it is assigned to a server message object once it's parsed. |
| [Modality](https://firebase.google.com/docs/reference/js/ai.md#modality) | Content part modality. |
| [Outcome](https://firebase.google.com/docs/reference/js/ai.md#outcome) | Represents the result of the code execution. |
| [Part](https://firebase.google.com/docs/reference/js/ai.md#part) | Content part - includes text, image/video, or function call/response part types. |
| [ResponseModality](https://firebase.google.com/docs/reference/js/ai.md#responsemodality) | ***(Public Preview)*** Generation modalities to be returned in generation responses. |
| [Role](https://firebase.google.com/docs/reference/js/ai.md#role) | Role is the producer of the content. |
| [SchemaType](https://firebase.google.com/docs/reference/js/ai.md#schematype) | Contains the list of OpenAPI data types as defined by the [OpenAPI specification](https://swagger.io/docs/specification/data-models/data-types/) |
| [ThinkingLevel](https://firebase.google.com/docs/reference/js/ai.md#thinkinglevel) | A preset that controls the model's "thinking" process. Use `ThinkingLevel.LOW` for faster responses on less complex tasks, and `ThinkingLevel.HIGH` for better reasoning on more complex tasks. |
| [Tool](https://firebase.google.com/docs/reference/js/ai.md#tool) | Defines a tool that model can call to access external knowledge. |
| [TypedSchema](https://firebase.google.com/docs/reference/js/ai.md#typedschema) | A type that includes all specific Schema types. |
| [URLRetrievalStatus](https://firebase.google.com/docs/reference/js/ai.md#urlretrievalstatus) | The status of a URL retrieval. |

## function(app, ...)

### getAI(app, options)

Returns the default [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with the default settings.

**Signature:**

    export declare function getAI(app?: FirebaseApp, options?: AIOptions): AI;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) to use. |
| options | [AIOptions](https://firebase.google.com/docs/reference/js/ai.aioptions.md#aioptions_interface) | [AIOptions](https://firebase.google.com/docs/reference/js/ai.aioptions.md#aioptions_interface) that configure the AI instance. |

**Returns:**

[AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface)

The default [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) instance for the given [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface).

### Example 1

    const ai = getAI(app);

### Example 2

    // Get an AI instance configured to use the Gemini Developer API (via Google AI).
    const ai = getAI(app, { backend: new GoogleAIBackend() });

### Example 3

    // Get an AI instance configured to use the Vertex AI Gemini API.
    const ai = getAI(app, { backend: new VertexAIBackend() });

## function(ai, ...)

### getGenerativeModel(ai, modelParams, requestOptions)

Returns a [GenerativeModel](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodel_class) class with methods for inference and other functionality.

**Signature:**

    export declare function getGenerativeModel(ai: AI, modelParams: ModelParams | HybridParams, requestOptions?: RequestOptions): GenerativeModel;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ai | [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) |   |
| modelParams | [ModelParams](https://firebase.google.com/docs/reference/js/ai.modelparams.md#modelparams_interface) \| [HybridParams](https://firebase.google.com/docs/reference/js/ai.hybridparams.md#hybridparams_interface) |   |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) |   |

**Returns:**

[GenerativeModel](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodel_class)

### getImagenModel(ai, modelParams, requestOptions)

Returns an [ImagenModel](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodel_class) class with methods for using Imagen.

Only Imagen 3 models (named `imagen-3.0-*`) are supported.

**Signature:**

    export declare function getImagenModel(ai: AI, modelParams: ImagenModelParams, requestOptions?: RequestOptions): ImagenModel;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ai | [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) | An [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) instance. |
| modelParams | [ImagenModelParams](https://firebase.google.com/docs/reference/js/ai.imagenmodelparams.md#imagenmodelparams_interface) | Parameters to use when making Imagen requests. |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) | Additional options to use when making requests. |

**Returns:**

[ImagenModel](https://firebase.google.com/docs/reference/js/ai.imagenmodel.md#imagenmodel_class)

#### Exceptions

If the `apiKey` or `projectId` fields are missing in your Firebase config.

### getLiveGenerativeModel(ai, modelParams)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns a [LiveGenerativeModel](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodel_class) class for real-time, bidirectional communication.

The Live API is only supported in modern browser windows and Node \>= 22.

**Signature:**

    export declare function getLiveGenerativeModel(ai: AI, modelParams: LiveModelParams): LiveGenerativeModel;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ai | [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) | An [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) instance. |
| modelParams | [LiveModelParams](https://firebase.google.com/docs/reference/js/ai.livemodelparams.md#livemodelparams_interface) | Parameters to use when setting up a [LiveSession](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesession_class). |

**Returns:**

[LiveGenerativeModel](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodel_class)

#### Exceptions

If the `apiKey` or `projectId` fields are missing in your Firebase config.

### getTemplateGenerativeModel(ai, requestOptions)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns a [TemplateGenerativeModel](https://firebase.google.com/docs/reference/js/ai.templategenerativemodel.md#templategenerativemodel_class) class for executing server-side templates.

**Signature:**

    export declare function getTemplateGenerativeModel(ai: AI, requestOptions?: RequestOptions): TemplateGenerativeModel;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ai | [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) | An [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) instance. |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) | Additional options to use when making requests. |

**Returns:**

[TemplateGenerativeModel](https://firebase.google.com/docs/reference/js/ai.templategenerativemodel.md#templategenerativemodel_class)

### getTemplateImagenModel(ai, requestOptions)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns a [TemplateImagenModel](https://firebase.google.com/docs/reference/js/ai.templateimagenmodel.md#templateimagenmodel_class) class for executing server-side Imagen templates.

**Signature:**

    export declare function getTemplateImagenModel(ai: AI, requestOptions?: RequestOptions): TemplateImagenModel;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ai | [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) | An [AI](https://firebase.google.com/docs/reference/js/ai.ai.md#ai_interface) instance. |
| requestOptions | [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) | Additional options to use when making requests. |

**Returns:**

[TemplateImagenModel](https://firebase.google.com/docs/reference/js/ai.templateimagenmodel.md#templateimagenmodel_class)

## function(liveSession, ...)

### startAudioConversation(liveSession, options)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Starts a real-time, bidirectional audio conversation with the model. This helper function manages the complexities of microphone access, audio recording, playback, and interruptions.

> [!IMPORTANT]
> **Important:** This function must be called in response to a user gesture (for example, a button click) to comply with [browser autoplay policies](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices#autoplay_policy).

**Signature:**

    export declare function startAudioConversation(liveSession: LiveSession, options?: StartAudioConversationOptions): Promise<AudioConversationController>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| liveSession | [LiveSession](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesession_class) | An active [LiveSession](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesession_class) instance. |
| options | [StartAudioConversationOptions](https://firebase.google.com/docs/reference/js/ai.startaudioconversationoptions.md#startaudioconversationoptions_interface) | Configuration options for the audio conversation. |

**Returns:**

Promise\<[AudioConversationController](https://firebase.google.com/docs/reference/js/ai.audioconversationcontroller.md#audioconversationcontroller_interface)\>

A `Promise` that resolves with an [AudioConversationController](https://firebase.google.com/docs/reference/js/ai.audioconversationcontroller.md#audioconversationcontroller_interface).

#### Exceptions

`AIError` if the environment does not support required Web APIs (`UNSUPPORTED`), if a conversation is already active (`REQUEST_ERROR`), the session is closed (`SESSION_CLOSED`), or if an unexpected initialization error occurs (`ERROR`).

`DOMException` Thrown by `navigator.mediaDevices.getUserMedia()` if issues occur with microphone access, such as permissions being denied (`NotAllowedError`) or no compatible hardware being found (`NotFoundError`). See the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions) for a full list of exceptions.

### Example

    const liveSession = await model.connect();
    let conversationController;

    // This function must be called from within a click handler.
    async function startConversation() {
      try {
        conversationController = await startAudioConversation(liveSession);
      } catch (e) {
        // Handle AI-specific errors
        if (e instanceof AIError) {
          console.error("AI Error:", e.message);
        }
        // Handle microphone permission and hardware errors
        else if (e instanceof DOMException) {
          console.error("Microphone Error:", e.message);
        }
        // Handle other unexpected errors
        else {
          console.error("An unexpected error occurred:", e);
        }
      }
    }

    // Later, to stop the conversation:
    // if (conversationController) {
    //   await conversationController.stop();
    // }

## AIErrorCode

Standardized error codes that [AIError](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierror_class) can have.

**Signature:**

    AIErrorCode: {
        readonly ERROR: "error";
        readonly REQUEST_ERROR: "request-error";
        readonly RESPONSE_ERROR: "response-error";
        readonly FETCH_ERROR: "fetch-error";
        readonly SESSION_CLOSED: "session-closed";
        readonly INVALID_CONTENT: "invalid-content";
        readonly API_NOT_ENABLED: "api-not-enabled";
        readonly INVALID_SCHEMA: "invalid-schema";
        readonly NO_API_KEY: "no-api-key";
        readonly NO_APP_ID: "no-app-id";
        readonly NO_MODEL: "no-model";
        readonly NO_PROJECT_ID: "no-project-id";
        readonly PARSE_FAILED: "parse-failed";
        readonly UNSUPPORTED: "unsupported";
    }

## BackendType

An enum-like object containing constants that represent the supported backends for the Firebase AI SDK. This determines which backend service (Vertex AI Gemini API or Gemini Developer API) the SDK will communicate with.

These values are assigned to the `backendType` property within the specific backend configuration objects ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class) or [VertexAIBackend](https://firebase.google.com/docs/reference/js/ai.vertexaibackend.md#vertexaibackend_class)) to identify which service to target.

**Signature:**

    BackendType: {
        readonly VERTEX_AI: "VERTEX_AI";
        readonly GOOGLE_AI: "GOOGLE_AI";
    }

## BlockReason

Reason that a prompt was blocked.

**Signature:**

    BlockReason: {
        readonly SAFETY: "SAFETY";
        readonly OTHER: "OTHER";
        readonly BLOCKLIST: "BLOCKLIST";
        readonly PROHIBITED_CONTENT: "PROHIBITED_CONTENT";
    }

## FinishReason

Reason that a candidate finished.

**Signature:**

    FinishReason: {
        readonly STOP: "STOP";
        readonly MAX_TOKENS: "MAX_TOKENS";
        readonly SAFETY: "SAFETY";
        readonly RECITATION: "RECITATION";
        readonly OTHER: "OTHER";
        readonly BLOCKLIST: "BLOCKLIST";
        readonly PROHIBITED_CONTENT: "PROHIBITED_CONTENT";
        readonly SPII: "SPII";
        readonly MALFORMED_FUNCTION_CALL: "MALFORMED_FUNCTION_CALL";
    }

## FunctionCallingMode

**Signature:**

    FunctionCallingMode: {
        readonly AUTO: "AUTO";
        readonly ANY: "ANY";
        readonly NONE: "NONE";
    }

## HarmBlockMethod

This property is not supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)).

**Signature:**

    HarmBlockMethod: {
        readonly SEVERITY: "SEVERITY";
        readonly PROBABILITY: "PROBABILITY";
    }

## HarmBlockThreshold

Threshold above which a prompt or candidate will be blocked.

**Signature:**

    HarmBlockThreshold: {
        readonly BLOCK_LOW_AND_ABOVE: "BLOCK_LOW_AND_ABOVE";
        readonly BLOCK_MEDIUM_AND_ABOVE: "BLOCK_MEDIUM_AND_ABOVE";
        readonly BLOCK_ONLY_HIGH: "BLOCK_ONLY_HIGH";
        readonly BLOCK_NONE: "BLOCK_NONE";
        readonly OFF: "OFF";
    }

## HarmCategory

Harm categories that would cause prompts or candidates to be blocked.

**Signature:**

    HarmCategory: {
        readonly HARM_CATEGORY_HATE_SPEECH: "HARM_CATEGORY_HATE_SPEECH";
        readonly HARM_CATEGORY_SEXUALLY_EXPLICIT: "HARM_CATEGORY_SEXUALLY_EXPLICIT";
        readonly HARM_CATEGORY_HARASSMENT: "HARM_CATEGORY_HARASSMENT";
        readonly HARM_CATEGORY_DANGEROUS_CONTENT: "HARM_CATEGORY_DANGEROUS_CONTENT";
    }

## HarmProbability

Probability that a prompt or candidate matches a harm category.

**Signature:**

    HarmProbability: {
        readonly NEGLIGIBLE: "NEGLIGIBLE";
        readonly LOW: "LOW";
        readonly MEDIUM: "MEDIUM";
        readonly HIGH: "HIGH";
    }

## HarmSeverity

Harm severity levels.

**Signature:**

    HarmSeverity: {
        readonly HARM_SEVERITY_NEGLIGIBLE: "HARM_SEVERITY_NEGLIGIBLE";
        readonly HARM_SEVERITY_LOW: "HARM_SEVERITY_LOW";
        readonly HARM_SEVERITY_MEDIUM: "HARM_SEVERITY_MEDIUM";
        readonly HARM_SEVERITY_HIGH: "HARM_SEVERITY_HIGH";
        readonly HARM_SEVERITY_UNSUPPORTED: "HARM_SEVERITY_UNSUPPORTED";
    }

## ImagenAspectRatio

Aspect ratios for Imagen images.

To specify an aspect ratio for generated images, set the `aspectRatio` property in your [ImagenGenerationConfig](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfig_interface).

See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) for more details and examples of the supported aspect ratios.

**Signature:**

    ImagenAspectRatio: {
        readonly SQUARE: "1:1";
        readonly LANDSCAPE_3x4: "3:4";
        readonly PORTRAIT_4x3: "4:3";
        readonly LANDSCAPE_16x9: "16:9";
        readonly PORTRAIT_9x16: "9:16";
    }

## ImagenPersonFilterLevel

A filter level controlling whether generation of images containing people or faces is allowed.

See the [personGeneration](http://firebase.google.com/docs/vertex-ai/generate-images) documentation for more details.

**Signature:**

    ImagenPersonFilterLevel: {
        readonly BLOCK_ALL: "dont_allow";
        readonly ALLOW_ADULT: "allow_adult";
        readonly ALLOW_ALL: "allow_all";
    }

## ImagenSafetyFilterLevel

A filter level controlling how aggressively to filter sensitive content.

Text prompts provided as inputs and images (generated or uploaded) through Imagen on Vertex AI are assessed against a list of safety filters, which include 'harmful categories' (for example, `violence`, `sexual`, `derogatory`, and `toxic`). This filter level controls how aggressively to filter out potentially harmful content from responses. See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) and the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-filters) for more details.

**Signature:**

    ImagenSafetyFilterLevel: {
        readonly BLOCK_LOW_AND_ABOVE: "block_low_and_above";
        readonly BLOCK_MEDIUM_AND_ABOVE: "block_medium_and_above";
        readonly BLOCK_ONLY_HIGH: "block_only_high";
        readonly BLOCK_NONE: "block_none";
    }

## InferenceMode

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Determines whether inference happens on-device or in-cloud.

**PREFER_ON_DEVICE:** Attempt to make inference calls using an on-device model. If on-device inference is not available, the SDK will fall back to using a cloud-hosted model.   
**ONLY_ON_DEVICE:** Only attempt to make inference calls using an on-device model. The SDK will not fall back to a cloud-hosted model. If on-device inference is not available, inference methods will throw.   
**ONLY_IN_CLOUD:** Only attempt to make inference calls using a cloud-hosted model. The SDK will not fall back to an on-device model.   
**PREFER_IN_CLOUD:** Attempt to make inference calls to a cloud-hosted model. If not available, the SDK will fall back to an on-device model.

**Signature:**

    InferenceMode: {
        readonly PREFER_ON_DEVICE: "prefer_on_device";
        readonly ONLY_ON_DEVICE: "only_on_device";
        readonly ONLY_IN_CLOUD: "only_in_cloud";
        readonly PREFER_IN_CLOUD: "prefer_in_cloud";
    }

## InferenceSource

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Indicates whether inference happened on-device or in-cloud.

**Signature:**

    InferenceSource: {
        readonly ON_DEVICE: "on_device";
        readonly IN_CLOUD: "in_cloud";
    }

## Language

The programming language of the code.

**Signature:**

    Language: {
        UNSPECIFIED: string;
        PYTHON: string;
    }

## LiveResponseType

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The types of responses that can be returned by [LiveSession.receive()](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionreceive).

**Signature:**

    LiveResponseType: {
        SERVER_CONTENT: string;
        TOOL_CALL: string;
        TOOL_CALL_CANCELLATION: string;
        GOING_AWAY_NOTICE: string;
    }

## Modality

Content part modality.

**Signature:**

    Modality: {
        readonly MODALITY_UNSPECIFIED: "MODALITY_UNSPECIFIED";
        readonly TEXT: "TEXT";
        readonly IMAGE: "IMAGE";
        readonly VIDEO: "VIDEO";
        readonly AUDIO: "AUDIO";
        readonly DOCUMENT: "DOCUMENT";
    }

## Outcome

Represents the result of the code execution.

**Signature:**

    Outcome: {
        UNSPECIFIED: string;
        OK: string;
        FAILED: string;
        DEADLINE_EXCEEDED: string;
    }

## POSSIBLE_ROLES

Possible roles.

**Signature:**

    POSSIBLE_ROLES: readonly ["user", "model", "function", "system"]

## ResponseModality

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Generation modalities to be returned in generation responses.

**Signature:**

    ResponseModality: {
        readonly TEXT: "TEXT";
        readonly IMAGE: "IMAGE";
        readonly AUDIO: "AUDIO";
    }

## SchemaType

Contains the list of OpenAPI data types as defined by the [OpenAPI specification](https://swagger.io/docs/specification/data-models/data-types/)

**Signature:**

    SchemaType: {
        readonly STRING: "string";
        readonly NUMBER: "number";
        readonly INTEGER: "integer";
        readonly BOOLEAN: "boolean";
        readonly ARRAY: "array";
        readonly OBJECT: "object";
    }

## ThinkingLevel

A preset that controls the model's "thinking" process. Use `ThinkingLevel.LOW` for faster responses on less complex tasks, and `ThinkingLevel.HIGH` for better reasoning on more complex tasks.

**Signature:**

    ThinkingLevel: {
        MINIMAL: string;
        LOW: string;
        MEDIUM: string;
        HIGH: string;
    }

## URLRetrievalStatus

The status of a URL retrieval.

**URL_RETRIEVAL_STATUS_UNSPECIFIED:** Unspecified retrieval status.   
**URL_RETRIEVAL_STATUS_SUCCESS:** The URL retrieval was successful.   
**URL_RETRIEVAL_STATUS_ERROR:** The URL retrieval failed.   
**URL_RETRIEVAL_STATUS_PAYWALL:** The URL retrieval failed because the content is behind a paywall.   
**URL_RETRIEVAL_STATUS_UNSAFE:** The URL retrieval failed because the content is unsafe.   

**Signature:**

    URLRetrievalStatus: {
        URL_RETRIEVAL_STATUS_UNSPECIFIED: string;
        URL_RETRIEVAL_STATUS_SUCCESS: string;
        URL_RETRIEVAL_STATUS_ERROR: string;
        URL_RETRIEVAL_STATUS_PAYWALL: string;
        URL_RETRIEVAL_STATUS_UNSAFE: string;
    }

## AIErrorCode

Standardized error codes that [AIError](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierror_class) can have.

**Signature:**

    export type AIErrorCode = (typeof AIErrorCode)[keyof typeof AIErrorCode];

## BackendType

Type alias representing valid backend types. It can be either `'VERTEX_AI'` or `'GOOGLE_AI'`.

**Signature:**

    export type BackendType = (typeof BackendType)[keyof typeof BackendType];

## BlockReason

Reason that a prompt was blocked.

**Signature:**

    export type BlockReason = (typeof BlockReason)[keyof typeof BlockReason];

## FinishReason

Reason that a candidate finished.

**Signature:**

    export type FinishReason = (typeof FinishReason)[keyof typeof FinishReason];

## FunctionCallingMode

**Signature:**

    export type FunctionCallingMode = (typeof FunctionCallingMode)[keyof typeof FunctionCallingMode];

## HarmBlockMethod

This property is not supported in the Gemini Developer API ([GoogleAIBackend](https://firebase.google.com/docs/reference/js/ai.googleaibackend.md#googleaibackend_class)).

**Signature:**

    export type HarmBlockMethod = (typeof HarmBlockMethod)[keyof typeof HarmBlockMethod];

## HarmBlockThreshold

Threshold above which a prompt or candidate will be blocked.

**Signature:**

    export type HarmBlockThreshold = (typeof HarmBlockThreshold)[keyof typeof HarmBlockThreshold];

## HarmCategory

Harm categories that would cause prompts or candidates to be blocked.

**Signature:**

    export type HarmCategory = (typeof HarmCategory)[keyof typeof HarmCategory];

## HarmProbability

Probability that a prompt or candidate matches a harm category.

**Signature:**

    export type HarmProbability = (typeof HarmProbability)[keyof typeof HarmProbability];

## HarmSeverity

Harm severity levels.

**Signature:**

    export type HarmSeverity = (typeof HarmSeverity)[keyof typeof HarmSeverity];

## ImagenAspectRatio

Aspect ratios for Imagen images.

To specify an aspect ratio for generated images, set the `aspectRatio` property in your [ImagenGenerationConfig](https://firebase.google.com/docs/reference/js/ai.imagengenerationconfig.md#imagengenerationconfig_interface).

See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) for more details and examples of the supported aspect ratios.

**Signature:**

    export type ImagenAspectRatio = (typeof ImagenAspectRatio)[keyof typeof ImagenAspectRatio];

## ImagenPersonFilterLevel

A filter level controlling whether generation of images containing people or faces is allowed.

See the [personGeneration](http://firebase.google.com/docs/vertex-ai/generate-images) documentation for more details.

**Signature:**

    export type ImagenPersonFilterLevel = (typeof ImagenPersonFilterLevel)[keyof typeof ImagenPersonFilterLevel];

## ImagenSafetyFilterLevel

A filter level controlling how aggressively to filter sensitive content.

Text prompts provided as inputs and images (generated or uploaded) through Imagen on Vertex AI are assessed against a list of safety filters, which include 'harmful categories' (for example, `violence`, `sexual`, `derogatory`, and `toxic`). This filter level controls how aggressively to filter out potentially harmful content from responses. See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) and the [Responsible AI and usage guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-filters) for more details.

**Signature:**

    export type ImagenSafetyFilterLevel = (typeof ImagenSafetyFilterLevel)[keyof typeof ImagenSafetyFilterLevel];

## InferenceMode

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Determines whether inference happens on-device or in-cloud.

**Signature:**

    export type InferenceMode = (typeof InferenceMode)[keyof typeof InferenceMode];

## InferenceSource

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Indicates whether inference happened on-device or in-cloud.

**Signature:**

    export type InferenceSource = (typeof InferenceSource)[keyof typeof InferenceSource];

## Language

The programming language of the code.

**Signature:**

    export type Language = (typeof Language)[keyof typeof Language];

## LanguageModelMessageContentValue

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Content formats that can be provided as on-device message content.

**Signature:**

    export type LanguageModelMessageContentValue = ImageBitmapSource | AudioBuffer | BufferSource | string;

## LanguageModelMessageRole

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Allowable roles for on-device language model usage.

**Signature:**

    export type LanguageModelMessageRole = 'system' | 'user' | 'assistant';

## LanguageModelMessageType

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Allowable types for on-device language model messages.

**Signature:**

    export type LanguageModelMessageType = 'text' | 'image' | 'audio';

## LiveResponseType

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The types of responses that can be returned by [LiveSession.receive()](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesessionreceive). This is a property on all messages that can be used for type narrowing. This property is not returned by the server, it is assigned to a server message object once it's parsed.

**Signature:**

    export type LiveResponseType = (typeof LiveResponseType)[keyof typeof LiveResponseType];

## Modality

Content part modality.

**Signature:**

    export type Modality = (typeof Modality)[keyof typeof Modality];

## Outcome

Represents the result of the code execution.

**Signature:**

    export type Outcome = (typeof Outcome)[keyof typeof Outcome];

## Part

Content part - includes text, image/video, or function call/response part types.

**Signature:**

    export type Part = TextPart | InlineDataPart | FunctionCallPart | FunctionResponsePart | FileDataPart | ExecutableCodePart | CodeExecutionResultPart;

## ResponseModality

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Generation modalities to be returned in generation responses.

**Signature:**

    export type ResponseModality = (typeof ResponseModality)[keyof typeof ResponseModality];

## Role

Role is the producer of the content.

**Signature:**

    export type Role = (typeof POSSIBLE_ROLES)[number];

## SchemaType

Contains the list of OpenAPI data types as defined by the [OpenAPI specification](https://swagger.io/docs/specification/data-models/data-types/)

**Signature:**

    export type SchemaType = (typeof SchemaType)[keyof typeof SchemaType];

## ThinkingLevel

A preset that controls the model's "thinking" process. Use `ThinkingLevel.LOW` for faster responses on less complex tasks, and `ThinkingLevel.HIGH` for better reasoning on more complex tasks.

**Signature:**

    export type ThinkingLevel = (typeof ThinkingLevel)[keyof typeof ThinkingLevel];

## Tool

Defines a tool that model can call to access external knowledge.

**Signature:**

    export type Tool = FunctionDeclarationsTool | GoogleSearchTool | CodeExecutionTool | URLContextTool;

## TypedSchema

A type that includes all specific Schema types.

**Signature:**

    export type TypedSchema = IntegerSchema | NumberSchema | StringSchema | BooleanSchema | ObjectSchema | ArraySchema | AnyOfSchema;

## URLRetrievalStatus

The status of a URL retrieval.

**URL_RETRIEVAL_STATUS_UNSPECIFIED:** Unspecified retrieval status.   
**URL_RETRIEVAL_STATUS_SUCCESS:** The URL retrieval was successful.   
**URL_RETRIEVAL_STATUS_ERROR:** The URL retrieval failed.   
**URL_RETRIEVAL_STATUS_PAYWALL:** The URL retrieval failed because the content is behind a paywall.   
**URL_RETRIEVAL_STATUS_UNSAFE:** The URL retrieval failed because the content is unsafe.   

**Signature:**

    export type URLRetrievalStatus = (typeof URLRetrievalStatus)[keyof typeof URLRetrievalStatus];