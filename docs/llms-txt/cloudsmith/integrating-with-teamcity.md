# Source: https://help.cloudsmith.io/docs/integrating-with-teamcity.md

# TeamCity

How to integrate TeamCity with Cloudsmith

<Image align="center" src="https://files.readme.io/0c7b1154f877d1cd226998ae87bdc1d16ffa1b7995ef81e7737acb2d8a582b34-Integration_4.png" />

Integrating TeamCity with Cloudsmith enables seamless management of your software packages within your CI/CD pipelines. This integration allows you to push build artifacts directly to Cloudsmith repositories from TeamCity, leveraging TeamCity’s build pipelines for efficient artifact publishing.

<HTMLBlock>
  {`
  <div class="row cs-box-row">
    <div class="cs-box cs-box-66 cs-box-green">
      <div class="cs-box-title cs-box-title-green">No Code Uploading</div><p>
      The Cloudsmith CLI gives you full control when connecting to any CI/CD process; allowing you to upload any of our support formats or query your repositories. Just configure your API Key, install the CLI, and you'll be all set.</div>
    </div>
  </div>
  `}
</HTMLBlock>

## Prerequisites

Before proceeding, ensure you have the following:

1. **TeamCity Server**: A functioning installation of TeamCity.
2. **Cloudsmith Account**: An active Cloudsmith account with the necessary repository access.
3. **API Key**: A Cloudsmith API key for authentication, obtainable from your Cloudsmith account under Account > API Settings.
4. **Build Agent**: A configured build agent to execute TeamCity builds.

***

## Integration Steps

**Go to Project Build Configuration in TeamCity and add the following build steps:**

### Step 1: Install Python

* Runner Type: Command Line
* Custom Script:
  ```
  apt-get update -y
  apt-get install -y python3 python3-pip
  ```
* Execution Policy: If all previous steps finished successfully.

> 📘
>
> You can skip this step if the build agent is consistent as Python installation is a one-time setup

### Step 2: Install Cloudsmith CLI

* Runner Type: Command Line
* Custom Script:
  ```
  pip install cloudsmith-cli
  ```
* Execution Policy: If all previous steps finished successfully.

### Step 3: Add Cloudsmith API Key Parameter

1. Navigate to **Project Settings > Parameters**.
2. Add the following parameter:
   * **Name**: env.CLOUDSMITH\_API\_KEY
   * **Kind**: Environment variable(env.)
   * **Value Type**: Password (to ensure security).
   * **Value**: Your Cloudsmith API key.

<Image align="center" src="https://files.readme.io/a1a5eb0bcf41b906bfaa7b7b2cd01c0e6c69c361166d2b2d902e9c7b8f8332f8-Screenshot_2024-12-04_at_4.24.04_AM.png" />

### Step 4: Push Your Artifacts

* Runner Type: Command Line
* Custom Script:
  ```
  cloudsmith push raw &lt;owner&gt;/&lt;your-repository&gt; &lt;artifact-path&gt; 
  ```
* Replace **\<owner>/\<your-repository>** and **\<artifact-path>** with:
  * Replace **\<owner>** with your Cloudsmith Organisation name.
  * **Your Cloudsmith Repository Name**: For example, my-repository.
  * **Artifact Path**: Artifact path, such as ./example-artifact.tar.gz.
* Execution Policy: If all previous steps finished successfully.

***

## Enable Versioned Settings in TeamCity

> 📘
>
> Optional: If you want to track build configuration in your VCS.

1. In Project Settings, navigate to Versioned Settings.
2. Configure the following options:
   1. **Synchronization**: Enable.
   2. **Project settings VCS root**: Set as per your preference.
   3. **Settings format**: Choose either from Kotlin or XML.
   4. **Settings path in VCS**: .teamcity
   5. **Allow editing project settings via UI:** Enable.
   6. **Store passwords and API tokens outside of VCS**: Enable.
3. Apply the changes to ensure your build configuration is tracked in the version control system (VCS).
4. Allow it to complete and then hit Commit current project settings button and TeamCity will commit the build configuration to your VCS.

<Image align="center" src="https://files.readme.io/beb223f87a19a1722f8702c7a16bbd5174bfec7446b3c3e7efc22e7b5edd170e-Screenshot_2024-12-04_at_4.05.14_AM.png" />

**Here's a Kotlin Snip for You Reference**

```
import jetbrains.buildServer.configs.kotlin.*
import jetbrains.buildServer.configs.kotlin.buildFeatures.perfmon
import jetbrains.buildServer.configs.kotlin.buildSteps.script
import jetbrains.buildServer.configs.kotlin.triggers.vcs

version = "2024.03"

project {

    buildType(TestCloudsmith)
}

object TestCloudsmith : BuildType({
    name = "TestCloudsmith"

    artifactRules = "./"

    params {
        password("env.CLOUDSMITH_API_KEY", "credentialsJSON:4ad9ee86-2dd4-4acf-8070-123e96c647fc")
    }

    vcs {
        root(DslContext.settingsRoot)
    }

    steps {
        script {
            name = "InstallPython"
            id = "InstallCloudsmith"
            scriptContent = """
                apt-get update -y
                apt-get install -y python3 python3-pip
            """.trimIndent()
        }
        script {
            name = "InstallCloudsmith"
            id = "InstallCloudsmith"
            scriptContent = "pip3 install cloudsmith-cli"
        }
        script {
            name = "CheckCloudsmithAuth"
            id = "CheckCloudsmithAuth"
            scriptContent = "cloudsmith whoami"
        }
        script {
            name = "Cloudsmith Push"
            id = "Cloudsmith_Push"
            scriptContent = "cloudsmith push raw testenv/rawrepo raw-example.tar.gz"
        }
    }

    triggers {
        vcs {
        }
    }

    features {
        perfmon {
        }
    }
})

```

***

## Best Practices

* **Use Entitlement token Authentication**: If you only need to pull packages, use Entitlement tokens for authentication to avoid using long-lived API keys.
* **Secure Secrets**: Store sensitive information like API keys/Entitlement tokens as Passwords instead of any other Value type.

## Troubleshooting

* **Authentication Issues**: Verify the API key is correctly configured as a hidden parameter.
* **Artifact Upload Errors**: Ensure owner/your-repository and artifact-path are properly specified in the push command.
* **Build Failures**: Review the TeamCity build logs for errors in specific steps.