# HomeKit: Automation

Classes for creating action sets (scenes), triggers, and events for home automation.

## Class: HMActionSet

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMActionSet
```


Action sets can be executed as a result of evaluating a trigger (instances of `HMTrigger`) or manually with `executeActionSet(_:completionHandler:)`. Actions in an action set are performed in an unspecified order. You create new action sets using the `addActionSet(withName:completionHandler:)` method of `HMHome`.

A collection of actions that you trigger as a group.

### Identifiying an action set

#### `var uniqueIdentifier: UUID` (HMActionSet)

The action set’s unique identifier.


#### `var name: String` (HMActionSet)

The name of the action set.


#### `func updateName(String, completionHandler: ((any Error)?) -> Void)` (HMActionSet)

Updates the name of the action set.


### Specifying a type

#### `var actionSetType: String`

The type of the action set, such as built-in or user-defined.


#### Action Set Types

The types of action sets that you can define.


### Defining the associated actions

#### `var actions: Set<HMAction>`

Set of actions in the action set.


#### `func addAction(HMAction, completionHandler: ((any Error)?) -> Void)`

Adds an action to the action set.


#### `func removeAction(HMAction, completionHandler: ((any Error)?) -> Void)`

Removes an action from the action set.


#### `class HMCharacteristicWriteAction`

An action in an action set that writes a value to a characteristic.


#### `class HMAction`

An abstract base class for actions in HomeKit.


### Keeping track of execution

#### `var isExecuting: Bool`

The execution status of the action set.


#### `var lastExecutionDate: Date?`

The last execution date of the action set.


### Relationships (HMActionSet)

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

### See Also: Action Sets (HMActionSet)

- **HMTimerTrigger**: A trigger to activate an action set based on a periodic timer.
- **HMEventTrigger**: A trigger to activate an action set based on a set of events and optional conditions.

---

## Class: HMAction

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMAction
```


Actions can be added to `HMActionSet` objects. Action sets can then be set for automatic execution in response to specific conditions using `HMTrigger` objects, or manually triggered with `executeActionSet(_:completionHandler:)`.

An abstract base class for actions in HomeKit.

### Identifying an action

#### `var uniqueIdentifier: UUID` (HMAction)

A unique identifier for the action.


### Initializers (HMAction)

#### `init()` **(Deprecated)** (HMAction)


### Type Methods (HMAction)

#### `class func new() -> Self` **(Deprecated)** (HMAction)


### Relationships (HMAction)

**Inherits From:**

- `NSObject`

**Inherited By:**

- `HMCharacteristicWriteAction`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Related Documentation

- **HomeKit Developer Guide**:

### See Also: Defining the associated actions (HMAction)

- **actions**: Set of actions in the action set.
- **addAction(_:completionHandler:)**: Adds an action to the action set.
- **removeAction(_:completionHandler:)**: Removes an action from the action set.
- **HMCharacteristicWriteAction**: An action in an action set that writes a value to a characteristic.

---

## Class: HMCharacteristicWriteAction

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMCharacteristicWriteAction<TargetValueType> where TargetValueType : NSCopying
```


Action sets are instances of `HMActionSet`.

An action in an action set that writes a value to a characteristic.

### New Methods

#### `init(characteristic: HMCharacteristic, targetValue: TargetValueType)`

Initialize a characteristic write action with a specified characteristic and target value.


#### `var characteristic: HMCharacteristic` (HMCharacteristicWriteAction)

The characteristic whose value is to be written by the action.


#### `var targetValue: TargetValueType`

The value that will be written to the characteristic when the action is executed.


#### `func updateTargetValue(TargetValueType, completionHandler: ((any Error)?) -> Void)`

Updates the target value.


### Relationships (HMCharacteristicWriteAction)

**Inherits From:**

- `HMAction`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Defining the associated actions (HMCharacteristicWriteAction)

- **actions**: Set of actions in the action set.
- **addAction(_:completionHandler:)**: Adds an action to the action set.
- **removeAction(_:completionHandler:)**: Removes an action from the action set.
- **HMAction**: An abstract base class for actions in HomeKit.

---

## Class: HMTrigger

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMTrigger
```


