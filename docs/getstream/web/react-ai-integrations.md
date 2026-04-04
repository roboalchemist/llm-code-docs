# Stream.io Documentation
# Source: https://getstream.io/chat/docs/sdk/react/guides/ai-integrations/

* [Chat Messaging](/chat/)

/

  * [Docs](/chat/docs/)

/

  * [React](/chat/docs/sdk/react/)

/

  * [AI Integrations](/chat/docs/sdk/react/guides/ai-integrations/)

# AI Integrations

The AI UI components are designed specifically for AI-first applications
written in React. When paired with our real-time [Chat
API](https://getstream.io/chat/), it makes integrating with and rendering
responses from LLM providers such as ChatGPT, Gemini, Anthropic or any custom
backend easier by providing rich with out-of-the-box components able to render
markdown, syntax highlighted code blocks, tables, thinking indicators, charts
and so on.

This library includes the following components which assist with this task:

  * `StreamingMessage` \- a component that is able to render text, markdown and code in real-time, using a typewriter, character-by-character animation, similar to ChatGPT
  * `AIMessageComposer` \- a fully featured prompt composer with attachments and speech input
  * `AIStateIndicator` \- a component that is useful to keep the userâs attention while the AI generates an answer
  * `SpeechToTextButton` \- a reusable button that records voice input and streams the recognized transcript back into your UI

Our team plans to keep iterating and adding more components over time. If
thereâs a component you use every day in your apps and would like to see
added, please open an issue and we will take it into consideration.

You can find a complete ChatGPT clone sample that uses these components
[here](https://github.com/GetStream/chat-ai-samples/tree/main/react-native).

## Installation

The `@stream-io/chat-react-ai` SDK is available on NPM.

To install it and its peer dependencies, you may run the following command:

yarnpnpmnpm

    
    
    yarn add @stream-io/chat-react-ai
    
    
    pnpm add @stream-io/chat-react-ai
    
    
    npm i @stream-io/chat-react-ai

## Components

All of the components listed below are designed to work seamlessly with our
existing [React Chat SDK](https://getstream.io/chat/react-chat/tutorial/). Our
[developer guide](https://getstream.io/chat/solutions/ai-integration/)
explains how to get started building AI integrations with Stream.

### `StreamingMessage`

The `StreamingMessage` is a component that can render markdown content
efficiently. It has code syntax highlighting, supporting all the major
languages. It can render most of the standard markdown content, such as
tables, inline code, headings, lists etc.

Under the hood, it implements a letter-by-letter typewriter animation with a
character queue, similar to ChatGPT.

Name| Type| Required| Description  
`text`| `string`| yes| The text we want to pass as markdown.  
`letterIntervalMs`| `number`| no| A number signifying the interval at which
the typewriter animation is going to render characters. Defaults to `30`  
`renderingLetterCount`| `number`| no| A number signifying the number of
letters that are going to be rendered per tick of the interval during the
typewriter animation. Defaults to `2`  
  
If you need to build your own `StreamingMessage` \- itâs as simple as
importing `AIMarkdown` component and `useMessageTextStreaming` hook and
combining them together.

#### Example

Provided below is an example of how to use the component.

    
    
    const markdownText = ```
    # Heading
    
    some text
    
    ## Another heading
    ```;
    
    <StreamingMessage
      text={markdownText}
      letterIntervalMs={30} // every 30ms
      renderingLetterCount={3} // render 3 letters at a time
    />;

### `AIStateIndicator`

The `AIStateIndicator` is used to represent different states of the LLM, such
as `Thinking`, `Checking External Sources` and so on, depending on the states
youâve defined on your backend. You can provide your own text or pass none
to let the component pick one of the pre-defined phrases. To change the phrase
pass any new value to a `key` prop which resets componentâs internal state.

Name| Type| Required| Description  
`text`| `string`| no| The text we want to be displayed inside of the
component.  
  
#### Example

    
    
    {
      (aiState === "thinking" || aiState === "generating") && (
        <AIStateIndicator key={resetKey} />
      );
    }
    
    // or
    
    {
      (aiState === "thinking" || aiState === "generating") && (
        <AIStateIndicator text="Thinking of a proper response..." />
      );
    }

### `AIMessageComposer`

The `AIMessageComposer` gives users a complete message composer component with
support for text input, file attachments, speech-to-text, and model selection.

Name| Type| Required| Description  
`resetAttachmentsOnSelect`| `boolean`| no| Resets file input after selection.
Defaults to `true`.  
`nameMapping`| `{ message?: string; attachments?: string }`| no| Maps custom
input names to internal state. By default, the composer expects inputs named
`message` (for text) and `attachments` (for files). Use this prop to map
different names to these internal keys.  
`onSubmit`| `(e: FormEvent<HTMLFormElement>) => void`| no| Form submission
handler.  
`onChange`| `(e: FormEvent<HTMLFormElement>) => void`| no| Form change
handler.  
| `...HTMLFormElement props`| no| Supports all standard HTML form element
props.  
  
#### Sub-components

  * **`AIMessageComposer.FileInput`** \- File input button for attaching files. Supports multiple file selection.
  * **`AIMessageComposer.TextInput`** \- Text input field for typing messages. Automatically syncs with composer state.
  * **`AIMessageComposer.SpeechToTextButton`** \- Button to toggle speech-to-text input using the Web Speech API.
  * **`AIMessageComposer.SubmitButton`** \- Submit button for sending the message.
  * **`AIMessageComposer.ModelSelect`** \- Dropdown for selecting AI models. Customizable via `options` prop.
  * **`AIMessageComposer.AttachmentPreview`** \- Preview container for attached files.
  * **`AIMessageComposer.AttachmentPreview.Item`** \- Preview item component, renders a different look for file types that begin with `image/`.

#### Example

    
    
    import { AIMessageComposer } from "@stream-io/chat-react-ai";
    
    function ChatComposer({ attachments }: ChatComposerProps) {
      const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        // Handle submission
      };
    
      return (
        <AIMessageComposer onSubmit={handleSubmit}>
          <AIMessageComposer.FileInput name="attachments" />
          <AIMessageComposer.TextInput name="message" />
          <AIMessageComposer.SpeechToTextButton />
          <AIMessageComposer.ModelSelect name="model" />
          <AIMessageComposer.SubmitButton />
          <AIMessageComposer.AttachmentPreview>
            {attachments.map((attachment) => (
              <AIMessageComposer.AttachmentPreview.Item {...attachment} />
            ))}
          </AIMessageComposer.AttachmentPreview>
        </AIMessageComposer>
      );
    }

> [!NOTE] Some default input components come with default `name` attributes
> (`TextInput` defaults to `"message"`, `FileInput` defaults to
> `"attachments"`). You can override these names via props, and use the
> `nameMapping` prop to tell the composer how to map your custom names to its
> internal state.

### `SpeechToTextButton`

The `SpeechToTextButton` is a button component for voice input using the Web
Speech API. It provides a simple interface for converting speech to text with
built-in microphone icon and listening state visualization.

Name| Type| Required| Description  
`options`| `UseSpeechToTextOptions`| no| Options for speech recognition (see
`useSpeechToText` hook documentation for available options like `lang`,
`continuous`, etc.).  
| `...HTMLButtonElement props`| no| Supports all standard HTML button element
props.  
  
#### Example

    
    
    import { SpeechToTextButton } from "@stream-io/chat-react-ai";
    
    function VoiceInputButton() {
      return (
        <SpeechToTextButton
          options={{
            lang: "en-US",
            continuous: false,
            interimResults: true,
          }}
        />
      );
    }

> [!NOTE] When used within an `AIMessageComposer`, the button automatically
> updates the composerâs text input. When used standalone, you can control
> the behavior through the `speechToTextOptions.onTranscript` callback.

### AI States

As per our current specification, the AI is allowed several states that are
related to its current progress in producing a response. You may find the
currently available states here: <https://github.com/GetStream/stream-chat-
react/blob/0577ffdbd2abf11b6b99a2e70caa938ea19635e9/src/components/AIStateIndicator/hooks/useAIState.ts#L7>.

Provided below is a brief explanation of what each state means:

  * `AI_STATE_THINKING` \- the AI is thinking and trying to internally craft an answer to your query
  * `AI_STATE_GENERATING` \- the actual response to your query is being generated
  * `AI_STATE_EXTERNAL_SOURCES` \- the AI is checking external resources for information
  * `AI_STATE_ERROR` \- the AI has reached an error state while trying to answer your query
  * `AI_STATE_IDLE` \- the AI is in an idle state and is not doing anything

If you are using your own implementation and have different states than these,
you can feel free to override our default components as well as their
behaviour.

Please, refer to [our React Assistant
tutorial](https://getstream.io/blog/react-assistant/) for more in-depth
guidance. It is highly encouraged to read the tutorial before integrating AI
in your application.

### Theming

Did you find this page helpful?

It was helpful

It was not helpful

I have feedback

Submit

Thank you for the feedback.

An error has occurred. Please refresh the page and try again.

[PreviousAudio Playback](/chat/docs/sdk/react/guides/audio-playback/)[NextSDK
Integration](/chat/docs/sdk/react/guides/ai-integrations/sdk-integration)

Â© Stream.io, Inc. All Rights Reserved.

[Chat Messaging](https://getstream.io/chat/)[Video &
Audio](https://getstream.io/video/)[Activity
Feeds](https://getstream.io/activity-
feeds/)[Moderation](https://getstream.io/moderation/)

  * Copy LLM prompt
  * [ View as markdown](https://getstream.io/chat/docs/sdk/react/guides/ai-integrations.md)
  *   * [ Open in ChatGPT](https://chatgpt.com/?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react/guides/ai-integrations.md)
  * [ Open in Claude](https://claude.ai/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react/guides/ai-integrations.md)
  * [ Open in Gemini](https://gemini.google.com/app?query=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react/guides/ai-integrations.md)
  * [ Open in Grok](https://x.com/i/grok?text=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react/guides/ai-integrations.md)
  * [ Open in Perplexity](https://www.perplexity.ai/search/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react/guides/ai-integrations.md)

On this page:

  * Installation
  * Components

    * StreamingMessage
    * AIStateIndicator
    * AIMessageComposer
    * SpeechToTextButton
    * AI States
    * Theming

Is this helpful?

Thank you .

An error has occurred.