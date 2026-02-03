# Source: https://ui.nuxt.com/raw/docs/components/chat-palette.md

# ChatPalette

> A chat palette to create a chatbot interface inside an overlay.

## Usage

The ChatPalette component is a structured layout wrapper that organizes [ChatMessages](/docs/components/chat-messages) in a scrollable content area and [ChatPrompt](/docs/components/chat-prompt) in a fixed bottom section, creating cohesive chatbot interfaces for modals, slideovers, or drawers.

```vue
<template>
  <UChatPalette>
    <UChatMessages />

    <template #prompt>
      <UChatPrompt />
    </template>
  </UChatPalette>
</template>
```

## Examples

> [!TIP]
> See: /docs/components/chat-messages#examples
> Check the ChatMessages documentation for server API setup and installation instructions.

### Within a Modal

You can use the ChatPalette component inside a [Modal](/docs/components/modal)'s content.

```vue [ChatPaletteModalExample.vue]
<script setup lang="ts">
import { Chat } from '@ai-sdk/vue'
import type { UIMessage } from 'ai'

const messages: UIMessage[] = []
const input = ref('')

const chat = new Chat({
  messages
})

function onSubmit() {
  chat.sendMessage({ text: input.value })

  input.value = ''
}
</script>

<template>
  <UModal open :ui="{ content: 'sm:max-w-3xl sm:h-[28rem]' }">
    <template #content>
      <UChatPalette>
        <UChatMessages
          :messages="chat.messages"
          :status="chat.status"
          :user="{ side: 'left', variant: 'naked', avatar: { src: 'https://github.com/benjamincanac.png' } }"
          :assistant="{ icon: 'i-lucide-bot' }"
        >
          <template #content="{ message }">
            <template v-for="(part, index) in message.parts" :key="`${message.id}-${part.type}-${index}`">
              <MDC
                v-if="part.type === 'text' && message.role === 'assistant'"
                :value="part.text"
                :cache-key="`${message.id}-${index}`"
                class="[&_.my-5]:my-2.5 *:first:!mt-0 *:last:!mb-0 [&_.leading-7]:!leading-6"
              />
              <p v-else-if="part.type === 'text' && message.role === 'user'" class="whitespace-pre-wrap">
                {{ part.text }}
              </p>
            </template>
          </template>
        </UChatMessages>

        <template #prompt>
          <UChatPrompt
            v-model="input"
            icon="i-lucide-search"
            variant="naked"
            :error="chat.error"
            @submit="onSubmit"
          />
        </template>
      </UChatPalette>
    </template>
  </UModal>
</template>
```

### Within ContentSearch

You can use the ChatPalette component conditionally inside [ContentSearch](/docs/components/content-search)'s content to display a chatbot interface when a user selects an item.

```vue [ChatPaletteContentSearchExample.vue]
<script setup lang="ts">
import { Chat } from '@ai-sdk/vue'
import type { UIMessage } from 'ai'

const messages: UIMessage[] = []
const input = ref('')

const groups = computed(() => [{
  id: 'ai',
  ignoreFilter: true,
  items: [{
    label: searchTerm.value ? `Ask AI for “${searchTerm.value}”` : 'Ask AI',
    icon: 'i-lucide-bot',
    onSelect: (e: any) => {
      e.preventDefault()

      ai.value = true

      if (searchTerm.value) {
        messages.push({
          id: '1',
          role: 'user',
          parts: [{ type: 'text', text: searchTerm.value }]
        })

        chat.regenerate()
      }
    }
  }]
}])

const ai = ref(false)
const searchTerm = ref('')

const chat = new Chat({
  messages
})

function onSubmit() {
  chat.sendMessage({ text: input.value })

  input.value = ''
}

function onClose(e: Event) {
  e.preventDefault()

  ai.value = false
}
</script>

<template>
  <UContentSearch v-model:search-term="searchTerm" open :groups="groups">
    <template v-if="ai" #content>
      <UChatPalette>
        <UChatMessages
          :messages="chat.messages"
          :status="chat.status"
          :user="{ side: 'left', variant: 'naked', avatar: { src: 'https://github.com/benjamincanac.png' } }"
          :assistant="{ icon: 'i-lucide-bot' }"
        >
          <template #content="{ message }">
            <template v-for="(part, index) in message.parts" :key="`${message.id}-${part.type}-${index}`">
              <MDC
                v-if="part.type === 'text' && message.role === 'assistant'"
                :value="part.text"
                :cache-key="`${message.id}-${index}`"
                class="[&_.my-5]:my-2.5 *:first:!mt-0 *:last:!mb-0 [&_.leading-7]:!leading-6"
              />
              <p v-else-if="part.type === 'text' && message.role === 'user'" class="whitespace-pre-wrap">
                {{ part.text }}
              </p>
            </template>
          </template>
        </UChatMessages>

        <template #prompt>
          <UChatPrompt
            v-model="input"
            icon="i-lucide-search"
            variant="naked"
            :error="chat.error"
            @submit="onSubmit"
            @close="onClose"
          />
        </template>
      </UChatPalette>
    </template>
  </UContentSearch>
</template>
```

> [!TIP]
> You can enhance your chatbot with tool calling capabilities using the [Model Context Protocol](https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools) (`@ai-sdk/mcp`). This allows the AI to search your documentation or perform other actions:
> ```ts
> import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js'
> import { streamText, convertToModelMessages, stepCountIs } from 'ai'
> import { experimental_createMCPClient } from '@ai-sdk/mcp'
> import { gateway } from '@ai-sdk/gateway'
> 
> export default defineEventHandler(async (event) => {
>   const { messages } = await readBody(event)
> 
>   const httpTransport = new StreamableHTTPClientTransport(
>     new URL('https://your-app.com/mcp')
>   )
>   const httpClient = await experimental_createMCPClient({
>     transport: httpTransport
>   })
>   const tools = await httpClient.tools()
> 
>   return streamText({
>     model: gateway('anthropic/claude-sonnet-4.5'),
>     maxOutputTokens: 10000,
>     system: 'You are a helpful assistant. Use your tools to search for relevant information before answering questions.',
>     messages: await convertToModelMessages(messages),
>     stopWhen: stepCountIs(6),
>     tools,
>     onFinish: async () => {
>       await httpClient.close()
>     },
>     onError: async (error) => {
>       console.error(error)
>       await httpClient.close()
>     }
>   }).toUIMessageStreamResponse()
> })
> 
> ```

## API

### Props

```ts
/**
 * Props for the ChatPalette component
 */
interface ChatPaletteProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
  ui?: { root?: ClassNameValue; prompt?: ClassNameValue; close?: ClassNameValue; content?: ClassNameValue; } | undefined;
}
```

### Slots

```ts
/**
 * Slots for the ChatPalette component
 */
interface ChatPaletteSlots {
  default(): any;
  prompt(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    chatPalette: {
      slots: {
        root: 'relative flex-1 flex flex-col min-h-0 min-w-0',
        prompt: 'px-0 rounded-t-none border-t border-default',
        close: '',
        content: 'overflow-y-auto flex-1 flex flex-col py-3'
      }
    }
  }
})
```

## Changelog

See the [releases page](https://github.com/nuxt/ui/releases) for the latest changes.
