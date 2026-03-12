# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/enable-a-repository-wiki-for-configuration.md

# Enable a Repository Wiki for Configuration

{% hint style="success" %}
**Supported platforms:** GitHub, GitLab, Bitbucket (Not supported on Bitbucket Data Center), Azure DevOps.
{% endhint %}

For the best experience with the Qodo Git interface, Qodo recommends enabling a wiki for each repository where it is installed.

### What is a wiki?

Set configurations by creating a page named `.pr_agent.toml` in the repository [wiki](https://github.com/Codium-ai/pr-agent/wiki/pr_agent.toml).\
This approach allows configuration changes without committing new content to the repository, simply edit the wiki page and save.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FyQm5E8I8IV77dTsyjCCz%2Fimage.png?alt=media&#x26;token=eb94a9ff-834a-4e7d-8482-146a51d4bd55" alt="" width="563"><figcaption></figcaption></figure>

### Benefits of creating a wiki

* Storing your Qodo Git interface configuration file.
* Tracking accepted code suggestions over time.
* Improve your Qodo experience over time by creating a `auto_best_practices.md` file to capture learning and best practices automatically.

### Enable a wiki&#x20;

### GitHub <a href="#github" id="github"></a>

1. Go to your repository’s **main page** on GitHub.
2. Click **Settings** in the top navigation bar.
3. Scroll to the **Features** section.
4. Check the box to **Enable Wikis**.
5. Return to the repository’s main page and click the new **Wiki** tab.
6. Click **Create the first page** and save it.

{% hint style="info" %}
The wiki must have at least one page to be fully active.
{% endhint %}

![](https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-298821614/https%3A%2F%2Fqodo.ai%2Fimages%2Fpr_agent%2Fpr_agent_accepted_suggestions_create_first_page.png)

### Azure DevOps

Azure DevOps Wikis are created at the **project level**, not per repository. Each repository is represented by a **wiki sub-page**.&#x20;

#### **Step 1: Create a Project Wiki**

1. Sign in to the Azure DevOps portal (for example: `https://dev.azure.com/<YOUR_ORGANIZATION>`).
2. Open your project and go to **Overview** → **Wiki**.
3. Click **Create Project Wiki**.
4. Set the page title to **`home`**, then **Save** and **Close**.
5. Refresh the page.

You should now see a **house icon** next to the `home` page.

#### **Step 2: Create repository sub-pages**

Create a **sub-page for each repository** where Qodo is installed.

1. Hover over the **three dots (⋮)** next to `home` and select **Add sub-page**.
2. Name the page **exactly as the repository name,** then **Save** and **Close**.

You can repeat this step to create **additional sub-pages** for other repositories in the project.

#### **Step 3: Add Qodo configuration and data files**

Under the repository sub-page, create wiki pages for Qodo configuration and related data files. To add files:

1. Hover over the repository sub-page.
2. Click the **three dots (⋮)**.
3. Select **Add sub-page**.
4. Add the required files as wiki pages.

Wiki page names **cannot start with a dot (`.`)**. Remove the leading dot when creating files (for example, `.pr_agent.toml` → `pr_agent.toml`).

### Writing wiki content <a href="#wiki-configuration-file-1" id="wiki-configuration-file-1"></a>

It is recommend surrounding the configuration content with triple-quotes ` ``` ` to allow better presentation when displayed as markdown. Qodo will remove the surrounding quotes when reading the configuration content.