This class defines the basic behavior of triggers, but does not itself specify any criteria for firing a trigger. Use instances of subclasses of `HMTrigger` to set up concrete triggers for actions.

An abstract base class for triggering actions based on a set of conditions.

### Managing Triggers

#### `var name: String` (HMTrigger)

The name of the trigger.


#### `func updateName(String, completionHandler: ((any Error)?) -> Void)` (HMTrigger)

Updates the name of the trigger.


#### `var isEnabled: Bool`

State of the trigger.


#### `func enable(Bool, completionHandler: ((any Error)?) -> Void)`

Changes the enabled state of the trigger.


#### `var lastFireDate: Date?` **(Deprecated)**

The last time this trigger fired.


#### `var uniqueIdentifier: UUID` (HMTrigger)

A unique identifier for this trigger.


### Managing Action Sets

#### `var actionSets: [HMActionSet]`

Array of all action sets that will be executed by the trigger.


#### `func addActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)`

Adds an action set to the trigger.


#### `func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)`

Removes an action set from the trigger.


### Relationships (HMTrigger)

**Inherits From:**

- `NSObject`

**Inherited By:**

- `HMEventTrigger`
- `HMTimerTrigger`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Triggering an action set

- **triggers**: An array of triggers defined in the home.
- **addTrigger(_:completionHandler:)**: Adds a trigger to the home.
- **removeTrigger(_:completionHandler:)**: Removes a trigger from the home.
- **HMTimerTrigger**: A trigger to activate an action set based on a periodic timer.
- **HMEventTrigger**: A trigger to activate an action set based on a set of events and optional conditions.

---

## Class: HMTimerTrigger

**Availability:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMTimerTrigger
```


When a timer trigger is enabled using `enable(_:completionHandler:)`, the system checks to verify that the timer trigger’s fire date, time zone, and recurrence rules yield a next fire date that is in the future.

A trigger to activate an action set based on a periodic timer.

### Creating a timer trigger

#### `init(name: String, fireDate: Date, recurrence: DateComponents?)`


### Choosing the fire date

#### `var fireDate: Date`

The time at which the trigger will next fire.


#### `func updateFireDate(Date, completionHandler: ((any Error)?) -> Void)`

Updates the next fire date for the trigger.


### Using recurrence

#### `var recurrence: DateComponents?`

The interval on which to repeat firing the trigger.


#### `func updateRecurrence(DateComponents?, completionHandler: ((any Error)?) -> Void)`

Updates the recurrence interval.


### Deprecated symbols (HMTimerTrigger)

#### `init(name: String, fireDate: Date, timeZone: TimeZone?, recurrence: DateComponents?, recurrenceCalendar: Calendar?)` **(Deprecated)**

Initializes a timer trigger with specified timing information.


#### `var timeZone: TimeZone?` **(Deprecated)**

The timezone in which to evaluate the fire time.


#### `func updateTimeZone(TimeZone?, completionHandler: ((any Error)?) -> Void)` **(Deprecated)**

Updates the trigger’s time zone.


#### `var recurrenceCalendar: Calendar?` **(Deprecated)**

The calendar in which the recurrence value is evaluated.


### Relationships (HMTimerTrigger)

**Inherits From:**

- `HMTrigger`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Action Sets (HMTimerTrigger)

- **HMActionSet**: A collection of actions that you trigger as a group.
- **HMEventTrigger**: A trigger to activate an action set based on a set of events and optional conditions.

---

## Class: HMEventTrigger

**Availability:** iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMEventTrigger
```


Use an `HMEventTrigger` object to trigger the execution of a scene when a combination of characteristic or location events and conditions occur. To create an event trigger, first create one or more event objects that fire an event when the specified trigger values are met. For example, you might create an `HMCharacteristicEvent` that fires when the front door is open. Then, you can use `HMEventTrigger` convenience methods to create optional predicates that specify conditions that must be met before a scene is executed. For example, you might create a condition that ensures the scene is executed only after sunset.

