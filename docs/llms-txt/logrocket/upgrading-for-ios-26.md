# Source: https://docs.logrocket.com/reference/upgrading-for-ios-26.md

# Upgrading for iOS 26

Guidance for using the LogRocket SDK when updating your app for iOS 26

iOS 26 introduces changes to SwiftUI that can cause certain elements to not be redacted by the LogRocket SDK **when your app is submitted using Xcode 26**. You must use at least LogRocket SDK [1.57.0](https://docs.logrocket.com/docs/mobile-sdk-changelog#/1570-2025-09-11)to avoid these issues, but we recommend upgrading to the latest available version LogRocket in order to have the most accurate view capture.

For developers using the `textSanitizer: excluded` configuration, it is advised to upgrade to version [1.61.1](https://docs.logrocket.com/docs/mobile-sdk-changelog#1611-2026-02-05) of the LogRocket SDK, and consult the [iOS text sanitization documentation](./ios-automatically-sanitize-text) for more information.

If you used Xcode 26 to submit your app, please contact [support@logrocket.com](mailto:support@logrocket.com) or your customer success manager, and we will block iOS 26 sessions until the LogRocket SDK is updated.

<br />