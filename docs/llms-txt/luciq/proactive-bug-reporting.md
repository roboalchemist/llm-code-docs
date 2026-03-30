# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/bug-reporting/proactive-bug-reporting.md

# Proactive Bug Reporting

### What is Proactive Reporting?

Proactive Reporting is a feature that prompts end users to submit their feedback after our SDK automatically detects a frustrating experience. <br>

<figure><img src="https://files.readme.io/aae6c1770a4d42429856d92eb93248024babff70a66c3de6d9fe92e11603bb00-Bug_Reporting.gif" alt=""><figcaption></figcaption></figure>

The frustrating experience our SDK detects to trigger the feedback modal is [**Force Restart**](https://docs.luciq.ai/product-guides-and-integrations/product-guides/crash-reporting/force-restarts).

If you have our **Force Restart** product enabled as part of your plan, users will be prompted to submit their feedback and explain what triggered them to force restart the app.

The details of the feature are as follows:

* You should have **Force Restart** as part of your plan.
* Enable the feature (Using the APIs in the upcoming section).
* Once the SDK captures a Force Restart occurrence, a modal will be triggered to ask your end-users if they want to share their feedback and experience.
* This feedback will reflect on your Bug Reporting page in the dashboard.

If enabled, users will first see a modal asking if they want to report this experience. If their answer is yes, they will see a **Feedback** description model that allows them to enter their email and describe their experience using their own words.

|                                                                                                                             |                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| ![](https://files.readme.io/ba2fb841c90a3ee873e13a59fa07c9c64fc7d3eb27379cd89e17d96b0e9422bd-ios-proactive-reporting-1.png) | ![](https://files.readme.io/96690010a0bb1031eaeba0c1a136279c9ff405974320fce53d4dbcec4134bec3-ios-proactive-reporting-2.png) |

On the dashboard, your end-user's feedback will be reflected in the Bug Reporting page as a **Frustrating Experience** report type.

Clicking the **Open Occurrence** under the **Force Restart** section will take you to the occurrence where the end-user force closed the app in the Force Restart product.

<figure><img src="https://files.readme.io/72c393502da0f2ade0af17cb5ca540a6703f720c4061e20fc2415f37f2e0615b-ios-proactive-reporting-3.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The report's details show the data from the session after the user force-closed the app, while the details you’ll see in the Force Restart occurrence are from the session in which they force-closed the app.
{% endhint %}

### Good to know about Proactive Reporting

The feature’s default behavior is as follows:

* Feature is disabled.
* If you don’t configure the gap between pop-ups, the default gap will be 24 hours.
* If you don’t configure the gap between the launch and the first pop-up, the default gap will be 2 seconds.
* If you have [Surveys](https://docs.luciq.ai/product-guides-and-integrations/product-guides/in-app-surveys) enabled in your plan, please contact the support team to enable this feature for you from our backend. Remember to configure the surveys triggering differently from the proactive reporting modal to avoid overwhelming your users.
* To use this feature, [Force Restart](https://docs.luciq.ai/product-guides-and-integrations/product-guides/crash-reporting/force-restarts) (part of Crash Reporting) has to be part of your plan.
* Proactive reports have the same data retention as Force Restart (part of Crash Reporting)
* If you use our Crash Consent feature, the pop-up won’t be displayed in the session in which the crash consent will appear.
