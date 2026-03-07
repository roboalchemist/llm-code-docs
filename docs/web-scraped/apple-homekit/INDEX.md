# Apple HomeKit Framework Documentation

Comprehensive API reference for Apple's HomeKit framework.

**Framework:** HomeKit
**Platforms:** iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 10.0+, visionOS 1.0+, watchOS 2.0+

## Files

- [Framework Overview](001-overview.md) - Top-level framework description and topic organization
- [Home Management](002-home-management.md) - HMHomeManager, HMHome, HMRoom, HMZone, HMUser, HMAccessControl, delegates
- [Accessories](003-accessories.md) - HMAccessory, HMAccessoryBrowser, HMAccessoryCategory, HMAccessoryProfile, setup classes, delegates
- [Services & Characteristics](004-services-characteristics.md) - HMService, HMServiceGroup, HMCharacteristic, HMCharacteristicMetadata
- [Automation](005-automation.md) - Action sets, triggers (timer/event), events (calendar, characteristic, duration, location, presence, significant time)
- [Camera](006-camera.md) - HMCameraProfile, HMCameraControl, audio/settings/snapshot/stream controls
- [Matter & SwiftUI](007-matter-swiftui.md) - Matter integration notes, CameraView
- [Service Types Reference](008-service-types-reference.md) - Complete list of 50+ accessory service type constants
- [Characteristic Types Reference](009-characteristic-types-reference.md) - Complete list of 100+ characteristic type constants
- [Accessory Category Types](010-accessory-category-types.md) - Complete list of 30+ accessory category type constants
- [Errors](011-errors.md) - HMError, HMError.Code enumeration, HMErrorDomain
- [Guides & Articles](012-guides.md) - Setup guides, configuration articles, sample code references
- [Action Set Types](013-action-set-types.md) - Action set type constants

## Coverage

- **Classes:** 45 (HMAccessControl, HMAccessory, HMAccessoryBrowser, HMAccessoryCategory, HMAccessoryOwnershipToken, HMAccessoryProfile, HMAccessorySetupManager, HMAccessorySetupPayload, HMAccessorySetupRequest, HMAccessorySetupResult, HMAction, HMActionSet, HMCalendarEvent, HMCameraAudioControl, HMCameraControl, HMCameraProfile, HMCameraSettingsControl, HMCameraSnapshot, HMCameraSnapshotControl, HMCameraStream, HMCameraStreamControl, HMCameraView, HMCharacteristic, HMCharacteristicEvent, HMCharacteristicMetadata, HMCharacteristicThresholdRangeEvent, HMCharacteristicWriteAction, HMDurationEvent, HMEvent, HMEventTrigger, HMHome, HMHomeAccessControl, HMHomeManager, HMLocationEvent, HMMediaSourceDisplayOrderProfile, HMNetworkConfigurationProfile, HMPresenceEvent, HMRoom, HMService, HMServiceGroup, HMSignificantTimeEvent, HMTimerTrigger, HMTrigger, HMUser, HMZone)
- **Protocols:** 4 (HMAccessoryBrowserDelegate, HMAccessoryDelegate, HMHomeDelegate, HMHomeManagerDelegate)
- **Enumerations:** 4 (HMCameraStreamState, HMHomeHubState, HMPresenceEventType, HMPresenceEventUserType)
- **Structures:** 3 (CameraView, HMError, HMHomeManagerAuthorizationStatus)
- **Type Collections:** 7 (Accessory Category Types, Accessory Service Types, Action Set Types, Characteristic Data Formats, Characteristic Properties, Characteristic Units, Characteristic types)
- **Articles/Guides:** 4

**Source:** [Apple Developer Documentation](https://developer.apple.com/documentation/homekit/)
