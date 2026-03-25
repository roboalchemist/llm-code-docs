# Source: https://help.aikido.dev/code-scanning/miscellaneous/split-your-monorepo-per-path.md

# Split Your Monorepo Per Path

{% hint style="warning" %}
If you are looking for a clearer overview within Aikido by dividing large repositories into smaller, more manageable parts, we recommend using [this alternative](https://help.aikido.dev/getting-started/manage-teams-and-applications/assign-team-responsibilities-by-specific-path-in-repo).
{% endhint %}

{% hint style="info" %}
This functionality is **only** available for GitLab (Cloud/On-Prem) and Azure DevOps (Git/TFVC).&#x20;
{% endhint %}

{% hint style="info" %}
For **TFVC repos**, make sure to first set the specific branch you want to scan on the repo page (the default is 'All Branches')
{% endhint %}

Aikido allows you to split up your large repositories / monorepositories per path, improving the overall management of your security issues.

## Use Case <a href="#use-cases" id="use-cases"></a>

* Giant repos often take a lot of time to scan or can time out. This can improve scanning speed.&#x20;
* **Not:** If you are looking for a clearer overview within Aikido by dividing large repositories into smaller, more manageable parts. In this case, we recommend using [this alternative](https://help.aikido.dev/getting-started/manage-teams-and-applications/assign-team-responsibilities-by-specific-path-in-repo).

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* Only available for **Pro Plans**. Contact Aikido in order to enable this functionality.
* You are using **GitLab** or **Azure DevOps**.
* Supports **SCA, SAST,** and **IaC** scans only. Secret scanning is not available for split repositories.

## How to split up your repositories <a href="#how-to-split-up-your-repositories" id="how-to-split-up-your-repositories"></a>

**Step 1:** Go to the repository detail page and add `/split` to the end of its URL in the browser's address bar (e.g., `https://app.aikido.dev/repositories/330080/split`*).* This will direct you to the page allowing you to split your repository.

![Interface for defining split points to divide a repository into subdirectories.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b4b84c69949417a9b94a067543984f856adceb89%2Fsplit-your-monorepo-per-path_1acc303c-9047-47c6-90a4-8997e18de9e1.png?alt=media)

**Step 2:** Enter the split points. These are the paths within your repository that you wish to separate. Input all the paths you want to see as individual entities.\
​\
​

![Repository split points defined as: bad\_sast\_findings, secrets, and autofix.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-898f2b7fbe7d50317b1c9d5234ace7d5d33f1f1d%2Fsplit-your-monorepo-per-path_7eb2ed38-070e-4182-9875-dfbb27d99557.png?alt=media)

**Step 3:** Select ***Split repo***. This action deactivates the original repository configuration and divides it into smaller repositories for scanning. You can view all these in the [**repository overview**](https://app.aikido.dev/repositories). All specified paths will be shown with a **tag** next to the original repo name.

![Repository dashboard displaying security scan results and severity for three active repositories.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1e185b4ead3115814180ab2cc169c7b8607ecb10%2Fsplit-your-monorepo-per-path_da0abeab-31ee-4f9c-ba0b-937d6dd8622e.png?alt=media)

**Step 4.** Assign different subpaths to different teams. More information on how to set up teams and assign responsibilities can be found [here](https://help.aikido.dev/en/articles/9005606-using-teams-for-repository-and-user-management).

> Notes: You can add new paths at a later stage. You can do this by going again to the base repo from where it was split. Do not add the already existing paths, new ones are sufficient.

***
