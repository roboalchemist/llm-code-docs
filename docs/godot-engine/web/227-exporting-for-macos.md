# Exporting for macOS

# Exporting for macOS
See also
This page describes how to export a Godot project to macOS.
If you're looking to compile editor or export template binaries from source instead,
readCompiling for macOS.
macOS apps exported with the official export templates are exported as a single "Universal 2" binary.appbundle, a folder with a specific structure which stores the executable, libraries and all the project files.
This bundle can be exported as is, packed in a ZIP archive, or packed in a DMG disk image (only supported when exporting from macOS).Universal binaries for macOS support both Intel x86_64 and ARM64 (Apple Silicon) architectures.
Warning
Due to file system limitations,.appbundles exported from Windows lack theexecutableflag and won't run on macOS. Projects exported as.zipare not
affected by this issue. To run.appbundles exported from Windows on macOS,
transfer the.appto a device running macOS or Linux and use thechmod+x{executable_name}terminal command to add theexecutablepermission.
The main executable located in theContents/MacOS/subfolder, as well
as optional helper executables in theContents/Helpers/subfolder, should have
theexecutablepermission for the.appbundle to be valid.

## Requirements
- Download the Godot export templates. Use the Godot menu:Editor>ManageExportTemplates.
Download the Godot export templates. Use the Godot menu:Editor>ManageExportTemplates.
- A valid and uniqueBundleidentifiershould be set in theApplicationsection of the export options.
A valid and uniqueBundleidentifiershould be set in theApplicationsection of the export options.
Warning
Projects exported without code signing and notarization will be blocked by Gatekeeper if they are downloaded from unknown sources, see theRunning Godot apps on macOSpage for more information.

## Code signing and notarization
By default, macOS will run only applications that are signed and notarized. If you use any other signing configuration, seeRunning Godot apps on macOSfor workarounds.
To notarize an app, youmusthave a validApple Developer ID Certificate.

### If you have an Apple Developer ID Certificate and exporting from macOS
InstallXcodecommand line tools and open Xcode at least once or run thesudoxcodebuild-licenseacceptcommand to accept license agreement.

#### To sign exported app
- SelectXcodecodesignin theCodeSigning>Codesignoption.
SelectXcodecodesignin theCodeSigning>Codesignoption.
- Set valid Apple ID certificate identity (certificate "Common Name") in theCodeSigning>Identitysection.
Set valid Apple ID certificate identity (certificate "Common Name") in theCodeSigning>Identitysection.

#### To notarize exported app
- SelectXcodealtoolin theNotarization>Notarizationoption.
SelectXcodealtoolin theNotarization>Notarizationoption.
- Disable theDebuggingentitlement.
Disable theDebuggingentitlement.
- Set valid Apple ID login / app. specific password orApp Store ConnectAPI UUID / Key in theNotarizationsection.
Set valid Apple ID login / app. specific password orApp Store ConnectAPI UUID / Key in theNotarizationsection.
You can use thexcrunnotarytoolhistorycommand to check notarization status and use thexcrunnotarytoollog{ID}command to download the notarization log.
If you encounter notarization issues, seeResolving common notarization issuesfor more info.
After notarization is completed,staple the ticketto the exported project.

### If you have an Apple Developer ID Certificate and exporting from Linux or Windows
InstallPyOxidizer rcodesign, and configure the path torcodesignin theEditorSettings>Export>macOS>rcodesign.

#### To sign exported app
- SelectPyOxidizerrcodesignin theCodeSigning>Codesignoption.
SelectPyOxidizerrcodesignin theCodeSigning>Codesignoption.
- Set valid Apple ID PKCS #12 certificate file and password in theCodeSigningsection.
Set valid Apple ID PKCS #12 certificate file and password in theCodeSigningsection.

