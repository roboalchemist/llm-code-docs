# Source: https://firebase.google.com/docs/ml-kit/identify-languages.md.txt

# Language Identification

> [!CAUTION]
> This page describes an old version of the Language Identification API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Language Identification](https://developers.google.com/ml-kit/language/identification)
> for the latest documentation.

![](https://firebase.google.com/static/docs/ml-kit/images/language_detection@2x.png)

With ML Kit's on-device language identification API, you can determine the
language of a string of text.

Language identification can be useful when working with user-provided text,
which often doesn't come with any language information.

[iOS](https://firebase.google.com/docs/ml-kit/ios/identify-languages)
[Android](https://firebase.google.com/docs/ml-kit/android/identify-languages)
This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|---|---|
| Broad language support | Identifies over a hundred different languages. See the [complete list](https://firebase.google.com/docs/ml-kit/langid-support). |
| Romanized text support | Identifies Arabic, Bulgarian, Greek, Hindi, Japanese, Russian, and Chinese text in both native and romanized script. |

## Example results

| Simple language identification ||
|---|---|
| "My hovercraft is full of eels." | `en` (English) |
| "Dao shan xue hai" | `zh-Latn` (Latinized Chinese) |
| "ph'nglui mglw'nafh TensorFlow Google wgah'nagl fhtagn" | `und` (undetermined) |

| Confidence distribution ||
|---|---|
| "an amicable coup d'etat" | `en` (0.52) `fr` (0.44) `ca` (0.03) |