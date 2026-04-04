# Source: https://firebase.google.com/docs/storage/security/get-started.md.txt

# Get started with Firebase Security Rules

<br />

<br />

Firebase Security Rules provide robust, completely customizable protection for your data in
Cloud Firestore, Realtime Database, and Cloud Storage. You can easily get
started with Security Rules following the steps in this guide, securing your
data and protecting your app from malicious users.

## Understand the Firebase Security Rules language

Before you start writing rules, it's worthwhile to take some time to review
the specific Firebase Security Rules language for the Firebase products you're using.
Cloud Storage leverages a superset
of the Common Expression Language (CEL) that relies on `match` and `allow`
statements that set a condition for access at a defined path..

Start by learning the [core syntax of the Firebase Security Rules language](https://firebase.google.com/docs/storage/security/core-syntax).

## Set up Authentication

If you haven't done it already, add [Firebase Authentication to your app](https://firebase.google.com/docs/auth).
Firebase Authentication supports many common authentication methods and integrates with
Firebase Security Rules to provide comprehensive verification capabilities.

You can set up additional, custom authentication information for your app.

Learn more about [Firebase Security Rules and Firebase Authentication](https://firebase.google.com/docs/rules/rules-and-auth).

## Define your data and rules structures

The way you structure your data might affect the way you structure and
implement your rules. As you define your data structures, consider the
implications they might have on your Security Rules structure.

For example, in Cloud Storage, you might want to include
a field that denotes a specific role for each user. Then, your rules can read
that field and use it to grant role-based access. You can also create
a Cloud Firestore database, store access criteria in Cloud Firestore
documents, then access those documents from Cloud Storage Security Rules.

As you define your data and rules architectures, keep in mind the way that
rules cascade or don't cascade, depending on your product. With Realtime Database,
rules work from top-down, with shallower rules overriding deeper rules. If a
rule grants read or write permissions at a particular path, then it also grants
access to all child nodes under it. In contrast, with Cloud Firestore and
Cloud Storage, rules apply only at specified levels of the data hierarchy,
and you write explicit rules to control access to different levels.

## Access your rules

To view your existing Security Rules, use either the Firebase CLI or the
Firebase console. Make sure you edit your rules using the same method,
consistently, to avoid mistakenly overwriting updates. If you're not sure
whether your locally defined rules reflect the most recent updates, the Firebase
console always shows the most recently deployed version of your Firebase Security Rules.

To access your rules from the [Firebase console](https://console.firebase.google.com/), select your
project, then in the left-hand navigation panel, click
**Storage** . Click **Security Rules** once you're
in the correct database or storage bucket.

To access your rules from the Firebase CLI, go to the
rules file noted in your [firebase.json file](https://firebase.google.com/docs/cli#the_firebasejson_file).

## Write basic rules

> [!NOTE]
> **Note:** Many AI assistants, such as [Gemini CLI](https://cloud.google.com/gemini/docs/codeassist/gemini-cli), can help generate Firebase Security Rules for Cloud Firestore and Cloud Storage for Firebase. For a detailed, pre-written prompt you can use with your AI assistant, refer to [AI Prompt: Write Firebase Security Rules](https://firebase.google.com/docs/ai-assistance/prompt-catalog/write-security-rules).

As you're developing your app and understanding Security Rules, try
implementing Security Rules to address a few [basic use cases](https://firebase.google.com/docs/rules/basics),
including the following:

- **Content-owner only:** Restrict access to content by user.
- **Mixed access:** Restrict write access by user, but allow public read access.
- **Attribute-based access:** Restrict access to a group or type of user.

## Test your rules

If you're setting up your Firebase Security Rules in the Firebase console, you can use
the [Firebase Rules Playground](https://firebase.google.com/docs/rules/simulator) to quickly validate
behavior. However, we recommend more thorough testing with the
[Local Emulator Suite](https://firebase.google.com/docs/rules/emulator-setup) before you deploy your
changes to production.

## Deploy rules

Use the Firebase console or the Firebase CLI to deploy your rules
to production. Follow the steps outlined in
[Manage and deploy Firebase Security Rules](https://firebase.google.com/docs/rules/manage-deploy).