#### To notarize exported app
- SelectPyOxidizerrcodesignin theNotarization>Notarizationoption.
SelectPyOxidizerrcodesignin theNotarization>Notarizationoption.
- Disable theDebuggingentitlement.
Disable theDebuggingentitlement.
- Set validApp Store ConnectAPI UUID / Key in theNotarizationsection.
Set validApp Store ConnectAPI UUID / Key in theNotarizationsection.
You can use thercodesignnotary-logcommand to check notarization status.
After notarization is completed, use thercodesignstaplecommand to staple the ticket to the exported project.

### If you do not have an Apple Developer ID Certificate
- SelectBuilt-in(ad-hoconly)in theCodeSigning>Codesignoption.
SelectBuilt-in(ad-hoconly)in theCodeSigning>Codesignoption.
- SelectDisabledin theNotarization>Notarizationoption.
SelectDisabledin theNotarization>Notarizationoption.
In this case Godot will use an ad-hoc signature, which will make running an exported app easier for the end users,
see theRunning Godot apps on macOSpage for more information.

### Signing Options

| Option | Description |
|---|---|
| Codesign | Tool to use for code signing. |
| Identity | The "Full Name" or "Common Name" of the signing identity, store in the macOS keychain.[1] |
| Certificate File | The PKCS #12 certificate file.[2] |
| Certificate Password | Password for the certificate file.[2] |
| Custom Options | Array of command line arguments passed to the code signing tool. |

Option
Description
Codesign
Tool to use for code signing.
Identity
The "Full Name" or "Common Name" of the signing identity, store in the macOS keychain.[1]
Certificate File
The PKCS #12 certificate file.[2]
Certificate Password
Password for the certificate file.[2]
Custom Options
Array of command line arguments passed to the code signing tool.
This option is visible only when signing with Xcode codesign.
These options are visible only when signing with PyOxidizer rcodesign.

### Notarization Options

| Option | Description |
|---|---|
| Notarization | Tool to use for notarization. |
| Apple ID Name | Apple ID account name (email address).[3] |
| Apple ID Password | Apple ID app-specific password. SeeUsing app-specific passwordsto enable two-factor authentication and create app password.[3] |
| Apple Team ID | Team ID ("Organization Unit"), if your Apple ID belongs to multiple teams (optional).[3] |
| API UUID | AppleApp Store ConnectAPI issuer UUID. |
| API Key | AppleApp Store ConnectAPI key. |

Option
Description
Notarization
Tool to use for notarization.
Apple ID Name
Apple ID account name (email address).[3]
Apple ID Password
Apple ID app-specific password. SeeUsing app-specific passwordsto enable two-factor authentication and create app password.[3]
Apple Team ID
Team ID ("Organization Unit"), if your Apple ID belongs to multiple teams (optional).[3]
API UUID
AppleApp Store ConnectAPI issuer UUID.
API Key
AppleApp Store ConnectAPI key.
Note
You should set either Apple ID Name/Password or App Store Connect API UUID/Key.
These options are visible only when notarizing with Xcode altool.
SeeNotarizing macOS Software Before Distributionfor more info.

## Entitlements

### Hardened Runtime Entitlements
Hardened Runtime entitlements manage security options and resource access policy.
SeeHardened Runtimefor more info.

