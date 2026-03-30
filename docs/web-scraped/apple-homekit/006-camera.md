# HomeKit: Camera

Classes for accessing and controlling camera accessories.

## Class: HMCameraProfile

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
class HMCameraProfile
```


Each profile control is optional, because an individual camera vendor may not support all of the features defined by the HomeKit camera specifications.

A camera profile that interacts with an accessory’s camera.

### Controlling camera settings

#### `var settingsControl: HMCameraSettingsControl?`

Controls the settings on the camera.


#### `class HMCameraSettingsControl`

An object that represents the ability to control a camera’s settings.


#### `class HMCameraControl`

An abstract class that represents a camera control.


### Playing audio

#### `var microphoneControl: HMCameraAudioControl?`

Controls the microphone settings on the camera.


#### `var speakerControl: HMCameraAudioControl?`

Controls the speaker settings on the camera.


#### `class HMCameraAudioControl`

An object that controls a camera’s audio settings.


### Streaming

#### `var streamControl: HMCameraStreamControl?`

Controls the camera stream.


#### `class HMCameraStreamControl`

An object that can start and stop the camera stream and contains the view into which the stream is rendered.


### Capturing snapshots

#### `var snapshotControl: HMCameraSnapshotControl?`

Controls the camera’s snapshot function.


#### `class HMCameraSnapshotControl`

An object that can take an image snapshot from a camera.


### Relationships (HMCameraProfile)

**Inherits From:**

- `HMAccessoryProfile`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Managing accessory profiles

- **profiles**: An array of profiles implemented by the accessory.
- **HMAccessoryProfile**: A profile that certain accessories implement.
- **HMNetworkConfigurationProfile**: A profile that provides information about network protection for an accessory.

---

## Class: HMCameraControl

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
class HMCameraControl
```

An abstract class that represents a camera control.

### Initializers (HMCameraControl)

#### `init()` **(Deprecated)**


### Relationships (HMCameraControl)

**Inherits From:**

- `NSObject`

**Inherited By:**

- `HMCameraAudioControl`
- `HMCameraSettingsControl`
- `HMCameraSnapshotControl`
- `HMCameraStreamControl`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Controlling camera settings (HMCameraControl)

- **settingsControl**: Controls the settings on the camera.
- **HMCameraSettingsControl**: An object that represents the ability to control a camera’s settings.

---

## Class: HMCameraAudioControl

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
class HMCameraAudioControl
```

An object that controls a camera’s audio settings.

### Controlling audio characteristics

#### `var mute: HMCharacteristic?`


#### `var volume: HMCharacteristic?`


### Relationships (HMCameraAudioControl)

**Inherits From:**

- `HMCameraControl`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Playing audio

- **microphoneControl**: Controls the microphone settings on the camera.
- **speakerControl**: Controls the speaker settings on the camera.

---

## Class: HMCameraSettingsControl

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
class HMCameraSettingsControl
```

An object that represents the ability to control a camera’s settings.

### Controlling camera characteristics

#### `var currentHorizontalTilt: HMCharacteristic?`

Characteristic corresponding to the camera’s current horizontal tilt setting.


#### `var targetHorizontalTilt: HMCharacteristic?`

Characteristic corresponding to adjusting the camera’s horizontal tilt setting.


#### `var currentVerticalTilt: HMCharacteristic?`

Characteristic corresponding to the camera’s current vertical tilt setting.


#### `var targetVerticalTilt: HMCharacteristic?`

Characteristic corresponding to adjusting the camera’s vertical tilt setting.


#### `var opticalZoom: HMCharacteristic?`

Characteristic corresponding to the camera’s optical zoom setting.


#### `var digitalZoom: HMCharacteristic?`

Characteristic corresponding to the camera’s digital zoom setting.


#### `var imageMirroring: HMCharacteristic?`

Characteristic corresponding to the camera’s image mirroring setting.


#### `var imageRotation: HMCharacteristic?`

Characteristic corresponding to the camera’s image rotation setting.


#### `var nightVision: HMCharacteristic?`

Characteristic corresponding to the camera’s night vision setting.


### Relationships (HMCameraSettingsControl)

**Inherits From:**

- `HMCameraControl`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Controlling camera settings (HMCameraSettingsControl)

- **settingsControl**: Controls the settings on the camera.
- **HMCameraControl**: An abstract class that represents a camera control.

---

