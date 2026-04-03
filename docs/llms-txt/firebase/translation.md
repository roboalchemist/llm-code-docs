# Source: https://firebase.google.com/docs/ml-kit/translation.md.txt

# Translation

plat_iosplat_android  
| This page describes an old version of the Translation API, which was part of ML Kit for Firebase. Development of this API has been moved to the standalone ML Kit SDK, which you can use with or without Firebase.[Learn more](https://developers.google.com/ml-kit/migration).
|
| See[Translation](https://developers.google.com/ml-kit/language/translation)for the latest documentation.

![](https://firebase.google.com/static/docs/ml-kit/images/on_device_translate@2x.png)

With ML Kit's on-device translation API, you can dynamically translate text between 59 languages.

[iOS](https://firebase.google.com/docs/ml-kit/ios/translate-text)[Android](https://firebase.google.com/docs/ml-kit/android/translate-text)
| This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Broad language support    | Translate between 59 different languages. See the[complete list](https://firebase.google.com/docs/ml-kit/translation-language-support). |
| Proven translation models | Powered by the same models used by the Google Translate app's offline mode.                                                             |
| Dynamic model management  | Keep on-device storage requirements low by dynamically downloading and managing language packs.                                         |
| Runs on the device        | Translations are performed quickly, and don't require you to send users' text to a remote server.                                       |

## Limitations

On-device translation is intended for casual and simple translations, and the quality of translations depends on the specific languages being translated from and to. As such, you should evaluate the quality of the translations for your specific use case. If you require higher fidelity, try the[Cloud Translation API](https://cloud.google.com/translate/).

Also, ML Kit's translation models are trained to translate to and from English. When you translate between non-English languages, English is used as an intermediate translation, which can affect quality.

## Usage guidelines

Refer to[Usage Guidelines for ML Kit On-device Translation](https://firebase.google.com/docs/ml-kit/translation-terms)for important guidelines and restrictions on usage of this API. This document covers requirements around doing attribution in your app when translating text.

## Providing feedback

Due to the complexity of natural language processing, the translations provided might not be appropriate for all contexts or audiences. If you encounter inappropriate translations, reach out to[Firebase support](https://firebase.google.com/support). Your feedback helps to continue to improve the models, and also allows us to disable inappropriate translations.