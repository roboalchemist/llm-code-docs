# Source: https://ui.nuxt.com/raw/docs/components/chat-prompt.md

# ChatPrompt

> An enhanced Textarea for submitting prompts in AI chat interfaces.

## Usage

The ChatPrompt component renders a `<form>` element and extends the [Textarea](/docs/components/textarea) component so you can pass any property such as `icon`, `placeholder`, `autofocus`, etc.

```vue
<template>
  <u-chat-prompt variant=subtle>
  <u-chat-prompt-submit color=neutral />
  <template v-slot:footer=>
  <u-select :items=[{"label":"Gemini 2.5 Pro","value":"gemini-2.5-pro","icon":"i-simple-icons-googlegemini"},{"label":"GPT-4o","value":"gpt-4o","icon":"i-simple-icons-openai"},{"label":"Claude 3.5 Sonnet","value":"claude-3.5-sonnet","icon":"i-simple-icons-anthropic"},{"label":"Llama 4","value":"llama-4","icon":"i-simple-icons-ollama"}] icon=i-simple-icons-openai modelValue=gpt-4o placeholder=Select a model variant=ghost /></template></u-chat-prompt>
</template>
```

> [!NOTE]
> The ChatPrompt handles the following events:The form is submitted when the user presses  or when the user clicks on the submit button.The textarea is blurred when  is pressed and emits a `close` event.

### Variant

Use the `variant` prop to change the style of the prompt. Defaults to `outline`.

```vue
<template>
  <UChatPrompt variant="soft" />
</template>
```

## Examples

> [!TIP]
> See: /docs/components/chat-messages#examples
> Check the ChatMessages documentation for server API setup and installation instructions.

### Within a page

Use the ChatPrompt component with the `Chat` class from AI SDK v5 to display a chat prompt within a page.

Pass the `input` prop alongside the `error` prop to disable the textarea when an error occurs.

```vue [pages/[id].vue]
<script setup lang="ts">
import { Chat } from '@ai-sdk/vue'

const input = ref('')

const chat = new Chat({
  onError(error) {
    console.error(error)
  }
})

function onSubmit() {
  chat.sendMessage({ text: input.value })

  input.value = ''
}
</script>

<template>
  <UDashboardPanel>
    <template #body>
      <UContainer>
        <UChatMessages :messages="chat.messages" :status="chat.status">
          <template #content="{ message }">
            <template v-for="(part, index) in message.parts" :key="`${message.id}-${part.type}-${index}`">
              <MDC v-if="part.type === 'text' && message.role === 'assistant'" :value="part.text" :cache-key="`${message.id}-${index}`" class="*:first:mt-0 *:last:mb-0" />
              <p v-else-if="part.type === 'text' && message.role === 'user'" class="whitespace-pre-wrap">{{ part.text }}</p>
            </template>
          </template>
        </UChatMessages>
      </UContainer>
    </template>

    <template #footer>
      <UContainer class="pb-4 sm:pb-6">
        <UChatPrompt v-model="input" :error="chat.error" @submit="onSubmit">
          <UChatPromptSubmit :status="chat.status" @stop="chat.stop()" @reload="chat.regenerate()" />
        </UChatPrompt>
      </UContainer>
    </template>
  </UDashboardPanel>
</template>
```

You can also use it as a starting point for a chat interface.

```vue [pages/index.vue]
<script setup lang="ts">
import { Chat } from '@ai-sdk/vue'

const input = ref('')

const chat = new Chat()

async function onSubmit() {
  chat.sendMessage({ text: input.value })

  // Navigate to chat page after first message
  if (chat.messages.length === 1) {
    await navigateTo('/chat')
  }
}
</script>

<template>
  <UDashboardPanel>
    <template #body>
      <UContainer>
        <h1>How can I help you today?</h1>

        <UChatPrompt v-model="input" @submit="onSubmit">
          <UChatPromptSubmit :status="chat.status" />
        </UChatPrompt>
      </UContainer>
    </template>
  </UDashboardPanel>
</template>
```

