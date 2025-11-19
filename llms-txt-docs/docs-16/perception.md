# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/perception.md

# Perception

> Learn how to configure the perception layer with Raven to enable the real-time visual understanding.

The **Perception Layer** in Tavus enhances an AI agent with real-time visual understanding.
By using [Raven](/sections/models#raven%3A-perception-model), the AI agent becomes more context-aware, responsive, and capable of triggering actions based on visual input.

## Configuring the Perception Layer

To configure the Perception Layer, define the following parameters within the `layers.perception` object:

### 1. `perception_model`

Specifies the perception model to use.

* **Options**:
  * `raven-0` (default and recommended): Advanced visual capabilities, including screen share support, ambient queries, and perception tools.
  * `basic`: Legacy model with limited features.
  * `off`: Disables the perception layer.

<Note>
  **Screen Share Feature**: When using `raven-0`, screen share feature is enabled by default without additional configuration.
</Note>

```json  theme={null}
"layers": {
  "perception": {
    "perception_model": "raven-0"
  }
}
```

### 2. `ambient_awareness_queries`

An array of custom queries that `raven-0` continuously monitors in the visual stream.

```json  theme={null}
"ambient_awareness_queries": [
  "Is the user wearing a bright outfit?"
]
```

### 3. `perception_analysis_queries`

An array of custom queries that `raven-0` processes at the end of the call to generate a visual analysis summary for the user.

<Note>
  You do not need to set `ambient_awareness_queries` in order to use `perception_analysis_queries`.
</Note>

```json  theme={null}
"perception_analysis_queries": [
  "Is the user wearing multiple bright colors?",
  "Is there any indication that more than one person is present?",
  "On a scale of 1-100, how often was the user looking at the screen?"
]
```

<Tip>
  Best practices for `ambient_awareness_queries` and `perception_analysis_queries`:

  * Use simple, focused prompts.
  * Use queries that support your persona’s purpose.
</Tip>

### 4. `perception_tool_prompt`

Tell `raven-0` when and how to trigger tools based on what it sees.

```json  theme={null}
"perception_tool_prompt":
  "You have a tool to notify the system when a bright outfit is detected, named `notify_if_bright_outfit_shown`. You MUST use this tool when a bright outfit is detected."
```

### 5. `perception_tools`

Defines callable functions that `raven-0` can trigger upon detecting specific visual conditions. Each tool must include a `type` and a `function` object detailing its schema.

```json  theme={null}
"perception_tools": [
  {
    "type": "function",
    "function": {
      "name": "notify_if_bright_outfit_shown",
      "description": "Use this function when a bright outfit is detected in the image with high confidence",
      "parameters": {
        "type": "object",
        "properties": {
          "outfit_color": {
            "type": "string",
            "description": "Best guess on what color of outfit it is"
          }
        },
        "required": ["outfit_color"]
      }
    }
  }
]
```

<Note>
  Please see [Tool Calling](/sections/conversational-video-interface/persona/perception-tool) for more details.
</Note>

## Example Configuration

This example demonstrates a persona designed to identify when a user wears a bright outfit and triggers an internal action accordingly.

```json  theme={null}
{
  "persona_name": "Fashion Advisor",
  "system_prompt": "As a Fashion Advisor, you specialize in offering tailored fashion advice.",
  "pipeline_mode": "full",
  "context": "You're having a video conversation with a client about their outfit.",
  "default_replica_id": "r79e1c033f",
  "layers": {
    "perception": {
      "perception_model": "raven-0",
      "ambient_awareness_queries": [
        "Is the user wearing a bright outfit?"
      ],
      "perception_analysis_queries": [
        "Is the user wearing multiple bright colors?",
        "Is there any indication that more than one person is present?",
        "On a scale of 1-100, how often was the user looking at the screen?"
      ],
      "perception_tool_prompt": "You have a tool to notify the system when a bright outfit is detected, named `notify_if_bright_outfit_shown`. You MUST use this tool when a bright outfit is detected.",
      "perception_tools": [
        {
          "type": "function",
          "function": {
            "name": "notify_if_bright_outfit_shown",
            "description": "Use this function when a bright outfit is detected in the image with high confidence",
            "parameters": {
              "type": "object",
              "properties": {
                "outfit_color": {
                  "type": "string",
                  "description": "Best guess on what color of outfit it is"
                }
              },
              "required": ["outfit_color"]
            }
          }
        }
      ]
    }
  }
}
```

<Note>
  Please see the <a href="/api-reference/personas/create-persona" target="_blank">Create a Persona</a> endpoint for more details.
</Note>

## End-of-call Perception Analysis

At the end of the call, `raven-0` will generate a visual summary including all detected visual artifacts. This will be sent as a [Perception Analysis](/sections/event-schemas/conversation-perception-analysis) event to the [conversation callback](/sections/webhooks-and-callbacks#conversation-callbacks) (if specified).

<Note>
  This feature is exclusive to personas with `raven-0` specified in the Perception Layer.
</Note>

Once processed, your backend will receive a payload like the following:

```json  theme={null}
{
  "properties": {
    "analysis": "Here's a summary of the visual observations:\n\n*   **User Appearance:** The subject is a young person, likely in their teens or early twenties, with dark hair and an East Asian appearance. They consistently wear a dark blue or black hooded jacket/hoodie with pink and white accents, patterns, or text on the sleeves, and possibly a white undershirt. A pendant or charm was observed on their chest. The setting is consistently an indoor environment with a plain white or light-colored wall background.\n*   **User Behavior and Demeanor:** The user frequently holds a wired earpiece, microphone, or earbuds near their mouth or chin, appearing to be speaking, listening intently, or in deep thought. Their gaze is predominantly cast downwards, occasionally looking slightly off to the side, with only rare, brief glances forward. They generally maintain a still posture.\n*   **User Emotions:** The user's expression is consistently neutral, conveying a sense of quiet concentration, engagement, contemplation, or thoughtful introspection. There are no overt signs of strong emotion; their demeanor is described as calm, focused, sometimes pensive, or slightly subdued. They appear to be actively listening or processing information.\n*    **User's gaze towards the screen:** On a scale of 1-100, the user was looking at the screen approximately 75% of the time. While there was one instance where their gaze was averted, for the majority of the observations, the user was either looking directly at the screen or in its general direction."
  },
  "conversation_id": "<conversation_id>",
  "webhook_url": "<webhook_url>",
  "message_type": "application",
  "event_type": "application.perception_analysis",
  "timestamp": "2025-07-11T09:13:35.361736Z"
}

```

### `ambient_awareness_queries`

For example, if you include the following query:

```json  theme={null}
"ambient_awareness_queries": [
  "Is the user wearing a jacket?"
]
```

Once processed, your backend will receive a payload containing the following sentence:

```json  theme={null}
**Ambient Awareness Queries:** The user was consistently wearing a jacket throughout the observed period.\n*
```

### `perception_analysis_queries`

For example, if you include the following query:

```json  theme={null}
"perception_analysis_queries": [
  "On a scale of 1-100, how often was the user looking at the screen?"
]
```

Once processed, your backend will receive a payload containing the following sentence:

```json  theme={null}
**User's Gaze Toward Screen:** "The participant looked at the screen approximately 75% of the time. Their gaze was occasionally diverted, but mostly remained focused in the direction of the camera."

```
