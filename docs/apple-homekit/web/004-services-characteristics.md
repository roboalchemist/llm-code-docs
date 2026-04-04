# HomeKit: Services and Characteristics

Classes for interacting with accessory services and their characteristics.

## Class: HMService

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMService
```


An `HMService` instance represents a service provided by an accessory. Accessories have both user-controllable services, like a light, and services that are for the use of the accessory itself, like a firmware update service.

You don’t create services directly. Instead you find them in the `services` array of an `HMAccessory` instance.

A single accessory may have more than one user-controllable service. For example, most garage door openers have a service for opening and closing the door, and another service for the light on the garage door opener. These services are what Apple’s Home app labels as “accessories”.

You inspect or change a service’s `HMCharacteristic` instances to discover state, or modify behavior.

A controllable feature of an accessory, like a light attached to a garage door opener.

### Getting service characteristics

#### `var characteristics: [HMCharacteristic]`

An array of characteristics for the service.


#### `class HMCharacteristic`

A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.


### Identifying the service

#### `var name: String` (HMService)

The user specified name of the service.


#### `func updateName(String, completionHandler: ((any Error)?) -> Void)` (HMService)

Updates the name of the service to the specified string.


#### `var uniqueIdentifier: UUID` (HMService)

A unique identifier for the service.


### Getting the service type

#### `var serviceType: String`

The type of the service.


#### Accessory Service Types

The service types supported by HomeKit.


#### `var localizedDescription: String` (HMService)

The localized description of the service.


### Reading service properties

#### `var isPrimaryService: Bool`

A Boolean value that indicates whether this service is the primary service on the accessory.


#### `var isUserInteractive: Bool`

A Boolean value that indicates whether this service supports user interaction.


### Associating a secondary service

#### `var associatedServiceType: String?`

The type of the service associated with an outlet or a switch.


#### `func updateAssociatedServiceType(String?, completionHandler: ((any Error)?) -> Void)`

Associates the service type of the plugged-in device with a switch or an outlet service.


### Finding the linked services

#### `var linkedServices: [HMService]?`

An array of service objects that represents all the services to which the service links.


### Getting the service’s provider

#### `var accessory: HMAccessory?`

The accessory that provides this service.


### Initializers (HMService)

#### `init()` **(Deprecated)** (HMService)


### Instance Properties

#### `var matterEndpointID: UInt16?`


### Relationships (HMService)

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

### See Also: Accessories (HMService)

- **HMAccessorySetupManager**: An object that setups up new accessories.
- **HMAccessorySetupResult**: A result object describing information about a successful accessory setup request.
- **HMAccessorySetupRequest**: An object that describes how to add and setup up new accessories.
- **Interacting with a home automation network**: Find all the automation accessories in the primary home and control their state.
- **HMAccessory**: A home automation accessory, like a garage door opener or a thermostat.
- **HMCharacteristic**: A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- **HMMediaSourceDisplayOrderProfile**: An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

---

## Class: HMServiceGroup

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMServiceGroup
```


A service group makes it easier to address the services as a single entity. For example, a user might choose to group a set of lights together as “Desk Lamps,” and have another set of lights grouped as “Ceiling Lights”. You create service groups using the `addServiceGroup(withName:completionHandler:)` method of `HMHome`. Service groups are visible to Siri and allow users to control a group of services through Siri.

A collection of accessory services.

### Managing Service Groups

#### `var name: String` (HMServiceGroup)

The name of the service group.


#### `var uniqueIdentifier: UUID` (HMServiceGroup)

The unique identifier for the service group.


#### `func updateName(String, completionHandler: ((any Error)?) -> Void)` (HMServiceGroup)

Updates the name of the service group.


#### `var services: [HMService]`

Array of the services in the service group.


#### `func addService(HMService, completionHandler: ((any Error)?) -> Void)`

Adds a new service to the service group.


#### `func removeService(HMService, completionHandler: ((any Error)?) -> Void)`

Removes a service from the service group.


### Relationships (HMServiceGroup)

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

### See Also: Grouping services

- **servicesWithTypes(_:)**: Returns an array of all services provided by accessories in the home that match the specified types.
- **serviceGroups**: An array of all service groups in the home.
- **addServiceGroup(withName:completionHandler:)**: Adds a service group to the home.
- **removeServiceGroup(_:completionHandler:)**: Removes a service group from the home.

---