A trigger to activate an action set based on a set of events and optional conditions.

### Creating an event trigger

#### `init(name: String, events: [HMEvent], predicate: NSPredicate?)`

Creates a new event trigger with the specified name, events, and predicate.


#### `init(name: String, events: [HMEvent], end: [HMEvent]?, recurrences: [DateComponents]?, predicate: NSPredicate?)`

Creates a new event trigger with the specified name, events, end events, recurrences, and predicate.


### Querying trigger activation state

#### `var triggerActivationState: HMEventTriggerActivationState`

The current activation state of the trigger.


#### `enum HMEventTriggerActivationState`

The activation state of an event trigger.


### Setting trigger events

#### `var events: [HMEvent]`

The events that activate the trigger.


#### `func updateEvents([HMEvent], completionHandler: ((any Error)?) -> Void)`

Updates the set of trigger events.


#### Location events

Events that represent the user’s movement among regions.


#### Time events

Events based on time, significant occurrences, and time durations.


#### Characteristic events

Events based on the capabilities or characteristics of accessories.


#### Presence events

Events based on the user’s presence in a home.


#### `class HMEvent`

The abstract base class for a HomeKit event.


### Restoring the previous scene after an event

#### `var endEvents: [HMEvent]`

The events associated with the end of scene represented by this trigger.


#### `func updateEndEvents([HMEvent], completionHandler: ((any Error)?) -> Void)`

Updates the set of end events associated with the event trigger.


### Controlling recurrence

#### `var recurrences: [DateComponents]?`

Specifies the days on which the trigger can execute.


#### `func updateRecurrences([DateComponents]?, completionHandler: ((any Error)?) -> Void)`

Updates the days of the week the trigger can repeat.


#### `var executeOnce: Bool`

A Boolean that can execute the trigger many times.


#### `func updateExecuteOnce(Bool, completionHandler: ((any Error)?) -> Void)`

Updates the repetition status of the event trigger.


### Adding a trigger condition

#### `var predicate: NSPredicate?`

The predicate to evaluate before executing the scene associated with the event trigger.


#### `func updatePredicate(NSPredicate?, completionHandler: ((any Error)?) -> Void)`

Replaces the predicate used to evaluate execution of the scene associated with the event trigger.


### Creating predicates

#### `class func predicateForEvaluatingTriggerOccurring(beforeSignificantEvent: HMSignificantTimeEvent) -> NSPredicate`

Creates a predicate that evaluates whether the event occurred before a significant event.


#### `class func predicateForEvaluatingTriggerOccurring(afterSignificantEvent: HMSignificantTimeEvent) -> NSPredicate`

Creates a predicate that evaluates whether the event occurred after a significant event.


#### `class func predicate(forEvaluatingTriggerOccurringBetweenSignificantEvent: HMSignificantTimeEvent, secondSignificantEvent: HMSignificantTimeEvent) -> NSPredicate`

Creates a predicate that evaluates whether the event occurred between two significant events.


#### `class func predicateForEvaluatingTrigger(occurringBefore: DateComponents) -> NSPredicate`

Creates a predicate that evaluates whether the event occurred before the specified time.


#### `class func predicateForEvaluatingTrigger(occurringOn: DateComponents) -> NSPredicate`

Creates a predicate that evaluates whether the event occurred at the specified time.


#### `class func predicateForEvaluatingTrigger(occurringAfter: DateComponents) -> NSPredicate`

Creates a predicate that evaluates whether the event occurred at or after the specified time.


#### `class func predicateForEvaluatingTriggerOccurringBetweenDate(with: DateComponents, secondDateWith: DateComponents) -> NSPredicate`

Creates a predicate that evaluates whether the event occurred between the specified times.


#### `class func predicateForEvaluatingTrigger(HMCharacteristic, relatedBy: NSComparisonPredicate.Operator, toValue: Any) -> NSPredicate`

