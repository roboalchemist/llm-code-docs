# Source: https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024.md.txt

<br />

Firebase is making some changes toCloud Storage for Firebaseand taking proactive steps to prevent abuse on our platform. This requires us to update our infrastructure to better align withGoogle Cloud Storagequota and billing.

One result of these infrastructure changes is that**we'll soon start requiring projects to be on the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)to useCloud Storage for Firebase. No-cost usage is still available even on the Blaze pricing plan.**

Review the following FAQs about the changes we announced in September 2024:

- [Changes for pricing plan requirements](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-pricing-plan-reqs)
- [Changes for the defaultCloud Storage for Firebasebucket](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-default-storage-bucket)
- [Changes for programmatic interactions (like REST APIs and Terraform)](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-programmatic-interactions)
- [Changes for "defaultGoogle Cloudresources"](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#all-changes-default-gcp-resources)

| If you have an`*.appspot.com`default bucket, your Firebase project must be upgraded to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)by**as early as February 02, 2026** to maintain access to your default bucket. Learn more about this requirement on this page.
|
| Note that in our original announcement back in September 2024, this requirement to be on the Blaze pricing plan was in October 2025. However, to give you more time to prepare and avoid disruptions during the busy end-of-year season, we've now extended the deadline for this requirement to beas early as February 02, 2026.

## **Changes for pricing plan requirements**

We'll soon start requiring the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)if you want to useCloud Storage for Firebase.**No-cost usage is still available even on the Blaze pricing plan.**
| **Important** : Here are the summarized key points of the FAQs in this section (but make sure to review each FAQ below for details):
|
| - **StartingOctober 30, 2024** , your Firebase project must be on the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)to provision a newCloud Storage for Firebasedefault bucket. The bucket can optionally use the["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free)forGoogle Cloud Storage.
| - **Startingas early as February 02, 2026** , your Firebase project must be on the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)to maintain access to your default bucket and all otherCloud Storageresources. Any`*.appspot.com`default bucket will maintain its current no-cost level of usage even on the Blaze pricing plan.

We understand that these changes will require your time to evaluate and make changes to your Firebase project and workflows. If you have any questions, please reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

#### What are the new pricing plan requirements announced in September 2024?

<br />

- **StartingOctober 30, 2024, the following changes will happen:**

  - To provision a new default bucket using theFirebaseconsole or REST API, your project must be on the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing).

  - Note the following about all default buckets**provisioned afterOctober 30, 2024**:

    - They will follow[Google Cloud Storagepricing and usage](https://cloud.google.com/storage/pricing), which provides an["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free)for buckets in`US-CENTRAL1`,`US-EAST1`, and`US-WEST1`.

    - They will have a name format of<var translate="no">PROJECT_ID</var>`.firebasestorage.app`(instead of the former<var translate="no">PROJECT_ID</var>`.appspot.com`).

- **Startingas early as February 02, 2026, the following changes will happen:**

  - To maintain access to your default bucket and all otherCloud Storageresources, your project must be on the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing). Any`*.appspot.com`default bucket will maintain its current no-cost level of usage even on the Blaze pricing plan.

Learn more about[what happens if you don't upgrade to the Blaze pricing plan](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#what-happens-if-no-upgrade-to-blaze)by this date. If you have any questions, please reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

<br />

<br />

#### Why is Firebase making these pricing plan changes?

<br />

Firebase strives to keep our products and our ecosystem safe and secure. As part of that, we're making some changes toCloud Storage for Firebaseand taking proactive steps to prevent abuse on our platform. This includes updating our infrastructure to better align withGoogle Cloud Storagequota and billing.

<br />

<br />

<br />

#### Can I keep no-cost usage if I upgrade to the Blaze pricing plan?

<br />

Yes. If you have a<var translate="no">PROJECT_ID</var>`.appspot.com`default bucket and you upgrade to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), then you will maintain your default bucket's current no-cost level of usage, as described below. Any usage over this no-cost usage will be charged according to[GoogleApp Enginepricing](https://cloud.google.com/appengine/pricing).

