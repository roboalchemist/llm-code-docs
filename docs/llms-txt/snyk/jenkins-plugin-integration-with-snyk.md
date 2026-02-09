# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/jenkins-plugin-integration-with-snyk.md

# Jenkins plugin integration with Snyk

Snyk offers a native plugin for Jenkins that is based on the [Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli), to test and monitor Projects for vulnerabilities in your pipelines.

{% hint style="warning" %}
The Snyk Jenkins plugin supports Snyk Open Source. If you plan to include Snyk Code, Snyk Container, and Snyk IaC scans in your pipeline, use the generic [Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli).
{% endhint %}

For more information, [see the Snyk Jenkins Plugin repository](https://github.com/jenkinsci/snyk-security-scanner-plugin).

Follow the steps in each section of this document to use the Snyk Jenkins plugin:

1. [Install the Snyk Security Jenkins Plugin](#install-the-snyk-security-jenkins-plugin)
2. [Configure a Snyk installation](#configure-a-snyk-installation)
3. [Configure a Snyk API token credential](#configure-a-snyk-pat-or-api-token-credential)
4. [Add Snyk Security to your Project](#add-snyk-security-to-your-project)
5. [View your Snyk Security Report](#view-your-snyk-security-report)

## Install the Snyk Security Jenkins Plugin

* From your Jenkins dashboard, navigate to **Manage Jenkins**, **Plugins** > **Available plugins** tab.
* Search for **Snyk Security**.
* Install the plugin.

## Configure a Snyk installation

* Navigate to **Manage Jenkins** > **Tools**.
* Add a **Snyk Installation**.
* Configure the Installation.
* Remember the **Name** to use when configuring the build step.

### Automatic installation

The plugin can download the latest version of Snyk binaries and keep them up-to-date for you.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-7b288c31df4658ca2403564a92699cd34cd824e8%2Fsnyk_config_auto-update_v2.png?alt=media" alt=""><figcaption><p>Snyk Jenkins plugin automatic installation</p></figcaption></figure>

### Manual installation

* Download the following binaries. Choose the binary suitable for your agent's operating system:
  * [Snyk CLI](https://github.com/snyk/snyk/releases/latest)
  * [snyk-to-html](https://github.com/snyk/snyk-to-html/releases/latest)
* Place the binaries in a single directory on your agent.
  * Do not change the filename of the binaries.
  * Ensure you have the correct permissions to execute the binaries.
* Provide the absolute path to the directory under **Installation directory**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a33ce1b0630b0b9c6a340a5c0142814a4b440424%2Fsnyk_config_manual_v2.png?alt=media" alt=""><figcaption><p>Snyk Jenkins plugin manual installation</p></figcaption></figure>

### Custom API endpoints

If you are in a region other than `SNYK-US-01`, which uses the `https://api.snyk.io` endpoint, configure Snyk to use a different endpoint by changing the `SNYK_API` environment variable:

* Go to **Manage Jenkins** > **System**.
* Under **Global Properties**, check the **Environment** variables option.
* Click **Add**.
* Set the name to `SNYK_API` and the value to the custom endpoint.

For more information, see [Configure Snyk CLI to connect to Snyk API](https://docs.snyk.io/developer-tools/snyk-cli/configure-the-snyk-cli/configure-snyk-cli-to-connect-to-snyk-api).

## Configure a Snyk PAT or API token credential

* Get your [Snyk API Token or Snyk PAT](https://docs.snyk.io/snyk-api/authentication-for-api).
* Navigate to **Manage Jenkins** > **Credentials**.
* Choose a **Store**.
* Choose a **Domain**.
* Navigate to **Add Credentials**.
* Select **Snyk API Token**.
* Configure the Credentials.
* Remember the **ID** for use when configuring the build step.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ef916245e5d180541488823fe493b796ed8257c4%2Fsnyk_configuration_token_v2.png?alt=media" alt=""><figcaption><p>Configure Snyk API token for Jenkins plugin</p></figcaption></figure>

## Add Snyk Security to your Project

This step depends on whether you are using Freestyle Projects or Pipeline Projects.

### Freestyle Projects

* Select a Project.
* Navigate to **Configure**.
* Under **Build**, select **Add build step** and **Invoke Snyk Security Task**.
* Configure as needed. Click the **?** icons for more information about each option.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f15ea67199151b5a6d567321ea20d27e22f81ad7%2Fsnyk_buildstep_freestyle.png?alt=media" alt=""><figcaption><p>Configure for Freestyle Project</p></figcaption></figure>

### Pipeline Projects

Use the `snykSecurity` step as part of your pipeline script. You can use the **Snippet Generator** to generate the code from a web form and copy it into your pipeline. Refer to the following example.

```
pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        echo 'Building...'
      }
    }
    stage('Test') {
      steps {
        echo 'Testing...'
        snykSecurity(
          snykInstallation: '<Your Snyk Installation Name>',
          snykTokenId: '<Your Snyk API Token ID>',
          // place other parameters here
        )
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying...'
      }
    }
  }
}
```

You can pass the following parameters to your`snykSecurity` step.

**`snykInstallation`** (required)

Snyk Installation Name, as configured in [Configure a Snyk installation](#configure-a-snyk-installation).

**`snykTokenId`** (optional, default: `_none_`)

Snyk API Token Credential ID, as configured in [Configure a Snyk API token credential](#configure-a-snyk-pat-or-api-token-credential).

If you prefer to provide the Snyk API token another way, such as using alternative credential bindings, you must provide a `SNYK_TOKEN` build environment variable.

**`failOnIssues`** (optional, default: `true`)

Whether the step should fail if issues and vulnerabilities are found.

**`failOnError`** (optional, default: `true`)

Whether the step should fail if Snyk fails to scan the Project due to an error. Errors include scenarios like: failing to download the Snyk binaries, improper Jenkins setup, bad configuration, and server errors.

**`monitorProjectOnBuild`** (optional, default: `_none_`)

Whether to monitor the Project on every build by taking a snapshot of its current dependencies on snyk.io. Selecting this option keeps you notified about newly disclosed vulnerabilities and remediation options in the Project.

**`organisation`** (optional, default: `_automatic_`)

The Snyk `organization` in which this Project should be tested and monitored. See `--org` in the [CLI commands and options summary](https://docs.snyk.io/developer-tools/snyk-cli/cli-commands-and-options-summary) for the default behavior.

**`projectName`** (optional, default: `_automatic_`)

A custom name for the Snyk Project created for this Jenkins project on every build. See `--project-name` in the [CLI commands and options summary](https://docs.snyk.io/developer-tools/snyk-cli/cli-commands-and-options-summary) for default behavior.

**`targetFile`** (optional, default: `_automatic_`)

The path to the manifest file to be used by Snyk. See `--file` in the [CLI commands and options summary](https://docs.snyk.io/developer-tools/snyk-cli/cli-commands-and-options-summary) for default behavior

**`severity`** (optional, default: `_automatic_`)

The minimum severity to detect. Can be one of the following: `low`, `medium`, `high`, `critical`. See `--severity-threshold` in the [CLI commands and options summary](https://docs.snyk.io/developer-tools/snyk-cli/cli-commands-and-options-summary) for default behavior.

**`additionalArguments`** (optional, default: `_none_`)

See the [CLI commands and options summary](https://docs.snyk.io/developer-tools/snyk-cli/cli-commands-and-options-summary) for information on additional CLI options.

## View your Snyk Security Report

* Complete a new build of your Project.
* Navigate to the build page.
* Select **Snyk Security Report** in the sidebar to see the results.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-651e7fc0c6d44cdf22ef003006b330937032d148%2Fsnyk_build_report.png?alt=media" alt=""><figcaption><p>Snyk Security Report for Jenkins plugin</p></figcaption></figure>

If there are any errors, you may not see the report. Refer to the troubleshooting section that follows.

## Troubleshooting the Jenkins plugin

### Increase logging

To see more information on your steps, you can increase logging and re-run your steps.

* View the **Console Output** for a specific build.
* Add a logger to capture all `io.snyk.jenkins` logs. See [How do I create a logger in Jenkins for troubleshooting and diagnostic information?](https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/client-and-managed-masters/how-do-i-create-a-logger-in-jenkins-for-troubleshooting-and-diagnostic-information)
* Add `--debug` to **Additional Arguments** to capture all Snyk CLI logs. Debug output is available under **Console Output** for your build.

### Failed installations

By default, Snyk Installations download Snyk binaries over the network from `downloads.snyk.io` and use `static.snyk.io` as a fallback. If this fails, there may be a network or proxy issue. If you cannot fix the issue, you can do a manual installation instead. See [Configure a Snyk installation](#configure-a-snyk-installation).
