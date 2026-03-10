# CopilotTextarea

An AI-powered textarea component for your application, which serves as a drop-in replacement for any textarea.

![](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/CopilotTextarea.gif)

`<CopilotTextarea>` is a React component that acts as a drop-in replacement for the standard `<textarea>`,
offering enhanced autocomplete features powered by AI. It is context-aware, integrating seamlessly with the
[`useCopilotReadable`](https://docs.copilotkit.ai/reference/hooks/useCopilotReadable) hook to provide intelligent suggestions based on the application context.

In addition, it provides a hovering editor window (available by default via `Cmd + K` on Mac and `Ctrl + K` on Windows) that allows the user to
suggest changes to the text, for example providing a summary or rephrasing the text.

## [Example](https://docs.copilotkit.ai/reference/components/CopilotTextarea\#example)

```
import { CopilotTextarea } from '@copilotkit/react-textarea';
import "@copilotkit/react-textarea/styles.css";

<CopilotTextarea
  autosuggestionsConfig={{
    textareaPurpose:
     "the body of an email message",
    chatApiConfigs: {},
  }}
/>
```

## [Usage](https://docs.copilotkit.ai/reference/components/CopilotTextarea\#usage)

### [Install Dependencies](https://docs.copilotkit.ai/reference/components/CopilotTextarea\#install-dependencies)

This component is part of the [@copilotkit/react-textarea](https://npmjs.com/package/@copilotkit/react-textarea) package.

```
npm install @copilotkit/react-core @copilotkit/react-textarea
```

### [Usage](https://docs.copilotkit.ai/reference/components/CopilotTextarea\#usage-1)

Use the CopilotTextarea component in your React application similarly to a standard `<textarea />`,
with additional configurations for AI-powered features.

For example:

```
import { useState } from "react";
import { CopilotTextarea } from "@copilotkit/react-textarea";
import "@copilotkit/react-textarea/styles.css";

export function ExampleComponent() {
  const [text, setText] = useState("");

  return (
    <CopilotTextarea
      className="custom-textarea-class"
      value={text}
      onValueChange={(value: string) => setText(value)}
      placeholder="Enter your text here..."
      autosuggestionsConfig={{
        textareaPurpose: "Provide context or purpose of the textarea.",
        chatApiConfigs: {
          suggestionsApiConfig: {
            maxTokens: 20,
            stop: [".", "?", "!"],
          },
        },
      }}
    />
  );
}
```

### [Look & Feel](https://docs.copilotkit.ai/reference/components/CopilotTextarea\#look--feel)

By default, CopilotKit components do not have any styles. You can import CopilotKit's stylesheet at the root of your project:

YourRootComponent.tsx

```
...
import "@copilotkit/react-textarea/styles.css";

export function YourRootComponent() {
  return (
    <CopilotKit>
      ...
    </CopilotKit>
  );
}
```

For more information about how to customize the styles, check out the [Customize Look & Feel](https://docs.copilotkit.ai/guides/custom-look-and-feel/customize-built-in-ui-components) guide.

## [Properties](https://docs.copilotkit.ai/reference/components/CopilotTextarea\#properties)

disableBrandingboolean

Determines whether the CopilotKit branding should be disabled. Default is `false`.

placeholderStyleReact.CSSProperties

Specifies the CSS styles to apply to the placeholder text.

suggestionsStyleReact.CSSProperties

Specifies the CSS styles to apply to the suggestions list.

hoverMenuClassnamestring

A class name to apply to the editor popover window.

valuestring

The initial value of the textarea. Can be controlled via `onValueChange`.

onValueChange(value: string) => void

Callback invoked when the value of the textarea changes.

onChange(event: React.ChangeEvent<HTMLTextAreaElement>) => void

Callback invoked when a `change` event is triggered on the textarea element.

shortcutstring

The shortcut to use to open the editor popover window. Default is `"Cmd-k"`.

autosuggestionsConfigAutosuggestionsConfigUserSpecifiedrequired

Configuration settings for the autosuggestions feature.
For full reference, [check the interface on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/CopilotKit/packages/react-textarea/src/types/base/base-copilot-textarea-props.tsx#L8).

textareaPurposestringrequired

The purpose of the text area in plain text.

Example: "The body of the email response"

chatApiConfigsChatApiConfigs

The chat API configurations.

**NOTE:** You must provide specify at least one of `suggestionsApiConfig` or `insertionApiConfig`.

suggestionsApiConfigSuggestionsApiConfig

For full reference, please [click here](https://github.com/CopilotKit/CopilotKit/blob/main/CopilotKit/packages/react-textarea/src/types/autosuggestions-config/suggestions-api-config.tsx#L4).

insertionApiConfigInsertionApiConfig

For full reference, please [click here](https://github.com/CopilotKit/CopilotKit/blob/main/CopilotKit/packages/react-textarea/src/types/autosuggestions-config/insertions-api-config.tsx#L4).

disabledboolean

Whether the textarea is disabled.

disableBrandingboolean

Whether to disable the CopilotKit branding.

placeholderStyleReact.CSSProperties

Specifies the CSS styles to apply to the placeholder text.

suggestionsStyleReact.CSSProperties

Specifies the CSS styles to apply to the suggestions list.

hoverMenuClassnamestring

A class name to apply to the editor popover window.

valuestring

The initial value of the textarea. Can be controlled via `onValueChange`.

onValueChange(value: string) => void

Callback invoked when the value of the textarea changes.

onChange(event: React.ChangeEvent<HTMLTextAreaElement>) => void

Callback invoked when a `change` event is triggered on the textarea element.

shortcutstring

The shortcut to use to open the editor popover window. Default is `"Cmd-k"`.

[Previous\\
\\
CopilotSidebar](https://docs.copilotkit.ai/reference/components/chat/CopilotSidebar) [Next\\
\\
CopilotKit](https://docs.copilotkit.ai/reference/components/CopilotKit)

### On this page

[Example](https://docs.copilotkit.ai/reference/components/CopilotTextarea#example) [Usage](https://docs.copilotkit.ai/reference/components/CopilotTextarea#usage) [Install Dependencies](https://docs.copilotkit.ai/reference/components/CopilotTextarea#install-dependencies) [Usage](https://docs.copilotkit.ai/reference/components/CopilotTextarea#usage-1) [Look & Feel](https://docs.copilotkit.ai/reference/components/CopilotTextarea#look--feel) [Properties](https://docs.copilotkit.ai/reference/components/CopilotTextarea#properties)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/components/CopilotTextarea.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CopilotKit Quickstart Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageInstall CopilotKit