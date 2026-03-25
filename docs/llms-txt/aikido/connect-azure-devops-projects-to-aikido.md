# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-azure-devops-projects-to-aikido.md

# Connect Azure DevOps Projects

**Table of contents:**

* [Select Microsoft / Office 365 or Google to authenticate](#select-microsoft--office-365-or-google-to-authenticate)
* [Insert your organization's name](#insert-your-organizations-name)
* [Create a Personal Access Token](#create-a-personal-access-token)
* [Select the project and repos you'd like to secure](#select-the-project-and-repos-youd-like-to-secure)

## Connect Azure DevOps Projects to Aikido

Aikido allows you to connect your Azure DevOps projects to secure your code. To connect your Azure DevOps projects to Aikido, you will need to follow the steps below.

Note that each Azure Project with one or more repos will map to one Aikido workspace.

### Select Microsoft / Office 365 or Google to authenticate <a href="#select-microsoft--office-365-or-google-to-authenticate" id="select-microsoft--office-365-or-google-to-authenticate"></a>

**Step 1.** To connect your Azure DevOps project, you first need to authenticate via Microsoft / Office 365 or Google to create a user in Aikido. On the [signup screen](https://app.aikido.dev/login), click on 'Microsoft / Google' to continue.

> Depending on your organization's Microsoft Entra settings, you may need IT admin approval to authorize the Aikido application. [For more information about the approval process, check Azure docs.](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal)

**Step 2.** Once you are authenticated via Google/Microsoft, you can go ahead and select 'Connect Azure' on the page like below.

![Repository integration options: Connect with GitHub, Azure DevOps, GitLab, or Bitbucket.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0538cafa47734c6ab1098288262536d38e0f83be%2Fconnect-azure-devops-projects-to-aikido_8fece096-ffc3-4775-bd8d-52b44b022ee8.png?alt=media)

**Step 3.** Enter the details to connect the Azure Devops project of your choosing. We'll explain how to obtain the required information right below.

![Aikido onboarding: Enter Azure DevOps details to authenticate and connect your projects.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b90f85e72e89d499f3d58e420dd508b56c9156f7%2Fconnect-azure-devops-projects-to-aikido_3b1a2af6-64ef-4b33-b436-5e61e388e8dc.png?alt=media)

### Insert your organization's name <a href="#insert-your-organizations-name" id="insert-your-organizations-name"></a>

Enter the name of the Azure DevOps organization you'd like to connect. You can find this name by going to [https://dev.azure.com](https://dev.azure.com/) and copying it from the left-side navigation.

### Create a Personal Access Token <a href="#create-a-personal-access-token" id="create-a-personal-access-token"></a>

Next up, you need to create a Personal Access Token to give us access to the resources you want.

* Log in to your Azure DevOps account
* In the upper-right corner, click the user settings icon next to your avatar. It looks like this:

  ![User profile icon with a settings gear for account management options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1a7d3d50a15bc9f2a63c718d2fdb779dc55b3eca%2Fconnect-azure-devops-projects-to-aikido_8ac6922c-38e0-481b-a9e7-0be293fa315a.png?alt=media)
* Select **Personal Access Token** in the dropdown.
* Click on the **+New Token** button in the top left corner
* Enter a name for the token, eg: 'Aikido Security Access Token'
* Make sure to select the same organization as the one you entered in the previous step
* Make sure to select an expiration date in the future, the max should be 1 year.
* Next, we need the following scopes to be selected (click 'show all scopes'):
  * **Code: Read**
  * **Member Entitlement Management: Read**
  * **Project and Team: Read**
  * **User Profile: Read**
* Click the **Create** button at the bottom.

![Editing Azure DevOps personal access token with custom-defined code read permissions.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8f592ae4b0c29f78271e25fdd8fb18470239fb07%2Fconnect-azure-devops-projects-to-aikido_06457a8f-e8dd-47b3-a629-8cb8cff94338.png?alt=media)

* Copy the token being shown on the following screen and enter it in the input field .

**Important**: You will no longer be able to view the value of the token once you hit continue. Make sure you copied it first.

Aikido will now check the connection to your Azure DevOps organization. If the connection was not successful, make sure to double-check the organization name and personal access token you provided.

### Select the project and repos you'd like to secure <a href="#select-the-project-and-repos-youd-like-to-secure" id="select-the-project-and-repos-youd-like-to-secure"></a>

On the next screen, you can select which project you'd like to start with. You'll always be able to connect more of your projects to Aikido.

In the final step you can select all the repos you would like us to monitor.

#### Specific notes on TFVC Repos

Aikido supports the integration of both Git and Team Foundation Version Control (TFVC) repositories.&#x20;

* For TFVC repositories, Aikido **does not** perform secret scanning.
* By default, Aikido tries to scan 'All Branches' for TFVC repos. This might result in slow scanning speed. **It is recommended to select the actual branch to scan.** This can be changed by clicking the branch label on the repo detail page.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FP3dD3aHfu20Em6CrMhJi%2Fimage.png?alt=media&#x26;token=caf72359-e3c2-4e6e-9e1f-17314252f773" alt=""><figcaption></figcaption></figure>
