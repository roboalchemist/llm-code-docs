# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-current-iac.md

# Getting started with Snyk IaC

You can use Snyk IaC (Infrastructure as Code) in the Snyk Web UI to find, view, and fix issues in configuration files. You can also use Snyk IaC in the Snyk CLI. For details, see [Snyk CLI for Infrastructure as Code](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-iac).

On this page, you will find steps to find, view, and fix issues in configuration files for the supported environments: [Terraform](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-terraform-files), [AWS CloudFormation](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-cloudformation-files), [Kubernetes](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-kubernetes-configuration-files), including Helm, and [Azure Resource Manager (ARM)](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-arm-configuration-files). These steps are specific to the current IaC.

## **Prerequisites for Snyk IaC**

Before using Snyk IaC, be sure you have the prerequisites as follows:

* A Snyk account. For details, see [Getting started](https://docs.snyk.io/discover-snyk/getting-started).
* An existing Terraform, CloudFormation, Kubernetes, or ARM environment to work in.
* A Git repository you have integrated with Snyk in the same way as for other Snyk products. For details, see [Git repository (SCM)](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations).

For more information about IaC and supported environments, see the following pages:

* [Configure your integration to find security issues in your Terraform files](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-terraform-files/configure-your-integration-to-find-security-issues-in-your-terraform-files-current-iac)
* [Configure your integration to find security issues in your CloudFormation files](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-cloudformation-files/configure-your-integration-to-find-security-issues-in-your-cloudformation-files-current-iac)
* [Configure your integration to find security issues in your Kubernetes configuration files](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-kubernetes-configuration-files/configure-integration-to-find-security-issues-in-kubernetes-configuration-files-current-iac)

{% hint style="info" %}
You must use the Snyk CLI to scan ARM configuration files. See [Scan ARM configuration files](https://docs.snyk.io/scan-with-snyk/snyk-iac/scan-your-iac-source-code/scan-arm-configuration-files).
{% endhint %}

## Import IaC Projects

You will start by importing [Projects](https://docs.snyk.io/snyk-platform-administration/snyk-projects) you want to scan with Snyk. In these steps, you choose repositories for Snyk to test and re-test:

1. Log in to Snyk and on your dashboard, select **Projects** from the navigation.
2. On the Projects page, from the **Add projects** dropdown, select the SCM where the repositories and projects that you want to scan are; for example, select GitHub.
3. From the list of **Personal and Organization repositories**, select the Git repositories and projects you want to import for scanning.\
   You can select one or more repositories or projects in a repository.
4. Click **Add selected repositories** to import the selected SCM projects and repositories into Snyk.
5. Select **View import Log** to see the results on the import log.\
   You can scan multiple types of configuration files simultaneously.\
   The import completes and the Projects page displays the Snyk Project imported.

{% hint style="info" %}
After you have imported an IaC Project, Snyk re-tests your Project once a week by default. You can de-activate recurring tests on the **Settings** tab of the Projects page; Set **Test & Automated Pull Request Frequency** to **Test never**.
{% endhint %}

## View configuration file issues in IaC

On the Projects page, you can view the results for configuration files in the imported Projects.

* If **Group by targets** is selected, a list of [Targets](https://docs.snyk.io/snyk-platform-administration/snyk-projects#target) is displayed. These are the repositories with the Projects you imported. Select a Target to expand its list of Projects.
* If **Group by none** is selected: A list of all [Projects](https://docs.snyk.io/snyk-platform-administration/snyk-projects#project) is displayed.

In your **Projects** listing, select the Project to open to display detailed information about that Project.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d1ff4cdc0928eae669b565234d2b8eeaed904752%2Fsnyk-iac-getting-started-list-of-projects.png?alt=media&#x26;token=e1ab1705-67f0-4af5-9169-2eb949b33951" alt="A list of Snyk IaC Projects"><figcaption><p>List of Snyk Projects</p></figcaption></figure>

Each Project detail page has a snapshot showing when the Project was last tested, the name of the user who imported the Project, and, on the **Issues** tab, the number of critical, high, medium, and low-severity issues found and issue cards for each scanned configuration file. You can also select the **Overview**, **History,** and **Settings** options. Choose **History** to see previous snapshots of the Project.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3154f08ad2e6c3d67cab2711f6769d3412656264%2Fimage.png?alt=media" alt="Snyk Project issue card"><figcaption><p>Snyk Project issue card</p></figcaption></figure>

## Issue card details for Snyk IaC

Each issue card shows information about the resource and the path by which it was introduced.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6d7634e65b44e7b6a0cffcb1283a65418a8c9823%2FScreenshot%202022-05-23%20at%2014.24.14.png?alt=media" alt="Issue card details"><figcaption><p>Issue card details</p></figcaption></figure>

The information on the issue cards includes the following:

* The severity level, for example, **H** for high, and the name of the issue, for example, **Non-encrypted S3 Bucket**
* The **ID** of the security rule, for example, [SNYK-CC-TF-99](https://security.snyk.io/rules/cloud/SNYK-CC-TF-99).\
  Click the link to view more information on the [Snyk Security Rules](https://security.snyk.io/rules/cloud/).
* A snippet of your code showing the exact area that is vulnerable
* The exact path of the issue
* More details, such as:
  * brief description of the issue
  * impact of the issue
  * remediation advice to resolve the issue

Click **Full details** to see a preview of the full code:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1d3f434a816ec465316127091366ae3f53b299ab%2FScreenshot%202022-05-23%20at%2014.24.20.png?alt=media" alt="Preview of the full code"><figcaption><p>Preview of the full code</p></figcaption></figure>

Click **Ignore** to ignore this vulnerability. For details, see [Ignore Issues](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/ignore-issues).

## Fix configuration files in IaC

The steps to act on recommendations produced by Snyk IaC follow.

1. On a Project detail page, select an issue to see the details for that issue and specific recommendations from Snyk IaC.
2. Based on the recommendations, edit the configuration file to fix the issue identified and then commit the change.\
   Snyk automatically rescans the changed file.
3. View the change reflected in the issue display.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c6562cdb417d90f74dafb041c60c624a866db408%2Fsnyk-iac-getting-started-issue-card.png?alt=media&#x26;token=cdc01239-0f51-4c40-afee-24ccceaa359e" alt="Example of an IaC issues that has been fixed"><figcaption><p>Example of an IaC issues that has been fixed</p></figcaption></figure>

## Examples of IaC results

Examples follow of results displayed for current IaC.

### Terraform Cloud and Helm examples

Terraform Cloud and Helm do not show a code snippet, only the path details. There is no **Full details** button to show the preview of the full code.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8c8c118bda369dab4e72a688e50fc0def9acbd22%2Fimage%20(114)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(2).png?alt=media&#x26;token=e92d8cd1-8d14-493f-9ad0-2090969bf866" alt="Details for Helm"><figcaption><p>Details for Helm</p></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4ba16295b90dc286d6e2ec3c538533286b87d4f2%2Fimage%20(78).png?alt=media" alt="Details for Terraform Cloud"><figcaption><p>Details for Terraform Cloud</p></figcaption></figure>

### Example showing the code preview is not available

If Snyk can not identify the exact line of the vulnerable path in the file, Snyk does not show a code snippet, only a message and the path details. If possible, Snyk shows the **Full details** button so you can see a preview of the full code.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3d768e423a02295301dfe450d0146e4138cd5457%2FScreenshot%202022-05-23%20at%2014.28.07.png?alt=media" alt="Issue card without code snippet"><figcaption><p>Issue card without code snippet</p></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c954c6ac63ca25e90cc3a3f2cd52d9b5923b31c5%2FScreenshot%202022-05-23%20at%2014.28.17.png?alt=media" alt="Full code display"><figcaption><p>Full code display</p></figcaption></figure>
