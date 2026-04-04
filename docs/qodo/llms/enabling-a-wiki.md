# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/enabling-a-wiki.md

# Enabling a Wiki

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="success" %}
**Supported platforms:** GitHub, GitLab, Bitbucket (Not supported on Bitbucket Data Center), Azure DevOps.
{% endhint %}

For the best experience with Qodo Git interface, we recommend enabling a **wiki** for each repository where it is installed.

### What is a wiki?

Set configurations by creating a page called `.pr_agent.toml` in the [wiki](https://github.com/Codium-ai/pr-agent/wiki/pr_agent.toml) of the repo.

The advantage of this method is that it allows to set configurations without needing to commit new content to the repository: just edit the wiki page and **save**.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FrmDCvUWM2fwV6ScYTsz6%2Fimage.png?alt=media&#x26;token=81ee3053-4502-48fc-b9f3-bd82d59bbe10" alt="" width="563"><figcaption></figcaption></figure>

### Benefits of creating a Wiki

* Storing your [Qodo Git interface configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).
* Tracking [accepted code suggestions](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/improve) over time.
* Improve your Qodo experience over time by [creating a `auto_best_practices.md` file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/best-practices) to capture learning and best practices automatically.

### How to enable a wiki&#x20;

### GitHub

1. Go to your repository’s **main page** on GitHub.
2. Click **Settings** in the top navigation bar.
3. Scroll to the **Features** section.
4. Check the box to **Enable Wikis**.
5. Return to the repository’s main page and click the new **Wiki** tab.
6. Click **Create the first page** and save it.

{% hint style="warning" %}
**Important:** The wiki must have at least one page to be fully active.
{% endhint %}

**To initialize the wiki:** navigate to `Wiki`, select `Create the first page`, then click `Save page`.

<figure><img src="https://qodo.ai/images/pr_agent/pr_agent_accepted_suggestions_create_first_page.png" alt=""><figcaption></figcaption></figure>

### Azure DevOps <a href="#wiki-configuration-file" id="wiki-configuration-file"></a>

Azure DevOps Wikis are created at the **project level**, not per repository. Each repository is represented by a **wiki sub-page**.

#### Step 1: Create a Project Wiki

1. Sign in to the Azure DevOps portal\
   (for example: `https://dev.azure.com/<YOUR_ORGANIZATION>`).
2. Open your project and go to **Overview** → **Wiki**.
3. Click **Create Project Wiki**.
4. Set the page title to **`home`**, then **Save** and **Close**.
5. Refresh the page.

You should now see a **house icon** next to the `home` page.

#### Step 2: Create repository sub-pages

Create a **sub-page for each repository** where Qodo is installed.

1. Hover over the **three dots (⋮)** next to `home` and select **Add sub-page**.
2. Name the page **exactly as the repository name,** then **Save** and **Close**.

You can repeat this step to create **additional sub-pages** for other repositories in the project.

#### Step 3: Add Qodo configuration and data files

Under the repository sub-page, create wiki pages for Qodo configuration and related data files.

To add files:

1. Hover over the repository sub-page.
2. Click the **three dots (⋮)**.
3. Select **Add sub-page**.
4. Add the required files as wiki pages.

{% hint style="warning" %}
Wiki page names **cannot start with a dot (`.`)**.\
Remove the leading dot when creating files (for example, `.pr_agent.toml` → `pr_agent.toml`).
{% endhint %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FB6UR4kWTtgCzllI09e1F%2Fimage.png?alt=media&#x26;token=1a438aad-8385-4101-b4f6-336e1cc85df2" alt="" width="563"><figcaption></figcaption></figure>

### Writing wiki content <a href="#wiki-configuration-file" id="wiki-configuration-file"></a>

We recommend surrounding the configuration content with triple-quotes ` ``` ` to allow better presentation when displayed as markdown.

Qodo will remove the surrounding quotes when reading the configuration content.
