# Source: https://firebase.google.com/docs/test-lab/usage-quotas-pricing.md.txt

# Usage levels, quotas, and pricing for Test Lab

Firebase Test Lab and [Android Device
Streaming](https://developer.android.com/studio/run/android-device-streaming)
provide a Cloud API quota and a testing quota, which is included in the standard
Spark and Blaze pricing
plans. These quotas are based on your project's usage of the [testing
resource](https://firebase.google.com/docs/test-lab/usage-quotas-pricing#testing-quota), [device resource](https://firebase.google.com/docs/test-lab/usage-quotas-pricing#device-streaming) or [Cloud
API](https://firebase.google.com/docs/test-lab/usage-quotas-pricing#cloud-api-quota).

These quotas are applied project-level, not site-level. These limits are shared
across all APIs (including instrumentation tests, Robo tests, and Game Loop
tests) and test matrixes. When you run a test, you can check its run time (i.e.,
the time it takes the test to run) under **Test execution and test matrix
results** in the Firebase console. When using Android Device Streaming, you
can check your project's usage in either Android Studio or
Google Cloud console. Run times are displayed next to each device. If you're in
the Blaze plan, the test run times are used for billing.

> [!CAUTION]
> When your project is on the Blaze pricing plan, [**set up budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) using the console. You can use the [Blaze plan calculator](https://firebase.google.com/pricing#blaze-calculator) to estimate your monthly costs.
>
> Be aware that **budget alerts do *not* cap your usage or
> charges** --- they are *alerts* about your costs so that you can
> take action, if needed. For example, you might consider
> [using
> budget notifications to programmatically disable Cloud Billing on a
> project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

## **Quotas**

### Testing quota

Test Lab's testing quota is measured by the
number of test runs per day:

- **Spark plan (no-cost)**: The resource limits are
  listed for up to 15 test runs per day in total:

  - 10 test runs per day on virtual devices

  - 5 test runs per day on physical devices

- **Blaze plan** : Not all projects in the Blaze plan have the same quotas. If
  your usage of Google Cloud increases over time, your quotas might increase
  correspondingly. If you expect a sizable upcoming increase in usage, you can
  proactively request [quota adjustments](https://firebase.google.com/docs/test-lab/usage-quotas-pricing#increase-cloud-quotas).

  Billing is calculated by the minutes spent running tests. The Blaze plan
  begins with a no-cost time limit that's similar to the resource limit offered
  by the Spark plan:
  - 30 minutes of test time per day on physical devices

  - 60 minutes of test time per day on virtual devices

  Any usage above these limits is charged according to the following hourly
  rates:
  - $5 per hour for each physical device

  - $1 per hour for each virtual device

Charges are calculated on a per-minute basis, rounded up to the nearest
minute. For example, a 22-second test is billed for one minute, while a
75-second test is billed for two minutes. You are charged only for the
time spent running tests (the time it takes to install your app
and collect test results will not be charged).

You can monitor your testing quota usage in the
[Google Cloud console](https://console.cloud.google.com/apis/api/testing.googleapis.com/quotas).

### Cloud API quotas

The Testing and Tool Results APIs come with two API limits: requests per day per
project, and requests per minute per project.

- Cloud Testing API limit (including calls for Android Device Streaming):

  - 10,000,000 calls per day
  - 120,000 calls per 1-minute interval

  You can monitor your usage of this API in the
  [Google Cloud console](https://console.cloud.google.com/apis/api/testing.googleapis.com/quotas).
- Cloud Tool Results API limit:

  - 200,000 calls per day
  - 2,400 calls per 1-minute interval

  You can monitor your usage of this API in the
  [Google Cloud console](https://console.cloud.google.com/apis/api/toolresults.googleapis.com/quotas).

## Android Device Streaming quotas

- **(no cost) Spark plan**: 30 no cost minutes per project, per month
- **Blaze plan**: 30 no cost minutes per project, per month, 15 cents for each additional minute

Not all projects in the Blaze plan have the same quotas. If your usage of
Google Cloud console increases over time, your quotas might increase
correspondingly. If you expect a sizable upcoming increase in usage, you can
proactively request [quota adjustments](https://firebase.google.com/docs/test-lab/usage-quotas-pricing#increase-cloud-quotas).

## Increase quotas

If you've reached a Cloud API or Blaze plan testing quota, you can request a
higher limit by doing one of the following:

- [Requesting a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota)
  directly in the Google Cloud console.

- Contacting [Firebase support](https://support.google.com/firebase/contact/support).