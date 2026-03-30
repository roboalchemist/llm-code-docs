# Source: https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024.md.txt

# FAQs about changes to Cloud Storage for Firebase pricing and default buckets

<br />

As announced in September 2024, Firebase is making some changes to
Cloud Storage for Firebase and taking proactive steps to prevent abuse on our
platform. This requires us to update our infrastructure to better align with
Google Cloud Storage quota and billing.

One result of these infrastructure changes is that **we now require projects to
be on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) to use Cloud Storage for Firebase. No-cost
usage is still available even on the Blaze pricing plan.**

> [!CAUTION]
> If you have an `*.appspot.com` default bucket, your Firebase project must be upgraded to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) by **February 03, 2026** to maintain access to your default bucket. Learn more about this requirement on this page.
>
> [**Learn about the expected experience
> (like 402 and 403 errors) if you haven't yet upgraded.**](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#errors)
>
> Note that in our original announcement back in September 2024, this
> requirement to be on the Blaze pricing plan was in October 2025.
> However, to give you more time to prepare and avoid disruptions during the
> busy end-of-year season, we've now extended the deadline for this
> requirement to be February 03, 2026.

Review the following FAQs for details about the changes:

- [Changes for pricing plan requirements](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-pricing-plan-reqs)
- [Changes for the default Cloud Storage for Firebase bucket](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-default-storage-bucket)
- [Changes for programmatic interactions (like REST APIs and Terraform)](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-programmatic-interactions)
- [Changes for "default Google Cloud resources"](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-default-gcp-resources)

<br />

*** ** * ** ***

## Expected experience if you haven't upgraded

**What will happen:** Starting
February 03, 2026, if you have an
`*.appspot.com` default bucket, and your Firebase project is
*still on the Spark pricing plan*, you'll lose console access to your
bucket and your API calls will start returning 402 and 403 errors.

**What you need to do:** To regain access and quality of service, upgrade to the
[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing). No-cost usage is still available even on the
Blaze pricing plan.

### No access in console

**You'll no longer have access to your bucket in the Firebase console and the
Google Cloud console.** Instead, you'll be redirected to the Cloud Storage
landing page where you can upgrade to the Blaze pricing plan.

### 402 and 403 errors

**Your calls to Cloud Storage APIs (like from your app) will start failing and
returning 402 or 403 errors.**

##### 402 errors

    "error": {
        "code": 402,
        "message": "Cloud Storage for Firebase no longer supports Firebase projects that are on the no-cost Spark pricing plan. Please upgrade to the pay-as-you-go Blaze pricing plan to maintain access to your default bucket and all other Cloud Storage resources. For details, see our FAQ: https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024"
      }

OR

    storage/quota-exceeded: Firebase Storage: Quota for bucket '{project-id}.appspot.com' exceeded, please view quota on https://firebase.google.com/pricing/. (storage/quota-exceeded)

##### 403 errors

    <Error>
      <Code>UserProjectAccountProblem</Code>
      <Message>The project to be billed is associated with an absent billing account.</Message>
      <Details>The billing account for the owning project is disabled in state absent</Details>
    </Error>

OR

    storage/unauthorized: User does not have permission to access {path}

### Troubleshooting

If you're experiencing any issues, check out these troubleshooting resources. If
none of the following help with your issue, then
[reach out to Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

#### Troubleshoot billing setup

The Cloud Billing documentation provides
[troubleshooting help for common billing and payment issues](https://support.google.com/a/topic/2413217).
For example, you can find solutions if your
[Indian debit or credit card isn't accepted](https://support.google.com/a/answer/3401127).

#### Troubleshoot service account permissions

For Cloud Storage for Firebase to function properly, a service account in your
Firebase project needs certain IAM permissions.

If you get errors in the Firebase console about permissions for this
service account, it's often because the service account has been deleted from
your Firebase project. To resolve this issue, follow the steps described in
[this FAQ](https://firebase.google.com/support/faq#storage-accounts).

<br />

*** ** * ** ***

## Changes for pricing plan requirements

We now require the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) if you want to use
Cloud Storage for Firebase. **No-cost usage is still available even on the
Blaze pricing plan.**

> [!NOTE]
> **Important** : Here are the summarized key points of the FAQs in this section (but make sure to review each FAQ below for details):
>
> - **Starting
>   October 30, 2024** , your Firebase project must be on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) to provision a new Cloud Storage for Firebase default bucket. The bucket can optionally use the ["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free) for Google Cloud Storage.
> - **Starting
>   February 03, 2026** , your Firebase project must be on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) to maintain access to your default bucket and all other Cloud Storage resources. Any `*.appspot.com` default bucket will maintain its current no-cost level of usage even on the Blaze pricing plan.

We understand that these changes will require your time to evaluate and make
changes to your Firebase project and workflows. If you have any questions,
please reach out to [Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

#### What are the new pricing plan requirements announced in September 2024?

<br />

- **Starting October 30, 2024, the following
  changes will happen:**

  - To provision a new default bucket using the Firebase console or REST API,
    your project must be on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing).

  - Note the following about all default buckets **provisioned after
    October 30, 2024**:

    - They will follow
      [Google Cloud Storage pricing and usage](https://cloud.google.com/storage/pricing),
      which provides an ["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free) for buckets in
      `US-CENTRAL1`, `US-EAST1`, and `US-WEST1`.

    - They will have a name format of `PROJECT_ID.firebasestorage.app`
      (instead of the former `PROJECT_ID.appspot.com`).

- **Starting February 03, 2026, the following
  changes will happen:**

  - To maintain access to your default bucket and all other Cloud Storage resources, your project must be on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing). Any `*.appspot.com` default bucket will maintain its current no-cost level of usage even on the Blaze pricing plan.

Learn more about
[what happens if you don't upgrade to the Blaze pricing plan](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#what-happens-if-no-upgrade-to-blaze)
by this date. If you have any questions, please reach out to
[Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

<br />

<br />

#### Why is Firebase making these pricing plan changes?

<br />

Firebase strives to keep our products and our ecosystem safe and secure. As part
of that, we're making some changes to Cloud Storage for Firebase and taking
proactive steps to prevent abuse on our platform. This includes updating our
infrastructure to better align with Google Cloud Storage quota and billing.

<br />

<br />

<br />

#### Can I keep no-cost usage if I upgrade to the Blaze pricing plan?

<br />

Yes. If you have a `PROJECT_ID.appspot.com` default bucket and you
upgrade to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), then you will maintain your default
bucket's current no-cost level of usage, as described below. Any usage over this
no-cost usage will be charged according to
[Google App Engine pricing](https://cloud.google.com/appengine/pricing).

- 5 GB stored
- 1 GB downloaded / day
- 20,000 uploads / day
- 50,000 downloads / day

Note that **starting October 30, 2024** , all new
default buckets have the name format of `PROJECT_ID.firebasestorage.app`
and they follow
[Google Cloud Storage pricing and usage](https://cloud.google.com/storage/pricing),
which provides an ["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free) for buckets in
`US-CENTRAL1`, `US-EAST1`, and `US-WEST1`.

<br />

<br />

<br />

#### How do I upgrade to the Blaze pricing plan?

<br />

To upgrade your project to the pay-as-you-go Blaze pricing plan, you need to link your
project with a
[Cloud Billing account](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#cloud-billing-accounts).
You can
[use the Firebase console workflow to upgrade your pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).

To upgrade the pricing plan, you need to have the IAM role of
[Owner](https://firebase.google.com/docs/projects/iam/roles-basic) for your project.

> [!IMPORTANT]
> **Important:** When you upgrade to the Blaze pricing plan, we strongly recommend setting up [budget alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails). The console flow for upgrading your pricing plan automatically prompts you to set up this alert. Learn more about [avoiding surprise bills](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills).

If you have any questions, please reach out to [Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

<br />

<br />

#### When do I need to upgrade to the Blaze pricing plan?

<br />

If you want to maintain access to your `PROJECT_ID.appspot.com` default
bucket, then you need to **upgrade to the pay-as-you-go Blaze pricing plan plan
by February 03, 2026**.

To upgrade your project to the pay-as-you-go Blaze pricing plan, you need to link your
project with a
[Cloud Billing account](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#cloud-billing-accounts).
You can
[use the Firebase console workflow to upgrade your pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).

<br />

<br />

<br />

#### What if I don't upgrade my project to the Blaze pricing plan?

<br />

- **Starting October 30, 2024** : If you haven't
  yet provisioned a default Cloud Storage bucket in your project, then you won't be
  able to provision it unless your project is on the Blaze pricing plan.

- **Starting February 03, 2026** : If your
  project isn't on the Blaze pricing plan, then you'll lose read/write
  access to your `PROJECT_ID.appspot.com` default bucket. You also won't
  be able to view the bucket or access its data in the Firebase console or
  the Google Cloud console.

  Note that any data will remain in your bucket, but it will be inaccessible
  until you upgrade to the Blaze pricing plan.

If you have any questions, please reach out to [Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

<br />

<br />

#### What happens if my `*.appspot.com` default bucket's usage is over the no-cost usage level ?

<br />

If you have a `PROJECT_ID.appspot.com` default bucket, and you upgrade to
the Blaze pricing plan with a usage that's over the no-cost usage
levels described below, then you will be charged for the overage according to
[Google App Engine pricing](https://cloud.google.com/appengine/pricing)
on your next billing cycle.

- 5 GB stored
- 1 GB downloaded / day
- 20,000 uploads / day
- 50,000 downloads / day

If you have any questions, please reach out to [Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

<br />

<br />

*** ** * ** ***

## Changes for the default Cloud Storage bucket

> [!NOTE]
> **Important** : Here are the summarized key points of the FAQs in this section (but make sure to review each FAQ below for details):
>
> - **Starting
>   October 30, 2024** , all *newly provisioned* default Cloud Storage buckets will have the name format of `PROJECT_ID.firebasestorage.app`.  
>   These buckets will follow [Google Cloud Storage pricing and usage](https://cloud.google.com/storage/pricing), which provides an ["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free) for buckets in `US-CENTRAL1`, `US-EAST1`, and `US-WEST1`.
> - There are no changes to any existing `PROJECT_ID.appspot.com` default buckets (as long as you upgrade your project to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) by February 03, 2026).

We understand that these changes will require your time to evaluate and make
changes to your Firebase project and workflows. If you have any questions,
please reach out to [Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

#### Will the name of my default bucket change?

<br />

No. When you upgrade to the Blaze pricing plan, the name of your
default Cloud Storage bucket will ***not*** change.

- **If you provisioned your default bucket *before*
  October 30, 2024** , then your default bucket
  will always have a name format of `PROJECT_ID.appspot.com`.

  The only exception is if you
  [delete your `*.appspot.com` bucket](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#what-happens-if-delete-appspot-bucket)
  and provision a new default bucket.
- **If you provisioned your default bucket *on or after*
  October 30, 2024** , then your default bucket
  will always have a name format of `PROJECT_ID.firebasestorage.app`.

<br />

<br />

<br />

#### What happens if I delete my `*.appspot.com` default bucket?

<br />

A deleted bucket is restorable using the Cloud Storage
[Buckets: restore](https://cloud.google.com/storage/docs/json_api/v1/buckets/restore)
API until its hard delete time has elapsed.

**Starting October 30, 2024** : If you delete your
`PROJECT_ID.appspot.com` default bucket, then you won't be able to
provision a bucket with that same name format.

Instead, you can create a new default Cloud Storage bucket (if your project is on
the Blaze pricing plan) that has a name format of
`PROJECT_ID.firebasestorage.app`. It will follow
[Google Cloud Storage pricing and usage](https://cloud.google.com/storage/pricing),
which provides an ["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free) for buckets in
`US-CENTRAL1`, `US-EAST1`, and `US-WEST1`.

<br />

<br />

<br />

#### Do I need to update my app's codebase?

<br />

No. To accommodate these changes, you do ***not*** need to update your app's
codebase.

All existing `PROJECT_ID.appspot.com` default buckets will maintain their
name format.

To avoid any service interruptions, make sure to upgrade your project to the
[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) by February 03, 2026.
After upgrading to the Blaze pricing plan, your codebase will continue
to interact with the `PROJECT_ID.appspot.com` default bucket as it always
has.

<br />

<br />

<br />

#### Do I need to move my data out of my `*.appspot.com` default bucket?

<br />

No. To accommodate these changes, you do ***not*** need to move your data out of
your `PROJECT_ID.appspot.com` default bucket.

As long as you upgrade your project to the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) by
February 03, 2026, then you'll see no service
interruptions.

<br />

<br />

<br />

*** ** * ** ***

## Changes for programmatic interactions (like REST APIs and Terraform)

If you provision or work with default Cloud Storage for Firebase buckets
programmatically (for example, using REST APIs or Terraform), review the
following changes to see if you need to change anything in your workflows or
apps.

> [!NOTE]
> **Important** : Here are the summarized key points of the FAQs in this section (but make sure to review each FAQ below for details):
>
> - On **October 30, 2024** , two REST APIs are shutting down: the [`projects.defaultLocation.finalize`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.defaultLocation/finalize) endpoint and the [`projects.availableLocations.list`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list) endpoint.
> - The changes to these REST APIs also affect how you might use Terraform with Cloud Storage for Firebase (and possibly Cloud Firestore).

We understand that these changes will require your time to evaluate and make
changes to your Firebase project and workflows. If you have any questions,
please reach out to [Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

#### What are the changes for using REST APIs?

<br />

**Starting October 30, 2024**, the following
changes will happen:

- The [`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create) endpoint is changing:

  - To call this endpoint, your project must be on the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing).

  - The default buckets provisioned by this endpoint will have the name format
    of `PROJECT_ID.firebasestorage.app` (instead of the former
    `PROJECT_ID.appspot.com`).

  - These default buckets will follow Google Cloud Storage pricing and
    usage, which provides an ["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free) for buckets in
    `US-CENTRAL1`, `US-EAST1`, and `US-WEST1`.

- The [`projects.defaultLocation.finalize`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.defaultLocation/finalize) and
  [`projects.availableLocations.list`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list) endpoints will be shutdown and will
  start returning `404: METHOD_NOT_FOUND` errors.

  Instead, to set a resource's location programmatically, you should use the
  resource-specific APIs. For example, set the locations of the default
  Cloud Storage bucket and the default Cloud Firestore instance during their
  individual provisioning when calling [`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create)
  and [`projects.databases.create`](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/create), respectively. For more details
  about replacements for REST APIs and locations, see the FAQ:
  [How do I set or get the location for a "default Google Cloud resource"?](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#set-get-location-for-default-gcp-resources)

<br />

<br />

<br />

#### What are the changes for using Terraform?

<br />

**Starting October 30, 2024** , the following
changes will happen that are related to using Terraform with
Cloud Storage for Firebase.

You can no longer provision the default Cloud Storage for Firebase bucket using
Terraform. This is because you can no longer provision this bucket via
Google App Engine. Instead, you can do one of the following:

- Provision the bucket by calling [`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create).
  This API is not yet available via Terraform.

- Provision the bucket through the Firebase console. Visit the
  [***Storage*** section](https://console.firebase.google.com/project/_/storage)
  of the console to get started.

Additionally, note the following about default Cloud Storage buckets provisioned
starting October 30, 2024:

- Your project must be on the pay-as-you-go Blaze pricing plan to provision a
  default Cloud Storage bucket.

- You no longer need to provision your default Cloud Firestore instance before
  your default Cloud Storage bucket.

- The location you select for your default Cloud Firestore instance is not
  applicable to your default Cloud Storage bucket (this means that your default
  Cloud Firestore instance and your default Cloud Storage bucket can be in different
  locations).

- The name format of the default Cloud Storage bucket will be
  `PROJECT_ID.firebasestorage.app` (instead of the former
  `PROJECT_ID.appspot.com`).

<br />

<br />

<br />

*** ** * ** ***

## Changes for "default Google Cloud resources"

The ["default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location)
are any project resources associated with Google App Engine, including
the following:

- default Cloud Firestore instance
- default Cloud Storage for Firebase bucket (specifically those with the name format of `PROJECT_ID.appspot.com`)
- Google Cloud Scheduler (specifically for 1st gen scheduled functions)

With many changes over the years to the Firebase ecosystem, the associations of
Firebase-related resources to Google App Engine have been changing.

We understand that these changes will require your time to evaluate and make
changes to your Firebase project and workflows. If you have any questions,
please reach out to [Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

#### What's happening to the "location for default Google Cloud resources"?

<br />

The ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location)
is the location setting for any project resources associated with
Google App Engine, including the following:

- default Cloud Firestore instance
- default Cloud Storage for Firebase bucket (specifically those with the name format of `PROJECT_ID.appspot.com`)
- Google Cloud Scheduler (specifically for 1st gen scheduled functions)

When you set up any one of these resources in your project, you're transitively
setting the location of the Google App Engine app in your project.
This, in turn, sets the location for all the resources associated with
Google App Engine.

> [!IMPORTANT]
> **Important:** **Starting October 30, 2024** , provisioning the default Cloud Storage bucket will not set the "location for default Google Cloud resources" (like the location for the project's default Cloud Firestore instance). Also, provisioning the default Cloud Firestore instance will no longer set the location for a new default Cloud Storage bucket (those with the name format of `PROJECT_ID.firebasestorage.app`).

Note the following:

- **Any default Cloud Storage bucket provisioned *before*
  October 30, 2024** (with a name format of
  `PROJECT_ID.appspot.com`) is associated with
  Google App Engine. This means the following:

  - The bucket's location will set the location of resources associated with Google App Engine (like the location of the default Cloud Firestore instance).
- **Any default Cloud Storage bucket provisioned starting
  October 30, 2024** (with the name format of
  `PROJECT_ID.firebasestorage.app`) is ***not*** associated with
  Google App Engine. This means the following:

  - Provisioning your default Cloud Storage bucket will no longer set the location
    of resources associated with Google App Engine (like the location
    of the default Cloud Firestore instance).

  - Provisioning your default Cloud Firestore instance will no longer set the
    location of your project's default Cloud Storage bucket.

  - The locations available for your default Cloud Storage bucket are now the same
    [locations available for Google Cloud Storage](https://cloud.google.com/storage/docs/locations#available-locations)
    (rather than limited to those for Google App Engine).

<br />

<br />

<br />

#### How do I set or get the location for a "default Google Cloud resource"?

<br />

The ["default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location)
are any project resources associated with Google App Engine, including
the following:

- default Cloud Firestore instance
- default Cloud Storage for Firebase bucket (specifically those with the name format of `PROJECT_ID.appspot.com`)
- Google Cloud Scheduler (specifically for 1st gen scheduled functions)

**Starting October 30, 2024** , the concept of
"default Google Cloud resources" doesn't apply to *newly provisioned* default
Cloud Storage buckets. Default buckets provisioned *after* this date have the name
format of `PROJECT_ID.firebasestorage.app`, and they are ***not***
associated with Google App Engine. To learn more, review the FAQ:
[What happens to the "location for default Google Cloud resources"?](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#location-for-default-gcp-resources)

> [!IMPORTANT]
> **Important:** Since default Cloud Storage buckets provisioned starting October 30, 2024 aren't associated with Google App Engine, their location will ***not*** set the "location for default Google Cloud resources" (like the location for the default Cloud Firestore instance). Also, provisioning the default Cloud Firestore instance *first* in your project will no longer set the location for these new default Cloud Storage buckets.

If you want to set or get the location for any resource in a project, then you
should interact directly with the resource instead.

##### Default Cloud Storage for Firebase bucket

- **In the Firebase console:**

  - Set and find the location of a default Cloud Storage bucket in the [***Storage*** section](https://console.firebase.google.com/u/0/project/_/storage) of the Firebase console.
- **Using REST APIs:**

  - Set the location of a default Cloud Storage bucket during its provisioning
    when calling [`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create).

    Note that starting October 30, 2024,
    calling this endpoint will require the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing). So before
    attempting to create a default bucket, make sure that the project is
    linked to a Cloud Billing account (for example, using
    [`projects.updateBillingInfo`](https://cloud.google.com/billing/docs/reference/rest/v1/projects/updateBillingInfo)).
  - Get the location of a default Cloud Storage bucket using
    [`projects.buckets.get`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/get).

##### Default Cloud Firestore instance

Note that if you provisioned a default Cloud Storage bucket before
October 30, 2024, then the location of the
project's default Cloud Firestore instance has already been set (due to
associations with Google App Engine).

- **In the Firebase console:**

  - Set and find the location of a default Cloud Firestore instance in the [***Firestore*** section](https://console.firebase.google.com/u/0/project/_/firestore) of the Firebase console.
- **Using REST APIs:**

  - Set the location of a default Cloud Firestore instance during its provisioning
    when calling [`projects.databases.create`](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/create).

  - Get the location of a default Cloud Firestore instance using
    [`projects.databases.get`](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/get).

##### Scheduled functions (1st gen)

Note that if you provisioned a default Cloud Storage bucket before
October 30, 2024, then the project's scheduled
functions (1st gen) has already been set (due to associations with
Google App Engine).

- Set the location of a scheduled function during its
  [setup and deployment](https://firebase.google.com/docs/functions/schedule-functions?gen=2nd).

- Get the location of a scheduled function from the topic name of its job and function in the
  [Google Cloud console](https://console.cloud.google.com/project/_/cloudscheduler)
  (`firebase-schedule-FUNCTION_NAME-REGION`.

<br />

<br />