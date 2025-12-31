# Source: https://docs.livekit.io/agents/logic/turns.md

# Source: https://docs.livekit.io/agents/build/turns.md

LiveKit docs › Building voice agents › Turn detection & interruptions › Overview

---

# Turn detection and interruptions

> Guide to managing conversation turns in voice AI.

## Overview

Turn detection is the process of determining when a user begins or ends their "turn" in a conversation. This lets the agent know when to start listening and when to respond.

Most turn detection techniques rely on voice activity detection (VAD) to detect periods of silence in user input. The agent applies heuristics to the VAD data to perform phrase endpointing, which determines the end of a sentence or thought. The agent can use endpoints alone or apply more contextual analysis to determine when a turn is complete.

Effective turn detection and interruption management is essential to great voice AI experiences.

## Turn detection

The `AgentSession` supports the following turn detection modes, in addition to manual turn control that's always available.

- **Turn detector model**: A custom, open-weights model for context-aware turn detection on top of VAD or STT endpoint data.
- **Realtime models**: Support for the built-in turn detection or VAD in realtime models like the OpenAI Realtime API.
- **VAD only**: Detect end of turn from speech and silence data alone.
- **STT endpointing**: Use phrase endpoints returned in realtime STT data from your chosen provider.
- **Manual turn control**: Disable automatic turn detection entirely.

### Turn detector model

To achieve the recommended behavior of an agent that listens while the user speaks and replies after they finish their thought, use the following plugins in an STT-LLM-TTS pipeline:

