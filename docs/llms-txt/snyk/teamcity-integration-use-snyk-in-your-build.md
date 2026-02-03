# Source: https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/teamcity-jetbrains-integration-using-the-snyk-security-plugin/teamcity-integration-use-snyk-in-your-build.md

# TeamCity integration: use Snyk in your build

For any Project, you can add Snyk to your build to scan the code while you build and to fail the build for vulnerabilities, based on your configurations.

Snyk recommends running a build with the Snyk Security step before deployment, to ensure an excellent security posture.

For additional information about TeamCity and its features, refer to the [TeamCity documentation](https://www.jetbrains.com/help/teamcity/teamcity-documentation.html).

The following explains **how to configure your build with a Snyk step**.

* Add the Snyk step to a new or existing Project:
  * For new Projects, after configuring the Git repo from which to create the build, activate the auto-detect feature to automatically identify relevant steps for your Project build.
  * For existing Projects, navigate to **edit the project build steps**.\
    \
    When the Snyk step has been added, **Snyk Security** appears in the list of suggested steps, and the current test policy appears in the **Parameters Description** column:

![Snyk Security in the list of suggested build steps](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4e8d4914bb4cb99c7fa2bbc1623858e85fc1ab5c%2Fuuid-97395df2-f141-6f77-4551-f19397ac0781-en.png?alt=media\&token=38a23374-6afe-4f62-bd86-a4299b365459)

* Navigate to configure the Snyk Security step as follows:
  * Click anywhere on the **Snyk Security** row to open the configuration screen, or
  * For existing Projects, click **Add build step** to open the configuration screen.

![Configure Snyk security for TeamCity](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-db2956c5f43183b5cdb087f4dbb1c53fbafadeec%2Fuuid-88e38280-121e-a17b-cfd3-9fde89305b5c-en.png?alt=media\&token=42a399a0-ef00-453d-86e5-4ad7cc78d2e5)

* Configure the TeamCity fields (**Runner type**, **Step name**, and **Execute Step** (an advanced option)).
* Optionally, click **Show advanced options** to display additional fields and Snyk parameters:

![Additional Snyk parameters](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6853e0e225f1fddba200d07efa52568055c7e418%2Fuuid-8f294e8d-ca5e-123b-2992-a98c1e62fd6f-en.png?alt=media\&token=642d021b-c0ea-47b7-8b7e-b4c2cdeac752)

* Configure **Snyk Settings** and **Snyk Tool Settings**. For more information, see [TeamCity configuration parameters](https://docs.snyk.io/developer-tools/snyk-ci-cd-integrations/teamcity-jetbrains-integration-using-the-snyk-security-plugin/teamcity-configuration-parameters).
* When the configuration is complete, run the build. When the Snyk Security step ends successfully, you can navigate to the **Snyk Security Report** tab to view results within TeamCity and to navigate to the Snyk UI for further action:

![Snyk test report](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-2b8179e0afd3d4e86003ebf2e88a28781fb0042d%2Fuuid-e8b1fd6f-3b49-069c-c9fe-c0948931b141-en.png?alt=media\&token=809a46ad-06cb-42c5-b852-b0179a2d40c0)

* From the top of the report, click **View on Snyk.io** to view the snapshot and vulnerability information directly from the Snyk Web UI.
