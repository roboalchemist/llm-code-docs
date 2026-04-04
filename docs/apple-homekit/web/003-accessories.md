# HomeKit: Accessories

Classes for discovering, configuring, and managing home automation accessories.

## Class: HMAccessory

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMAccessory
```


An `HMAccessory` instance represents a physical device, like a garage door opener, installed in a home and assigned to a room.

You don’t create accessories directly. Instead you get them from the `accessories` array of an `HMHome` instance when you want all the accessories in a home, or the `accessories` array of an `HMRoom` instance when you want all the accessories in a particular room. Each physical accessory in the home is represented by exactly one accessory instance, so that one instance appears in both a home and a room collection. This is because it’s simultaneously part of the home and in one of the home’s rooms.

When you want to add new accessories, you call the home’s `addAndSetupAccessories(completionHandler:)` method. In response, HomeKit presents the user with an interface that steps through the process of searching for new accessories in the physical environment, naming them, and assigning them to a room.

Accessories provide one or more services, represented by instances of `HMService`, that are the features that the user can control, like the light attached to a garage door opener, or the door opener mechanism itself.

A home automation accessory, like a garage door opener or a thermostat.

### Tracking changes to an accessory

#### `var delegate: (any HMAccessoryDelegate)?`

A delegate that receives updates on the state of the accessory.


#### `protocol HMAccessoryDelegate`

A set of methods that defines the communication method for state updates from accessories to their delegates.


### Identifying an Accessory

#### `var name: String`

The name of the accessory.


#### `func updateName(String, completionHandler: ((any Error)?) -> Void)`

Changes the name of the accessory.


#### `var uniqueIdentifier: UUID` (HMAccessory)

A unique identifier for the accessory.


#### `var identifier: UUID` **(Deprecated)**

A unique identifier for the accessory.


### Categorizing an accessory

#### `var category: HMAccessoryCategory`

The category to which the accessory belongs.


#### `class HMAccessoryCategory`

A category for a HomeKit accessory.


### Locating an accessory

#### `var room: HMRoom?`

The room containing the accessory.


#### `class HMRoom`

The smallest subdivision of a home’s space.


### Managing accessory profiles

#### `var profiles: [HMAccessoryProfile]`

An array of profiles implemented by the accessory.


#### `class HMAccessoryProfile`

A profile that certain accessories implement.


#### `class HMNetworkConfigurationProfile`

A profile that provides information about network protection for an accessory.


#### `class HMCameraProfile` (HMAccessory)

A camera profile that interacts with an accessory’s camera.


### Managing camera profiles

#### `struct CameraView`

A SwiftUI view into which a video stream or an image snapshot is rendered.


#### `var cameraProfiles: [HMCameraProfile]?`

An array of camera profiles implemented by the accessory.


#### `class HMCameraProfile` (HMAccessory, Managing camera profiles)

A camera profile that interacts with an accessory’s camera.


#### `class HMCameraView`

The view into which a video stream or an image snapshot is rendered.


### Getting accessory state

#### `var isReachable: Bool`

A Boolean value indicating whether the accessory can be communicated with in the current network environment.


#### `var isBlocked: Bool`

A Boolean value indicating whether the accessory is blocked.


### Asking an accessory to identify itself

#### `var supportsIdentify: Bool`

A Boolean value that indicates whether the accessory supports the identify action.


#### `func identify(completionHandler: ((any Error)?) -> Void)`

Asks an accessory to identify itself.


### Controlling accessory features

#### `var services: [HMService]` (HMAccessory)

An array of services provided by the accessory.


#### `class HMService`

A controllable feature of an accessory, like a light attached to a garage door opener.


### Managing bridged accessories

#### `var isBridged: Bool`

A Boolean that indicates whether the accessory is accessed through a bridge.


#### `var uniqueIdentifiersForBridgedAccessories: [UUID]?`

An array of unique identifiers, each of which represents an accessory vended by the bridge.


#### `var identifiersForBridgedAccessories: [UUID]?` **(Deprecated)**

An array of identifiers for accessories available through a bridge.


### Getting manufacturer information

#### `var firmwareVersion: String?`

The firmware version of the accessory.


#### `var manufacturer: String?`

The manufacturer of the accessory.


#### `var model: String?`

The model name of the accessory.


### Browsing for accessories

#### `class HMAccessoryBrowser`

A network browser you can use to discover new accessories in a home.


### Instance Properties (HMAccessory)

#### `var matterNodeID: UInt64?`


#### `var bridgedAccessories: [HMAccessory]`


#### `var hapInstanceID: UInt64?`


#### `var home: HMHome?`


#### `var isVendorAccessory: Bool`


### Initializers (HMAccessory)

#### `init()` **(Deprecated)**


### Relationships (HMAccessory)

**Inherits From:**

- `NSObject`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Accessories (HMAccessory)

- **HMAccessorySetupManager**: An object that setups up new accessories.
- **HMAccessorySetupResult**: A result object describing information about a successful accessory setup request.
- **HMAccessorySetupRequest**: An object that describes how to add and setup up new accessories.
- **Interacting with a home automation network**: Find all the automation accessories in the primary home and control their state.
- **HMService**: A controllable feature of an accessory, like a light attached to a garage door opener.
- **HMCharacteristic**: A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- **HMMediaSourceDisplayOrderProfile**: An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

---

## Class: HMAccessoryBrowser

**Availability:** iOS 8.0+, iPadOS 8.0+, visionOS 1.0+

```swift
class HMAccessoryBrowser
```


Discovering new network accessories is an expensive operation in terms of time and power. Only start searching for new accessories when the user explicitly asks to do so, and stop searching as soon as the user has chosen the new accessories to add to their home.

> **Important:** To enable a consistent user experience across HomeKit enabled apps, use either the `addAndSetupAccessories(completionHandler:)` or the `addAndSetupAccessories(with:completionHandler:)` method of the `HMHome` class instead of an accessory browser. These calls manage all the details of the accessory search process for you.

A network browser you can use to discover new accessories in a home.

### Discovering accessories

#### `var discoveredAccessories: [HMAccessory]`

An array of accessories discovered during a search.


#### `func startSearchingForNewAccessories()`

Starts searching for accessories not yet associated with a home.


#### `func stopSearchingForNewAccessories()`

Stops searching for new accessories.


### Tracking the addition or removal of accessories

#### `var delegate: (any HMAccessoryBrowserDelegate)?`

A delegate that receives updates on the discovered accessories.


#### `protocol HMAccessoryBrowserDelegate`

An interface used to notify an accessory browser delegate of new accessories.


### Initializers (HMAccessoryBrowser)

#### `init()` (HMAccessoryBrowser)


### Relationships (HMAccessoryBrowser)

**Inherits From:**

- `NSObject`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

---

## Class: HMAccessoryCategory

**Availability:** iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMAccessoryCategory
```


