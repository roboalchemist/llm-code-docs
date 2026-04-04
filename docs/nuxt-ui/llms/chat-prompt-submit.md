# Source: https://ui.nuxt.com/raw/docs/components/chat-prompt-submit.md

# ChatPromptSubmit

> A Button for submitting chat prompts with automatic status handling.

## Usage

The ChatPromptSubmit component is used inside the [ChatPrompt](/docs/components/chat-prompt) component to submit the prompt. It automatically handles the different `status` values to control the chat.

It extends the [Button](/docs/components/button) component, so you can pass any property such as `color`, `variant`, `size`, etc.

```vue
<template>
  <u-chat-prompt-submit />
  <template v-slot:code=>
  <pre className=language-vue shiki shiki-themes material-theme-lighter material-theme material-theme-palenight code=<template>
    <UChatPrompt>
      <UChatPromptSubmit />
    </UChatPrompt>
  </template>
   language=vue meta= style=>
  <code __ignoreMap=>
  <span class=line>
  <span class=sMK4o>
  <</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
    <</span>
  <span class=swJcz>
  UChatPrompt</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
      <</span>
  <span class=swJcz>
  UChatPromptSubmit</span>
  <span class=sMK4o>
   />
  </span></span>
  <span class=line>
  <span class=sMK4o>
    </</span>
  <span class=swJcz>
  UChatPrompt</span>
  <span class=sMK4o>
  >
  </span></span>
  <span class=line>
  <span class=sMK4o>
  </</span>
  <span class=swJcz>
  template</span>
  <span class=sMK4o>
  >
  </span></span></code></pre></template>
</template>
```

> [!NOTE]
> You can also use it inside the `footer` slot of the [`ChatPrompt`](/docs/components/chat-prompt) component.

### Ready

When its status is `ready`, use the `color`, `variant` and `icon` props to customize the Button. Defaults to:

- `color="primary"`
- `variant="solid"`
- `icon="i-lucide-arrow-up"`

```vue
<template>
  <UChatPromptSubmit color="primary" variant="solid" icon="i-lucide-arrow-up" />
</template>
```

**Nuxt:**
> [!TIP]
> See: /docs/getting-started/integrations/icons/nuxt#theme
> You can customize this icon globally in your `app.config.ts` under `ui.icons.arrowUp` key.

**Vue:**
> [!TIP]
> See: /docs/getting-started/integrations/icons/vue#theme
> You can customize this icon globally in your `vite.config.ts` under `ui.icons.arrowUp` key.

### Submitted

When its status is `submitted`, use the `submitted-color`, `submitted-variant` and `submitted-icon` props to customize the Button. Defaults to:

- `submittedColor="neutral"`
- `submittedVariant="subtle"`
- `submittedIcon="i-lucide-square"`

> [!NOTE]
> The `stop` event is emitted when the user clicks on the Button.

```vue
<template>
  <UChatPromptSubmit submitted-color="neutral" submitted-variant="subtle" submitted-icon="i-lucide-square" status="submitted" />
</template>
```

**Nuxt:**
> [!TIP]
> See: /docs/getting-started/integrations/icons/nuxt#theme
> You can customize this icon globally in your `app.config.ts` under `ui.icons.stop` key.

**Vue:**
> [!TIP]
> See: /docs/getting-started/integrations/icons/vue#theme
> You can customize this icon globally in your `vite.config.ts` under `ui.icons.stop` key.

### Streaming

When its status is `streaming`, use the `streaming-color`, `streaming-variant` and `streaming-icon` props to customize the Button. Defaults to:

- `streamingColor="neutral"`
- `streamingVariant="subtle"`
- `streamingIcon="i-lucide-square"`

> [!NOTE]
> The `stop` event is emitted when the user clicks on the Button.

```vue
<template>
  <UChatPromptSubmit streaming-color="neutral" streaming-variant="subtle" streaming-icon="i-lucide-square" status="streaming" />
</template>
```

**Nuxt:**
> [!TIP]
> See: /docs/getting-started/integrations/icons/nuxt#theme
> You can customize this icon globally in your `app.config.ts` under `ui.icons.stop` key.

**Vue:**
> [!TIP]
> See: /docs/getting-started/integrations/icons/vue#theme
> You can customize this icon globally in your `vite.config.ts` under `ui.icons.stop` key.

### Error

When its status is `error`, use the `error-color`, `error-variant` and `error-icon` props to customize the Button. Defaults to:

- `errorColor="error"`
- `errorVariant="soft"`
- `errorIcon="i-lucide-rotate-ccw"`

> [!NOTE]
> The `reload` event is emitted when the user clicks on the Button.

```vue
<template>
  <UChatPromptSubmit error-color="error" error-variant="soft" error-icon="i-lucide-rotate-ccw" status="error" />
</template>
```

**Nuxt:**
> [!TIP]
> See: /docs/getting-started/integrations/icons/nuxt#theme
> You can customize this icon globally in your `app.config.ts` under `ui.icons.reload` key.

