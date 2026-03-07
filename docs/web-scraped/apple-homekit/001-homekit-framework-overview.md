# HomeKit Framework Overview

## Introduction

HomeKit enables your app to coordinate and control home automation accessories from multiple vendors to present a coherent, user-focused interface.

Using HomeKit, your app can:

- Discover HomeKit-compatible automation accessories and add them to a persistent, cross-device home configuration database
- Display, edit, and act upon the data in the home configuration database
- Communicate with configured accessories and services in order to perform actions like turning on the lights in the living room
- Create groups of accessories and services called action sets
- Create timers and event-triggered automation workflows
- Set up secure remote access to control your home while away
- View live camera streams from HomeKit cameras and video doorbells

## Framework Architecture

### Core Components

The HomeKit framework provides these main classes:

- **HMHomeManager** - Manages all homes and their accessories in the user's HomeKit database
- **HMHome** - Represents a single home with rooms, accessories, and automation rules
- **HMRoom** - Groups accessories within a home (e.g., "Living Room")
- **HMAccessory** - Represents a physical smart home device
- **HMService** - A service provided by an accessory (e.g., a light service)
- **HMCharacteristic** - Individual properties of a service (e.g., brightness)
- **HMTrigger** - Automation rules (timers and events)
- **HMScene** - Sets a group of accessories to specific states
- **HMActionSet** - Groups actions to be executed together

### Permissions & Authorization

HomeKit requires explicit user permission to access home data. Use `HMHomeManager` to request authorization status:

```swift
let manager = HMHomeManager()
// Check authorization status
let status = HMHomeManager.authorizationStatus()
```

Authorization statuses:

- `notDetermined` - User hasn't made a choice yet
- `restricted` - User cannot change authorization
- `denied` - User denied HomeKit access
- `authorized` - HomeKit access is authorized

## Getting Started

### Step 1: Enable HomeKit Capability

In Xcode, add the HomeKit capability to your app's entitlements.

### Step 2: Request Authorization

```swift
let manager = HMHomeManager()
```

When a user first uses HomeKit features, the system will prompt for permission.

### Step 3: Access Homes

```swift
let homes = manager.homes
let home = manager.primaryHome
```

### Step 4: Control Accessories

```swift
for accessory in home.accessoriesWithServices(ofType: HMServiceTypeLight) {
    if let lightService = accessory.services.first(where: { $0.serviceType == HMServiceTypeLight }) {
        if let brightnessCharacteristic = lightService.characteristics.first(where: { $0.characteristicType == HMCharacteristicTypeBrightness }) {
            try await brightnessCharacteristic.writeValue(100)
        }
    }
}
```

## Key Concepts

### Service Types

Common service types defined in HomeKit:

- `HMServiceTypeLight` - Lightbulb
- `HMServiceTypeThermostat` - Thermostat
- `HMServiceTypeSwitch` - Switch
- `HMServiceTypeLock` - Door lock
- `HMServiceTypeCameraRTPStreamManagement` - Camera
- `HMServiceTypeDoorbell` - Doorbell
- `HMServiceTypeFan` - Fan
- `HMServiceTypeOutlet` - Electrical outlet
- `HMServiceTypeHumidifier` - Humidifier/dehumidifier
- `HMServiceTypeMotionSensor` - Motion sensor
- `HMServiceTypeContactSensor` - Contact sensor
- `HMServiceTypeTemperatureSensor` - Temperature sensor

### Characteristic Types

Common characteristic types:

- `HMCharacteristicTypePowerState` - On/off state
- `HMCharacteristicTypeBrightness` - Light brightness (0-100)
- `HMCharacteristicTypeCurrentTemperature` - Current temperature
- `HMCharacteristicTypeTargetTemperature` - Desired temperature
- `HMCharacteristicTypeLockCurrentState` - Lock state
- `HMCharacteristicTypeLockTargetState` - Lock target state
- `HMCharacteristicTypeCurrentRelativeHumidity` - Humidity level
- `HMCharacteristicTypeContactState` - Contact sensor state
- `HMCharacteristicTypeMotionDetected` - Motion detection state

