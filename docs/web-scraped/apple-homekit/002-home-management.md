# HomeKit: Home Management

Classes for managing homes, rooms, zones, and user access.

## Class: HMHomeManager

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMHomeManager
```


HomeKit stores the user’s home automation information in a database that’s shared among Apple’s built-in iOS Home app, your HomeKit-enabled app, and apps from other developers. All these apps access the database as peers using the HomeKit framework.

[Image: media-3111423]

Each app creates a single `HMHomeManager` instance to coordinate its HomeKit-related activities. The manager’s `homes` array gives your app access to a collection of `HMHome` instances that represent the user’s homes. These in turn contain references to the home automation accessories that your app can inspect and control.

[Image: media-3111594]

Adopt the `HMHomeManagerDelegate` protocol in your app to stay informed of any changes to the set of homes made outside your app.

The manager for a collection of one or more of a user’s homes.

### Inspecting authorization status

#### `var authorizationStatus: HMHomeManagerAuthorizationStatus`

The current state of the app’s access to home data.


#### `struct HMHomeManagerAuthorizationStatus`

The possible home-access states.


### Working with the home layout

#### `var homes: [HMHome]`

An array of all homes managed by this home manager.


#### `class HMHome`

The primary unit of living space, typically composed of rooms organized into zones.


### Keeping track of connected homes

#### `var delegate: (any HMHomeManagerDelegate)?`

A delegate that receives updates on the collection of homes.


#### `protocol HMHomeManagerDelegate`

An interface the home manager uses to communicate changes to the state of the home network.


### Adding and removing homes (HMHomeManager)

#### `func addHome(withName: String, completionHandler: (HMHome?, (any Error)?) -> Void)`

Adds a new home to this home manager.


#### `func removeHome(HMHome, completionHandler: ((any Error)?) -> Void)`

Removes a home from this home manager.


### Managing the primary home

#### `var primaryHome: HMHome?` **(Deprecated)**

The primary home managed by this home manager.


#### `func updatePrimaryHome(HMHome, completionHandler: ((any Error)?) -> Void)` **(Deprecated)**

Updates the primary home of this home manager.


### Initializers

#### `init()`


### Instance Methods

#### `func findVendorAccessory(hapPublicKey: Data, completionHandler: (HMAccessory?, (any Error)?) -> Void)`


### Relationships (HMHomeManager)

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

### See Also: Home Manager

- **Configuring a home automation device**: Give users a familiar experience when they manage HomeKit accessories.
- **Testing your app with the HomeKit Accessory Simulator**: Install the HomeKit Accessory Simulator to help you debug your HomeKit-enabled app.

---

## Class: HMHome

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMHome
```


An `HMHome` instance is a top-level container in HomeKit representing a structure that a user considers as a single home. Users might have multiple homes that are far apart, like a primary home and a vacation home. Or they might have two homes that are close together, but that they consider as distinct units—for example, a main home and a guest cottage on the same property.

An `HMHome` instance:

- Is the main access point for communicating with and configuring accessories, like a garage door opener or a thermostat.
- Organizes accessories into a number of rooms, which are themselves optionally grouped into zones, such as the upstairs.
- Allows the user to define sets of actions that can be performed with a single operation, and triggers that cause an action set to be performed at a specific time.

You create a new home only in response to a specific user request, but you don’t do it directly. When the user asks your app to create a new home—for example, by tapping an Add button in your interface—your app calls the home manager’s `addHome(withName:completionHandler:)` method with a name that the user supplies. To get a list of existing home instances, use the `homes` array of the home manager (an instance of `HMHomeManager`).

Because HomeKit gives your app access to a shared database of home automation information, other apps can change the home’s configuration. Adopt the `HMHomeDelegate` protocol in your app to stay informed of any such changes that happen outside your app.

The primary unit of living space, typically composed of rooms organized into zones.

### Keeping track of home configuration changes

#### `var delegate: (any HMHomeDelegate)?`

A delegate that receives updates on the state of the home.


#### `protocol HMHomeDelegate`

An interface that communicates changes to a home’s configuration.


### Identifying a home

#### `var name: String` (HMHome)

