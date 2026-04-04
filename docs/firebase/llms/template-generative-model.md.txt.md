# Source: https://firebase.google.com/docs/reference/unity/class/firebase/a-i/template-generative-model.md.txt

# Firebase.AI.TemplateGenerativeModel Class Reference

# Firebase.AI.TemplateGenerativeModel

A type that represents a remote multimodal model (like Gemini), with the ability to generate content based on defined server prompt templates.

## Summary

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/a-i/template-generative-model#class_firebase_1_1_a_i_1_1_template_generative_model_1addf17cea3ebbb207bdacbc2b3ade58f6(string templateId, IDictionary< string, object > inputs, CancellationToken cancellationToken)` | `Task< https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response >` Generates new content by calling into a server prompt template. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/a-i/template-generative-model#class_firebase_1_1_a_i_1_1_template_generative_model_1af493e96d71baa6500d988c930c2b23d3(string templateId, IDictionary< string, object > inputs, CancellationToken cancellationToken)` | `IAsyncEnumerable< https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/generate-content-response#struct_firebase_1_1_a_i_1_1_generate_content_response >` Generates new content as a stream by calling into a server prompt template. |

## Public functions

### GenerateContentAsync

```c#
Task< GenerateContentResponse > GenerateContentAsync(
  string templateId,
  IDictionary< string, object > inputs,
  CancellationToken cancellationToken
)
```
Generates new content by calling into a server prompt template.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `templateId` | The id of the server prompt template to use. | | `inputs` | Any input parameters expected by the server prompt template. | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions | |---|---| | `HttpRequestException` | Thrown when an error occurs during content generation. | |
| **Returns** | The generated content response from the model. |

### GenerateContentStreamAsync

```c#
IAsyncEnumerable< GenerateContentResponse > GenerateContentStreamAsync(
  string templateId,
  IDictionary< string, object > inputs,
  CancellationToken cancellationToken
)
```
Generates new content as a stream by calling into a server prompt template.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `templateId` | The id of the server prompt template to use. | | `inputs` | Any input parameters expected by the server prompt template. | | `cancellationToken` | An optional token to cancel the operation. | |
| Exceptions | |---|---| | `HttpRequestException` | Thrown when an error occurs during content generation. | |
| **Returns** | A stream of generated content responses from the model. |