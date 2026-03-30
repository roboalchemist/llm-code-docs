# Source: https://docs.luciq.ai/product-guides-and-integrations/integrations/grafana/grafana-app-health-plugin.md

# Grafana App Health Plugin

The Luciq Grafana Plugin allows you to visualize mobile metrics alongside other metrics from different sources, such as product analytics and revenue metrics, all within a single pane of glass. Our pre-built dashboard captures all the essential mobile metrics, providing a comprehensive overview of your app's health without leaving Grafana.

Below are instructions on how to install, configure, and navigate through the app health plugin.

### Install the Luciq Plugin

{% stepper %}
{% step %}

#### Open Grafana’s plugin directory

Search for "Luciq."

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FwVzGerftb8BXr7lx1aqo%2Fimage.png?alt=media&#x26;token=9a49123b-bc30-47a2-af16-0095afb7c835" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Install the [Luciq Plugin](https://grafana.com/grafana/plugins/instabug-instabug-app/)

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FddJI8gS63quivP9PQDHj%2Fimage.png?alt=media&#x26;token=d5624ae1-eabe-4351-9481-bcdc749b1c66" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### Configure the Luciq Plugin

{% hint style="info" %}
After the plugin is installed, navigate to the **Configuration** tab. It may take a couple of minutes for the Configuration tab to appear while the plugin finishes installing. If it doesn't appear right away, refresh the page after a few minutes.
{% endhint %}

* Make sure the plugin is enabled.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FxOg6qrUbayJhU6WcOITA%2Fimage.png?alt=media&#x26;token=7b2baf07-c204-4407-928f-4ca93c08927f" alt=""><figcaption></figcaption></figure>

**Prerequisites:**

* Ensure Grafana version 10.0.0 or higher is installed.
* Install the [Infinity Plugin](https://grafana.com/grafana/plugins/yesoreyeram-infinity-datasource/) (v2.4.0 or higher).

**Configuration:**

{% stepper %}
{% step %}

#### If Infinity Plugin is missing

If the Infinity Plugin is not installed, you'll receive a prompt to install it before proceeding.
{% endstep %}

{% step %}

#### Contact Luciq support for configuration fields

Contact the Luciq support team at <support@luciq.ai> to receive the necessary configuration fields:

* API Link
* Dashboard URL
* Authentication Token
* Email
  {% endstep %}

{% step %}

#### Apply settings

Once you have these fields, input the provided information in the plugin configuration page and click on “Apply Settings”.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FMxpBxSEI2uONJ301Zm0h%2Fimage.png?alt=media&#x26;token=796a8333-a33e-48c7-9a17-b7bf5946c7c7" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### Access the Pre-built Dashboard

* After configuration, go to the **Dashboards** tab. The Luciq dashboard will be automatically imported.
* Open the Luciq App Health dashboard to view the health metrics for all your Luciq apps directly within Grafana.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FSvIsoVlILWXXVGIb2A4k%2Fimage.png?alt=media&#x26;token=cbdaf808-14cc-49d9-b511-1fa3b2125c34" alt=""><figcaption></figcaption></figure>

### Luciq Grafana Dashboard Walkthrough

{% stepper %}
{% step %}

#### Filters available

You can filter by the following:

* App
* Environment
* Platform (for cross-platform applications)
* Date
  {% endstep %}

{% step %}

#### Drill down into metrics

Gain a comprehensive overview of your app's stability and performance through our high-level metrics. To delve deeper into a specific metric, click the redirection icon to open the Luciq dashboard with the same applied filters for further analysis.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FiKNNME71GgpnnPdxp87P%2Fimage.png?alt=media&#x26;token=ddcf75f4-903d-4c53-bcc9-19bb4c487043" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
