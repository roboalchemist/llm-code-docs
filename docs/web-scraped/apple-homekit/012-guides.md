# HomeKit: Guides and Articles

## Sample Code: Configuring a home automation device

Give users a familiar experience when they manage HomeKit accessories.


This sample presents a simplified version of the kind of app a HomeKit-enabled accessory manufacturer might provide. You use the app to configure and control a specific device—a garage door opener from a fictional manufacturer, Kilgo Devices. The app offers access to secondary and custom characteristics that Apple’s Home app doesn’t expose. It provides a user experience that’s consistent with the Home app’s approach and terminology, but doesn’t attempt to replicate every feature of the Home app.

[Image: GarageControl.png]

For more information about user interface considerations for HomeKit-enabled apps, see the `` section of the ``.


To be able to use HomeKit, you enable the HomeKit capability and include the `nshomekitusagedescription` key in your app’s `Info.plist` file, as described in `enabling_homekit_in_your_app`. In this sample app, the capability is already enabled and a usage description is provided.

Perform the following steps before building and running the app:

1. Set a valid signing team in the target’s General pane so that Xcode can create a provisioning profile containing the HomeKit entitlement when you build for the first time.
2. Download and install the Home Accessory Simulator (HAS) on your Mac to be able to emulate HomeKit-enabled accessories. See `testing_your_app_with_the_homekit_accessory_simulator`.
3. Import the `hasaccessory` file that the sample app bundles to define the specific garage door opener accessory that the app controls. Choose `File > Import Accessory` from the HAS menu. In the dialog that appears, navigate to the downloaded sample code project’s `Documentation` folder, and select the `garage.hasaccessory` file.

The import creates a single accessory with a hidden accessory information service that all accessories have, and two user-interactive services: one that controls a garage door and another to control an attached light bulb. Most of the associated characteristics are standard for their service. Only one—the light bulb’s fade rate—is custom. You can use HAS to inspect and manipulate all of these items.


You always use an instance of `hmhomemanager` as the root HomeKit object. The home manager contains an array of homes, each of which has a collection of accessories. The sample app defines a `HomeStore` class for use as a singleton that holds the one and only home manager for the app:

```swift
class HomeStore: NSObject {
    /// A singleton that can be used anywhere in the app to access the home manager.
    static var shared = HomeStore()
    
    /// The one and only home manager that belongs to the home store singleton.
    let homeManager = HMHomeManager()
    
    /// A set of objects that want to receive home delegate callbacks.
    var homeDelegates = Set<NSObject>()
    
    /// A set of objects that want to receive accessory delegate callbacks.
    var accessoryDelegates = Set<NSObject>()
}
```

You create an accessory list collection view controller to present the list of connected accessories. Because this root view controller never gets deallocated, it can safely assign itself as the `hmhomemanagerdelegate` protocol delegate:

```swift
HomeStore.shared.homeManager.delegate = self
```

The manager tells its delegate when the list of homes changes, including the first time the home manager loads data from the HomeKit database during initialization. When this happens, the accessory list reloads to show the accessories in the primary home, or prompts the user to create a new home if none exists.

You can extend the app to allow the user to select among all known homes instead of always choosing the primary home. You can also allow users to add, remove, or rename homes, although the user performs these tasks infrequently, and typically relies on the Home app to do so.


The first time you run the app, the accessory list is empty, because you haven’t associated any accessories from Kilgo Devices. The app’s UI presents a `+` button in the navigation bar that you tap to initiate a search for accessories on the local network. The button’s tap handler calls the home’s `1771427-addandsetupaccessories` method.

```swift
home?.addAndSetupAccessories(completionHandler: { error in
    if let error = error {
        print(error)
    } else {
        // Make no assumption about changes; just reload everything.
        self.reloadData()
    }
})
```

This presents the standard HomeKit UI for locating and adding new accessories to a given home. On success, the completion handler refreshes the app’s copy of the HomeKit data and redraws the display.

When your app enters the standard accessory association flow, which is the same one that the Home app uses, the user follows these steps:

1. **Scan or enter the new device’s HomeKit setup code.** This code comes packaged with the device, or is available in the HAS display for the accessory.
2. **Select from a list of devices on the network that don’t already have an existing HomeKit association.** This includes both real and simulated devices that can access the local area network.
3. **Wait for HomeKit to verify that the setup code entered in step 1 matches the device’s code.**
4. **Assign a name and room to each service associated with the device.** HomeKit provides a default name and room for each service, one page per service, that the user can accept or change.