A category represents a class of devices, like light bulbs or outlets. You can use a category to help users identify the types of accessories they’re browsing. For example, when adding a lamp and a fan to a home, users might not be able to distinguish these accessories if you display only the manufacturer name and model number for each accessory. To improve the user experience, you can use the category information associated with each accessory to help the user understand which accessory is the lamp and which is the fan.

A category for a HomeKit accessory.

### Reading the category type

#### `var categoryType: String`

The category to which this accessory belongs.


#### Accessory Category Types

The accessory category types supported by HomeKit.


### Describing the category

#### `var localizedDescription: String`

A localized description of the category.


### Relationships (HMAccessoryCategory)

**Inherits From:**

- `NSObject`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Categorizing an accessory

- **category**: The category to which the accessory belongs.

---

## Class: HMAccessoryProfile

**Availability:** iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+

```swift
class HMAccessoryProfile
```


This is an abstract superclass for classes such as `HMCameraProfile` and `HMNetworkConfigurationProfile`. Each profile subclass controls specific features for a specific set of accessories.

A profile that certain accessories implement.

### Getting information about a profile

#### `var accessory: HMAccessory?`

The accessory that implements this profile.


#### `var services: [HMService]` (HMAccessoryProfile)

An array of services that represents this profile.


#### `var uniqueIdentifier: UUID` (HMAccessoryProfile)

