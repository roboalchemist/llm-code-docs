# Source: https://docs.earthly.dev/ci-integration/vendor-specific-guides/google-cloud-build.md

# Source: https://docs.earthly.dev/earthly-0.7/ci-integration/vendor-specific-guides/google-cloud-build.md

# Source: https://docs.earthly.dev/earthly-0.6/ci-integration/vendor-specific-guides/google-cloud-build.md

# Google Cloud Build

## Overview

Google's Cloud Build is a popular, hosted build platform with deep integrations into the Google Cloud ecosystem. It includes native support for containerized builds, as well as other build scenarios. This guide will cover the use of Earthly within the `cloudbuild.yaml` spec (though it should be easily ported over to the `json` format if desired).

### Compatibility

Earthly itself is able to run as expected within Cloud Build, including privileged mode features like `WITH DOCKER`. However, Application Default Credentials are not available, so any `gcloud` or `gsutil` commands within your `Earthfile` will require additional manual configuration via a service account.

### Resources

* [Getting Started With Cloud Build](https://cloud.google.com/build/docs/quickstart-build)
* [Authenticating As A Service Account](https://cloud.google.com/docs/authentication/production)
* [`cloudbuild.yaml` Specification](https://cloud.google.com/build/docs/build-config-file-schema)
* [Creating and Managing build triggers](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers)

## Setup

Depending on your needs and existing infrastructure, there may be additional configuration needed in your Google Cloud environment.

### Dependencies

Ensure that your repositories are connected to Cloud Build. [Google has a fantastic walkthrough for this](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo).

### Configuration

{% hint style="danger" %}
**Note**

If you do not intend to use any Google Cloud utilities or capabilities within your build, this service account configuration is optional.
{% endhint %}

Begin by following [Google's instructions to create a service account](https://cloud.google.com/docs/authentication/production#create_service_account). These instructions are partially duplicated below, with some screenshots for completeness.

Start by creating a build service account. Go to the "Create service account" page in the "IAM & Admin" API section, choose the appropriate project, and fill out the step 1 "Service account details". When you are done, click "Create and Continue".

![Step One of configuring a new Google Cloud Service account, with account name and description fields](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-6b8a0bf7ea67b718a7430539da16478aa9dd3565%2Fgoogle-cloud-build-1.png?alt=media\&token=3f25a3dc-c093-41e9-b7f6-6d7938bcca4c)

The creation steps should now ask you for a role to use in your build. The needs for each build are different; so examine your needs, and take care to grant the least privilege needed for your build. One reasonable starting point might be the [default Cloud Build service account permissions](https://cloud.google.com/build/docs/cloud-build-service-account#default_permissions_of_service_account).

![Step two of configuring a new Google Cloud Service account, with a chosen role selected](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-9bc9ad4c3d82bf1faeadb1ac1ad09fb0e82526b1%2Fgoogle-cloud-build-2.png?alt=media\&token=c015a76f-1fc2-4999-afad-67eb874a1cf4)

Click "Done". The console should navigate you to a list of service accounts within the project. At this point, the account should be created, but we still need to create an account key. To do this, click on the email address for this service account in the list.

![The Google Cloud list view of service accounts, with our new account highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-9f17636d754f996101781b0104755d60368b7b19%2Fgoogle-cloud-build-3.png?alt=media\&token=7c735c9c-f9e7-4314-b553-cb81c7f2f590)

Then select "Keys" from the top navigation.

![The top nav of the service account drilldown, with the keys tab highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-57f5282cc128d5afc6e15bda5519cc1504d2b402%2Fgoogle-cloud-build-4.png?alt=media\&token=78be8daa-4158-48b4-8f97-ba39c98f79b9)

Click "Add Key", and then "Create New Key". Choose "JSON" as the key format, and click create. This will download the key to your computer, and you should see it in the list of keys.

![The list view of available keys for a Google Cloud service account](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-333efab4fe36f79e2408247ad6d274315ca1b635%2Fgoogle-cloud-build-5.png?alt=media\&token=bab23c8e-a23c-420a-ade2-6f7257dbab92)

Stash the key in your secret management utility of choice. You'll need to make this key available to your build at runtime. For the rest of our example, we will be using Earthly's [Cloud Secrets](https://docs.earthly.dev/earthly-0.6/earthly-cloud/cloud-secrets).

Often, external secrets management requires some kind of bootstrapping secret (or additional integration) to allow you to access the rest of the secrets in your store. Earthly is no different. We will keep our `EARTHLY_TOKEN` in [Googles Secret Manager](https://cloud.google.com/build/docs/securing-builds/use-secrets) for ease of use.

{% hint style="danger" %}
**Note**

It is also possible to perform these steps via the CLI; the steps are [also detailed in Googles instructions](https://cloud.google.com/docs/authentication/production#command-line). It can also be automated using much of the same steps.
{% endhint %}

## Additional Notes

`earthly` misinterprets the Cloud Build environment as a terminal. To hide the ANSI color codes, set `NO_COLOR` to `1`.

## Example

{% hint style="danger" %}
**Note**

This example is not production ready, and is intended to showcase configuration needed to get Earthly off the ground. If you run into any issues, or need help, [don't hesitate to reach out](https://github.com/earthly/earthly/issues/new)!
{% endhint %}

You can find our [`cloudbuild.yaml`](https://github.com/earthly/ci-example-project/blob/main/cloudbuild.yaml) and the [`Earthfile`](https://github.com/earthly/ci-example-project/blob/main/Earthfile) used on GitHub.

Start by adding a new [Trigger](https://console.cloud.google.com/cloud-build/triggers). Triggers are the things that link changes in your source code with new instances of builds in Cloud Build. Start by clicking on "Create Trigger".

![The triggers page for a project, with "Create Trigger" highlighted.](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-ec0f92b14914a703efed1e7f3383c887c9b45575%2Fgoogle-cloud-build-6.png?alt=media\&token=989f56b9-ae77-4e68-89ab-0d9cad32707e)

Fill out the "Name", "Description", and "Event" sections for this trigger, as they make sense for your project. For our example (and for ease of testing) we will be using the "Manual Invocation" trigger here.

![Creating a trigger for Google Cloud Build, specifying a name, description, and trigger event](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-b59bb46f4c7f82908fc52ad6208aa1e97f98b597%2Fgoogle-cloud-build-7.png?alt=media\&token=bbbf5210-03d0-4b1a-8675-a1dec4f627c3)

Configure your source repository. If you do not see your desired repository in the drop down list, follow [Google's instructions to add it](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo).

![Creating a trigger for Google Cloud Build, specifying a repository and branch name](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-26f3379d5ee5efd5bcb4de90527e90bbcd129d48%2Fgoogle-cloud-build-8.png?alt=media\&token=aa1c81be-c19d-4706-819b-e9d117334bc7)

Finally, fill in the "Configuration" section. For Earthly, you can only use the "Cloud Build configuration file", as Earthly itself will *also* be running containers. Our example will also be using an embedded [`cloudbuild.yaml`](https://github.com/earthly/ci-example-project/blob/main/cloudbuild.yaml).

![Creating a trigger for Google Cloud Build, specifying the configuration, including cloudbuild location and configuration type](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-f645f6e9dcd5fd8f663709fc4d65eb975cbbfd1d%2Fgoogle-cloud-build-9.png?alt=media\&token=a86862a9-7b3e-4e1b-9fee-fe7007c9dff2)

Click "Done" and you will be navigated back to the Triggers list view. To test the build, click "Run" since we chose a manual trigger only:

![Google Cloud Build Trigger list, with the manual run button highlighted](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-396675a7d42eb1e6976876efc21cc53b84299209%2Fgoogle-cloud-build-10.png?alt=media\&token=18e5269b-a46c-4c91-a884-03bae967faa0)

Running this build will use the [`cloudbuild.yaml`](https://github.com/earthly/ci-example-project/blob/main/cloudbuild.yaml) file in our sample repository. This file is also a key part of the build, so lets break this down as well.

[The first step](https://github.com/earthly/ci-example-project/blob/ea44992b020b52cb5a46920d5d11d4b8389ce19d/cloudbuild.yaml#L2-L6) simply uses the [all-in-one Earthly image](https://hub.docker.com/r/earthly/earthly) to do a simple build.

```yaml
  - id: 'build'
    name: 'earthly/earthly:v0.5.24'
    args:
      - --allow-privileged
      - +docker
```

[The second step](https://github.com/earthly/ci-example-project/blob/ea44992b020b52cb5a46920d5d11d4b8389ce19d/cloudbuild.yaml#L8-L13) runs a sample, Google Cloud Build only example to show how you would use an external service account to do things that normally requires credentials.

```yaml
  - id: 'gcp-test'
    name: 'earthly/earthly:v0.5.24'
    args:
      - +gcp-cloudbuild
    secretEnv:
      - 'EARTHLY_TOKEN'
```

The secret environment variable bootstraps the Earthly secret store, and we can load it from Google's Secret Store like this:

```yaml
availableSecrets:
  secretManager:
  - versionName: projects/earthly-jupyterlab/secrets/EARTHLY_TOKEN/versions/2
    env: 'EARTHLY_TOKEN'
```