Each item that the user names in step 4 appears in the Home app as an “accessory”. However, in HomeKit, these are `hmservice` instances. They are owned by an `hmaccessory` instance that represents the physical device that you selected in step 2. To maintain a user experience consistent with the Home app, the sample app UI (and the rest of this article) also refers to each `hmservice` instance as an accessory.


You draw the display based on a copy of data from HomeKit captured into an array of Kilgo services:

```swift
var kilgoServices = [HMService]()    // These are called "accessories" in the UI.
```

When the accessory list reloads, either because a new home is set or because the accessory-add flow completes, you populate the above array, filtering out `hmaccessory` instances from manufacturers other than Kilgo, and `hmservice` instances that aren’t user interactive. Also while gathering the list, you request notifications for changes on any of the corresponding characteristics, which are the individual points of status and control for a given service:

```swift
for accessory in home.accessories.filter({ $0.manufacturer == "Kilgo Devices, Inc." }) {
    accessory.delegate = HomeStore.shared
    
    for service in accessory.services.filter({ $0.isUserInteractive }) {
        kilgoServices.append(service)
        
        // Ask for notifications from any characteristics that support them.
        for characteristic in service.characteristics.filter({
            $0.properties.contains(HMCharacteristicPropertySupportsEventNotification)
        }) {
            characteristic.enableNotification(true) { _ in }
        }
    }
}
```

As a result, the display shows only the accessories relevant to this particular app.

> **Note:** Use care when crafting your filters. For example, the name “Kilgo Devices, Inc.” might not be unique among all past and future manufacturers, and therefore might not serve as a sufficient predicate in a real app.


Accessories (like light bulbs) have characteristics (like power state, color temperature, brightness, and so on) that users control or observe. Users typically care about one of these characteristics above the others, because they change or read that characteristic most often. This is the primary characteristic, and you should give users quick access to it. For a light bulb, users most often want to switch it on or off, so the power state is the primary characteristic.

It’s up to you to define what the primary charactersitc is for the accessories you control. You can do that by creating a computed property on `hmservice` in an extension that returns the type of primary characteristic:

```swift
var primaryControlCharacteristicType: String? {
    switch kilgoServiceType {
    case .lightBulb: return HMCharacteristicTypePowerState
    case .garageDoor: return HMCharacteristicTypeTargetDoorState
    case .unknown: return nil
    }
}
```

Then use this primary characteristic type to locate and return the characteristic that has that type:

```swift
var primaryControlCharacteristic: HMCharacteristic? {
    return characteristics.first { $0.characteristicType == primaryControlCharacteristicType }
}
```

For Kilgo Devices, both the light bulb and garage door have binary primary state. The bulb is on or off. The target state of the door is open or closed. This lends itself to an interface where a toggle switch is sufficient to control all primary characteristics. You can implement this as the tap handler on each item in the accessory list collection view. When the user taps the accessory, you read the current characteristic value and then write the opposite:

```swift
func tap() {
    if let characteristic = service?.primaryControlCharacteristic,
        let value = characteristic.value as? Bool {

        // Provide visual feedback that the item was tapped.
        bounce()
        
        // Write the new value to HomeKit.
        characteristic.writeValue(!value) { error in
            self.redrawState(error: error)
        }
    }
}
```

The write involves network access, so HomeKit calls a completion handler when the write completes. Use this opportunity to update the state of the interface, as shown in the snippet above.


When the user taps an accessory’s information button, the app reveals details about the accessory. From the detail view, the user can rename the accessory, assign it to a room, remove it from the home, and see device information, like the firmware version. The user can also tap Settings to reveal a list of secondary characteristics for that accessory.

Control the user experience by presenting only relevant characteristic types. The `KilgoService` extension of `hmservice` defines a computed property that limits the list of displayable characteristics to those in a curated list:

```swift
var displayableCharacteristics: [HMCharacteristic] {
    let characteristicTypes = [HMCharacteristicTypePowerState,
                               HMCharacteristicTypeBrightness,
                               HMCharacteristicTypeHue,
                               HMCharacteristicTypeSaturation,
                               HMCharacteristicTypeTargetDoorState,
                               HMCharacteristicTypeCurrentDoorState,
                               HMCharacteristicTypeObstructionDetected,
                               HMCharacteristicTypeTargetLockMechanismState,
                               HMCharacteristicTypeCurrentLockMechanismState,
                               KilgoCharacteristicTypes.fadeRate.rawValue]
    
    return characteristics.filter { characteristicTypes.contains($0.characteristicType) }
}
```

