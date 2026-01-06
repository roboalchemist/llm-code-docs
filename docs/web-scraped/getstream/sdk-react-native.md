# Stream.io Documentation
# Source: https://getstream.io/chat/docs/sdk/react-native/

* [Chat Messaging](/chat/)

/

  * [Docs](/chat/docs/)

/

  * [React Native](/chat/docs/sdk/react-native/)

# Overview

Built on top of the Stream Chat API, the Stream Chat React Native SDK
components include everything you need to build feature-rich and high-
functioning chat user experiences out of the box.

We have component libraries available for both RN CLI and Expo. Each approach
includes an extensive set of fast performing and customizable UI components
and support which allow you to get started quickly with little to no plumbing
required. The libraries support:

  * Rich media messages
  * Reactions
  * Threads and quoted replies
  * Text input commands (ex: Giphy, emojis and @mentions)
  * Image and file uploads
  * Video playback
  * Read state and typing indicators.
  * Channel and message lists
  * Push (APN or Firebase)
  * Offline storage
  * and a lot more.

Additionally, starting with version `6.0.0` our SDK supports the [React Native
new architecture](https://reactnative.dev/architecture/landing-page) as well.
You can read more about it [here](/chat/docs/sdk/react-native/guides/new-
architecture).

Before getting started with our docs, we recommend going through our tutorials
for our [**React Native SDK**](https://getstream.io/chat/react-native-
chat/tutorial/).

## Where to get started?

If you are new to our SDK, it is best to go through our [**React Native
SDK**](https://getstream.io/chat/react-native-chat/tutorial/) tutorial.

## Architecture

Stream Chat React Native SDK primarily uses theÂ [Stream Chat
client](https://github.com/GetStream/stream-chat-js)Â to connect to and
communicate with the Stream API.

The fullÂ [JavaScript client docs](/chat/docs/javascript/)Â should be
referenced for detailed information on directly using the client.

Do not install the `stream-chat` dependency externally. This may lead to
problems while using our SDK. Our SDK has it as a development dependency, so
you need not install it externally.

The Stream Chat React Native SDK is segregated into two separate packages:

  * `stream-chat-react-native` for **React Native CLI** applications.
  * `stream-chat-expo` for **Expo CLI** applications.

We recommend using the corresponding package for the respective CLI that the
application uses.

Our SDK components are highly customizable for both the interfaces. Unless
your UI is completely different from the common industry standard, you should
be able to customize the built-in components to match your needs.

The UI SDKs provide both ready-made components that you can directly integrate
(and customize) in your apps, or you can build your own, by reacting to the
state we expose and re-using our components as building blocks, if needed.

## Upgrading and Versioning Strategy

The Stream Chat React Native SDK adheres to theÂ [semantic
versioning](https://semver.org/)Â rules.

  * Bug fixes and behavior improvements causeÂ **patch** Â version bump.
  * New features are shipped with an increasedÂ **minor** Â version.
  * Incompatible changes in the API will cause aÂ **major** Â version increase.

Occasionally, the SDK can include visual changes (whitespace, color changes,
sizing, etc) in minor versions, as we are continuously improving the default
look of our UI components. Bumping the major version for such changes would
not be practical.

## Platform Compatibilities

We only supportÂ **Android** Â andÂ **iOS** Â as platforms for the React
Native SDK. We do not supportÂ **Web** Â currently, but this is in our
backlog, and we plan to take this up in the future. As an alternative, you can
use StreamâsÂ [React SDK](/chat/docs/sdk/react/)Â for Web.

## Sample Apps

We have created some of the sample apps to help understand the usage of the
Stream Chat React Native SDK. They can be found in the
[`examples`](https://github.com/GetStream/stream-chat-react-
native/tree/develop/examples) directory of the main repository. Apart from the
samples we use for internal development, we also provide some small clone
projects like a Slack clone and an iMessage clone. You can check out the code
inÂ [our repository](https://github.com/GetStream/react-native-samples)Â and
even run the apps yourself.

Did you find this page helpful?

It was helpful

It was not helpful

I have feedback

Submit

Thank you for the feedback.

An error has occurred. Please refresh the page and try again.

[PreviousMigration from 6.x to 7.x](/chat/docs/sdk/react-
native/v7/basics/upgrading-from-v6/)[NextInstallation](/chat/docs/sdk/react-
native/basics/installation/)

Â© Stream.io, Inc. All Rights Reserved.

[Chat Messaging](https://getstream.io/chat/)[Video &
Audio](https://getstream.io/video/)[Activity
Feeds](https://getstream.io/activity-
feeds/)[Moderation](https://getstream.io/moderation/)

  * Copy LLM prompt
  * [ View as markdown](https://getstream.io/chat/docs/sdk/react-native.md)
  *   * [ Open in ChatGPT](https://chatgpt.com/?q=I'm working with the Stream Chat React Native SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react-native.md)
  * [ Open in Claude](https://claude.ai/new?q=I'm working with the Stream Chat React Native SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react-native.md)
  * [ Open in Gemini](https://gemini.google.com/app?query=I'm working with the Stream Chat React Native SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react-native.md)
  * [ Open in Grok](https://x.com/i/grok?text=I'm working with the Stream Chat React Native SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react-native.md)
  * [ Open in Perplexity](https://www.perplexity.ai/search/new?q=I'm working with the Stream Chat React Native SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/react-native.md)

On this page:

  * Where to get started?
  * Architecture
  * Upgrading and Versioning Strategy
  * Platform Compatibilities
  * Sample Apps

Is this helpful?

Thank you .

An error has occurred.