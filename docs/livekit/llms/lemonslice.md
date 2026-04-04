# Source: https://docs.livekit.io/agents/models/avatar/plugins/lemonslice.md

LiveKit docs › Models › Virtual avatar › Plugins › LemonSlice

---

# LemonSlice virtual avatar integration guide

> How to use the LemonSlice virtual avatar plugin for LiveKit Agents.

Available in:
- [ ] Node.js
- [x] Python

## Overview

[LemonSlice](https://www.lemonslice.com/) provides lifelike realtime avatars that naturally interact with users. You can use the open source LemonSlice integration for LiveKit Agents to seamlessly add virtual avatars to your voice AI app.

## Quick reference

This section includes a basic usage example and some reference material. For links to more detailed documentation, see [Additional resources](#additional-resources).

### Installation

Install the plugin from PyPI:

```shell
uv add "livekit-plugins-lemonslice~=1.3"

```

### Authentication

The LemonSlice plugin requires a [LemonSlice API key](https://lemonslice.com/docs/api-reference/authentication).

Set `LEMONSLICE_API_KEY` in your `.env` file.

### Avatar setup

The LemonSlice plugin requires either a base image set by `agent_image_url` or an agent ID set by `agent_id` to start an avatar session. Only one of these parameters can be configured.

#### Agent Image URL

The LemonSlice plugin accepts a source image URL from which to generate the avatar. The avatars render as 368x560 pixel videos. LemonSlice will automatically center-crop your image to the target aspect ratio if the dimensions do not match the expected values. LemonSlice supports a wide range of faces, from humanoid to animal, and styles from photorealistic to animated. Best results are achieved with anthropomorphic images where the face and mouth are clearly identifiable. The image URL must be publicly accessible and return an image/* content type.

#### Agent ID

To use an existing LemonSlice agent as your avatar, set the `agent_id` in `AvatarSession`. You can find the agent ID in the [LemonSlice agent dashboard](https://lemonslice.com/agents). You can also create new LemonSlice agents through the [agent creation flow](https://lemonslice.com/agents/create) by specifying an image.

> ℹ️ **Note**
> 
> LiveKit TTS settings will supersede selected voices and personalities configured for the LemonSlice agent.

### Usage

Use the plugin in an `AgentSession`. For example, you can use this avatar in the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md).

```python
from livekit import agents
from livekit.agents import AgentServer, AgentSession
from livekit.plugins import lemonslice

server = AgentServer() 

@server.rtc_session()
async def my_agent(ctx: agents.JobContext):
    session = AgentSession(
        # ... stt, llm, tts, etc.
    ) 
    
    avatar = lemonslice.AvatarSession(
        # Publicly accessible image URL for the avatar
        agent_image_url="...",
        # Prompt to guide the avatar's movements
        agent_prompt="Be expressive in your movements and use your hands while talking."
    )
    
    # Start the avatar and wait for it to join
    await avatar.start(session, room=ctx.room)
    
    # Start your agent session with the user
    await session.start(
        # ... room, agent, room_options, etc....
    )

```

Preview the avatar in the [Agents Playground](https://docs.livekit.io/agents/start/playground.md) or a frontend [starter app](https://docs.livekit.io/agents/start/frontend.md#starter-apps) that you build.

### Parameters

This section describes some of the available parameters. See the [plugin reference](https://docs.livekit.io/reference/python/v1/livekit/plugins/lemonslice/index.html.md#livekit.plugins.lemonslice.AvatarSession) for a complete list of all available parameters.

- **`agent_image_url`** _(string)_ (optional): Publicly accessible image url for the avatar. See [Agent Image Setup](#agent-image-url) for details.

- **`agent_id`** _(string)_ (optional): The ID of the LemonSlice agent to use. See [Agent ID Setup](#agent-id) for details.

- **`agent_prompt`** _(string)_ (optional): A high-level system prompt that subtly influences the avatar's movements, expressions, and emotional demeanor. This prompt is best used to suggest general affect or behavior (e.g., "feel excited" or "look sad") rather than precise or deterministic actions.

- **`idle_timeout`** _(int)_ (optional): Idle timeout in seconds. The avatar will leave the session if this timeout is hit. Defaults to 60 seconds. If a negative number is provided, the session will have no idle timeout.

## Additional resources

The following resources provide more information about using LemonSlice with LiveKit Agents.

- **[Python package](https://pypi.org/project/livekit-plugins-lemonslice/)**: The `livekit-plugins-lemonslice` package on PyPI.

- **[Plugin reference](https://docs.livekit.io/reference/python/v1/livekit/plugins/lemonslice/index.html.md)**: Reference for the LemonSlice avatar plugin.

- **[GitHub repo](https://github.com/livekit/agents/tree/main/livekit-plugins/livekit-plugins-lemonslice)**: View the source or contribute to the LiveKit LemonSlice avatar plugin.

- **[LemonSlice docs](https://lemonslice.com/docs/api-reference/overview)**: LemonSlice's full docs site.

- **[Agents Playground](https://docs.livekit.io/agents/start/playground.md)**: A virtual workbench to test your avatar agent.

- **[Frontend starter apps](https://docs.livekit.io/agents/start/frontend.md#starter-apps)**: Ready-to-use frontend apps with avatar support.

---

This document was rendered at 2026-02-03T03:25:07.524Z.
For the latest version of this document, see [https://docs.livekit.io/agents/models/avatar/plugins/lemonslice.md](https://docs.livekit.io/agents/models/avatar/plugins/lemonslice.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).