The name the user gives to the home.


#### `func updateName(String, completionHandler: ((any Error)?) -> Void)` (HMHome)

Updates the name of the home.


#### `var uniqueIdentifier: UUID` (HMHome)

A unique identifier for the home.


#### `var isPrimary: Bool`

A Boolean value that indicates whether this is the primary home for its home manager.


### Dividing a house into rooms

#### `var rooms: [HMRoom]` (HMHome)

An array of the rooms created and managed by the user.


#### `func roomForEntireHome() -> HMRoom`

A room that represents all parts of the home that don’t have a more specific room to represent them.


#### `func addRoom(withName: String, completionHandler: (HMRoom?, (any Error)?) -> Void)`

Creates a new room with the specified name.


#### `func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)` (HMHome)

Removes a room from the home.


#### `class HMRoom`

The smallest subdivision of a home’s space.


### Grouping rooms into zones

#### `var zones: [HMZone]`

An array of all the zones in the home.


#### `func addZone(withName: String, completionHandler: (HMZone?, (any Error)?) -> Void)`

Adds a new zone to the home.


#### `func removeZone(HMZone, completionHandler: ((any Error)?) -> Void)`

Removes a zone from the home.


#### `class HMZone`

A collection of rooms that users think of as a single area, like upstairs or downstairs.


### Managing accessories

#### `var accessories: [HMAccessory]` (HMHome)

The collection of accessories that are part of the home.


#### `func addAndSetupAccessories(completionHandler: ((any Error)?) -> Void)` **(Deprecated)**

Finds and adds nearby accessories to the home.


#### `func addAndSetupAccessories(with: HMAccessorySetupPayload, completionHandler: ([HMAccessory]?, (any Error)?) -> Void)` **(Deprecated)**

Finds and adds nearby accessories to the home using a HomeKit code provided by your app.


#### `func addAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)`

Adds a new accessory to the home.


#### `func assignAccessory(HMAccessory, to: HMRoom, completionHandler: ((any Error)?) -> Void)`

Assigns an accessory to a different room.


#### `func removeAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)`

Removes an accessory from the home.


#### `var supportsAddingNetworkRouter: Bool`

A Boolean that indicates whether a home supports all of the requirements for adding a network router.


#### `func unblockAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)`

Unblocks a blocked accessory.


#### `class HMAccessory`

A home automation accessory, like a garage door opener or a thermostat.


### Grouping services

#### `func servicesWithTypes([String]) -> [HMService]?`

Returns an array of all services provided by accessories in the home that match the specified types.


#### `var serviceGroups: [HMServiceGroup]`

An array of all service groups in the home.


#### `func addServiceGroup(withName: String, completionHandler: (HMServiceGroup?, (any Error)?) -> Void)`

Adds a service group to the home.


#### `func removeServiceGroup(HMServiceGroup, completionHandler: ((any Error)?) -> Void)`

Removes a service group from the home.


#### `class HMServiceGroup`

A collection of accessory services.


### Querying the state of a home hub

#### `var homeHubState: HMHomeHubState`

The state of the home hub.


#### `enum HMHomeHubState` (HMHome)

The possible states of the home hub.


### Creating action sets

#### `var actionSets: [HMActionSet]`

An array of the action sets in the home.


#### `func addActionSet(withName: String, completionHandler: (HMActionSet?, (any Error)?) -> Void)`

Adds a new action set to the home.


#### `func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)`

Removes an action set from the home.


#### `func executeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)`

Executes all the actions in a specified action set.


#### `func builtinActionSet(ofType: String) -> HMActionSet?`

Retrieves the builtin action set for the specified type.


#### `class HMActionSet`

A collection of actions that you trigger as a group.


### Triggering an action set

#### `var triggers: [HMTrigger]`

An array of triggers defined in the home.


#### `func addTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)`

Adds a trigger to the home.


#### `func removeTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)`

Removes a trigger from the home.


#### `class HMTimerTrigger`

A trigger to activate an action set based on a periodic timer.


#### `class HMEventTrigger`

A trigger to activate an action set based on a set of events and optional conditions.


#### `class HMTrigger`

