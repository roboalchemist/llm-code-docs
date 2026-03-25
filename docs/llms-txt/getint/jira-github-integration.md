# Source: https://docs.getint.io/guides/integration-synchronization/jira-github-integration.md

# Jira GitHub integration

Integrating Jira with GitHub using Getint connects your project tracking and code management through two-way synchronization. Whether you’re logging issues in Jira or handling code in GitHub, this setup keeps both teams aligned and informed.

This step-by-step guide shows you how to configure the integration using Personal Access Tokens for authentication.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FSYEVjXgxno7iiLBoXU2c%2FGitHub%20Integration%20for%20Jira.png?alt=media&#x26;token=c3dc8b64-9e26-486f-8002-38268c43a32b" alt=""><figcaption><p><a href="https://marketplace.atlassian.com/apps/1223933/github-integration-for-jira-github-connector?hosting=cloud&#x26;tab=overview">Check out our GitHub integration app on the Atlassian Marketplace</a></p></figcaption></figure>

***

### GitHub-Jira Licensing Model <a href="#github-jira-licensing-model" id="github-jira-licensing-model"></a>

The GitHub-Jira licensing model with Getint is designed to accommodate different integration needs. Here’s an overview:

#### Standard Licensing <a href="#standard-licensing" id="standard-licensing"></a>

* A Getint license is only required on Jira, allowing seamless data synchronization between GitHub and Jira.

  This makes setup simpler and faster, without the need for additional configurations in GitHub.

#### Flexible License <a href="#flexible-license" id="flexible-license"></a>

* For managed services companies or organizations looking to integrate four or more instances (regardless of whether they are the same or different tools), Getint offers a **Flexible License.** This custom license covers a specific number of connections (i.e., up to 10 instances) without restrictions on the tools involved. You can also swap the integrated tools while the license remains active, offering unparalleled flexibility.

