# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/bug-reporting/bug-grouping/bug-grouping-or-alerts-and-rules.md

# Bug Grouping | Alerts & Rules

## Overview

If you have Bug Grouping enabled, you can choose which report types to alert on or automate with rules. You can set alerts or rules for:

* **Master & Ungrouped reports**: the parent report and any report that is not part of any group.
* **Duplicate report**: a report automatically or manually marked as a duplicate of a master.

***

### How it works

#### Main Approach

Start by choosing a trigger. You can target either **Any report type** or **Master & Ungrouped reports**.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F2Th0SDjjQrX3wYZSdGtm%2FScreenshot%202026-02-24%20at%201.44.00%E2%80%AFPM.png?alt=media&#x26;token=51532bb0-5643-44ae-b566-430528957c5e" alt=""><figcaption></figcaption></figure>

To trigger on **all reports** (masters, singles, and duplicates), choose **Any bug is reported**. It triggers whenever you receive **any** bug report.

If you only want **Master & Ungrouped/Single** reports (**recommended**), choose **Not a duplicate bug is reported**. This reduces noise from alerts when a **duplicate report** is received.

#### Another Approach | Utilize report tags

* By default, when a report becomes a **master report,** a new "Luciq\_Master\_report" tag is added to it.
* The same applies to **duplicate reports**. When a duplicate bug is reported, it gets a new "Luciq\_Duplicate\_report" tag.
* You can use these tags to trigger a rule when:
  * A bug report becomes a group master.
  * A bug report is marked as a duplicate of an existing report.

{% columns %}
{% column %}

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FgcsySym4rw6rYgaoAMzi%2FScreenshot%202026-02-24%20at%202.22.19%E2%80%AFPM.png?alt=media&#x26;token=b0a322a5-1d26-463e-8a88-f4efb703623d" alt=""><figcaption><p>Setting a rule for master reports</p></figcaption></figure>
{% endcolumn %}

{% column %}

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FdrxMzkrmC3c4OZVvxW1r%2FScreenshot%202026-02-24%20at%202.22.59%E2%80%AFPM.png?alt=media&#x26;token=90cfa665-458d-4441-b827-765ac16df481" alt=""><figcaption><p>Setting a rule for duplicate reports</p></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

{% hint style="warning" %}

## Noise Alert

Rules based on **tags** can get noisy if you rely heavily on tags in your workflow. This rule **triggers every time** a new tag is added to the report.
{% endhint %}

{% hint style="info" %}

## Why are Master & Duplicate reports tagged?

For 3rd-party integration tools that support 2-way tag sync (for example, Jira), these tags can show up in those tools. They help you identify the report type outside the Luciq dashboard.&#x20;

<p align="center"><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FB2xX6sWdOncl1HtX2Swh%2FScreenshot%202026-02-24%20at%202.42.31%E2%80%AFPM.png?alt=media&#x26;token=d489c280-5435-4859-9d9a-5e4ec6a6de47" alt="" data-size="original"></p>
{% endhint %}

***

## Good to know

* By default, our **Triage Agent** adds a comment in the Activity & Comments section when a new **duplicate report** is added to a **master report.**&#x20;
* This comment is then be shown in **Jira** (or other integrations that support syncing of comments) to update you on the volume of duplicate reports received.

{% columns %}
{% column %}

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F3oPVCgYU5VAKMN6jmnHP%2FScreenshot%202026-02-24%20at%202.57.54%E2%80%AFPM.png?alt=media&#x26;token=a2a51578-b2dc-4b3b-acec-8221773ec3c6" alt=""><figcaption><p>Triage Agent's comment on Luciq's dashboard</p></figcaption></figure>
{% endcolumn %}

{% column %}

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FqFO0ob2Lgcc2FQNXDJCY%2FScreenshot%202026-02-24%20at%202.58.17%E2%80%AFPM.png?alt=media&#x26;token=fadba23e-95e1-4bdb-b6c1-4afc8eb40195" alt=""><figcaption><p>Triage Agent's comment inside the Jira ticket</p></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

{% hint style="info" %}

## Note on comments syncing

Make sure you enable the Comment One-way Sync from Luciq to Jira for the comments to reflect on Jira.

<p align="center"><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2Fa9nvFMRnpH26iIAh4t9N%2FScreenshot%202026-02-24%20at%203.02.37%E2%80%AFPM.png?alt=media&#x26;token=4e232175-cb57-4c95-b9be-1c6387faee84" alt="" data-size="original"></p>
{% endhint %}
