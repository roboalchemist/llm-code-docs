# Source: https://developers.make.com/custom-apps-documentation/best-practices/trigger-modules.md

# Polling triggers

A polling trigger checks for new data in a service account since the last scenario run, based on the scenario's schedule.

The polling trigger sends a request to the service. If new data exists, the scenario runs and you see the data in the module’s output as bundles. If not, you see no bundles.

Use a polling trigger only if the results:

* consist of either a numeric ID or a date as the identifier, or
* the results can be sorted or defaulted in descending order.

{% hint style="info" %}
Using `unordered` or `asc` order in a polling trigger may not work due to a 3200 pagination limit, which could result in the trigger not returning new items.

However, if the API accepts filtering and gets results only after a specified numeric ID or date, this could reduce the number of items.
{% endhint %}

## Epoch

The Epoch tab of a polling trigger defines the look of the **Choose where to start** setting so a user can select a point in the past from where the trigger should start to process data.

Use the `limit` parameter to restrict the number of results returned in the RPC, to avoid issues should the user have too many objects.

‌The `limit` parameter should be a static number that should be equal to, at maximum, 300 or 3 times the number of objects per page.

{% tabs %}
{% tab title="Incorrect" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-4b39e0b79eb5f2171f5b3f85af6387646e659b64%2FintegromatTriggerEpochWrong.png?alt=media" alt="" width="442"></div>

{% hint style="info" %}
The code is missing a `limit` parameter.
{% endhint %}
{% endtab %}

{% tab title="Correct" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-ea6390d2b60f98b9d6b5a9ad4825b4a87030237d%2Fimage.png?alt=media" alt="" width="443"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The code includes a `limit` parameter.
{% endhint %}
{% endtab %}
{% endtabs %}

## API endpoint requires `from` and/or `to` date parameters

Some API services require `date` parameters that define the interval of records to be retrieved, for example `from` and `to`, `fromDate` and `toDate`, etc.

In this case, it is important to handle the `date` parameters correctly.

{% tabs %}
{% tab title="Incorrect" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-4b44bd21f50ad8739565f8376d383b9113c11920%2Ffrom_date_parameters_incorrect.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
In this module example, the `From` and `To` parameters are required.

Since triggers don't allow mapping/functions, the user has to hardcode the `From` and `To` dates. Therefore, Make will always request the same interval of records.
{% endhint %}
{% endtab %}

{% tab title="Correct" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-ba888944df8d8969960cb45b3fda7ec5bb712886%2Ffrom_date_parameters_correct.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
In this module example, there aren't any required `From` or `To` fields.
{% endhint %}
{% endtab %}

{% tab title="Source" %}

```javascript
...
"qs": {
         "from": "{{data.lastDate}}",
         "to": "{{now}}"
      },
...

```

{% hint style="info" %}
The mapped `data.lastDate` IML variable is available to the user in the **Choose where to start** setting, defined in the [Epoch tab](#epoch).
{% endhint %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-3628c78a61878b09d52672617ae6476b78cfa2c7%2Ftrigger_choosewheretostart.png?alt=media" alt="" width="336"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The behavior of the supported options:

* **From now on** - The current date will be sent.
* **Since specific date** - The date provided will be sent.
* **Choose manually** - The date of the chosen item will be sent.
* **All** - The default date `1970-01-01` will be sent.
  {% endhint %}
  {% endtab %}
  {% endtabs %}
