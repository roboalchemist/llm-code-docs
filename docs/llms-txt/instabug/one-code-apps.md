# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/one-code-apps.md

# One Code Apps

## Overview

The **One Code Apps** feature enables teams with **shared code base applications** to integrate multiple app variants under a single Luciq app token. This is ideal for organizations that release the same app to different brands, markets, or regions but want to consolidate stability and performance monitoring.

Instead of creating a separate Luciq application for each variant, you integrate all variants using **one Luciq app token** and identify each variant via the **bundle-id using the App variant API**.

{% hint style="info" %}
To enable One code apps, please reach out to our [support team](mailto:contactus@luciq.ai).
{% endhint %}

{% hint style="success" %}
Supported Metrics

* Bug Reporting
* Crash Reportin
* Application Performance Monitoring
* Session Replay
* Issues list
* Alerting
* In-App Surveys
  {% endhint %}

## How it works?

{% hint style="warning" %}
You need to configure One Code Apps by configuring the App variant API.
{% endhint %}

Once the SDK is integrated with the variant set:

You can use the **bundle-id filter** on the dashboard to:

* View **aggregated data** across all variants (default view).
* Filter by a specific variant to investigate brand- or region-specific issues within the supported products:
  * App health
  * Bug reporting
  * Crash reporting
  * APM
  * Alerting
  * Releases

#### Filtering by a specific variant

You will see a new filter called Bundle-id which enables you to filter by a certain app variant.

<figure><img src="https://files.readme.io/b4c08652c6b06be11b834bf50d4b850e46e0b2dc264c0d45544e043d849305dc-ios-one-code-apps-1.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://files.readme.io/5531b6c30ae155cb37218eb256e202a6daedc1f3248a6efdfb321fbc570c89d7-ios-one-code-apps-3.png" alt=""><figcaption></figcaption></figure>

#### Alerting on specific variant

You will see a new condition called bundle-id which enables you to set up alerts on a certain app variant.

<figure><img src="https://files.readme.io/9796a51d24edf2406abb1dee2ddc58a5133ac68c25c95a8d2d8df90bc7707656-ios-one-code-apps-2.png" alt=""><figcaption></figcaption></figure>

#### Presentation in Metrics & Reports

In various dashboard views, bundle IDs (variants) are displayed alongside relevant metrics. In Patterns and dimensions, Variants appear next to the app version so you can spot variant-specific trends.

<figure><img src="https://files.readme.io/434563b1a4aede24bbefd10dfde67ecf77646b1f59a6a8cd939f5124cd67c1ff-ios-one-code-apps-4.png" alt=""><figcaption></figcaption></figure>
