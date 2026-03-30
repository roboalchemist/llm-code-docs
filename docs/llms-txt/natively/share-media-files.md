# Source: https://docs.buildnatively.com/guides/integration/share-media-files.md

# Share Media/Files

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

### 🧋 Bubble.io Plugin

#### \[Action] Natively - Share

* Type - text, image, text and image or file
* Image Url
* Text or Url
* File Url

First of all, specify a type if you want to share just a URL, select **Type** (text), and provide a URL in the **Text or Url** field.

Same for Text/Url + Image. Selecting a **Type** (both) and filling a **Text or Url** and **Image Url** fields.

For files, you need to select **Type** (file), and provide a URL in the **File url** field

### 🛠 JavaScript SDK

#### Share Image

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const imageUrl = "https://awik.io/wp-content/uploads/2018/06/unsplash.jpg";
window.natively.shareImage(imageUrl);
```

{% endcode %}

#### Share Text

{% code lineNumbers="true" %}

```javascript
const text = "Text for sharing";
window.natively.shareText(text);
```

{% endcode %}

#### Share Text & Image

{% code lineNumbers="true" %}

```javascript
const text = "Text for sharing";
const imageUrl = "https://awik.io/wp-content/uploads/2018/06/unsplash.jpg";
window.natively.shareTextAndImage(text, imageUrl);
```

{% endcode %}

#### Share File

{% code lineNumbers="true" %}

```javascript
const fileUrl = "http://www.africau.edu/images/default/sample.pdf";
window.natively.shareFile(fileUrl);
```

{% endcode %}
