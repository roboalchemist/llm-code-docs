# HMHomeManager Class Reference

## Overview

HMHomeManager manages all homes and their accessories in the HomeKit database. It's the entry point for all HomeKit functionality.

```swift
class HMHomeManager: NSObject
```

## Authorization

### authorizationStatus() -> HMHomeManagerAuthorizationStatus

Returns the current HomeKit authorization status for the app.

```swift
let status = HMHomeManager.authorizationStatus()
```

Possible statuses:
- `.notDetermined` - User hasn't decided
- `.restricted` - App is restricted from HomeKit access
- `.denied` - User denied HomeKit access
- `.authorized` - HomeKit access is authorized

### requestAuthorization()

Requests HomeKit authorization from the user. The system automatically shows the permission prompt.

## Home Management

### homes: [HMHome]

Array of all homes configured by the user.

```swift
let allHomes = homeManager.homes
```

### primaryHome: HMHome?

The primary home set by the user.

```swift
if let primary = homeManager.primaryHome {
    // Use primary home
}
```

### addHome(withName name: String) -> HMHome

Adds a new home to the user's HomeKit database.

```swift
do {
    let newHome = try await homeManager.addHome(withName: "Vacation Home")
    print("Created home: \(newHome.name)")
} catch {
    print("Failed to add home: \(error)")
}
```

### removeHome(_ home: HMHome)

Removes a home and all its accessories from HomeKit.

```swift
do {
    try await homeManager.removeHome(home)
} catch {
    print("Failed to remove home: \(error)")
}
```

### updatePrimaryHome(_ home: HMHome)

Sets the primary home.

```swift
do {
    try await homeManager.updatePrimaryHome(home)
} catch {
    print("Failed to update primary home: \(error)")
}
```

## Observing Changes

### homeManagerDidUpdateHomes Notification

Posted when the homes array changes.

```swift
NotificationCenter.default.addObserver(
    forName: HMHomeManagerDidUpdateHomesNotification,
    object: homeManager,
    queue: .main
) { _ in
    // Homes were added or removed
}
```

### homeManagerDidUpdatePrimaryHome Notification

Posted when the primary home changes.

```swift
NotificationCenter.default.addObserver(
    forName: HMHomeManagerDidUpdatePrimaryHomeNotification,
    object: homeManager,
    queue: .main
) { _ in
    // Primary home was updated
}
```

### homeManagerDidUpdateAuthorizationStatus Notification

Posted when authorization status changes.

```swift
NotificationCenter.default.addObserver(
    forName: HMHomeManagerDidUpdateAuthorizationStatusNotification,
    object: homeManager,
    queue: .main
) { _ in
    // Authorization status changed
}
```

### homeManagerDidUpdateWhiteList Notification

Posted when the whitelist changes (tvOS only).

## Delegate Methods

Implement HMHomeManagerDelegate for callbacks:

```swift
class MyDelegate: HMHomeManagerDelegate {
    func homeManager(_ manager: HMHomeManager, didAdd home: HMHome) {
        print("Home added: \(home.name)")
    }

    func homeManager(_ manager: HMHomeManager, didRemove home: HMHome) {
        print("Home removed: \(home.name)")
    }

    func homeManager(_ manager: HMHomeManager, didUpdatePrimaryHome home: HMHome) {
        print("Primary home: \(home.name)")
    }

    func homeManagerDidUpdateAuthorizationStatus(_ manager: HMHomeManager) {
        let status = HMHomeManager.authorizationStatus()
        print("Authorization: \(status)")
    }
}
```

## Usage Example

```swift
import HomeKit

class HomeKitManager: NSObject, HMHomeManagerDelegate {
    let homeManager = HMHomeManager()

    override init() {
        super.init()
        homeManager.delegate = self
    }

    func setupHomeKit() {
        let status = HMHomeManager.authorizationStatus()

        switch status {
        case .authorized:
            setupUI(withHomes: homeManager.homes)
        case .notDetermined:
            // User will be prompted on next HomeKit access
            setupUI(withHomes: homeManager.homes)
        case .denied, .restricted:
            showAuthorizationError()
        @unknown default:
            break
        }
    }

    func createHome(named name: String) async {
        do {
            let home = try await homeManager.addHome(withName: name)
            print("Home created: \(home.name)")
        } catch {
            print("Failed to create home: \(error)")
        }
    }

    // MARK: - HMHomeManagerDelegate

    func homeManager(_ manager: HMHomeManager, didAdd home: HMHome) {
        print("New home available: \(home.name)")
        updateUI()
    }

    func homeManager(_ manager: HMHomeManager, didRemove home: HMHome) {
        print("Home removed: \(home.name)")
        updateUI()
    }

    func homeManagerDidUpdateAuthorizationStatus(_ manager: HMHomeManager) {
        print("Authorization status changed")
        setupHomeKit()
    }

    // ... other delegate methods
}
```

## Thread Safety

HMHomeManager must be accessed from the main thread. All delegate callbacks are invoked on the main thread.

## Availability

- iOS 8.0+
- macOS 10.12+
- tvOS 10.1+
- watchOS 2.0+