For more details on licensing, visit our [**Pricing Page**](https://docs.getint.io/billing-and-services/licensing).

#### Requirements to Build Your Integration: <a href="#requirements-to-build-your-integration" id="requirements-to-build-your-integration"></a>

* The **Getint app** must be installed in Jira.
* Comments are attributed to the user who created the connection. Therefore, we recommend using dedicated Service Accounts for both instances.
* Jira instances must have a dedicated user and an associated API token with permissions to read, write, view, and modify the project.
* **Personal Access Tokens** are required for Jira and GitHub authentication. You can find the steps to generate the access token for your connectors here: [Connection Guide](https://docs.getint.io/guides/quickstart/connection#github).

### Setting Up Your GitHub-Jira Integration <a href="#setting-up-your-github-jira-integration" id="setting-up-your-github-jira-integration"></a>

**1. Access the Getint App in Jira**

* Navigate to **Apps** and select **Jira - GitHub Integration**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FKtiTHpWuah3KFrxNxcqv%2FJira%20GitHub%20app.png?alt=media&#x26;token=b16944e5-5dc1-48aa-bfb8-2267322bd683" alt=""><figcaption></figcaption></figure>

**2. Create Integration**

* Click **Create integration** or **Migration**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTKrsyipUrJ5JuTpaDYSL%2FChoosing%20Continuos%20sync%20or%20Migration.png?alt=media&#x26;token=76875dc4-c6e6-4855-9718-1ce6ff853122" alt=""><figcaption></figcaption></figure>

**3. Token Generation (Password for Jira Cloud)**

* For Jira Cloud, generate a Jira token. This token will act as your password:
  * Go to Atlassian Account Settings.
  * Navigate to Security and generate an API token, then use this token as the password for Jira integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FeRhhFwwP7bFhYfywv20q%2FToken%20Generation%20for%20GitHub.png?alt=media&#x26;token=c2f93a38-19f7-4118-86cd-46ef5f5cd20d" alt=""><figcaption></figcaption></figure>

**4. Generate a GitHub Personal Access Token**

* Log in to your GitHub account.
* Select your Avatar in the top right corner. Navigate to Settings > Developer Settings > Personal access tokens.
* Generate a new Token (Classic) or Fine-grained token.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FcZI6Kl1yE9gGhWGjUlUQ%2FGitHub%20Personal%20Access%20Token.png?alt=media&#x26;token=c9908b7d-8019-4bcb-8725-77abf6e5da9e" alt=""><figcaption></figcaption></figure>

* Provide a name for your token, select the expiration date, and set the required scopes (permissions). For a detailed description of how to create the token, please follow this [guide](https://docs.getint.io/guides/quickstart/connection#github).
* Click **Generate Token** and make sure to securely store your token, as it will only be visible once.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FvjqQ1HxHe8NlMCtPpUc5%2FGenerate%20token%20button.png?alt=media&#x26;token=032f4686-7770-48fe-afff-da4182f051cc" alt=""><figcaption></figcaption></figure>

**5. Connect to Jira**

* In Getint, enter your Jira instance URL, username, and the API token.
* Use the Personal Access Token for Jira Cloud.
* Follow our [Quickstart Guide](https://docs.getint.io/guides/quickstart/connection#jira) for more details on how to create the connection.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTM4mxWp0iygKg9Ey0ZZa%2FCreate%20a%20connection.png?alt=media&#x26;token=d615fc24-d004-49e2-80f2-1600738e4acf" alt=""><figcaption></figcaption></figure>

* Select the Jira project you wish to integrate with GitHub.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVIKxUlQfvPzPm23omA33%2FConfigure%20the%20connection.png?alt=media&#x26;token=f9da4ee8-b416-4334-9fe8-df33f9b0c7c7" alt=""><figcaption></figcaption></figure>

**6. Enter GitHub Token in Getint**

* Once you have generated a Personal Access Token in your GitHub instance, you will now have the option to connect the tool with Getint.
* Paste the GitHub Personal Access Token into the API token field.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbeokfRzBNHUTiJKlq2V8%2FGitHub%20entering%20API%20token.png?alt=media&#x26;token=a06eb84b-1780-4ab3-b8b7-f443792b1f51" alt=""><figcaption></figcaption></figure>

* Select the GitHub repository or the Project you want to sync with Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuYkG6xcvanrQL6ebtPce%2FConnection%20to%20GitHub.png?alt=media&#x26;token=18b06aee-f09a-406c-93d0-dadfb6fe1b12" alt=""><figcaption></figcaption></figure>

* Click Save to establish the connection.

**7. Issue Type Mapping**

* Map the Jira issue types you want to sync with GitHub tasks, such as mapping a GitHub Task to a Jira task or a Jira bug to a GitHub task.
* Consider using the **Quick Build** beta feature for automated type and field mapping, which can streamline the setup process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F7QJTEaNHF8ET6nsnfId4%2FJira%20GitHub%20integration%20main%20screen.png?alt=media&#x26;token=851237ad-c4e0-417f-bade-dd2259d11a9d" alt=""><figcaption></figcaption></figure>

#### 8. Field Mapping <a href="#id-7.-field-mapping" id="id-7.-field-mapping"></a>

* Review or manually map fields within mapped types, including title, description, and assignees.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FLB3W6KC6VK4eCUe11jZu%2FField%20Mapping.png?alt=media&#x26;token=12a1abbe-3bac-4d8e-a365-8c18f5ef192b" alt=""><figcaption></figcaption></figure>

**9. Assignee Mapping**

* Use the assignee mapping option to match Jira assignees to GitHub collaborators, enabling precise synchronization of task ownership. For more details, visit our doc: [Assignees (users) mapping](https://docs.getint.io/getintio-platform/workflows/assignees-users-mapping).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9u3PwXpgnKsl8PwKvwn0%2FAsignee%20Mapping.png?alt=media&#x26;token=88059e10-c0bf-4231-ad5f-c4528dd4fa87" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
When syncing **projects**, make sure your repository is linked to the target project. If it isn’t, assignees won’t appear in the mapping dropdown.
{% endhint %}

#### 10. Status Mapping

* Map status fields to align between Jira and GitHub. For example, **To do** in Jira could be mapped to **Opened** in GitHub.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FmdPpFvoAlrK2lMAfQ5Pj%2FStatus%20Mapping.png?alt=media&#x26;token=86bd30ee-b5f1-4ef9-a076-48c62bae1fb3" alt=""><figcaption></figcaption></figure>

#### 11. Comments <a href="#id-10.-comments" id="id-10.-comments"></a>

* When enabling comment synchronization, you can filter by criteria such as created date, author, or visibility (public/private).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FbWUDWHZTBZuydDO5ZWrv%2FComments.png?alt=media&#x26;token=1f257003-8e9a-439f-a5fa-48cc3ce2496b" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Attachment Limitation**: Attachments are currently limited to one-way syncing and are only supported from Jira to GitHub. Attachments in GitHub will not sync to Jira
{% endhint %}

**12. Filtering:**

* It is possible to filter the synchronization to have it customized for your needs and requirements. Please see the doc [Items Filtering](https://docs.getint.io/getintio-platform/workflows/items-filtering) for more details.

**UI Filtering Option:**

* Click on the filtering icon near the app icon in your integration. This will apply to that side of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0hJ9uxMKjOazAFXe8yHk%2FFiltering.png?alt=media&#x26;token=916e2e03-a017-4db0-9d18-8dc644776e40" alt=""><figcaption></figcaption></figure>

* Select if the filtering applies to All, New, and Synced items.
* Note that if the option **New items** is selected, the filtering will apply only to the new items, and the already synced items will continue to sync and update. If the option **Synced items** is selected, only the already synced items will be updated based on that filter.
* Choose the options and add the value for the filter. It is possible to filter more than one option for each field.
* Select **Apply** once you have created the filters and **Save** the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F2OYcFAuHtmED9CyXmJDN%2FUI%20Filtering.png?alt=media&#x26;token=f0899ace-21e6-4d9a-a638-076fc8ba16cf" alt=""><figcaption></figcaption></figure>

**13. Test the Integration**

* Create test issues or tasks in Jira or GitHub and observe how they synchronize.
* Ensure that the data between the two platforms is correctly synced.
* Monitor the integration status and the logs in Getint to verify that everything functions as expected.

***

### Conclusion <a href="#conclusion" id="conclusion"></a>

By following this guide, you can successfully integrate **Jira** and **GitHub** using Getint. This setup enables smooth synchronization of issues, tasks, and workflows between development and project management tools, helping teams collaborate more effectively and bridging the gap between developers and project managers.

For further assistance, please contact us at the [Support Center](https://getint.io/help-center) or [Schedule a Demo](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FquqlmoKO6zqGHsjk6DTL%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=de8e62c8-2dd6-4ee8-8d8d-c133b8b954b4" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Having issues building your integration? Schedule a free consultation with our Integration Experts now!</a></p></figcaption></figure>
