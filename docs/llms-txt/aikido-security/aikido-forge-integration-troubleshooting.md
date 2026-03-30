# Source: https://help.aikido.dev/miscellaneous-integrations/aikido-forge-integration-troubleshooting.md

# Forge Integration: Troubleshooting

**Table of contents:**

* [1. Missing permissions](#1-missing-permissions)
* [2. Repository not active in Aikido](#2-repository-not-active-in-aikido)
* [3. Setup for multiple Gits](#3-setup-for-multiple-gits)

## Aikido - Forge Integration: Troubleshooting

#### 1. Missing permissions <a href="#id-1-missing-permissions" id="id-1-missing-permissions"></a>

> A person has a user on aikido, but have not given permission to the current repository in the workspace

All permissions for Aikido can be managed inside your source code manager. This often can be found at App Permissions. A quick way to **grant permissions and activating repos** is through the Aikido UI

**Steps to give permissions and activate repos**

* Go to the [Repository Settings page](https://app.aikido.dev/settings/integrations/repositories)and click **Add Repo**. This will open up the respective source code manager
* Select repos you want to Aikido to have access to

  ![Repository access settings: choose all or specific repositories for permissions.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d94b4a3237bdb435d50388cc06e7a4b523f63169%2Faikido-forge-integration-troubleshooting_c60a1b0d-3f9c-41ff-b65c-c27c907979e4.png?alt=media)
* Select which repos Aikido should **activate** and scan

  > This is important so Aikido can scan for vulnerabilities and send information to Forge.

  ![Aikido interface for selecting repositories to scan for vulnerabilities.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c7af082dd2d1ecb9fe451d7de7d500d05c55c39c%2Faikido-forge-integration-troubleshooting_0231037c-bf20-4269-8702-88cca5d15856.png?alt=media)

#### 2. Repository not active in Aikido <a href="#id-2-repository-not-active-in-aikido" id="id-2-repository-not-active-in-aikido"></a>

> The repository has permission, but was not selected as one of the repos to scan.

It is possible that you have granted permission to Aikido to all repositories, but that only a few were selected for being nightly scanned. By default, Aikido disables these repositories for scanning.

**Steps to activate a single repository in Aikido**

* Go to the [Repository Settings page](https://app.aikido.dev/settings/integrations/repositories)
* Go to the repository that you want to activate and click the triple dots on the right. In the action menu, select 'Activate'.

  ![Dropdown menu showing "Configure" and "Activate" actions for a Javaspringvulny entry.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f6f17b27b5b24c1cdc3e51e4196423640ca66f55%2Faikido-forge-integration-troubleshooting_443198a2-31e5-4cd8-a788-2430d4fa5e4f.png?alt=media)

If you need to enable a big number of repos at once, you can click 'add repo' which will take you back through the [initial setup](https://app.aikido.dev/onboarding/github/connect-repositories) page. There you can multiselect which repos you would like to be scanned / activated.

![Select repositories to scan for vulnerabilities using Aikido's platform.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a0d1088a5c143bea548509a1d8fcb9b03f07bf73%2Faikido-forge-integration-troubleshooting_5fdc0e3b-3ab0-47d3-a86f-09beca7245f6.png?alt=media)

#### 3. Setup for multiple Gits <a href="#id-3-setup-for-multiple-gits" id="id-3-setup-for-multiple-gits"></a>

> A user has a workspace, but the repository is not in that workspace. This can be the case when a repository is another GitHub organisation.

Aikido supports [connecting multiple Gits](https://help.aikido.dev/getting-started/setting-up-your-account/account-setup-with-multiple-gits) (e.g., GitHub combined with Bitbucket) or different organisations within the same Git. If you want to connect a new GitHub organisation to an existing account, **you will need to create a new workspace.**

**Steps to setup a new workspace**

**Step 1:** Add a new workspace by clicking your profile icon in the top right corner.

![User profile dropdown with option to add another workspace highlighted.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9e8383f7e131fbf7800ee5466bc7341f327a810b%2Faikido-forge-integration-troubleshooting_8622f892-c25d-4192-9d4b-1718d6d954f5.png?alt=media)

**Step 2:** Continue by selecting "Add a New Workspace."

![Aikido dashboard: create new workspace or logout option available.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4b562977262ec5c2325165f5866d7d5917724830%2Faikido-forge-integration-troubleshooting_520e5e25-cbcf-4056-8b41-0a092ce3df96.png?alt=media)

**Step 3:** Switch between different Git accounts using the workspace switcher located in the top left corner.

![Dashboard showing GitHub organization selection and security vulnerability overview by severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9d0c46ff88832f76efae093d92e2fbc1ead03f3d%2Faikido-forge-integration-troubleshooting_7e3091ac-77d5-46b6-8712-4568446b068e.png?alt=media)