These are mostly HomeKit standard types, all of which are applicable to Kilgo devices. There’s also one custom type—fade rate—defined earlier in the same extension:

```swift
enum KilgoCharacteristicTypes: String {
    case fadeRate = "7E536242-341C-4862-BE90-272CE15BD633"
}
```

Characteristic types are stored as UUID strings. The value specified in the code for fade rate matches the value found in the accessory simulator, which you can inspect in HAS. If you also build a real Kilgo device, the value used there would have to match as well.

### See Also: Home Manager

- **Testing your app with the HomeKit Accessory Simulator**: Install the HomeKit Accessory Simulator to help you debug your HomeKit-enabled app.
- **HMHomeManager**: The manager for a collection of one or more of a user’s homes.

---

## Article: Enabling HomeKit in your app

Declare your app’s intention to use HomeKit, and get permission from the user to access home automation accessories.


To access the devices in the user’s home automation network, you enable the HomeKit capability for your app. You also provide a usage description that explains to the user why the app needs access, and handle the case where the user denies access.


To ready your app to work with HomeKit, enable the HomeKit capability for your app in Xcode. Open your project, select the app target, and choose the Signing & Capabilities pane. Then click the + button. In the window that appears, choose HomeKit.

[Image: media-3369803]

When you enable the HomeKit capability, Xcode automatically adds the `com.apple.developer.homekit` to your entitlements file. It also adds the corresponding feature to your App ID and links the HomeKit framework.

> **Important:** HomeKit supports independent Apple Watch apps in watchOS 7 and later.


A user’s home automation network is a sensitive resource. Apps with access can collect sensor data and change the state of physical objects in the real world. To protect users, the first time your app uses the HomeKit framework—typically, when you create a `HMHomeManager` instance—the system prompts the user for permission.

You provide a message for this prompt called a *purpose string* or a *usage description* by setting a string value for the `NSHomeKitUsageDescription` that you add to your app’s `Information-Property-List` file. Find and select your project’s `Info.plist` file in Xcode’s project navigator. Modify the file using the property list editor built into Xcode:

[Image: media-3369804]

The system automatically generates the prompt’s title, which includes the name of your app. Your usage description—in this case, “Configure accessories from Kilgo Devices, Inc.”—indicates the reason that your app needs the access.

[Image: media-3369805]

Accurately and concisely explaining to the user why your app needs access to the home network, typically in one complete sentence, lets the user make an informed decision and improves the chances that they’ll grant access.

> **Important:** If you don’t include a purpose string, your app crashes when you first try to use HomeKit.


If the user grants permission, the system remembers the user’s choice and doesn’t prompt again. If the user denies permission, the access attempt that initiated the prompt and any further attempts fail. Look for a `homeAccessNotAuthorized` error in your completion handlers to detect this condition. Alternatively, you can inspect the home manager’s `authorizationStatus` property.

Be aware that even if the user allows the initial access, they can revoke permission at any time in the Settings app. Your app should handle both initial and subsequent access denials gracefully.

If home automation is a secondary function of your app—like an alarm app that plays an audible alert on the device and can also turn the house lights on when the alarm triggers—respect the user’s choice and work around denied access. For example, you can omit unavailable features from the user interface.

If your app can’t provide meaningful functionality without HomeKit access, you can display a message to the user saying so, directing them to change the privacy setting for your app to continue.

### See Also: Essentials

- **HomeKit Entitlement**: A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.
- **NSHomeKitUsageDescription**: A message that tells people why the app is requesting access to their HomeKit configuration data.

---

## Sample Code: Interacting with a home automation network

Find all the automation accessories in the primary home and control their state.


This sample app introduces you to the accessories, services, and characteristics found in a home automation network, represented by instances of `HMAccessory`, `HMService`, and `HMCharacteristic`, respectively. The sample displays all the properties and relationships it finds using a simple set of hierarchical views inside a split view controller.

[Image: AccessoryFinderHierarchy.png]

This view hierarchy is useful for learning how HomeKit structures device data, which is slightly different than the way the Apple Home app refers to related concepts. It’s also useful for device developers who want to understand how HomeKit sees custom hardware.

