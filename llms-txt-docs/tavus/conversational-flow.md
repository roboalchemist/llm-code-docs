# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/conversational-flow.md

# Conversational Flow

> Learn how to configure the Conversational Flow layer to fine-tune turn-taking, interruption handling, and active listening behavior.

The **Conversational Flow Layer** in Tavus gives you precise control over the natural dynamics of conversation. This layer allows you to customize how your replica handles turn-taking, interruptions, and backchannel responses to create conversational experiences that match your specific use case.

## Understanding Conversational Flow

Conversational flow encompasses the subtle dynamics that make conversations feel natural:

* **Turn-taking**: How the replica decides when to speak and when to listen
* **Turn commitment**: How firmly the replica holds its conversational turn once it starts speaking
* **Interruptibility**: How easily the replica can be interrupted by the user
* **Active listening**: How the replica provides verbal acknowledgments while listening

<Note>
  All conversational flow parameters are optional. When not explicitly configured, the layer remains inactive. However, if you configure any single parameter, the system will apply sensible defaults to all other parameters to ensure consistent behavior.
</Note>

## Configuring the Conversational Flow Layer

Define the conversational flow layer under the `layers.conversational_flow` object. Below are the parameters available:

### 1. `turn_detection_model`

Specifies the model used for detecting conversational turns.

* **Options**:
  * `sparrow-0`: Standard turn detection model
  * `sparrow-1`: Advanced turn detection model - faster, more accurate, and more natural than `sparrow-0` (recommended)
  * `time-based`: Simple timeout-based turn detection

* **Default**: `sparrow-0` (when any conversational flow parameter is provided)

```json  theme={null}
"turn_detection_model": "sparrow-1"
```

<Tip>
  `sparrow-1` is recommended for all use cases as it provides superior performance with faster response times, higher accuracy, and more natural conversational flow compared to `sparrow-0`.
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

### 3. `turn_commitment`

Controls how aggressively the replica will barge in and take its turn at the start of speaking. This affects the replica's willingness to start talking even when the user may still be speaking.

* **Options**:
  * `low`: Less aggressive barge-in. The replica waits more clearly for the user to finish before starting to speak.
  * `medium` **(default)**: Balanced barge-in behavior. The replica will start speaking when it detects an appropriate opportunity.
  * `high`: More aggressive barge-in. The replica will more readily start speaking even if the user may still be talking, allowing for more dynamic and overlapping conversation.

```json  theme={null}
"turn_commitment": "medium"
```

**Use Cases:**

* `low`: Formal conversations, interviews, scenarios where the user should complete their thoughts
* `medium`: General conversations, Q\&A sessions, guided interactions
* `high`: Fast-paced conversations, collaborative brainstorming, scenarios requiring quick back-and-forth exchanges

### 4. `replica_interruptibility`

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

<Note>
  `turn_commitment` and `replica_interruptibility` work together to create natural conversational dynamics. `turn_commitment` controls how aggressively the replica will barge in at the start of its turn, while `replica_interruptibility` controls how easily the replica can be interrupted once it's already speaking.
</Note>

### 5. `active_listening`

Controls the frequency of backchannel responses (like "yeah", "mhmm", "I see") while the user is speaking. These verbal cues signal attentiveness and engagement.

<Note>
  This feature is currently in **English-only beta**. Backchannel responses will only be generated for English conversations.
</Note>

* **Options**:
  * `off` **(default)**: No backchannel responses during user speech
  * `low`: Infrequent backchannels, minimal verbal acknowledgment
  * `medium`: Moderate backchannels at natural conversation breaks
  * `high`: Frequent backchannels, active engagement signals

```json  theme={null}
"active_listening": "medium"
```

**Use Cases:**

* `off`: Formal presentations, legal contexts, recorded sessions
* `low`: Professional consultations, technical support
* `medium`: Coaching sessions, sales calls, general conversations
* `high`: Therapy sessions, counseling, empathetic support conversations

<Warning>
  Use `high` active listening carefully. While it creates engaging conversations, too many backchannels can be distracting in some contexts or feel unnatural if overused.
</Warning>

## Relationship with STT Layer (Sparrow-0)

The Conversational Flow layer provides advanced configuration for **Sparrow-1**, which supersedes the legacy Sparrow-0 configuration in the STT layer. When you configure the Conversational Flow layer with `turn_detection_model` set to `sparrow-1`, these settings **override** the corresponding Sparrow-0 settings in the STT layer.

### Parameter Mapping: Sparrow-0 to Sparrow-1

Here's how Sparrow-0 (STT layer) parameters map to Sparrow-1 (Conversational Flow layer):

