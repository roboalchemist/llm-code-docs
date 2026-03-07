# Change Log

All notable changes to `hap-nodejs` will be documented in this file. This project tries to adhere to [Semantic Versioning](http://semver.org/).

## v2.1.0 (2026-02-08)

### Changes

- update readme badges (use `shields.io`) (#1104)
- update publish workflows for npm oidc auth (#1105)
- dependency updates
- update hap characteristics and services
- regenerate documentation (`typedoc`) files

### Homebridge Dependencies

- `@homebridge/ciao` @ `v1.3.5`
- `@homebridge/dbus-native` @ `v0.7.3`
- `bonjour-hap` @ `v3.10.0`

## v2.0.2 (2025-09-17)

### Changes (v2.0.2)

- dependency updates
- code style - use `subarray` instead of `slice` for buffers
- fix types around buffers in test files
- update hap characteristics and services
- regenerate documentation (`typedoc`) files
- docs: remove unnecessary `@group` tags on interface declarations

### Homebridge Dependencies (v2.0.2)

- `@homebridge/ciao` @ `v1.3.4`
- `@homebridge/dbus-native` @ `v0.7.2`
- `bonjour-hap` @ `v3.9.1`

## v2.0.1 (2025-07-23)

### Changes (v2.0.1)

- dependency updates

### Homebridge Dependencies (v2.0.1)

- `@homebridge/ciao` @ `v1.3.4`
- `@homebridge/dbus-native` @ `v0.7.2`
- `bonjour-hap` @ `v3.9.1`

## v2.0.0 (2025-06-17)

### Breaking

- ⚠️ drop support for node v18
  - the minimum node version required is now `v20`
- ⚠️ republish as `@homebridge/hap-nodejs` for consistency

### Changes (v2.0.0)

- update `commander` from `v13` to `v14`
- Added support for NodeJS 24
- Update @homebridge/ciao to 1.3.3
- update `jest` to `v30` and required migration steps
- update `eslint` to `v9` and required migration steps

### Homebridge Dependencies (v2.0.0)

- `@homebridge/ciao` @ `v1.3.3`
- `@homebridge/dbus-native` @ `v0.7.1`
- `bonjour-hap` @ `v3.9.0`

## v1.2.0 (2025-06-08)

### Changes (v1.2.0)

- add constants for `SecuritySystemAlarmType` (#1086)
- update hk plist file from V=880 to V=886 (#1087)
- updated dependencies (#1085)
- fix OOC errors from `validateUserInput` on steps
- merge branch 'release-0.x' into latest
- fix some bad merge conflicts from previous commit
- updated dependencies, use included types from `dbus-native` (#1092)

### Homebridge Dependencies (v1.2.0)

- `@homebridge/ciao` @ `v1.3.2`
- `@homebridge/dbus-native` @ `v0.7.1`
- `bonjour-hap` @ `v3.8.0`

## v1.1.2 (2025-06-04)

*No changes since v1.1.1, just a version bump to trigger a new release.*

## v1.1.1 (2025-03-11)

### Changes (v1.1.1)

- Update name checking (#1083)

### Other Changes

- Update docs
- support node 22 + dependency updates (#1075)

### Homebridge Dependencies (v1.1.1)

- `@homebridge/ciao` @ `v1.3.0`
- `bonjour-hap` @ `v3.8.0`

## v1.1.0 (2024-07-21)

### Changes (v1.1.0)

- Set `Ciao` as the default Advertiser

### Other Changes (v1.1.0)

- Update docs
- Updated dependencies

### Homebridge Dependencies (v1.1.0)

- `@homebridge/ciao` @ `v1.3.0`
- `bonjour-hap` @ `v3.8.0`

## v1.0.0 (2024-07-10)

### Breaking Changes

- **The minimum Node.js version required is now `v18`.**
- **Important notice:** Because of the cleanup of the Deprecated code, you will need to migrate you code base.
  - Remove the long-deprecated init().
  - Deprecate Core, BridgedCore, legacy Camera characteristics. (#1058) (@hjdhjd)
    - For deprecated `Core` and `BridgedCore` see: https://github.com/homebridge/HAP-NodeJS/wiki/Deprecation-of-Core-and-BridgeCore
  - Legacy code deprecation cleanup. (#1059) (@hjdhjd)
    - For deprecated `storagePath` switch to `HAPStorage.setCustomStoragePath`, `AudioCodec` switch to `AudioStreamingCodec`, `VideoCodec` switch to `H264CodecParameters`,`StreamAudioParams` switch to `AudioStreamingOptions`, `StreamVideoParams` switch to `VideoStreamingOptions`,`cameraSource` switch to `CameraController`.
  - Others deprecated code to highlight removed: `useLegacyAdvertiser`, `AccessoryLoader`.
- Fix: Naming for Characteristic.ProgramMode has been corrected from `PROGRAM_SCHEDULED_MANUAL_MODE_` to `PROGRAM_SCHEDULED_MANUAL_MODE`

### Fixed

- Fix: Build Issues (#1041) (@NorthernMan54)
- Fix: Ensure data is only transmitted on open and ready connections. (#1051) (@hjdhjd)
- Fix: Ensure we check names using the full UTF-8 character set. (#1052) (@hjdhjd)
- Fix: ConfiguredName (#1049) (@donavanbecker)
- Fix: Manufacturer looking at checkName but should look at checkValue. (#1053) (@donavanbecker)

### Other Changes (v1.0.0)

- Implement warning messages for invalid characters in names (#1009) (@NorthernMan54)
- Mitigate event emitter "memory leak" warnings when a significant number of camera streaming events occur simultaneously (#1037) (@hjdhjd)
- AdaptiveLightingController fix & improvement (#1038) (@Shaquu)
- Minor fixes to recording logging and one change in logging. (#1040) (@hjdhjd)
- Bridged core and core cleanup (#1048) (@Shaquu)
- Increase snapshot handler warning timeout to 8000ms. (#1055) (@hjdhjd)
- Cleanup and refactor getLocalNetworkInterface and address a potential edge case. (#1056) (@hjdhjd)
- Correct log spacing
- Updated and fixed `typedoc` config file
- Updated dependencies

### Homebridge Dependencies (v1.0.0)

- `@homebridge/ciao` @ `v1.3.0`
- `bonjour-hap` @ `v3.8.0`

## v0.14.1 (2026-02-07)

### Changed

- dependency updates
- update release script for oidc releases

## v0.14.0 (2025-10-29)

### Changed (v0.14.0)

- remove `treatWarningsAsErrors` flag from doc gen
- updated dependencies, fix `Buffer` types
- add node 24 to node engines in `package.json`

### Homebridge Dependencies (v0.14.0)

- `@homebridge/ciao` @ `v1.3.4`
- `bonjour-hap` @ `v3.9.1`

## v0.13.1 (2025-06-04)

*No changes since v0.13.0, just a version bump to trigger a new release.*

### Homebridge Dependencies (v0.13.1)

- `@homebridge/ciao` @ `v1.3.1`
- `bonjour-hap` @ `v3.9.0`

## v0.13.0 (2025-06-04)

### Changed (v0.13.0)

_Most of these commits have been backported from the `v1.x` track. None should be breaking changes._

- Mitigate event emitter "memory leak" warnings when a significant number of HomeKit camera streaming events occur simultaneously. (#1037)
- fix type issue and fix ts build issue
- Correct the formatting and presentation of some recording-related debug and error logging. (#1040)
- AdaptiveLightingController fix & improvement (#1038)
- Bridged core and core cleanup (#1048)
- correct log spacing
- fix: Ensure data is only transmitted on open and ready connections. (#1051)
- Increase snapshot handler warning timeout to 8000ms. (#1055)
- Cleanup and refactor `getLocalNetworkInterface` and address a potential edge case. (#1056)
- add constants for `SecuritySystemAlarmType` (#1086)
- update hk plist file from `V=880` to `V=886` (#1087)
- dependency updates, lint and repo maintenance
- fix OOC errors from `validateUserInput` on steps
- regenerate documentation for new version

### Homebridge Dependencies (v0.13.0)

- `@homebridge/ciao` @ `v1.3.1`
- `bonjour-hap` @ `v3.9.0`

## v0.12.3 (2024-10-26)

### Changed (v0.12.3)

- minor dependency update
- mark compatible with node v22
- fix `initWithServices` reference in typedoc

### Homebridge Dependencies (v0.12.3)

- `@homebridge/ciao` @ `v1.3.0`
- `bonjour-hap` @ `v3.8.0`

## v0.12.2 (2024-05-31)

### Changed (v0.12.2)

- Updated dependencies (`rimraf` and `@types/node`)
- Updated dependencies (`simple-plist`)
- Updated dependencies (`typescript`)

### Homebridge Dependencies (v0.12.2)

- `@homebridge/ciao` @ `v1.2.0`
- `@homebridge/dbus-native` @ `v0.6.0`

## v0.12.1 (2024-05-11)

### Changed (v0.12.1)

- Updated dependencies (`axios` and `commander`)

### Fixed (v0.12.1)

- Mitigate event emitter "memory leak" warnings when a significant number of HSV events occur simultaneously (#1029) (@hjdhjd)

### Other Changes (v0.12.1)

- Update Discord Webhooks to trigger only after published to npm

### Homebridge Dependencies (v0.12.1)

- `@homebridge/ciao` @ `v1.2.0`
- `@homebridge/dbus-native` @ `v0.6.0`

## v0.12.0 (2024-04-19)

### Changed (v0.12.0)

- Create `CHANGELOG.md` file
- Fix: typos + add logo to `README.md`
- Refresh `package-lock.json` (no major changes to dep versions)
- general repo updates
- add alpha releases
- dependency updates
- Fix: typedoc generation
- update homebridge dependencies
- regenerate docs

### Homebridge Dependencies (v0.12.0)

- `@homebridge/ciao` @ `v1.2.0`
- `@homebridge/dbus-native` @ `v0.6.0`
