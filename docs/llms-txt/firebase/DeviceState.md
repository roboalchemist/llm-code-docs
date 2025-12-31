# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceState.md.txt

# DeviceState

The state displayed with the ADB Device when running "adb devices"

|                                    Enums                                    ||
|----------------------------|-------------------------------------------------|
| `DEVICE_STATE_UNSPECIFIED` | The device state is unknown.                    |
| `DEVICE`                   | The ADB device is in the "device" status.       |
| `RECOVERY`                 | The ADB device is in the "recovery" status.     |
| `RESCUE`                   | The ADB device is in the "rescue" status.       |
| `SIDELOAD`                 | The ADB device is in the "sideload" status.     |
| `MISSING`                  | The ADB device is in the "missing" status.      |
| `OFFLINE`                  | The ADB device is in the "offline" status.      |
| `UNAUTHORIZED`             | The ADB device is in the "unauthorized" status. |
| `AUTHORIZING`              | The ADB device is in the "authorizing" status.  |
| `CONNECTING`               | The ADB device is in the "connecting" status.   |