## Class: HMCharacteristic

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMCharacteristic
```


An `HMCharacteristic` instance represents an aspect of a service that provides data, or that your app can control.

You don’t create characteristic instances. Instead, an accessory manufacturer incorporates them into a device, which publishes them to you through the `characteristics` array of an `HMService` instance.

Characteristics have a `properties` array that indicates attributes like readability, writability, and user-visibility. They also have a `characteristicType` property that tells your app what the characteristic controls or describes. Device manufacturers can use one of the standard types, given in `characteristic-types`, or they can create custom types.

Each characteristic has a `value` that you can read or write. Some characteristics use plain numbers, Booleans, or strings. Others have application specific meanings declared in enumerations associated with the given characteristic type. The characteristic’s `metadata` can help your app interpret the value.

A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.

### Identifying a characteristic

#### `var uniqueIdentifier: UUID` (HMCharacteristic)

A unique identifier for the characteristic.


#### `var localizedDescription: String` (HMCharacteristic)

The localized description of the characteristic.


### Reading characteristic properties

#### `var properties: [String]`

An array of properties that describe the characteristic.


#### Characteristic Properties

The properties that characteristics can have.


### Determining what a characteristic controls

#### `var characteristicType: String`

The type of the characteristic.


#### Characteristic types

The characteristic types supported by HomeKit-based accessories.


### Controlling a characteristic

#### `var value: Any?`

The current value of the characteristic.


#### `func readValue(completionHandler: ((any Error)?) -> Void)`

Reads the value for the characteristic.


#### `func writeValue(Any?, completionHandler: ((any Error)?) -> Void)`

Modifies the value of the characteristic.


#### `func updateAuthorizationData(Data?, completionHandler: ((any Error)?) -> Void)`

Sets or clears authorization data used when writing to the characteristic.


### Managing characteristic presentation

#### `var metadata: HMCharacteristicMetadata?`

Metadata about the units and other properties of the characteristic.


#### `class HMCharacteristicMetadata`

Metadata that describes a characteristic’s value and that may be useful for presentation purposes.


### Receiving change notifications

#### `func enableNotification(Bool, completionHandler: ((any Error)?) -> Void)`

Enables or disables notifications for changes in the value of the characteristic.


#### `var isNotificationEnabled: Bool`

A Boolean indicating whether the characteristic has been set to send notifications.


### Getting the characterized service

#### `var service: HMService?`

The service that contains this characteristic.


### Initializers (HMCharacteristic)

#### `init()` **(Deprecated)** (HMCharacteristic)


### Relationships (HMCharacteristic)

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

### See Also: Accessories (HMCharacteristic)

- **HMAccessorySetupManager**: An object that setups up new accessories.
- **HMAccessorySetupResult**: A result object describing information about a successful accessory setup request.
- **HMAccessorySetupRequest**: An object that describes how to add and setup up new accessories.
- **Interacting with a home automation network**: Find all the automation accessories in the primary home and control their state.
- **HMAccessory**: A home automation accessory, like a garage door opener or a thermostat.
- **HMService**: A controllable feature of an accessory, like a light attached to a garage door opener.
- **HMMediaSourceDisplayOrderProfile**: An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

---

## Class: HMCharacteristicMetadata

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMCharacteristicMetadata
```


Querying a characteristic’s metadata enables you to build a user interface that reflects the underlying units, minima, and maxima, and other aspects of the characteristic value.

Metadata that describes a characteristic’s value and that may be useful for presentation purposes.

### Describing a characteristic

#### `var manufacturerDescription: String?`

A description of the characteristic provided by the accessory manufacturer.


### Bounding the value

#### `var validValues: [NSNumber]?`

The subset of valid values supported by the characteristic when the format is of type unsigned integer.


#### `var minimumValue: NSNumber?`

The minimum value for the characteristic.


#### `var maximumValue: NSNumber?`

The maximum value for the characteristic.


#### `var stepValue: NSNumber?`

The minimum interval between values for the characteristic.


#### `var maxLength: NSNumber?`

The maximum number of UTF-8 characters allowed in a characteristic that uses a string format.


### Formatting the value

#### `var format: String?`

The format of the values for the characteristic.


#### Characteristic Data Formats

Constants for identifying the data format of characteristic values.


### Specifying units

#### `var units: String?`

The units of the characteristic value.


#### Characteristic Units

Descriptions of the units of a characteristic.


### Initializers (HMCharacteristicMetadata)

#### `init()`


### Relationships (HMCharacteristicMetadata)

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

### See Also: Managing characteristic presentation

- **metadata**: Metadata about the units and other properties of the characteristic.

---

