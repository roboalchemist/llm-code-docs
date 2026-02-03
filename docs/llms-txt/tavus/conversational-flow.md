# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/conversational-flow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Conversational Flow

> Learn how to configure the Conversational Flow layer to fine-tune turn-taking and interruption handling behavior.

The **Conversational Flow Layer** in Tavus gives you precise control over the natural dynamics of conversation. This layer allows you to customize how your replica handles turn-taking and interruptions to create conversational experiences that match your specific use case.

## Understanding Conversational Flow

Conversational flow encompasses the subtle dynamics that make conversations feel natural:

* **Turn-taking**: How the replica decides when to speak and when to listen
* **Interruptibility**: How easily the replica can be interrupted by the user

<Note>
  All conversational flow parameters are optional. When not explicitly configured, the layer remains inactive. However, if you configure any single parameter, the system will apply sensible defaults to all other parameters to ensure consistent behavior.
</Note>

## Configuring the Conversational Flow Layer

<Note>
  If you're migrating from sparrow-0 (formerly called `smart_turn_detection` on the STT Layer) then check out the [migration guide here](/sections/troubleshooting#conversational-flow-vs-stt-relationship-and-migration).
</Note>

Define the conversational flow layer under the `layers.conversational_flow` object. Below are the parameters available:

### 1. `turn_detection_model`

Specifies the model used for detecting conversational turns.

* **Options**:
  * `sparrow-1`: Advanced turn detection model - faster, more accurate, and more natural than `sparrow-0` **(recommended)**
  * `sparrow-0`: Legacy turn detection model (available for backward compatibility)
  * `time-based`: Simple timeout-based turn detection

* **Default**: `sparrow-1`

```json  theme={null}
"turn_detection_model": "sparrow-1"
```

<Tip>
  **Sparrow-1 is recommended for all use cases** as it provides superior performance with faster response times, higher accuracy, and more natural conversational flow compared to the legacy Sparrow-0.
</Tip>

### 2. `turn_taking_patience`

Controls how eagerly the replica claims conversational turns. This affects both response latency and the likelihood of interrupting during natural pauses.

* **Options**:
  * `low`: Eager and quick to respond. May interrupt natural pauses. Best for rapid-fire exchanges or customer service scenarios where speed is prioritized.
  * `medium` **(default)**: Balanced behavior. Waits for appropriate conversational cues before responding.
  * `high`: Patient and waits for clear turn completion. Ideal for thoughtful conversations, interviews, or therapeutic contexts.

```json  theme={null}
"turn_taking_patience": "medium"
```

**Use Cases:**

* `low`: Fast-paced customer support, quick information lookups, casual chat
* `medium`: General purpose conversations, sales calls, presentations
* `high`: Medical consultations, legal advice, counseling sessions

### 3. `replica_interruptibility`

Controls how sensitive the replica is to user speech while the replica is talking. Determines whether the replica stops to listen or keeps speaking when interrupted.

* **Options**:
  * `low`: Less interruptible. The replica keeps talking through minor interruptions.
  * `medium` **(default)**: Balanced sensitivity. Responds to clear interruption attempts.
  * `high`: Highly sensitive. Stops easily when the user begins speaking, maximizing user control.

```json  theme={null}
"replica_interruptibility": "high"
```

**Use Cases:**

* `low`: Educational content delivery, storytelling, guided onboarding
* `medium`: Standard conversations, interviews, consultations
* `high`: User-driven conversations, troubleshooting, interactive support

## Default Behavior

When the conversational flow layer is not configured, all parameters default to `None` and the layer remains inactive. However, if you configure **any single parameter**, the system automatically applies the following defaults to ensure consistent behavior:

* `turn_detection_model`: `sparrow-1`
* `turn_taking_patience`: `medium`
* `replica_interruptibility`: `medium`

## Example Configurations

The following example configurations demonstrate how to tune conversational timing and interruption behavior for different use cases. Use `turn_taking_patience` to bias how quickly the replica responds after a user finishes speaking. Set it high when the replica should avoid interrupting, and low when fast responses are preferred. Use `replica_interruptibility` to control how easily the replica recalculates its response when interrupted; lower values are recommended for most experiences, with higher values reserved for cases where frequent, abrupt interruptions are desirable. Sparrow-1 dynamically handles turn-taking in all cases, with these settings acting as guiding biases rather than hard rules.

### Example 1: Customer Support Agent

Fast, responsive, and easily interruptible for customer-driven conversations:

```json  theme={null}
{
  "persona_name": "Support Agent",
  "system_prompt": "You are a helpful customer support agent...",
  "pipeline_mode": "full",
  "default_replica_id": "rfe12d8b9597",
  "layers": {
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "low",
      "replica_interruptibility": "medium"
    }
  }
}
```

### Example 2: Medical Consultation

Patient, thoughtful, with engaged listening for sensitive conversations:

```json  theme={null}
{
  "persona_name": "Medical Advisor",
  "system_prompt": "You are a compassionate medical professional...",
  "pipeline_mode": "full",
  "default_replica_id": "rfe12d8b9597",
  "layers": {
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "high",
      "replica_interruptibility": "verylow"
    }
  }
}
```

### Example 3: Educational Instructor

Delivers complete information with minimal interruption:

```json  theme={null}
{
  "persona_name": "Instructor",
  "system_prompt": "You are an experienced educator teaching complex topics...",
  "pipeline_mode": "full",
  "default_replica_id": "rfe12d8b9597",
  "layers": {
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "medium",
      "replica_interruptibility": "low"
    }
  }
}
```

### Example 4: Minimal Configuration

Configure just one parameter—others will use defaults:

```json  theme={null}
{
  "persona_name": "Quick Chat",
  "system_prompt": "You are a friendly conversational AI...",
  "pipeline_mode": "full",
  "default_replica_id": "rfe12d8b9597",
  "layers": {
    "conversational_flow": {
      "turn_taking_patience": "low"
    }
  }
}
```

In this example, the system will automatically set:

* `turn_detection_model`: `sparrow-1`
* `replica_interruptibility`: `medium`

## Best Practices

### Match Flow to Use Case

Choose conversational flow settings that align with your application's purpose:

* **Speed-critical applications**: Use `low` turn-taking patience and `high` interruptibility
* **Thoughtful conversations**: Use `high` turn-taking patience
* **Important information delivery**: Use `low` interruptibility
* **User-controlled interactions**: Use `high` interruptibility

### Consider Cultural Context

Conversational norms vary across cultures. Some cultures prefer:

* More overlap and interruption (consider lower commitment, higher interruptibility)
* Clear turn-taking with pauses (consider higher patience, lower interruptibility)

### Test with Real Users

Conversational flow preferences can be subjective. Test your configuration with representative users to ensure it feels natural for your audience.

<Note>
  Refer to the <a href="/api-reference/personas/create-persona" target="_blank">Create Persona API</a> for the complete API specification and additional persona configuration options.
</Note>
