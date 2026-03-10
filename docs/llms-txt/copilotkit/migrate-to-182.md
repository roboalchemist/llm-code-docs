# Migrate to 1.8.2

Migration guide for CopilotKit 1.8.2

## [What's changed?](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2\#whats-changed)

### [New Look and Feel](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2\#new-look-and-feel)

CopilotKit 1.8.2 introduces a new default look and feel. This includes new use of theming variables, new components, and generally a fresh look.

**Click the button in the bottom right to see the new look and feel in action!**

### [Thumbs Up/Down Handlers](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2\#thumbs-updown-handlers)

The chat components now have `onThumbsUp` and `onThumbsDown` handlers. Specifying these will add icons to each message
on hover allowing the user to provide feedback.

```
<CopilotChat
  onThumbsUp={(message) => console.log(message)}
  onThumbsDown={(message) => console.log(message)}
/>
```

This was previously achievable in our framework, but we're making it first class now! You can use this to help fine-tune your model through CopilotKit
or just generally track user feedback.

### [ResponseButton prop removed](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2\#responsebutton-prop-removed)

The `ResponseButton` prop has been removed. This was a prop that was used to customize the button that appears after a response was generated
in the chat.

In its place, we now place buttons below each message for:

- Thumbs up
- Thumbs down
- Copy
- Regenerate

The behvior, icons and styling for each of these buttons can be customized. Checkout our [look and feel guides](https://docs.copilotkit.ai/guides/custom-look-and-feel) for more details.

### [Out-of-the-box dark mode support](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2\#out-of-the-box-dark-mode-support)

CopilotKit now has out-of-the-box dark mode support. This is controlled by the `.dark` class (Tailwind) as well as the
`color-scheme` CSS selector.

If you would like to make a custom theme, you can do so by checking out the [custom look and feel](https://docs.copilotkit.ai/guides/custom-look-and-feel) guides.

CopilotKit

Hey there Let's have a fun conversation!

[Previous\\
\\
Common Issues](https://docs.copilotkit.ai/troubleshooting/common-issues) [Next\\
\\
Code Contributions](https://docs.copilotkit.ai/contributing/code-contributions)

### On this page

[What's changed?](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2#whats-changed) [New Look and Feel](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2#new-look-and-feel) [Thumbs Up/Down Handlers](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2#thumbs-updown-handlers) [ResponseButton prop removed](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2#responsebutton-prop-removed) [Out-of-the-box dark mode support](https://docs.copilotkit.ai/troubleshooting/migrate-to-1.8.2#out-of-the-box-dark-mode-support)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/troubleshooting/migrate-to-1.8.2.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Generative UI Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageRender custom components in the chat UI