In a real app that you publish on the App Store, you would provide a user experience more like the one found in `configuring-a-home-automation-device`. For example, you would focus on the actions a user can take and hide the underlying technical details. For more tips about presenting HomeKit data to users, see the “Adjust the Interface for a Published App” section at the end of this article.


To be able to use HomeKit, you enable the HomeKit capability and include the `NSHomeKitUsageDescription` key in your app’s `Info.plist` file, as described in `enabling-homekit-in-your-app`. In this sample app, the capability is already enabled and a usage description is provided.

To be able to build an app that has the HomeKit capability, you must set a valid signing team in the target’s General pane before you build, so that Xcode can create a provisioning profile containing the HomeKit entitlement.

The sample app works with both real devices and simulated ones. If you don’t have any real home automation accessories, or if you want to try an accessory type that you don’t have, use the HomeKit Accessory Simulator (HAS), as described in `testing-your-app-with-the-homekit-accessory-simulator`. You can use a mix of simulated devices and real ones.


You always use an instance of `HMHomeManager` as the root HomeKit object, following the pattern described in `configuring-a-home-automation-device`. As in that sample, this app finds the primary home, allowing the user to create a new one if none exists. In other respects, this sample leaves home management to the Home app.

When HomeKit data finishes loading after initialization, or after the user creates a new home, your home manager delegate—an adopter of the `HMHomeManagerDelegate` protocol—gets access to the user’s homes. Use the delegate to set the home view’s `home` property based on this information. From the corresponding `didSet` observer, you then call the `resetDisplay(for:)` method to retrieve data from HomeKit and redraw the display, which consists of a list of accessories in the home:

```swift
func resetDisplay(for home: HMHome?) {
    reloadDisplayData(for: home)
    accessoryView?.accessory = nil
    tableView.reloadData()
}
```

Before triggering a table view reload, use the `reloadDisplayData(for:)` method to prepare a list of accessories sorted by room that can serve as a data source for the home view’s table view. Start with the home’s default room—accessible using the `roomForEntireHome()` method. Add that to the contents of the home’s `rooms` array. Then filter out any rooms from this composite group lacking accessories. Sort the remaining rooms by name:

```swift
rooms = ([home.roomForEntireHome()] + home.rooms)
    .filter { !$0.accessories.isEmpty }
    .sorted { $0.name < $1.name }
```


Alternatively, you can display accessories sorted by category. Accessories have a `category` property, which is an instance of the `HMAccessoryCategory` class that indicates what the device is, like a door or a light. You can derive a name from this information, and use that to group accessories:

```swift
home.accessories.forEach {
    let name = $0.displayName   // Computed from the accessory's category.
    if let index = categories.firstIndex(where: { $0.name == name }) {
        categories[index].accessories.append($0)
    } else {
        categories.append(Category(name: name, accessories: [$0]))
    }
}
```

Unlike the `HMRoom` class, the `HMAccessoryCategory` class doesn’t natively contain the list of related accessories. So you define a local `Category` type to serve as a category container:

```swift
struct Category: AccessoryGroup {
    var name: String
    var accessories: [HMAccessory]
}
```

As indicated in the previous and next snippet, both the `Category` type and the `HMRoom` type adopt the `AccessoryGroup` protocol, which declares both a name and a list of accessories. This ensures that either type can serve as the data source:

```swift
protocol AccessoryGroup {
    var name: String { get }
    var accessories: [HMAccessory] { get }
}

// Assert that HMRoom already adopts the AccessoryGroup protocol.
extension HMRoom: AccessoryGroup {}
```


To enable the user to select between displaying accessories grouped by room or category, use a segmented controller in the home view’s toolbar to set the `groupKey` property:

```swift
@objc
func changeSeg(_ sender: UISegmentedControl) {
    groupKey = sender.selectedSegmentIndex == 0 ? .room : .category
}
```

Inside the `groupKey` property’s `didSet` observer, reload the table view without reloading data from HomeKit:

```swift
var groupKey = GroupKey.room {
    didSet {
        // Refreshes the view without reloading the display data from HomeKit.
        accessoryView?.accessory = nil
        tableView.reloadData()
    }
}
```

You use the table view’s data source and delegate methods to prepare table cells based on the current grouping of accessories, as specified by the `groupKey` property.


