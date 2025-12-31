# Source: https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project.md.txt

A Firebase project is aGoogle Cloudproject that has some additional Firebase-specific configurations and services enabled. This is commonly called "adding Firebase" to aGoogle Cloudproject. This page describes[how to "add Firebase"](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#how-to-add-firebase), along with some[frequently asked questions (FAQs)](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faqs-and-troubleshooting).

When you add Firebase to aGoogle Cloudproject, Firebase automatically enables several APIs and creates service accounts to simplify the use of all Firebase services and interfaces. Firebase also adds a[`firebase:enabled`label](https://firebase.google.com/support/faq#project-label-firebase-enabled)to your project within the[*Labels*page](https://console.cloud.google.com/iam-admin/labels?project=_)of theGoogle Cloudconsole. Learn more details about[what happens when you "add Firebase"](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_what-happens-when-add-firebase).

## Relationship between a Firebase project and aGoogle Cloudproject

Since a Firebase project***is*** aGoogle Cloudproject:

- You can access and interact with the project in the[Firebaseconsole](https://console.firebase.google.com/)as well as in the[Google Cloudconsole](https://cloud.google.com/docs/overview/#google-cloud-console)and[Google APIs console](https://console.cloud.google.com/apis/).

- You can interact with the project using the[FirebaseCLI](https://firebase.google.com/docs/cli), the[gcloud CLI](https://cloud.google.com/sdk/gcloud), and any Terraform resource from Google.

- You can use products and APIs from both Firebase andGoogle Cloudin the project.

- [IAM permissions and roles](https://firebase.google.com/docs/projects/iam/overview)for the project are shared across Firebase andGoogle Cloud. Any access a project member (that is, a principal) has to yourGoogle Cloudproject will also apply to your Firebase project (and vice-versa).

- [Billing](https://firebase.google.com/pricing)for the project is shared across Firebase andGoogle Cloud. If billing is enabled on yourGoogle Cloudproject, then your Firebase project will be on Firebase's pay-as-you-go Blaze pricing plan.

- Unique identifiers for the project (like[project number](https://firebase.google.com/docs/projects/learn-more#project-number)and[project ID](https://firebase.google.com/docs/projects/learn-more#project-id)) are shared across Firebase andGoogle Cloud.

- Any[resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)applied to yourGoogle Cloudproject (for example, organization, folders, etc.) will also apply to your Firebase project.

- Deleting the project deletes it across Firebase andGoogle Cloud.

- Deleting or modifying a resource or data within the project applies across Firebase andGoogle Cloud.

## How to add Firebase to an existingGoogle Cloudproject

You can "add Firebase" to an existingGoogle Cloudproject using any of the following options. Make sure that you have the[required permissions to add Firebase](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_required-permissions-to-add-firebase)to theGoogle Cloudproject.

Be aware that once you "add Firebase" to an existingGoogle Cloudproject, it can't be undone (that is, you can't*fully* "remove Firebase" from theGoogle Cloudproject). Learn more in this[FAQ](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_remove-firebase-from-project).
| **Note:** In order to access and use all capabilities of Firebase in aGoogle Cloudproject, you need to accept the[Firebase Terms of Service](https://firebase.google.com/terms). Learn more about the requirement for Firebase Terms in this[FAQ](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_requirement-to-accept-firebase-terms).  
|
Later on this page, you can find other[FAQ and troubleshooting](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faqs-and-troubleshooting)for "adding Firebase" to yourGoogle Cloudproject.  

### Firebaseconsole

1. Sign into the[Firebaseconsole](https://console.firebase.google.com/)with the account that gives you access to the existingGoogle Cloudproject.

2. Click the button to create a new Firebase project.

3. At the bottom of the page, click**Add Firebase to Google Cloud project**.

4. In the text field, start entering the**project name**of the existing project, and then select the project from the displayed list.

5. Click**Open project**.

6. If prompted, accept the[Firebase Terms](https://firebase.google.com/terms).

7. Follow the on-screen instructions to "add Firebase" and set up a Firebase project.

   Note that enabling AI assistance in theFirebaseconsole andGoogle Analyticsare both optional.

### FirebaseCLI

1. If you haven't already,[install theFirebaseCLI](https://firebase.google.com/docs/cli#install_the_firebase_cli).

2. [Log in](https://firebase.google.com/docs/cli#sign-in-test-cli)with the same Google Account that gives you access to the existingGoogle Cloudproject.

3. Run the following command:

   ```text
   firebase projects:addfirebase
   ```
4. When prompted, select the existingGoogle Cloudproject from the displayed list.

| **Note:** If you get a`403 PERMISSION_DENIED`error when trying to "add Firebase" to an existingGoogle Cloudproject, it can mean that you don't have the[required permissions](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_required-permissions-to-add-firebase)or that you haven't[accepted the Firebase Terms of Service](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_requirement-to-accept-firebase-terms).

### REST API

1. Enable the[Firebase Management API](https://console.cloud.google.com/apis/library/firebase.googleapis.com)in the existingGoogle Cloudproject.

2. Generate your API access token.

3. Enable Firebase services for the project by calling[`projects.addFirebase`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/addFirebase).

   Note that you'll need the resource name of your project to make this call.

For detailed instructions, see[Add Firebase services to your project](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#add-firebase)in the Firebase guide: "Set up and manage a Firebase project using the Management REST API". Make sure to follow all the instructions in the[Before you begin](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project#before-you-begin)section of that guide.
| **Note:** If you get a`403 PERMISSION_DENIED`error when trying to "add Firebase" to an existingGoogle Cloudproject, it can mean that you don't have the[required permissions](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_required-permissions-to-add-firebase)or that you haven't[accepted the Firebase Terms of Service](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_requirement-to-accept-firebase-terms).

### Terraform

1. Enable the Firebase Management API (`firebase.googleapis.com`) in the existingGoogle Cloudproject.

2. Enable Firebase services for the project using the`google_firebase_project`resource.

For detailed information about using Firebase and Terraform, see[Get started with Terraform and Firebase](https://firebase.google.com/docs/projects/terraform/get-started).
| **Note:** If you get a`403 PERMISSION_DENIED`error when trying to "add Firebase" to an existingGoogle Cloudproject, it can mean that you don't have the[required permissions](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_required-permissions-to-add-firebase)or that you haven't[accepted the Firebase Terms of Service](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_requirement-to-accept-firebase-terms).

## FAQs and troubleshooting

<br />

#### Is accepting the Firebase Terms of Service required to start using Firebase?

<br />

In order to access and use all capabilities of Firebase in aGoogle Cloudproject, you need to accept the[Firebase Terms of Service](https://firebase.google.com/terms). You also need to accept the Firebase Terms in order to "add Firebase" to an existingGoogle Cloudproject.

**You only need to accept the Firebase Terms once for your Google Account** no matter how many projects you have access to. When you accept the terms, you're accepting them only for your Google Account; acceptance is*not*at the project-level for all project members.

You can accept the Firebase Terms through the[Firebaseconsole](https://console.firebase.google.com/)using any of the following options. When prompted, accept the Terms.

- Create a new Firebase project using theFirebaseconsole.

- Open an existing Firebase project in theFirebaseconsole (for example, someone has invited you to become a project member (that is, a principal) on the project).

- Open an existingGoogle Cloudin theFirebaseconsole and["add Firebase"](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#how-to-add-firebase_console)to it.

| **Note:** Accepting the Firebase Terms is*not* possible using theFirebaseCLI, REST API, or Terraform. It can only be done using theFirebaseconsole.
| **Important:** If you signed an offline variant of the Google Cloud Master Agreement for use of specified Firebase services under the same Google Cloud Platform Account, the[Firebase Terms](https://firebase.google.com/terms)do not apply to your use of such Firebase services, and your offline terms govern your use of such Firebase services.

<br />

<br />

<br />

#### Which permissions are required to "add Firebase"?

<br />

To "add Firebase" to an existingGoogle Cloudproject, a project member (that is, a principal) must have the following IAM permissions:

- `firebase.projects.update`
- `resourcemanager.projects.get`
- `serviceusage.services.enable`
- `serviceusage.services.get`

The IAM roles of Editor and Owner contain these permissions by default.

<br />

<br />

<br />

#### Why is theFirebaseconsole failing to load a list of my existingGoogle Cloudprojects?

<br />

This FAQ is most often applicable if you're trying to "add Firebase" to an existingGoogle Cloudproject using theFirebaseconsole*and you have access to many thousands ofGoogle Cloudprojects*.

TheFirebaseconsole isn't built to load many thousands ofGoogle Cloudprojects. Instead, we recommend[using theFirebaseCLI, REST API, or Terraform to "add Firebase" to your existingGoogle Cloudproject](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#how-to-add-firebase).

Also, you might want to review the FAQ["Why isn't my Firebase project showing up in my list of Firebase projects?"](https://firebase.google.com/support/faq#gcp-projects-not-loading-in-console)

<br />

<br />

<br />

#### Is adding the`firebase:enabled`label sufficient to add Firebase?

<br />

All Firebase projects have a[`firebase:enabled`label](https://firebase.google.com/support/faq#project-label-firebase-enabled)within the[*Labels*page](https://console.cloud.google.com/iam-admin/labels?project=_)of theGoogle Cloudconsole.

However, just manually adding the`firebase:enabled`label to your list of project labels does NOT enable Firebase-specific configurations and services for yourGoogle Cloudproject. To do that, you need to[add Firebase](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#how-to-add-firebase)using theFirebaseconsole (or, for advanced use cases, using theFirebaseCLI, Firebase Management REST API, or Terraform).

<br />

<br />

<br />

#### What happens when you "add Firebase" to an existingGoogle Cloudproject?

<br />

A Firebase project is aGoogle Cloudproject that has some additional Firebase-specific configurations and services enabled. So, when you "add Firebase" to an existingGoogle Cloudproject, Firebase takes the following actions to simplify the use of all Firebase services and interfaces:

- Adds the[`firebase:enabled`label](https://firebase.google.com/support/faq#project-label-firebase-enabled)within the[*Labels*page](https://console.cloud.google.com/iam-admin/labels?project=_)of theGoogle Cloudconsole.

- Creates a "Browser" API key and auto-restricts it to the[Firebase-related APIs](https://firebase.google.com/docs/projects/api-keys#faq-required-apis-for-restricted-firebase-api-key).

- Creates the following service accounts:

  - `service-`<var translate="no">PROJECT_NUMBER</var>`@gcp-sa-firebase.iam.gserviceaccount.com`
  - `firebase-adminsdk-`<var translate="no">random5chars</var>`@`<var translate="no">PROJECT_ID</var>`.iam.gserviceaccount.com`
- Enables the following APIs:

  - App Engine Admin API
  - Cloud Pub/Sub API
  - Cloud Resource Manager API
  - Cloud Runtime Configuration API
  - Cloud Testing API
  - Firebase Cloud Messaging API
  - Firebase Dynamic Links API
  - Firebase Hosting API
  - Firebase Installations API
  - Firebase Management API
  - Firebase Remote Config API
  - Firebase Remote Config Realtime API
  - Firebase Rules API
  - Identity Toolkit API
  - Token Service API

<br />

<br />

<br />

#### Can I "remove Firebase" from a project?

<br />

After you "add Firebase" to an existingGoogle Cloudproject, it can't be undone (that is, you can't*fully* "remove Firebase" from theGoogle Cloudproject).

The process of "adding Firebase" enables APIs and backend services that may be used for otherGoogle Cloudfeatures. Disabling all these enabled services could cause unexpected and unintended consequences due to dependencies.

However, if you choose, it is possible for you to manually disable all the APIs and delete the label, API key, and service accounts[automatically enabled and created when you "added Firebase"](https://firebase.google.com/docs/projects/use-firebase-with-existing-cloud-project#faq_what-happens-when-add-firebase).
| **Warning:** If you choose to manually disable and delete what happened during "add Firebase", do so with extreme caution. You need to be absolutely sure that yourGoogle Cloudproject and apps associated with the project are not using*anything*related to what you're disabling and deleting; otherwise your project or app could stop working or behave in unexpected ways.

<br />

<br />

<br />

#### Can I block "adding Firebase" for an existingGoogle Cloudproject?

<br />

While you can't actually block the possibility of "adding Firebase" to an existingGoogle Cloudproject, you can do the following:

Limit the project members (that is, principals) that have the IAM permission`firebase.projects.update`, which is required to "add Firebase".

<br />

<br />

## Next steps

- Check out the following resources for learning more about Firebase projects:

  - [Understand Firebase projects](https://firebase.google.com/docs/projects/learn-more)--- provides brief overviews of several important concepts about Firebase projects, including their relationship withGoogle Cloudand the basic hierarchy of a project and its apps and resources.

  - [General best practices for setting up Firebase projects](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices)--- provides general, high-level best practices for setting up Firebase projects and registering your apps with a project so that you have a clear development workflow that uses distinct environments.

- Get started using Firebase in your mobile and web apps by registering your apps with your Firebase project and connecting them to Firebase:[iOS+](https://firebase.google.com/docs/ios/setup)\|[Android](https://firebase.google.com/docs/android/setup)\|[Web](https://firebase.google.com/docs/web/setup)\|[Flutter](https://firebase.google.com/docs/flutter/setup)\|[Unity](https://firebase.google.com/docs/unity/setup)\|[C++](https://firebase.google.com/docs/cpp/setup).