- 5 GB stored
- 1 GB downloaded / day
- 20,000 uploads / day
- 50,000 downloads / day

Note that**startingOctober 30, 2024** , all new default buckets have the name format of<var translate="no">PROJECT_ID</var>`.firebasestorage.app`and they follow[Google Cloud Storagepricing and usage](https://cloud.google.com/storage/pricing), which provides an["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free)for buckets in`US-CENTRAL1`,`US-EAST1`, and`US-WEST1`.

<br />

<br />

<br />

#### How do I upgrade to the Blaze pricing plan?

<br />

To upgrade your project to the pay-as-you-go Blaze pricing plan, you need to link your project with a[Cloud Billingaccount](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#cloud-billing-accounts). You can[use theFirebaseconsole workflow to upgrade your pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).

To upgrade the pricing plan, you need to have the IAM role of[Owner](https://firebase.google.com/docs/projects/iam/roles-basic)for your project.
| **Important:** When you upgrade to the Blaze pricing plan, we strongly recommend setting up[budget alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails). The console flow for upgrading your pricing plan automatically prompts you to set up this alert. Learn more about[avoiding surprise bills](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills).

If you have any questions, please reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

<br />

<br />

#### When do I need to upgrade to the Blaze pricing plan?

<br />

If you want to maintain access to your<var translate="no">PROJECT_ID</var>`.appspot.com`default bucket, then you need to**upgrade to the pay-as-you-go Blaze pricing plan plan byas early as February 02, 2026**.

To upgrade your project to the pay-as-you-go Blaze pricing plan, you need to link your project with a[Cloud Billingaccount](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#cloud-billing-accounts). You can[use theFirebaseconsole workflow to upgrade your pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).

<br />

<br />

<br />

#### What if I don't upgrade my project to the Blaze pricing plan?

<br />

- **StartingOctober 30, 2024** : If you haven't yet provisioned a defaultCloud Storagebucket in your project, then you won't be able to provision it unless your project is on the Blaze pricing plan.

- **Startingas early as February 02, 2026** : If your project isn't on the Blaze pricing plan, then you'll lose read/write access to your<var translate="no">PROJECT_ID</var>`.appspot.com`default bucket. You also won't be able to view the bucket or access its data in theFirebaseconsole or theGoogle Cloudconsole.

  Note that any data will remain in your bucket, but it will be inaccessible until you upgrade to the Blaze pricing plan.

If you have any questions, please reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

<br />

<br />

#### What happens if my`*.appspot.com`default bucket's usage is over the no-cost usage level ?

<br />

If you have a<var translate="no">PROJECT_ID</var>`.appspot.com`default bucket, and you upgrade to the Blaze pricing plan with a usage that's over the no-cost usage levels described below, then you will be charged for the overage according to[GoogleApp Enginepricing](https://cloud.google.com/appengine/pricing)on your next billing cycle.

- 5 GB stored
- 1 GB downloaded / day
- 20,000 uploads / day
- 50,000 downloads / day

If you have any questions, please reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

<br />

## **Changes for the defaultCloud Storagebucket**

| **Important** : Here are the summarized key points of the FAQs in this section (but make sure to review each FAQ below for details):
|
| - **StartingOctober 30, 2024** , all*newly provisioned* defaultCloud Storagebuckets will have the name format of<var translate="no">PROJECT_ID</var>`.firebasestorage.app`.  
|   These buckets will follow[Google Cloud Storagepricing and usage](https://cloud.google.com/storage/pricing), which provides an["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free)for buckets in`US-CENTRAL1`,`US-EAST1`, and`US-WEST1`.
| - There are no changes to any existing<var translate="no">PROJECT_ID</var>`.appspot.com`default buckets (as long as you upgrade your project to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)byas early as February 02, 2026).

We understand that these changes will require your time to evaluate and make changes to your Firebase project and workflows. If you have any questions, please reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

#### Will the name of my default bucket change?

<br />

No. When you upgrade to the Blaze pricing plan, the name of your defaultCloud Storagebucket will***not***change.

- **If you provisioned your default bucket*before* October 30, 2024** , then your default bucket will always have a name format of<var translate="no">PROJECT_ID</var>`.appspot.com`.

  The only exception is if you[delete your`*.appspot.com`bucket](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#what-happens-if-delete-appspot-bucket)and provision a new default bucket.
- **If you provisioned your default bucket*on or after* October 30, 2024** , then your default bucket will always have a name format of<var translate="no">PROJECT_ID</var>`.firebasestorage.app`.

<br />

<br />

<br />

#### What happens if I delete my`*.appspot.com`default bucket?

<br />

A deleted bucket is restorable using the Cloud Storage[Buckets: restore](https://cloud.google.com/storage/docs/json_api/v1/buckets/restore)API until its hard delete time has elapsed.

**StartingOctober 30, 2024** : If you delete your<var translate="no">PROJECT_ID</var>`.appspot.com`default bucket, then you won't be able to provision a bucket with that same name format.

Instead, you can create a new defaultCloud Storagebucket (if your project is on the Blaze pricing plan) that has a name format of<var translate="no">PROJECT_ID</var>`.firebasestorage.app`. It will follow[Google Cloud Storagepricing and usage](https://cloud.google.com/storage/pricing), which provides an["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free)for buckets in`US-CENTRAL1`,`US-EAST1`, and`US-WEST1`.

<br />

<br />

<br />

#### Do I need to update my app's codebase?

<br />

No. To accommodate these changes, you do***not***need to update your app's codebase.

All existing<var translate="no">PROJECT_ID</var>`.appspot.com`default buckets will maintain their name format.

To avoid any service interruptions, make sure to upgrade your project to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)byas early as February 02, 2026. After upgrading to the Blaze pricing plan, your codebase will continue to interact with the<var translate="no">PROJECT_ID</var>`.appspot.com`default bucket as it always has.

<br />

<br />

<br />

#### Do I need to move my data out of my`*.appspot.com`default bucket?

<br />

No. To accommodate these changes, you do***not*** need to move your data out of your<var translate="no">PROJECT_ID</var>`.appspot.com`default bucket.

As long as you upgrade your project to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing)byas early as February 02, 2026, then you'll see no service interruptions.

<br />

<br />

## **Changes for programmatic interactions (like REST APIs and Terraform)**

If you provision or work with defaultCloud Storage for Firebasebuckets programmatically (for example, using REST APIs or Terraform), review the following changes to see if you need to change anything in your workflows or apps.
| **Important** : Here are the summarized key points of the FAQs in this section (but make sure to review each FAQ below for details):
|
| - On**October 30, 2024** , two REST APIs are shutting down: the[`projects.defaultLocation.finalize`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.defaultLocation/finalize)endpoint and the[`projects.availableLocations.list`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list)endpoint.
| - The changes to these REST APIs also affect how you might use Terraform withCloud Storage for Firebase(and possiblyCloud Firestore).

We understand that these changes will require your time to evaluate and make changes to your Firebase project and workflows. If you have any questions, please reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

#### What are the changes for using REST APIs?

<br />

**StartingOctober 30, 2024**, the following changes will happen:

- The[`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create)endpoint is changing:

  - To call this endpoint, your project must be on the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing).

  - The default buckets provisioned by this endpoint will have the name format of<var translate="no">PROJECT_ID</var>`.firebasestorage.app`(instead of the former<var translate="no">PROJECT_ID</var>`.appspot.com`).

  - These default buckets will followGoogle Cloud Storagepricing and usage, which provides an["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free)for buckets in`US-CENTRAL1`,`US-EAST1`, and`US-WEST1`.

- The[`projects.defaultLocation.finalize`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.defaultLocation/finalize)and[`projects.availableLocations.list`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.availableLocations/list)endpoints will be shutdown and will start returning`404: METHOD_NOT_FOUND`errors.

  Instead, to set a resource's location programmatically, you should use the resource-specific APIs. For example, set the locations of the defaultCloud Storagebucket and the defaultCloud Firestoreinstance during their individual provisioning when calling[`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create)and[`projects.databases.create`](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/create), respectively. For more details about replacements for REST APIs and locations, see the FAQ:[How do I set or get the location for a "defaultGoogle Cloudresource"?](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#set-get-location-for-default-gcp-resources)

<br />

<br />

<br />

#### What are the changes for using Terraform?

<br />

**StartingOctober 30, 2024** , the following changes will happen that are related to using Terraform withCloud Storage for Firebase.

You can no longer provision the defaultCloud Storage for Firebasebucket using Terraform. This is because you can no longer provision this bucket viaGoogleApp Engine. Instead, you can do one of the following:

- Provision the bucket by calling[`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create). This API is not yet available via Terraform.

- Provision the bucket through theFirebaseconsole. Visit the[***Storage***section](https://console.firebase.google.com/project/_/storage)of the console to get started.

Additionally, note the following about defaultCloud Storagebuckets provisioned startingOctober 30, 2024:

- Your project must be on the pay-as-you-go Blaze pricing plan to provision a defaultCloud Storagebucket.

- You no longer need to provision your defaultCloud Firestoreinstance before your defaultCloud Storagebucket.

- The location you select for your defaultCloud Firestoreinstance is not applicable to your defaultCloud Storagebucket (this means that your defaultCloud Firestoreinstance and your defaultCloud Storagebucket can be in different locations).

- The name format of the defaultCloud Storagebucket will be<var translate="no">PROJECT_ID</var>`.firebasestorage.app`(instead of the former<var translate="no">PROJECT_ID</var>`.appspot.com`).

<br />

<br />

## **Changes for "defaultGoogle Cloudresources"**

The["defaultGoogle Cloudresources"](https://firebase.google.com/docs/projects/locations#default-cloud-location)are any project resources associated withGoogleApp Engine, including the following:

- defaultCloud Firestoreinstance
- defaultCloud Storage for Firebasebucket (specifically those with the name format of<var translate="no">PROJECT_ID</var>`.appspot.com`)
- GoogleCloud Scheduler(specifically for 1st gen scheduled functions)

With many changes over the years to the Firebase ecosystem, the associations of Firebase-related resources toGoogleApp Enginehave been changing.

We understand that these changes will require your time to evaluate and make changes to your Firebase project and workflows. If you have any questions, please reach out to[Firebase Support](https://firebase.google.com/support/troubleshooter/storage/pricing-plan-changes).

<br />

#### What's happening to the "location for defaultGoogle Cloudresources"?

<br />

The["location for defaultGoogle Cloudresources"](https://firebase.google.com/docs/projects/locations#default-cloud-location)is the location setting for any project resources associated withGoogleApp Engine, including the following:

- defaultCloud Firestoreinstance
- defaultCloud Storage for Firebasebucket (specifically those with the name format of<var translate="no">PROJECT_ID</var>`.appspot.com`)
- GoogleCloud Scheduler(specifically for 1st gen scheduled functions)

When you set up any one of these resources in your project, you're transitively setting the location of theGoogleApp Engineapp in your project. This, in turn, sets the location for all the resources associated withGoogleApp Engine.
| **Important:** **StartingOctober 30, 2024** , provisioning the defaultCloud Storagebucket will not set the "location for defaultGoogle Cloudresources" (like the location for the project's defaultCloud Firestoreinstance). Also, provisioning the defaultCloud Firestoreinstance will no longer set the location for a new defaultCloud Storagebucket (those with the name format of<var translate="no">PROJECT_ID</var>`.firebasestorage.app`).

Note the following:

- **Any defaultCloud Storagebucket provisioned*before* October 30, 2024** (with a name format of<var translate="no">PROJECT_ID</var>`.appspot.com`) is associated withGoogleApp Engine. This means the following:

  - The bucket's location will set the location of resources associated withGoogleApp Engine(like the location of the defaultCloud Firestoreinstance).
- **Any defaultCloud Storagebucket provisioned startingOctober 30, 2024** (with the name format of<var translate="no">PROJECT_ID</var>`.firebasestorage.app`) is***not*** associated withGoogleApp Engine. This means the following:

  - Provisioning your defaultCloud Storagebucket will no longer set the location of resources associated withGoogleApp Engine(like the location of the defaultCloud Firestoreinstance).

  - Provisioning your defaultCloud Firestoreinstance will no longer set the location of your project's defaultCloud Storagebucket.

  - The locations available for your defaultCloud Storagebucket are now the same[locations available forGoogle Cloud Storage](https://cloud.google.com/storage/docs/locations#available-locations)(rather than limited to those forGoogleApp Engine).

<br />

<br />

<br />

#### How do I set or get the location for a "defaultGoogle Cloudresource"?

<br />

The["defaultGoogle Cloudresources"](https://firebase.google.com/docs/projects/locations#default-cloud-location)are any project resources associated withGoogleApp Engine, including the following:

- defaultCloud Firestoreinstance
- defaultCloud Storage for Firebasebucket (specifically those with the name format of<var translate="no">PROJECT_ID</var>`.appspot.com`)
- GoogleCloud Scheduler(specifically for 1st gen scheduled functions)

**StartingOctober 30, 2024** , the concept of "defaultGoogle Cloudresources" doesn't apply to*newly provisioned* defaultCloud Storagebuckets. Default buckets provisioned*after* this date have the name format of<var translate="no">PROJECT_ID</var>`.firebasestorage.app`, and they are***not*** associated withGoogleApp Engine. To learn more, review the FAQ:[What happens to the "location for defaultGoogle Cloudresources"?](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#location-for-default-gcp-resources)
| **Important:** Since defaultCloud Storagebuckets provisioned startingOctober 30, 2024aren't associated withGoogleApp Engine, their location will***not*** set the "location for defaultGoogle Cloudresources" (like the location for the defaultCloud Firestoreinstance). Also, provisioning the defaultCloud Firestoreinstance*first* in your project will no longer set the location for these new defaultCloud Storagebuckets.

If you want to set or get the location for any resource in a project, then you should interact directly with the resource instead.

##### DefaultCloud Storage for Firebasebucket

- **In theFirebaseconsole:**

  - Set and find the location of a defaultCloud Storagebucket in the[***Storage***section](https://console.firebase.google.com/u/0/project/_/storage)of theFirebaseconsole.
- **Using REST APIs:**

  - Set the location of a defaultCloud Storagebucket during its provisioning when calling[`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create).

    Note that startingOctober 30, 2024, calling this endpoint will require the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing). So before attempting to create a default bucket, make sure that the project is linked to aCloud Billingaccount (for example, using[`projects.updateBillingInfo`](https://cloud.google.com/billing/docs/reference/rest/v1/projects/updateBillingInfo)).
  - Get the location of a defaultCloud Storagebucket using[`projects.buckets.get`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/get).

##### DefaultCloud Firestoreinstance

Note that if you provisioned a defaultCloud Storagebucket beforeOctober 30, 2024, then the location of the project's defaultCloud Firestoreinstance has already been set (due to associations withGoogleApp Engine).

- **In theFirebaseconsole:**

  - Set and find the location of a defaultCloud Firestoreinstance in the[***Firestore***section](https://console.firebase.google.com/u/0/project/_/firestore)of theFirebaseconsole.
- **Using REST APIs:**

  - Set the location of a defaultCloud Firestoreinstance during its provisioning when calling[`projects.databases.create`](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/create).

  - Get the location of a defaultCloud Firestoreinstance using[`projects.databases.get`](https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/get).

##### Scheduled functions (1st gen)

Note that if you provisioned a defaultCloud Storagebucket beforeOctober 30, 2024, then the project's scheduled functions (1st gen) has already been set (due to associations withGoogleApp Engine).

- Set the location of a scheduled function during its[setup and deployment](https://firebase.google.com/docs/functions/schedule-functions?gen=2nd).

- Get the location of a scheduled function from the topic name of its job and function in the[Google Cloudconsole](https://console.cloud.google.com/project/_/cloudscheduler)(`firebase-schedule-`<var translate="no">FUNCTION_NAME</var>`-`<var translate="no">REGION</var>.

<br />

<br />