An abstract base class for triggering actions based on a set of conditions.


### Managing users

#### `func manageUsers(completionHandler: ((any Error)?) -> Void)`

Presents a view controller to manage users of the home.


#### `var currentUser: HMUser`

The current HomeKit user.


#### `class HMUser`

A person in the home who may have access to control accessories and services in the home.


### Controlling user access

#### `func homeAccessControl(for: HMUser) -> HMHomeAccessControl`

Retrieves the access level of a user associated with the home.


#### `class HMHomeAccessControl`

The access privileges of a user associated with a home.


#### `class HMAccessControl`

An abstract superclass for accessing user privileges.


#### `let HMUserFailedAccessoriesKey: String`

The key for retrieving details of what accessories failed to add or remove a user.


### Deprecated symbols

#### `var users: [HMUser]` **(Deprecated)**

All users associated with the home.


#### `func addUser(completionHandler: (HMUser?, (any Error)?) -> Void)` **(Deprecated)**

Adds a user to the home.


#### `func removeUser(HMUser, completionHandler: ((any Error)?) -> Void)` **(Deprecated)**

Removes a user from the home.


### Instance Properties

#### `var matterControllerID: String`


#### `var matterControllerXPCConnectBlock: () -> NSXPCConnection`


#### `var matterStartupParametersXPCConnectBlock: () -> NSXPCConnection`


### Relationships (HMHome)

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

### See Also: Working with the home layout

- **homes**: An array of all homes managed by this home manager.

---

## Class: HMRoom

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMRoom
```


An `HMRoom` instance is a part of a home representing an individual room in the home. Rooms don’t have any physical characteristics like size or location. Instead, they’re names that are meaningful to the user, like “living room” or “kitchen”. Meaningful room names enable voice commands like “Siri, turn on the kitchen lights.”

You create new rooms using the `addRoom(withName:completionHandler:)` method of `HMHome`. You can also group rooms into zones using instances of `HMZone`. You can assign accessories to rooms, indicating the presence of that accessory in that room.

The smallest subdivision of a home’s space.

### Identifying a room

#### `var name: String` (HMRoom)

The name of the room.


#### `func updateName(String, completionHandler: ((any Error)?) -> Void)` (HMRoom)

Updates the name of the room.


#### `var uniqueIdentifier: UUID` (HMRoom)

The unique identifier for a room.


### Finding accessories

#### `var accessories: [HMAccessory]` (HMRoom)

The collection of accessories in the room.


### Relationships (HMRoom)

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

### See Also: Locating an accessory

- **room**: The room containing the accessory.

---

## Class: HMZone

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMZone
```


An `HMZone` instance is an optional grouping of rooms in a home, with names like “upstairs” and “downstairs”. Zones are optional—rooms don’t need to be in a zone. By adding rooms to a zone, the user can give commands to Siri like “Siri, turn on all of the lights downstairs.” A single room can be in multiple zones—for example, “kitchen” might be in both the “downstairs” and “entertainment area” zones.

You create new zones using the `addZone(withName:completionHandler:)` method of `HMHome`. A zone can’t span homes—that is, you can’t create a zone that includes rooms from more than one home.

A collection of rooms that users think of as a single area, like upstairs or downstairs.

### Identifying a Zone

#### `var name: String` (HMZone)

The name of the zone.


#### `func updateName(String, completionHandler: ((any Error)?) -> Void)` (HMZone)

Updates the name of the zone.


#### `var uniqueIdentifier: UUID` (HMZone)

The unique identifier for a zone.


### Assigning Rooms to a Zone

#### `var rooms: [HMRoom]` (HMZone)

Array of rooms in the zone.


#### `func addRoom(HMRoom, completionHandler: ((any Error)?) -> Void)`

Adds a room to the zone.


#### `func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)` (HMZone)

Removes a room from the zone.


### Relationships (HMZone)

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

### See Also: Grouping rooms into zones

- **zones**: An array of all the zones in the home.
- **addZone(withName:completionHandler:)**: Adds a new zone to the home.
- **removeZone(_:completionHandler:)**: Removes a zone from the home.

---

