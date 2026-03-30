# Source: https://firebase.google.com/docs/projects/terraform/get-started.md.txt

# Get started with Terraform and Firebase

Firebase is beginning to support
[Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs).
If you're on a team that wants to automate and standardize creating Firebase
projects with specific resources provisioned and services enabled, then using
Terraform with Firebase can be a good fit for you.

The basic workflow for using Terraform with Firebase includes the following:

- Creating and customizing a Terraform configuration file (a `.tf` file) which
  specifies the infrastructure you want to provision (that is, resources you
  want to provision and the services you want to enable).

- Using gcloud CLI commands that interface with Terraform to
  provision the infrastructure specified in the `.tf` file.

> [!NOTE]
> This is a beta release of Firebase support for Terraform. This set of features and tools might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## What can you do with Terraform and Firebase?

The [example generalized workflow in this guide](https://firebase.google.com/docs/projects/terraform/get-started#general-workflow-terraform-and-firebase)
is creating a new Firebase project with an Android app. But you can do a lot
more with Terraform, such as:

- Delete and modify existing infrastructure using Terraform.

- Manage product-specific configuration and tasks using Terraform, like:

  - Enabling Firebase Authentication sign-in providers.
  - Creating Cloud Storage buckets or database instances and deploying Firebase Security Rules for them.
  - Creating Firebase App Hosting backends, builds, and other related resources.

You can use standard Terraform config files and commands to accomplish all these
tasks. And to help you with this, we've provided
[sample Terraform config files](https://firebase.google.com/docs/projects/terraform/get-started#sample-config-files) for several common use
cases.

> [!NOTE]
> This guide and the currently available Firebase resources with Terraform support are the first releases for Firebase's support of Terraform. If you have feedback or encounter an issue, we'd like to hear from you! Please file an [issue in the GitHub repo](https://github.com/hashicorp/terraform-provider-google/issues?q=is:issue+is:open+firebase) (make sure to include the applicable `resource` type).

<br />

*** ** * ** ***

## Generalized workflow for using Terraform with Firebase

### **Prerequisites**

This guide is an introduction to using Terraform with Firebase, so it assumes
basic proficiency with Terraform. Make sure that you've completed the following
prerequisites before starting this workflow.

- [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/gcp-get-started)
  and familiarize yourself with Terraform using their official tutorials.

- [Install the Google Cloud CLI](https://cloud.google.com/sdk/docs/install-sdk)
  (gcloud CLI). Login using a
  [user account](https://cloud.google.com/sdk/gcloud/reference/auth/application-default)
  or a
  [service account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account).

  <br />

  View requirements for user accounts and service accounts

  <br />

  > - If using a user account, you must have accepted the Firebase Terms of Service (Firebase ToS). You have accepted the Firebase ToS if you can view a Firebase project in the [Firebase console](https://console.firebase.google.com/)
  > - For Terraform to take certain actions (for example, create projects), the following must be true:
  >   - The user or service account must have the applicable IAM access for those actions.
  >   - If the user or service account is part of a Google Cloud organization, then the org policies must allow the account to take those actions.

  <br />

  <br />

*** ** * ** ***

### **Step 1:** Create and customize a Terraform config file

A Terraform config file needs two main sections (which are described in detail
below):

- [A`provider` setup section which dictates which Terraform resources can be
  accessed](https://firebase.google.com/docs/projects/terraform/get-started#general-workflow-set-up-provider)
- [A section of individual `resource` blocks that specify what infrastructure to
  create](https://firebase.google.com/docs/projects/terraform/get-started#general-workflow-specify-infrastructure-to-create)

#### **Set up your `provider`**

A `provider` setup is required no matter which Firebase products or services are
involved.

1. Create a Terraform config file (like `main.tf` file) in your local
   directory.

   In this guide, you'll use this config file to specify both the `provider`
   setup and all the infrastructure that you want Terraform to create. Note,
   though, that you have options for how to include the provider setup.

   <br />

   View options for how
   to include the `provider` setup

   <br />

   > You have the following options for how to include a `provider` setup to
   > the rest of your Terraform configuration:
   > - **Option 1:** Include it at the top of a single Terraform `.tf` config
   >   file (as shown in this guide).
   >
   >   - Use this option if you're just getting started with Terraform or just trying out Terraform with Firebase.
   > - **Option 2:** Include it in a separate `.tf` file (like a `provider.tf`
   >   file), apart from the `.tf` file where you specify infrastructure to
   >   create (like a `main.tf` file).
   >
   >   - Use this option if you're part of a larger team that needs to standardize setup.
   >   - When running Terraform commands, both the `provider.tf` file and the `main.tf` file must be in the same directory.

   <br />

   <br />

2. Include the following `provider` setup at the top of the `main.tf` file.

   You must use the `google-beta` provider because this is a beta release of
   using Firebase with Terraform. Exercise caution when using in production.

   ```terraform
   # Terraform configuration to set up providers by version.
   terraform {
     required_providers {
       google-beta = {
         source  = "hashicorp/google-beta"
         version = "~> 6.0"
       }
     }
   }

   # Configures the provider to use the resource block's specified project for quota checks.
   provider "google-beta" {
     user_project_override = true
   }

   # Configures the provider to not use the resource block's specified project for quota checks.
   # This provider should only be used during project creation and initializing services.
   provider "google-beta" {
     alias = "no_user_project_override"
     user_project_override = false
   }
   ```

   Learn more about the
   [different types of project-related attributes](https://firebase.google.com/docs/projects/terraform/get-started#faq-understand-project-related-attributes)
   (including what this guide calls the "quota-check project") when using
   Terraform with Firebase.
3. Continue to the next section to complete your config file and specify what
   infrastructure to create.

#### **Specify what infrastructure to create using `resource` blocks**

In your Terraform config file (for this guide, your `main.tf` file), you need to
specify all the infrastructure you want Terraform to create (meaning all the
resources you want to provision and all the services you want to enable). In
this guide, find a full list of all
[Firebase resources that support Terraform](https://firebase.google.com/docs/projects/terraform/get-started#supported-resources).

> [!NOTE]
> **Note:** Check out our [sample Terraform config files](https://firebase.google.com/docs/projects/terraform/get-started#sample-config-files) for several common use cases.

1. Open your `main.tf` file.

2. Under the `provider` setup, include the following config of `resource`
   blocks.

   This basic example creates a new Firebase project and then creates a
   Firebase Android App within that project.

   > [!IMPORTANT]
   > **Important:** Whenever you create a Firebase App, you also need to configure your app's codebase to use Firebase, which includes adding your app's Firebase config and the Firebase SDKs for the products you want to use.

   ```terraform
   # Terraform configuration to set up providers by version.
   ...

   # Configures the provider to use the resource block's specified project for quota checks.
   ...

   # Configures the provider to not use the resource block's specified project for quota checks.
   ...

   # Creates a new Google Cloud project.
   resource "google_project" "default" {
     provider   = google-beta.no_user_project_override

     name       = "Project Display Name"
     project_id = "project-id-for-new-project"
     # Required for any service that requires the Blaze pricing plan
     # (like Firebase Authentication with GCIP)
     billing_account = "000000-000000-000000"

     # Required for the project to display in any list of Firebase projects.
     labels = {
       "firebase" = "enabled"
     }
   }

   # Enables required APIs.
   resource "google_project_service" "default" {
     provider = google-beta.no_user_project_override
     project  = google_project.default.project_id
     for_each = toset([
       "cloudbilling.googleapis.com",
       "cloudresourcemanager.googleapis.com",
       "firebase.googleapis.com",
       # Enabling the ServiceUsage API allows the new project to be quota checked from now on.
       "serviceusage.googleapis.com",
     ])
     service = each.key

     # Don't disable the service if the resource block is removed by accident.
     disable_on_destroy = false
   }

   # Enables Firebase services for the new project created above.
   resource "google_firebase_project" "default" {
     provider = google-beta
     project  = google_project.default.project_id

     # Waits for the required APIs to be enabled.
     depends_on = [
       google_project_service.default
     ]
   }

   # Creates a Firebase Android App in the new project created above.
   resource "google_firebase_android_app" "default" {
     provider = google-beta

     project      = google_project.default.project_id
     display_name = "My Awesome Android app"
     package_name = "awesome.package.name"

     # Wait for Firebase to be enabled in the Google Cloud project before creating this App.
     depends_on = [
       google_firebase_project.default,
     ]
   }
   ```

<br />

##### View a highly
annotated version of this example config file

<br />

If you're not familiar with the infrastructure of projects and apps as
resources, review the following documentation:

- [Understand Firebase projects](https://firebase.google.com/docs/projects/learn-more)
- [Reference documentation](https://firebase.google.com/docs/reference/firebase-management/rest) for Firebase project management

```terraform
# Terraform configuration to set up providers by version.
...

# Configures the provider to use the resource block's specified project for quota checks.
...

# Configures the provider to not use the resource block's specified project for quota checks.
...

# Creates a new Google Cloud project.
resource "google_project" "default" {
  # Use the provider that enables the setup of quota checks for a new project
  provider   = google-beta.no_user_project_override

  name            = "Project Display Name"        // learn more about the https://firebase.google.com/docs/projects/learn-more#project-name
  project_id      = "project-id-for-new-project"  // learn more about the https://firebase.google.com/docs/projects/learn-more#project-id
  # Required for any service that requires the Blaze pricing plan
  # (like Firebase Authentication with GCIP)
  billing_account = "000000-000000-000000"

  # Required for the project to display in any list of Firebase projects.
  labels = {
    "firebase" = "enabled"  // learn more about the https://firebase.google.com/support/faq#project-label-firebase-enabled
  }
}

# Enables required APIs.
resource "google_project_service" "default" {
  # Use the provider without quota checks for enabling APIS
  provider = google-beta.no_user_project_override
  project  = google_project.default.project_id
  for_each = toset([
    "cloudbilling.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "firebase.googleapis.com",
    # Enabling the ServiceUsage API allows the new project to be quota checked from now on.
    "serviceusage.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created above.
# This action essentially "creates a Firebase project" and allows the project to use
# Firebase services (like Firebase Authentication) and
# Firebase tooling (like the Firebase console).
# Learn more about the https://firebase.google.com/docs/projects/learn-more#firebase-cloud-relationship.
resource "google_firebase_project" "default" {
  # Use the provider that performs quota checks from now on
  provider = google-beta

  project  = google_project.default.project_id

  # Waits for the required APIs to be enabled.
  depends_on = [
    google_project_service.default
  ]
}

# Creates a Firebase Android App in the new project created above.
# Learn more about the https://firebase.google.com/docs/projects/learn-more#projects-apps-products.
resource "google_firebase_android_app" "default" {
  provider = google-beta

  project      = google_project.default.project_id
  display_name = "My Awesome Android app"  # learn more about an https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp.FIELDS.display_name
  package_name = "awesome.package.name"    # learn more about an https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps#AndroidApp.FIELDS.package_name

  # Wait for Firebase to be enabled in the Google Cloud project before creating this App.
  depends_on = [
    google_firebase_project.default,
  ]
}
```

<br />

<br />

*** ** * ** ***

### **Step 2:** Run Terraform commands to create the specified infrastructure

To provision the resources and enable the services specified in your `main.tf`
file, run the following commands from the same directory as your `main.tf` file.
For detailed information about these commands, see the
[Terraform documentation](https://developer.hashicorp.com/terraform/cli/commands).

1. If this is the first time that you're running Terraform commands in the
   directory, you need to initialize the configuration directory and install
   the Google Terraform provider. Do this by running the following command:

   ```
   terraform init
   ```
2. Create the infrastructure specified in your `main.tf` file by running the
   following command:

   ```
   terraform apply
   ```
3. Confirm that everything was provisioned or enabled as expected:

   - **Option 1:** See the configuration printed in your terminal by running the
     following command:

     ```
     terraform show
     ```
   - **Option 2:** View your Firebase project in the
     [Firebase console](https://console.firebase.google.com/).

<br />

*** ** * ** ***

## Firebase resources with Terraform support

The following Firebase and Google resources have Terraform support. And we're
adding more resources all the time! So if you don't see the resource that you
want to manage with Terraform, then check back soon to see if it's available or
request it by
[filing an issue in the GitHub repo](https://github.com/hashicorp/terraform-provider-google/issues?q=is:issue+is:open+firebase).

*** ** * ** ***

### Firebase project and app management

- [`google_firebase_project`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_project) ---
  enable Firebase services on an existing Google Cloud project

- Firebase Apps

  - [`google_firebase_apple_app`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_apple_app) --- create or manage a Firebase Apple platforms App
  - [`google_firebase_android_app`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_android_app) --- create or manage a Firebase Android App
  - [`google_firebase_web_app`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_web_app) --- create or manage a Firebase Web App

  > [!IMPORTANT]
  > **Important:** Whenever you create a Firebase App, you also need to configure your app's codebase to use Firebase, which includes adding your app's Firebase config and the Firebase SDKs for the products you want to use.

*** ** * ** ***

### Firebase Authentication

- [`google_identity_platform_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/identity_platform_config) ---
  enable Google Cloud Identity Platform (GCIP) (which is the backend for Firebase Authentication)
  and provide project-level authentication settings

  - Configuring Firebase Authentication via Terraform requires enabling GCIP. Make
    sure to review the
    [sample `.tf` file for how to set up Firebase Authentication](https://firebase.google.com/docs/projects/terraform/get-started#tf-sample-auth).

  - The project in which Terraform will enable GCIP and/or Firebase Authentication
    must be on the Blaze pricing plan (that is, the project must have an
    associated Cloud Billing account). You can do this programmatically by
    setting the
    [`billing_account`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/google_project#billing_account)
    attribute in the `google_project` resource.

  - This resource also enables more configurations, like local sign-in methods,
    such as anonymous, email/password, and phone authentication, as well as
    blocking functions and authorized domains.

- [`google_identity_platform_default_supported_idp_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/identity_platform_default_supported_idp_config) ---
  configure common federated Identity Providers, like Google, Facebook, or Apple

- [`identity_platform_oauth_idp_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/identity_platform_oauth_idp_config) ---
  configure arbitrary OAuth Identity Provider (IdP) sources

- [`google_identity_platform_inbound_saml_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/identity_platform_inbound_saml_config) ---
  configure SAML integrations

Not yet supported:

- Configuring multi-factor authentication (MFA) via Terraform

*** ** * ** ***

### Firebase App Hosting

- [`google_firebase_app_hosting_backend`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firebase_app_hosting_backend)
  --- create and manage a Firebase App Hosting backend, including its GitHub
  repository connection and live branch for continuous deployment.

- [`google_firebase_app_hosting_build`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firebase_app_hosting_build)
  --- create a build for a backend, at a specific point codebase reference tag
  and point in time.

- [`google_firebase_app_hosting_traffic`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firebase_app_hosting_traffic)
  --- roll out a build or configure continuous GitHub deployment.

*** ** * ** ***

### Firebase Data Connect

- [`google_firebase_data_connect_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firebase_data_connect_service) --- create a Data Connect service

*** ** * ** ***

### Firebase Realtime Database

- [`google_firebase_database_instance`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_database_instance) --- create a Realtime Database instance

Not yet supported:

- Deploying Firebase Realtime Database Security Rules via Terraform (learn how to [deploy these Security Rules](https://firebase.google.com/docs/rules/manage-deploy#realtime-database) using other tooling, including programmatic options)

*** ** * ** ***

### Cloud Firestore

- [`google_firestore_database`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firestore_database) ---
  create a Cloud Firestore instance

  > [!IMPORTANT]
  > **Important:** Set the following field to use Cloud Firestore with Firebase: `type = "FIRESTORE_NATIVE"`

- [`google_firestore_index`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_index) ---
  enable efficient queries for Cloud Firestore

- [`google_firestore_document`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_document) ---
  seed a Cloud Firestore instance with a specific document in a collection

  **Important:** Do not use real end-user or production data in this seed
  document.

*** ** * ** ***

### Cloud Storage for Firebase

- [`google_firebase_storage_bucket`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_storage_bucket) ---
  make an existing Cloud Storage bucket accessible for Firebase SDKs,
  authentication, and Firebase Security Rules

- [`google_storage_bucket_object`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/storage_bucket_object) ---
  add an object to a Cloud Storage bucket

  **Important:** Do not use real end-user or production data in this file.

> [!CAUTION]
> **Starting October 30, 2024** ,
> you can no longer provision the *default* Cloud Storage bucket
> using Terraform. For details about these changes, see our
> [FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#terraform-changes).
>
> Instead, provision the default Cloud Storage bucket using the
> [Firebase console](https://console.firebase.google.com/project/_/storage/) or the
> [`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create)
> endpoint.

*** ** * ** ***

### Firebase Security Rules (for Cloud Firestore and Cloud Storage)

Note that Firebase Realtime Database uses a different provisioning system for its
Firebase Security Rules.

- [`google_firebaserules_ruleset`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firebaserules_ruleset) ---
  define Firebase Security Rules that apply to a Cloud Firestore instance or a
  Cloud Storage bucket

- [`google_firebaserules_release`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firebaserules_release) ---
  deploy specific rulesets to a Cloud Firestore instance or a
  Cloud Storage bucket

  > [!IMPORTANT]
  > **Important:** A `ruleset` doesn't go into effect until the latest deployed `release` specifies that `ruleset` as the one to be in effect for the Cloud Firestore instance and/or Cloud Storage bucket.

*** ** * ** ***

### Firebase App Check

- [`google_firebase_app_check_service_config`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_app_check_service_config) --- enable App Check enforcement for a service
- [`google_firebase_app_check_app_attest_config`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_app_check_app_attest_config) --- register an Apple platforms app with the App Attest provider
- [`google_firebase_app_check_device_check_config`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_app_check_device_check_config) --- register an Apple platforms app with the DeviceCheck provider
- [`google_firebase_app_check_play_integrity_config`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_app_check_play_integrity_config) --- register an Android app with the Play Integrity provider
- [`google_firebase_app_check_recaptcha_enterprise_config`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_app_check_recaptcha_enterprise_config) --- register a web app with the reCAPTCHA Enterprise provider
- [`google_firebase_app_check_recaptcha_v3_config`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_app_check_recaptcha_v3_config) --- register a web app with the reCAPTCHA v3 provider
- [`google_firebase_app_check_debug_token`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firebase_app_check_debug_token) --- use debug tokens for testing

*** ** * ** ***

### Firebase Extensions

- [`google_firebase_extensions_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firebase_extensions_instance) --- install or update an instance of a Firebase Extension

<br />

*** ** * ** ***

## Sample Terraform config files for common use cases

<br />

#### Set up Firebase Authentication with
GCIP

<br />

This config creates a new Google Cloud project,
associates the project with a Cloud Billing account (the Blaze pricing plan
is required for Firebase Authentication with GCIP),
enables Firebase services for the project,
sets up Firebase Authentication with GCIP,
and registers three different app types with the project.

Note that enabling GCIP is required to set up Firebase Authentication via Terraform.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "auth" {
  provider  = google-beta.no_user_project_override
  folder_id = "folder-id-for-new-project"
  name            = "Project Display Name"
  project_id      = "project-id-for-new-project"

  # Associates the project with a Cloud Billing account
  # (required for Firebase Authentication with GCIP).
  billing_account = "000000-000000-000000"
}

# Enables required APIs.
resource "google_project_service" "auth" {
  provider = google-beta.no_user_project_override
  project  = google_project.auth.project_id
  for_each = toset([
    "cloudbilling.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "serviceusage.googleapis.com",
    "identitytoolkit.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created above.
resource "google_firebase_project" "auth" {
  provider = google-beta
  project  = google_project.auth.project_id

  depends_on = [
    google_project_service.auth,
  ]
}

# Creates an Identity Platform config.
# Also enables Firebase Authentication with Identity Platform in the project if not.
resource "google_identity_platform_config" "auth" {
  provider = google-beta
  project  = google_firebase_project.auth.project

  # Auto-deletes anonymous users
  autodelete_anonymous_users = true

  # Configures local sign-in methods, like anonymous, email/password, and phone authentication.
  sign_in {
    allow_duplicate_emails = true

    anonymous {
      enabled = true
    }

    email {
      enabled = true
      password_required = false
    }

    phone_number {
      enabled = true
      test_phone_numbers = {
        "+11231231234" = "000000"
      }
    }
  }

  # Sets an SMS region policy.
  sms_region_config {
    allowlist_only {
      allowed_regions = [
        "US",
        "CA",
      ]
    }
  }

  # Configures blocking functions.
  blocking_functions {
    triggers {
      event_type = "beforeSignIn"
      function_uri = "https://us-east1-${google_project.auth.project_id}.cloudfunctions.net/before-sign-in"
    }
    forward_inbound_credentials {
      refresh_token = true
      access_token = true
      id_token = true
    }
  }

  # Configures a temporary quota for new signups for anonymous, email/password, and phone number.
  quota {
    sign_up_quota_config {
      quota = 1000
      start_time = ""
      quota_duration = "7200s"
    }
  }

  # Configures authorized domains.
  authorized_domains = [
    "localhost",
    "${google_project.auth.project_id}.firebaseapp.com",
    "${google_project.auth.project_id}.web.app",
  ]
}

# Creates a Firebase Android App in the new project created above.
resource "google_firebase_android_app" "auth" {
  provider     = google-beta
  project      = google_firebase_project.auth.project
  display_name = "My Android app"
  package_name = "android.package.name"
}

# Creates a Firebase Apple-platforms App in the new project created above.
resource "google_firebase_apple_app" "auth" {
  provider     = google-beta
  project      = google_firebase_project.auth.project
  display_name = "My Apple app"
  bundle_id    = "apple.app.12345"
}

# Creates a Firebase Web App in the new project created above.
resource "google_firebase_web_app" "auth" {
  provider     = google-beta
  project      = google_firebase_project.auth.project
  display_name = "My Web app"
}
```

<br />

<br />

<br />

#### Provision a
Firebase Data Connect service

<br />

This config creates a new Google Cloud project,
enables Firebase services for the project, and
provisions a Data Connect service.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "dataconnect" {
  provider   = google-beta.no_user_project_override
  folder_id  = "folder-id-for-new-project"
  name       = "Project Display Name"
  project_id = "project-id-for-new-project"

  # Associates the project with a Cloud Billing account
  # (required to use Firebase Data Connect).
  billing_account = "000000-000000-000000"

  # Required for the project to display in a list of Firebase projects.
  labels = {
    "firebase" = "enabled"
  }
}

# Enables required APIs.
resource "google_project_service" "services" {
  provider = google-beta.no_user_project_override
  project  = google_project.dataconnect.project_id
  for_each = toset([
    "serviceusage.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "firebasedataconnect.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created earlier.
resource "google_firebase_project" "dataconnect" {
  provider = google-beta
  project  = google_project.dataconnect.project_id

  depends_on = [google_project_service.services]
}

# Create a Firebase Data Connect service
resource "google_firebase_data_connect_service" "dataconnect-default" {
  project         = google_firebase_project.dataconnect.project
  location        = "name-of-region-for-service"
  service_id      = "${google_firebase_project.dataconnect.project}-default-fdc"
  deletion_policy = "DEFAULT"
}
```

<br />

<br />

<br />

#### Provision the
default Firebase Realtime Database instance

<br />

This config creates a new Google Cloud project,
enables Firebase services for the project,
provisions the project's default Realtime Database instance,
and registers three different app types with the project.

> [!NOTE]
> **Note:** Currently, Firebase doesn't support deploying Firebase Realtime Database Security Rules via Terraform. Learn how to [deploy these Security Rules](https://firebase.google.com/docs/rules/manage-deploy#realtime-database) using other tooling, including programmatic options.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "rtdb" {
  provider   = google-beta.no_user_project_override
  folder_id  = "folder-id-for-new-project"
  name       = "Project Display Name"
  project_id = "project-id-for-new-project"
}

# Enables required APIs.
resource "google_project_service" "rtdb" {
  provider = google-beta.no_user_project_override
  project  = google_project.rtdb.project_id
  for_each = toset([
    "serviceusage.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "firebasedatabase.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created above.
resource "google_firebase_project" "rtdb" {
  provider = google-beta
  project  = google_project.rtdb.project_id

  depends_on = [google_project_service.rtdb]
}

# Provisions the default Realtime Database default instance.
resource "google_firebase_database_instance" "database" {
  provider    = google-beta
  project     = google_firebase_project.rtdb.project
  # See available locations: https://firebase.google.com/docs/database/locations
  region      = "name-of-region"
  # This value will become the first segment of the database's URL.
  instance_id = "${google_project.rtdb.project_id}-default-rtdb"
  type        = "DEFAULT_DATABASE"
}

# Creates a Firebase Android App in the new project created above.
resource "google_firebase_android_app" "rtdb" {
  provider     = google-beta
  project      = google_firebase_project.rtdb.project
  display_name = "My Android app"
  package_name = "android.package.name"
}

# Creates a Firebase Apple-platforms App in the new project created above.
resource "google_firebase_apple_app" "rtdb" {
  provider     = google-beta
  project      = google_firebase_project.rtdb.project
  display_name = "My Apple app"
  bundle_id    = "apple.app.12345"
}

# Creates a Firebase Web App in the new project created above.
resource "google_firebase_web_app" "rtdb" {
  provider     = google-beta
  project      = google_firebase_project.rtdb.project
  display_name = "My Web app"
}
```

<br />

<br />

<br />

#### Provision multiple
Firebase Realtime Database instances

<br />

This config creates a new Google Cloud project,
associates the project with a Cloud Billing account (the Blaze pricing plan
is required for multiple Realtime Database instances),
enables Firebase services for the project,
provisions multiple Realtime Database instances
(including the project's default Realtime Database instance),
and registers three different app types with the project.

> [!NOTE]
> **Note:** Currently, Firebase doesn't support deploying Firebase Realtime Database Security Rules via Terraform. Learn how to [deploy these Security Rules](https://firebase.google.com/docs/rules/manage-deploy#realtime-database) using other tooling, including programmatic options.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "rtdb-multi" {
  provider   = google-beta.no_user_project_override
  folder_id  = "folder-id-for-new-project"
  name       = "Project Display Name"
  project_id = "project-id-for-new-project"

  # Associate the project with a Cloud Billing account
  # (required for multiple Realtime Database instances).
  billing_account = "000000-000000-000000"
}

# Enables required APIs.
resource "google_project_service" "rtdb-multi" {
  provider = google-beta.no_user_project_override
  project  = google_project.rtdb-multi.project_id
  for_each = toset([
    "cloudbilling.googleapis.com",
    "serviceusage.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "firebasedatabase.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created above.
resource "google_firebase_project" "rtdb-multi" {
  provider = google-beta
  project  = google_project.rtdb-multi.project_id

  depends_on = [google_project_service.rtdb-multi]
}

# Provisions the default Realtime Database default instance.
resource "google_firebase_database_instance" "database-default" {
  provider    = google-beta
  project     = google_firebase_project.rtdb-multi.project
  # See available locations: https://firebase.google.com/docs/database/locations
  region      = "name-of-region"
  # This value will become the first segment of the database's URL.
  instance_id = "${google_project.rtdb-multi.project_id}-default-rtdb"
  type        = "DEFAULT_DATABASE"
}

# Provisions an additional Realtime Database instance.
resource "google_firebase_database_instance" "database-additional" {
  provider    = google-beta
  project     = google_firebase_project.rtdb-multi.project
  # See available locations: https://firebase.google.com/docs/projects/locations#rtdb-locations
  # This location doesn't need to be the same as the default database instance.
  region      = "name-of-region"
  # This value will become the first segment of the database's URL.
  instance_id = "name-of-additional-database-instance"
  type        = "USER_DATABASE"
}

# Creates a Firebase Android App in the new project created above.
resource "google_firebase_android_app" "rtdb-multi" {
  provider     = google-beta
  project      = google_firebase_project.rtdb-multi.project
  display_name = "My Android app"
  package_name = "android.package.name"
}

# Creates a Firebase Apple-platforms App in the new project created above.
resource "google_firebase_apple_app" "rtdb-multi" {
  provider     = google-beta
  project      = google_firebase_project.rtdb-multi.project
  display_name = "My Apple app"
  bundle_id    = "apple.app.12345"
}

# Creates a Firebase Web App in the new project created above.
resource "google_firebase_web_app" "rtdb-multi" {
  provider     = google-beta
  project      = google_firebase_project.rtdb-multi.project
  display_name = "My Web app"
}
```

<br />

<br />

<br />

#### Provision the default
Cloud Firestore instance

<br />

This config creates a new Google Cloud project,
enables Firebase services for the project,
provisions the project's default Cloud Firestore instance,
and registers three different app types with the project.

It also provisions Firebase Security Rules for the default Cloud Firestore instance,
creates a Cloud Firestore index,
and adds a Cloud Firestore document with seed data.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "firestore" {
  provider   = google-beta.no_user_project_override
  folder_id  = "folder-id-for-new-project"
  name       = "Project Display Name"
  project_id = "project-id-for-new-project"
}

# Enables required APIs.
resource "google_project_service" "firestore" {
  provider = google-beta.no_user_project_override
  project  = google_project.firestore.project_id
  for_each = toset([
    "cloudresourcemanager.googleapis.com",
    "serviceusage.googleapis.com",
    "firestore.googleapis.com",
    "firebaserules.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created above.
resource "google_firebase_project" "firestore" {
  provider = google-beta
  project  = google_project.firestore.project_id

  depends_on = [google_project_service.firestore]
}

# Provisions the Firestore database instance.
resource "google_firestore_database" "firestore" {
  provider                    = google-beta
  project                     = google_firebase_project.firestore.project
  name                        = "(default)"
  # See available locations: https://firebase.google.com/docs/firestore/locations
  location_id                 = "name-of-region"
  # "FIRESTORE_NATIVE" is required to use Firestore with Firebase SDKs, authentication, and Firebase Security Rules.
  type                        = "FIRESTORE_NATIVE"
  concurrency_mode            = "OPTIMISTIC"
}

# Creates a ruleset of Firestore Security Rules from a local file.
resource "google_firebaserules_ruleset" "firestore" {
  provider = google-beta
  project  = google_firestore_database.firestore.project
  source {
    files {
      name = "firestore.rules"
      # Write security rules in a local file named "firestore.rules".
      # Learn more: https://firebase.google.com/docs/firestore/security/get-started
      content = file("firestore.rules")
    }
  }
}

# Releases the ruleset for the Firestore instance.
resource "google_firebaserules_release" "firestore" {
  provider     = google-beta
  name         = "cloud.firestore"  # must be cloud.firestore
  ruleset_name = google_firebaserules_ruleset.firestore.name
  project      = google_firestore_database.firestore.project
}

# Adds a new Firestore index.
resource "google_firestore_index" "indexes" {
  provider = google-beta
  project  = google_firestore_database.firestore.project

  collection  = "quiz"
  query_scope = "COLLECTION"

  fields {
    field_path = "question"
    order      = "ASCENDING"
  }

  fields {
    field_path = "answer"
    order      = "ASCENDING"
  }
}

# Adds a new Firestore document with seed data.
# Don't use real end-user or production data in this seed document.
resource "google_firestore_document" "doc" {
  provider    = google-beta
  project     = google_firestore_database.firestore.project
  collection  = "quiz"
  document_id = "question-1"
  fields      = "{\"question\":{\"stringValue\":\"Favorite Database\"},\"answer\":{\"stringValue\":\"Firestore\"}}"
}

# Creates a Firebase Android App in the new project created above.
resource "google_firebase_android_app" "firestore" {
  provider     = google-beta
  project      = google_firebase_project.firestore.project
  display_name = "My Android app"
  package_name = "android.package.name"
}

# Creates a Firebase Apple-platforms App in the new project created above.
resource "google_firebase_apple_app" "firestore" {
  provider     = google-beta
  project      = google_firebase_project.firestore.project
  display_name = "My Apple app"
  bundle_id    = "apple.app.12345"
}

# Creates a Firebase Web App in the new project created above.
resource "google_firebase_web_app" "firestore" {
  provider     = google-beta
  project      = google_firebase_project.firestore.project
  display_name = "My Web app"
}
```

This is the ruleset of Cloud Firestore Security Rules that should be in a local file
named `firestore.rules`.

```terraform
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /some_collection/{document} {
      allow read, create, update: if request.auth != null;
    }
  }
}
```

<br />

<br />

<br />

#### Provision the
default Cloud Storage bucket

<br />

> [!CAUTION]
> **Starting October 30, 2024** ,
> you can no longer provision the *default* Cloud Storage bucket
> using Terraform. For details about these changes, see our
> [FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#terraform-changes).
>
> Instead, provision the default Cloud Storage bucket using the
> [Firebase console](https://console.firebase.google.com/project/_/storage/) or the
> [`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create)
> endpoint.

<br />

<br />

<br />

#### Provision
additional Cloud Storage buckets

<br />

This config creates a new Google Cloud project,
associates the project with a Cloud Billing account (the Blaze pricing plan
is required for additional buckets),
enables Firebase services for the project,
provisions additional, non-default Cloud Storage buckets,
and registers three different app types with the project.

It also provisions Firebase Security Rules for each Cloud Storage bucket,
and uploads a file to one of the Cloud Storage buckets.

> [!CAUTION]
> **Starting October 30, 2024** ,
> you can no longer provision the *default* Cloud Storage bucket
> using Terraform. For details about these changes, see our
> [FAQs](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024#terraform-changes).
>
> Instead, provision the default Cloud Storage bucket using the
> [Firebase console](https://console.firebase.google.com/project/_/storage/) or the
> [`projects.defaultBucket.create`](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create)
> endpoint.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "storage-multi" {
  provider  = google-beta.no_user_project_override
  folder_id = "folder-id-for-new-project"
  name            = "Project Display Name"
  project_id      = "project-id-for-new-project"

  # Associates the project with a Cloud Billing account
  # (required for multiple Cloud Storage buckets).
  billing_account = "000000-000000-000000"
}

# Enables required APIs.
resource "google_project_service" "storage-multi" {
  provider = google-beta.no_user_project_override
  project  = google_project.storage-multi.project_id
  for_each = toset([
    "cloudbilling.googleapis.com",
    "serviceusage.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "firebaserules.googleapis.com",
    "firebasestorage.googleapis.com",
    "storage.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created above.
resource "google_firebase_project" "storage-multi" {
  provider = google-beta
  project  = google_project.storage-multi.project_id

  depends_on = [google_project_service.storage-multi]
}

# Provisions a Cloud Storage bucket.
resource "google_storage_bucket" "bucket-1" {
  provider = google-beta
  project  = google_firebase_project.storage-multi.project
  name     = "name-of-storage-bucket"
  # See available locations: https://cloud.google.com/storage/docs/locations#available-locations
  location = "name-of-region-for-bucket"
}

# Provisions an additional Cloud Storage bucket.
resource "google_storage_bucket" "bucket-2" {
  provider = google-beta
  project  = google_firebase_project.storage-multi.project
  name     = "name-of-additional-storage-bucket"
  # See available locations: https://cloud.google.com/storage/docs/locations#available-locations
  # This location does not need to be the same as the existing Storage bucket.
  location = "name-of-region-for-additional-bucket"
}

# Makes the first Storage bucket accessible for Firebase SDKs, authentication, and Firebase Security Rules.
resource "google_firebase_storage_bucket" "bucket-1" {
  provider  = google-beta
  project   = google_firebase_project.storage-multi.project
  bucket_id = google_storage_bucket.bucket-1.name
}

# Makes the additional Storage bucket accessible for Firebase SDKs, authentication, and Firebase Security Rules.
resource "google_firebase_storage_bucket" "bucket-2" {
  provider  = google-beta
  project   = google_firebase_project.storage-multi.project
  bucket_id = google_storage_bucket.bucket-2.name
}

# Creates a ruleset of Firebase Security Rules from a local file.
resource "google_firebaserules_ruleset" "storage-multi" {
  provider = google-beta
  project  = google_firebase_project.storage-multi.project
  source {
    files {
      # Write security rules in a local file named "storage.rules"
      # Learn more: https://firebase.google.com/docs/storage/security/get-started
      name    = "storage.rules"
      content = file("storage.rules")
    }
  }
}

# Releases the ruleset to the first Storage bucket.
resource "google_firebaserules_release" "bucket-1" {
  provider     = google-beta
  name         = "firebase.storage/${google_storage_bucket.bucket-1.name}"
  ruleset_name = "projects/${google_project.storage-multi.project_id}/rulesets/${google_firebaserules_ruleset.storage-multi.name}"
  project      = google_firebase_project.storage-multi.project
}

# Releases the ruleset to the additional Storage bucket.
resource "google_firebaserules_release" "bucket-2" {
  provider     = google-beta
  name         = "firebase.storage/${google_storage_bucket.bucket-2.name}"
  ruleset_name = "projects/${google_project.storage-multi.project_id}/rulesets/${google_firebaserules_ruleset.storage-multi.name}"
  project      = google_firebase_project.storage-multi.project
}

# Uploads a new file to the first Storage bucket.
# Do not use real end-user or production data in this file.
resource "google_storage_bucket_object" "cat-picture-multi" {
  provider = google-beta
  name     = "cat.png"
  source   = "path/to/cat.png"
  bucket   = google_storage_bucket.bucket-1.name
}

# Creates a Firebase Android App in the new project created above.
resource "google_firebase_android_app" "storage-multi" {
  provider     = google-beta
  project      = google_firebase_project.storage-multi.project
  display_name = "My Android app"
  package_name = "android.package.name"
}

# Creates a Firebase Apple-platforms App in the new project created above.
resource "google_firebase_apple_app" "storage-multi" {
  provider     = google-beta
  project      = google_firebase_project.storage-multi.project
  display_name = "My Apple app"
  bundle_id    = "apple.app.12345"
}

# Creates a Firebase Web App in the new project created above.
resource "google_firebase_web_app" "storage-multi" {
  provider     = google-beta
  project      = google_firebase_project.storage-multi.project
  display_name = "My Web app"
}
```

This is the ruleset of Cloud Storage Security Rules that should be in a local file
named `storage.rules`.

```terraform
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /some_folder/{fileName} {
      allow read, write: if request.auth != null;
    }
  }
}
```

<br />

<br />

<br />

#### Protect an API resource
with Firebase App Check

<br />

> [!NOTE]
> **Note:** This config shows an example for enabling enforcement of App Check for Cloud Firestore, but you can also [use App Check with other products and services](https://firebase.google.com/docs/app-check).

This config creates a new Google Cloud project,
enables Firebase services for the project, and
sets up and enables enforcement of Firebase App Check for Cloud Firestore
so that it can only be accessed from your Android app.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "appcheck" {
  provider   = google-beta.no_user_project_override
  folder_id  = "folder-id-for-new-project"
  name       = "Project Display Name"
  project_id = "project-id-for-new-project"
}

# Enables required APIs.
resource "google_project_service" "services" {
  provider = google-beta.no_user_project_override
  project  = google_project.appcheck.project_id
  for_each = toset([
    "cloudresourcemanager.googleapis.com",
    "firebase.googleapis.com",
    "firebaseappcheck.googleapis.com",
    "firestore.googleapis.com",
    "serviceusage.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created earlier.
resource "google_firebase_project" "appcheck" {
  provider = google-beta
  project  = google_project.appcheck.project_id

  depends_on = [google_project_service.services]
}

# Provisions the Firestore database instance.
resource "google_firestore_database" "database" {
  provider = google-beta
  project  = google_firebase_project.appcheck.project
  name     = "(default)"
  # See available locations: https://firebase.google.com/docs/projects/locations#default-cloud-location
  location_id = "name-of-region"
  # "FIRESTORE_NATIVE" is required to use Firestore with Firebase SDKs, authentication, and Firebase Security Rules.
  type             = "FIRESTORE_NATIVE"
  concurrency_mode = "OPTIMISTIC"
}

# Creates a Firebase Android App in the new project created earlier.
resource "google_firebase_android_app" "appcheck" {
  provider     = google-beta
  project      = google_firebase_project.appcheck.project
  display_name = "Play Integrity app"
  package_name = "package.name.playintegrity"
  sha256_hashes = [
    # TODO: insert your Android app's SHA256 certificate
  ]
}

# Register the Android app with the Play Integrity provider
resource "google_firebase_app_check_play_integrity_config" "appcheck" {
  provider = google-beta
  project  = google_firebase_project.appcheck.project
  app_id   = google_firebase_android_app.appcheck.app_id

  depends_on = [google_firestore_database.database]

  lifecycle {
    precondition {
      condition     = length(google_firebase_android_app.appcheck.sha256_hashes) > 0
      error_message = "Provide a SHA-256 certificate on the Android App to use App Check"
    }
  }
}

# Enable enforcement of App Check for Firestore
resource "google_firebase_app_check_service_config" "firestore" {
  provider = google-beta

  project    = google_firebase_project.appcheck.project
  service_id = "firestore.googleapis.com"

  depends_on = [google_project_service.services]
}
```

<br />

<br />

<br />

#### Install an
instance of a Firebase Extension

<br />

This config creates a new Google Cloud project,
enables Firebase services for the project, and
installs a new instance of a Firebase Extension
in the project. If the instance already exists,
its parameters are updated based on the values provided in the config.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "extensions" {
  provider   = google-beta.no_user_project_override
  folder_id  = "folder-id-for-new-project"
  name       = "Project Display Name"
  project_id = "project-id-for-new-project"

  # Associates the project with a Cloud Billing account
  # (required to use Firebase Extensions).
  billing_account = "000000-000000-000000"
}

# Enables required APIs.
resource "google_project_service" "extensions" {
  provider = google-beta.no_user_project_override
  project  = google_project.extensions.project_id
  for_each = toset([
    "cloudbilling.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "serviceusage.googleapis.com",
    "firebase.googleapis.com",
    "firebaseextensions.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created above.
resource "google_firebase_project" "extensions" {
  provider = google-beta
  project  = google_project.extensions.project_id

  depends_on = [
    google_project_service.extensions,
  ]
}

# Installs an instance of the "Translate Text in Firestore" extension.
# Or updates the extension if the specified instance already exists.
resource "google_firebase_extensions_instance" "translation" {
  provider = google-beta
  project = google_firebase_project.extensions.project

  instance_id = "translate-text-in-firestore"
  config {
    extension_ref = "firebase/firestore-translate-text"

    params = {
      COLLECTION_PATH      = "posts/comments/translations"
      DO_BACKFILL          = true
      LANGUAGES            = "ar,en,es,de,fr"
      INPUT_FIELD_NAME     = "input"
      LANGUAGES_FIELD_NAME = "languages"
      OUTPUT_FIELD_NAME    = "translated"
    }

    system_params = {
      "firebaseextensions.v1beta.function/location"                   = "us-central1"
      "firebaseextensions.v1beta.function/memory"                     = "256"
      "firebaseextensions.v1beta.function/minInstances"               = "0"
      "firebaseextensions.v1beta.function/vpcConnectorEgressSettings" = "VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED"
    }
  }
}
```

<br />

<br />

<br />

#### Enable and protect Firebase AI Logic

<br />

This config creates a new Google Cloud project,
enables Firebase services for the project, including Firebase AI Logic, and
sets up and enables enforcement of Firebase App Check for
Firebase AI Logic so that it can only be accessed from your apps.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "vertex" {
  provider   = google-beta.no_user_project_override
  folder_id  = "folder-id-for-new-project"
  name       = "Project Display Name"
  project_id = "project-id-for-new-project"

  # Associate the project with a Cloud Billing account
  # (required for Vertex AI in Firebase).
  billing_account = "000000-000000-000000"
}

# Enables required APIs.
resource "google_project_service" "services" {
  provider   = google-beta.no_user_project_override

  project  = google_project.vertex.project_id
  for_each = toset([
    "cloudresourcemanager.googleapis.com",
    "firebase.googleapis.com",
    "serviceusage.googleapis.com",
    # Required APIs for Vertex AI in Firebase
    "aiplatform.googleapis.com",
    "firebasevertexai.googleapis.com",
    # App Check is recommended to protect Vertex AI in Firebase from abuse
    "firebaseappcheck.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created earlier.
resource "google_firebase_project" "vertex" {
  provider = google-beta
  project  = google_project.vertex.project_id

  depends_on = [google_project_service.services]
}

# Creates a Firebase Web App in the new project created earlier.
resource "google_firebase_web_app" "app" {
  provider = google-beta
  project  = google_firebase_project.vertex.project

  display_name = "My Web App"
}

# Creates a Firebase Android App in the new project created earlier.
resource "google_firebase_android_app" "app" {
  provider     = google-beta
  project      = google_firebase_project.vertex.project
  display_name = "My Android App"
  package_name = "package.name.playintegrity"
  sha256_hashes = [
    # TODO: insert your Android app's SHA256 certificate
  ]
}

# Creates a Firebase Apple App in the new project created earlier.
resource "google_firebase_apple_app" "app" {
  provider     = google-beta
  project      = google_firebase_project.vertex.project
  display_name = "My Apple App"
  bundle_id    = "bundle.id"
  team_id      = "1234567890"
}

### Protects Vertex AI in Firebase with App Check.

# Turns on enforcement for Vertex AI in Firebase
resource "google_firebase_app_check_service_config" "vertex" {
  provider = google-beta

  project          = google_firebase_project.vertex.project
  service_id       = "firebaseml.googleapis.com"
  enforcement_mode = "ENFORCED"
}

# Enables the reCAPTCHA Enterprise API
resource "google_project_service" "recaptcha_enterprise" {
  provider = google-beta

  project = google_firebase_project.vertex.project
  service = "recaptchaenterprise.googleapis.com"

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables the Play Integrity API
resource "google_project_service" "play_integrity" {
  provider = google-beta

  project = google_firebase_project.vertex.project
  service = "playintegrity.googleapis.com"

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Allows the web app to use reCAPTCHA Enterprise with App Check
resource "google_firebase_app_check_recaptcha_enterprise_config" "appcheck" {
  provider = google-beta

  project   = google_firebase_project.vertex.project
  app_id    = google_firebase_web_app.app.app_id
  site_key  = "your site key"
  token_ttl = "7200s" # Optional

  depends_on = [google_project_service.recaptcha_enterprise]
}

# Registers the Android app with the Play Integrity provider
resource "google_firebase_app_check_play_integrity_config" "appcheck" {
  provider  = google-beta
  project   = google_firebase_project.vertex.project
  app_id    = google_firebase_android_app.app.app_id
  token_ttl = "7200s" # Optional

  lifecycle {
    precondition {
      condition     = length(google_firebase_android_app.app.sha256_hashes) > 0
      error_message = "Provide a SHA-256 certificate on the Android App to use App Check"
    }
  }

  depends_on = [google_project_service.play_integrity]
}

# Registers the Apple app with the AppAttest provider
resource "google_firebase_app_check_app_attest_config" "appcheck" {
  provider  = google-beta
  project   = google_firebase_project.vertex.project
  app_id    = google_firebase_apple_app.app.app_id
  token_ttl = "7200s" # Optional

  lifecycle {
    precondition {
      condition     = google_firebase_apple_app.app.team_id != ""
      error_message = "Provide a Team ID on the Apple App to use App Check"
    }
  }
}
```

<br />

<br />

<br />

#### Manually provision an App Hosting backend

<br />

This configuration demonstrates how to manually provision an App Hosting
backend using Terraform. This approach gives you fine-grained control over the
resources created, but requires you to define each resource individually. This
is useful when you need to customize the backend beyond the default options.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "apphosting" {
  provider   = google-beta.no_user_project_override
  folder_id  = "folder-id-for-new-project"
  name       = "Project Display Name"
  project_id = "project-id-for-new-project"

  # Associates the project with a Cloud Billing account
  # (required to use Firebase App Hosting).
  billing_account = "000000-000000-000000"
}

# Enables required APIs.
resource "google_project_service" "services" {
  provider = google-beta.no_user_project_override
  project  = google_project.apphosting.project_id
  for_each = toset([
    "cloudresourcemanager.googleapis.com",
    "firebase.googleapis.com",
    "firebaseapphosting.googleapis.com",
    "serviceusage.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created earlier.
resource "google_firebase_project" "apphosting" {
  provider = google-beta
  project  = google_project.apphosting.project_id

  depends_on = [google_project_service.services]
}

# Creates a Firebase Web App in the new project created earlier.
resource "google_firebase_web_app" "apphosting" {
  provider     = google-beta
  project      = google_firebase_project.apphosting.project
  display_name = "My web app"
}

# Creates a Firebase App Hosting Backend
resource "google_firebase_app_hosting_backend" "example" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project

  # Choose the region closest to your users
  location         = "name-of-region-for-service"
  backend_id       = "name-of-backend-for-service"
  app_id           = google_firebase_web_app.apphosting.app_id
  display_name     = "My Backend"
  serving_locality = "GLOBAL_ACCESS"
  service_account  = google_service_account.service_account.email
}

# Creates the service account for Firebase App Hosting
resource "google_service_account" "service_account" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project

  # Must be firebase-app-hosting-compute
  account_id                   = "firebase-app-hosting-compute"
  display_name                 = "Firebase App Hosting compute service account"

  # Do not throw if already exists
  create_ignore_already_exists = true
}

# Adds permission to the App Hosting service account
resource "google_project_iam_member" "app_hosting_sa" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project

  for_each = toset([
    "roles/firebase.sdkAdminServiceAgent",
    "roles/firebaseapphosting.computeRunner"
  ])

  role   = each.key
  member = google_service_account.service_account.member
}

# Creates a Build
resource "google_firebase_app_hosting_build" "example" {
  provider = google-beta

  project          = google_firebase_app_hosting_backend.example.project
  location         = google_firebase_app_hosting_backend.example.location
  backend          = google_firebase_app_hosting_backend.example.backend_id
  build_id         = "my-build"

  source {
    container {
      # TODO: use your own image
      image = "us-docker.pkg.dev/cloudrun/container/hello"
    }
  }
}

# Rolls out the Build
resource "google_firebase_app_hosting_traffic" "example" {
  provider = google-beta

  project          = google_firebase_app_hosting_backend.example.project
  location         = google_firebase_app_hosting_backend.example.location
  backend          = google_firebase_app_hosting_backend.example.backend_id

  target {
    splits {
      build = google_firebase_app_hosting_build.example.name
      percent = 100
    }
  }
}
```

<br />

<br />

<br />

#### Provision an
App Hosting backend using GitHub

<br />

This configuration demonstrates how to provision an App Hosting backend
using application code stored in a GitHub repository. This approach allows you
to manage and update your infrastructure through GitHub pull requests and CI/CD
pipelines according to the typical model for App Hosting deployments.

```terraform
# Creates a new Google Cloud project.
resource "google_project" "apphosting" {
  provider   = google-beta.no_user_project_override
  folder_id  = "folder-id-for-new-project"
  name       = "Project Display Name"
  project_id = "project-id-for-new-project"

  # Associates the project with a Cloud Billing account
  # (required to use Firebase App Hosting).
  billing_account = "000000-000000-000000"
}

# Enables required APIs.
resource "google_project_service" "services" {
  provider = google-beta.no_user_project_override
  project  = google_project.apphosting.project_id
  for_each = toset([
    "cloudresourcemanager.googleapis.com",
    "firebase.googleapis.com",
    "firebaseapphosting.googleapis.com",
    "serviceusage.googleapis.com",
    "developerconnect.googleapis.com",
  ])
  service = each.key

  # Don't disable the service if the resource block is removed by accident.
  disable_on_destroy = false
}

# Enables Firebase services for the new project created earlier.
resource "google_firebase_project" "apphosting" {
  provider = google-beta
  project  = google_project.apphosting.project_id

  depends_on = [google_project_service.services]
}

# Creates a Firebase Web App in the new project created earlier.
resource "google_firebase_web_app" "apphosting" {
  provider     = google-beta
  project      = google_firebase_project.apphosting.project
  display_name = "My web app"
}

### Setting up Firebase App Hosting ###

# Creates a Firebase App Hosting Backend
resource "google_firebase_app_hosting_backend" "example" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project

  # Choose the region closest to your users
  location         = "name-of-region-for-service"
  backend_id       = "name-of-backend-for-service"
  app_id           = google_firebase_web_app.apphosting.app_id
  display_name     = "My Backend"
  serving_locality = "GLOBAL_ACCESS"
  service_account  = google_service_account.service_account.email

  codebase {
    repository = google_developer_connect_git_repository_link.my-repository.name
    root_directory = "/"
  }
}

# Creates the service account for Firebase App Hosting
resource "google_service_account" "service_account" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project

  # Must be firebase-app-hosting-compute
  account_id                   = "firebase-app-hosting-compute"
  display_name                 = "Firebase App Hosting compute service account"

  # Do not throw if already exists
  create_ignore_already_exists = true
}

# Adds permission to the App Hosting service account
resource "google_project_iam_member" "app_hosting_sa" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project

  for_each = toset([
    "roles/developerconnect.readTokenAccessor",
    "roles/firebase.sdkAdminServiceAgent",
    "roles/firebaseapphosting.computeRunner"
  ])

  role   = each.key
  member = google_service_account.service_account.member
}

# Configures auto rollout from GitHub
resource "google_firebase_app_hosting_traffic" "example" {
  provider = google-beta

  project  = google_firebase_app_hosting_backend.example.project
  location = google_firebase_app_hosting_backend.example.location
  backend  = google_firebase_app_hosting_backend.example.backend_id

  rollout_policy {
    codebase_branch = "main" # Or another branch
  }
}

###

### Setting up a connection to GitHub ###

# Provisions Service Agent for Developer Connect
resource "google_project_service_identity" "devconnect-p4sa" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project

  service  = "developerconnect.googleapis.com"
}

# Adds permission to Developer Connect Service Agent to manager GitHub tokens
resource "google_project_iam_member" "devconnect-secret" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project

  role     = "roles/secretmanager.admin"
  member   = google_project_service_identity.devconnect-p4sa.member
}

# Connects to a GitHub account
resource "google_developer_connect_connection" "my-connection" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project

  # Must match the google_firebase_app_hosting_backend's location
  location = "name-of-region-for-service"

  # Must be `firebase-app-hosting-github-oauth`
  connection_id = "firebase-app-hosting-github-oauth"
  github_config {
    github_app = "FIREBASE"
  }
  depends_on = [google_project_iam_member.devconnect-secret]
}

# Follow the next steps to set up the GitHub connection
# Tip: Run terraform refresh to obtain the output
output "next_steps" {
  description = "Follow the action_uri if present to continue setup"
  value = google_developer_connect_connection.my-connection.installation_state
}

# Links a GitHub repo to the project
resource "google_developer_connect_git_repository_link" "my-repository" {
  provider = google-beta
  project  = google_firebase_project.apphosting.project
  location = google_developer_connect_connection.my-connection.location

  git_repository_link_id = "my-repo-id"
  parent_connection = google_developer_connect_connection.my-connection.connection_id
  clone_uri = "https://github.com/myuser/myrepo.git"
}

###
```

<br />

<br />

<br />

*** ** * ** ***

## Troubleshooting and FAQ

<br />

#### You want
to learn more about all the different project-related attributes (like
`project` and `user_project_override`)

<br />

This guide uses the following Terraform attributes when working with "projects".

`project` within a `resource` block

:   Recommended: whenever possible, include the `project` attribute within each
    `resource` block

:   By including a project attribute, Terraform will create the infrastructure
    specified in the resource block within the specified project. This guide and
    our sample config files all use this practice.

:   See the official Terraform documentation about
    [`project`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/guides/provider_reference#project).

`user_project_override` within the `provider` block

:   For provisioning most resources, you should use
    `user_project_override = true`, which means to check quota against your own
    Firebase project. However, to set up your new project so that it can accept
    quota checks, you first need to use `user_project_override = false`.

:   See the official Terraform documentation about
    [`user_project_override`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/guides/provider_reference#user_project_override).

<br />

<br />

<br />

#### You get this error:
`generic::permission_denied: Firebase Tos Not Accepted`.

<br />

Make sure that the user account that you're using to run gcloud CLI
commands has accepted the Firebase Terms of Service (Firebase ToS).

- You can do this check by using a browser signed into the user account and
  trying to view an existing Firebase project in the
  [Firebase console](https://console.firebase.google.com/). If you can view
  an existing Firebase project, then the user account has accepted the
  Firebase ToS.

- If you can't view any existing Firebase project, then the user account
  probably hasn't accepted the Firebase ToS. To fix this, create a new
  Firebase project via the
  [Firebase console](https://console.firebase.google.com/) and accept the
  Firebase ToS as part of project creation. You can immediately delete this
  project via *Project Settings* in the console.

<br />

<br />

<br />

#### After running
`terraform apply`, you get this error:
`generic::permission_denied: IAM authority does not have the
permission`.

<br />

Wait a few minutes, and then try running `terraform apply` again.

<br />

<br />

<br />

#### The
creation of a resource failed, but when you run `terraform apply`
again, it says `ALREADY_EXISTS`.

<br />

This could be due to a propagation delay in various systems. Try to resolve this
issue by importing the resource into the Terraform state by running
`terraform import`. Then try running `terraform apply` again.

You can learn how to import each resource in the "Import" section of its
Terraform documentation (for example, the
["Import" documentation for Cloud Firestore](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/firestore_database#import)).

<br />

<br />

<br />

#### When working with
Cloud Firestore, you get this error: `Error creating Index: googleapi:
Error 409;...Concurrent access -- try again`

<br />

As the error suggests, Terraform may be trying to provision multiple indices
and/or creating a document at the same time and ran into a concurrency error.
Try running `terraform apply` again.

<br />

<br />

<br />

#### You get
this error:
`"you may need to specify 'X-Goog-User-Project' HTTP header for quota and
billing purposes"`.

<br />

This error means that Terraform doesn't know which project to check quota
against. To troubleshoot, check the following in the `resource` block:

- Make sure that you have specified a value for the `project` attribute.
- Make sure that you're using the provider with `user_project_override = true` (no alias), which in the Firebase samples is `google-beta`.

<br />

<br />

<br />

#### When creating a
new Google Cloud project, you get the error that the project ID specified for
the new project already exists.

<br />

Here are the possible reasons the project ID may already exist:

- The project associated with that ID belongs to someone else.

  - **To resolve:** Choose another project ID.
- The project associated with that ID was recently deleted (in soft-delete
  state).

  - **To resolve:** If you think that the project associated with the ID belongs to you, then check the state of the project using the [`projects.get` REST API](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects/get).
- The project associated with that ID exists correctly under the current user. A
  possible cause for the error could be that a previous `terraform apply` got
  interrupted.

  - **To resolve:** Run the following commands:  
    `terraform import google_project.default PROJECT_ID` and then  
    `terraform import google_firebase_project.default PROJECT_ID`

<br />

<br />

<br />

#### Why do you
need to provision the default Cloud Firestore instance before the default
Cloud Storage bucket?

<br />

> [!IMPORTANT]
> **Important:** **Starting October 30, 2024** , you can no longer provision the default Cloud Storage bucket using Terraform.

If you provisioned your default Cloud Storage bucket (via
`google_app_engine_application`) *before* you try to provision your
default Cloud Firestore instance, then you'll find that your
default Cloud Firestore instance has already been provisioned. Note that the
provisioned database instance is in Datastore mode, which means that it's *not*
accessible to Firebase SDKs, authentication, or Firebase Security Rules. If you want to use
Cloud Firestore with these Firebase services, then you'll need to empty the
database and then change its database type in the
[Google Cloud console](https://console.cloud.google.com/).

<br />

<br />

<br />

#### When
trying to provision Cloud Storage (via
`google_app_engine_application`) and then your default
Cloud Firestore instance, you get this error:
`Error: Error creating Database: googleapi: Error 409: Database already
exists. Please use another database_id`.

<br />

> [!IMPORTANT]
> **Important:** **Starting October 30, 2024** , you can no longer provision the default Cloud Storage bucket using Terraform.

When you provision a project's default Cloud Storage bucket (via
`google_app_engine_application`) and the project doesn't yet have its default
Cloud Firestore instance, then `google_app_engine_application` automatically
provisions the project's default Cloud Firestore instance.

So, since your project's default Cloud Firestore instance is *already*
provisioned, `google_firestore_database` will error if you try to explicitly
provision that default instance again.

Once the project's default Cloud Firestore instance is provisioned, you cannot
"re-provision" it or change its location. Note that the provisioned database
instance is in Datastore mode, which means that it's *not* accessible to
Firebase SDKs, authentication, or Firebase Security Rules. If you want to use Cloud Firestore
with these Firebase services, then you'll need to empty the database and then
change its database type in the
[Google Cloud console](https://console.cloud.google.com/).

<br />

<br />