A unique identifier for the profile.


### Relationships (HMAccessoryProfile)

**Inherits From:**

- `NSObject`

**Inherited By:**

- `HMCameraProfile`
- `HMMediaSourceDisplayOrderProfile`
- `HMNetworkConfigurationProfile`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Managing accessory profiles (HMAccessoryProfile)

- **profiles**: An array of profiles implemented by the accessory.
- **HMNetworkConfigurationProfile**: A profile that provides information about network protection for an accessory.
- **HMCameraProfile**: A camera profile that interacts with an accessory’s camera.

---

## Class: HMAccessorySetupManager

**Availability:** iOS 15.0+, iPadOS 15.0+

```swift
class HMAccessorySetupManager
```


Use this class to provides steps for the user to add one or more accessories to a particular home, and follow up with additional setup. These APIs don’t require that the current app has home data authorization.

An object that setups up new accessories.

### Adding accessories

#### `func performAccessorySetup(using: HMAccessorySetupRequest, completionHandler: (HMAccessorySetupResult?, (any Error)?) -> Void)`

Performs the process of setting up accessories with Apple Home.


### Initializers (HMAccessorySetupManager)

#### `init()` (HMAccessorySetupManager)


### Relationships (HMAccessorySetupManager)

**Inherits From:**

- `NSObject`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Accessories (HMAccessorySetupManager)

- **HMAccessorySetupResult**: A result object describing information about a successful accessory setup request.
- **HMAccessorySetupRequest**: An object that describes how to add and setup up new accessories.
- **Interacting with a home automation network**: Find all the automation accessories in the primary home and control their state.
- **HMAccessory**: A home automation accessory, like a garage door opener or a thermostat.
- **HMService**: A controllable feature of an accessory, like a light attached to a garage door opener.
- **HMCharacteristic**: A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- **HMMediaSourceDisplayOrderProfile**: An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

---

## Class: HMAccessorySetupPayload

**Availability:** iOS 11.3+, iPadOS 11.3+, visionOS 1.0+

```swift
class HMAccessorySetupPayload
```


The setup payload provides a URL to authenticate an accessory. Typically, the URL comes from scanning a QR code on the accessory. Use a setup payload to authenticate devices that are already deployed, for which scanning a QR code would be difficult, or if you need to provide an optional ownership token that you negotiate with the accessory outside of HomeKit.

For details about the payload’s content, please join the ``.

A payload for authenticating a HomeKit accessory.

### Creating a Payload

#### `init?(url: URL?)`

Creates an accessory setup payload.


#### `init?(url: URL, ownershipToken: HMAccessoryOwnershipToken?)`

Creates an accessory setup payload instance that includes an ownership token.


#### `class HMAccessoryOwnershipToken`

Authentication data that your app provides when adding an accessory to a home.


### Relationships (HMAccessorySetupPayload)

**Inherits From:**

- `NSObject`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

---

## Class: HMAccessorySetupRequest

**Availability:** iOS 15.4+, iPadOS 15.4+

```swift
class HMAccessorySetupRequest
```


Use this class to provide steps for the user to add one or more accessories to a particular home, and follow up with additional setup.

An object that describes how to add and setup up new accessories.

### Setting up accessorices

#### `var homeUniqueIdentifier: UUID?`

The identifier corresponding to the home that the accessory should be added to when being set up.


#### `var payload: HMAccessorySetupPayload?`

The payload to use for accessory setup.


#### `var suggestedAccessoryName: String?`

The name that the framework suggests when the user names the accessory being set up.


#### `var suggestedRoomUniqueIdentifier: UUID?`

The identifier corresponding to the room that the framework suggests.


### Instance Properties (HMAccessorySetupRequest)

#### `var matterPayload: MTRSetupPayload?`


### Initializers (HMAccessorySetupRequest)

#### `init()` (HMAccessorySetupRequest)