To enable the pairing of new accessories, the UI presents a `+` button in the home view that the user taps to initiate a search for accessories on the local network. The button’s tap handler calls the home’s `addAndSetupAccessories(completionHandler:)` method, which presents the standard HomeKit UI for locating and adding new accessories to a given home:

```swift
home?.addAndSetupAccessories { error in
    if let error = error {
        print(error)
    } else {
        // Make no assumption about changes; just reload everything.
        self.resetDisplay(for: self.home)
    }
}
```

On success, the completion handler refreshes the app’s copy of the HomeKit data and redraws the display.


The sample app’s split view detail controller shows an `AccessoryView` with information about a single accessory. This includes a list of accessory properties, like the accessory’s name and manufacturer. It also includes services, like a door opener or a light bulb, that the accessory offers. Optionally, for an accessory that’s a bridge, which is an accessory that serves as a link to accessories on a non-HomeKit network, the view also shows a list of the accessories to which the bridge provides access.

> **Note:** Bridged accessories (those with the `isBridged` property set to `true`) also appear in the home view’s main list of accessories because HomeKit makes them directly accessible. Listing them in the accessory view is a convenience to show the relationship with their bridge.

When the user taps an accessory in the home view, you use the `prepare(for:sender:)` method override to assign the corresponding accessory to the accessory view, which triggers the view to reload its content:

```swift
let accessory = grouping[indexPath.section].accessories[indexPath.row]
controller.accessory = accessory
```

When the user taps a service in the accessory view, you push a `ServiceView` instance on the navigation stack. The service view lists the corresponding service’s properties, like its name. It also lists the associated characteristics, which are the control points and data values that the service exposes. For example, the garage door opener service might have a characteristic whose value you set to indicate whether the garage door should be opened or closed. It might have another characteristic whose value you read to find out where the garage door is right now—open, closed, or something in between.

When the user taps a characteristic in the service view, you push a `CharacteristicView` instance onto the navigation stack to provide details about that specific characteristic, like its name and the content of its associated value.


A characteristic is primarily a container for its `value` property that represents an input to or output from a service. Other properties of the characteristic tell you about that value, like if it’s a Boolean, number, string, or something else, what units apply to it, whether you can read or write it, and so on.

When the user taps a service in the accessory view, the incoming service view writes a characteristic to each of its characteristic cells. This begins the process of populating the cell’s UI, for example by adjusting the visibility of the cell’s controls depending on the characteristic value’s type. But the cell can’t rely on the actual value until it calls the characteristic’s `readValue(completionHandler:)` method.

```swift
characteristic.readValue { error in
    if let error = error {
        print(error.localizedDescription)
    } else {
        self.redrawValueLabel()
        self.redrawControls(animated: animated)
    }
}
```

You can access the `value` property at any time, but this is a cached value from the last interaction with the physical accessory, if any. Performing an explicit read operation prompts HomeKit to ask the accessory for the characteristic’s current value, and update its local copy. Because this query involves network access, HomeKit reports the value to your app in a completion handler, which then finalizes the UI changes by setting the cell’s label text and the control state.

The characteristic view, which also displays the characteristic value, doesn’t perform an explicit read. The user can only get to the characteristic view by tapping on a service view’s characteristic cell, which has recently refreshed the corresponding value. Both views rely on accessory delegate callbacks to track any further changes in the value, as described in the next section.


HomeKit gives apps access to a shared home automation network. Apps other than yours, including the Home app, can change service names, characteristic values, the layout of a home, and other attributes. Accessories can also drive changes independently. For example, a garage door opener might have an obstruction sensor with output that varies based on physical changes in the environment. To keep your app’s local data caches and user interfaces up to date with outside changes, your app adopts HomeKit delegate protocols.

The sample app’s home view adopts the  `HMHomeManagerDelegate` protocol to handle changes in the list of homes, as described in the section “Create a Home Manager and Get the Primary Home”. This particular implementation ensures that the home view always shows the primary home.

The home view also implements the  `HMHomeDelegate` protocol to be informed of changes within the chosen home. Because these kinds of changes affect the entire user interface, the app redraws the whole display when anything changes, such as when a room is added by another app:

```swift
func home(_ home: HMHome, didAdd room: HMRoom) {
    guard home == self.home else { return }
    resetDisplay(for: home)
}
```


Accessory changes, reported by the  `HMAccessoryDelegate` protocol, typically don’t warrant completely redrawing the entire interface, but can nonetheless affect multiple view controllers. However, an accessory can have only a single delegate.

