# Automation and Scenes

## Scenes

Scenes allow users to activate a group of accessories with specific states all at once.

### Creating a Scene

```swift
let home: HMHome = ...

do {
    let scene = try await home.addScene(withName: "Movie Time")
    print("Scene created: \(scene.name)")
} catch {
    print("Failed to create scene: \(error)")
}
```

### Adding Actions to Scenes

```swift
let scene: HMScene = ...
let lightAccessory: HMAccessory = ...

if let lightService = lightAccessory.services.first(where: { $0.serviceType == HMServiceTypeLight }) {
    if let powerChar = lightService.characteristics.first(where: { $0.characteristicType == HMCharacteristicTypePowerState }) {
        
        // Create action
        let action = HMCharacteristicWriteAction(
            characteristic: powerChar,
            targetValue: 0  // Turn off
        )
        
        do {
            try await scene.addAction(action)
        } catch {
            print("Failed to add action: \(error)")
        }
    }
}
```

### Executing Scenes

```swift
let scene: HMScene = ...

do {
    try await scene.executeActionSet(scene.actionSets.first!)
    print("Scene executed: \(scene.name)")
} catch {
    print("Failed to execute scene: \(error)")
}
```

### Scene Names and Siri Compatibility

Common scene names that Siri recognizes:

- "Good Morning"
- "Good Night"
- "Movie Time"
- "Reading Time"
- "Work"
- "Leaving Home"
- "Coming Home"

```swift
// Create a scene Siri can understand
let scene = try await home.addScene(withName: "Coming Home")

// Add lights that turn on
// Add thermostat that sets temperature
// Add music that plays
// ...
```

## Automation Rules (Triggers)

Automation allows accessories to respond automatically based on conditions or schedules.

### Timer Triggers

Execute actions at specific times:

```swift
// Create a daily trigger at 7:00 AM
let components = DateComponents(hour: 7, minute: 0)
let calendar = Calendar.current
let date = calendar.date(from: components) ?? Date()

let trigger = HMTimerTrigger(
    name: "Morning Routine",
    fireDate: date,
    recurrence: .daily
)

do {
    try await home.addTrigger(trigger)
    print("Trigger created: \(trigger.name)")
} catch {
    print("Failed to create trigger: \(error)")
}
```

### Timer Trigger Recurrence

```swift
// One-time trigger
let onceDate = Date().addingTimeInterval(3600)
let onceTrigger = HMTimerTrigger(
    name: "In One Hour",
    fireDate: onceDate,
    recurrence: nil
)

// Daily trigger
let dailyTrigger = HMTimerTrigger(
    name: "Every Day",
    fireDate: Date(),
    recurrence: .daily
)

// Weekly trigger
let weeklyTrigger = HMTimerTrigger(
    name: "Every Monday",
    fireDate: Date(),
    recurrence: .weekly
)
```

### Event-Based Triggers

Execute actions when sensors detect events:

```swift
let home: HMHome = ...
let motionSensor: HMAccessory = ...

if let motionService = motionSensor.services.first(where: { $0.serviceType == HMServiceTypeMotionSensor }) {
    if let motionChar = motionService.characteristics.first(where: { $0.characteristicType == HMCharacteristicTypeMotionDetected }) {
        
        // Create event for motion detection
        let event = HMEventCharacteristicHasValue(characteristic: motionChar, triggerValue: 1)
        
        // Create trigger that fires on this event
        let trigger = HMEventTrigger(
            name: "Motion Detected",
            events: [event],
            condition: nil
        )
        
        do {
            try await home.addTrigger(trigger)
        } catch {
            print("Failed to create event trigger: \(error)")
        }
    }
}
```

### Event Types

#### HMEventCharacteristicHasValue

Triggers when characteristic reaches specific value:

```swift
let event = HMEventCharacteristicHasValue(
    characteristic: contactSensor,
    triggerValue: 0  // Door opened
)
```

#### HMEventCharacteristicRangeValue

Triggers when characteristic is within range:

```swift
let event = HMEventCharacteristicRangeValue(
    characteristic: temperatureSensor,
    triggerValue: 20
)
// Triggers when temperature reaches 20°C
```

#### HMEventCharacteristicThresholdValue

Triggers based on threshold:

```swift
let event = HMEventCharacteristicThresholdValue(
    characteristic: temperatureSensor,
    triggerValue: 25
)
// Triggers when temperature exceeds 25°C
```

### Trigger Conditions

Add conditions to make triggers smarter:

```swift
// Condition: time of day
let morningCondition = HMConditionCharacteristicIsWithinTimeRange(
    characteristic: timeChar,
    startHour: 6,
    endHour: 9
)

// Trigger only in morning
let trigger = HMEventTrigger(
    name: "Morning Motion",
    events: [motionEvent],
    condition: morningCondition
)
```

### Trigger Actions

Define what happens when trigger fires:

```swift
let trigger: HMEventTrigger = ...
let actionSet: HMActionSet = ...

do {
    // Trigger will execute this action set
    try await trigger.addActionSet(actionSet)
} catch {
    print("Failed to add action set: \(error)")
}
```

## Action Sets

Action sets are groups of characteristic write actions:

```swift
let home: HMHome = ...

// Create action set
do {
    let actionSet = try await home.addActionSet(withName: "Bedtime")
    
    // Add actions
    // Light off
    // Thermostat to cool mode
    // Doors locked
    // ...
    
} catch {
    print("Failed to create action set: \(error)")
}
```

## Managing Automation

### Listing Triggers

```swift
let home: HMHome = ...

for trigger in home.triggers {
    print("Trigger: \(trigger.name)")
    
    if let timerTrigger = trigger as? HMTimerTrigger {
        print("  Type: Timer")
        print("  Fire Date: \(timerTrigger.fireDate)")
    } else if let eventTrigger = trigger as? HMEventTrigger {
        print("  Type: Event-based")
    }
}
```

### Updating Triggers

```swift
let trigger: HMTimerTrigger = ...

do {
    // Update fire time
    try await trigger.updateFireDate(Date().addingTimeInterval(3600))
    
    // Update recurrence
    try await trigger.updateRecurrence(.weekly)
    
} catch {
    print("Failed to update trigger: \(error)")
}
```

### Removing Triggers

```swift
let home: HMHome = ...
let trigger: HMTrigger = ...

do {
    try await home.removeTrigger(trigger)
} catch {
    print("Failed to remove trigger: \(error)")
}
```

## Best Practices

1. **Name scenes intuitively** - Users will say these names to Siri
2. **Test triggers thoroughly** - Especially time-based ones
3. **Use conditions to prevent unintended executions**
4. **Handle accessories that are offline gracefully**
5. **Let users control automation from UI**
6. **Monitor battery accessories in time-based triggers**

## Availability

- iOS 8.0+
- macOS 10.12+
- tvOS 10.1+
- watchOS 2.0+
