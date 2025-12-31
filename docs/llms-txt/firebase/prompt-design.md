# Source: https://firebase.google.com/docs/ai-logic/prompt-design.md.txt

<br />

<br />

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

<br />

<br />

When you make a request to a generative model, you send along a*prompt*with your request. By carefully crafting these prompts, you can influence the model to generate output specific to your needs.

## Prompting forGeminimodels

Prompts forGeminimodels can contain questions, instructions, contextual information, few-shot examples, and partial input for the model to complete or continue.

Learn about prompt design in theGemini Developer APIdocumentation:

- [Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)

- [Prompt samples](https://ai.google.dev/gemini-api/prompts)

| **Tip:** You can experiment with prompts and model configurations and rapidly iterate using[Google AI Studio](https://aistudio.google.com).

## Prompting forImagenmodels

ForImagen, learn about[specific prompting strategies and options](https://ai.google.dev/gemini-api/docs/imagen#imagen-prompt-guide)

## Other options to control content generation

- Configure[model parameters](https://firebase.google.com/docs/ai-logic/model-parameters)to control how the model generates a response. ForGeminimodels, these parameters include max output tokens, temperature, topK, and topP. ForImagenmodels, these include aspect ratio, person generation, watermarking, etc.
- Use[safety settings](https://firebase.google.com/docs/ai-logic/safety-settings)to adjust the likelihood of getting responses that may be considered harmful, including hate speech and sexually explicit content.
- Set[system instructions](https://firebase.google.com/docs/ai-logic/system-instructions)to steer the behavior of the model. This feature is like a preamble that you add before the model gets exposed to any further instructions from the end user.
- Pass a[*response schema*](https://firebase.google.com/docs/ai-logic/generate-structured-output)along with the prompt to specify a specific output schema. This feature is most commonly used when[generating JSON output](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-json-basic), but it can also be used for[classification tasks](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-enum-basic)(like when you want the model to use specific labels or tags).