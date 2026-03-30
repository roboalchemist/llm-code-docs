# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/in-app-surveys/creating-in-app-surveys.md

# Creating In-app Surveys

You can create In-app surveys to collect feedback from your users. There are three different types of In app Surveys that you can create:

* ​[Custom Survey](https://docs.luciq.ai/ios-creating-surveys#section-custom-survey): create a set of customized questions using different question types
* ​[NPS Survey](https://docs.luciq.ai/ios-creating-surveys#section-nps-survey): find out whether your users would promote your application or not, then have them rate your application
* ​[App Rating](https://docs.luciq.ai/ios-creating-surveys#section-app-rating): ask your users if they like your app. If they answer yes, they'll be prompted to rate your application

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FEQ3scUACoivBOp5fOpWt%2Fimage.png?alt=media&#x26;token=9fbd9201-6ab0-4ceb-a7eb-9506b0db47a8" alt=""><figcaption></figcaption></figure>

### Surveys

You can choose between three types of surveys when creating a new one: **Custom Survey**, **NPS Survey**, and **App Rating**.

#### Custom Survey

Create your own custom surveys with any number of questions displayed to your user one by one, sequentially. You can select between three types of answers:

* **Text Field**: The user must answer the question by typing their response in a text field.
* **Multiple Choice**: The user must answer the question by choosing one of any number of answers you have defined in your dashboard.
* **Stars**: The user must answer the question with one to five stars.

This type of survey can use both manal and automatic [targeting](https://docs.luciq.ai/product-guides-and-integrations/product-guides/in-app-surveys/broken-reference).

<figure><img src="https://files.readme.io/db609f4c5a7480116b41aec7812089900e06b18a87cd09aa8f2bd789d3bb23ff-image.png" alt=""><figcaption></figcaption></figure>

#### NPS Survey

The default first question in an NPS Survey is "How likely are you to recommend `<Your App Name>` to a friend or colleague?" The user must reply on a scale of 1-10, least to most likely.

Depending on the rating given by the user, they will be shown one of three possible follow-up questions:

* **User rating is 9 or 10 (Promoter)**: The user will be asked for feedback about how to improve the app. You will also have the option to allow the users to rate the application while creating the survey. A link is then generated to your app on the App Store. The user will be asked to rate your app. If they accept, they will be redirected to the App Store link. If your app is in beta, or if your app is not available on the App Store, the user will instead be asked to submit their survey.
* **User rating is 7 or 8 (Passive)**: The user will be asked for feedback about how to improve the app. You will also have the option to allow the users to rate the application while creating the survey.
* **User rating is less than 7 (Detractor)**: The user will be asked for feedback about how to improve the app.

This type of survey can use both manual and automatic targeting.

From your dashboard, you can customize the text of any question in an NPS Survey.

<figure><img src="https://files.readme.io/e77ea6c576080d1cbfc8d44fd2b31f5faf2bf42e3aaa593d75d01ec956b54814-image.png" alt=""><figcaption></figcaption></figure>

#### App Rating

This template is used to identify happy users and ask them to rate your app.

First, your users will see an alert, native to the OS, which asks if they are satisfied with the application.

* If the user answers yes, they will be asked to rate the application on the App Store in another alert automatically. If the application is in beta mode, the user will not be asked to rate on the App Store.
* If the user answers no, they will be asked how the application can do better in a survey format similar to the one in the custom survey section.

This type of survey can use both manual and automatic targeting.

You can set the frequency for how often this message shows. By default, it is set to every 30 days.

{% hint style="info" %}

#### Changing the Alert Text

During the creation process, you can edit any of the text that will be in the alerts shown to the users.
{% endhint %}

<figure><img src="https://files.readme.io/b327d876d9c4ada50096a787014028731fcd26667d2c893e45c1ededa3cf5939-image.png" alt=""><figcaption></figcaption></figure>

### Survey Localization

You can display your surveys and announcements to your users in their language. To do this, you only need to add the locale when creating the survey, then add the questions in that language.

<figure><img src="https://files.readme.io/230fa410440ab9e8ab6519bf67bc85c7900bdd0cf547ea031f8e7458d2a07be5-image.png" alt=""><figcaption></figcaption></figure>

### Editing Survey Locales

There are some rules that should be adhered to when adding and editing locales and languages for surveys and announcements.

#### Default Language

Every survey and announcement you create must have a default language. This default language is used when no locale is set and you don't support the device's current locale, so make sure you set the right default language. By default, the default language is set to English.

For each locale you add, a new tab will be added in the dashboard from where you can modify the text that will be displayed for that locale. Other changes to the survey, like adding or removing questions, can only be done from the default locale tab.

<figure><img src="https://files.readme.io/c2d4703faae66b9a428d2eb04fb1e1aeaf913ac631494b81559d5c72e8071d6f-image.png" alt=""><figcaption></figcaption></figure>

#### Determining Shown Locale

The SDK determines which survey language is shown based on a few priorities. If you use the [set locale API](https://docs.luciq.ai/product-guides-and-integrations/product-guides/in-app-surveys/broken-reference), this locale will take precedence over the device locale so the survey will be shown in the locale you set through the API. Otherwise, surveys will be displayed in the language that matches the device locale. In case you don't support this locale, the survey will use the default language.

To summarize, in order of priority:\
1 - Locale set through API\
2 - The device locale\
3 - Default locale set through the dashboard (if device locale isn't supported)

#### Supported Locales

Currently, most locales supported by the SDK are supported in the survey localization, with more locales to be added soon. Below is the list for supported locales.

```
- English en
- Arabic ar
- Czech cs
- Danish da
- German de
- Spanish es
- French fr
- Italian it
- Japanese ja
- Korean ko
- Dutch nl
- Norwegian (no, nb) --> nb-NO
- Polish pl
- Portuguese Brazil pt-BR
- Portuguese Portugal pt-PT
- Russian ru
- Slovak sk
- Swedish sv
- Turkish tr
- Chinese Simplified (zh-hans, zh-CN) --> zh-CN
- Chinese Traditional (zh-TW,  zh-hant-TW, zh-Hant) --> zh-TW
- Hindi hi
- Greek el
- Finnish fi
- Estonian et
- Romanian ro
- Vietnamese vi
```

{% hint style="info" %}

#### **Backwards Compatibility**

Multiple locale surveys will appear starting from version 8.3. If you're targeting older SDKs, only the default survey locale will be shown. All surveys created before version 8.3 will continue to work with only a single locale.
{% endhint %}

#### Duplicating Surveys

If you need to create a copy of an already existing survey, you can duplicate it by opening the survey itself from the survey list, and clicking on the duplicate button in the survey results page. Please note that any duplicated survey is placed directly in a draft state, so you'll have to publish it manually once the duplication is complete.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-1942622943/https%3A%2F%2Ffiles.readme.io%2Fad74d1fe3d698fb09765241dd6969d0536f43de644a75fdbbe6c6dd5c79a8b5b-ios-creating-surveys-1.png" alt=""><figcaption></figcaption></figure>
