# Source: https://docs.asapp.com/messaging-platform/integrations/ios-sdk/deep-links-and-web-links.md

# Deep Links and Web Links

## Handle Deep Links in Chat

Certain chat flows may present buttons that are deep links to another part of your app. To react to taps on these buttons, implement the `ASAPPDelegate` protocol, including the `chatViewControlledDidTapDeepLink(name:data:)` method. Please ask your Implementation Manager if you have questions regarding deep link names and data.

## Handle Web Links in Chat

Certain chat flows may present buttons that are web links. To react to taps on these buttons, implement the `ASAPPDelegate` protocol, including the `chatViewControllerShouldHandleWebLink(url:)` method. Return true if the ASAPP SDK should open the link in an `SFSafariViewController`; return `false` if you'd like to handle it instead.

## Implement Deep Links into Chat

### Getting Started

Please see Apple's documentation on [Allowing Apps and Websites to Link to Your Content](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content).

### Connect the Pieces

Once you have set up a custom URL scheme for your app, you can detect links pointing to ASAPP chat within `application(_:open:options:)`. Call one of the four provided methods to create an ASAPP chat view controller:

```json  theme={null}
ASAPP.createChatViewControllerForPushing(fromNotificationWith:)
ASAPP.createChatViewControllerForPresenting(fromNotificationWith:)
ASAPP.createChatViewControllerForPushing(withIntent:)
ASAPP.createChatViewControllerForPresenting(withIntent:)
```