## Class: HMUser

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMUser
```

A person in the home who may have access to control accessories and services in the home.

### Getting Information About the User

#### `var name: String` (HMUser)

The name of the user.


#### `var uniqueIdentifier: UUID` (HMUser)

A unique identifier for the user.


### Relationships (HMUser)

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

### See Also: Managing users

- **manageUsers(completionHandler:)**: Presents a view controller to manage users of the home.
- **currentUser**: The current HomeKit user.

---

## Class: HMAccessControl

**Availability:** iOS 11.2+, iPadOS 11.2+, Mac Catalyst 11.2+, tvOS 11.2+, visionOS 1.0+, watchOS 4.2+

```swift
class HMAccessControl
```


Use a concrete subclass, like `HMHomeAccessControl`, instead.

An abstract superclass for accessing user privileges.

### Relationships (HMAccessControl)

**Inherits From:**

- `NSObject`

**Inherited By:**

- `HMHomeAccessControl`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Controlling user access

- **homeAccessControl(for:)**: Retrieves the access level of a user associated with the home.
- **HMHomeAccessControl**: The access privileges of a user associated with a home.
- **HMUserFailedAccessoriesKey**: The key for retrieving details of what accessories failed to add or remove a user.

---

## Protocol: HMHomeDelegate

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
protocol HMHomeDelegate : NSObjectProtocol
```


Adopt this protocol to find out about changes made outside your app to a particular home, like when the home’s name changes, or when a room is added.

Changes that your app initiates—even those made asynchronously followed by a call to a completion handler—generate delegate callbacks in other apps, but not in your own. As a result, your app must update its internal data store or user interface from both the completion handler of an asynchronous call, and the delegate callback that corresponds to the same kind of change made by another app.

To be alerted about changes made to the overall list of homes, adopt the `HMHomeManagerDelegate` protocol. To find out about changes made to specific accessories, adopt the `HMAccessoryDelegate` protocol.

An interface that communicates changes to a home’s configuration.

### Observing Home Configuration

#### `func homeDidUpdateName(HMHome)`

Tells the delegate that a home’s name changed.


#### `func home(HMHome, didAdd: HMAccessory)`

Tells the delegate that a home added a new accessory.


#### `func home(HMHome, didUpdate: HMRoom, for: HMAccessory)`

Tells the delegate that a home assigned an accessory to a different room.


#### `func home(HMHome, didRemove: HMAccessory)`

Tells the delegate that a home removed an accessory.


#### `func home(HMHome, didAdd: HMRoom)`

Tells the delegate that a home added a new room.


#### `func home(HMHome, didUpdateNameFor: HMRoom)`

Tells the delegate that a home updated the name of one of its rooms.


#### `func home(HMHome, didAdd: HMRoom, to: HMZone)`

Tells the delegate that a home added a room to a zone.


#### `func home(HMHome, didRemove: HMRoom, from: HMZone)`

Tells the delegate that a home removed a room from a zone.


#### `func home(HMHome, didRemove: HMRoom)`

Tells the delegate that a home removed a room.


#### `func home(HMHome, didAdd: HMZone)`

Tells the delegate that a home added a new zone.


#### `func home(HMHome, didUpdateNameFor: HMZone)`

Tells the delegate that a home changed the name of a zone.


#### `func home(HMHome, didRemove: HMZone)`

Tells the delegate that a home removed a zone.


#### `func home(HMHome, didAdd: HMUser)`

Tells the delegate that a home added a user.


#### `func home(HMHome, didRemove: HMUser)`

Tells the delegate that a home removed a user.


#### `func homeDidUpdateAccessControl(forCurrentUser: HMHome)`

Tells the delegate that the access control for the current user has changed.


#### `func home(HMHome, didUpdate: HMHomeHubState)`

Tells the delegate that the state of the home hub has changed.


#### `func homeDidUpdateSupportedFeatures(HMHome)`

Tells the delegate that the home’s supported features changed.


#### `enum HMHomeHubState` (HMHomeDelegate)

The possible states of the home hub.


### Observing Service Configuration

#### `func home(HMHome, didAdd: HMServiceGroup)`

Tells the delegate that a home added a service group.


