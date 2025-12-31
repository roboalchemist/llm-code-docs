# Source: https://firebase.google.com/docs/studio/set-up-gemini.md.txt

# Source: https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini.md.txt

# Set up Gemini in Firebase

| **Important:** This section describes setting up Gemini in Firebase within the Firebase console. To learn about setting up Gemini in Firebase within Firebase Studio, see [AI assistance within Firebase Studio](https://firebase.google.com/docs/studio/ai-assistance).

Before you start using Gemini in Firebase, you must enable it in the
Firebase console. Gemini in Firebase is enabled on a per-user,
per-project basis and enablement depends on your user type and plan.

- If you are a Google Workspace (formerly G Suite) user,
  Gemini in Firebase is included with
  [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist).
  Gemini Code Assist subscriptions can be purchased
  and enabled by your administrator directly from the Firebase console.
  Learn more at [Set up
  Gemini Code Assist](https://cloud.google.com/gemini/docs/discover/set-up-gemini).

- If you are an individual user, Gemini in Firebase is available at no-cost
  or with a
  [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist)
  subscription, which provides contextual awareness and messaging campaign
  insights.

Note that the terms of service are different for Gemini in Firebase
(no-cost) and Gemini in Firebase with a Gemini Code Assist
subscription. Learn more at [How Gemini in Firebase uses your
data](https://firebase.google.com/docs/gemini-in-firebase#how-gemini-in-firebase-uses-your-data).

## Required permissions

To enable and use features of Gemini in Firebase requires certain IAM roles
and permissions.

- Project members with the [owner or editor IAM role](https://firebase.google.com/docs/projects/iam/roles-basic) can enable Gemini in Firebase and use its features.
- Project viewers cannot enable Gemini in Firebase, but they can use its features, including [Gemini in Firebase chat](https://firebase.google.com/docs/gemini-in-firebase/try-gemini), help, and [AI assistance in Crashlytics](https://firebase.google.com/docs/crashlytics/ai-assistance) *if they are assigned the Gemini for Google Cloud User role*.
- **If the project is part of Google Workspace (formerly G Suite)**, a Google Workspace administrator must enable it.

Here's how to assign the Gemini for Google Cloud User role to a project
member. Note that only project owners can edit IAM roles.

1. From the Firebase console, select settings [**Project settings**](https://console.firebase.google.com/project/_/settings/general/), then select **Users and permissions**.
2. Find the row for the applicable project member.
3. Click more_vert **More options** , then select **Edit access.**
4. Expand **Role(s)** , select **Gemini for Google Cloud User** , then click **Done**.
5. Click **Update roles** to save the change. It may take a minute or two for the new role to apply to your user.

| **Note:** If using Gemini in Firebase with a Gemini Code Assist subscription, a license must be assigned to each user. Learn more at [Assign Gemini Code Assist
| licenses](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini#assign-code-assist-licenses).

## Set up Gemini in Firebase

After ensuring that your account has [required
permissions](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini#required-permissions), you can enable Gemini in Firebase for
your project.

Perform the following to enable Gemini in Firebase usage for your project.
| **Important:** This procedure is a prerequisite for all editions of Gemini in Firebase, including Gemini in Firebase (no-cost) and [Gemini in Firebase with a Gemini Code Assist
| subscription](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini#code-assist).

1. As a project owner or editor, open the
   [Firebase console](https://console.firebase.google.com/), select a project,
   and click â¦**Gemini in Firebase**
   located in the upper-right console menu.

   The Gemini pane appears.
2. Review the information that appears and click **Get started**.

3. Optionally, enable Gemini in Firebase for other users in your
   project: From
   settings**Project settings** ,
   select **Users and permissions** and assign additional users the
   [Gemini for Google Cloud role](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini#required-permissions).

   | **Tip:** You can also assign the Gemini for Google Cloud role to users using IAM in the Google Cloud console or the gcloud CLI.

You are now ready to accelerate your Firebase development with
Gemini in Firebase. Learn more about interacting with Gemini in Firebase
at [Try Gemini in the
Firebase console](https://firebase.google.com/docs/gemini-in-firebase/try-gemini).

If you plan to use Gemini in Firebase with a Gemini Code Assist
subscription, proceed to [Gemini in Firebase with a
Gemini Code Assist subscription](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini#code-assist) for setup instructions.

## Gemini in Firebase with a Gemini Code Assist subscription

When you purchase a subscription to Gemini Code Assist, you unlock
Gemini in Firebase. To enable Gemini Code Assist, you must
purchase a subscription and assign licenses to individual users.

You can enable Gemini Code Assist through the Firebase console
or the Google Cloud console using
[Gemini Admin](https://cloud.google.com/gemini/docs/admin).
| **Important:** If you plan to enable Gemini Code Assist for a project that uses the no-cost Spark pricing plan, we recommend using the Firebase console to purchase and manage your Gemini Code Assist subscription. Managing your subscription through the Firebase console ensures that your project on the Spark plan does not get upgraded to the pay-as-you-go Blaze pricing plan.  
|
| While Gemini Code Assist licenses are assigned on a per-user basis (regardless of project membership), the Google Cloud console requires that you link the Cloud Billing account you use for purchasing the subscription with your Firebase project. *This action automatically upgrades your project to
| the pay-as-you-go Blaze plan.* Learn more about the Spark and Blaze plans at [Firebase pricing plans](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans).

The following sections describe how to purchase Gemini Code Assist and
assign licenses to users.

### Purchase Gemini Code Assist and assign licenses

Before purchasing, you must have a Google Cloud Billing account and must be a
billing administrator on that account. If you don't have a Cloud Billing
account, follow the instructions in [Create a new self-serve Cloud Billing
account](https://cloud.google.com/billing/docs/how-to/create-billing-account).

To purchase Gemini Code Assist subscription and assign licenses:

1. Click â¦**Gemini in Firebase** to open the Gemini pane.
2. Depending on your user type:
   - From the informational note that appears, click **purchase a
     subscription**.
   - From the **Want to do more with Gemini?** banner, click **Try
     Gemini Code Assist**.
3. Select the Gemini Code Assist subscription type you'd like to purchase, then click **Get started** . Learn more about the differences between Standard and Enterprise editions at [Compare
   Gemini Code Assist
   editions](https://cloud.google.com/products/gemini/code-assist#compare-gemini-code-assist-editions).
4. Click **Continue**.
5. Select the Cloud Billing account you want to use to purchase the subscription.
6. Select the Gemini Code Assist subscription type you want to purchase, then click **Continue**.
7. In **Configure subscription** , complete the fields to configure the subscription, including the following:
   - **Subscription display name**.
   - **Number of licenses** . Licenses are assigned on a per-user basis, so make sure to purchase enough for all of the users who should have access to Gemini Code Assist and Gemini in Firebase features. Note that if you are purchasing Enterprise edition, then you must purchase at least 10 licenses.
   - **Subscription period** (monthly or yearly). With an annual subscription, you are given a discounted rate that is charged on a monthly basis rather than a one-time payment. To learn more about pricing plans for Gemini Code Assist, see [Gemini Code Assist
     pricing](https://cloud.google.com/products/gemini/code-assist#pricing).
   - **Automatic subscription renewal** after the commitment term (monthly or yearly) ends. Auto-renew keeps your subscription and licenses active. If the subscription doesn't auto-renew, it ends when the current term ends, and you must follow the purchase process again and re-assign licenses.
8. To confirm the subscription, click **Continue**.
9. Review the subscription details and, if you agree to the terms, select **I agree to the terms of this purchase** , and then select **Complete
   purchase**.
10. Next, you must assign licenses to each user. Click **Next: Manage Gemini
    License Assignments** and proceed to **Assign licenses**.
11. Click **Add licensed users**. A user selection dialog appears. To search for specific users, enter their name in the search box.
12. Select one or more users from the list, and then click **Next**.
13. Click **Assign Licenses**.

    | **Tip:** Optionally, you can enable automatic license assignment instead of assigning licenses to individual users. This enables licenses to be automatically assigned to users with permission to self-assign licenses for this billing account. You can also set an expiration date to unassign licenses for inactive users. Learn more at [Automatically assign Gemini Code Assist
    | licenses](https://cloud.google.com/gemini/docs/manage-licenses#automatic).
14. After you've finished assigning licenses, return to the Firebase console
    and click **Done**.

### Manage your Gemini Code Assist subscription

If you've already completed the Gemini Code Assist subscription
purchase flow, you can manage your Gemini Code Assist subscription
and assign licenses from the Firebase console.
| **Note:** You can enable Gemini Code Assist through the Firebase console or the Google Cloud console using [Gemini
| Admin](https://cloud.google.com/gemini/docs/admin). If you plan to enable Gemini Code Assist for a project that uses the no-cost Spark plan, we recommend using the Firebase console to purchase and manage your Gemini Code Assist subscription. While Gemini Code Assist licenses are assigned on a per-user basis, regardless of project, the Google Cloud console requires that you associate the Cloud Billing account you use for purchase with a project. This automatically upgrades that project to the pay-as-you-go Blaze plan. Managing your subscription through the Firebase console ensures that your project on the Spark plan does not get upgraded to Blaze. Learn more about the Spark and Blaze plans at [Firebase pricing
| plans](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans).

To manage your subscription and assign Gemini Code Assist licenses:

1. From the Firebase console, select settings**Project settings** \> **Usage
   and Billing** \> **Subscriptions**.
2. From **Manage your subscriptions**, click the subscription link.
3. From the window that appears, click **Manage licenses** . Gemini Code Assist licensing management and subscription settings open in the Google Cloud console.
4. To add licensed users:

   1. Click **Add licensed users**. A user selection dialog appears. To search for specific users, enter their name in the search box.
   2. Select one or more users from the list, and then click **Next**.
   3. Click **Assign Licenses**.

   | **Tip:** Optionally, you can enable automatic license assignment instead of assigning licenses to individual users. This enables licenses to be automatically assigned to users with permission to self-assign licenses for this billing account. You can also set an expiration date to unassign licenses for inactive users. Learn more at [Automatically
   | assign Gemini Code Assist
   | licenses](https://cloud.google.com/gemini/docs/manage-licenses#automatic).
5. To unassign licenses:

   1. Select the user or users you want to unassign, then click **Unassign
      licenses**.
6. To make changes to your subscription, the **Subscription settings** tab, then
   click **Modify subscription**.

7. Select the Gemini Code Assist subscription, then click **Continue**.

8. Next, you can update any of the following subscription settings:

   - **Subscription display name**.
   - **Number of licenses** . Licenses are assigned on a per-user basis, so make sure to purchase enough for all of the users who should have access to Gemini Code Assist and Gemini in Firebase features. Note that if you are purchasing Enterprise edition, then you must purchase at least 10 licenses.
   - **Subscription period** (monthly or yearly). With an annual subscription, you are given a discounted rate that is charged on a monthly basis rather than a one-time payment. To learn more about pricing plans for Gemini Code Assist, see [Gemini Code Assist
     pricing](https://cloud.google.com/products/gemini/code-assist#pricing).
   - **Automatic subscription renewal** after the commitment term (monthly or yearly) ends. Auto-renew keeps your subscription and licenses active. If the subscription doesn't auto-renew, it ends when the current term ends, and you must follow the purchase process again and re-assign licenses.
9. Click **Continue**.

10. If you agree to the terms, click **I agree to the terms of this purchase**
    and click **Save changes**.

## Turn off Gemini in Firebase

To turn off all Gemini for Google Cloud products including
Gemini in Firebase and features that it supports, like
[AI assistance in Crashlytics](https://firebase.google.com/docs/crashlytics/ai-assistance), see
[Turn off the Gemini for Google Cloud API](https://cloud.google.com/gemini/docs/turn-off-gemini#companion-api).
Otherwise, you can limit access for specific users.
| **Note:** If you turn off the Gemini for Google Cloud API, then you disable all Gemini for Google Cloud features.

To limit access for specific users, you can remove the
Gemini for Google Cloud user role from each user:

- From the Firebase console, open settings**Project settings** , select **Users and permissions** and, for each user you want to update, remove the [Gemini for Google Cloud role](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini#required-permissions).

To turn off Gemini Code Assist, follow the instructions in [Turn off
Gemini Code Assist](https://cloud.google.com/gemini/docs/turn-off-gemini#code-assist).

## Troubleshoot Gemini in Firebase

If â¦**Gemini in Firebase** doesn't
appear in the Firebase console, perform the following steps:

- Verify that the **Gemini for Google Cloud API** is enabled in the [Google Cloud console](https://console.cloud.google.com/apis/api/cloudaicompanion.googleapis.com?project=_).
- Ensure that users to whom you want to give access have been assigned the **Cloud AI companion user** role in [IAM](https://console.cloud.google.com/iam-admin/iam?project=_).
- If you're using Gemini Code Assist, make sure that affected users have been [assigned a license](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini#assign-code-assist-licenses).

If you see the message, "You don't currently have a Gemini Code Assist
license," this indicates that you're a Google Workspace user and must have a
Gemini Code Assist subscription to use Gemini in Firebase. Learn
more at
[Gemini in Firebase with a Gemini Code Assist
subscription](https://firebase.google.com/docs/gemini-in-firebase/set-up-gemini#code-assist).

## Next steps

- [Try Gemini in the Firebase console](https://firebase.google.com/docs/gemini-in-firebase/try-gemini).
- Learn more about [prompt
  optimization](https://cloud.google.com/gemini/docs/discover/write-prompts).