| Sparrow-0 (STT Layer)               | Sparrow-1 (Conversational Flow Layer) | Notes                                                |
| ----------------------------------- | ------------------------------------- | ---------------------------------------------------- |
| `participant_pause_sensitivity`     | `turn_taking_patience`                | Controls how long to wait before responding          |
| `participant_interrupt_sensitivity` | `replica_interruptibility`            | Controls how easily the replica can be interrupted   |
| N/A                                 | `turn_commitment`                     | **New in Sparrow-1**: Controls barge-in behavior     |
| N/A                                 | `active_listening`                    | **New in Sparrow-1**: Controls backchannel responses |

<Warning>
  **Important**: When using Sparrow-1 via the Conversational Flow layer, any conflicting settings in the STT layer (Sparrow-0) will be overridden. For example, if you set `participant_pause_sensitivity: "high"` in the STT layer but `turn_taking_patience: "low"` in the Conversational Flow layer with `turn_detection_model: "sparrow-1"`, the Conversational Flow setting (`low`) will take precedence.
</Warning>

### Migration Guide

If you're currently using Sparrow-0 settings in the STT layer and want to upgrade to Sparrow-1:

**Before (Sparrow-0):**

```json  theme={null}
{
  "layers": {
    "stt": {
      "participant_pause_sensitivity": "high",
      "participant_interrupt_sensitivity": "low"
    }
  }
}
```

**After (Sparrow-1):**

```json  theme={null}
{
  "layers": {
    "conversational_flow": {
      "turn_detection_model": "sparrow-1",
      "turn_taking_patience": "low",
      "replica_interruptibility": "high",
      "turn_commitment": "medium",
      "active_listening": "off"
    }
  }
}
```

<Note>
  Note the inverted mapping:

  * `participant_pause_sensitivity: "high"` (quick response) → `turn_taking_patience: "low"` (eager)
  * `participant_interrupt_sensitivity: "low"` (hard to interrupt) → `replica_interruptibility: "high"` (easy to interrupt)

  The naming has been updated in Sparrow-1 to be more intuitive from the replica's perspective.
</Note>

## Default Behavior

When the conversational flow layer is not configured, all parameters default to `None` and the layer remains inactive. However, if you configure **any single parameter**, the system automatically applies the following defaults to ensure consistent behavior:

* `turn_detection_model`: `sparrow-0`
* `turn_taking_patience`: `medium`
* `turn_commitment`: `medium`
* `replica_interruptibility`: `medium`
* `active_listening`: `off`

## Example Configurations

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
      "turn_detection_model": "sparrow-0",
      "turn_taking_patience": "low",
      "turn_commitment": "low",
      "replica_interruptibility": "high",
      "active_listening": "low"
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
      "turn_commitment": "medium",
      "replica_interruptibility": "medium",
      "active_listening": "high"
    }
  }
}
```

### Example 3: Educational Instructor

Committed to delivering complete information with minimal interruption:

```json  theme={null}
{
  "persona_name": "Instructor",
  "system_prompt": "You are an experienced educator teaching complex topics...",
  "pipeline_mode": "full",
  "default_replica_id": "rfe12d8b9597",
  "layers": {
    "conversational_flow": {
      "turn_detection_model": "sparrow-0",
      "turn_taking_patience": "medium",
      "turn_commitment": "high",
      "replica_interruptibility": "low",
      "active_listening": "low"
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

* `turn_detection_model`: `sparrow-0`
* `turn_commitment`: `medium`
* `replica_interruptibility`: `medium`
* `active_listening`: `off`

## Best Practices

### Match Flow to Use Case

Choose conversational flow settings that align with your application's purpose:

* **Speed-critical applications**: Use `low` turn-taking patience
* **Thoughtful conversations**: Use `high` turn-taking patience
* **Important information delivery**: Use `high` turn commitment and `low` interruptibility
* **User-controlled interactions**: Use `low` turn commitment and `high` interruptibility

### Balance Patience and Commitment

The combination of `turn_taking_patience` and `turn_commitment` creates different conversational feels:

| Patience | Commitment | Result                              |
| -------- | ---------- | ----------------------------------- |
| Low      | Low        | Rapid, flexible, back-and-forth     |
| Low      | High       | Quick to start, committed to finish |
| High     | Low        | Thoughtful but flexible             |
| High     | High       | Deliberate, complete responses      |

### Consider Cultural Context

Conversational norms vary across cultures. Some cultures prefer:

* More overlap and interruption (consider lower commitment, higher interruptibility)
* Clear turn-taking with pauses (consider higher patience, lower interruptibility)

### Test with Real Users

Conversational flow preferences can be subjective. Test your configuration with representative users to ensure it feels natural for your audience.

<Note>
  Refer to the <a href="/api-reference/personas/create-persona" target="_blank">Create Persona API</a> for the complete API specification and additional persona configuration options.
</Note>
