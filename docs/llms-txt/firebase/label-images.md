# Source: https://firebase.google.com/docs/ml/label-images.md.txt

# Source: https://firebase.google.com/docs/ml/ios/label-images.md.txt

# Source: https://firebase.google.com/docs/ml-kit/ios/label-images.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/label-images.md.txt

# Source: https://firebase.google.com/docs/ml/android/label-images.md.txt

# Source: https://firebase.google.com/docs/ml-kit/label-images.md.txt

# Image Labeling

plat_iosplat_android  
| This page describes an old version of the Image Labeling API, which was part of ML Kit for Firebase. The functionality of this API has been split into two new APIs ([learn more](https://developers.google.com/ml-kit/migration)):
|
| - [On-device image labeling](https://developers.google.com/ml-kit/vision/image-labeling)is part of the new standalone ML Kit SDK, which you can use with or without Firebase.
| - [Cloud image labeling](https://firebase.google.com/docs/ml/label-images)is part ofFirebase ML, which includes all of Firebase's cloud-based ML features.

![](https://firebase.google.com/static/docs/ml-kit/images/image_labeling@2x.png)

With ML Kit's image labeling APIs, you can recognize entities in an image without having to provide any additional contextual metadata, using either an on-device API or a cloud-based API.

Image labeling gives you insight into the content of images. When you use the API, you get a list of the entities that were recognized: people, things, places, activities, and so on. Each label found comes with a score that indicates the confidence the ML model has in its relevance. With this information, you can perform tasks such as automatic metadata generation and content moderation.

[iOS](https://firebase.google.com/docs/ml-kit/ios/label-images)[Android](https://firebase.google.com/docs/ml-kit/android/label-images)

If you're a Flutter developer, you might be interested in[FlutterFire](https://github.com/FirebaseExtended/flutterfire/tree/master/packages/firebase_ml_vision), which includes a plugin for Firebase's ML Vision APIs.
| **Want to label images with your own categories?** Train your own image labeling models with[AutoML Vision Edge](https://firebase.google.com/docs/ml-kit/automl-image-labeling).
| This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Choose between on-device and Cloud APIs

|                                   |                                   On-device                                   |                                                                                              Cloud                                                                                              |
|              Pricing              |                                     Free                                      |                                              Free for first 1000 uses of this feature per month: see[Pricing](https://firebase.google.com/pricing)                                              |
|          Label coverage           | 400+ labels that cover the most commonly-found concepts in photos. See below. | 10,000+ labels in many categories. See below. Also, try the[Cloud Vision API demo](https://cloud.google.com/vision/docs/drag-and-drop)to see what labels can be found for an image you provide. |
| Knowledge Graph entity ID support |                                                                               |                                                                                                                                                                                                 |
|-----------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Example on-device labels

The device-based API supports 400+ labels, such as the following examples:

|  Category  |        Example labels        |
|------------|------------------------------|
| People     | `Crowd` `Selfie` `Smile`     |
| Activities | `Dancing` `Eating` `Surfing` |
| Things     | `Car` `Piano` `Receipt`      |
| Animals    | `Bird` `Cat` `Dog `          |
| Plants     | `Flower` `Fruit` `Vegetable` |
| Places     | `Beach` `Lake` `Mountain`    |

### Example cloud labels

The cloud-based API supports 10,000+ labels, such as the following examples:

|        Category        |              Example labels              |       Category       |                Example labels                 |
|------------------------|------------------------------------------|----------------------|-----------------------------------------------|
| Arts \& entertainment  | `Sculpture` `Musical Instrument` `Dance` | Astronomical objects | `Comet` `Galaxy` `Star`                       |
| Business \& industrial | `Restaurant` `Factory` `Airline`         | Colors               | `Red` `Green` `Blue`                          |
| Design                 | `Floral` `Pattern` `Wood Stain`          | Drink                | `Coffee` `Tea` `Milk`                         |
| Events                 | `Meeting` `Picnic` `Vacation`            | Fictional characters | `Santa Claus` `Superhero` `Mythical creature` |
| Food                   | `Casserole` `Fruit` `Potato chip`        | Home \& garden       | `Laundry basket` `Dishwasher` `Fountain`      |
| Activities             | `Wedding` `Dancing` `Motorsport`         | Materials            | `Ceramic` `Textile` `Fiber`                   |
| Media                  | `Newsprint` `Document` `Sign`            | Modes of transport   | `Aircraft` `Motorcycle` `Subway`              |
| Occupations            | `Actor` `Florist` `Police`               | Organisms            | `Plant` `Animal` `Fungus`                     |
| Organizations          | `Government` `Club` `College`            | Places               | `Airport` `Mountain` `Tent`                   |
| Technology             | `Robot` `Computer` `Solar panel`         | Things               | `Bicycle` `Pipe` `Doll`                       |

## Google Knowledge Graph entity IDs

In addition the text description of each label that ML Kit returns, it also returns the label's Google Knowledge Graph entity ID. This ID is a string that uniquely identifies the entity represented by the label, and is the same ID used by the[Knowledge Graph Search API](https://developers.google.com/knowledge-graph/). You can use this string to identify an entity across languages, and independently of the formatting of the text description.

## Example results

![](https://firebase.google.com/static/docs/ml-kit/images/examples/1024px-Valais_Cup_2013_-_OM-FC_Porto_13-07-2013_-_Brice_Samba_en_extension.jpg)Photo: ClÃ©ment Bucco-Lechat / Wikimedia Commons / CC BY-SA 3.0

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          On-device                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Cloud                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| |-------------------------------|-----------| | **Description**               | Stadium   | | **Knowledge Graph entity ID** | /m/019cfy | | **Confidence**                | 0.9205354 | |-------------------------------|-----------| | **Description**               | Sports    | | **Knowledge Graph entity ID** | /m/06ntj  | | **Confidence**                | 0.7531109 | |-------------------------------|------------| | **Description**               | Event      | | **Knowledge Graph entity ID** | /m/081pkj  | | **Confidence**                | 0.66905296 | |-------------------------------|------------| | **Description**               | Leisure    | | **Knowledge Graph entity ID** | /m/04g3r   | | **Confidence**                | 0.59904146 | |-------------------------------|------------| | **Description**               | Soccer     | | **Knowledge Graph entity ID** | /m/02vx4   | | **Confidence**                | 0.56384534 | |-------------------------------|------------| | **Description**               | Net        | | **Knowledge Graph entity ID** | /m/02qdwbp | | **Confidence**                | 0.54679185 | |-------------------------------|----------| | **Description**               | Plant    | | **Knowledge Graph entity ID** | /m/05s2s | | **Confidence**                | 0.524364 | ... etc. | |-------------------------------|-------------| | **Description**               | sport venue | | **Knowledge Graph entity ID** | /m/0bmgjqz  | | **Confidence**                | 0.9860726   | |-------------------------------|-----------| | **Description**               | player    | | **Knowledge Graph entity ID** | /m/02vzx9 | | **Confidence**                | 0.9797604 | |-------------------------------|-----------| | **Description**               | stadium   | | **Knowledge Graph entity ID** | /m/019cfy | | **Confidence**                | 0.9635762 | |-------------------------------|-------------------------| | **Description**               | soccer specific stadium | | **Knowledge Graph entity ID** | /m/0404y4               | | **Confidence**                | 0.95806926              | |-------------------------------|-----------------| | **Description**               | football player | | **Knowledge Graph entity ID** | /m/0gl2ny2      | | **Confidence**                | 0.9510419       | |-------------------------------|-----------| | **Description**               | sports    | | **Knowledge Graph entity ID** | /m/06ntj  | | **Confidence**                | 0.9253524 | |-------------------------------|---------------| | **Description**               | soccer player | | **Knowledge Graph entity ID** | /m/0pcq81q    | | **Confidence**                | 0.9033665     | |-------------------------------|-----------| | **Description**               | arena     | | **Knowledge Graph entity ID** | /m/018lrm | | **Confidence**                | 0.8897188 | ... etc. |