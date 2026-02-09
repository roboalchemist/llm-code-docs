# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/guardrails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Guardrails

> Guardrails provide your persona with strict behavioral guidelines that will be rigorously followed throughout every conversation.

Guardrails act as a safety layer that works alongside your system prompt to enforce specific rules, restrictions, and behavioral patterns that your persona must adhere to during conversations.

For example, if you're creating a customer service persona for a financial institution, you can apply guardrails that prevent the persona from discussing a competitor's products, sharing sensitive financial data, or providing investment advice outside of approved guidelines.

<Note>
  It is highly recommended to use the [Persona Builder](https://platform.tavus.io/conversations/builder) to create your guardrails, although you can use the [Create Guardrails](/api-reference/guardrails/create-guardrails) API directly.
</Note>

When designing your guardrails with the Persona Builder, it's helpful to keep a few things in mind:

* Be specific about what topics, behaviors, or responses should be restricted or avoided.
* Consider edge cases where participants might try to circumvent the guardrails through creative prompting.
* Ensure your guardrails complement, rather than contradict, your persona's system prompt and intended functionality.
* Test your guardrails with various conversation scenarios to ensure they activate appropriately without being overly restrictive.

If you would like to manually attach guardrails to a persona, you can either:

* Add them during [persona creation](/api-reference/personas/create-persona) like this:

```sh  theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/personas/ \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
    "system_prompt": "You are a health intake assistant.",
    "guardrails_id": "g12345"
  }'
```

OR

* Add them by [editing the persona](/api-reference/personas/patch-persona) like this:

```sh  theme={null}
curl --request PATCH \
  --url https://tavusapi.com/v2/personas/{persona_id} \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '[
    {"op": "add", "path": "/guardrails_id", "value": "g12345"}
  ]'
```

<Note>
  For the best results, try creating specific guardrails for different types of personas or conversation contexts.

  For example, a healthcare consultation might use guardrails to maintain medical compliance, while an educational tutor might use guardrails to enforce child safety and appropriate content guidelines.
</Note>

## Parameters

<Note>
  Within each set of guardrails, you can have multiple guardrail objects defined.
</Note>

### `guardrails_name`

A desciptive name for an individual guardrail.

Example: `"Never Discuss Competitor's Products"`

<Note>
  This must be a string value without spaces.
</Note>

### `guardrails_prompt`

A text prompt that explains what particular behavior(s) should be observed for a particular guardrail. The more detail you can provide, the better.

Example: `"Only mention products within Our Company Inc. during conversations, and never discuss competitors' products."`

### `modality`

This value represents whether a specific guardrail should be enforced based on the participant's verbal or visual responses. Each individual guardrail can be visual or verbal (not both), but this can vary across the same set of guardrails.

<Note>
  The default value for `modality` is `"verbal"`.
</Note>

### `callback_url` (optional)

A URL that you can send notifications to when a particular guardrail has been triggered.

Example: `"https://your-server.com/guardrails-webhook"`

# Example Guardrails

```json  theme={null}
{
  "guardrails_id": "g12345",
  "data": [
    {
      "guardrails_name": "Healthcare Compliance Guardrails",
      "guardrails_prompt": "Never share sensitive medical information or provide medical advice outside approved guidelines",
      "modality": "verbal",
      "callback_url": "https://your-server.com/guardrails-webhook"
    },
    {
      "guardrails_name": "Check if the participant is alone",
      "guardrails_prompt": "Confirm throughout the call that the participant is alone (i.e. not with other individuals in the background) throughout the call.",
      "modality": "visual"
    }
  ]
}
```
