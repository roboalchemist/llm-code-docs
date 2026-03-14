# Source: https://docs.beefree.io/beefree-sdk/other-customizations/appearance/themes.md

# Themes

{% hint style="info" %}
This feature is available on Beefree SDK [Core plan](https://developers.beefree.io/pricing-plans) and above. Upgrade a [development application](https://docs.beefree.io/beefree-sdk/getting-started/readme/development-applications) at no extra charge to explore features from higher plan tiers. **Note:** Usage on a development application still counts toward [usage-based fees](https://devportal.beefree.io/hc/en-us/articles/4403095825042-Usage-based-fees) and limits.
{% endhint %}

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fjr2jDpfeHivPiR7BkTrt%2Fgif-base_hi-res_2.gif?alt=media&#x26;token=7e7e99ef-61f1-4078-9d7e-ae04361e832b" alt=""><figcaption></figcaption></figure>

### How it works <a href="#how-it-works" id="how-it-works"></a>

This Beefree SDK configuration allows you to change the builder’s appearance when rendered within your application so that it will blend even more seamlessly with the rest of your user interface.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F4m0w0xgxIy76QYWhzgvf%2FCleanShot%202025-03-13%20at%2014.53.58.png?alt=media&#x26;token=802ac1cb-8d99-4e06-93b6-8f59e8650374" alt=""><figcaption></figcaption></figure>

Technically speaking, it allows you to change some parts of the CSS (Cascading Style Sheets) that controls the look & feel of the editor. If you want to use your own CSS, please refer to our [Custom CSS](https://docs.beefree.io/beefree-sdk/other-customizations/appearance/custom-css) feature.

### Using a predefined theme <a href="#using-a-predefined-theme" id="using-a-predefined-theme"></a>

To change the builder’s appearance with just one click – and to familiarize with this feature – try one of the available, pre-built themes. All of them were created based on UI best practices, such as using the right amount of contrast between elements.

You can apply one of these themes as is, or use them as a starting point. And you can roll back to the default theme at any time, if things go wrong.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F5WBImtRpmG4ijaRbnYAb%2FCleanShot%202025-03-13%20at%2014.54.25.png?alt=media&#x26;token=7b4ccfd9-d7bb-4055-a2ed-5f57f78d0c38" alt=""><figcaption></figcaption></figure>

Note that themes will **not be applied automatically**, but rather will change the Look & feel values displayed in the lower part of the page.

Once you’re happy with your selection, press **Save** to apply the new theme to your Beefree SDK application.

### Building your own theme <a href="#building-your-own-theme" id="building-your-own-theme"></a>

The properties that make up a theme are divided into sections for clarity and easy of use.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fv1d4vg6aktF1iKhipvkw%2FCleanShot%202025-03-13%20at%2014.54.58.png?alt=media&#x26;token=eb3b5a07-8e5f-4c3c-a244-a3c91e40cb97" alt=""><figcaption></figcaption></figure>

### Available settings explained <a href="#available-settings-explained" id="available-settings-explained"></a>

#### General

The basic settings for your theme. They provide control over the font used and the general color scheme.

**Font URL**

You can use a Web font by adding the URL of a public CSS file (e.g., <https://fonts.googleapis.com/css?family=Roboto>)

**Font-family stack**

Will be used as font-family property. Remember that – when using web fonts – a fallback value will help to deal with downtime or network issues.

**Brand color palette**

Use this section to configure basic properties of your color scheme. These colors will be displayed in buttons, active widgets, hover & selection helpers, etc.

The *Primary* color will be the most important color in your scheme, as it will identify highlighted elements. Here are two examples of how a highlighted row is rendered using two different themes (the default theme is shown at the top).

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FwOexIyYIVWOt6MuR50Oc%2F5brand-2.png?alt=media&#x26;token=2b1bf675-3719-4e18-9786-12ae21d5dede" alt=""><figcaption></figcaption></figure>

#### Stage

The stage is the area where the message is displayed while you design it. The main elements will inherit colors from *General | Brand Color Palette* so only the text color is available as an editable property.

#### Right panel tabs

This section controls the appearance of the right panel’s top tabs. You can add custom colors and even hide the default icons (which may be useful for some translations in order to create more real estate for the text labels). Here is an example (left: default theme, right: aubergine).

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F2dfOKrjRWHfdtrkYurl7%2F6tabs-1024x72.png?alt=media&#x26;token=e19deb14-fe74-42fd-98c9-2eb464edab55" alt=""><figcaption></figcaption></figure>

### Draggable tiles and Tile icons

These sections will help you customize the tiles that are used for content items and row structures. Here is an example (left: default theme, right: aubergine).

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FfWkcHVtbZUZ1015I0qok%2F7tiles-1024x363.png?alt=media&#x26;token=43f922c7-0a63-4680-8979-cc5312c0cdfb" alt=""><figcaption></figcaption></figure>

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fk3rtjpAdwv5ktebxO0lg%2F8tiles2-1024x422.png?alt=media&#x26;token=4e980e12-e6b0-495a-bb7c-270aac02af29" alt=""><figcaption></figcaption></figure>

### Properties top bar

This is the title bar that is displayed in the right side panel when you select an item on the editing stage. It displays important information and actions that can be performed on that item.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fs2oJAekBmWDD6DSL6LyE%2F9row_prop-1024x57.png?alt=media&#x26;token=1a1e64df-39ba-4e3c-b0f9-3046f25ddd79" alt=""><figcaption></figcaption></figure>

### Widgets

All the properties displayed in the right side panel when you select an item in the editing stage are a mix of shared widgets.

The following is a visual guide of the available customizations (left: default theme, right: aubergine).

### **Sections**

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FIDwGSDX7OHgkjmuK9v6z%2F10section-1-1024x62.png?alt=media&#x26;token=27adc909-0ed7-4cd6-a44f-b364fc2c4be7" alt=""><figcaption></figcaption></figure>

### **Input fields**

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FHAOxzjn1JKOidi5wVwN4%2F11inputs-1-1024x153.png?alt=media&#x26;token=d42554ba-534b-4c9a-a40a-3fc681a54658" alt=""><figcaption></figcaption></figure>

### **Toggle control**

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FayDgv0poConMA4o6mVGP%2F12toggle-1-1024x69.png?alt=media&#x26;token=1d4afc7e-0862-45c1-bb2c-e5a8de43e4b7" alt=""><figcaption></figcaption></figure>

### **Social icons**

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FYp3qH5RFwDyd6Ff2N6fU%2F13icons_1.png?alt=media&#x26;token=494b7c7f-ee81-4636-b6d4-ff5a572b2b69" alt=""><figcaption></figcaption></figure>

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2F2b96QohLCicZAmo9GyTl%2F14icons_2.png?alt=media&#x26;token=816116d4-4df2-43a2-9e3a-537d70da8c11" alt=""><figcaption></figcaption></figure>
