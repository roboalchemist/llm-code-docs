# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/bitbucket-pipelines.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/bitbucket-pipelines.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/bitbucket-pipelines.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/bitbucket-pipelines.md

# Adding analysis to Bitbucket pipeline

Once you have created your project in SonarQube, you can add the SonarQube analysis to your Bitbucket pipeline. To do so, you need to:

* Configure your project analysis parameters.
* Configure your `bitbucket-pipelines.yml` file.

{% hint style="info" %}
SonarScanners running in Bitbucket Pipelines can automatically detect branches or pull requests being built so you don’t need to specifically pass them as parameters to the scanner.
{% endhint %}

### Prerequisites

You should clone the full depth to make sure the scanner has access to all of your history when running analysis. For more information, see the documentation about[ Git clone behavior in Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/git-clone-behavior/).

### Configuring your project analysis parameters

For general information about the configuration of project analysis parameters, see [configuration-overview](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters/configuration-overview "mention").

You can set environment variables securely for all pipelines in Bitbucket Cloud’s settings. See[ User-defined variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/#User-defined-variables) for more information.

{% hint style="info" %}
You may need to commit your bitbucket-pipelines.yml before being able to set environment variables for pipelines.
{% endhint %}

You need to set the following environment variables in Bitbucket Cloud for analysis:

* `SONAR_TOKEN`: Generate a SonarQube token for Bitbucket Cloud and create a custom, secure environment variable in Bitbucket Cloud with `SONAR_TOKEN` as the **Name** and the token you generated as the **Value**.
* `SONAR_HOST_URL`: Create a custom environment variable with `SONAR_HOST_URL` as the **Name** and your SonarQube URL as the **Value**.

See [managing-tokens](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens "mention") for more information.

### Configuring your bitbucket-pipelines.yml file

This section shows you how to configure your `bitbucket-pipelines.yml` file. Bitbucket Pipelines can build specific branches and pull requests if you use the branches and pull-requests pipelines as shown in the example configurations below.

{% hint style="info" %}

* This setup assumes a typical gitflow workflow. See[ Use glob patterns on the Pipelines YAML file](https://support.atlassian.com/bitbucket-cloud/docs/use-glob-patterns-on-the-pipelines-yaml-file/) provided by Atlassian for more information on customizing which branches or pull requests trigger an analysis.
* For more information on configuring your build with Bitbucket Pipelines, see the[ Configure bitbucket-pipelines.yml](https://support.atlassian.com/bitbucket-cloud/docs/configure-bitbucket-pipelinesyml/) documentation provided by Atlassian.
  {% endhint %}

<details>

<summary>SonarScanner for Gradle</summary>

In SonarQube, after you select a project imported from Bitbucket, you’ll need to select an analysis method. Select **With Bitbucket Pipelines** and follow the in-product tutorial to create environment variables and configure your `bitbucket-pipelines.yml` for analysis.

{% hint style="info" %}
A project key might have to be provided through a `build.gradle` file, or through the command line parameter. For more information, see [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-gradle "mention").
{% endhint %}

</details>

<details>

<summary>SonarScanner for Maven</summary>

In SonarQube, after you select a project imported from Bitbucket, you’ll need to select an analysis method. Select **With Bitbucket Pipelines** and follow the in-product tutorial to create environment variables and configure your `bitbucket-pipelines.yml` for analysis.

{% hint style="info" %}
A project key might have to be provided through the command line parameter. For more information, see [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven "mention").
{% endhint %}

</details>

<details>

<summary>SonarScanner for .NET</summary>

In SonarQube, after you select a project imported from Bitbucket, you’ll need to select an analysis method. Select **With Bitbucket Pipelines** and follow the in-product tutorial to create environment variables and configure your `bitbucket-pipelines.yml` for analysis.

</details>

<details>

<summary>SonarScanner CLI</summary>

{% hint style="info" %}
The Advanced Configuration below is an alternative to the SonarQube Scan Bitbucket Pipe. If you do not need a setup that allows for scanner caching, we recommend using the Bitbucket Pipe configuration.
{% endhint %}

You can set up the SonarScanner CLI configuration the following ways:

* **SonarQube Scan Bitbucket Pipe**: Using the SonarQube Scan Bitbucket Pipe is an easy way to set up a basic configuration. You’ll find the Bitbucket Pipe and configuration instructions on the [SonarQube Scan Bitbucket Pipe](https://bitbucket.org/sonarsource/sonarqube-scan/) page.
* **Advanced Configuration**: If you need an advanced setup that allows for scanner caching, you can add the following to your `bitbucket-pipelines.yml` file:

```yaml
image: <image for build>

definitions:
  steps: &build-step
    - step:
        name: SonarQube analysis
        image: sonarsource/sonar-scanner-cli:latest
        caches:
          - sonar
        script:
          - sonar-scanner
  caches:
    sonar: /opt/sonar-scanner/.sonar

clone:
  depth: full

pipelines:
  branches:
    '{master,main,develop}':
      - step: *build-step

  pull-requests:
    '**':
      - step: *build-step
```

{% hint style="info" %}
A project key has to be provided through a `sonar-project.properties` file, or through the command line parameter. For more information, see [sonarscanner](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner "mention").
{% endhint %}

</details>

### Failing the pipeline job when the quality gate fails

You can use the [SonarQube quality gate check Bitbucket Pipe](https://bitbucket.org/sonarsource/sonarqube-quality-gate) to ensure your code meets your quality standards by failing your pipeline job when your quality gate fails.

If you do not want to use the SonarQube quality gate Check Pipe, you can instruct the scanner to wait for the SonarQube quality gate status at the end of the analysis. To enable this, pass the `-Dsonar.qualitygate.wait=true` parameter to the scanner in the `bitbucket-pipelines.yml` file.

This will make the analysis step poll SonarQube regularly until the quality gate is computed. This will increase your pipeline duration. Note that, if the quality gate is red, this will make the analysis step fail, even if the actual analysis itself is successful. We advise only using this parameter when necessary (for example, to block a deployment pipeline if the quality gate is red). It should not be used to report the quality gate status in a pull request.

You can set the `sonar.qualitygate.timeout` property to an amount of time (in seconds) that the scanner should wait for a report to be processed. The default is 300 seconds.

### If you use a monorepo <a href="#monorepo" id="monorepo"></a>

The monorepo feature is supported starting in the [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) provided the Bitbucket Cloud integration with SonarQube Server has been properly set up.

To add the SonarQube Server analysis to your Bitbucket pipeline:

1. If not already done, create the SonarQube Server projects related to your monorepo: see [monorepos](https://docs.sonarsource.com/sonarqube-server/project-administration/monorepos "mention").
2. For each project, set up integration features: see [project](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/project "mention").
3. For each project in the monorepo, configure the project analysis parameters. See [#configuring-the-project-analysis-parameters](#configuring-the-project-analysis-parameters "mention").
4. Configure the `bitbucket-pipelines.yml` file of your monorepo. You need to ensure that you specify the path to each project for analysis in your `bitbucket-pipelines.yml` file.

### Related pages

[global](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/global "mention")\
[import-repos](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/import-repos "mention")\
[project](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/project "mention")\\
