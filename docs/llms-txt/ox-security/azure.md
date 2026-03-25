# Source: https://docs.ox.security/get-started/onboarding-to-ox/source-control/azure.md

# Azure Repos

Azure Repos is a set of version control tools that you can use to manage your code. Azure Repos provides two types of version control:

1. Git: distributed version control.
2. Team Foundation Version Control (TFVC): centralized version control.

Azure Pipelines is a cloud-based solution that automatically builds and tests code projects.

Connecting your Azure account allows OX to map and scan your apps for security issues.

### Connection options

* **Identity Provider** - just click “Connect” under the “Identity Provider” tab and follow the instructions on the screen.
* **Token** - [Create an access token in Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=Windows) with the permissions mentioned below, copy the token into the token field and click “Connect”.

### Token scopes required

* Auditing - Read Audit Log
* Build - Read
* Code - Full
* Code - Status
* Graph - Read and Manage
* Identity - Read and Manage
* Member Entitlement Management - Read and Write
* Project and Team - Read, Write and Manage
* Release - Read
* Security - Manage
* User profile - Read
* Wiki - Read
* Work items - Read and Write

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4013c036920e65983326e62a8743799d26e55dde%2Fimage%20(9).png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3aa2bbe7e67e18579c33fe233292735f85e0e248%2Fimage%20(10).png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a41864dc3bd7ee84d61c371fb1a2038f7f1ebff1%2Fimage%20(11).png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3222c5ff39aaa3b55869ea18646248b4566fda46%2Fimage%20(12).png?alt=media" alt=""><figcaption></figcaption></figure>

Once you have verified Azure repos connectivity, you can see all the repositories and can select them for scanning.

### Setting repositories' scope

You can use the "Gear" icon to choose the repositories' scope OX will cover. Only repositories chosen here will be covered and scanned.

Here you can also decide what will happen by default with newly discovered repositories.