- **[Turn detection model](https://docs.livekit.io/agents/build/turns/turn-detector.md)**: Open-weights model for contextually-aware turn detection.

- **[Silero VAD](https://docs.livekit.io/agents/build/turns/vad.md)**: Silero VAD model for voice activity detection.

**Python**:

```python
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.plugins import silero

session = AgentSession(
    turn_detection=MultilingualModel(), # or EnglishModel()
    vad=silero.VAD.load(),
    # ... stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';
import * as livekit from '@livekit/agents-plugin-livekit';
import * as silero from '@livekit/agents-plugin-silero';

const session = new voice.AgentSession({
  turnDetection: new livekit.turnDetector.MultilingualModel(), // or EnglishModel()
  vad: await silero.VAD.load(),
  // ... stt, tts, llm, etc.
});

```

See the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md) for a complete example.

> 💡 **Realtime model turn detection**
> 
> For a realtime model, LiveKit recommends using the built-in turn detection capabilities of the [chosen model provider](https://docs.livekit.io/agents/models/realtime.md). This is the most cost-effective option, since the custom turn detection model requires realtime speech-to-text (STT) that would need to run separately.

### Realtime models

Realtime models include built-in turn detection options based on VAD and other techniques. Leave the `turn_detection` parameter unset and configure the realtime model's turn detection options directly.

To use the LiveKit turn detector model with a realtime model, you must also provide an STT plugin. The turn detector model operates on STT output.

- **[OpenAI Realtime API turn detection](https://docs.livekit.io/agents/models/realtime/plugins/openai.md#turn-detection)**: Turn detection options for the OpenAI Realtime API.

- **[Gemini Live API turn detection](https://docs.livekit.io/agents/models/realtime/plugins/gemini.md#turn-detection)**: Turn detection options for the Gemini Live API.

### VAD only

In some cases, VAD is the best option for turn detection. For example, VAD works with any spoken language. To use VAD alone, use the Silero VAD plugin and set `turn_detection="vad"`.

**Python**:

```python
session = AgentSession(
    turn_detection="vad",
    vad=silero.VAD.load(),
    # ... stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';
import * as silero from '@livekit/agents-plugin-silero';

const session = new voice.AgentSession({
  turnDetection: 'vad',
  vad: await silero.VAD.load(),
  // ... stt, tts, llm, etc.
});

```

### STT endpointing

You can also use your STT model's built-in phrase endpointing features for turn detection. Some providers, including [AssemblyAI](https://docs.livekit.io/agents/models/stt/plugins/assemblyai.md), include sophisticated semantic turn detection models.

You should still provide a VAD plugin for responsive interruption handling. When you use STT endpointing only, your agent is less responsive to user interruptions.

To use STT endpointing, set `turn_detection="stt"` and provide an STT plugin.

**Python**:

```python
session = AgentSession(
    turn_detection="stt",
    stt=assemblyai.STT(), # AssemblyAI is the recommended STT plugin for STT-based endpointing
    vad=silero.VAD.load(), # Recommended for responsive interruption handling
    # ... tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';
import * as assemblyai from '@livekit/agents-plugin-assemblyai';
import * as silero from '@livekit/agents-plugin-silero';

const session = new voice.AgentSession({
  turnDetection: 'stt',
  stt: new assemblyai.STT(), // AssemblyAI is the recommended STT plugin for STT-based endpointing
  vad: await silero.VAD.load(), // Recommended for responsive interruption handling
  // ... tts, llm, etc.
});

```

### Manual turn control

Disable automatic turn detection entirely by setting `turn_detection="manual"` in the `AgentSession` constructor.

You can control the user's turn with `session.interrupt()`, `session.clear_user_turn()`, and `session.commit_user_turn()` methods.

> 💡 **Tip**
> 
> This is different from toggling audio input/output for [text-only sessions](https://docs.livekit.io/agents/build/text.md#text-only-sessions).

For instance, you can use this to implement a push-to-talk interface. Here is a simple example using [RPC](https://docs.livekit.io/home/client/data/rpc.md) methods that the frontend can call:

**Python**:

```python
session = AgentSession(
    turn_detection="manual",
    # ... stt, tts, llm, etc.
)

# Disable audio input at the start
session.input.set_audio_enabled(False)

# When user starts speaking
@ctx.room.local_participant.register_rpc_method("start_turn")
async def start_turn(data: rtc.RpcInvocationData):
    session.interrupt()  # Stop any current agent speech
    session.clear_user_turn()  # Clear any previous input
    session.input.set_audio_enabled(True)  # Start listening

# When user finishes speaking
@ctx.room.local_participant.register_rpc_method("end_turn")
async def end_turn(data: rtc.RpcInvocationData):
    session.input.set_audio_enabled(False)  # Stop listening
    session.commit_user_turn()  # Process the input and generate response

# When user cancels their turn
@ctx.room.local_participant.register_rpc_method("cancel_turn")
async def cancel_turn(data: rtc.RpcInvocationData):
    session.input.set_audio_enabled(False)  # Stop listening
    session.clear_user_turn()  # Discard the input

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

const session = new voice.AgentSession({
  turnDetection: 'manual',
  // ... stt, tts, llm, etc.
});

// Disable audio input at the start
session.input.setAudioEnabled(false);

// When user starts speaking
ctx.room.localParticipant.registerRpcMethod('start_turn', async (data) => {
  session.interrupt(); // Stop any current agent speech
  session.clearUserTurn(); // Clear any previous input
  session.input.setAudioEnabled(true); // Start listening
  return 'ok';
});

// When user finishes speaking
ctx.room.localParticipant.registerRpcMethod('end_turn', async (data) => {
  session.input.setAudioEnabled(false); // Stop listening
  session.commitUserTurn(); // Process the input and generate response
  return 'ok';
});

// When user cancels their turn
ctx.room.localParticipant.registerRpcMethod('cancel_turn', async (data) => {
  session.input.setAudioEnabled(false); // Stop listening
  session.clearUserTurn(); // Discard the input
  return 'ok';
});

```

A more complete example is available here:

- **[Push-to-Talk Agent](https://github.com/livekit/agents/blob/main/examples/voice_agents/push_to_talk.py)**: A voice AI agent that uses push-to-talk for controlled multi-participant conversations, only enabling audio input when explicitly triggered.

### Reducing background noise

[Enhanced noise cancellation](https://docs.livekit.io/home/cloud/noise-cancellation.md) is available in LiveKit Cloud and improves the quality of turn detection and speech-to-text (STT) for voice AI apps. You can add background noise and voice cancellation to your agent by adding it to the `room_input_options` when you start your agent session. To learn how to enable it, see the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md).

## Interruptions

The framework pauses the agent's speech whenever it detects user speech in the input audio, ensuring the agent feels responsive. The user can interrupt the agent at any time, either by speaking (with automatic turn detection) or via the `session.interrupt()` method. When interrupted, the agent stops speaking and automatically truncates its conversation history to include only the portion of the speech that the user heard before interruption.

> ℹ️ **Disabling interruptions**
> 
> You can disable user interruptions when [scheduling speech](https://docs.livekit.io/agents/build/audio.md#initiating-speech) using the `say()` or `generate_reply()` methods by setting `allow_interruptions=False`.

To explicitly interrupt the agent, call the `interrupt()` method on the handle or session at any time. This can be performed even when `allow_interruptions` is set to `False`.

**Python**:

```python
handle = session.say("Hello world")
handle.interrupt()

# or from the session
session.interrupt()

```

---

**Node.js**:

```typescript
const handle = session.say('Hello world');
handle.interrupt();

// or from the session
session.interrupt();

```

> 💡 **Long-running tool calls**
> 
> See the section on tool [interruptions](https://docs.livekit.io/agents/build/tools.md#interruptions) for more information on handling interruptions during long-running tool calls.

### False interruptions

In some cases, an interruption is a false positive where no actual user speech occurs. The framework identifies this by detecting the absence of recognized words. By default, the agent resumes speaking from where it left off after a false interruption. You can configure this behavior using the `resume_false_interruption` and `false_interruption_timeout` parameters on the agent session.

## Session configuration

The following parameters related to turn detection and interruptions are available on the `AgentSession` constructor:

- **`allow_interruptions`** _(bool)_ (optional) - Default: `True`: Whether to allow the user to interrupt the agent mid-turn. Ignored when using a realtime model with built-in turn detection.

- **`discard_audio_if_uninterruptible`** _(bool)_ (optional) - Default: `True`: When `True`, buffered audio is dropped while the agent is speaking and cannot be interrupted.

- **`min_interruption_duration`** _(float)_ (optional) - Default: `0.5`: Minimum detected speech duration before triggering an interruption.

- **`min_interruption_words`** _(int)_ (optional) - Default: `0`: Minimum number of words to consider an interruption, only used if STT is enabled.

- **`min_endpointing_delay`** _(float)_ (optional) - Default: `0.5`: The number of seconds to wait before considering the turn complete. The session uses this delay when no turn detector model is present, or when the model indicates a likely turn boundary.

- **`max_endpointing_delay`** _(float)_ (optional) - Default: `6.0`: The maximum time to wait for the user to speak after the turn detector model indicates the user is likely to continue speaking. This parameter has no effect without the turn detector model.

- **`false_interruption_timeout`** _(float)_ (optional) - Default: `2.0`: The time (in seconds) to wait before signaling a false interruption. If no transcribed speech is generated during this period, an `agent_false_interruption` event is emitted and the agent resumes speaking from where it left off if `resume_false_interruption` is `True`.

Set to `None` to turn off false interruption handling. When disabled, false interruptions are treated as intentional: the agent's speech is not resumed and no `agent_false_interruption` event is emitted.

- **`resume_false_interruption`** _(bool)_ (optional) - Default: `True`: Determines whether the agent resumes speech output after a false interruption. When set to `True`, the agent continues speaking from where it left off after the time specified by the `false_interruption_timeout` parameter has passed if no user transcription is generated.

## Turn-taking events

The `AgentSession` exposes user and agent state events to monitor the flow of a conversation:

**Python**:

```python
from livekit.agents import UserStateChangedEvent, AgentStateChangedEvent

@session.on("user_state_changed")
def on_user_state_changed(ev: UserStateChangedEvent):
    if ev.new_state == "speaking":
        print("User started speaking")
    elif ev.new_state == "listening":
        print("User stopped speaking")
    elif ev.new_state == "away":
        print("User is not present (e.g. disconnected)")

@session.on("agent_state_changed")
def on_agent_state_changed(ev: AgentStateChangedEvent):
    if ev.new_state == "initializing":
        print("Agent is starting up")
    elif ev.new_state == "idle":
        print("Agent is ready but not processing")
    elif ev.new_state == "listening":
        print("Agent is listening for user input")
    elif ev.new_state == "thinking":
        print("Agent is processing user input and generating a response")
    elif ev.new_state == "speaking":
        print("Agent started speaking")

```

---

**Node.js**:

```typescript
import { voice } from '@livekit/agents';

session.on(voice.AgentSessionEventTypes.UserStateChanged, (ev) => {
  if (ev.newState === 'speaking') {
    console.log('User started speaking');
  } else if (ev.newState === 'listening') {
    console.log('User stopped speaking');
  } else if (ev.newState === 'away') {
    console.log('User is not present (e.g. disconnected)');
  }
});

session.on(voice.AgentSessionEventTypes.AgentStateChanged, (ev) => {
  if (ev.newState === 'initializing') {
    console.log('Agent is starting up');
  } else if (ev.newState === 'idle') {
    console.log('Agent is ready but not processing');
  } else if (ev.newState === 'listening') {
    console.log('Agent is listening for user input');
  } else if (ev.newState === 'thinking') {
    console.log('Agent is processing user input and generating a response');
  } else if (ev.newState === 'speaking') {
    console.log('Agent started speaking');
  }
});

```

## Additional resources

- **[Agent speech](https://docs.livekit.io/agents/build/audio.md)**: Guide to agent speech and related methods.

- **[Pipeline nodes](https://docs.livekit.io/agents/build/nodes.md)**: Monitor input and output as it flows through the voice pipeline.

---

This document was rendered at 2025-11-18T23:55:04.699Z.
For the latest version of this document, see [https://docs.livekit.io/agents/build/turns.md](https://docs.livekit.io/agents/build/turns.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).