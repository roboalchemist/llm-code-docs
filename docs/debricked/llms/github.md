# Source: https://docs.debricked.com/tools-and-integrations/integrations/github.md

# GitHub

With CI integration to GitHub, you can automatically upload your latest commits and pull requests to OpenText Core SCA.&#x20;

There are currently two ways of integrating your projects with OpenText Core SCA:

* GitHub Actions
* GitHub App&#x20;

### **GitHub actions**  <a href="#githubactions" id="githubactions"></a>

#### **Configure** OpenText Core SCA **token** <a href="#configuredebrickedtoken" id="configuredebrickedtoken"></a>

Start by [generating an access token](https://docs.debricked.com/product/administration/generate-access-token). Copy the token so that you can use it in the next step.

You can add your access token as a secret, called *DEBRICKED\_TOKEN*, under *Settings* → *Secrets and variables* → *Actions* in your repository.

#### **Integrate a single repository** <a href="#integrateasinglerepository" id="integrateasinglerepository"></a>

You can scan your repositories as part of your CI pipeline by using the GitHub action: [ https://github.com/debricked/actions](https://github.com/debricked/actions).

Depending on what package manager you are using there are different job setups.

In order for us to analyze all dependencies in your project, their versions, and relations, files containing the resolved dependency trees have to be created prior to scanning. Those depend on the package manager used. OpenText Core SCA tries to generate the lacking files, which can negatively affect speed and accuracy.

**Example 1:** If [npm](https://www.npmjs.com/) is used in your project you will have a package.json file, but in order for us to scan all your dependencies, OpenText Core SCA requires either package-lock.json or yarn.lock as well.

**Example 2:** If [Maven](https://maven.apache.org/) is used in your project, you will have a pom.xml file, but in order for us to resolve all your dependencies, OpenText Core SCA requires a second file, as Maven does not offer a lock file system. Instead, "Maven dependency:tree" plugin can be used to create a file called "*.debricked-maven-dependencies.tgf".*

1. Create a ".*github/workflows/debricked.yml"* file and put in the contents of the [**template**](https://github.com/debricked/cli/tree/main/examples/templates/GitHub)**.**
2. Commit your changes to "*.github/workflows/debricked.yml"* and watch the pipeline run.

#### **Integrate multiple repositories** <a href="#integratemultiple-repositories" id="integratemultiple-repositories"></a>

Integrating many repositories with one workflow using GitHub can greatly simplify the process of managing and deploying code across multiple projects. You can set this up with required workflows set up in an organization ruleset, which triggers for every pull request and blocks the merge if the pipeline fails.

Considerations:

* Organization Rulesets are only available with GitHub Enterprise.
* GitHub Actions must be enabled for a repository in the organization's settings in order for required workflows to run.
* Ruleset workflows only work with the `pull_request` or `merge_group` events.
* Ruleset workflows and workflows from a specific repository are not mutually exclusive. If you use a required workflow and configure GitHub Actions for a specific repository, they will both run.

#### **Step 1: Create an organization secret**

To avoid having to add the `DEBRICKED_TOKEN` to every integrated repository, it is possible to share the OpenText Core SCA token between repositories in your organisation. In order to enable this, you need to create an organization secret:&#x20;

1. [Generate a OpenText Core SCA access token](https://docs.debricked.com/product/administration/generate-access-token).
2. Go to organization **Settings** → **Secrets and variables** → **Actions**.
3. Click **New organization secret**.
4. Add the generated token to a variable called `DEBRICKED_TOKEN.`

#### **Step 2: Create repository for the shared workflow**

Set up a repository within your workspace for the shared workflow:

1. Create a new repository in your workspace or enter an already existing one.
2. Create a workflow *yaml* file and paste the OpenText Core SCA workflow template contents as below:

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/GitHub/debricked.yml>" %}

3. Change line 3 from `on: [push]` to `on: [pull_request]` for it to be able to run as a required workflow.

#### **Step 3: Configure ruleset**

1. Visit the settings page of your organization by clicking your avatar in the top right of the GitHub UI, select **Your organizations** and then the **Settings** button for the organization.
2. Under *Code, planning, and automation* go to **Repository**→ **Repository Rulesets**.
3. Click **New branch ruleset** or select an already existing ruleset.
4. In **Enforcement status** drop-down, select either **Active** if you want to enforce the rules from the start or **Evaluate** if you want to test it first.
5. In **Target repositories** section, select which repositories and branches the ruleset should be enforced for. It is recommended to start with either the default branches or including by pattern. If not, you have to set up bypassing roles or teams, to avoid situations where all branch actions in the repository get blocked.
6. in **Branch protections** tick **Require workflows to pass before merging**.
7. Click the **Add workflow**.
8. Select imported repository and branch from the dropdown lists and workflow from that repository in the modal window.

After these steps, the workflow should be executed for pull request events in the selected repositories and branches.

### Enable Pull Requests for GitHub action integrations

Although Pull Requests are not natively supported for GitHub actions, it is possible to use GitHub app integration along with GitHub actions to enable Pull Requests.

{% hint style="info" %}
See the below section to more information on setting up GitHub app integration.
{% endhint %}

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FOnDmu7ILpgu8MYIdfKhF%2Fimage.png?alt=media&#x26;token=0b93442d-0d0a-4e4d-a6cf-45d411e5f405" alt=""><figcaption></figcaption></figure>

The scanning method depends on the 'GitHub App Scanning' setting. As shown in the above screen, when 'GitHub App scanning' is disabled, GitHub actions integration is used for scanning. When enabled, GitHub app integration is used for scanning. To enable Pull Requests for GitHub actions, set up the GitHub application and then disable it.

### GitHub application  <a href="#githubapp" id="githubapp"></a>

#### **Installation** <a href="#installation" id="installation"></a>

1. Start by heading over to <https://github.com/apps/debricked/>.
2. Click **install** on the top right corner.&#x20;
3. Choose your personal account or your organization’s account.
4. If you have not entered your password in a while, you might have to re-enter your personal account password.
5. Install directly or request access to install:

* If installing to a personal account or an organization account where you are an admin, you will be able to select the repositories to install the integration.

  &#x20;
* &#x20;If you do not have the admin permissions, you will still be able to select which repositories to install the integration, but an organization admin should approve your installation request.

6. If the installation is successful, you or your organisation admin will be redirected to OpenText Core SCA’s service settings, where pop-up will be shown letting you trigger a first-time scan of your repositories.\
   &#x20;

Repositories not selected during the first scan will not be scanned initially. However, new commits to a repository will trigger a scan.

#### **Permissions**

The GitHub app requires certain permissions in order for OpenText Core SCA service to work:

* Read access to [metadata ](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#metadata-permissions)- This is a default permission to all GitHub apps and does not leak any sensitive information.
* Read and write access to [checks](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#permission-on-checks) - Checks are also known as actions, which are created and updated in order to inform users about the scan progress. It is also used for posting results and trigger events for the GitHub App.
* Read access to code - This is used in order for us to scan the dependency files. **Note that OpenText Core SCA only reads dependency files, not the source code.**
* Write access to code - This is required to create pull-requests with fixes for the dependency files.
* Read and write access to [pull-requests](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#permission-on-pull-requests) - This is also necessary for creating pull-requests.
* Read and write access to [issues](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps?apiVersion=2022-11-28#permission-on-issues) - This is for future capabilities of issue integration between OpenText Core SCA and GitHub.

#### **Configuration** <a href="#configuration" id="configuration"></a>

If you selected specific repositories upon installation, and would like to add more repos to be scanned:

1. Click **Repositories** on the left side menu.
2. Click **New**.
3. Select **Repository**.
4. Follow the link to grant access to more repositories.

The added repos will only show in the UI once a scan is started by either:

* Starting a scan manually, by going to **New** -> **Repository**
* Pushing a commit, which will start the scan automatically

You can also go directly into your GitHub account and edit the app configuration.

**Enable or disable application scanning**

If you want to enable/disable scanning repositories via the GitHub App:

1. Go to **Repository Settings**.
2. Toggle the **GitHub App scanning** switch to **off**.

Disabling GitHub App scanning allows you to scan your repositories using a CI integration instead, while still keeping the app for opening Fix Pull Requests to the repository.

**Configuring integration**

It is possible to configure the GitHub integration by adding a *.debricked.yaml* file to the root of your repository, such as excluding directories and skipping adding the scan output to GitHub.&#x20;

It can take up to an hour before the configuration changes take effect. OpenText Core SCA *GitHub actions* alternative does not have this limitation.

**Enabling slow scan**

In cases where you get the “Your repository seems to be too large” error, you may want to enable *slow scan* to make the scan pass. To do so:

1. Create or edit the .*debricked.yaml* in the root of your repository.
2. Set *slow\_scan* to true:

```bash
slow_scan: true
```

3. Commit the changes.

**Excluding directories**

Another solution to resolve the “Your repository seems to be too large” error is to exclude some directories in order to make the scan pass. To do so:

1. Create or edit the *.debricked.yaml* in the root of your repository.
2. Put the directories you want to exclude in the file:

```bash
excluded_directories: ['large-directory', 'important-directory/unwanted-directory', 'another-directory']
```

3. Commit the changes.\
   &#x20;

**Enable skip scan**

In order to prevent your pipeline from breaking due to vulnerabilities (or if you have a very complex project where the scan time is too long for your needs) you may want to enable the skip scan. This means that OpenText Core SCA still scan your repositories, but the pipeline won't wait for the results. To skip adding scan output to GitHub:

1. Create or edit the *.debricked.yaml* in the root of your repository.
2. Set *skip\_scan* to true as below:

```bash
skip_scan: true
```

3. Commit the changes.

#### **Uninstallation** <a href="#uninstallation" id="uninstallation"></a>

If there is a problem during installation of the app, follow these steps to uninstall the app:

1. In GitHub, go to your **GitHub user settings**.
2. If the app was installed on an organizational account, switch to that account.

To re-install the app, follow the installation guide or set up GitHub actions.

If you are uninstalling the app due to unmet expectations or other issues, let us know at <support@debricked.com>.