## API

### Props

```ts
/**
 * Props for the ChatPrompt component
 */
interface ChatPromptProps {
  /**
   * The element or component this component should render as.
   * @default "\"form\""
   */
  as?: any;
  /**
   * The placeholder text for the textarea.
   */
  placeholder?: string | undefined;
  variant?: "outline" | "soft" | "subtle" | "naked" | undefined;
  error?: Error | undefined;
  ui?: ({ root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; base?: ClassNameValue; } & { root?: ClassNameValue; base?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailing?: ClassNameValue; trailingIcon?: ClassNameValue; }) | undefined;
  /**
   * @default "true"
   */
  autofocus?: boolean | undefined;
  disabled?: boolean | undefined;
  /**
   * Display an icon based on the `leading` and `trailing` props.
   */
  icon?: any;
  /**
   * Display an avatar on the left side.
   */
  avatar?: AvatarProps | undefined;
  /**
   * When `true`, the loading icon will be displayed.
   */
  loading?: boolean | undefined;
  /**
   * The icon when the `loading` prop is `true`.
   */
  loadingIcon?: any;
  /**
   * @default "1"
   */
  rows?: number | undefined;
  autofocusDelay?: number | undefined;
  /**
   * @default "true"
   */
  autoresize?: boolean | undefined;
  autoresizeDelay?: number | undefined;
  maxrows?: number | undefined;
  /**
   * @default "\"\""
   */
  modelValue?: string | undefined;
}
```

> [!NOTE]
> See: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea#attributes
> This component also supports all native `<textarea>` HTML attributes.

### Slots

```ts
/**
 * Slots for the ChatPrompt component
 */
interface ChatPromptSlots {
  header(): any;
  footer(): any;
  leading(): any;
  default(): any;
  trailing(): any;
}
```

### Emits

```ts
/**
 * Emitted events for the ChatPrompt component
 */
interface ChatPromptEmits {
  close: (payload: [event: Event]) => void;
  submit: (payload: [event: Event]) => void;
  update:modelValue: (payload: [value: string]) => void;
}
```

### Expose

When accessing the component via a template ref, you can use the following:

<table>
<thead>
  <tr>
    <th>
      Name
    </th>
    
    <th>
      Type
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code className="language-ts-type shiki shiki-themes material-theme-lighter material-theme material-theme-palenight" language="ts-type" style="">
        <span class="sBMFI">
          textareaRef
        </span>
      </code>
    </td>
    
    <td>
      <code className="language-ts-type shiki shiki-themes material-theme-lighter material-theme material-theme-palenight" language="ts-type" style="">
        <span class="sBMFI">
          Ref
        </span>
        
        <span class="sMK4o">
          <
        </span>
        
        <span class="sBMFI">
          HTMLTextAreaElement
        </span>
        
        <span class="sMK4o">
          |
        </span>
        
        <span class="sBMFI">
          null
        </span>
        
        <span class="sMK4o">
          >
        </span>
      </code>
    </td>
  </tr>
</tbody>
</table>

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    chatPrompt: {
      slots: {
        root: 'relative flex flex-col items-stretch gap-2 px-2.5 py-2 w-full rounded-lg backdrop-blur',
        header: 'flex items-center gap-1.5',
        body: 'items-start',
        footer: 'flex items-center justify-between gap-1.5',
        base: 'text-base/5'
      },
      variants: {
        variant: {
          outline: {
            root: 'bg-default/75 ring ring-default'
          },
          soft: {
            root: 'bg-elevated/50'
          },
          subtle: {
            root: 'bg-elevated/50 ring ring-default'
          },
          naked: {
            root: ''
          }
        }
      },
      defaultVariants: {
        variant: 'outline'
      }
    }
  }
})
```

## Changelog

See the [releases page](https://github.com/nuxt/ui/releases) for the latest changes.
