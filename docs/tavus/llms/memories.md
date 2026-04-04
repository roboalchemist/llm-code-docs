# Source: https://docs.tavus.io/sections/conversational-video-interface/memories.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Memories

> Memories let personas remember information across conversations, allowing participants to have personalized, flowing conversations across multiple sessions.

Memories are pieces of information that the persona learns during a conversation. Once learned, these memories can be referenced and used by the persona during subsequent conversations.

Developers are able to organize memories within `memory_stores` - a flexible tag-based system to track memories across conversations and participants into different buckets.
If a `memory_stores` value is provided in the conversation creation request, memories will automatically be created and associated to the tag provided.

<Note>
  When defining `memory_stores` values, we recommend incorporating static values that will not change with persona updates, like persona ID.

  For example, using a persona's name as part of your `memory_stores` values could result in memories being miscategorized if you were to change their name.
</Note>

## Basic Example

For example, if a participant named Anna starts a conversation with the persona (Charlie, with the persona ID `p123`), we can specify `memory_stores=["anna_p123"]` in the conversation creation request.
By doing so, Charlie will:

* Remember what was mentioned in a conversation and form new memories with Anna.
* Reference memories from previous conversations that Charlie had with Anna in new conversations.

Example [conversation creation](https://docs.tavus.io/api-reference/conversations/create-conversation) request body:

```json  theme={null}
{
  "persona_id": "your_persona_id",
  "replica_id": "your_replica_id",
  "memory_stores": ["anna_p123"]
}
```

## Managing Memories Between Participants and Conversations

<Note>
  To prevent different personas from mixing up information for the same participant, we generally recommend you to create separate `memory_stores` values for each user when they talk to different personas.

  For example,\`

  * When Anna talks to Charlie (persona ID of `p123`), you can use the `memory_stores` value of `["anna-p123"]`.
  * when she talks with Gloria (persona ID of `p456`), you can use the `memory_stores` value of `["anna-p456"]`.
</Note>

The `memory_stores` system can be used flexibly to cover your use cases - they do not have to map 1:1 with your participants and instead can be designed for your unique use cases.

For example,

* If you were setting up an online classroom, you could use a `memory_stores` tag value of `"classroom-1"` so any participant of this group could reference and create new memories to enhance and deepen learning and connections.
* You can control whether you want personas to share memory or not (and if so, which personas) by passing them different `memory_stores` values.
