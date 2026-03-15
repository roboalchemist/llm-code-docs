# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-session-replay/video-like-replay.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-session-replay/video-like-replay.md

# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/session-replay/video-like-replay.md

# Video-Like Replay

### Overview <a href="#overview" id="overview"></a>

Video-like Session Replay transforms your session recordings from simple screen-by-screen captures into smooth, video-like playback. This feature gives you complete visibility into user behavior by:

* **Capturing more frequent screenshots** -> See every interaction, not just screen transitions
* **Providing configurable quality profiles** -> Balance visual fidelity with storage efficiency
* **Supporting multiple capture modes** -> Choose the right approach for your debugging needs

{% hint style="info" %}
***Minimum SDK Version:** iOS SDK 19.2.0+*
{% endhint %}

### Capturing Modes <a href="#capturing-modes" id="capturing-modes"></a>

Control **when** screenshots are captured using the ***Capturing Mode*** API.

#### **1 - Navigation Mode (Default)**

Captures screenshots only when users navigate between screens. This is the default behavior, providing the lowest overhead.

**Best for:** Apps where screen transitions are the primary user flow

***

#### **2 - Interactions Mode**

Captures screenshots on screen navigation **and** user interactions. Includes debouncing to prevent excessive captures.

**Best for:** Debugging user interaction issues, understanding how users interact with complex screens

**Supported Interactions**

| **UIKit**   | **SwiftUI** |
| ----------- | ----------- |
| Tap         | Tap         |
| Double Tap  | Double Tap  |
| Long Press  | Long Press  |
| Force Touch | Force Touch |
| Swipe       | Swipe       |
| Pinch       | Pinch       |
| Scroll      | Scroll\*    |

***

#### **3 - Frequency Mode**

Captures screenshots at a fixed time interval for true video-like playback. Also captures on screen navigation.

**Best for:** Full video-like replay experience, debugging visual issues, understanding complete user journeys

***

### Screenshot Quality <a href="#screenshot-quality" id="screenshot-quality"></a>

Control the **visual quality** of captured screenshots. Higher quality provides better visuals but uses more storage.

#### **Quality Profiles**

| **Profile**          | **Compression**                | **Use Case**                                  |
| -------------------- | ------------------------------ | --------------------------------------------- |
| **High**             | 50% quality (WebP)             | Detailed debugging, visual regression testing |
| **Normal** (Default) | 25% quality (WebP)             | Balanced quality and storage                  |
| **Greyscale**        | 25% quality + grayscale (WebP) | Maximum storage efficiency, text-heavy apps   |

#### **Estimated Screenshots per Session**

Based on the default 1MB session screenshot limit:

| **Quality Profile** | **Approx. Screenshots per Session** |
| ------------------- | ----------------------------------- |
| High                | \~62 screenshots                    |
| Normal              | \~104 screenshots                   |
| Greyscale           | \~130 screenshots                   |

> ***Tip:** For video-like replay at 1 FPS with Normal quality, you can capture approximately 1-2 minutes of continuous session activity.*

***

### SwiftUI Considerations <a href="#swiftui-considerations" id="swiftui-considerations"></a>

For SwiftUI apps, most interactions are captured automatically. However, **scroll detection in SwiftUI requires manual gesture handling** if you want scroll events to trigger captures in Interactions mode.UIKit views embedded in SwiftUI work as expected with full interaction detection.

*→ Please refer to our SwiftUI integration docs for more details* [SwiftUI Integration for iOS](https://docs.luciq.ai/docs/ios-swiftui-integration)*.*

***

### Privacy & Masking <a href="#privacy-and-masking" id="privacy-and-masking"></a>

Video-like Session Replay **respects all existing privacy** configurations:

* **Auto-masking** continues to work across all capturing modes
* **Private views** are masked in all captured screenshots

***

### Migration Guide <a href="#migration-guide" id="migration-guide"></a>

If you’re upgrading from a previous SDK version:

1. **No breaking changes** -> Default behavior remains Navigation mode with Normal quality
2. **Opt-in feature** -> Video-like replay must be explicitly configured
3. **Repro Steps unaffected** -> Bug and Crash report screenshots continue to use Navigation mode and Normal quality
