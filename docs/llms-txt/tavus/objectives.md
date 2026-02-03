# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/objectives.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Objectives

> Objectives are goal-oriented instructions to define the desired outcomes and flow of your conversations.

Objectives work alongside your system prompt to provide a structured, flexible approach to guide conversations. They provide the most value during purposeful conversations that need to be tailored to specific processes, customer journeys, or workflows, while maintaining engaging and natural interactions.

For example, if you're creating a lead qualification persona for sales, you can set objectives to gather contact information, understand budget requirements, and assess decision-making authority before scheduling a follow-up meeting.

<Note>
  Objectives can only be created using the [Create Objectives](/api-reference/objectives/create-objectives) API.
</Note>

When designing your objectives, it's helpful to keep a few things in mind:

* Plan your entire ideal workflow. This will help create a robust branching structure that successfully takes the participant from start to finish.
* Think through the possible answers a participant might give, and ensure the workflow covers these cases.
* Ensure your persona's system prompt does not conflict with the objectives. For example, a system prompt, "You are a tutor," would not perform well with the objectives workflow of a sales associate.

## Attaching objectives to a persona

To attach objectives to a persona, you can either:

* Add them during [persona creation](/api-reference/personas/create-persona) like this:

```sh  theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/personas/ \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '{
    "system_prompt": "You are a lead qualification assistant.",
    "objectives_id": "o12345"
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
    {"op": "add", "path": "/objectives_id", "value": "o12345"}
  ]'
```

<Note>
  For the best results, try creating unique objectives for different conversation purposes or business outcomes.

  For example, a customer onboarding persona might use objectives focused on data collection, while a support persona might use objectives focused on issue resolution.
</Note>

## Parameters

### `objective_name`

A desciptive name for the objective.

Example: `"check_patient_status"`

<Note>
  This must be a string value without spaces.
</Note>

### `objective_prompt`

A text prompt that explains what the goals of this objective are. The more detail you can provide, the better.

Example: `"Ask the patient if they are new or are returning."`

### `confirmation_mode`

This string value defines whether the LLM should determine whether this objective was completed or not.

* If set to `auto`, the LLM makes this decision.
* If set to `manual`, the participant must manually confirm that the objective was completed by the platform triggering an app message (`conversation.objective.pending`) and the participant having the ability to send one back called `conversation.objective.confirm`. This can include having the participant review the collected values for accuracy.

<Note>
  The default value of `confirmation_mode` is `auto`.
</Note>

### `output_variables` (optional)

This is a list of string variables that should be collected as a result of the objective being successfully completed.

Example: `["patient_status", "patient_group"]`

### `modality`

This value represents whether a specific objective should be completed based on the participant's verbal or visual responses. Each individual objective can be visual or verbal (not both), but this can vary across objectives.

<Note>
  The default value for `modality` is `"verbal"`.
</Note>

### `next_conditional_objectives`

This represents a mapping of objectives (identified by `objective_name`), to conditions that must be satisfied for that objective to be triggered.

Example:

```json  theme={null}
{
  "new_patient_intake_process": "If the patient has never been to the practice before",
  "existing_patient_intake_process": "If the patient has been to the practice before"
}
```

### `next_required_objectives`

This represents a list of objectives (identified by `objective_name`) that should be triggered once the current objective is completed.

Example: `["get_patient_name"]`

### `callback_url` (optional)

A URL that you can send notifications to when a particular objective has been completed.

Example: `"https://your-server.com/objectives-webhook"`
