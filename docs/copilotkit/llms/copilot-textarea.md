# Copilot Textarea

Learn how to use the Copilot Textarea for AI-powered autosuggestions.

![](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/CopilotTextarea.gif)

`<CopilotTextarea>` is a React component that acts as a drop-in replacement for the standard `<textarea>`,
offering enhanced autocomplete features powered by AI. It is context-aware, integrating seamlessly with the
[`useCopilotReadable`](https://docs.copilotkit.ai/reference/hooks/useCopilotReadable) hook to provide intelligent suggestions based on the application context.

In addition, it provides a hovering editor window (available by default via `Cmd + K` on Mac and `Ctrl + K` on Windows) that allows the user to
suggest changes to the text, for example providing a summary or rephrasing the text.

This guide assumes you have completed the [quickstart](https://docs.copilotkit.ai/quickstart) and have successfully set up CopilotKit.

### [Install `@copilotkit/react-textarea`](https://docs.copilotkit.ai/guides/copilot-textarea\#install-copilotkitreact-textarea)

npmpnpmyarnbun

```
npm install @copilotkit/react-textarea
```

### [Import Styles](https://docs.copilotkit.ai/guides/copilot-textarea\#import-styles)

Import the default styles in your root component (typically `layout.tsx`) :

layout.tsx

```
import "@copilotkit/react-textarea/styles.css";
```

### [Add `CopilotTextarea` to Your Component](https://docs.copilotkit.ai/guides/copilot-textarea\#add-copilottextarea-to-your-component)

Below you can find several examples showing how to use the `CopilotTextarea` component in your application.

Example 1Example 2

TextAreaComponent.tsx

```
import { FC, useState } from "react";
import { CopilotTextarea } from '@copilotkit/react-textarea';

const ExampleComponent: FC = () => {
  const [text, setText] = useState<string>('');

  return (
    <CopilotTextarea
      className="w-full p-4 border border-gray-300 rounded-md"
      value={text}
      onValueChange={setText}

      autosuggestionsConfig={{
        textareaPurpose: "the body of an email message",
        chatApiConfigs: {},
      }}
    />
  );
};
```

## [Next Steps](https://docs.copilotkit.ai/guides/copilot-textarea\#next-steps)

- We highly recommend that you check out our simple [Copilot Textarea Tutorial](https://docs.copilotkit.ai/tutorials/ai-powered-textarea/overview).
- Check out the full [CopilotTextarea reference](https://docs.copilotkit.ai/reference/components/CopilotTextarea)

[Previous\\
\\
Bring Your Own LLM](https://docs.copilotkit.ai/guides/bring-your-own-llm) [Next\\
\\
Self Hosting (Copilot Runtime)](https://docs.copilotkit.ai/guides/self-hosting)

### On this page

[Install @copilotkit/react-textarea](https://docs.copilotkit.ai/guides/copilot-textarea#install-copilotkitreact-textarea) [Import Styles](https://docs.copilotkit.ai/guides/copilot-textarea#import-styles) [Add CopilotTextarea to Your Component](https://docs.copilotkit.ai/guides/copilot-textarea#add-copilottextarea-to-your-component) [Next Steps](https://docs.copilotkit.ai/guides/copilot-textarea#next-steps)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/guides/copilot-textarea.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CrewAI Support
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

![CopilotKit Logo](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/copilotkit-logo.svg)