For example, it would be disruptive to reset the entire user interface to show only that a light bulb is turned off. But the corresponding characteristic value affects both a toggle switch in a characteristic cell and a value label in the related characteristic view. Both of these might be on the detail view’s navigation stack at the same time and need to be informed of the change.

To solve this, the home store singleton acts as the accessory delegate for all accessories, set whenever the home is updated:

```swift
home?.accessories.forEach { $0.delegate = HomeStore.shared }
```

The home store also becomes the accessory delegate for any accessories added later, set in the `home(_:didAdd:)-6jcl7` delegate method:

```swift
func home(_ home: HMHome, didAdd accessory: HMAccessory) {
    guard home == self.home else { return }
    resetDisplay(for: home)
    
    // Make sure the new accessory generates callbacks to the home store.
    accessory.delegate = HomeStore.shared
}
```

The home store can then act as an accessory delegate hub. Any view controllers that want to receive accessory delegate callbacks register themselves by calling the `addAccessoryDelegate(:)` method:

```swift
func addAccessoryDelegate(_ delegate: NSObject) {
    accessoryDelegates.insert(delegate)
}
```

When the home store receives a delegate callback, it passes the call along to all interested parties, such as when a characteristic value changes:

```swift
func accessory(_ accessory: HMAccessory, service: HMService, didUpdateValueFor characteristic: HMCharacteristic) {
    accessoryDelegates.forEach {
        guard let delegate = $0 as? HMAccessoryDelegate else { return }
        delegate.accessory?(accessory, service: service, didUpdateValueFor: characteristic)
    }
}
```


Most delegate callbacks work by default. However, your app only receives callbacks for characteristic value changes—the delegate method shown at the end of the previous section—when it explicitly enables them. The sample app does this by calling the service’s `enableNotifications` method whenever the service view’s `service` property changes.

```swift
var service: HMService? {
    willSet {
        // Disable notifications on the previous service characteristics.
        service?.enableNotifications(false)
    }
    didSet {
        // Enable notifications on the new service characteristics.
        service?.enableNotifications(true)
        reloadDisplayData()
    }
}
```

This method—defined in an `HMService` extension—in turn calls the  `enableNotification(_:completionHandler:)` method of all the characteristics within the given service that have the `HMCharacteristicPropertySupportsEventNotification-2f0ml` property.

```swift
func enableNotifications(_ enabled: Bool) {
    for characteristic in characteristics
        where characteristic.properties.contains(HMCharacteristicPropertySupportsEventNotification) {
        
        characteristic.enableNotification(enabled) { error in
            if let error = error {
                print(error.localizedDescription)
            }
        }
    }
}
```

The sample app also deactivates notifications for characteristics that are no longer needed. The `willSet` property observer, as shown in the code above, calls the same enabling method, but with `false` as the input, for the service property value as it exists before the update.


For a HomeKit app that you want to publish in the App Store, you design a different user interface than the one in this sample app.

**Expose a lot less detail about individual accessories, services, and characteristics.** Only present information that’s really useful. Most users aren’t interested in unique device identifiers and firmware versions. At a minimum, nest or deemphasize less important details.

**Focus on services as the root interface element, just like in the Home app.** Help users complete tasks by focusing on the actions they can perform, or the data they can read, rather than the physical objects in the environment.

**Expose only user interactive services.** Hide services not reported as user interactive by the device.

**Feature behaviors and settings specific to your app.** If your app supports devices only from a certain manufacturer, or with certain capabilities, filter out the accessories that don’t match. Reduce clutter and present only those devices or capabilities that make sense for your app.

**Provide meaningful interfaces for custom elements.** Your app might enable users to manage custom services and characteristics of a device that you develop. For example, a light service might offer a power-down decay rate characteristic, reducing brightness from full on to full off over a configurable period of time. The Home app doesn’t expose this characteristic, but your app can provide the user with a suitable interface to control it.

For more information about user interface considerations for HomeKit enabled apps, see the `` section of the ``.

### See Also: Accessories

- **HMAccessorySetupManager**: An object that setups up new accessories.
- **HMAccessorySetupResult**: A result object describing information about a successful accessory setup request.
- **HMAccessorySetupRequest**: An object that describes how to add and setup up new accessories.
- **HMAccessory**: A home automation accessory, like a garage door opener or a thermostat.
- **HMService**: A controllable feature of an accessory, like a light attached to a garage door opener.
- **HMCharacteristic**: A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- **HMMediaSourceDisplayOrderProfile**: An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

