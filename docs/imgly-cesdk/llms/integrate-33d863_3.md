# Source: https://img.ly/docs/cesdk/ios/import-media/capture-from-camera/integrate-33d863/

---
title: "Integrate Mobile Camera"
description: "Enable live camera capture in mobile apps to shoot and insert photos or videos."
platform: ios
url: "https://img.ly/docs/cesdk/ios/import-media/capture-from-camera/integrate-33d863/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/ios/import-media-4e3703/) > [Capture From Camera](https://img.ly/docs/cesdk/ios/import-media/capture-from-camera-92f388/) > [Integrate Mobile Camera](https://img.ly/docs/cesdk/ios/import-media/capture-from-camera/integrate-33d863/)

---

In this example, learn how to initialize the [CreativeEditor SDK](https://img.ly/products/creative-sdk)’s mobile camera in your iOS app.

Explore a full code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/camera-guides-quickstart/).

## Requirements

The mobile camera requires:

- iOS 16
- Swift 6.2 (Xcode 26.0.1) or later

### Using Swift Package Manager

If you use [Swift Package Manager](https://github.com/apple/swift-package-manager) to build your app, and want to integrate
the Creative Engine and UI modules using your regular workflows, add the [IMGLYUI Swift Package](https://github.com/imgly/IMGLYUI-swift) as a dependency to your project.

![](./assets/spm-ui-ios.png)

This package provides multiple library products. Add the default `IMGLYUI` library to your app target to add all available UI modules included in this package to your app.

To keep your app size minimal, only add the library product that you need, For example, only add the `IMGLYCamera` library if you need to `import IMGLYCamera` in your code.

![Settings location for modifying which part of the library is added](assets/integrate-ios-157-10.png)

On the *General* page of your app target's Xcode project settings the *Frameworks, Libraries, and Embedded Content* section lists all used library products. You can use the `+` and `-` buttons to change them.

## Usage

This example shows the basic usage of the camera.

### Launch the Camera

You can get started right away by importing the camera module into your own code.

<Tabs syncKey="code-language">
  <TabItem label="SwiftUI">
    ```swift
    import IMGLYCamera
    ```
  </TabItem>

  <TabItem label="UIKit">
    ```swift
    import IMGLYCamera
    ```
  </TabItem>
</Tabs>

In this integration example, the camera is presented as a modal view after tapping a button.

<Tabs syncKey="code-language">
  <TabItem label="SwiftUI">
    ```swift
        Button("Use the Camera") {
          isPresented = true
        }
    ```
  </TabItem>

  <TabItem label="UIKit">
    ```swift
      private lazy var button = UIButton(
        type: .system,
        primaryAction: UIAction(title: "Use the Camera") { [unowned self] _ in
          camera.modalPresentationStyle = .fullScreen
          present(camera, animated: true)
        }
      )
    ```
  </TabItem>
</Tabs>

### Initialization

The camera is initialized with `EngineSettings`. You need to provide the **license key** that you received from IMG.LY.
Optionally, you can provide a **unique ID** tied to your application's user. This helps us accurately calculate monthly active users (MAU) and it is especially useful when one person uses the app on multiple devices with a sign-in feature, ensuring they’re counted once.

<Tabs syncKey="code-language">
  <TabItem label="SwiftUI">
    ```swift
          Camera(.init(license: secrets.licenseKey,
                       userID: "<your unique user id>")) { result in
    ```
  </TabItem>

  <TabItem label="UIKit">
    ```swift
        Camera(.init(license: secrets.licenseKey,
                     userID: "<your unique user id>")) { result in
    ```
  </TabItem>
</Tabs>

### Result

The `Camera`’s `onDismiss` closure returns a `Result<CameraResult, CameraError>`. If the user has recorded videos, the `.success(_)` case contains the `CameraResult`.

<Tabs syncKey="code-language">
  <TabItem label="SwiftUI">
    ```swift
            switch result {
            case let .success(.recording(recordings)):
              let urls = recordings.flatMap { $0.videos.map(\.url) }
              let recordedVideos = urls
              // Do something with the recorded videos
              print(recordedVideos)

            case .success(.reaction):
              print("Reaction case not handled here")

            case let .failure(error):
              print(error.localizedDescription)
              isPresented = false
            }

    ```
  </TabItem>

  <TabItem label="UIKit">
    ```swift
          switch result {
          case let .success(.recording(recordings)):
            let urls = recordings.flatMap { $0.videos.map(\.url) }
            let recordedVideos = urls
            // Do something with the recorded videos
            print(recordedVideos)

          case .success(.reaction):
            print("Reaction case not handled here")

          case let .failure(error):
            print(error.localizedDescription)
            self.presentedViewController?.dismiss(animated: true)
          }
    ```
  </TabItem>
</Tabs>

When using UIKit, it needs to be integrated with a `UIHostingController` object into a UIKit view hierarchy.

```swift
  private lazy var camera = UIHostingController(rootView:
    Camera(.init(license: secrets.licenseKey,
                 userID: "<your unique user id>")) { result in
      switch result {
      case let .success(.recording(recordings)):
        let urls = recordings.flatMap { $0.videos.map(\.url) }
        let recordedVideos = urls
        // Do something with the recorded videos
        print(recordedVideos)

      case .success(.reaction):
        print("Reaction case not handled here")

      case let .failure(error):
        print(error.localizedDescription)
        self.presentedViewController?.dismiss(animated: true)
      }
    })
```

### Environment

When using SwiftUI, the camera is best opened in a [`fullScreenCover`](https://developer.apple.com/documentation/swiftui/view/fullscreencover\(ispresented:ondismiss:content:\)).

```swift
    .fullScreenCover(isPresented: $isPresented) {
```

## Full Code

Here's the full code:

<Tabs syncKey="code-language">
  <TabItem label="SwiftUI">
    ```swift
    import IMGLYCamera

    import SwiftUI

    struct CameraSwiftUI: View {
    @State private var isPresented = false

    var body: some View {
    Button("Use the Camera") {
    isPresented = true
    }

        .fullScreenCover(isPresented: $isPresented) {
          Camera(.init(license: secrets.licenseKey,
                       userID: "<your unique user id>")) { result in
            switch result {
            case let .success(.recording(recordings)):
              let urls = recordings.flatMap { $0.videos.map(\.url) }
              let recordedVideos = urls
              // Do something with the recorded videos
              print(recordedVideos)

            case .success(.reaction):
              print("Reaction case not handled here")

            case let .failure(error):
              print(error.localizedDescription)
              isPresented = false
            }
          }
        }

    }
    }

    ```
  </TabItem>

  <TabItem label="UIKit">
    ```swift
    import IMGLYCamera

    import SwiftUI

    class CameraUIKit: UIViewController {
      private lazy var camera = UIHostingController(rootView:
        Camera(.init(license: secrets.licenseKey,
                     userID: "<your unique user id>")) { result in
          switch result {
          case let .success(.recording(recordings)):
            let urls = recordings.flatMap { $0.videos.map(\.url) }
            let recordedVideos = urls
            // Do something with the recorded videos
            print(recordedVideos)

          case .success(.reaction):
            print("Reaction case not handled here")

          case let .failure(error):
            print(error.localizedDescription)
            self.presentedViewController?.dismiss(animated: true)
          }
        })

      private lazy var button = UIButton(
        type: .system,
        primaryAction: UIAction(title: "Use the Camera") { [unowned self] _ in
          camera.modalPresentationStyle = .fullScreen
          present(camera, animated: true)
        }
      )

      override func viewDidLoad() {
        super.viewDidLoad()

        view.addSubview(button)
        button.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
          button.centerXAnchor.constraint(equalTo: view.centerXAnchor),
          button.centerYAnchor.constraint(equalTo: view.centerYAnchor),
        ])
      }
    }
    ```
  </TabItem>
</Tabs>



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