| Entitlement | Description |
|---|---|
| Allow JIT Code Execution[4] | Allows creating writable and executable memory for JIT code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. |
| Allow Unsigned Executable Memory[4] | Allows creating writable and executable memory without JIT restrictions. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. |
| Allow DYLD Environment Variables[4] | Allows app to uss dynamic linker environment variables to inject code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation. |
| Disable Library Validation | Allows app to load arbitrary libraries and frameworks. Enable it if you are using GDExtension add-ons or ad-hoc signing, or want to support user-provided external add-ons. |
| Audio Input | Enable if you need to use the microphone or other audio input sources, if it's enabled you should also provide usage message in theprivacy/microphone_usage_descriptionoption. |
| Camera | Enable if you need to use the camera, if it's enabled you should also provide usage message in theprivacy/camera_usage_descriptionoption. |
| Location | Enable if you need to use location information from Location Services, if it's enabled you should also provide usage message in theprivacy/location_usage_descriptionoption. |
| Address Book | [5]Enable to allow access contacts in the user's address book, if it's enabled you should also provide usage message in theprivacy/address_book_usage_descriptionoption. |
| Calendars | [5]Enable to allow access to the user's calendar, if it's enabled you should also provide usage message in theprivacy/calendar_usage_descriptionoption. |
| Photo Library | [5]Enable to allow access to the user's Photos library, if it's enabled you should also provide usage message in theprivacy/photos_library_usage_descriptionoption. |
| Apple Events | [5]Enable to allow app to send Apple events to other apps. |
| Debugging | [6]You can temporarily enable this entitlement to use native debugger (GDB, LLDB) with the exported app. This entitlement should be disabled for production export. |

Entitlement
Description
Allow JIT Code Execution[4]
Allows creating writable and executable memory for JIT code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation.
Allow Unsigned Executable Memory[4]
Allows creating writable and executable memory without JIT restrictions. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation.
Allow DYLD Environment Variables[4]
Allows app to uss dynamic linker environment variables to inject code. If you are using add-ons with dynamic or self-modifying native code, enable them according to the add-on documentation.
Disable Library Validation
Allows app to load arbitrary libraries and frameworks. Enable it if you are using GDExtension add-ons or ad-hoc signing, or want to support user-provided external add-ons.
Audio Input
Enable if you need to use the microphone or other audio input sources, if it's enabled you should also provide usage message in theprivacy/microphone_usage_descriptionoption.
Camera
Enable if you need to use the camera, if it's enabled you should also provide usage message in theprivacy/camera_usage_descriptionoption.
Location
Enable if you need to use location information from Location Services, if it's enabled you should also provide usage message in theprivacy/location_usage_descriptionoption.
Address Book
[5]Enable to allow access contacts in the user's address book, if it's enabled you should also provide usage message in theprivacy/address_book_usage_descriptionoption.
Calendars
[5]Enable to allow access to the user's calendar, if it's enabled you should also provide usage message in theprivacy/calendar_usage_descriptionoption.
Photo Library
[5]Enable to allow access to the user's Photos library, if it's enabled you should also provide usage message in theprivacy/photos_library_usage_descriptionoption.
Apple Events
[5]Enable to allow app to send Apple events to other apps.
Debugging
[6]You can temporarily enable this entitlement to use native debugger (GDB, LLDB) with the exported app. This entitlement should be disabled for production export.
TheAllowJITCodeExecution,AllowUnsignedExecutableMemoryandAllowDYLDEnvironmentVariablesentitlements are always enabled for the Godot Mono exports, and are not visible in the export options.
These features aren't supported by Godot out of the box, enable them only if you are using add-ons which require them.
To notarize an app, you must disable theDebuggingentitlement.

### App Sandbox Entitlement
The App Sandbox restricts access to user data, networking and devices.
Sandboxed apps can't access most of the file system, can't use custom file dialogs and execute binaries (usingOS.executeandOS.create_process) outside the.appbundle.
SeeApp Sandboxfor more info.
Note
To distribute an app through the App Store, you must enable the App Sandbox.

| Entitlement | Description |
|---|---|
| Enabled | Enables App Sandbox. |
| Network Server | Enable to allow app to listen for incoming network connections. |
| Network Client | Enable to allow app to establish outgoing network connections. |
| Device USB | Enable to allow app to interact with USB devices. This entitlement is required to use wired controllers. |
| Device Bluetooth | Enable to allow app to interact with Bluetooth devices. This entitlement is required to use wireless controllers. |
| Files Downloads[7] | Allows read or write access to the user's "Downloads" folder. |
| Files Pictures[7] | Allows read or write access to the user's "Pictures" folder. |
| Files Music[7] | Allows read or write access to the user's "Music" folder. |
| Files Movies[7] | Allows read or write access to the user's "Movies" folder. |
| Files User Selected[7] | Allows read or write access to arbitrary folder. To gain access, a folder must be selected from the native file dialog by the user. |
| Helper Executable | List of helper executables to embedded to the app bundle. Sandboxed app are limited to execute only these executable. |