**Vue:**
> [!TIP]
> See: /docs/getting-started/integrations/icons/vue#theme
> You can customize this icon globally in your `vite.config.ts` under `ui.icons.reload` key.

## Examples

> [!TIP]
> See: /docs/components/chat-messages#examples
> Check the ChatMessages documentation for server API setup and installation instructions.

### Within a page

Use the ChatPromptSubmit component with the `Chat` class from AI SDK v5 to display a chat prompt within a page.

Pass the `status` prop and listen to the `stop` and `reload` events to control the chat.

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

## API

### Props

```ts
/**
 * Props for the ChatPromptSubmit component
 */
interface ChatPromptSubmitProps {
  /**
   * @default "\"ready\""
   */
  status?: ChatStatus | undefined;
  /**
   * The icon displayed in the button when the status is `ready`.
   */
  icon?: any;
  /**
   * The color of the button when the status is `ready`.
   */
  color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral" | undefined;
  /**
   * The variant of the button when the status is `ready`.
   */
  variant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link" | undefined;
  /**
   * The icon displayed in the button when the status is `streaming`.
   */
  streamingIcon?: any;
  /**
   * The color of the button when the status is `streaming`.
   * @default "\"neutral\""
   */
  streamingColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral" | undefined;
  /**
   * The variant of the button when the status is `streaming`.
   * @default "\"subtle\""
   */
  streamingVariant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link" | undefined;
  /**
   * The icon displayed in the button when the status is `submitted`.
   */
  submittedIcon?: any;
  /**
   * The color of the button when the status is `submitted`.
   * @default "\"neutral\""
   */
  submittedColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral" | undefined;
  /**
   * The variant of the button when the status is `submitted`.
   * @default "\"subtle\""
   */
  submittedVariant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link" | undefined;
  /**
   * The icon displayed in the button when the status is `error`.
   */
  errorIcon?: any;
  /**
   * The color of the button when the status is `error`.
   * @default "\"error\""
   */
  errorColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral" | undefined;
  /**
   * The variant of the button when the status is `error`.
   * @default "\"soft\""
   */
  errorVariant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link" | undefined;
  ui?: ({ base?: ClassNameValue; } & { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }) | undefined;
  /**
   * The type of the button when not a link.
   */
  type?: "reset" | "submit" | "button" | undefined;
  /**
   * Class to apply when the link is exact active
   */
  exactActiveClass?: string | undefined;
  /**
   * Pass the returned promise of `router.push()` to `document.startViewTransition()` if supported.
   */
  viewTransition?: boolean | undefined;
  autofocus?: Booleanish | undefined;
  disabled?: boolean | undefined;
  form?: string | undefined;
  formaction?: string | undefined;
  formenctype?: string | undefined;
  formmethod?: string | undefined;
  formnovalidate?: Booleanish | undefined;
  formtarget?: string | undefined;
  name?: string | undefined;
  onClick?: ((event: MouseEvent) => void | Promise<void>) | ((event: MouseEvent) => void | Promise<void>)[] | undefined;
  /**
   * The element or component this component should render as when not a link.
   */
  as?: any;
  label?: string | undefined;
  activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral" | undefined;
  activeVariant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link" | undefined;
  size?: "md" | "xs" | "sm" | "lg" | "xl" | undefined;
  /**
   * Render the button with equal padding on all sides.
   */
  square?: boolean | undefined;
  /**
   * Render the button full width.
   */
  block?: boolean | undefined;
  /**
   * Set loading state automatically based on the `@click` promise state
   */
  loadingAuto?: boolean | undefined;
  /**
   * Display an avatar on the left side.
   */
  avatar?: AvatarProps | undefined;
  /**
   * When `true`, the icon will be displayed on the left side.
   */
  leading?: boolean | undefined;
  /**
   * Display an icon on the left side.
   */
  leadingIcon?: any;
  /**
   * When `true`, the icon will be displayed on the right side.
   */
  trailing?: boolean | undefined;
  /**
   * Display an icon on the right side.
   */
  trailingIcon?: any;
  /**
   * When `true`, the loading icon will be displayed.
   */
  loading?: boolean | undefined;
  /**
   * The icon when the `loading` prop is `true`.
   */
  loadingIcon?: any;
}
```

> [!NOTE]
> See: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button#attributes
> This component also supports all native `<button>` HTML attributes.

### Slots

```ts
/**
 * Slots for the ChatPromptSubmit component
 */
interface ChatPromptSubmitSlots {
  leading(): any;
  default(): any;
  trailing(): any;
}
```

### Emits

```ts
/**
 * Emitted events for the ChatPromptSubmit component
 */
interface ChatPromptSubmitEmits {
  stop: (payload: [event: MouseEvent]) => void;
  reload: (payload: [event: MouseEvent]) => void;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    chatPromptSubmit: {
      slots: {
        base: ''
      }
    }
  }
})
```

## Changelog

See the [releases page](https://github.com/nuxt/ui/releases) for the latest changes.
