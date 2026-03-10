# Source: https://firebase.google.com/docs/ai-logic/hybrid/web/generate-structured-output.md.txt

> [!WARNING]
> **Preview** : Using the Firebase AI Logic SDKs to build hybrid experiences in Web apps is a Preview feature, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.
>
> This initial release only **supports on-device inference for
> web apps running on Chrome on Desktop.**

<br />

Gemini models return responses as unstructured text by default.
However, some use cases require structured text, like JSON. For example, you
might be using the response for other downstream tasks that require an
established data schema.

To ensure that the model's generated output always adheres to a specific schema,
you can define a *schema*, which works like a blueprint for model responses. You
can then directly extract data from the model's output with less
post-processing.

Here are some examples:

- **Ensure that a model's response produces valid JSON and conforms to your
  provided schema.**   

  For example, the model can generate structured entries for recipes that always
  include the recipe name, list of ingredients, and steps. You can then more
  easily parse and display this information in the UI of your app.

- **Constrain how a model can respond during classification tasks.**   

  For example, you can have the model annotate text with a specific set of
  labels (for instance, a specific set of enums like `positive` and `negative`),
  rather than labels that the model produces (which could have a degree of
  variability like `good`, `positive`, `negative`, or `bad`).

This page describes how to generate structured output (like JSON and enums)
in your hybrid experiences for web apps.

## Before you begin

Make sure that you've completed the
[getting started guide for building hybrid experiences](https://firebase.google.com/docs/ai-logic/hybrid/web/get-started#get-started).

## Set the configuration for structured output

Generating structured output (like JSON and enums) is supported for
inference using both cloud-hosted and on-device models.

For hybrid inference, use both
[`inCloudParams`](https://firebase.google.com/docs/reference/js/ai.hybridparams#hybridparamsincloudparams)
and
[`onDeviceParams`](https://firebase.google.com/docs/reference/js/ai.hybridparams#hybridparamsondeviceparams)
to configure the model to respond with structured output. For the other modes,
use only the applicable configuration.

- **For `inCloudParams`** : Specify the appropriate `responseMimeType` (for
  example, `application/json`) as well as the `responseSchema` that you want the
  model to use.

- **For `onDeviceParams`** : Specify the `responseConstraint` that you want the
  model to use.

## JSON output

The following example adapts the
[general JSON output example](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-json-basic)
to accommodate hybrid inference (in this example, `PREFER_ON_DEVICE`):

    import {
      getAI,
      getGenerativeModel,
      Schema
    } from "firebase/ai";

    const jsonSchema = Schema.object({
     properties: {
        characters: Schema.array({
          items: Schema.object({
            properties: {
              name: Schema.string(),
              accessory: Schema.string(),
              age: Schema.number(),
              species: Schema.string(),
            },
            optionalProperties: ["accessory"],
          }),
        }),
      }
    });

    const model = getGenerativeModel(ai, {
      mode: InferenceMode.PREFER_ON_DEVICE,
      inCloudParams: {
        generationConfig: {
          responseMimeType: "application/json",
          responseSchema: jsonSchema
        },
      }
      onDeviceParams: {
        promptOptions: {
          responseConstraint: jsonSchema
        }
      }
    });

    // ...

## Enum output

The following example adapts the
[general enum output example](https://firebase.google.com/docs/ai-logic/generate-structured-output#generate-enum-basic)
to accommodate hybrid inference (in this example, `PREFER_ON_DEVICE`):

    import {
      getAI,
      getGenerativeModel,
      Schema
    } from "firebase/ai";

    const enumSchema = Schema.enumString({
      enum: ["drama", "comedy", "documentary"],
    });

    const model = getGenerativeModel(ai, {
      mode: InferenceMode.PREFER_ON_DEVICE,
      inCloudParams: {
        generationConfig: {
          responseMimeType: "text/x.enum",
          responseSchema: enumSchema
        },
      }
      onDeviceParams: {
        promptOptions: {
          responseConstraint: enumSchema
        }
      }
    });

    // ...