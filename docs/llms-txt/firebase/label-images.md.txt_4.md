# Source: https://firebase.google.com/docs/ml/label-images.md.txt

# Image Labeling

![](https://firebase.google.com/static/docs/ml/images/image_labeling.png)

With Cloud Vision's image labeling APIs, you can recognize entities in
an image without having to provide any additional contextual metadata.

Image labeling gives you insight into the content of images. When you use the
API, you get a list of the entities that were recognized: people, things,
places, activities, and so on. Each label found comes with a score that
indicates the confidence the ML model has in its relevance. With this
information, you can perform tasks such as automatic metadata generation
and content moderation.

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/ml/ios/label-images)
[Android](https://firebase.google.com/docs/ml/android/label-images)

<br />

> [!NOTE]
> **Want to label images with your own categories?** Train your own image labeling models with [AutoML Vision Edge](https://firebase.google.com/docs/ml/automl-image-labeling).

> [!NOTE]
> **Looking for on-device image labeling?** Try the [standalone ML Kit library](https://developers.google.com/ml-kit/vision/image-labeling).

## Key capabilities

|---|---|
| High-accuracy image labeling | Firebase ML's image labeling API is powered by Google Cloud's industry-leading image understanding capability, which can classify images with 10,000+ labels in many categories. (See below.) Try it yourself with the [Cloud Vision API demo](https://cloud.google.com/vision/docs/drag-and-drop). |
| Knowledge Graph entity support | In addition the text description of each label that Firebase ML returns, it also returns the label's Google Knowledge Graph entity ID. This ID is a string that uniquely identifies the entity represented by the label, and is the same ID used by the [Knowledge Graph Search API](https://developers.google.com/knowledge-graph/). You can use this string to identify an entity across languages, and independently of the formatting of the text description. |
| Limited no-cost use | No-cost for first 1000 uses of this feature per month: see [Pricing](https://firebase.google.com/pricing) |

### Example labels

The image labeling API supports 10,000+ labels, including the following examples
and many more:

| Category | Example labels | Category | Example labels |
|---|---|---|---|
| Arts \& entertainment | `Sculpture` `Musical Instrument` `Dance` | Astronomical objects | `Comet` `Galaxy` `Star` |
| Business \& industrial | `Restaurant` `Factory` `Airline` | Colors | `Red` `Green` `Blue` |
| Design | `Floral` `Pattern` `Wood Stain` | Drink | `Coffee` `Tea` `Milk` |
| Events | `Meeting` `Picnic` `Vacation` | Fictional characters | `Santa Claus` `Superhero` `Mythical creature` |
| Food | `Casserole` `Fruit` `Potato chip` | Home \& garden | `Laundry basket` `Dishwasher` `Fountain` |
| Activities | `Wedding` `Dancing` `Motorsport` | Materials | `Ceramic` `Textile` `Fiber` |
| Media | `Newsprint` `Document` `Sign` | Modes of transport | `Aircraft` `Motorcycle` `Subway` |
| Occupations | `Actor` `Florist` `Police` | Organisms | `Plant` `Animal` `Fungus` |
| Organizations | `Government` `Club` `College` | Places | `Airport` `Mountain` `Tent` |
| Technology | `Robot` `Computer` `Solar panel` | Things | `Bicycle` `Pipe` `Doll` |

## Example results

![](https://firebase.google.com/static/docs/ml/images/examples/1024px-Valais_Cup_2013_-_OM-FC_Porto_13-07-2013_-_Brice_Samba_en_extension.jpg) Photo: Clément Bucco-Lechat / Wikimedia Commons / CC BY-SA 3.0

| Label | Knowledge Graph entity ID | Confidence |
|---|---|---|
| sport venue | /m/0bmgjqz | 0.9860726 |
| player | /m/02vzx9 | 0.9797604 |
| stadium | /m/019cfy | 0.9635762 |
| soccer specific stadium | /m/0404y4 | 0.95806926 |
| football player | /m/0gl2ny2 | 0.9510419 |
| sports | /m/06ntj | 0.9253524 |
| soccer player | /m/0pcq81q | 0.9033665 |
| arena | /m/018lrm | 0.8897188 |