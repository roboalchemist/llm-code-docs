# Source: https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md.txt

# GtagConfigParams interface

A set of common Google Analytics config settings recognized by `gtag.js`.

**Signature:**  

    export interface GtagConfigParams 

## Properties

|                                                                             Property                                                                             |  Type   |                                                                                                            Description                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [allow_ad_personalization_signals](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamsallow_ad_personalization_signals) | boolean | If set to false, disables all advertising personalization with `gtag.js`. See [Disable advertising features](https://developers.google.com/analytics/devguides/collection/ga4/display-features)                                   |
| [allow_google_signals](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamsallow_google_signals)                         | boolean | If set to false, disables all advertising features with `gtag.js`. See [Disable advertising features](https://developers.google.com/analytics/devguides/collection/ga4/display-features)                                          |
| [cookie_domain](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamscookie_domain)                                       | string  | Defaults to `auto`. See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)                                                                                       |
| [cookie_expires](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamscookie_expires)                                     | number  | Defaults to 63072000 (two years, in seconds). See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)                                                             |
| [cookie_flags](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamscookie_flags)                                         | string  | Appends additional flags to the cookie when set. See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)                                                          |
| [cookie_prefix](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamscookie_prefix)                                       | string  | Defaults to `_ga`. See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)                                                                                        |
| [cookie_update](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamscookie_update)                                       | boolean | If set to true, will update cookies on each page load. Defaults to true. See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)                                  |
| [page_location](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamspage_location)                                       | string  | The URL of the page. See [Page views](https://developers.google.com/analytics/devguides/collection/ga4/views)                                                                                                                     |
| [page_title](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamspage_title)                                             | string  | The title of the page. See [Page views](https://developers.google.com/analytics/devguides/collection/ga4/views)                                                                                                                   |
| [send_page_view](https://firebase.google.com/docs/reference/js/analytics.gtagconfigparams.md#gtagconfigparamssend_page_view)                                     | boolean | Whether or not a page view should be sent. If set to true (default), a page view is automatically sent upon initialization of analytics. See [Page views](https://developers.google.com/analytics/devguides/collection/ga4/views) |

## GtagConfigParams.allow_ad_personalization_signals

If set to false, disables all advertising personalization with `gtag.js`. See [Disable advertising features](https://developers.google.com/analytics/devguides/collection/ga4/display-features)

**Signature:**  

    'allow_ad_personalization_signals'?: boolean;

## GtagConfigParams.allow_google_signals

If set to false, disables all advertising features with `gtag.js`. See [Disable advertising features](https://developers.google.com/analytics/devguides/collection/ga4/display-features)

**Signature:**  

    'allow_google_signals'?: boolean;

## GtagConfigParams.cookie_domain

Defaults to `auto`. See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)

**Signature:**  

    'cookie_domain'?: string;

## GtagConfigParams.cookie_expires

Defaults to 63072000 (two years, in seconds). See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)

**Signature:**  

    'cookie_expires'?: number;

## GtagConfigParams.cookie_flags

Appends additional flags to the cookie when set. See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)

**Signature:**  

    'cookie_flags'?: string;

## GtagConfigParams.cookie_prefix

Defaults to `_ga`. See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)

**Signature:**  

    'cookie_prefix'?: string;

## GtagConfigParams.cookie_update

If set to true, will update cookies on each page load. Defaults to true. See [Cookies and user identification](https://developers.google.com/analytics/devguides/collection/ga4/cookies-user-id)

**Signature:**  

    'cookie_update'?: boolean;

## GtagConfigParams.page_location

The URL of the page. See [Page views](https://developers.google.com/analytics/devguides/collection/ga4/views)

**Signature:**  

    'page_location'?: string;

## GtagConfigParams.page_title

The title of the page. See [Page views](https://developers.google.com/analytics/devguides/collection/ga4/views)

**Signature:**  

    'page_title'?: string;

## GtagConfigParams.send_page_view

Whether or not a page view should be sent. If set to true (default), a page view is automatically sent upon initialization of analytics. See [Page views](https://developers.google.com/analytics/devguides/collection/ga4/views)

**Signature:**  

    'send_page_view'?: boolean;