### Relationships (HMAccessorySetupRequest)

**Inherits From:**

- `NSObject`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCopying`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Accessories (HMAccessorySetupRequest)

- **HMAccessorySetupManager**: An object that setups up new accessories.
- **HMAccessorySetupResult**: A result object describing information about a successful accessory setup request.
- **Interacting with a home automation network**: Find all the automation accessories in the primary home and control their state.
- **HMAccessory**: A home automation accessory, like a garage door opener or a thermostat.
- **HMService**: A controllable feature of an accessory, like a light attached to a garage door opener.
- **HMCharacteristic**: A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- **HMMediaSourceDisplayOrderProfile**: An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

---

## Class: HMAccessorySetupResult

**Availability:** iOS 15.4+, iPadOS 15.4+

```swift
class HMAccessorySetupResult
```

A result object describing information about a successful accessory setup request.

### Getting results

#### `var accessoryUniqueIdentifiers: [UUID]`

The values corresponding to accessories that are set up.


#### `var homeUniqueIdentifier: UUID`

The home that accessories were added to.


### Relationships (HMAccessorySetupResult)

**Inherits From:**

- `NSObject`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCopying`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Accessories (HMAccessorySetupResult)

- **HMAccessorySetupManager**: An object that setups up new accessories.
- **HMAccessorySetupRequest**: An object that describes how to add and setup up new accessories.
- **Interacting with a home automation network**: Find all the automation accessories in the primary home and control their state.
- **HMAccessory**: A home automation accessory, like a garage door opener or a thermostat.
- **HMService**: A controllable feature of an accessory, like a light attached to a garage door opener.
- **HMCharacteristic**: A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- **HMMediaSourceDisplayOrderProfile**: An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

---

## Class: HMMediaSourceDisplayOrderProfile

**Availability:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

```swift
@objc class HMMediaSourceDisplayOrderProfile
```


This class represents a media source display that orders functionality for the `HMServiceTypeTelevision` service contained in the services array of the profile.

An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

### Managing input source order

#### `func writeOrder([Int]) async throws`

Writes the display order of the media sources to the accessory.


#### `var delegate: (any HMMediaSourceDisplayOrderProfile.Delegate)?`

The property that handles updates to the display order.


#### `var order: [Int]`

The display order of input media sources.


#### `let canModifyOrder: Bool`

A Boolean that indicates if the display order of the input media sources can be modified.


#### `protocol Delegate`

The protocol through which a delegate receives updates on the order of input media sources.


### Relationships (HMMediaSourceDisplayOrderProfile)

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

### See Also: Accessories (HMMediaSourceDisplayOrderProfile)

- **HMAccessorySetupManager**: An object that setups up new accessories.
- **HMAccessorySetupResult**: A result object describing information about a successful accessory setup request.
- **HMAccessorySetupRequest**: An object that describes how to add and setup up new accessories.
- **Interacting with a home automation network**: Find all the automation accessories in the primary home and control their state.
- **HMAccessory**: A home automation accessory, like a garage door opener or a thermostat.
- **HMService**: A controllable feature of an accessory, like a light attached to a garage door opener.
- **HMCharacteristic**: A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.

---

## Class: HMNetworkConfigurationProfile

**Availability:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

```swift
class HMNetworkConfigurationProfile
```


To increase security, HomeKit can restrict network access for specific accessories, including access to other accessories in the home, and to the internet. However, an accessory your app controls might need network access to carry out certain functions, like downloading new firmware.

Check the `isNetworkAccessRestricted` property of an accessory’s network configuration profile to find out if an accessory has restricted access. You can use this information to ask the user to relax network restrictions in the Home app.

A profile that provides information about network protection for an accessory.

### Restricting network access

#### `var isNetworkAccessRestricted: Bool`

An indication of whether the accessory’s access to the network is restricted.


### Listening for access changes

#### `var delegate: (any HMNetworkConfigurationProfileDelegate)?`

A delegate that HomeKit tells about changes in the state of network access.


#### `protocol HMNetworkConfigurationProfileDelegate`

