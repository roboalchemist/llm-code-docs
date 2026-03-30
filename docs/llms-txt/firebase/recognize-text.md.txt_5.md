# Source: https://firebase.google.com/docs/ml/recognize-text.md.txt

# Text Recognition

![](https://firebase.google.com/static/docs/ml/images/text_recognition.png)

With Cloud Vision's text recognition API, you can recognize text in
[100+ different
languages and scripts](https://cloud.google.com/vision/docs/languages).

With this Cloud-based API, you can automate tedious data entry and extract text
from pictures of documents, which you can use to increase
accessibility or translate documents.

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/ml/ios/recognize-text)
[Android](https://firebase.google.com/docs/ml/android/recognize-text)

<br />

> [!NOTE]
> **Looking for on-device text recognition?** Try the [standalone ML Kit library](https://developers.google.com/ml-kit/vision/text-recognition).

## Key capabilities

|---|---|
| High-accuracy text recognition | Firebase ML's text recognition APIs are powered by Google Cloud's industry-leading image understanding capability. Try it yourself with the [Cloud Vision API demo](https://cloud.google.com/vision/docs/drag-and-drop). |
| Suitable for photos and documents | APIs optimized for both recognizing sparse text in images (such as photos of road signs or business cards) and recognizing densely-spaced text in pictures of documents. |
| Broad language support | Recognizes text in [100+ different languages and scripts](https://cloud.google.com/vision/docs/languages). |
| Limited no-cost use | No-cost for first 1000 uses of this feature per month: see [Pricing](https://firebase.google.com/pricing) |

## Example results

### Sparse text

![](https://firebase.google.com/static/docs/ml/images/examples/Wege_der_parlamentarischen_Demokratie.jpg) Photo: [Dietmar Rabich](https://commons.wikimedia.org/wiki/User:XRay "User:XRay") / [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page "Main Page") / ["Düsseldorf, Wege der parlamentarischen Demokratie -- 2015 -- 8123"](https://commons.wikimedia.org/wiki/File:D%C3%BCsseldorf,_Wege_der_parlamentarischen_Demokratie_--_2015_--_8123.jpg) / [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

#### Partial results

| Recognized Text ||
| Text | `Wege der parlamentarischen Demokratie` |
| Bounding Box / Frame | `Rect` (Android) or `CGRect` (iOS+) |
| Blocks | (1 block) |
|---|---|

| Block 0 ||
| Text | `Wege der parlamentarischen Demokratie` |
| Bounding Box / Frame | `Rect` (Android) or `CGRect` (iOS+) |
| Recognized Language Code | de |
| Lines | (3 lines) |
|---|---|

| Line 0 ||
| Text | `Wege der` |
| Bounding Box / Frame | `Rect` (Android) or `CGRect` (iOS+) |
| Recognized Language Code | de |
| Elements | (2 elements) |
|---|---|

| Element 0 ||
| Text | `Wege` |
|---|---|

### Document text

![](https://firebase.google.com/static/docs/ml/images/examples/dracula_p361.jpg)

#### Partial results

| Full text ||
| Text | ``` 361 DR. SEWARD'S DIARY Professor. He had evidently expected some such call, for I found him dressed in his room. His door was ajar, so that he could hear the opening of the door of our room. He came at once, as he passed into the room, he asked Mina if the others might come, too. "No," she said quite simply, "it will not be necessary. You can tell them just as well. I must go with you on your journey." Dr. Van Helsing was as startled as I was. After a mo- ment's pause he asked :- "But why?" "You must take me with you. I am safer with you, and you shall be safer, too." "But why, dear Madam Mina? You know that your safety is our solemnest duty. We go into danger, to which you are, or may be, more liable than any of us from from circumstances--things that have been." He paused, embarrassed. As she replied, she raised her finger and pointed to her forehead: "I know. That is why I must go. I can tell you now, whilst the sun is coming up; I may not be able again. I know that when the Count wills me I must go. I know that if he tells me to come in secret, I must come by wile; by any device to hoodwink—even Jonathan." God saw the look that she turned on me as she spoke, and if there be indeed a Recording Angel that look is noted to her ever- lasting honour. I could only clasp her hand. I could not speak; my emotion was too great for even the relief of tears. She went on "You men are brave and strong. You are strong in your numbers, for you can defy that which would break down the human endurance of one who had to guard alone. Be- sides, I may be of service, since you can hypotise me and so learn that which even I myself do not know." Dr. Van Helsing said very gravely "Madam Mina, you are, as always, most wise. You shall with us come; and together we shall do that which we go forth to achieve." When he had spoken, Mina's long spell of silence made me look at her. She had fallen back on her ``` |
| Blocks | (2 blocks) |
|---|---|

| Block 1 ||
| Text | ``` DR. SEWARD'S DIARY Professor. He had evidently expected some such call, for I found him dressed in his room. His door was ajar, so that he could hear the opening of the door of our room. He came at once, as he passed into the room, he asked Mina if the others might come, too. "No," she said quite simply, "it will not be necessary. You can tell them just as well. I must go with you on your journey." Dr. Van Helsing was as startled as I was. After a mo- ment's pause he asked :- "But why?" "You must take me with you. I am safer with you, and you shall be safer, too." "But why, dear Madam Mina? You know that your safety is our solemnest duty. We go into danger, to which you are, or may be, more liable than any of us from from circumstances--things that have been." He paused, embarrassed. As she replied, she raised her finger and pointed to her forehead: "I know. That is why I must go. I can tell you now, whilst the sun is coming up; I may not be able again. I know that when the Count wills me I must go. I know that if he tells me to come in secret, I must come by wile; by any device to hoodwink—even Jonathan." God saw the look that she turned on me as she spoke, and if there be indeed a Recording Angel that look is noted to her ever- lasting honour. I could only clasp her hand. I could not speak; my emotion was too great for even the relief of tears. She went on "You men are brave and strong. You are strong in your numbers, for you can defy that which would break down the human endurance of one who had to guard alone. Be- sides, I may be of service, since you can hypotise me and so learn that which even I myself do not know." Dr. Van Helsing said very gravely "Madam Mina, you are, as always, most wise. You shall with us come; and together we shall do that which we go forth to achieve." When he had spoken, Mina's long spell of silence made me look at her. She had fallen back on her ``` |
| Confidence | 0.98 |
| Bounding Box / Frame | `Rect` (Android) or `CGRect` (iOS+) |
| Recognized Language Code | en |
| Paragraphs | (10 paragraphs) |
|---|---|

| Paragraph 1 ||
| Text | ``` "No," she said quite simply, "it will not be necessary. You can tell them just as well. I must go with you on your journey." ``` |
| Confidence | 0.97 |
| Bounding Box / Frame | `Rect` (Android) or `CGRect` (iOS+) |
| Recognized Language Code | en |
| Words | (34 words) |
|---|---|

| Word 7 ||
| Text | ``` simply ``` |
| Confidence | 0.99 |
| Bounding Box / Frame | `Rect` (Android) or `CGRect` (iOS+) |
| Recognized Language Code | en |
| Symbols | (6 symbols) |
|---|---|

| Symbol 0 ||
| Text | ``` s ``` |
| Confidence | 0.97 |
| Bounding Box / Frame | `Rect` (Android) or `CGRect` (iOS+) |
| Recognized Language Code | en |
|---|---|