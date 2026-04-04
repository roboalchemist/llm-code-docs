# Stream.io Documentation
# Source: https://getstream.io/chat/docs/sdk/ios/

* [Chat Messaging](/chat/)

/

  * [Docs](/chat/docs/)

/

  * [iOS](/chat/docs/sdk/ios/)

# Overview

Building on top of the Stream Chat API, the Stream Chat iOS components include
everything you need to build feature-rich and high-functioning chat user
experiences out of the box.

We have component libraries available for both UIKit and SwiftUI. Each library
includes an extensive set of fast performing and customizable UI components
which allow you to get started quickly with little to no plumbing required.
The libraries support:

  * Rich media messages
  * Reactions
  * Threads and quoted replies
  * Text input commands (ex: Giphy and @mentions)
  * Image and file uploads and downloads
  * Video playback
  * Read state and typing indicators
  * Channel and message lists
  * Push (APN or Firebase)
  * Offline storage
  * Voice messages
  * macOS
  * and a lot more.

Before getting started with our docs, we recommend going through our tutorials
for the [UIKit](https://getstream.io/tutorials/ios-uikit-chat/) and
[SwiftUI](https://getstream.io/tutorials/ios-chat/) SDKs.

## Architecture

StreamChat Swift SDK consists of three separate frameworks:

  * [`StreamChatUI`](/chat/docs/sdk/ios/uikit/getting-started/) provides a set of reusable and customizable UI components to add chat to your UIKit application.
  * [`StreamChatSwiftUI`](/chat/docs/sdk/ios/swiftui/getting-started/) provides a set of reusable and customizable UI components to add chat to your SwiftUI application.
  * [`StreamChat`](/chat/docs/ios-swift/) is the low-level client that provides the main chat functionality, including offline storage and optimistic updates. You can use it directly in case you want to build your own UI layer for the chat.

We suggest using either [`StreamChatUI`](/chat/docs/sdk/ios/uikit/getting-
started/) or [`StreamChatSwiftUI`](/chat/docs/sdk/ios/swiftui/getting-
started/) to most of our customers. Unless your UI is completely different
from the common industry standard, you should be able to customize the built-
in components to match your needs.

The UI SDKs provide both ready-made components that you can directly integrate
(and customize) in your apps, or you can build your own, by reacting to the
state we expose and re-using our components as building blocks, if needed.

You can learn more about how the state is exposed on [this
page](/chat/docs/sdk/ios/client/) and in the [low-level client
docs](/chat/docs/ios-swift/).

You can use this library to develop OSX application by using the `StreamChat`
framework

### Dependencies

The SDK tries to keep the list of external dependencies to a minimum, these
are the dependencies currently used:

#### StreamChatUI

  * [Nuke](https://github.com/kean/Nuke) for loading images
  * [SwiftyGif](https://github.com/alexiscreuzot/SwiftyGif) for high performance gif rendering
  * [StreamChat](/chat/docs/sdk/ios/\(https:/getstream.io/chat/docs/ios-swift/\)) the low-level client for the Stream Chat API

#### StreamChatSwiftUI

  * [Nuke](https://github.com/kean/Nuke) for loading images
  * [NukeUI](https://github.com/kean/Nuke) for loading images
  * [SwiftyGif](https://github.com/alexiscreuzot/SwiftyGif) for high performance gif rendering
  * [StreamChat](/chat/docs/sdk/ios/\(https:/getstream.io/chat/docs/ios-swift/\)) the low-level client for the Stream Chat API

Starting **4.6.0** , and in order to improve the developer experience,
dependencies are hidden inside our libraries.

## Choosing the right SDK

When integrating with our chat platform, you get to choose which SDK you would
like to integrate with.

Our best options are either the UIKit or SwiftUI SDKs. We suggest you choose
what is closest to your current App.

Note that integrating our SwiftUI SDK into a UIKit based app is fully
supported. It could provide you and your development team an amazing
opportunity to get started with SwiftUI in your codebase.

Both UI SDKs expose a channel list and a channel component.

The channel list component consists of a channel list header, channel list and
other helper views (such as search, swipe actions, and more). You can learn
more about the channel list in
[UIKit](/chat/docs/sdk/ios/uikit/components/channel-list/) and
[SwiftUI](/chat/docs/sdk/ios/swiftui/channel-list-components/helper-views/) in
our docs.

The channel component consists of a channel header, message list, message
composer and other helper views (such as reactions overlay, different media
pickers, threads etc). More details about these components can be found in our
[UIKit](/chat/docs/sdk/ios/uikit/components/channel/) and
[SwiftUI](/chat/docs/sdk/ios/swiftui/chat-channel-components/overview/) docs.

## Upgrade and Versioning Strategy

The StreamChat Swift SDK adheres to the [semantic
versioning](https://semver.org/) rules.

  * Bug fixes and behavior improvements cause **patch** version bump.
  * New features are shipped with an increased **minor** version.
  * Incompatible changes in the API will cause a **major** version increase.

Occasionally, the SDK can include visual changes (whitespace, color changes,
sizing, etc) in minor versions, as we are continuously improving the default
look of our UI components. Bumping the major version for such changes would
not be practical.

### How Should I Specify My Dependency Version?

You should either use a fixed version, or an optimistic operator (a.k.a.
squiggly arrow), with **all three versions specified**.

For example with CocoaPods:

    
    
    pod 'StreamChat', '~> 4.62.0'

To stay up-to-date with our updates and get a detailed breakdown of whatâs
new, subscribe to the releases of [getstream/stream-chat-
swift](https://github.com/GetStream/stream-chat-swift/releases) by clicking
the âwatchâ button. You can further tweak your watch preferences and
subscribe only to the release events.

Did you find this page helpful?

It was helpful

It was not helpful

I have feedback

Submit

Thank you for the feedback.

An error has occurred. Please refresh the page and try again.

[NextInstallation](/chat/docs/sdk/ios/basics/integration/)

Â© Stream.io, Inc. All Rights Reserved.

[Chat Messaging](https://getstream.io/chat/)[Video &
Audio](https://getstream.io/video/)[Activity
Feeds](https://getstream.io/activity-
feeds/)[Moderation](https://getstream.io/moderation/)

  * Copy LLM prompt
  * [ View as markdown](https://getstream.io/chat/docs/sdk/ios.md)
  *   * [ Open in ChatGPT](https://chatgpt.com/?q=I'm working with the Stream Chat IOS SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/ios.md)
  * [ Open in Claude](https://claude.ai/new?q=I'm working with the Stream Chat IOS SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/ios.md)
  * [ Open in Gemini](https://gemini.google.com/app?query=I'm working with the Stream Chat IOS SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/ios.md)
  * [ Open in Grok](https://x.com/i/grok?text=I'm working with the Stream Chat IOS SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/ios.md)
  * [ Open in Perplexity](https://www.perplexity.ai/search/new?q=I'm working with the Stream Chat IOS SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/sdk/ios.md)

On this page:

  * Architecture

    * Dependencies

  * Choosing the right SDK
  * Upgrade and Versioning Strategy

    * How Should I Specify My Dependency Version?

Is this helpful?

Thank you .

An error has occurred.