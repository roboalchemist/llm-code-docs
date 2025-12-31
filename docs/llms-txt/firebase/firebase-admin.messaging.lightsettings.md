# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.lightsettings.md.txt

# LightSettings interface

Represents settings to control notification LED that can be included in [AndroidNotification](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.androidnotification.md#androidnotification_interface).

**Signature:**  

    export interface LightSettings 

## Properties

|                                                                           Property                                                                            |  Type  |                                    Description                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------|
| [color](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.lightsettings.md#lightsettingscolor)                                   | string | Required. Sets color of the LED in `#rrggbb` or `#rrggbbaa` format.               |
| [lightOffDurationMillis](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.lightsettings.md#lightsettingslightoffdurationmillis) | number | Required. Along with `light_on_duration`, defines the blink rate of LED flashes.  |
| [lightOnDurationMillis](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.lightsettings.md#lightsettingslightondurationmillis)   | number | Required. Along with `light_off_duration`, defines the blink rate of LED flashes. |

## LightSettings.color

Required. Sets color of the LED in `#rrggbb` or `#rrggbbaa` format.

**Signature:**  

    color: string;

## LightSettings.lightOffDurationMillis

Required. Along with `light_on_duration`, defines the blink rate of LED flashes.

**Signature:**  

    lightOffDurationMillis: number;

## LightSettings.lightOnDurationMillis

Required. Along with `light_off_duration`, defines the blink rate of LED flashes.

**Signature:**  

    lightOnDurationMillis: number;