## Observation & Notifications

### Observe Characteristic Changes

```swift
let characteristic: HMCharacteristic = ...
// Set up observation
try await characteristic.enableNotification(true)

// Listen for changes
NotificationCenter.default.addObserver(
    forName: HMCharacteristicDidUpdateValueNotification,
    object: characteristic,
    queue: .main
) { _ in
    // Characteristic value changed
}
```

### Observe Home Changes

```swift
let home: HMHome = ...
let observation = home.objectWillChangePublisher.sink { _ in
    // Home configuration changed
}
```

## Camera Streaming

HomeKit supports secure SRTP video and audio streaming from cameras and video doorbells.

### HMCameraProfile

Access camera capabilities:

```swift
if let cameraProfile = accessory.cameraProfiles.first {
    // Camera information
    let info = cameraProfile.cameraInformation

    // Video stream settings
    let settings = cameraProfile.streamingVideoSettings
    let audioSettings = cameraProfile.streamingAudioSettings
}
```

### Starting a Stream

```swift
let controller = HMCameraStreamController()
try await controller.startStream(with: sessionID, controller: delegate)
```

## Matter Accessory Support

HomeKit supports Matter accessories in addition to HomeKit native accessories.

- Matter accessories integrate with HomeKit framework
- Same HMHome, HMAccessory, HMService APIs apply
- Matter accessories provide enhanced interoperability

## Automation & Scenes

### Scenes

Scenes are named groups of accessory states that can be activated at once:

```swift
// Create a scene
let scene = try await home.addScene(withName: "Good Morning")

// Add accessory state to scene
let light: HMAccessory = ...
let service = light.services.first!
let powerChar = service.characteristics.first!
try await scene.addAccessoryWithState(HMAccessoryPowerState(accessory: light, state: true))

// Activate scene
try await scene.executeActionSet(scene.actionSets.first!)
```

### Automation Rules

Automation rules (triggers) execute action sets based on time or events:

```swift
// Timer trigger - execute at specific time
let trigger = HMTimerTrigger(name: "Morning", fireDate: Date(), recurrence: .daily)

// Event trigger - execute when something happens
let trigger = HMEventTrigger(name: "Motion", events: [motionEvent], condition: nil)

// Add to home
try await home.addTrigger(trigger)
```

## Error Handling

HomeKit operations throw `HMError`:

```swift
do {
    try await characteristic.writeValue(newValue)
} catch let error as HMError {
    switch error.code {
    case .authorizationDenied:
        print("HomeKit authorization denied")
    case .accessoryNotResponding:
        print("Accessory is not responding")
    case .cannotActivateAccessory:
        print("Cannot activate this accessory")
    case .unsupportedCharacteristic:
        print("Unsupported characteristic")
    @unknown default:
        print("Other error: \(error)")
    }
}
```

## Best Practices

1. **Check Authorization First** - Always verify HomeKit authorization before accessing homes

2. **Handle Errors** - Network calls and accessory control can fail; handle errors gracefully

3. **Observe Changes** - Enable notifications for characteristics that users might control externally

4. **Batch Operations** - Group multiple accessory updates to improve performance

5. **Test with Simulator** - Use the HomeKit Accessory Simulator for testing (available in Additional Tools)

6. **Provide Feedback** - Show users progress when controlling accessories, as operations may take time

7. **Respect Privacy** - Only request HomeKit permissions when needed and explain why to users

## Platform Availability

- iOS 8.0+
- macOS 10.12+
- tvOS 10.1+
- watchOS 2.0+

For camera streaming (tvOS 17.1+, iOS 17.1+, macOS 14.1+).

## References

- [HomeKit Accessory Protocol Specification](https://developer.apple.com/homekit/)
- [HomeKit Sample Code](https://developer.apple.com/sample-code/)
- [HomeKit Developer Forum](https://forums.developer.apple.com/)