Creates a predicate that evaluates whether a characteristic value relates to the specified value.


#### `class func predicateForEvaluatingTrigger(withPresence: HMPresenceEvent) -> NSPredicate`

Creates a predicate that evaluates the current user presence against that specified in the presence event.


#### `let HMCharacteristicKeyPath: String`

Specifies the key path for a characteristic in a predicate.


#### `let HMCharacteristicValueKeyPath: String`

Specifies the key path for a characteristic value in a predicate.


#### `let HMPresenceKeyPath: String`

Specifies the key path for a presence event in a predicate.


### Deprecated symbols (HMEventTrigger)

#### `func addEvent(HMEvent, completionHandler: ((any Error)?) -> Void)` **(Deprecated)**

Adds a new event to the event trigger.


#### `func removeEvent(HMEvent, completionHandler: ((any Error)?) -> Void)` **(Deprecated)**

Removes the specified event from the event trigger.


#### `class func predicateForEvaluatingTrigger(occurringBefore: String, applyingOffset: DateComponents?) -> NSPredicate` **(Deprecated)**

Creates a predicate that evaluates whether the event occurred before a significant event.


#### `class func predicateForEvaluatingTrigger(occurringAfter: String, applyingOffset: DateComponents?) -> NSPredicate` **(Deprecated)**

Creates a predicate that evaluates whether the event occurred before a significant event.


### Relationships (HMEventTrigger)

**Inherits From:**

- `HMTrigger`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Action Sets (HMEventTrigger)

- **HMActionSet**: A collection of actions that you trigger as a group.
- **HMTimerTrigger**: A trigger to activate an action set based on a periodic timer.

---

## Class: HMEvent

**Availability:** iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMEvent
```

The abstract base class for a HomeKit event.

### Getting information about the event

#### `var uniqueIdentifier: UUID` (HMEvent)

A unique identifier for the event.


#### `class func isSupported(for: HMHome) -> Bool`

A Boolean value indicating whether the event can be added to an event trigger on the specified home.


### Initializers (HMEvent)

#### `init()` **(Deprecated)** (HMEvent)


### Type Methods (HMEvent)

#### `class func new() -> Self` **(Deprecated)** (HMEvent)


### Relationships (HMEvent)

**Inherits From:**

- `NSObject`

**Inherited By:**

- `HMCharacteristicEvent`
- `HMCharacteristicThresholdRangeEvent`
- `HMLocationEvent`
- `HMPresenceEvent`
- `HMTimeEvent`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Setting trigger events

- **events**: The events that activate the trigger.
- **updateEvents(_:completionHandler:)**: Updates the set of trigger events.
- **Location events**: Events that represent the user’s movement among regions.
- **Time events**: Events based on time, significant occurrences, and time durations.
- **Characteristic events**: Events based on the capabilities or characteristics of accessories.
- **Presence events**: Events based on the user’s presence in a home.

---

## Class: HMCalendarEvent

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

```swift
class HMCalendarEvent
```

An event that fires at a specified time.

### Creating a calendar event

#### `init(fire: DateComponents)`

Creates a calendar event which fires based on the value of the supplied date components.


### Inspecting the calendar event

#### `var fireDateComponents: DateComponents`

The date components that specify when the event is triggered.


### Relationships (HMCalendarEvent)

**Inherits From:**

- `HMTimeEvent`

**Inherited By:**

- `HMMutableCalendarEvent`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCopying`
- `NSMutableCopying`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Dates and times

- **HMMutableCalendarEvent**: A mutable event that fires at a specified time.
- **HMTimeEvent**: An abstract superclass for time-based events.

---

## Class: HMCharacteristicEvent

**Availability:** iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

```swift
class HMCharacteristicEvent<TriggerValueType> where TriggerValueType : NSCopying
```

An event that is evaluated based on the value of a characteristic.

### Creating a characteristic event

#### `init(characteristic: HMCharacteristic, triggerValue: TriggerValueType?)`

