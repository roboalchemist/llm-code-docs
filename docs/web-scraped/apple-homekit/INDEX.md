# Apple HomeKit Framework Documentation

Official Apple HomeKit framework documentation for iOS, macOS, tvOS, and watchOS developers.

## Documentation Source

- [HomeKit Framework](https://developer.apple.com/documentation/homekit/)
- [HomeKit Accessory Protocol Specification](https://developer.apple.com/homekit/)

## Overview

HomeKit is Apple's framework for building home automation applications. It enables developers to:

- Discover and manage HomeKit-compatible accessories
- Control lights, thermostats, locks, cameras, and other smart home devices
- Create automation rules and scenes
- Stream video from HomeKit cameras
- Manage user access and permissions

## Coverage

This documentation set covers:

- **Framework Architecture** - Core classes and patterns
- **Home Management** - Managing homes, rooms, accessories
- **Accessories & Services** - Understanding device capabilities
- **Characteristics** - Reading, writing, and observing device properties
- **Automation** - Timer-based and event-based automation rules
- **Scenes** - Grouping accessories for coordinated control
- **Camera Streaming** - Video from HomeKit cameras and doorbells
- **Matter Support** - Working with Matter accessories
- **Error Handling** - Common errors and solutions

## Table of Contents

1. [HomeKit Framework Overview](001-homekit-framework-overview.md)
   - Introduction to HomeKit
   - Core components and architecture
   - Getting started guide
   - Key concepts and terminology

2. [HMHomeManager Class Reference](002-hmhomemanager.md)
   - Managing homes in HomeKit database
   - Authorization and permissions
   - Creating, updating, and removing homes
   - Observing home changes

3. [HMHome Class Reference](003-hmhome.md)
   - Home configuration and management
   - Managing rooms, accessories, and zones
   - Creating scenes and automation rules
   - User access control

4. [Characteristics and Services Reference](004-characteristics-and-services.md)
   - Understanding services (lights, thermostats, locks, etc.)
   - Reading and writing characteristics
   - Observing characteristic changes
   - Handling errors

5. [Automation and Scenes](005-automation-and-scenes.md)
   - Creating and executing scenes
   - Timer-based automation triggers
   - Event-based automation triggers
   - Action sets and conditions

## Quick Start

### 1. Set Up HomeKit

```swift
import HomeKit

let homeManager = HMHomeManager()

// Check authorization
let status = HMHomeManager.authorizationStatus()
if status == .authorized {
    // Access homes
    let homes = homeManager.homes
}
```

### 2. Access Home Information

```swift
if let home = homeManager.primaryHome {
    // Get accessories
    for accessory in home.accessories {
        print("Accessory: \(accessory.name)")
    }

    // Find lights
    let lights = home.accessoriesWithServices(ofType: HMServiceTypeLight)
}
```

### 3. Control Accessories

```swift
let light: HMAccessory = ...

if let service = light.services.first(where: { $0.serviceType == HMServiceTypeLight }) {
    if let powerChar = service.characteristics.first(where: { $0.characteristicType == HMCharacteristicTypePowerState }) {
        do {
            try await powerChar.writeValue(1)  // Turn on
        } catch {
            print("Failed: \(error)")
        }
    }
}
```

### 4. Create Scenes

```swift
let home: HMHome = ...

do {
    let scene = try await home.addScene(withName: "Good Night")
    // Add actions to scene
    // ...
} catch {
    print("Failed to create scene: \(error)")
}
```

### 5. Set Up Automation

```swift
// Timer trigger - runs at specific time
let trigger = HMTimerTrigger(
    name: "Morning Lights",
    fireDate: Date(),
    recurrence: .daily
)

do {
    try await home.addTrigger(trigger)
} catch {
    print("Failed to add trigger: \(error)")
}
```

## Platform Support

- **iOS**: 8.0+
- **macOS**: 10.12+
- **tvOS**: 10.1+
- **watchOS**: 2.0+
- **Camera Streaming**: tvOS 17.1+, iOS 17.1+, macOS 14.1+

## Key Features by Platform

### iOS
- Full HomeKit framework support
- Remote access via iCloud
- Siri integration
- Background execution

### macOS
- Full HomeKit framework support
- HomeKit hub functionality
- Remote access coordination

### tvOS
- HomeKit hub (manage remote access)
- Full remote access capability
- Scene execution via Siri

### watchOS
- Limited HomeKit support
- Control scenes and accessories
- View status

## Common Tasks

### Enable HomeKit in Your App

1. Add HomeKit capability in Xcode
2. Request authorization when needed
3. Implement error handling

### Control a Light

```swift
// Find light service
if let lightService = accessory.services.first(where: { $0.serviceType == HMServiceTypeLight }) {
    // Find power characteristic
    if let powerChar = lightService.characteristics.first(where: { $0.characteristicType == HMCharacteristicTypePowerState }) {
        // Write new value
        try await powerChar.writeValue(1)
    }
}
```

### Create a Scene

```swift
// Create scene
let scene = try await home.addScene(withName: "Evening")

// Add accessories and their target states
// Users can activate via app or Siri
```

### Automate Actions

```swift
// Timer: Every morning at 7 AM
let trigger = HMTimerTrigger(name: "Morning", fireDate: Date(), recurrence: .daily)
try await home.addTrigger(trigger)

// Event: When motion detected
let event = HMEventCharacteristicHasValue(characteristic: motionSensor, triggerValue: 1)
let eventTrigger = HMEventTrigger(name: "Motion", events: [event], condition: nil)
try await home.addTrigger(eventTrigger)
```

## Error Handling

HomeKit operations throw `HMError`. Common error codes:

- `authorizationDenied` - User denied HomeKit permission
- `accessoryNotResponding` - Accessory offline or unreachable
- `cannotActivateAccessory` - Accessory cannot be activated
- `unsupportedCharacteristic` - Characteristic not supported
- `accessoryDisconnected` - Accessory disconnected during operation

```swift
do {
    try await characteristic.writeValue(newValue)
} catch let error as HMError {
    print("HomeKit error: \(error.code)")
}
```

## Best Practices

1. **Check Authorization First** - Always verify user granted HomeKit permission
2. **Handle Disconnections** - Accessories can go offline anytime
3. **Use Async/Await** - HomeKit operations are asynchronous
4. **Observe Changes** - Enable notifications for real-time updates
5. **Cache Metadata** - Avoid repeated queries for characteristic metadata
6. **Test Thoroughly** - Use HomeKit Accessory Simulator for testing
7. **Respect Privacy** - Only request permissions when necessary

## Testing

Use the **HomeKit Accessory Simulator** (available in Additional Tools) to:

- Simulate HomeKit accessories
- Test automation and scenes
- Test error conditions
- Verify app behavior without physical accessories

Location: `~/Library/Developer/Xcode/Additional/HomeKit\ Accessory\ Simulator.app`

## Sample Code

Apple provides sample code projects in the [Sample Code Library](https://developer.apple.com/sample-code/):

- Building a HomeKit app
- HomeKit accessory simulation
- Remote access patterns
- Camera streaming

## References

- [HomeKit Framework API Reference](https://developer.apple.com/documentation/homekit)
- [HomeKit Design Guidelines](https://developer.apple.com/design/homekit/)
- [HomeKit Accessory Protocol Spec](https://developer.apple.com/homekit/)
- [HomeKit Forum](https://forums.developer.apple.com/forums/thread/HomeKit)
- [WWDC Sessions on HomeKit](https://developer.apple.com/videos/play/wwdc2023/?q=homekit)

## Additional Resources

- [HomeKit Setup Code Format](https://developer.apple.com/homekit/HomeKit-Setup-Code-Format/)
- [HomeKit Accessory Setup](https://developer.apple.com/documentation/homekit/setting_up_a_homekit_accessory/)
- [Matter Integration](https://developer.apple.com/documentation/homekit/integrating_matter_accessories/)
- [Camera Video Streaming](https://developer.apple.com/documentation/homekit/providing_homekit_camera_recordings_in_the_home_app/)

---

**Last Updated**: March 2026
**Relevant for**: iOS 8+, macOS 10.12+, tvOS 10.1+, watchOS 2.0+
