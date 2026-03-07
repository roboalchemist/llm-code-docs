# HMHome Class Reference

## Overview

Represents a single home in the user's HomeKit database. Contains rooms, accessories, scenes, and automation rules.

```swift
class HMHome: NSObject
```

## Home Information

### name: String

The name of the home (e.g., "My House").

```swift
print("Home name: \(home.name)")
```

### updateName(_ name: String)

Updates the home's name.

```swift
do {
    try await home.updateName("Vacation Home")
} catch {
    print("Failed to update home name: \(error)")
}
```

### uniqueIdentifier: UUID

The unique identifier for this home.

```swift
let homeID = home.uniqueIdentifier
```

## Rooms

### rooms: [HMRoom]

Array of all rooms in the home.

```swift
for room in home.rooms {
    print("Room: \(room.name)")
}
```

### addRoom(withName name: String)

Adds a new room to the home.

```swift
do {
    let room = try await home.addRoom(withName: "Bedroom")
    print("Room created: \(room.name)")
} catch {
    print("Failed to add room: \(error)")
}
```

### removeRoom(_ room: HMRoom)

Removes a room from the home.

```swift
do {
    try await home.removeRoom(room)
} catch {
    print("Failed to remove room: \(error)")
}
```

## Accessories

### accessories: [HMAccessory]

Array of all accessories in the home.

```swift
for accessory in home.accessories {
    print("Accessory: \(accessory.name)")
}
```

### accessoriesWithServices(ofType: String) -> [HMAccessory]

Returns accessories that provide a specific service type.

```swift
let lights = home.accessoriesWithServices(ofType: HMServiceTypeLight)
```

### addAccessory(_ accessory: HMAccessory)

Adds an accessory to the home.

```swift
do {
    try await home.addAccessory(accessory)
} catch {
    print("Failed to add accessory: \(error)")
}
```

### removeAccessory(_ accessory: HMAccessory)

Removes an accessory from the home.

```swift
do {
    try await home.removeAccessory(accessory)
} catch {
    print("Failed to remove accessory: \(error)")
}
```

## Action Sets

### actionSets: [HMActionSet]

Array of all action sets in the home.

```swift
for actionSet in home.actionSets {
    print("Action Set: \(actionSet.name)")
}
```

### addActionSet(withName name: String)

Creates a new action set.

```swift
do {
    let actionSet = try await home.addActionSet(withName: "Movie Time")
    print("Action set created: \(actionSet.name)")
} catch {
    print("Failed to create action set: \(error)")
}
```

### removeActionSet(_ actionSet: HMActionSet)

Removes an action set from the home.

```swift
do {
    try await home.removeActionSet(actionSet)
} catch {
    print("Failed to remove action set: \(error)")
}
```

## Triggers

### triggers: [HMTrigger]

Array of all automation triggers in the home.

```swift
for trigger in home.triggers {
    print("Trigger: \(trigger.name)")
}
```

### addTrigger(_ trigger: HMTrigger)

Adds an automation trigger to the home.

```swift
let trigger = HMTimerTrigger(
    name: "Morning Routine",
    fireDate: Date(),
    recurrence: .daily
)

do {
    try await home.addTrigger(trigger)
    print("Trigger added: \(trigger.name)")
} catch {
    print("Failed to add trigger: \(error)")
}
```

### removeTrigger(_ trigger: HMTrigger)

Removes an automation trigger.

```swift
do {
    try await home.removeTrigger(trigger)
} catch {
    print("Failed to remove trigger: \(error)")
}
```

## Scenes

### scenes: [HMScene]

Array of all scenes in the home. Note: Scenes are a subset of action sets.

```swift
let scenes = home.scenes
```

### addScene(withName name: String)

Creates a new scene.

```swift
do {
    let scene = try await home.addScene(withName: "Good Night")
    print("Scene created: \(scene.name)")
} catch {
    print("Failed to create scene: \(error)")
}
```

## Zones

### zones: [HMZone]

Array of zones (logical groups of rooms).

```swift
for zone in home.zones {
    print("Zone: \(zone.name)")
}
```

### addZone(withName name: String)

Creates a new zone.

```swift
do {
    let zone = try await home.addZone(withName: "Downstairs")
} catch {
    print("Failed to create zone: \(error)")
}
```

## Users & Access Control

### users: [HMUser]

Array of users with access to this home.

```swift
for user in home.users {
    print("User: \(user.name)")
}
```

### addUser(withName name: String)

Invites a new user to access the home.

```swift
do {
    let user = try await home.addUser(withName: "John Doe")
} catch {
    print("Failed to add user: \(error)")
}
```

### removeUser(_ user: HMUser)

Removes a user's access to the home.

```swift
do {
    try await home.removeUser(user)
} catch {
    print("Failed to remove user: \(error)")
}
```

## Remote Access

### homeAccessoryServers: [HMHomeAccessoryServer]

HomeKit hubs and other accessory servers providing remote access.

## Observing Changes

Implement HMHomeDelegate:

```swift
protocol HMHomeDelegate {
    func homeDidUpdateName(_ home: HMHome)
    func home(_ home: HMHome, didAdd room: HMRoom)
    func home(_ home: HMHome, didRemove room: HMRoom)
    func home(_ home: HMHome, didAdd accessory: HMAccessory)
    func home(_ home: HMHome, didRemove accessory: HMAccessory)
    func home(_ home: HMHome, didAdd actionSet: HMActionSet)
    func home(_ home: HMHome, didRemove actionSet: HMActionSet)
    func home(_ home: HMHome, didAdd trigger: HMTrigger)
    func home(_ home: HMHome, didRemove trigger: HMTrigger)
    func home(_ home: HMHome, didAdd zone: HMZone)
    func home(_ home: HMHome, didRemove zone: HMZone)
    func home(_ home: HMHome, didAdd user: HMUser)
    func home(_ home: HMHome, didRemove user: HMUser)
}
```

## Example

```swift
class HomeViewController: UIViewController, HMHomeDelegate {
    let home: HMHome

    override func viewDidLoad() {
        super.viewDidLoad()
        home.delegate = self
        loadHomeData()
    }

    func loadHomeData() {
        title = home.name

        let lights = home.accessoriesWithServices(ofType: HMServiceTypeLight)
        let thermostats = home.accessoriesWithServices(ofType: HMServiceTypeThermostat)

        updateUI(lights: lights, thermostats: thermostats)
    }

    func home(_ home: HMHome, didAdd accessory: HMAccessory) {
        print("New accessory: \(accessory.name)")
        loadHomeData()
    }

    // ... other delegate methods
}
```

## Availability

- iOS 8.0+
- macOS 10.12+
- tvOS 10.1+
- watchOS 2.0+