Creates a new characteristic event which triggers when the specified characteristic reaches the specified value.


### Inspecting the event

#### `var characteristic: HMCharacteristic` (HMCharacteristicEvent)

The characteristic associated with the event.


#### `var triggerValue: TriggerValueType?`

The value of the characteristic that triggers the event.


### Configuring the event

#### `func updateTriggerValue(TriggerValueType?, completionHandler: ((any Error)?) -> Void)` **(Deprecated)**

Changes the trigger value associated with this event.


### Relationships (HMCharacteristicEvent)

**Inherits From:**

- `HMEvent`

**Inherited By:**

- `HMMutableCharacteristicEvent`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCopying`
- `NSMutableCopying`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Characteristics

- **HMMutableCharacteristicEvent**: A mutable event that is evaluated based on the value of a characteristic.

---

## Class: HMCharacteristicThresholdRangeEvent

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

```swift
class HMCharacteristicThresholdRangeEvent
```

An event that triggers when the value of a characteristic is within a specified range.

### Creating a characteristic threshold range event

#### `init(characteristic: HMCharacteristic, thresholdRange: HMNumberRange)`

Creates a characteristic threshold range event for the specified characteristic and number range.


### Inspecting a characteristic threshold event

#### `var characteristic: HMCharacteristic` (HMCharacteristicThresholdRangeEvent)

The characteristic associated with the event.


#### `var thresholdRange: HMNumberRange`

The range of the characteristic value that triggers the event.


### Relationships (HMCharacteristicThresholdRangeEvent)

**Inherits From:**

- `HMEvent`

**Inherited By:**

- `HMMutableCharacteristicThresholdRangeEvent`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCopying`
- `NSMutableCopying`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Characteristic ranges

- **HMNumberRange**: A set of numbers used to specify conditions for characteristic range threshold events.
- **HMMutableCharacteristicThresholdRangeEvent**: A mutable event that triggers when the value of a characteristic is within a specified range.

---

## Class: HMDurationEvent

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

```swift
class HMDurationEvent
```


Use a duration event to specify that a different event should end after a period of time.

An event that ends after the specified time duration.

### Creating a duration event

#### `init(duration: TimeInterval)`

Creates a duration event with the specified time duration.


### Inspecting a duration event

#### `var duration: TimeInterval`

The event’s duration, in seconds.


### Relationships (HMDurationEvent)

**Inherits From:**

- `HMTimeEvent`

**Inherited By:**

- `HMMutableDurationEvent`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCopying`
- `NSMutableCopying`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Durations

- **HMMutableDurationEvent**: A mutable event that fires after the specified time duration.

---

## Class: HMLocationEvent

**Availability:** iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, tvOS 10.0+, watchOS 2.0+

```swift
class HMLocationEvent
```

An event that is evaluated based on entry to or exit from a region.

### Creating a Location Event

#### `init(region: CLRegion)`

Creates a new location event with the specified region.


### Inspecting the Region

#### `var region: CLRegion?`

The region on which events are triggered.


### Configuring the Region

#### `func updateRegion(CLRegion, completionHandler: ((any Error)?) -> Void)` **(Deprecated)**

Changes the region associated with this event.


### Relationships (HMLocationEvent)

**Inherits From:**

- `HMEvent`

**Inherited By:**

- `HMMutableLocationEvent`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCopying`
- `NSMutableCopying`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Locations

- **HMMutableLocationEvent**: A mutable event that is evaluated based on entry to or exit from a region.

---

## Class: HMPresenceEvent

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

```swift
class HMPresenceEvent
```

An event that triggers based on the presence of users in the home.

### Creating a presence event

#### `init(presenceEventType: HMPresenceEventType, presenceUserType: HMPresenceEventUserType)`

Creates a new presence event with the specified event and user presence types.


### Inspecting a presence event

#### `var presenceEventType: HMPresenceEventType`

The event type that triggers the presence event.


#### `var presenceUserType: HMPresenceEventUserType`

