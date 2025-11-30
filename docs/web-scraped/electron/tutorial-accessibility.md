# Source: https://www.electronjs.org/docs/latest/tutorial/accessibility

On this page

# Accessibility

Accessibility concerns in Electron applications are similar to those of websites because they\'re both ultimately HTML.

## Manually enabling accessibility features[â€‹](#manually-enabling-accessibility-features "Direct link to Manually enabling accessibility features") 

Electron applications will automatically enable accessibility features in the presence of assistive technology (e.g. [JAWS](https://www.freedomscientific.com/products/software/jaws/) on Windows or [VoiceOver](https://help.apple.com/voiceover/mac/10.15/) on macOS). See Chrome\'s [accessibility documentation](https://www.chromium.org/developers/design-documents/accessibility#TOC-How-Chrome-detects-the-presence-of-Assistive-Technology) for more details.

You can also manually toggle these features either within your Electron application or by setting flags in third-party native software.

### Using Electron\'s API[â€‹](#using-electrons-api "Direct link to Using Electron's API") 

By using the [`app.setAccessibilitySupportEnabled(enabled)`](/docs/latest/api/app#appsetaccessibilitysupportenabledenabled-macos-windows) API, you can manually expose Chrome\'s accessibility tree to users in the application preferences. Note that the user\'s system assistive utilities have priority over this setting and will override it.

### Within third-party software[â€‹](#within-third-party-software "Direct link to Within third-party software") 

#### macOS[â€‹](#macos "Direct link to macOS") 

On macOS, third-party assistive technology can toggle accessibility features inside Electron applications by setting the `AXManualAccessibility` attribute programmatically:

Using Objective-C:

``` 
CFStringRef kAXManualAccessibility = CFSTR("AXManualAccessibility");

+ (void)enableAccessibility:(BOOL)enable inElectronApplication:(NSRunningApplication *)app

```

Using Swift:

``` 
import Cocoa
let name = CommandLine.arguments.count >= 2 ? CommandLine.arguments[1] : "Electron"
let pid = NSWorkspace.shared.runningApplications.first(where: )!.processIdentifier
let axApp = AXUIElementCreateApplication(pid)
let result = AXUIElementSetAttributeValue(axApp, "AXManualAccessibility" as CFString, true as CFTypeRef)
print("Setting 'AXManualAccessibility' \(error.rawValue == 0 ? "succeeded" : "failed")")
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/accessibility.md)