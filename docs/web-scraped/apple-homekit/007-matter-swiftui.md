# HomeKit: SwiftUI and Matter Integration

## Structure: CameraView

**Availability:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

```swift
@MainActor @preconcurrency struct CameraView
```

A SwiftUI view into which a video stream or an image snapshot is rendered.

### Creating a camera view

#### `init(source: HMCameraSource)`

Creates a new camera view using the given source.


#### `class HMCameraSource`

An abstract class for a camera’s data source.


### Relationships (CameraView)

**Conforms To:**

- `Sendable`
- `SendableMetatype`
- `View`

### See Also: Managing camera profiles (CameraView)

- **cameraProfiles**: An array of camera profiles implemented by the accessory.
- **HMCameraProfile**: A camera profile that interacts with an accessory’s camera.
- **HMCameraView**: The view into which a video stream or an image snapshot is rendered.

---

## Class: HMCameraView

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+

```swift
class HMCameraView
```

The view into which a video stream or an image snapshot is rendered.

### Getting the Camera Source

#### `var cameraSource: HMCameraSource?`


#### `class HMCameraSource` (HMCameraView)

An abstract class for a camera’s data source.


### Initializers (HMCameraView)

#### `init()`


### Relationships (HMCameraView)

**Inherits From:**

- `UIView`

**Conforms To:**

- `CALayerDelegate`
- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCoding`
- `NSObjectProtocol`
- `NSTouchBarProvider`
- `UIAccessibilityIdentification`
- `UIActivityItemsConfigurationProviding`
- `UIAppearance`
- `UIAppearanceContainer`
- `UICoordinateSpace`
- `UIDynamicItem`
- `UIFocusEnvironment`
- `UIFocusItem`
- `UIFocusItemContainer`
- `UILargeContentViewerItem`
- `UIPasteConfigurationSupporting`
- `UIPopoverPresentationControllerSourceItem`
- `UIResponderStandardEditActions`
- `UITraitChangeObservable`
- `UITraitEnvironment`
- `UIUserActivityRestoring`

### See Also: Managing camera profiles (HMCameraView)

- **CameraView**: A SwiftUI view into which a video stream or an image snapshot is rendered.
- **cameraProfiles**: An array of camera profiles implemented by the accessory.
- **HMCameraProfile**: A camera profile that interacts with an accessory’s camera.

---

