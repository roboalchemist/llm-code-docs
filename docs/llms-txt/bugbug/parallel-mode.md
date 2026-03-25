# Source: https://docs.bugbug.io/running-tests/parallel-mode.md

# Parallel runs

## Why run tests in parallel?

You can run your tests [in the cloud](https://docs.bugbug.io/running-tests/in-cloud-on-server) *in parallel*, which means that more than one test will be executed at the same time. Multiple tests will run simultaneously, resulting in **up to 32x shorter testing time.**

You can have up to 32 parallel runs, depending on your subscription plan.

## Parallel testing pricing

You can purchase parallel runs on the **PRO** and **BUSINESS** plans—either directly in the BugBug app or when selecting your plan.

Each additional parallel run costs **$80/month** for users on a monthly subscription.\
If you're on an annual plan, you’ll receive a **15% discount** on this price.

**PRO** plan pricing with extra parallels

<table><thead><tr><th width="212">Number of parallel test runs</th><th width="70">-</th><th width="73">2</th><th width="78">4</th><th width="87">8</th><th width="94">16</th><th>32</th></tr></thead><tbody><tr><td>Billed monthly</td><td>$219</td><td>$299</td><td>$459</td><td>$779</td><td>$1,419</td><td>$2,699</td></tr><tr><td>Billed yearly</td><td>$189</td><td>$257</td><td>$393 </td><td>$665</td><td>$1,209</td><td>$2,297</td></tr></tbody></table>

**BUSINESS** plan pricing with extra parallels

<table><thead><tr><th width="212">Number of parallel test runs</th><th width="70">-</th><th width="73">2</th><th width="78">4</th><th width="87">8</th><th width="94">16</th><th>32</th></tr></thead><tbody><tr><td>Billed monthly</td><td>$659</td><td>$739</td><td>$899</td><td>$1,219</td><td>$1,859</td><td>$3,139</td></tr><tr><td>Billed yearly</td><td>$559</td><td>$627</td><td>$763 </td><td>$1,035</td><td>$1,579</td><td>$2,667</td></tr></tbody></table>

## Enable parallel runs

1. Go to **Suites** view
2. Edit or create a suite
3. Change the option for Parallel cloud runs

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FLWiceSCVQhGi8kvZrnUe%2Fimage.png?alt=media\&token=03b1471e-b2b1-42b5-a5cb-3a9b75c41366)

When you trigger suite to run, your tests in that suite will run in parallel.&#x20;

{% hint style="info" %}
**Parallel testing is only possible when tests are** [**run in the cloud**](https://docs.bugbug.io/running-tests/in-cloud-on-server)

Suites run in your local browser will always run sequentially because your browser cookies and storage are shared among all incognito windows, so only one test can be run at a time.&#x20;

All cloud runs can be performed in parallel, regardless of whether they are manually triggered or [initiated via API](https://docs.bugbug.io/running-tests/running-via-api).
{% endhint %}

## Parallel runs within your organization

**Parallel runs let you run more than 1 test at the same time.**&#x20;

The number of tests you can simultaneously run within your [organization](https://docs.bugbug.io/collaboration/organization-settings#what-are-organizations) depends on your subscription plan.

If you are using BugBug with one of the paid subscriptions, you can run tests in the cloud, but only 1 test can be in progress at the same time.&#x20;

If you have multiple projects and run tests at the same time, they will be queued, they won't run in parallel - they will be executed one by one.&#x20;

**To run more tests in parallel you need to upgrade to one of the paid plans and purchase parallel runs either directly in the BugBug app or when selecting your plan.**

We support up to 32 parallel tests.
