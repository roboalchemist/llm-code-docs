# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-in-app-surveys/targeting-surveys.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-in-app-surveys/targeting-surveys.md

# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/in-app-surveys/targeting-surveys.md

# Targeting Surveys

You can define criteria that your users have to meet in order for your surveys to appear in their app. This can be done through both automatic and manual targeting. The available targeting types vary based on the survey or announcement template you're using.

### Auto Targeting

After choosing the survey type you want to create, you can target specific audiences using custom conditions.When you select **Auto Targeting**, you can define criteria for who should receive the survey. Your users matching the conditions you set will automatically see the survey. In addition to default attributes like App Version, OS, Email, Sessions Count, Last Seen, Country, etc., you can set conditions for custom user attributes or user events that you have created. Multiple different criteria of any type can be added.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-1352503449/https%3A%2F%2Ffiles.readme.io%2F1e828c5a46befda6b83022b3bc27e8842214040a743bbbbe97ef40c0ac8ae882-image.png" alt=""><figcaption></figcaption></figure>

You can specify the who, when, and frequency of the survey.

* **Who**: this is used to automatically target specific users. You can target users with specific attributes or users that have done specific events. Examples can be found in the screenshot below.
* **When**: specify when the survey should show to your users. By default, this is set to 10 seconds after the application launches. This can be set so that the survey shows the moment a specific event occurs.
* **Frequency**: the amount of times the user sees the survey within a certain period. By default, this is once every 30 days. The number of days can be edited and you can set it so that the survey only appears once and never again afterward.​

  <figure><img src="https://images.gitbook.com/__img/dpr=2,width=1168,onerror=redirect,format=auto,signature=-96283333/https%3A%2F%2Ffiles.readme.io%2F1c860858da95559637bf308a0d2287c67ee491af1f91da653b8af0afea820422-image.png" alt=""><figcaption></figcaption></figure>

Depending on the template you use, different options will be available to use for automatic targeting.

* Custom/NPS/App Rating: these three templates can automatically target using default attributes, custom attributes, and user events.

{% hint style="info" %}

#### **Targeting using App Version**

Starting from version 8.5.0, the accepted app versions can be any of the ones with the following formats:

* x.y.z (ex: 1.4.2)
* x.y.z.w (ex: 1.4.2.7)
* \[any string] (ex: 1.4.2april2016) *this format can only be used with equals/doesn't equal to and can't be set to greater or less than*
  {% endhint %}

#### Controlling Auto Targeting

You can have auto targeting surveys shown automatically at the start of a user's session or show it manually.

**Showing Automatically**

By default, a survey will automatically be presented to users who meet your conditions in their first session after you publish the survey within 10 seconds of opening your app. If you have multiple surveys running and a user meets the conditions for more than one survey, they will be shown each survey one by one.Auto-targeting surveys are shown once only, unless specified otherwise in the targeting section of the survey.

**Targeting Through CSV**

If you'd like to target a list of specific user emails, this is now possible by uploading a CSV in the targeting step. Each email should be in a separate row with no more than 100K entries. The file should also be less than 5MB in size. Once the file is uploaded, the dashboard will take care of the rest!

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=2044603175/https%3A%2F%2Ffiles.readme.io%2Ff852076f971accde59a5a0e942f31136de9b08ce3cbaff28151aa55a7400b4c6-image.png" alt=""><figcaption></figcaption></figure>

### Manual Targeting

You can also use **Manual Targeting** to show your surveys to specific audiences, and these surveys can be re-shown any number of times.Each created survey has a unique token that you can refer to in your code, as explained in the following section. Please note that manual targeting can only be used with custom surveys, NPS surveys, and app ratings.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-713341768/https%3A%2F%2Ffiles.readme.io%2F5bebe5873fcae4cd0803c1d4e2547ee94808d156334c3aae5685cd8401d54edf-image.png" alt=""><figcaption></figcaption></figure>