## Class: HMCameraSnapshot

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
class HMCameraSnapshot
```

An object that represents a snapshot taken from a camera.

### Accessing snapshot properties

#### `var captureDate: Date`

Date and time at which the snapshot was requested.


### Initializers (HMCameraSnapshot)

#### `init()` **(Deprecated)** (HMCameraSnapshot)


### Relationships (HMCameraSnapshot)

**Inherits From:**

- `HMCameraSource`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Taking snapshots

- **takeSnapshot()**: Takes an image snapshot.
- **mostRecentSnapshot**: The camera’s most recent snapshot.

---

## Class: HMCameraSnapshotControl

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
class HMCameraSnapshotControl
```

An object that can take an image snapshot from a camera.

### Taking snapshots

#### `func takeSnapshot()`

Takes an image snapshot.


#### `var mostRecentSnapshot: HMCameraSnapshot?`

The camera’s most recent snapshot.


#### `class HMCameraSnapshot`

An object that represents a snapshot taken from a camera.


### Observing snapshot activity

#### `var delegate: (any HMCameraSnapshotControlDelegate)?`

Delegate that receives updates as the camera takes snapshots.


#### `protocol HMCameraSnapshotControlDelegate`

A set of methods used to observe the camera’s snapshot activity.


### Initializers (HMCameraSnapshotControl)

#### `init()` **(Deprecated)** (HMCameraSnapshotControl)


### Relationships (HMCameraSnapshotControl)

**Inherits From:**

- `HMCameraControl`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Capturing snapshots

- **snapshotControl**: Controls the camera’s snapshot function.

---

## Class: HMCameraStream

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
class HMCameraStream
```

An object that represents a camera’s audiovisual stream.

### Configuring the audio stream

#### `var audioStreamSetting: HMCameraAudioStreamSetting`

The stream’s current audio setting.


#### `func updateAudioStreamSetting(HMCameraAudioStreamSetting, completionHandler: ((any Error)?) -> Void)`

Updates an audio stream’s settings.


#### `func setAudioStreamSetting(HMCameraAudioStreamSetting)` **(Deprecated)**


#### `enum HMCameraAudioStreamSetting`

The options associated with a camera’s audio stream.


### Initializers (HMCameraStream)

#### `init()` **(Deprecated)** (HMCameraStream)


### Relationships (HMCameraStream)

**Inherits From:**

- `HMCameraSource`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Controlling the stream (HMCameraStream)

- **startStream()**: Starts the camera stream.
- **stopStream()**: Stops the camera stream.
- **cameraStream**: The current camera stream.
- **streamState**: The current state of the camera stream.
- **HMCameraStreamState**: The states associated with a camera stream.

---

## Class: HMCameraStreamControl

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
class HMCameraStreamControl
```

An object that can start and stop the camera stream and contains the view into which the stream is rendered.

### Controlling the stream

#### `func startStream()`

Starts the camera stream.


#### `func stopStream()`

Stops the camera stream.


#### `var cameraStream: HMCameraStream?`

The current camera stream.


#### `class HMCameraStream`

An object that represents a camera’s audiovisual stream.


#### `var streamState: HMCameraStreamState`

The current state of the camera stream.


#### `enum HMCameraStreamState`

The states associated with a camera stream.


### Observing stream activity

#### `var delegate: (any HMCameraStreamControlDelegate)?`

Delegate that receives updates as the camera stream changes.


#### `protocol HMCameraStreamControlDelegate`

A protocol that gives the delegate updates on the camera stream.


### Initializers (HMCameraStreamControl)

#### `init()` **(Deprecated)** (HMCameraStreamControl)


### Relationships (HMCameraStreamControl)

**Inherits From:**

- `HMCameraControl`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Streaming

- **streamControl**: Controls the camera stream.

---

## Enumeration: HMCameraStreamState

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
enum HMCameraStreamState
```

The states associated with a camera stream.

### Observing the streaming state

#### `case notStreaming`

The state when the camera stream is not active.


#### `case starting`

The state when the camera stream start request is processing.


#### `case stopping`

The state when the camera stream is stopping.


#### `case streaming`

The state when the camera stream is currently in progress.


### Initializers (HMCameraStreamState)

#### `init?(rawValue: UInt)`


### Relationships (HMCameraStreamState)

**Conforms To:**

- `BitwiseCopyable`
- `Equatable`
- `Hashable`
- `RawRepresentable`
- `Sendable`
- `SendableMetatype`

### See Also: Controlling the stream (HMCameraStreamState)

- **startStream()**: Starts the camera stream.
- **stopStream()**: Stops the camera stream.
- **cameraStream**: The current camera stream.
- **HMCameraStream**: An object that represents a camera’s audiovisual stream.
- **streamState**: The current state of the camera stream.

---

