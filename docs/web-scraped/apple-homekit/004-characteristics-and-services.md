# Characteristics and Services Reference

## Services Overview

Services are provided by accessories and represent functional capabilities. Each service contains characteristics.

### Common Service Types

```swift
// Lighting
HMServiceTypeLight

// Environmental Control
HMServiceTypeThermostat
HMServiceTypeHumidifier

// Security
HMServiceTypeLock
HMServiceTypeDoorlock

// Sensing
HMServiceTypeTemperatureSensor
HMServiceTypeContactSensor
HMServiceTypeMotionSensor
HMServiceTypeOccupancySensor
HMServiceTypeCarbonMonoxideSensor
HMServiceTypeCarbonDioxideSensor
HMServiceTypeSmokeSensor
HMServiceTypeLeakSensor

// Media
HMServiceTypeTelevision
HMServiceTypeCameraRTPStreamManagement
HMServiceTypeDoorbell

// Outlets and Switches
HMServiceTypeOutlet
HMServiceTypeSwitch
HMServiceTypeStatelessSwitch

// Accessibility
HMServiceTypeGarageDoorOpener
HMServiceTypeCurtain
HMServiceTypeRollerShutter
HMServiceTypeWindow
HMServiceTypeWindowCovering
```

## Characteristics Overview

Characteristics are individual properties of services that can be read, written, or observed.

### Reading Characteristics

```swift
let service: HMService = ...
if let characteristic = service.characteristics.first(where: { $0.characteristicType == HMCharacteristicTypeBrightness }) {
    if let value = characteristic.value as? Int {
        print("Brightness: \(value)")
    }
}
```

### Writing Characteristics

```swift
let characteristic: HMCharacteristic = ...
do {
    try await characteristic.writeValue(75)
    print("Value written successfully")
} catch {
    print("Failed to write value: \(error)")
}
```

### Observing Characteristics

Enable notifications to observe changes:

```swift
let characteristic: HMCharacteristic = ...

// Enable notifications
do {
    try await characteristic.enableNotification(true)
} catch {
    print("Failed to enable notifications: \(error)")
}

// Listen for changes
NotificationCenter.default.addObserver(
    forName: HMCharacteristicDidUpdateValueNotification,
    object: characteristic,
    queue: .main
) { _ in
    print("Characteristic updated: \(characteristic.value ?? "")")
}
```

## Common Characteristic Types

### Power/State

**HMCharacteristicTypePowerState**
- Values: 0 (off), 1 (on)
- Used in: lights, switches, outlets

```swift
try await characteristic.writeValue(1)  // Turn on
try await characteristic.writeValue(0)  // Turn off
```

### Brightness

**HMCharacteristicTypeBrightness**
- Values: 0-100 (percentage)
- Used in: lights, dimmable switches

```swift
try await characteristic.writeValue(75)  // 75% brightness
```

### Temperature

**HMCharacteristicTypeCurrentTemperature**
- Read-only: actual temperature
- Units: Celsius

**HMCharacteristicTypeTargetTemperature**
- Read/Write: desired temperature
- Units: Celsius

```swift
// Set thermostat to 21°C
try await targetTempChar.writeValue(21)
```

### Lock State

**HMCharacteristicTypeLockCurrentState**
- Values: 0 (unsecured), 1 (secured), 2 (unknown), 3 (jammed)
- Read-only

**HMCharacteristicTypeLockTargetState**
- Values: 0 (unsecured), 1 (secured)
- Read/Write

```swift
// Lock a door
try await lockTargetChar.writeValue(1)

// Unlock a door
try await lockTargetChar.writeValue(0)
```

### Hue and Saturation

**HMCharacteristicTypeHue**
- Values: 0-360 (degrees)
- Used in: color-capable lights

**HMCharacteristicTypeSaturation**
- Values: 0-100 (percentage)
- Used in: color-capable lights

### Contact & Motion

**HMCharacteristicTypeContactState**
- Values: 0 (open), 1 (closed)
- Read-only, sensor

**HMCharacteristicTypeMotionDetected**
- Values: 0 (no motion), 1 (motion detected)
- Read-only, sensor

### Occupancy

**HMCharacteristicTypeOccupancyDetected**
- Values: 0 (not occupied), 1 (occupied)
- Read-only, sensor

### Humidity

**HMCharacteristicTypeCurrentRelativeHumidity**
- Values: 0-100 (percentage)
- Read-only, sensor

**HMCharacteristicTypeTargetRelativeHumidity**
- Values: 0-100 (percentage)
- Read/Write, humidifier

## Characteristic Properties

### Readable

Characteristic has a readable value:

```swift
if characteristic.properties.contains(.readable) {
    let value = characteristic.value
}
```

### Writable

Characteristic can be written to:

```swift
if characteristic.properties.contains(.writable) {
    try await characteristic.writeValue(newValue)
}
```

### Notification

Characteristic can send notifications when value changes:

```swift
if characteristic.properties.contains(.supportsEventNotification) {
    try await characteristic.enableNotification(true)
}
```

## Handling Errors

Common errors when working with characteristics:

```swift
do {
    try await characteristic.writeValue(value)
} catch let error as HMError {
    switch error.code {
    case .unsupportedCharacteristic:
        print("This accessory doesn't support this operation")
    case .accessoryNotResponding:
        print("The accessory is not responding")
    case .cannotActivateAccessory:
        print("Cannot activate this accessory")
    case .accessoryDisconnected:
        print("Accessory is disconnected")
    default:
        print("Error: \(error.localizedDescription)")
    }
}
```

## Characteristic Metadata

Get information about a characteristic:

```swift
let characteristic: HMCharacteristic = ...

// Get characteristic type
print("Type: \(characteristic.characteristicType)")

// Get properties
print("Readable: \(characteristic.properties.contains(.readable))")
print("Writable: \(characteristic.properties.contains(.writable))")
print("Notifiable: \(characteristic.properties.contains(.supportsEventNotification))")

// Get min/max values if available
if let minValue = characteristic.metadata?.minimumValue {
    print("Min: \(minValue)")
}
if let maxValue = characteristic.metadata?.maximumValue {
    print("Max: \(maxValue)")
}

// Get units
if let units = characteristic.metadata?.units {
    print("Units: \(units)")
}
```

## Best Practices

1. **Always check properties before reading/writing**
2. **Enable notifications only for characteristics you observe**
3. **Cache metadata values to avoid repeated lookups**
4. **Handle errors gracefully - accessories may disconnect**
5. **Use value types for numeric characteristics**
6. **Test with real accessories - simulators may behave differently**

## Availability

- iOS 8.0+
- macOS 10.12+
- tvOS 10.1+
- watchOS 2.0+