The user type whose presence triggers the event.


### Relationships (HMPresenceEvent)

**Inherits From:**

- `HMEvent`

**Inherited By:**

- `HMMutablePresenceEvent`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCopying`
- `NSMutableCopying`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: User presence (HMPresenceEvent)

- **HMMutablePresenceEvent**: A mutable event that triggers based on the presence of users in the home.
- **HMPresenceEventType**: The user presence type that triggers a presence event.
- **HMPresenceEventUserType**: The group of users that triggers a presence event.

---

## Class: HMSignificantTimeEvent

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

```swift
class HMSignificantTimeEvent
```


Use this class to represent an event that fires at a time relative to a significant event, for example “30 minutes before sunset”.

An event that fires at a time offset from a significant time-based event.

### Creating a significant time event

#### `init(significantEvent: HMSignificantEvent, offset: DateComponents?)`

Creates a new significant time event with the specified significant event and offset.


### Inspecting a significant time event

#### `var significantEvent: HMSignificantEvent`

The significant time-based event that is used to calculate when the event fires.


#### `var offset: DateComponents?`

The offset from the significant event that the event fires at.


### Relationships (HMSignificantTimeEvent)

**Inherits From:**

- `HMTimeEvent`

**Inherited By:**

- `HMMutableSignificantTimeEvent`

**Conforms To:**

- `CVarArg`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `NSCopying`
- `NSMutableCopying`
- `NSObjectProtocol`
- `Sendable`
- `SendableMetatype`

### See Also: Significant events

- **HMSignificantEvent**: An event that represents significant time-based events, including sunrise and sunset.
- **HMMutableSignificantTimeEvent**: A mutable event that fires at the specified temporal offset to a significant event.

---

## Enumeration: HMPresenceEventType

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

```swift
enum HMPresenceEventType
```

The user presence type that triggers a presence event.

### Specifying presence type

#### `case everyEntry`

Triggers the event every time a user enters the home.


#### `case everyExit`

Triggers the event every time a user leaves the home.


#### `case firstEntry`

Triggers an event for the first user entering the home.


#### `case lastExit`

Triggers an event when the last user leaves the home.


### Using presence as a predicate

#### `static var atHome: HMPresenceEventType`

Triggers the event when at least one user is in the home.


#### `static var notAtHome: HMPresenceEventType`

Triggers the event when there are no users in the home.


### Initializers (HMPresenceEventType)

#### `init?(rawValue: UInt)` (HMPresenceEventType)


### Relationships (HMPresenceEventType)

**Conforms To:**

- `BitwiseCopyable`
- `Equatable`
- `Hashable`
- `RawRepresentable`
- `Sendable`
- `SendableMetatype`

### See Also: User presence (HMPresenceEventType)

- **HMPresenceEvent**: An event that triggers based on the presence of users in the home.
- **HMMutablePresenceEvent**: A mutable event that triggers based on the presence of users in the home.
- **HMPresenceEventUserType**: The group of users that triggers a presence event.

---

## Enumeration: HMPresenceEventUserType

**Availability:** iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+

```swift
enum HMPresenceEventUserType
```

The group of users that triggers a presence event.

### Selecting users

#### `case currentUser`

The current user triggers the presence event.


#### `case homeUsers`

All users associated with a home trigger a presence event.


#### `case customUsers`

A custom set of users is used to trigger a presence event.


### Initializers (HMPresenceEventUserType)

#### `init?(rawValue: UInt)` (HMPresenceEventUserType)


### Relationships (HMPresenceEventUserType)

**Conforms To:**

- `BitwiseCopyable`
- `Equatable`
- `Hashable`
- `RawRepresentable`
- `Sendable`
- `SendableMetatype`

### See Also: User presence (HMPresenceEventUserType)

- **HMPresenceEvent**: An event that triggers based on the presence of users in the home.
- **HMMutablePresenceEvent**: A mutable event that triggers based on the presence of users in the home.
- **HMPresenceEventType**: The user presence type that triggers a presence event.

---

