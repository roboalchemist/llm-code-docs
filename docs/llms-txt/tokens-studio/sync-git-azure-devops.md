# Source: https://docs.tokens.studio/token-storage/remote/sync-git-azure-devops.md

# Azure DevOps - Git Sync Provider

## Azure DevOps sync setup guide

[Azure DevOps](https://azure.microsoft.com/en-us/services/devops/) is a Microsoft-owned suite of development tools and services you can use to create a Git-based source code repository.

You can use the Tokens Studio plugin native integration with Azure DevOps (ADO) to sync your Design Tokens to a repository of your choice.

We support two-way sync, meaning you can use the plugin to:

* **Push** JSON files of Design Tokens to ADO
* **Pull** the Tokens stored in ADO into any Figma file

This means the Design Tokens living in code are the source of truth for our design decisions, which can be shared between design and development teams.

This doc outlines how to set up an ADO repository and add it as a **Sync provider** in the plugin.

→Once set up, you can use the plugin's **Push** and **Pull** features to keep your Tokens in sync #add-doc-link/sync-push-pull

### How it works

* Set up a **project**, **repository** and **personal access token** in Azure DevOps
* Configure **Azure DevOps as a sync provider** within the Tokens Studio plugin.
* Use the plugin to **sync your Design Tokens** between Azure DevOps and Figma design files.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F0ULQPeeIlL2f3mJbuvpa%2Fsync-ado-header.png?alt=media&#x26;token=e8a19e80-bedf-40ef-bb70-b725f9e5f4ea" alt=""><figcaption></figcaption></figure>

***

### Azure DevOps setup instructions

If you haven't already, sign up for an Azure DevOps account at [Azure DevOps](https://www.atlassian.com/try/cloud/signup?bundle=jira-software\&edition=free\&skipBundles=true).

#### 1. Record your ADO Organization URL

Once you've logged in to your Azure DevOps (ADO) account, navigate to **the new project page**.

* Record your ADO **Organization URL**&#x20;
  * From the home page of ADO, copy the URL in your web browser window.
  * **Record the URL of** somewhere safe, as it's needed for the plugin configuration.

{% hint style="info" %}
Be sure to include the `https://` in your URL copy
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fg2ALJHNU7nunbuSiB15L%2Fsync-ADO-org-url-v2-0%201.png?alt=media&#x26;token=52997f60-4595-42a4-8531-4f36ca166c0a" alt=""><figcaption></figcaption></figure>

#### **2. Create your project and record its name**

**Create a new project** dedicated to storing and managing your Design Tokens.

* Choose a **descriptive name** for your project that is specific to its purpose and is memorable.
  * **Save the Project Name** somewhere safe, as it's needed for plugin configuration.
* Project description is optional
* Select if you want your project to be:
  * `Public` anyone can see it
  * `Private` needs permission to view
    * Your choice doesn't change the plugin's ability to sync with the repository
* Select **Create**

You are now looking at your new project. Well done!

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F9pVXE8tBMxG50Y77qjRz%2Fsync-ADO-New%20Project.png?alt=media&#x26;token=54bda31d-7c66-43e9-b01b-94d27fe567e3" alt=""><figcaption></figcaption></figure>

#### 3. Configure your repo

A repo is automatically created in your new project with the same name.

Now you'll need to add a `README` file to your repo as the plugin isn't able to sync to an empty repository.

* From the left side navigation, select the **Files** option (under **Repos**)
  * Scroll to the section called **Initialize main branch with a README or gitignore**.
  * Ensure `Add a README` is enabled.
  * Select **Initialize** to confirm

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F6GxTywREZPNCued1s7HT%2Fsync-ADO-Repo-ReadMe.png?alt=media&#x26;token=31d30144-912f-4eb3-96d1-c5e6b82dc91c" alt=""><figcaption></figcaption></figure>

#### 4. Record your repository name

Now you can navigate to your **Repo** using the left side navigation.

* You should see a **README** file has been added in the repository
* The repo was given a name that matches the project by default, you can change it to something else if you'd like.
* Save a copy of the **Repo name** as you need it to configure the plugin later.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FkIdf3gt6o3laYhjuForq%2Fsync-ADO-Repo-Finished.png?alt=media&#x26;token=b06c2b77-e19f-4ef0-97d8-1b0161139e9a" alt=""><figcaption></figcaption></figure>

#### 5. Generate a personal access token

Not to be confused with anything to do with Design *Tokens*, a p**ersonal access token** is a passcode from Azure DevOps you enter into the plugin that allows the connection to happen.

Navigate to your Azure DevOps **user settings**.

* Locate the **Personal Access Tokens section** and
* Select **new token**.
* Add a **Name** of what the token is for.
  * Example: `test-token repo sync to tokens studio`
* Select the **Organization** you recorded from above.
* Select an **Expiration** time frame
* Select the necessary **scopes** for this token to authorize:
  * `full access` or `custom defined`
    * is a choice made by you and your team
* Scroll down to the bottom and select **Create token**
* **Save the generated access token** somewhere safe as it's needed for the plugin configuration.

You're ready to configure the Tokens Studio plugin in Figma!

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FCCrksmnwMnDhJpGAldHa%2Fsync-ADO-PAT.png?alt=media&#x26;token=322792d9-991b-4469-a592-8233caebb850" alt=""><figcaption></figcaption></figure>

***

### Plugin settings for Azure DevOps

In Figma, open the Tokens Studio plugin and navigate to the **Settings** page.

* Under the **Sync Providers** section, select the **Add New** button to see a list of all Token storage providers
* add **Azure DevOps** as a sync provider.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FENVNuB3dE7c0LqlJNxgW%2Fsettings-page-ADO-v2-0.png?alt=media&#x26;token=97302440-bdb6-442c-b595-8655d056b3be" alt=""><figcaption></figcaption></figure>

#### Add credentials for Azure DevOps

Some of the inputs on the form come from the Azure DevOps steps above, others aren't so obvious as to where the info comes from.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FPduPyG3LBETiAGrcCirV%2Fsync-ADO-annotated-v2-0.png?alt=media&#x26;token=11cc4c34-5cc0-436a-8a9f-f464832d9740" alt=""><figcaption></figcaption></figure>

#### **1. Organization URL**

The **URL** of your Azure DevOps organization you saved in [step 1 above](#id-1.-creating-a-new-project).

Example `https://dev.azure.com/my_organization_name`

#### **2. Project Name**

The **Project name** you saved from the [step 2 above.](#id-2.-create-your-project-and-record-its-name)

* Each ADO project could have many repositories, and you could have the same named repository in many ADO projects, so this credential helps the plugin point the Tokens to the correct location.
* Example: `TokensTesting`

#### **3. Personal Access Token**

The **Personal access token** you saved from the [step 5 above](#id-3.-generate-a-personal-access-token).

#### **4. Repository name**

The **name of the repository** you recorded in [step 4 above](#id-4.-record-your-repository-name) that matches the **personal access token** you entered

Example: `test-tokens`

#### **5. Branch**

Your engineers might tell you what to add as the **default repository branch** where you will be pushing your Tokens, so if you aren't sure, ask them. You can create additional branches using the plugin later as needed.&#x20;

Example: `main`

#### **6. Token storage location (file/folder path)**

This tells the plugin:

* How to organize your Token JSON files in ADO.
  * In a folder of multiple files, or a single file.
* The location of where your Token data is stored.
  * The file or folder's pathway (or name) to sync with.

This setting impacts

* How engineers can work with our Token files during the Token transformation stage of the design-to-development process.
* May limit edit access of Tokens for other team members using the Tokens Studio plugin.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FNDbiHgWg5srZtswOkSsR%2Fsync-ADO-file-folder-both-v2-0.png?alt=media&#x26;token=76dafa1f-e07d-4808-8546-5c76d54e4837" alt=""><figcaption></figcaption></figure>

**Folder**

The folder option syncs Token data from the plugin into a folder that contains multiple JSON files or subfolders of JSON files.

> The **Multi-file sync to remote storage** feature requires a [Pro Licence](https://tokens.studio/pricing) for Tokens Studio. Read the guide for more details.&#x20;

{% content-ref url="../remote-multi-file-sync" %}
[remote-multi-file-sync](https://docs.tokens.studio/token-storage/remote-multi-file-sync)
{% endcontent-ref %}

{% hint style="info" %}
**We suggest setting your Token storage as the folder option when possible.** \
\
If you use the **Themes** feature in Tokens Studio and your engineers are consuming your Tokens from your Git provider, they require Tokens stored in a folder for the transformation process to work properly.
{% endhint %}

In the plugin, enter the pathway of the folder where you want the Token data to be stored, which is the **folder name** without any extensions.

For example:

```
tokens
```

Our Gitlab repository will have a folder called `tokens` synced to the Tokens Studio plugin in Figma.

* Each **Token Set** created in the plugin is added to the folder as an individual JSON file.
* Additional data files generated by the plugin are also added to the folder.
  * For example, `themes` configuration.

Recall that storing your Token data in a folder (multi-file sync) is a pro feature.

* If other team members are working with your Tokens and do not have a Pro Licence for Tokens Studio, your Tokens will be **read-only** for them.

**File Path**

Setting our Token storage as the **file** option syncs our Token data from the plugin into a single JSON file in code.

Combining Token data into a single file limits engineers' ability to work with **Theme** information when transforming Design Tokens.

→ Learn about the Themes (pro) feature in Tokens Studio here. #add-doc-link/themes-pro

**File** storage might work for you if:

* You are using the free version of Tokens Studio.
* Engineers are not using your Design Tokens in code.

In the plugin, we enter the pathway of the JSON file where we want our Token sets to be stored, which is the **file name** with the `.json` extension.

For example:

```
tokens.json
```

Our Gitlab repository will have a single code file called `tokens.json` synced to the Tokens Studio plugin in Figma.

* Each **Token Set** created in the plugin is combined into this single file in our repository.

#### Save and do the initial sync

Once you **Save** your credentials, the plugin will compare your Tokens with what's in your repository.

You'll see a modal asking you to **push** or **pull** to ADO to 'sync' the plugin data with your repository.

→ Read the Add New Sync Provider guide for more details.

{% content-ref url="../manage-sync-provider" %}
[manage-sync-provider](https://docs.tokens.studio/token-storage/manage-sync-provider)
{% endcontent-ref %}

***

### Shared source of truth

As you work in the plugin, push and pull indicators remind you to stay in sync with your Azure DevOps repository.

Read the Sync Changes guide for more details

{% content-ref url="../remote-push-pull-changes" %}
[remote-push-pull-changes](https://docs.tokens.studio/token-storage/remote-push-pull-changes)
{% endcontent-ref %}

Once your Token JSON files are synced to your ADO repo, you have a shared source of truth between Designers and Engineers!

The various Token Types supported by Tokens Studio have unique transforms to be aware of.

{% content-ref url="../../manage-tokens/token-types" %}
[token-types](https://docs.tokens.studio/manage-tokens/token-types)
{% endcontent-ref %}

***

### Resources

Mentioned in this doc:

* Azure Dev Ops - <https://azure.microsoft.com/en-us/products/devops/>
* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary - <https://styledictionary.com/>

Community resources:

* None yet!

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Sync ADO](https://github.com/tokens-studio/figma-plugin/labels/sync%20azure%20devops%20ado)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* 🧑‍💻 [Sync to external token storage enhancements - Feature Request](https://tokensstudio.featurebase.app/p/sync-external-storage-enhancements)
  * How might we improve the experience of working with sync providers in general?
* ↕️ [Git sync enhancements - push, pull, merge, branching - Feature Request](https://feedback.tokens.studio/p/git-sync-enhancements)
* 🔐 [Data security info request - Feature Request](https://feedback.tokens.studio/p/data-security-info)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