Entitlement
Description
Enabled
Enables App Sandbox.
Network Server
Enable to allow app to listen for incoming network connections.
Network Client
Enable to allow app to establish outgoing network connections.
Device USB
Enable to allow app to interact with USB devices. This entitlement is required to use wired controllers.
Device Bluetooth
Enable to allow app to interact with Bluetooth devices. This entitlement is required to use wireless controllers.
Files Downloads[7]
Allows read or write access to the user's "Downloads" folder.
Files Pictures[7]
Allows read or write access to the user's "Pictures" folder.
Files Music[7]
Allows read or write access to the user's "Music" folder.
Files Movies[7]
Allows read or write access to the user's "Movies" folder.
Files User Selected[7]
Allows read or write access to arbitrary folder. To gain access, a folder must be selected from the native file dialog by the user.
Helper Executable
List of helper executables to embedded to the app bundle. Sandboxed app are limited to execute only these executable.
You can optionally provide usage messages for various folders in theprivacy/*_folder_usage_descriptionoptions.
Note
You can override default entitlements by selecting custom entitlements file, in this case all other entitlement are ignored.

## Environment variables
You can use the following environment variables to set export options outside of
the editor. During the export process, these override the values that you set in
the export menu.

| Export option | Environment variable |
|---|---|
| Encryption / Encryption Key | GODOT_SCRIPT_ENCRYPTION_KEY |
| Options / Codesign / Certificate File | GODOT_MACOS_CODESIGN_CERTIFICATE_FILE |
| Options / Codesign / Certificate Password | GODOT_MACOS_CODESIGN_CERTIFICATE_PASSWORD |
| Options / Codesign / Provisioning Profile | GODOT_MACOS_CODESIGN_PROVISIONING_PROFILE |
| Options / Notarization / API UUID | GODOT_MACOS_NOTARIZATION_API_UUID |
| Options / Notarization / API Key | GODOT_MACOS_NOTARIZATION_API_KEY |
| Options / Notarization / API Key ID | GODOT_MACOS_NOTARIZATION_API_KEY_ID |
| Options / Notarization / Apple ID Name | GODOT_MACOS_NOTARIZATION_APPLE_ID_NAME |
| Options / Notarization / Apple ID Password | GODOT_MACOS_NOTARIZATION_APPLE_ID_PASSWORD |

Export option
Environment variable
Encryption / Encryption Key
GODOT_SCRIPT_ENCRYPTION_KEY
Options / Codesign / Certificate File
GODOT_MACOS_CODESIGN_CERTIFICATE_FILE
Options / Codesign / Certificate Password
GODOT_MACOS_CODESIGN_CERTIFICATE_PASSWORD
Options / Codesign / Provisioning Profile
GODOT_MACOS_CODESIGN_PROVISIONING_PROFILE
Options / Notarization / API UUID
GODOT_MACOS_NOTARIZATION_API_UUID
Options / Notarization / API Key
GODOT_MACOS_NOTARIZATION_API_KEY
Options / Notarization / API Key ID
GODOT_MACOS_NOTARIZATION_API_KEY_ID
Options / Notarization / Apple ID Name
GODOT_MACOS_NOTARIZATION_APPLE_ID_NAME
Options / Notarization / Apple ID Password
GODOT_MACOS_NOTARIZATION_APPLE_ID_PASSWORD

## Export options
You can find a full list of export options available in theEditorExportPlatformMacOSclass reference.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.