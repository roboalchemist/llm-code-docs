# Source: https://firebase.google.com/docs/ml-kit/recognize-text.md.txt

# Text Recognition

> [!CAUTION]
> This page describes an old version of the Text Recognition API, which was part
> of ML Kit for Firebase. The functionality of this API has been split into
> two new APIs ([learn more](https://developers.google.com/ml-kit/migration)):
>
> - [On-device text recognition](https://developers.google.com/ml-kit/vision/text-recognition) is part of the new standalone ML Kit SDK, which you can use with or without Firebase.
> - [Cloud text recognition](https://firebase.google.com/docs/ml/recognize-text) is part of Firebase ML, which includes all of Firebase's cloud-based ML features.

![](https://firebase.google.com/static/docs/ml-kit/images/text_recognition@2x.png)

With ML Kit's text recognition APIs, you can recognize text in any
Latin-based language ([and more, with Cloud-based text recognition](https://cloud.google.com/vision/docs/languages)).

Text recognition can automate tedious data entry for credit cards, receipts, and
business cards. With the Cloud-based API, you can also
extract text from pictures of documents, which you can use to increase
accessibility or translate documents. Apps can even keep track of real-world
objects, such as by reading the numbers on trains.

[iOS](https://firebase.google.com/docs/ml-kit/ios/recognize-text)
[Android](https://firebase.google.com/docs/ml-kit/android/recognize-text)

If you're a Flutter developer, you might be interested in
[FlutterFire](https://github.com/FirebaseExtended/flutterfire/tree/master/packages/firebase_ml_vision),
which includes a plugin for Firebase's ML Vision APIs.
This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Choose between on-device and Cloud APIs

|   | On-device | Cloud |
| Pricing | Free | Free for first 1000 uses of this feature per month: see [Pricing](https://firebase.google.com/pricing) |
| Ideal use cases | Real-time processing---ideal for a camera or video feed Recognizing sparse text in images | High-accuracy text recognition Recognizing sparse text in images Recognizing densely-spaced text in pictures of documents See the [Cloud Vision API demo](https://cloud.google.com/vision/docs/drag-and-drop). |
| Language support | Recognizes Latin characters | Recognizes and identifies a broad range of languages and special characters |
|---|---|---|

## Example results

### Sparse text

![](https://firebase.google.com/static/docs/ml-kit/images/examples/Wege_der_parlamentarischen_Demokratie.jpg) Photo: [Dietmar Rabich](https://commons.wikimedia.org/wiki/User:XRay "User:XRay") / [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page "Main Page") / ["Düsseldorf, Wege der parlamentarischen Demokratie -- 2015 -- 8123"](https://commons.wikimedia.org/wiki/File:D%C3%BCsseldorf,_Wege_der_parlamentarischen_Demokratie_--_2015_--_8123.jpg) / [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

| Recognized Text ||
| Text | `Wege der parlamentarischen Demokratie` |
| Blocks | (1 block) |
|---|---|

| Block 0 ||
| Text | `Wege der parlamentarischen Demokratie` |
| Frame | (117.0, 258.0, 190.0, 83.0) |
| Corner Points | (117, 270), (301.64, 258.49), (306.05, 329.36), (121.41, 340.86) |
| Recognized Language Code | de |
| Lines | (3 lines) |
|---|---|

| Line 0 ||
| Text | `Wege der` |
| Frame | (167.0, 261.0, 91.0, 28.0) |
| Corner Points | (167, 267), (255.82, 261.46), (257.19, 283.42), (168.36, 288.95) |
| Recognized Language Code | de |
| Elements | (2 elements) |
|---|---|

| Element 0 ||
| Text | `Wege` |
| Frame | (167.0, 263.0, 59.0, 26.0) |
| Corner Points | (167, 267), (223.88, 263.45), (225.25, 285.41), (168.36, 288.95) |
|---|---|

### Document text

![](https://firebase.google.com/static/docs/ml-kit/images/examples/dracula_p361.jpg)

| Recognized Text ||
| Text | `DR. SEWARD'S DIARY 361 Professor. He had evidently expected some such call, for I found him dressed in his room. His door was ajar, so that he could hear the opening of the door of our room. He came at once; as he passed into the room, he asked Mina if the others might come, too. "No," she said quite simply, "it will not be necessary. You can tell them just as well. I must go with you on your journey." Dr. Van Helsing was as startled as I was. After a mo- ment's pause he asked: "But why?"` ... (full text) |
| Blocks | (1 block) |
|---|---|

| Block 0 ||
| Text | `DR . SEWARD ' S DIARY 361 Professor . He had evidently expected some such call , for I found him dressed in his room . His door was ajar , so that he could hear the opening of the door of our room . He came at once ; as he passed into the room , he asked Mina if the others might come , too .` `" No , " she said quite simply , " it will not be necessary . You can tell them just as well . I must go with you on your journey . "` `Dr . Van Helsing was as startled as I was . After a mo ment ' s pause he asked :` ... (full text) |
| Confidence | 0.98 |
| Frame | (25.0, 21.0, 359.0, 583.0) |
| Recognized Language Code | en |
| Paragraphs | (10 paragraphs) |
|---|---|

| Paragraph 1 ||
| Text | `" No , " she said quite simply , " it will not be necessary . You can tell them just as well . I must go with you on your journey . "` |
| Confidence | 0.98 |
| Frame | (29.0, 110.0, 355.0, 44.0) |
| Recognized Language Code | en |
| Words | (34 words) |
|---|---|

| Word 7 ||
| Text | `simply` |
| Confidence | 0.99 |
| Frame | (179.0, 110.0, 37.0, 15.0) |
| Recognized Language Code | en |
| Symbols | (6 symbols) |
|---|---|

| Symbol 0 ||
| Text | `s` |
| Confidence | 1.00 |
| Frame | (179.0, 110.0, 3.0, 15.0) |
| Recognized Language Code | en |
|---|---|