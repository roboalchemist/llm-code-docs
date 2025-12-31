# Source: https://firebase.google.com/docs/ai-logic/control-content-gen.md.txt

<br />

You can control the generation of responses in a variety of ways depending on your use case and the level of control that you need.

## Prompt design

Learn about[prompt design](https://firebase.google.com/docs/ai-logic/prompt-design)so that you can influence the model to generate output specific to your needs.

For example, learn how to provide relevant information associated with the task in a structured way.

## Model configuration

Set a[model configuration](https://firebase.google.com/docs/ai-logic/model-parameters)to control how the model generates a response. The configuration options depend on the model and capability that you're using.

ForGeminimodels, you can configure parameters like max output tokens, temperature, top-K, and top-P. And if you're using theGemini Live APIor aGeminimodel capable of multimodal output, you can additionally configure the type of response (audio, text, or images) and the voice used in audio responses.

ForGeminimodels capable of*thinking* , you can also specify a[thinking-related configuration](https://firebase.google.com/docs/ai-logic/thinking), including a*thinking budget* and whether to include*thought summaries*.

ForImagenmodels, you can configure parameters like number of images to generate, aspect ratio, adding a watermark, etc.

## Safety settings

Use[safety settings](https://firebase.google.com/docs/ai-logic/safety-settings)to adjust the likelihood of getting responses that may be considered harmful. These settings can help you with controlling output for possible hate speech, harassment, sexual explicitness, and dangerous content.

For example, you can block responses that promote or enable access to harmful goods, services, and activities.

## System instructions

Set[system instructions](https://firebase.google.com/docs/ai-logic/system-instructions)to steer the behavior of the model. This feature is like a "preamble" that you add before the model gets exposed to any further instructions from the end user.

For example, you can tell the model to return responses as if it were a pirate or to return responses in a specific format.

## Structured output using response schema

Pass a[*response schema*](https://firebase.google.com/docs/ai-logic/generate-structured-output)along with the prompt to specify a specific output schema. This feature is most commonly used when[generating JSON output](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-json-basic), but it can also be used for[classification tasks](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-enum-basic)(like when you want the model to use specific labels or tags).