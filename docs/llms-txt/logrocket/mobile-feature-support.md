# Source: https://docs.logrocket.com/docs/mobile-feature-support.md

# Mobile Feature Support

> 👍 LogRocket Mobile SDK Documentation
>
> Looking for documentation on the LogRocket mobile SDKs? [View the Android SDK here](https://docs.logrocket.com/v3.0/reference/android) and [view the iOS SDK here](https://docs.logrocket.com/v3.0/reference/ios).

> 📘 React Native Feature Support
>
> React Native features are platform-specific and are not listed separately. If a feature is marked as supported on Android it is supported for React Native on Android devices.

## Session Playback

See [Performance Monitoring Documentation](https://docs.logrocket.com/docs/performance-monitoring) for more information.

|                               | Web | Android              | iOS |
| :---------------------------- | :-- | :------------------- | :-- |
| "Video" Replay                | ✅   | ✅                    | ✅   |
| Network Logs                  | ✅   | ✅                    | ✅   |
| Console Logs/Application Logs | ✅   | ✅                    | ✅   |
| Redux Logs                    | ✅   | ✅                    | ✅   |
| Performance Data              | ✅   | ✅                    | ✅   |
| Custom Fonts\*                | ✅   | :white\_check\_mark: | ✅   |
| Webview Capture†‡             | N/A | ✅                    | ✅   |

<div><sup>\* Text will always be captured for non-standard fonts, though in unsupported cases fonts can appear misaligned or cut off in session replay. Upload your custom font ([iOS](https://docs.logrocket.com/reference/ios-capture-custom-fonts), [Android](https://docs.logrocket.com/reference/android-capture-custom-fonts)) to see them in Session Replay.</sup><br /><sup>† Web SDK must be installed in webviews. See SDK documentation ([iOS](https://docs.logrocket.com/reference/webviews-on-ios), [Android](https://docs.logrocket.com/reference/webviews-on-android), [React Native](https://docs.logrocket.com/reference/webviews-on-react-native)) for implementation details.</sup><br /><sup>‡ For mobile apps using the [Flutter SDK](https://docs.logrocket.com/reference/configure-flutter-sdk/), webviews will be recorded as distinct sessions</sup></div>

## Filters

|                       | Web       | Android       | iOS                 |
| :-------------------- | :-------- | :------------ | :------------------ |
| User Identification   | ✅         | ✅             | ✅                   |
| Clicked               | ✅         | ✅             | ✅                   |
| Network Logs          | ✅         | ✅             | ✅                   |
| Console Logs          | ✅         | ✅             | ✅                   |
| Duration              | ✅         | ✅             | ✅                   |
| Device                | ✅         | ✅             | ✅                   |
| Browser               | ✅         | N/A           | N/A                 |
| Event Count           | ✅         | ✅             | ✅                   |
| Release               | ✅         | ✅             | ✅                   |
| Operating System      | ✅         | ✅             | ✅                   |
| Viewport Size         | ✅         | N/A           | N/A                 |
| Visited URL           | ✅         | ✅ (Activity)  | ✅ (View Controller) |
| Custom Event          | ✅         | ✅             | ✅                   |
| Element Visible\* †   | ✅         | ✅             | ✅                   |
| Element Not Visible\* | ✅         | ✅             | ✅                   |
| Redux Actions         | ✅         | ✅             | ✅                   |
| Text Input            | ✅         | ✅             | ✅                   |
| Scroll Depth          | ✅         | Not supported | Not supported       |
| Time Between Events   | ✅         | ✅             | ✅                   |
| Crashes               | ✅         | ✅             | ✅                   |
| CPU Load              | ✅         | ✅             | ✅                   |
| Memory Usage          | ✅         | ✅             | ✅                   |
| Mobile App Start Time | N/A       | ✅             | ✅                   |
| Network Throughput    | ✅ (Speed) | ✅             | ✅                   |

<div><sup>\* Not currently supported for Flutter applications</sup><br /><sup>† "With text" operator not supported for SwiftUI or [React Native New Architecture](https://reactnative.dev/architecture/landing-page)</sup></div>

## Issue Management

|                              | Web | Android       | iOS           |
| :--------------------------- | :-- | :------------ | :------------ |
| Exceptions                   | ✅   | ✅             | ✅             |
| Network Errors               | ✅   | ✅             | ✅             |
| Rage Clicks                  | ✅   | ✅             | ✅             |
| Dead Clicks                  | ✅   | Not supported | Not supported |
| Frustrating Network Requests | ✅   | Not supported | Not supported |
| Error States                 | ✅   | ✅             | ✅             |

## Metrics

|               | Web | Android | iOS |
| :------------ | :-- | :------ | :-- |
| Timeseries    | ✅   | ✅       | ✅   |
| Funnels       | ✅   | ✅       | ✅   |
| Heatmaps\*    | ✅   | ✅       | ✅   |
| Tables        | ✅   | ✅       | ✅   |
| Path Analysis | ✅   | ✅       | ✅   |

<div><sup>\* Not currently supported for Flutter applications</sup></div>

## General Features

|                       | Web | Android       | iOS           |
| :-------------------- | :-- | :------------ | :------------ |
| Surveys               | ✅   | Not supported | Not supported |
| Galileo AI Issues     | ✅   | ✅             | ✅             |
| Galileo AI Highlights | ✅   | ✅             | ✅             |

## Privacy

|                                            | Web | Android | iOS |
| :----------------------------------------- | :-- | :------ | :-- |
| Exclude data from any element              | ✅   | ✅       | ✅   |
| Redact recording of any form input         | ✅   | ✅       | ✅   |
| Redact any DOM element                     | ✅   | ✅       | ✅   |
| Automatically sanitize all text and inputs | ✅   | ✅       | ✅   |
| Exclude network data                       | ✅   | ✅       | ✅   |
| Exclude Redux state                        | ✅   | ✅       | ✅   |
| Exclude Redux actions                      | ✅   | ✅       | ✅   |

## Conditional Recording\*

|                    | Web | Android      | iOS                 |
| :----------------- | :-- | :----------- | :------------------ |
| Activity Lookback† | ✅   | ✅            | ✅                   |
| Session Duration   | ✅   | ✅            | ✅                   |
| Visited URL        | ✅   | ✅ (Activity) | ✅ (View Controller) |
| Clicked            | ✅   | ✅            | ✅                   |
| Custom Event       | ✅   | ✅            | ✅                   |
| Network Request    | ✅   | ✅            | ✅                   |
| Log Message        | ✅   | ✅            | ✅                   |
| Element Visible    | ✅   | ✅            | ✅                   |

<div><sup>\* Conditional Recording is not currently supported for [Shopify App](https://docs.logrocket.com/docs/shopify-capture-app/) sessions</sup><br /><sup>† Activity Lookback captures up to 10MB of activity prior to the trigger that persists the session</sup></div>