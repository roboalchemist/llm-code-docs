# Source: https://firebase.google.com/docs/ml/recognize-landmarks.md.txt

# Landmark Recognition

![](https://firebase.google.com/static/docs/ml/images/landmark_recognition.png)

With Cloud Vision's landmark recognition API, you can recognize well-known
landmarks in an image.

When you pass an image to this API, you get the landmarks that were recognized
in it, along with each landmark's geographic coordinates and the region of the
image the landmark was found. You can use this information to automatically
generate image metadata, create individualized experiences for users based on
the content they share, and more.

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/ml/ios/recognize-landmarks)
[Android](https://firebase.google.com/docs/ml/android/recognize-landmarks)

## Key capabilities

|---|---|
| Recognizes well-known landmarks | Get the name and geographic coordinates of natural and constructed landmarks, as well as the region of the image the landmark was found. Try the [Cloud Vision API demo](https://cloud.google.com/vision/docs/drag-and-drop) to see what landmarks can be found in an image you provide. |
| Get Google Knowledge Graph entity IDs | A Knowledge Graph entity ID is a string that uniquely identifies the landmark that was recognized, and is the same ID used by the [Knowledge Graph Search API](https://developers.google.com/knowledge-graph/). You can use this string to identify an entity across languages, and independently of the formatting of the text description. |
| Low-volume use at no cost | No-cost for first 1000 uses of this feature per month: see [Pricing](https://firebase.google.com/pricing) |

## Example Results

|---|---|
| ![](https://firebase.google.com/static/docs/ml/images/examples/680px-Bruegge_View_from_Rozenhoedkaai.jpg) Photo: Arcalino / Wikimedia Commons / CC BY-SA 3.0 | | Result || |---|---| | **Description** | Brugge | | **Geographic Coordinates** | 51.207367, 3.226933 | | **Knowledge Graph entity ID** | /m/0drjd2 | | **Bounding Polygon** | (20, 342), (651, 342), (651, 798), (20, 798) | | **Confidence Score** | 0.77150935 | |