# Source: https://firebase.google.com/docs/reference/js/analytics.controlparams.md.txt

# ControlParams interface

Standard `gtag.js` control parameters. For more information, see [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

**Signature:**  

    export interface ControlParams 

## Properties

|                                                        Property                                                        |         Type         | Description |
|------------------------------------------------------------------------------------------------------------------------|----------------------|-------------|
| [event_callback](https://firebase.google.com/docs/reference/js/analytics.controlparams.md#controlparamsevent_callback) | () =\> void          |             |
| [event_timeout](https://firebase.google.com/docs/reference/js/analytics.controlparams.md#controlparamsevent_timeout)   | number               |             |
| [groups](https://firebase.google.com/docs/reference/js/analytics.controlparams.md#controlparamsgroups)                 | string \| string\[\] |             |
| [send_to](https://firebase.google.com/docs/reference/js/analytics.controlparams.md#controlparamssend_to)               | string \| string\[\] |             |

## ControlParams.event_callback

**Signature:**  

    event_callback?: () => void;

## ControlParams.event_timeout

**Signature:**  

    event_timeout?: number;

## ControlParams.groups

**Signature:**  

    groups?: string | string[];

## ControlParams.send_to

**Signature:**  

    send_to?: string | string[];