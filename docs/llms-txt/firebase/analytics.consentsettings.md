# Source: https://firebase.google.com/docs/reference/js/analytics.consentsettings.md.txt

# ConsentSettings interface

Consent status settings for each consent type. For more information, see [the GA4 reference documentation for consent state and consent types](https://developers.google.com/tag-platform/tag-manager/templates/consent-apis).

**Signature:**  

    export interface ConsentSettings 

## Properties

|                                                                   Property                                                                   |                                                 Type                                                  |                                                      Description                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [ad_personalization](https://firebase.google.com/docs/reference/js/analytics.consentsettings.md#consentsettingsad_personalization)           | [ConsentStatusString](https://firebase.google.com/docs/reference/js/analytics.md#consentstatusstring) | Sets consent for personalized advertising.                                                                             |
| [ad_storage](https://firebase.google.com/docs/reference/js/analytics.consentsettings.md#consentsettingsad_storage)                           | [ConsentStatusString](https://firebase.google.com/docs/reference/js/analytics.md#consentstatusstring) | Enables storage, such as cookies, related to advertising                                                               |
| [ad_user_data](https://firebase.google.com/docs/reference/js/analytics.consentsettings.md#consentsettingsad_user_data)                       | [ConsentStatusString](https://firebase.google.com/docs/reference/js/analytics.md#consentstatusstring) | Sets consent for sending user data to Google for advertising purposes.                                                 |
| [analytics_storage](https://firebase.google.com/docs/reference/js/analytics.consentsettings.md#consentsettingsanalytics_storage)             | [ConsentStatusString](https://firebase.google.com/docs/reference/js/analytics.md#consentstatusstring) | Enables storage, such as cookies, related to analytics (for example, visit duration)                                   |
| [functionality_storage](https://firebase.google.com/docs/reference/js/analytics.consentsettings.md#consentsettingsfunctionality_storage)     | [ConsentStatusString](https://firebase.google.com/docs/reference/js/analytics.md#consentstatusstring) | Enables storage that supports the functionality of the website or app such as language settings                        |
| [personalization_storage](https://firebase.google.com/docs/reference/js/analytics.consentsettings.md#consentsettingspersonalization_storage) | [ConsentStatusString](https://firebase.google.com/docs/reference/js/analytics.md#consentstatusstring) | Enables storage related to personalization such as video recommendations                                               |
| [security_storage](https://firebase.google.com/docs/reference/js/analytics.consentsettings.md#consentsettingssecurity_storage)               | [ConsentStatusString](https://firebase.google.com/docs/reference/js/analytics.md#consentstatusstring) | Enables storage related to security such as authentication functionality, fraud prevention, and other user protection. |

## ConsentSettings.ad_personalization

Sets consent for personalized advertising.

**Signature:**  

    ad_personalization?: ConsentStatusString;

## ConsentSettings.ad_storage

Enables storage, such as cookies, related to advertising

**Signature:**  

    ad_storage?: ConsentStatusString;

## ConsentSettings.ad_user_data

Sets consent for sending user data to Google for advertising purposes.

**Signature:**  

    ad_user_data?: ConsentStatusString;

## ConsentSettings.analytics_storage

Enables storage, such as cookies, related to analytics (for example, visit duration)

**Signature:**  

    analytics_storage?: ConsentStatusString;

## ConsentSettings.functionality_storage

Enables storage that supports the functionality of the website or app such as language settings

**Signature:**  

    functionality_storage?: ConsentStatusString;

## ConsentSettings.personalization_storage

Enables storage related to personalization such as video recommendations

**Signature:**  

    personalization_storage?: ConsentStatusString;

## ConsentSettings.security_storage

Enables storage related to security such as authentication functionality, fraud prevention, and other user protection.

**Signature:**  

    security_storage?: ConsentStatusString;