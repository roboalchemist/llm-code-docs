# Source: https://developers.lottiefiles.com/dotlottie-players-mobile-llms.txt

# dotLottie Mobile Players

> dotLottie Mobile Players are a family of animation players designed to render both Lottie JSON (`.json`) and dotLottie (`.lottie`) animations on mobile platforms. Built on a high-performance, cross-platform rendering core, these players provide consistent animation playback across iOS, Android, and React Native applications.

**Core Features**
*   **Universal Format Support**: Native support for both `.lottie` and traditional Lottie `.json` files.
*   **Playback Control**: Includes play, pause, stop, speed control, looping, frame-by-frame navigation, and multiple playback modes (forward, reverse, bounce).
*   **Layout & Rendering**: Flexible layout options with fit modes (contain, cover, fill, etc.), alignment, and background color support.
*   **Multi-Animation Support**: Load and switch between multiple animations contained within a single `.lottie` file.
*   **Theming**: Runtime theme switching for dynamic color and style updates.
*   **State Machines**: Built-in support for interactive animations driven by states and events.
*   **Performance Optimization**: Optimized for mobile hardware with efficient memory management and battery-conscious rendering.

## Best Practices & Troubleshooting

**Resource Management**
*   **Native Mobile Players (iOS/Android)**: Avoid strong reference cycles. Remove listeners in appropriate lifecycle methods (e.g., `onDisappear`, `onDestroyView`).
*   **React Native**: The component automatically handles cleanup when unmounted, but ensure proper ref management for manual control.

**Performance Optimization**
*   **Frame Interpolation**: Consider disabling frame interpolation on lower-end devices to improve performance.
*   **Memory Management**: On mobile devices, be mindful of memory usage, especially with large or complex animations.
*   **Battery Optimization**: Pause animations when the app goes to background to conserve battery life.

**Troubleshooting Common Issues**
*   **Animation Not Loading**:
    1.  Verify file paths and ensure animations are properly bundled with your app.
    2.  Check that `.lottie` files are properly configured in your build system (e.g., `metro.config.js` for React Native).
    3.  Use error handlers to catch and log loading failures.
*   **Animation Not Playing**:
    1.  Ensure playback methods are called after the animation has loaded.
    2.  Check that autoplay properties are correctly set.
    3.  Verify that the animation view is properly sized and visible.

## React Native Player (`@lottiefiles/dotlottie-react-native`)

### Installation
```bash
npm install @lottiefiles/dotlottie-react-native
# then for iOS
cd ios && pod install
```
Configure `metro.config.js` to recognize `.lottie` files.

### Usage
```jsx
import React, { useRef } from 'react';
import { View, Button } from 'react-native';
import { DotLottie, type Dotlottie } from '@lottiefiles/dotlottie-react-native';

const ControlledAnimation = () => {
  const ref = useRef<Dotlottie>(null);
  return (
    <View>
      <DotLottie
        ref={ref}
        source={require('./animation.lottie')}
        style={{ width: 200, height: 200 }}
      />
      <Button title="Pause" onPress={() => ref.current?.pause()} />
    </View>
  );
};
```
**API**: `source`, `autoplay`, `loop`, `style` props. Event handlers `onLoad`, `onError`, `onPlay`, etc. Methods on ref: `play()`, `pause()`, `stop()`, `setSpeed()`.

## iOS Player (Native Swift)

### Installation
Use Swift Package Manager with the URL: [https://github.com/LottieFiles/dotlottie-ios](https://github.com/LottieFiles/dotlottie-ios)

### Usage (SwiftUI)
```swift
import SwiftUI
import DotLottie

struct AnimationView: View {
    @StateObject var animation = DotLottieAnimation(
        fileName: "animation",
        config: AnimationConfig(autoplay: true, loop: true)
    )

    var body: some View {
        VStack {
            animation.view()
                .frame(width: 300, height: 300)
            Button("Pause") { animation.pause() }
        }
    }
}
```

### Usage (UIKit)
```swift
import UIKit
import DotLottie

class AnimationViewController: UIViewController {
    var dotLottieAnimation: DotLottieAnimation?

    override func viewDidLoad() {
        super.viewDidLoad()
        let config = AnimationConfig(autoplay: true, loop: true)
        dotLottieAnimation = DotLottieAnimation(fileName: "animation", config: config)

        if let animation = dotLottieAnimation {
            let animationView = animation.createDotLottieView()
            animationView.frame = CGRect(x: 50, y: 100, width: 300, height: 300)
            view.addSubview(animationView)
        }
    }
}
```
**API**: Use `AnimationConfig` to set `autoplay`, `loop`, `speed`, `mode`, `marker`, `layout`, `themeId`, etc. The `DotLottieAnimation` instance provides methods like `play()`, `pause()`, `stop()`, `setFrame()`, `loadStateMachine()`, and `postEvent()`.

## Android Player (Native Kotlin)

### Installation
Add the JitPack repository and the dependency to your Gradle files.
```groovy
// settings.gradle.kts
// ...
maven { url 'https://jitpack.io' }
// ...

// build.gradle.kts (app)
implementation 'com.github.LottieFiles:dotlottie-android:0.4.1'
```

### Usage (Jetpack Compose)
```kotlin
import androidx.compose.runtime.Composable
import com.lottiefiles.dotlottie.core.compose.ui.DotLottieAnimation
import com.lottiefiles.dotlottie.core.util.DotLottieSource

@Composable
fun BasicAnimation() {
    DotLottieAnimation(
        source = DotLottieSource.Url("https://lottie.host/animation.lottie"),
        autoplay = true,
        loop = true,
    )
}
```

### Usage (XML)
```xml
<com.lottiefiles.dotlottie.core.widget.DotLottieAnimation
    android:id="@+id/lottie_view"
    android:layout_width="200dp"
    android:layout_height="200dp"
    app:src="swinging.json"
    app:autoplay="true"
    app:loop="true" />
```
**API**: The Composable takes parameters like `source`, `autoplay`, `loop`, `speed`, and `controller`. The `DotLottieController` provides fine-grained control for playback, theming, and state machines.