#### `func home(HMHome, didUpdateNameFor: HMServiceGroup)`

Tells the delegate that a home updated the name of a service group.


#### `func home(HMHome, didAdd: HMService, to: HMServiceGroup)`

Tells the delegate that a home added a service to a service group.


#### `func home(HMHome, didRemove: HMService, from: HMServiceGroup)`

Tells the delegate that a home removed a service from a service group.


#### `func home(HMHome, didRemove: HMServiceGroup)`

Tells the delegate that a home removed a service group.


### Observing Action and Trigger Configuration

#### `func home(HMHome, didAdd: HMActionSet)`

Tells the delegate that a home added an action set.


#### `func home(HMHome, didUpdateNameFor: HMActionSet)`

Tells the delegate that a home updated the name of an action set.


#### `func home(HMHome, didUpdateActionsFor: HMActionSet)`

Tells the delegate that a home updated the actions for an action set.


#### `func home(HMHome, didRemove: HMActionSet)`

Tells the delegate that a home removed an action set.


#### `func home(HMHome, didAdd: HMTrigger)`

Tells the delegate that a home added a trigger.


#### `func home(HMHome, didUpdateNameFor: HMTrigger)`

Tells the delegate that a home updated the name of a trigger.


#### `func home(HMHome, didUpdate: HMTrigger)`

Tells the delegate that a home updated a trigger.


#### `func home(HMHome, didRemove: HMTrigger)`

Tells the delegate that a home removed a trigger.


### Observing Accessories

#### `func home(HMHome, didEncounterError: any Error, for: HMAccessory)`

Tells the delegate that a configured accessory encountered an error.


#### `func home(HMHome, didUnblockAccessory: HMAccessory)`

Tells the delegate that an accessory has been unblocked.


### Relationships (HMHomeDelegate)

**Inherits From:**

- `NSObjectProtocol`

### See Also: Keeping track of home configuration changes

- **delegate**: A delegate that receives updates on the state of the home.

---

## Protocol: HMHomeManagerDelegate

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
protocol HMHomeManagerDelegate : NSObjectProtocol
```


Adopt this protocol to find out about changes made outside your app to the set of homes in the HomeKit database, like when homes are added or removed by another app. You also rely on this protocol when you first create an `HMHomeManager` instance. The home manager calls the `homeManagerDidUpdateHomes(_:)` method to indicate that it has finished its initial load of data from the HomeKit database.

Changes that your app initiates—even those made asynchronously followed by a call to a completion handler—generate delegate callbacks in other apps, but not in your own. As a result, your app must update its internal data store or user interface from both the completion handler of an asynchronous call, and the delegate callback that corresponds to the same kind of change made by another app.

To be alerted about changes made within a particular home, adopt the `HMHomeDelegate` protocol. To find out about changes made to specific accessories, adopt the `HMAccessoryDelegate` protocol.

An interface the home manager uses to communicate changes to the state of the home network.

### Adding and removing homes (HMHomeManagerDelegate)

#### `func homeManagerDidUpdateHomes(HMHomeManager)`

Tells the delegate that the home manager updated its collection of homes.


#### `func homeManager(HMHomeManager, didAdd: HMHome)`

Tells the delegate that the home manager added a home.


#### `func homeManager(HMHomeManager, didRemove: HMHome)`

Tells the delegate that the home manager removed a home.


#### `func homeManagerDidUpdatePrimaryHome(HMHomeManager)`

Tells the delegate that the home manager updated its primary home.


### Adding accessories

#### `func homeManager(HMHomeManager, didReceiveAddAccessoryRequest: HMAddAccessoryRequest)`

Tells the delegate to add an accessory to a home by using a setup payload.


#### `class HMAddAccessoryRequest`

A request to add an accessory to a particular home.


### Monitoring authorization status

#### `func homeManager(HMHomeManager, didUpdate: HMHomeManagerAuthorizationStatus)`

Tells the delegate when the authorization status changes.


### Relationships (HMHomeManagerDelegate)

**Inherits From:**

- `NSObjectProtocol`

### See Also: Keeping track of connected homes

- **delegate**: A delegate that receives updates on the collection of homes.

---

