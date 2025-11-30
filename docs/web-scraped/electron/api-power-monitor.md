# Source: https://www.electronjs.org/docs/latest/api/power-monitor

On this page

# powerMonitor

> Monitor power state changes.

Process: [Main](/docs/latest/glossary#main-process)

## Events[â€‹](#events "Direct link to Events") 

The `powerMonitor` module emits the following events:

### Event: \'suspend\'[â€‹](#event-suspend "Direct link to Event: 'suspend'") 

Emitted when the system is suspending.

### Event: \'resume\'[â€‹](#event-resume "Direct link to Event: 'resume'") 

Emitted when system is resuming.

### Event: \'on-ac\' *macOS* *Windows*[â€‹](#event-on-ac-macos-windows "Direct link to event-on-ac-macos-windows") 

Emitted when the system changes to AC power.

### Event: \'on-battery\' *macOS* *Windows*[â€‹](#event-on-battery-macos--windows "Direct link to event-on-battery-macos--windows") 

Emitted when system changes to battery power.

### Event: \'thermal-state-change\' *macOS*[â€‹](#event-thermal-state-change-macos "Direct link to event-thermal-state-change-macos") 

Returns:

- `details` Event\<\>
  - `state` string - The system\'s new thermal state. Can be `unknown`, `nominal`, `fair`, `serious`, `critical`.

Emitted when the thermal state of the system changes. Notification of a change in the thermal status of the system, such as entering a critical temperature range. Depending on the severity, the system might take steps to reduce said temperature, for example, throttling the CPU or switching on the fans if available.

Apps may react to the new state by reducing expensive computing tasks (e.g. video encoding), or notifying the user. The same state might be received repeatedly.

See [https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/RespondToThermalStateChanges.html](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/RespondToThermalStateChanges.html)

### Event: \'speed-limit-change\' *macOS* *Windows*[â€‹](#event-speed-limit-change-macos-windows "Direct link to event-speed-limit-change-macos-windows") 

Returns:

- `details` Event\<\>
  - `limit` number - The operating system\'s advertised speed limit for CPUs, in percent.

Notification of a change in the operating system\'s advertised speed limit for CPUs, in percent. Values below 100 indicate that the system is impairing processing power due to thermal management.

### Event: \'shutdown\' *Linux* *macOS*[â€‹](#event-shutdown-linux-macos "Direct link to event-shutdown-linux-macos") 

Emitted when the system is about to reboot or shut down. If the event handler invokes `e.preventDefault()`, Electron will attempt to delay system shutdown in order for the app to exit cleanly. If `e.preventDefault()` is called, the app should exit as soon as possible by calling something like `app.quit()`.

### Event: \'lock-screen\' *macOS* *Windows*[â€‹](#event-lock-screen-macos-windows "Direct link to event-lock-screen-macos-windows") 

Emitted when the system is about to lock the screen.

### Event: \'unlock-screen\' *macOS* *Windows*[â€‹](#event-unlock-screen-macos-windows "Direct link to event-unlock-screen-macos-windows") 

Emitted as soon as the systems screen is unlocked.

### Event: \'user-did-become-active\' *macOS*[â€‹](#event-user-did-become-active-macos "Direct link to event-user-did-become-active-macos") 

Emitted when a login session is activated. See [documentation](https://developer.apple.com/documentation/appkit/nsworkspacesessiondidbecomeactivenotification?language=objc) for more information.

### Event: \'user-did-resign-active\' *macOS*[â€‹](#event-user-did-resign-active-macos "Direct link to event-user-did-resign-active-macos") 

Emitted when a login session is deactivated. See [documentation](https://developer.apple.com/documentation/appkit/nsworkspacesessiondidresignactivenotification?language=objc) for more information.

## Methods[â€‹](#methods "Direct link to Methods") 

The `powerMonitor` module has the following methods:

### `powerMonitor.getSystemIdleState(idleThreshold)`[â€‹](#powermonitorgetsystemidlestateidlethreshold "Direct link to powermonitorgetsystemidlestateidlethreshold") 

- `idleThreshold` Integer

Returns `string` - The system\'s current idle state. Can be `active`, `idle`, `locked` or `unknown`.

Calculate the system idle state. `idleThreshold` is the amount of time (in seconds) before considered idle. `locked` is available on supported systems only.

### `powerMonitor.getSystemIdleTime()`[â€‹](#powermonitorgetsystemidletime "Direct link to powermonitorgetsystemidletime") 

Returns `Integer` - Idle time in seconds

Calculate system idle time in seconds.

### `powerMonitor.getCurrentThermalState()` *macOS*[â€‹](#powermonitorgetcurrentthermalstate-macos "Direct link to powermonitorgetcurrentthermalstate-macos") 

Returns `string` - The system\'s current thermal state. Can be `unknown`, `nominal`, `fair`, `serious`, or `critical`.

### `powerMonitor.isOnBatteryPower()`[â€‹](#powermonitorisonbatterypower "Direct link to powermonitorisonbatterypower") 

Returns `boolean` - Whether the system is on battery power.

To monitor for changes in this property, use the `on-battery` and `on-ac` events.

## Properties[â€‹](#properties "Direct link to Properties") 

### `powerMonitor.onBatteryPower`[â€‹](#powermonitoronbatterypower "Direct link to powermonitoronbatterypower") 

A `boolean` property. True if the system is on battery power.

See [`powerMonitor.isOnBatteryPower()`](#powermonitorisonbatterypower).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/power-monitor.md)