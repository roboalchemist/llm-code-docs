# Source: https://firebase.google.com/docs/ai-logic/server-prompt-templates/get-started.md.txt

> [!WARNING]
> **Preview**: Using server prompt templates is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

In each request to a model, you send a prompt and optionally schema and
configurations to control the model's response. When using
Firebase AI Logic, you can send all this information directly from your
client code, or you can specify this information server-side using
***server prompt templates***.

When using server prompt templates, you store your prompt, schema, and
configurations server-side, and your app passes from the client to the server
only the key (the template ID) referencing a specific template as well as the
required inputs for that template.

When using server prompt templates, you store your prompt and configurations
server-side and only provide a key (the template ID) in your app's codebase.
Here are some benefits of this approach:

- Protect against exposing your prompt client-side

- Update your prompt and configuration without releasing a new app version

This guide describes how to get started using server prompt templates.

[Jump to high-level overview](https://firebase.google.com/docs/ai-logic/server-prompt-templates/get-started#high-level)
[Jump to detailed instructions](https://firebase.google.com/docs/ai-logic/server-prompt-templates/get-started#detailed-instructions)

#### Supported models and capabilities

- Use server prompt templates with any of the
  [Gemini and Imagen models](https://firebase.google.com/docs/ai-logic/models) that
  Firebase AI Logic supports, *with the exception of Gemini Live models*.

- Review the
  [list of not-yet-supported features](https://firebase.google.com/docs/ai-logic/server-prompt-templates/best-practices-and-considerations).

<br />

*** ** * ** ***

## High-level overview

Here's the basic workflow for using server prompt templates:

1. Create the template using the guided UI in the
   [Firebase console](https://console.firebase.google.com/project/_/ailogic/templates).

2. Test the template in a real request using the Firebase console's testing
   experience.

3. Access the template from your app.

### Basic format of server prompt templates

For Firebase AI Logic, the
[Firebase console](https://console.firebase.google.com/project/_/ailogic/templates)
provides a guided UI for you to specify the contents of a template.

Server prompt templates use a Dotprompt-based syntax and format.
For more details, see
[Template format, syntax, and examples](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples).

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

### Use your template in code

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

Here's how to use the template in your code:

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

> [!IMPORTANT]
> **Important:** We strongly recommend [using Firebase Remote Config with server prompt templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/versioning-with-remote-config) so that you can more easily change the template ID and other values in your request.

<br />

*** ** * ** ***

## Detailed instructions

This section provides detailed instructions for creating, testing, and using
server prompt templates.

### Before you begin

- If you haven't already,
  **complete the [getting started guide](https://firebase.google.com/docs/ai-logic/get-started)** , which
  describes how to set up your Firebase project, connect your app to Firebase,
  add the SDK, initialize the backend service for your chosen
  Gemini API provider, and create a `GenerativeModel` instance.

- Make sure you have the **required permissions** to create and manage
  server prompt templates. By default, all these permissions are included in the
  Owner role.

  <br />

  View required permissions

  <br />

  - `firebasevertexai.googleapis.com/promptTemplates.create`
  - `firebasevertexai.googleapis.com/promptTemplates.get`
  - `firebasevertexai.googleapis.com/promptTemplates.update`
  - `firebasevertexai.googleapis.com/promptTemplates.delete`
  - `firebasevertexai.googleapis.com/promptTemplates.list`

  <br />

  <br />

- If you use the Vertex AI Gemini API and ***if your use case requires
  location-based restrictions*** , we support
  [advanced workflows for templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/advanced-workflows).

### **Step 1**: Create a server prompt template

For most use cases, you create and manage server prompt templates in the
Firebase console.

1. In the Firebase console, go to the
   [Firebase AI Logic **Prompt templates** tab](https://console.firebase.google.com/project/_/ailogic/templates).

2. Click **Create new template**, and select a starter template option.

   - These starter templates provide the format and syntax for some common use
     cases. No matter which option you select, though, you can completely
     change the template to meet your needs.

   - This getting started guide assumes you've selected the
     `Input + System Instructions` option.

3. Enter the template's identifiers:

   - **Template name** : This is a display name for the template (for example,
     `My First Template`). It's only visible within Firebase interfaces, like
     the Firebase console.

   - **Template ID** : This must be a unique ID for the template within your
     Firebase project (for example,
     `my-first-template-v1-0-0`). You'll reference this
     ID in the request from your app.

     - We recommend
       [using a versioning system](https://firebase.google.com/docs/ai-logic/server-prompt-templates/manage-templates#version-template)
       for your template IDs.

     - Template IDs can be max 63 characters and can contain lowercase letters,
       numbers, and hyphens.

4. Modify the **Configuration (frontmatter)** section of the template, as
   needed.

   - This section must include at minimum a model name, like this:

         ---
         model: 'gemini-3-flash-preview'
         ---

   - You can also optionally specify the model's configuration and any input \&
     output controls, etc. For more details and options, see
     [Template format, syntax, and examples](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples).

5. Modify the **Prompt and (as applicable) system instructions** section of the
   template, as needed.

   - This section must include at minimum the text prompt to send to the model.

         Write a story about a magic backpack.

   - You can also create more complex prompts, like the following options.
     For more details and options, see
     [Template format, syntax, and examples](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples).

     - *(Optional and as applicable)* Specify system instructions using the
       `{{role "system"}}` syntax, and the text
       prompt using the `{{role "user"}}`
       syntax.

     - *(Optional)* Specify input variables using
       [Handlebars](https://handlebarsjs.com/guide/) syntax (like
       `{{customerName}}`). You can provide a
       default value in the template, but the value of this input variable is
       usually passed in the request.

         {{role "system"}}
         All output must be a clearly structured invoice document.
         Use a tabular or clearly delineated list format for line items.

         {{role "user"}}
         Create an example customer invoice for a customer named {{customerName}}.

### **Step 2** : Test your template in the Firebase console

The Firebase console provides a testing experience for your template. This
experience lets you see what will happen when your template is used -- both the
format of the request as well as the output of an actual request.

1. Click **Save template** so that you can test your template.

   You can always edit or even delete the template later. The only value you
   can't change later is the template ID.
2. If your prompt uses input variables, include test values in the **Test
   input** field. For this example:

         {
           "customerName": "Jane"
         }

3. If you have multiple Gemini API providers enabled in your Firebase
   project, you can choose which one to use for the test request. If this
   option is displayed in the console, select either `Gemini Developer API` or
   `Vertex AI Gemini API`.

   Note that this selection only applies to requests submitted through the
   Firebase console testing experience. In the actual request from your app,
   you specify your chosen Gemini API provider just like you would for any
   request.
4. Click the **Create formatted test request** button.

   Review the resulting *Formatted test request* in the right-side of the
   screen, and iterate on any of your template's fields.

   <br />

   Expand to view example formatted test request

   <br />

       {
         "model": "projects/YOUR_PROJECT_ID/models/gemini-3-flash-preview",
         "contents": [{
           "parts": [{
             "text": "Create an example customer invoice for a customer named Jane"
           }],
           "role": "user"
         }],
         "systemInstruction": {
           "parts": [{
             "text": "All output must be a clearly structured invoice document.\nUse a tabular or clearly delineated list format for line items."
           }]
         }
       }

   <br />

   <br />

5. When you're satisfied with the formatted test request, click the **Run
   prompt test** button.

   Review the resulting *Test response* in the right-side of the screen, and
   iterate on any of your template's fields.

   > [!IMPORTANT]
   > **Important:** Each time you click **Run prompt test** , it might incur costs depending on your chosen Gemini API provider and pricing plan.

   <br />

   Expand to view example test response

   <br />

       {
         "candidates": [{
           "content": {
             "parts": [{
               "text": "```\n---\n                         **INVOICE**\n---\n\n**Creative Solutions Inc.**\n123 Business Lane, Suite 100\nAnytown, USA 12345\nPhone: (555) 123-4567\nEmail: info@creativesolutions.com\n\n**INVOICE NO:** INV-2023-001\n**INVOICE DATE:** October 26, 2023\n**DUE DATE:** November 25, 2023\n\n**BILL TO:**\nJane\n456 Client Street, Apt 2B\nAnytown, USA 12346\nPhone: (555) 987-6543\nEmail: jane@example.com\n\n---\n**ITEM DESCRIPTION**               **QTY**   **UNIT PRICE**   **AMOUNT**\n---\nWebsite Design Services            1         $800.00          $800.00\nContent Creation (Blog Posts)      4         $120.00          $480.00\nMonthly Hosting \u0026 Maintenance      1         $50.00           $50.00\nConsultation Fee                   2         $75.00           $150.00\n---\n\n**SUMMARY:**\nSubtotal:                                                     $1,480.00\nSales Tax (8%):                                               $118.40\n---\n**TOTAL DUE:**                                                **$1,598.40**\n---\n\n**PAYMENT TERMS:**\nPayment is due within 30 days of the invoice date. Please make checks payable to Creative Solutions Inc. For electronic payments, please contact us for details.\n\nThank you for your business!\n```"
             }],
             "role": "model"
           },
           "finishReason": "STOP",
           "index": 0
         }],
         "usageMetadata": {
           "promptTokenCount": 34,
           "candidatesTokenCount": 418,
           "totalTokenCount": 890,
           "promptTokensDetails": [{
             "modality": "TEXT",
             "tokenCount": 34
           }],
           "thoughtsTokenCount": 438
         },
         "modelVersion": "gemini-3-flash-preview",
         "responseId": "3w4Vad6yF-y1vdIP_q_zgAw",
         "turnToken": "v1:ChczdzRWYWQ2eUYteTF2ZElQX3FfemdBdxIXM3c0VmFkNnlGLXkxdmRJUF9xX3pnQXc"
       }

   <br />

   <br />

6. If you're ready to access the template from your app's code,
   [lock the template](https://firebase.google.com/docs/ai-logic/server-prompt-templates/manage-templates#lock-template)
   by clicking the
   lock icon in the
   top-right corner of the template.

7. Click **Close** to exit the editing experience.

### **Step 3**: Access your template from your code

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

A request using a server prompt template looks similar to other requests, with
the following adjustments:

- Use a `templateGenerativeModel` (or `templateImagenModel`, as needed).
- Provide the template ID.
- Provide the values of any variable inputs required by your template.

Note that after creating or updating your template, you may need to wait a
couple minutes for the template to propagate across Firebase servers before
accessing it from your code.

### Swift

Create a `templateGenerativeModel` instance (or `templateImagenModel`) to use
a template in your request.


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

Create a `templateGenerativeModel` instance (or `templateImagenModel`) to use
a template in your request.


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

Create a `templateGenerativeModel` instance (or `templateImagenModel`) to use
a template in your request.


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

Create a `templateGenerativeModel` instance (or `templateImagenModel`) to use
a template in your request.


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

The Flutter plugin will support server prompt templates soon!

Create a `templateGenerativeModel` instance (or `templateImagenModel`) to use
a template in your request.


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

Create a `templateGenerativeModel` instance (or `templateImagenModel`) to use
a template in your request.


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

> [!IMPORTANT]
> **Important:** We strongly recommend [using Firebase Remote Config with server prompt templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/versioning-with-remote-config) so that you can more easily change the template and other values in your request.

<br />

*** ** * ** ***

## What's next?

- Learn about
  [best practices and considerations](https://firebase.google.com/docs/ai-logic/server-prompt-templates/best-practices-and-considerations)
  for using server prompt templates.

- Learn details about the
  [template format and syntax, along with examples](https://firebase.google.com/docs/ai-logic/server-prompt-templates/syntax-and-examples).

- [Manage templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/manage-templates),
  including editing, locking, and version control.