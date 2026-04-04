# Source: https://firebase.google.com/docs/reference/js/analytics.settingsoptions.md.txt

# SettingsOptions interface

Specifies custom options for your Firebase Analytics instance. You must set these before initializing `firebase.analytics()`.

**Signature:**  

    export interface SettingsOptions 

## Properties

|                                                         Property                                                         |  Type  |                        Description                        |
|--------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------|
| [dataLayerName](https://firebase.google.com/docs/reference/js/analytics.settingsoptions.md#settingsoptionsdatalayername) | string | Sets custom name for `dataLayer` array used by `gtag.js`. |
| [gtagName](https://firebase.google.com/docs/reference/js/analytics.settingsoptions.md#settingsoptionsgtagname)           | string | Sets custom name for `gtag` function.                     |

## SettingsOptions.dataLayerName

Sets custom name for `dataLayer` array used by `gtag.js`.

**Signature:**  

    dataLayerName?: string;

## SettingsOptions.gtagName

Sets custom name for `gtag` function.

**Signature:**  

    gtagName?: string;