An interface that your app adopts to receive notifications about changes in the state of network access.


### Relationships (HMNetworkConfigurationProfile)

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

### See Also: Managing accessory profiles (HMNetworkConfigurationProfile)

- **profiles**: An array of profiles implemented by the accessory.
- **HMAccessoryProfile**: A profile that certain accessories implement.
- **HMCameraProfile**: A camera profile that interacts with an accessory’s camera.

---

## Protocol: HMAccessoryDelegate

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
protocol HMAccessoryDelegate : NSObjectProtocol, Sendable
```


Adopt this protocol to find out about changes made outside your app to a specific accessory, like when the accessory’s name changes, or when a characteristic value changes.

> **Note:** To receive `accessory(_:service:didUpdateValueFor:)` method calls for a particular characteristic, indicating when the characteristic value changes, you must first call the characteristic’s `enableNotification(_:completionHandler:)` method.

Changes that your app initiates—even those made asynchronously followed by a call to a completion handler—generate delegate callbacks in other apps, but not in your own. As a result, your app must update its internal data store or user interface from both the completion handler of an asynchronous call, and the delegate callback that corresponds to the same kind of change made by another app.

To find out about changes made to the accessory’s home, adopt the `HMHomeDelegate` protocol. To be alerted about changes made to the overall list of homes, adopt the `HMHomeManagerDelegate` protocol.

A set of methods that defines the communication method for state updates from accessories to their delegates.

### Observing accessories

#### `func accessoryDidUpdateName(HMAccessory)`

Informs the delegate when the name of the accessory is updated.


#### `func accessoryDidUpdateReachability(HMAccessory)`

Informs the delegate when the reachability of the accessory changes.


#### `func accessoryDidUpdateServices(HMAccessory)`

Informs the delegate when the services on the accessory have been updated.


#### `func accessory(HMAccessory, didUpdateNameFor: HMService)`

Informs the delegate when the name of a service is updated.


#### `func accessory(HMAccessory, service: HMService, didUpdateValueFor: HMCharacteristic)`

Informs the delegate of a change in value of a characteristic.


#### `func accessory(HMAccessory, didUpdateAssociatedServiceTypeFor: HMService)`

Informs the delegate when the associated service type of a service is modified.


#### `func accessory(HMAccessory, didAdd: HMAccessoryProfile)`

Informs the delegate when a profile is added to an accessory.


#### `func accessory(HMAccessory, didRemove: HMAccessoryProfile)`

Informs the delegate when a profile is removed from an accessory.


#### `func accessory(HMAccessory, didUpdateFirmwareVersion: String)`

Informs the delegate when firmwareVersion has been changed for an accessory.


### Relationships (HMAccessoryDelegate)

**Inherits From:**

- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Tracking changes to an accessory

- **delegate**: A delegate that receives updates on the state of the accessory.

---

## Protocol: HMAccessoryBrowserDelegate

**Availability:** iOS 8.0+, iPadOS 8.0+, visionOS 1.0+

```swift
protocol HMAccessoryBrowserDelegate : NSObjectProtocol
```


> **Important:** To enable a consistent user experience across HomeKit enabled apps, use either the `addAndSetupAccessories(completionHandler:)` or the `addAndSetupAccessories(with:completionHandler:)` method of the `HMHome` class instead of an accessory browser. These calls manage all the details of the accessory search process for you.

An interface used to notify an accessory browser delegate of new accessories.

### Tracking new accessories

#### `func accessoryBrowser(HMAccessoryBrowser, didFindNewAccessory: HMAccessory)`

Tells the delegate that a new accessory has been discovered.


#### `func accessoryBrowser(HMAccessoryBrowser, didRemoveNewAccessory: HMAccessory)`

Tells the delegate that a new accessory is no longer available in the browser.


### Relationships (HMAccessoryBrowserDelegate)

**Inherits From:**

- `NSObjectProtocol`

### See Also: Tracking the addition or removal of accessories

- **delegate**: A delegate that receives updates on the discovered accessories.

---

