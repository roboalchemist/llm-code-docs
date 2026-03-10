# Source: https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples.md.txt

> [!WARNING]
> **Preview**: Using server prompt templates is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

For Firebase AI Logic, the Firebase console provides a guided UI for you
to specify the contents of a template.

Server prompt templates use a Dotprompt-based syntax and format. On this page,
you can find detailed descriptions of the template format and syntax, along with
examples for both [Gemini](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini) and [Imagen](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#imagen).

Here are the most important components for an example request to a
Gemini model:

    ---
    model: 'gemini-3-flash-preview'
    ---

    {{role "system"}}
    All output must be a clearly structured invoice document.
    Use a tabular or clearly delineated list format for line items.

    {{role "user"}}
    Create an example customer invoice for a customer named {{customerName}}.

- The top section within the triple-dashes contains the model name as well as
  optionally any model configuration, input validation, or schema you want to
  send in the request. It's written as key-value pairs and is commonly called
  YAML *frontmatter*.

- The body of the template contains the prompt. It can also optionally include
  system instructions and input values (using
  [Handlebars](https://handlebarsjs.com/guide/) syntax).

> [!IMPORTANT]
> **Important:** Make sure to review the list of [not-yet-supported features](https://firebase.google.com/docs/ai-logic/server-prompt-templates/best-practices-and-considerations) for the initial release of server prompt templates.

<br />

This page provides detailed descriptions of the template format and syntax,
along with examples, for the following:

- [**Gemini**]()

  - [Hello world](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-hello-world)

  - [Model configuration](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-model-config)

  - [Thinking configuration](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-thinking)

  - [Safety settings](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-safety-settings)

  - [System instructions](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-system-instructions)

  - [Input variables](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-input-variables)

  - [Control flows (loops \& conditionals)](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-control-flows)

  - [Input validation and schema](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-input-validation-and-schema)

  - [Output schema](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-output-schema)

  - [Multimodal input](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-multimodal-input)

- [**Imagen**](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#imagen)

  - [Basic](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#imagen-basic)

  - [Advanced](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#imagen-advanced)

<br />

*** ** * ** ***

## **Gemini**

All the examples in this section show templates that use
`gemini-3-flash-preview`, but you can use any Gemini model supported by
Firebase AI Logic (except for Gemini Live models).

### Hello world

Here's a minimal example of a server prompt template:

**Configuration (frontmatter)**

    ---
    model: 'gemini-3-flash-preview'
    ---

**Prompt and (as applicable) system instructions**

    Write a story about a magic backpack.

<br />

### Control generation of responses

You can control the generation of responses in a variety of ways depending on
your use case and the level of control that you need.

#### Model configuration

Set a [model configuration](https://firebase.google.com/docs/ai-logic/model-parameters) to control how the
model generates a response,
like max output tokens, temperature, top-K, and top-P.

**Configuration (frontmatter)**

    ---
    model: 'gemini-3-flash-preview'
    config:
      candidateCount: 1
      temperature: 0.9
      topP: 0.1
      topK: 16
      maxOutputTokens: 200
      stopSequences: ["red"]
    ---

**Prompt and (as applicable) system instructions**

    Write a story about a magic backpack.

<br />

#### Thinking configuration

Specify a [thinking-related configuration](https://firebase.google.com/docs/ai-logic/thinking) for models
that support thinking.

> [!NOTE]
> **Note:** Gemini 3 and later models support *thinking budgets* for backwards-compatibility, but this configuration is *not* recommended. If you set both `thinkingLevel` and `thinkingBudget` in the same config, the request returns an error.

**Configuration (frontmatter)**

- Gemini 3 and later models (thinking levels)

      ---
      model: 'gemini-3-flash-preview'
      config:
        thinkingConfig:
          thinkingLevel: medium
          includeThoughts: true
      ---

- Gemini 2.5 models (thinking budgets)

      ---
      model: 'gemini-3-flash-preview'
      config:
        thinkingConfig:
          thinkingBudget: 1024
          includeThoughts: true
      ---

**Prompt and (as applicable) system instructions**

    Solve x^2 + 4x + 4 = 0

<br />

#### Safety settings

Use [safety settings](https://firebase.google.com/docs/ai-logic/safety-settings) to adjust the likelihood
of getting responses that may be considered harmful.

**Configuration (frontmatter)**

Example with one safety setting:

    ---
    model: 'gemini-3-flash-preview'
    config:
      safetySettings:
        - category: HARM_CATEGORY_HARASSMENT
          threshold: BLOCK_ONLY_HIGH
    ---

Example with multiple safety settings:

    ---
    model: 'gemini-3-flash-preview'
    config:
      safetySettings:
        - category: HARM_CATEGORY_HARASSMENT
          threshold: BLOCK_ONLY_HIGH
        - category: HARM_CATEGORY_HATE_SPEECH
          threshold: BLOCK_MEDIUM_AND_ABOVE
    ---

**Prompt and (as applicable) system instructions**

    Write a story about a magic backpack.

<br />

#### System instructions

Set [system instructions](https://firebase.google.com/docs/ai-logic/system-instructions) to steer the
behavior of the model. You include them as part of the prompt:

- Specify the system instructions using the
  `{{role "system"}}` syntax.

- Specify the text prompt using the
  `{{role "user"}}` syntax.

**Configuration (frontmatter)**

    ---
    model: 'gemini-3-flash-preview'
    ---

**Prompt and (as applicable) system instructions**

    {{role "system"}}
    All output must be a clearly structured invoice document.
    Use a tabular or clearly delineated list format for line items.

    {{role "user"}}
    Create an example customer invoice for a customer.

<br />

### Input variables

Some prompts are static, but you often need to include some data from the user
as part of the prompt.

You can include dynamic input variables in the prompt using
[Handlebars](https://handlebarsjs.com/guide/) expressions, which
are contained within `{{ }}` tags in the format
of `{{variableName}}` or
`{{object.propertyName}}` (for example,
`Hello, {{name}} from {{address.city}}`).

> [!IMPORTANT]
> **Important:** Always provide [input validation](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-input-validation-and-schema) to ensure that the data passed in the request matches your expectations. Note that if you use an input variable in your prompt and you provide input validation schema, then that value is considered required (unless you denote it as optional in the schema).

**Configuration (frontmatter)**

    ---
    model: 'gemini-3-flash-preview'
    ---

**Prompt and (as applicable) system instructions**

    Create an example customer invoice for a customer named {{customerName}}.

You can provide a [default value](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-input-validation-and-schema) in the
template, but the value of an input variable is usually provided by the client
as part of the request.

<br />

View client-side request that provides input values

<br />

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

### Swift


    // ...

    // Initialize the Gemini Developer API backend service
    // Create a `TemplateGenerativeModel` instance
    let model = FirebaseAI.firebaseAI(backend: .googleAI()).templateGenerativeModel()

    let customerName = "Jane"

    do {
        let response = try await model.generateContent(
            // Specify your template ID
            templateID: "my-first-template-v1-0-0",
            // Provide the values for any input variables required by your template.
            inputs: [
                "customerName": customerName
            ]
        )
        if let text = response.text {
            print("Response Text: \(text)")
        }
    } catch {
        print("An error occurred: \(error)")
    }
    print("\n")

### Kotlin


    // ...

    // Initialize the Gemini Developer API backend service
    // Create a `TemplateGenerativeModel` instance
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).templateGenerativeModel()

    val customerName = "Jane"

    val response = model.generateContent(
        // Specify your template ID
        "my-first-template-v1-0-0",
        // Provide the values for any input variables required by your template.
        mapOf(
            "customerName" to customerName
        )
    )

    val text = response.text
    println(text)

### Java


    // ...

    // Initialize the Gemini Developer API backend service
    // Create a `TemplateGenerativeModel` instance
    TemplateGenerativeModel generativeModel = FirebaseAI.getInstance().templateGenerativeModel();

    TemplateGenerativeModelFutures model = TemplateGenerativeModelFutures.from(generativeModel);

    String customerName = "Jane";

    Future response = model.generateContent(
        // Specify your template ID
        "my-first-template-v1-0-0",
        // Provide the values for any input variables required by your template.
        mapOf("customerName", customerName)
    );
    addCallback(response,
           new FutureCallback() {
               public void onSuccess(GenerateContentResponse result) {
                 System.out.println(result.getText());
               }
               public void onFailure(Throwable t) {
                 reportError(t);
               }
        }
    executor);

### Web


    // ...

    // Initialize the Gemini Developer API backend service
    const ai = getAI(app, { backend: new GoogleAIBackend() });

    // Create a `TemplateGenerativeModel` instance
    const model = getTemplateGenerativeModel(ai);

    const customerName = 'Jane';

    const result = await model.generateContent(
      // Specify your template ID
      'my-first-template-v1-0-0',
      // Provide the values for any input variables required by your template
      {
        customerName: customerName,
      }
    );

    const response = result.response;
    const text = response.text();

### Dart


    // ...

    // Initialize the Gemini Developer API backend service
    // Create a `TemplateGenerativeModel` instance
    var _model = FirebaseAI.googleAI().templateGenerativeModel()

    var customerName = 'Jane';

    var response = await _model.generateContent(
            // Specify your template ID
            'my-first-template-v1-0-0',
            // Provide the values for any input variables required by your template
            inputs: {
               'customerName': customerName,
            },
          );

    var text = response?.text;
    print(text);

### Unity


    // ...

    // Initialize the Gemini Developer API backend service
    var firebaseAI = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create a `TemplateGenerativeModel` instance
    var model = firebaseAI.GetTemplateGenerativeModel();

    var customerName = "Jane";

    try
    {
       var response = await model.GenerateContentAsync(
          // Specify your template ID
          "my-first-template-v1-0-0",
          // Provide the values for any input variables required by your template
          new Dictionary<string, object> {
             { "customerName", customerName },
          }
       );
       Debug.Log($"Response Text: {response.Text}");
    }
    catch (Exception e) {
      Debug.LogError($"An error occurred: {e.Message}");
    }

<br />

<br />

<br />

### Control flows (loops \& conditionals)

To write more complex prompts, you can use conditional blocks (like `#if` ,
`else`, and `#unless`) and iteration (`#each`).

You can provide additional contextual information as variables with a special
`@` prefix:

- `@first`: true when iterating the first item of an `#each` block.
- `@last`: true when iterating the last item of an `#each` block.
- `@index`: gives the (zero-based) index position of the current element.

See the
[Handlebars documentation](https://handlebarsjs.com/guide/builtin-helpers.html)
for information on all of the built-in logical helpers.

**Configuration (frontmatter)**

    ---
    model: 'gemini-3-flash-preview'
    ---

**Prompt and (as applicable) system instructions**

    Create an example customer invoice for a customer named {{customerName}}.

    Include entries for each of the following products

    {{#each productNames}}
      {{#if @first}}
      Include line items for the following purchases
      {{/if}}
      - {{this}}
    {{/each}}

    {{#if isVipCustomer}}
    Give the customer a 5% discount.
    {{/if}}

Note that conditionals only accept a variable reference, not any type of
expression, for example:

- The following works: `{{#if isVipCustomer}} ... {{/if}}`
- The following does *not* work: `{{#if customer.type == 'vip'}} ... {{/if}}`

If the variable is a boolean, then the conditional works as you would expect.
If the variable is *not* a boolean then the conditional is effectively an
"is-not-null" check. This can be useful for handling optional inputs, for
example:

    {{#if customerName}}
    Hello {{customerName}}
    {{else}}
    Hello Guest
    {{/if}}

<br />

### Input validation and schema

If you have data coming from the client, we strongly recommend using input
schema to help protect against prompt injection as well as ensure that the data
passed in the request matches your expectations.

- You can provide default values in case the client doesn't provide a value.

- The schema supports scalar types `string`, `integer`, `number`, `boolean`, and
  `object`. Objects, arrays, and enums are denoted by a parenthetical after the
  field name.

- All properties are considered required unless you denote it as optional with
  `?`. When a property is marked as optional, it's also made nullable to provide
  more leniency for LLMs to return null instead of omitting a field.

> [!NOTE]
> **Note:** If you specify an input schema and the client fails to pass valid inputs with a request, then the request will be rejected with a 400 error.

Here's a **basic example** for providing input schema. You can find a more
advanced schema just below.

**Configuration (frontmatter)**

    ---
    model: 'gemini-3-flash-preview'
    input:
      default:
        isVipCustomer: false
      schema:
        customerName: string, the customers name  # string, number, and boolean types are defined like this
        productNames?(array, list of products to include in the invoice): string  # optional fields are marked with a ?
        isVipCustomer?: boolean, whether or not the customer is a VIP
    ---

**Prompt and (as applicable) system instructions**

    Create an example customer invoice for a customer named {{customerName}}.

    Include entries for each of the following products

    {{#each productNames}}
      {{#if @first}}
      Include line items for the following purchases
      {{/if}}
      - {{this}}
    {{/each}}

    {{#if isVipCustomer}}
    Give the customer a 5% discount.
    {{/if}}

<br />

View a more **complex example** for providing input schema

<br />

**Configuration (frontmatter)**

    ---
    model: gemini-3-flash-preview
    input:
      schema:
        customer:
          type: object
          description: details about the customer
          required: [lastName, address]
          properties:
            firstName:
              type: string
              minLength: 2
              maxLength: 50
            lastName:
              type: string
              minLength: 2
              maxLength: 50
            address:
              type: object
              description: customer's address
              required: [street, city, country]
              properties:
                street:
                  type: string
                city:
                  type: string
                country:
                  type: string
            isVip:
              type: boolean
              description: whether or not the customer is a VIP
        purchases?:
          type: array
          description: list of things the customer purchased
          items:
            type: object
            required: [itemName, sku, cost, quantity]
            properties:
              itemName:
                type: string
              sku:
                type: string
                minLength: 7
                maxLength: 19
                pattern: "^[0-9]{1,3}-[a-zA-Z]{3,10}-[0-9]{1,4}$"
              category:
                enum: ["ELECTRONICS", "APPAREL", "HOME", "MISC" ]
              cost:
                type: number
                minimum: 0
              quantity:
                type: number
                minimum: 1
                maximum: 200
    ---

**Prompt and (as applicable) system instructions**

    Create an example customer invoice for a customer.

    The customer's address is

    {{customer.firstName}} {{customer.lastName}}
    {{customer.address.street}}
    {{customer.address.city}}
    {{customer.address.country}}

    {{#each purchases}}
      {{#if @first}}
      Include line items for the following purchaes
      {{/if}}
      - {{quantity}} x {{itemName}} ({{sku}}) @ ${{cost}}, category {{category}}
    {{/each}}

    {{#if customer.isVip}}
    Give the customer a 5% discount.
    {{/if}}

<br />

<br />

<br />

### Output schema

If you want the model to generate
[structured JSON output](https://firebase.google.com/docs/ai-logic/generate-structured-output),
then you can specify an output schema. By specifying `format: json`, you're
constraining the model to always return a JSON response that follows the
specified schema.

- The schema supports scalar types `string`, `integer`, `number`, `boolean`, and
  `object`. Objects, arrays, and enums are denoted by a parenthetical after the
  field name.

- All properties are considered required unless you denote it as optional with
  `?`. When a property is marked as optional, it's also made nullable to provide
  more leniency for LLMs to return null instead of omitting a field.

> [!NOTE]
> **Note:** Server prompt templates do ***not*** yet support [constraining the output to a list of enums](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-enum-basic).

Here's a **basic example** for generating structured JSON output. You can
find a more advanced schema just below.

**Configuration (frontmatter)**

    ---
    model: gemini-3-flash-preview
    output:
      format: json
      schema:
        invoiceId: string
        invoiceFile(object, an invoice file):
          url?: string
          contents: string
          mimeType: string
    ---

**Prompt and (as applicable) system instructions**

    Create an example customer invoice.

<br />

View a more **complex example** for generating structured JSON output

<br />

**Configuration (frontmatter)**

    ---
    model: gemini-3-flash-preview
    output:
      format: json
      schema:
        title: string  # string, number, and boolean types are defined like this
        subtitle?: string  # optional fields are marked with a ?
        draft?: boolean, true when in draft state
        status?(enum, approval status): [PENDING, APPROVED]
        date: string, the date of publication for example '2024-04-09' # descriptions follow a comma
        tags(array, relevant tags for article): string  # arrays are denoted via parentheses
        authors(array):
          name: string
          email?: string
        metadata?(object): # objects are also denoted via parentheses
          updatedAt?: string, ISO timestamp of last update
          approvedBy?: integer, id of approver
        extra?: any, arbitrary extra data
        (*): string, wildcard field
    ---

**Prompt and (as applicable) system instructions**

    Store all the specified information about the provided article.

<br />

<br />

<br />

### Multimodal input

Multimodal prompts sent to a Gemini model can include multiple types of input,
including [files](https://firebase.google.com/docs/ai-logic/input-file-requirements)
(like text along with images, PDFs, plain-text files, audio, and video).

- Provide a file using its URL with the `{{media url}}`
  syntax.

- Provide an inline file with the
  `{{media type="mime_type" data="contents"}}`
  syntax.

Here's a **basic example** for providing multimodal input. You can find a more
complex example just below.

**Configuration (frontmatter)**

    ---
    model: 'gemini-3-flash-preview'
    ---

**Prompt and (as applicable) system instructions**

    Describe this image

    {{media type="mimeType" data="imageData"}}

<br />

View how to provide base64-encoded data to test your template in the console

<br />

If your template has input that's base64-encoded data, here's how you can
include it in the testing experience of the Firebase console:

      {
        "mimeType": "image/png",
        "imageData": "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"
      }

<br />

<br />

<br />

View a more **complex example** for providing multimodal input

<br />

**Configuration (frontmatter)**

    ---
    model: gemini-3-flash-preview
    input:
      schema:
        image_urls?(array, urls of external images): string
        inline_images?(array, inline image data):
          type: object
          properties:
            mime_type: string
            contents: string  # inline data must be base64-encoded
    ---

**Prompt and (as applicable) system instructions**

    {{role "system"}}
    Use the following image as the basis for comparisons
    {{media url="http://example.com/reference_img.bmp"}}

    {{role "user"}}
    What do the following images have in common?

    {{#each image_urls}}
      {{media url="this"}}
    {{/each}}

    {{#each inline_images}}
      {{media type="mime_type" data="contents"}}
    {{/each}}

<br />

<br />

<br />

*** ** * ** ***

## **Imagen** (image generation)

With the initial release, server prompt templates support
[generating images using Imagen models and a text-only prompt](https://firebase.google.com/docs/ai-logic/generate-images-imagen).
Check back soon for more support, including
[editing images with Imagen](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview)
(when using the Vertex AI Gemini API).

### Basic

This example shows a basic template for generating images with
Imagen, with [input variables](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-input-variables) and
[input validation](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-input-validation-and-schema) similar to
Gemini.

**Configuration (frontmatter)**

    ---
    model: 'imagen-4.0-generate-001'
    input:
      schema:
        prompt: 'string'
    ---

**Prompt and (as applicable) system instructions**

    Create an image containing {{prompt}}

### Advanced

This example shows how to
add [model configuration](https://firebase.google.com/docs/ai-logic/model-parameters#imagen),
specify [safety settings](https://firebase.google.com/docs/ai-logic/safety-settings#imagen),
and use more advanced features in the prompt, like
[input variables](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-input-variables),
[input validation](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-input-validation-and-schema), and
[control flows](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples#gemini-control-flows)
similar to Gemini.

**Configuration (frontmatter)**

    ---
    model: 'imagen-4.0-fast-generate-001'
    config:
      sampleCount: 1
      aspectRatio: "16:9"
      personGeneration: dont_allow
      includeRaiReason: true
      safetySetting: block_medium_and_above
    input:
      schema:
        style(enum, The style of image): [photo, sketch, painting]
        subject: string, The object or animal or scenery to generate.
        context?: string, Optional background or context description.
      default:
        style: photo
    ---

**Prompt and (as applicable) system instructions**

    A {{style}} of {{subject}}{{#if context}}{{context}}{{/if}}.