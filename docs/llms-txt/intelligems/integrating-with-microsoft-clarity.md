# Source: https://docs.intelligems.io/integrations/heatmap-integrations/integrating-with-microsoft-clarity.md

# Microsoft Clarity

## Introduction

The Intelligems Microsoft Clarity integration tags visitor sessions with experiment data, allowing you to analyze behavior patterns across different test groups.

## **How It Works**

Enable the Microsoft Clarity integration on the Integrations page in Intelligems.

{% hint style="info" %}
Note that when you set up the Microsoft Clarity integration, you will not need to enter any login information - we use Microsoft Clarity's window API to authenticate.
{% endhint %}

Once active, Microsoft Clarity sessions will include events tagged with test group information following this pattern: \<Experiment Name> - \<Test Group Name> allowing you to view/filter sessions in Clarity by experiment name and test group name. You can filter by `experiment_name` or `ig_test_group` under the custom tags as seen below:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9f977cd0bfa7e005a282824f01a041ff88fd370c%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

## **Benefits**

Filter and compare sessions in Clarity by experiment to understand how different variations affect user behavior. See which test groups have higher engagement, where visitors drop off, or how different audiences interact with your site.
