# Source: https://firebase.google.com/docs/crashlytics/ai-assistance-in-dashboard.md.txt

In the Crashlytics dashboard, you can get AI-generated insights about your
issues to help speed up the time it takes for you to understand why an issue
happened and how you can address it. AI assistance in Crashlytics identifies
root causes, delivers actionable insights and tailored solutions, and recommends
best practices going forward.

> [!NOTE]
> **Note:** The AI assistance available through the Firebase console doesn't have access to and thus can't fix issues in your codebase. You'll need to make any changes to your codebase yourself or [use an AI agent to help fix it](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp).

## Available insights

AI assistance in Crashlytics can provide you with the following insights:

- **Summary/Cause**: A concise but information-rich explanation of what happened to the user and what caused the issue.
- **Debugging options:** Gemini will offer a few potential ways to either reproduce the error or will provide next steps to further debug the issue to identify a root cause. Gemini can provide recommended commands to try or code to use ([with caution](https://support.google.com/legal/answer/13505487)).
- **Actionable next steps:** While Gemini won't initially have all of the context about your issue, AI assistance in Crashlytics will use Firebase's wealth of knowledge on mobile app development to recommend a few potential resolution paths whenever possible.
- **Best Practices:** Part of the triage process is, ideally, future-proofing your app so these types of issues don't recur. Gemini references thousands of pages of Firebase documentation (and more) to provide you with possible approaches to resolve the issue.

> [!NOTE]
> **Note:** AI insights in the Crashlytics dashboard are available for crashes and ANRs. They're not yet available for non-fatal events.

## Before you begin

Make sure that you have the required permissions and you've enabled
Gemini in Firebase.

### Required permissions

To enable and use features of Gemini in Firebase requires certain IAM roles
and permissions.

- Project members with the [owner or editor IAM role](https://firebase.google.com/docs/projects/iam/roles-basic) can enable Gemini in Firebase and use its features.
- Project viewers cannot enable Gemini in Firebase, but they can use its features, including [Gemini in Firebase chat](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/try-gemini), help, and [AI assistance in Crashlytics](https://firebase.google.com/docs/crashlytics/ai-assistance-in-dashboard) *if they are assigned the Gemini for Google Cloud User role*.
- **If the project is part of Google Workspace (formerly G Suite)**, a Google Workspace administrator must enable it.

Here's how to assign the Gemini for Google Cloud User role to a project
member. Note that only project owners can edit IAM roles.

1. From the Firebase console, select [**Project settings**](https://console.firebase.google.com/project/_/settings/general/), then select **Users and permissions**.
2. Find the row for the applicable project member.
3. Click **More options** , then select **Edit access.**
4. Expand **Role(s)** , select **Gemini for Google Cloud User** , then click **Done**.
5. Click **Update roles** to save the change. It may take a minute or two for the new role to apply to your user.

> [!NOTE]
> **Note:** If using Gemini in Firebase with a Gemini Code Assist subscription, a license must be assigned to each user. Learn more at [Assign Gemini Code Assist licenses](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini#assign-code-assist-licenses).

### Enable Gemini in Firebase

AI insights in the Crashlytics dashboard are available as part of
Gemini in Firebase.

Make sure that Gemini in Firebase is enabled in your Firebase project, as
described in
[Set up Gemini in Firebase](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini).

## Generate insights

To use AI assistance in Crashlytics to generate insights about your crashes:

1. In the Firebase console, open the
   [Crashlytics dashboard](https://console.firebase.google.com/project/_/crashlytics)
   and select your app.

2. Locate and select a crash you want to investigate. The Crashlytics event
   page appears, including insights with one or more of the following:

   - an analysis of the crash with a possible cause
   - debugging instructions
   - actionable next steps
   - best practices

   If you don't see the AI assistance in Crashlytics feature at the top of the
   event page, verify that Gemini in Firebase has been enabled (for setup
   instructions, see
   [Set up Gemini in Firebase](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini)).
   Also, make sure that you're viewing a crash or ANR event. Non-fatal events
   are not yet supported.
3. If you'd like to use AI assistance to fix the issue directly in your app's
   codebase, consider using
   [AI assistance for Crashlytics via MCP](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp).

> [!IMPORTANT]
> **Important:** AI assistance in Crashlytics is an early-stage technology that can generate output that seems plausible but is factually incorrect. It may respond with inaccurate information that doesn't represent Google's views. Validate all output from Gemini before you use it and do not use untested generated code in production. Do not log personally-identifiable information (PII) through Crashlytics APIs. For more information, see [How AI assistance in Crashlytics uses your data](https://firebase.google.com/docs/crashlytics/ai-assistance-in-dashboard#governance) and [Gemini in Google Cloud and responsible AI](https://cloud.google.com/duet-ai/docs/discover/responsible-ai).

## Troubleshoot AI assistance in Crashlytics

Refer to
[Troubleshoot Gemini in Firebase](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini#troubleshoot-gemini-in-firebase).

## How AI assistance in Crashlytics uses your data

Refer to
[How Gemini in Firebase uses your data](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase#how-gemini-in-firebase-uses-your-data).

## Quotas and pricing

This section describes the quotas and pricing structure for
AI assistance in Crashlytics.

### Quotas and limits

AI assistance in Crashlytics quotas are included as part of the
Gemini for Google Cloud API quotas that Gemini in Firebase uses.

You can view your current quotas on the
[Quotas page for the Gemini for Google Cloud API](https://console.cloud.google.com/apis/api/cloudaicompanion.googleapis.com/quotas?project=_).

1. From the [Google Cloud console](https://console.cloud.google.com), select **Enabled APIs \& services**.
2. Search for, then click **Gemini for Google Cloud API**.
3. Click **Quotas \& system limits**.

Gemini for Google Cloud API quotas appear. AI assistance in Crashlytics uses the
"Chat API requests per day per user" quota.

To request a quota increase:

1. Select the quota you want to increase, and click **Edit request**.
2. Update the **New value** text field with the quota you'd like to request, then click **Submit** . The Google Cloud team will evaluate your request and respond by email.

### Pricing

AI assistance in Crashlytics is available as part of Gemini in Firebase,
which is included for individual users at no-cost or with a
Gemini Code Assist subscription.

See
[Gemini in Firebase pricing](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase#pricing)
for more information.