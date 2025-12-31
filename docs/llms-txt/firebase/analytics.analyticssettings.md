# Source: https://firebase.google.com/docs/reference/js/analytics.analyticssettings.md.txt

# AnalyticsSettings interface

[Analytics](https://firebase.google.com/docs/reference/js/analytics.analytics.md#analytics_interface) instance initialization options.

**Signature:**  

    export interface AnalyticsSettings 

## Properties

|                                                    Property                                                    |                                                                                                                   Type                                                                                                                    |                                           Description                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [config](https://firebase.google.com/docs/reference/js/analytics.analyticssettings.md#analyticssettingsconfig) | [GtagConfigParams](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparams_interface) \| [EventParams](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparams_interface) | Params to be passed in the initial `gtag` config call during Firebase Analytics initialization. |

## AnalyticsSettings.config

Params to be passed in the initial `gtag` config call during Firebase Analytics initialization.

**Signature:**  

    config?: GtagConfigParams | EventParams;