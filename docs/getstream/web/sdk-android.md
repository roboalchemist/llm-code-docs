# Stream.io Documentation
# Source: https://getstream.io/chat/docs/sdk/android/

* [Chat Messaging](/chat/)

/

  * [Docs](/chat/docs/)

/

  * [Android](/chat/docs/sdk/android/)

# Overview

The [Stream Chat Android SDK](https://github.com/GetStream/stream-chat-
android) enables you to easily build any type of chat or messaging experience
for Android, either in Kotlin or Java.

The fastest way to get started with the SDK is by trying the [Android Views
In-App Messaging Tutorial](https://getstream.io/tutorials/android-chat/). If
youâre using Jetpack Compose, see the [Compose In-App Messaging
Tutorial](https://getstream.io/chat/compose/tutorial/) instead.

## Architecture

The SDK consists of five major components:

  * [Views/XML UI components](/chat/docs/sdk/android/ui/overview/). Provides a set of reusable and customizable UI components based on Android Views.
  * [Compose UI components](/chat/docs/sdk/android/compose/overview/). Provides a set of reusable and customizable Jetpack Compose UI components.
  * [Low-level client](/chat/docs/android/). Provides the main chat functionality. You can use it directly if you intend to build your own UI layer for the chat.
  * [State](/chat/docs/sdk/android/client/guides/state-plugin/). Plugin that gives you the possibility to observe data via `StateFlows`. It exposes `StateFlow` objects containing the loading state, channel and message lists, channel members, users that are typing and more.
  * [Offline Support](/chat/docs/sdk/android/client/guides/offline-support/). Plugin that enables offline data and actions, like cached channels, messages, sending messages and reactions. Good for improving UX when the network connection is poor.

We recommend using either the [Views/XML UI
Components](/chat/docs/sdk/android/ui/overview/) or the [Compose UI
Components](/chat/docs/sdk/android/compose/overview/) to most of our
customers. If your UI doesnât significantly differ from the industry
standard, you should be able to customize the built-in components to match
your requirements.

For more information about including each component in your project, see the
[Installation](/chat/docs/sdk/android/basics/dependencies/) page.

## UI SDKs

Built on top of the Stream Chat low-level client, the Stream Chat Android UI
components enable you to easily build any type of chat or messaging experience
for Android.

We have UI component libraries available for both **Android Views** and
**Jetpack Compose**. Each of these libraries provides an extensive collection
of efficient and customizable UI components which enable you to quickly get
started with little to no setup required. The libraries support:

  * Rich-media messages
  * Channel and message lists
  * Message Reactions
  * Message threads and quoted replies
  * Text input commands (ex: Giphy and @mentions)
  * Image and file uploads
  * Video playback
  * Indicators for read state and typing
  * Push notifications
  * Offline storage
  * Voice messages (only in the Android Views library for now)
  * and more.

If needed, you can create your own UI components by listening to the state we
expose and using our components as building blocks. You can learn more about
how state is exposed [here](/chat/docs/sdk/android/client/guides/state-
plugin/) and in the [low-level client docs](/chat/docs/android/).

### Choosing the Right UI SDK

#### Views UI Components

The UI Components library includes pre-built Android Views to easily load and
display data from the Stream Chat API. These include a Channel List and a
Message List, a Message Composer View, and more. See the [Getting
Started](/chat/docs/sdk/android/ui/overview/) page for more details.

This library is built on top of the state library, and offers the quickest
integration of Stream Chat into an Android application. It also offers a
variety of [theming](/chat/docs/sdk/android/ui/general-customization/theming/)
options to make it fit your appâs needs.

You can see the UI Components in action by checking out the [UI Components
Sample App](https://github.com/GetStream/stream-chat-android/tree/main/stream-
chat-android-ui-components-sample), available in the GitHub repository.

#### Compose UI Components

The Compose UI Components library is a chat UI implementation built from
scratch with [Jetpack Compose](https://developer.android.com/jetpack/compose).
It contains modular Composable functions for building channel lists, messaging
screens, and more. See the [Getting
Started](/chat/docs/sdk/android/compose/overview/) page for more details.

This is also built on top of the state library, and offers easy integration of
Stream Chat into a Compose-based Android application. Itâs also highly
modular and customizable.

Check out the Compose implementation in action by trying the open-source
[Compose UI Components Sample App](https://github.com/GetStream/stream-chat-
android/tree/main/stream-chat-android-compose-sample).

Using our Compose SDK in an Android Views based app is fully supported. It
could provide you an amazing opportunity to explore and adopt Compose.

#### The Right SDK for You

If your use case requires a very high level of customization, runtime theming
changes, replacing whole parts of the default UI or stateless components that
donât rely on our ViewModels, the **Compose SDK is the way to go**. It
offers deep customization through several layers - the theme, modifiers for
components, bound and stateless component overloads, smaller reusable
components and slot APIs.

If, instead, youâre looking for a simpler, less customizable SDK which
currently offers slightly better performance in some scenarios or your project
is limited by technology, then the **UI Components SDK is a great option**. It
still offers a fair amount of customization through the theme and its
attributes and some programmatic ways to customize the UI.

Whichever SDK you choose, **we guarantee youâll be happy and weâll provide
amazing support** with your integration, through detailed documentation,
guides and direct support.

## Upgrade and Versioning Strategy

The StreamChat Android SDK adheres to the [semantic
versioning](https://semver.org/) rules.

  * Bug fixes and behavior improvements cause **patch** version bump.
  * New features are shipped with an increased **minor** version.
  * Incompatible changes in the API will cause a **major** version increase.

Occasionally, the SDK can include visual changes (whitespace, color changes,
sizing, etc) in minor versions, as we are continuously improving the default
look of our UI components. Bumping the major version for such changes would
not be practical.

You can see all the SDK changes in the [releases
page](https://github.com/GetStream/stream-chat-android/releases), and you can
also find the release notes of all past releases in our [CHANGELOG
file](https://github.com/GetStream/stream-chat-
android/blob/main/CHANGELOG.md).

You can get notified of new releases by using the _Watch_ button in the
[getstream/stream-chat-android](https://github.com/GetStream/stream-chat-
android) repository. You can tweak your watch preferences to subscribe only to
release events.

### How Should I Specify My Dependency Version?

You should use a fixed version in order to avoid any conflicts or unpredicted
behaviour.

For example:

    
    
    implementation "io.getstream:stream-chat-android-compose:6.4.4"

Did you find this page helpful?

It was helpful

It was not helpful

I have feedback

Submit

Thank you for the feedback.

An error has occurred. Please refresh the page and try again.

[PreviousSample Apps](/chat/docs/sdk/android/v5/resources/sample-
apps/)[NextInstallation](/chat/docs/sdk/android/basics/dependencies/)

Â© Stream.io, Inc. All Rights Reserved.

[Chat Messaging](https://getstream.io/chat/)[Video &
Audio](https://getstream.io/video/)[Activity
Feeds](https://getstream.io/activity-
feeds/)[Moderation](https://getstream.io/moderation/)

  * Copy LLM prompt
  * [ View as markdown](https://getstream.io/chat/docs/sdk/android.md)
  *   * [ Open in ChatGPT](https://chatgpt.com/?q=I'm working with the Stream Chat Android SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/android.md)
  * [ Open in Claude](https://claude.ai/new?q=I'm working with the Stream Chat Android SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/android.md)
  * [ Open in Gemini](https://gemini.google.com/app?query=I'm working with the Stream Chat Android SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/android.md)
  * [ Open in Grok](https://x.com/i/grok?text=I'm working with the Stream Chat Android SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/android.md)
  * [ Open in Perplexity](https://www.perplexity.ai/search/new?q=I'm working with the Stream Chat Android SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/android.md)

On this page:

  * Architecture
  * UI SDKs

    * Choosing the Right UI SDK

  * Upgrade and Versioning Strategy

    * How Should I Specify My Dependency Version?

Is this helpful?

Thank you .

An error has occurred.