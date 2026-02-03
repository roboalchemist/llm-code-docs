# Source: https://docs.squared.ai/activation/ai-modelling/input-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Input Schema

> Define and configure the input schema to structure the data your model receives.

The **Input Schema** defines the structure of the data passed to your AI/ML model during inference. This ensures that inputs sent from your business applications or workflows match the format expected by your model endpoint.

AI Squared provides a no-code interface to configure input fields, set value types, and ensure compatibility with model requirements.

***

## Why Input Schema Matters

* Ensures data integrity before reaching the model
* Maps business inputs to model parameters
* Prevents inference failures due to malformed payloads
* Enables dynamic or static parameter configuration

***

## Defining Input Fields

Each input field includes the following:

| Field          | Description                                                           |
| -------------- | --------------------------------------------------------------------- |
| **Name**       | The key name expected in your model’s request payload                 |
| **Type**       | The data type: `String`, `Integer`, `Float`, or `Boolean`             |
| **Value Type** | `Dynamic` (changes with each query/request) or `Static` (fixed value) |

📸 *Placeholder for: Screenshot of input schema editor*

***

## Static vs. Dynamic Values

* **Static**: Hardcoded values used for all model requests. Example: `country: "US"`
* **Dynamic**: Values sourced from the business application or runtime context. Example: `user_id` passed from Salesforce record

📘 *Tip: Use harvesting (covered later) to auto-fetch dynamic values from frontend apps like CRMs.*

***

## Example Input Schema

```json  theme={null}
{
  "customer_id": "12345",
  "email": "user@example.com",
  "plan_type": "premium",
  "language": "en"
}
```

In this example:

customer\_id and email may be dynamic

plan\_type could be static

Each key must align with your model's expected input structure

## Next Steps

Once your input schema is defined, you can:

Add optional Preprocessing logic to transform or clean inputs

Move forward with configuring your Output Schema