---

## Article: Testing your app with the HomeKit Accessory Simulator

Install the HomeKit Accessory Simulator to help you debug your HomeKit-enabled app.


While developing your HomeKit-enabled app, you might not have physical access to all the kinds of accessories that you want your app to control. To test your app, install the HomeKit Accessory Simulator (HAS) to simulate any accessories you don’t have, or to help automate your testing process.

HAS runs on your Mac, simulating accessories that you define as a supplement to any physical accessories in your network. You can create accessories with both standard and custom services and characteristics. You can use your Mac’s camera to simulate network cameras and video doorbells. You can also create bridges and bridged accessories to represent more complex network architectures.


You download the HAS as part of the *Additional Tools for Xcode* package found on the `?=for%20Xcode` page, which is part of the Apple developer portal. Choose the version of the package that matches your version of Xcode.

As a convenience, Xcode provides a link to the download page from the Capabilities pane. Xcode displays a button embedded in the HomeKit capability that takes you directly to the download page in Safari.

[Image: media-3150785]

After downloading the disk image file, open it and navigate to the `Hardware` folder. Drag the `HomeKitAccessorySimulator.app` from there to your `Applications` folder. Double-click to launch the simulator.


Accessories in a home automation network are physical devices like light bulbs or garage door openers. Accessories provide control points called services. For example, a garage door opener might offer a door opener and a light. Each service, in turn, has characteristics—the values that describe and control the service. The light has a power state (on or off), a brightness level, and so on. Accessories also have hidden services, like the accessory information service that provides manufacturing information.

[Image: media-3150784]

In the HomeKit Accessory Simulator, define accessories that you can use with your app. For details, see the *HomeKit Accessory Simulation Help*, accessible through the simulator’s `Help` menu.

**Add an accessory.** Assign a name and provide other identifying details. An accessory isn’t typically the user’s main focus, but does serve as a logical container for the services that the user cares about. When you create an accessory, HAS adds the accessory information service by default based on the information you provide.

**Add one or more services to the accessory.** Add as many additional services as you need, potentially including hidden services. For each, specify a service type using one of the standard values in `accessory-service-types`, or using a custom service with a new, unique identifier. Give each service a unique name. For user-visible services, the user might later change the name using the Home app, or using your app.

**Add or modify service characteristics.** HAS populates standard services with a set of standard characteristics for that service, but you can adjust these to match the specific devices you want to model. For example, if a light bulb offers a fade-to-off feature with configurable timing, you might add a custom characteristic indicating the fade rate. The Home app doesn’t expose custom characteristics to the user, but you can control them from your own app.


To be able to access simulated accessories from a HomeKit enabled app, you associate them with a home network. You can do this from any device on your local area network running the Home app, which is installed on all iOS devices by default. The accessory becomes part of the logged-in user’s home network. From the Home or Rooms tab, tap the plus button and choose Add Accessory. Then follow the instructions in the dialog that appears.

[Image: media-3150786]

Alternatively, you can call the `addAndSetupAccessories(completionHandler:)` method from your app.

```swift
home?.addAndSetupAccessories(completionHandler: { error in
    if let error = error {
        // Handle error
    } else {
        self.tableView.reloadData()
    }
})
```

This generates the same accessory association flow as the one presented in the Home app, and produces the same result. Doing it from within your app offers the advantage of being able to work on the iOS Simulator, where the Home app isn’t available.

> **Important:** If you add an accessory on a device, including an iOS Simulator, without a logged-in iCloud account, the accessory is isolated to that device. This means that if you add an accessory to an iPhone simulator and then switch over to using an iPad simulator, you have to reassociate the accessory for it to appear in the new environment.


After the simulated accessory is part of the home automation network, you can find it and control it from your app just as you would a real accessory.

Changes that you make to characteristics in your app show up immediately in HAS. For example, if you let the user switch a light bulb off in your app with a toggle switch, the state of the light bulb changes right away in the HAS interface to match. When you implement accessory delegate methods like `accessory(_:service:didUpdateValueFor:)`, changes made with HAS show up in your app right away as well.

### See Also: Home Manager (Testing)

- **Configuring a home automation device**: Give users a familiar experience when they manage HomeKit accessories.
- **HMHomeManager**: The manager for a collection of one or more of a user’s homes.

---

