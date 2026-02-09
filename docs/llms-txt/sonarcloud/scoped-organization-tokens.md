# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/scoped-organization-tokens.md

# Managing Scoped Organization Tokens

*This feature is only available in the Team and Enterprise plans. See* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") *for more information.*

Scoped Organization Tokens are used to run analyses on your code. To do so, the `sonar.token` property is used. For more details see [#authentication-to-the-server](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters#authentication-to-the-server "mention").

You must be an organization admin to be able to retrieve and manage Scoped Organization Tokens. This section explains how to do this in the UI. You can also use the [Authentication domain API](https://api-docs.sonarsource.com/sonarqube-cloud/default/public-externalauthentication-0-0).

### About Scoped Organization Tokens

Scoped Organization Tokens provide a secure way to manage non-user-specific authentication. Attached to an organization, they are created and managed by the organization admin who can revoke them anytime. Revoked tokens are automatically deleted.

{% hint style="info" %}

* Scoped Organization Tokens are identified through their `sqco_` prefix.
* SonarQube's S7791 rule can verify the non-disclosure of Scoped Organization Tokens within your code.
  {% endhint %}

Scoped Organization Tokens comply with the principle of least privilege through its scope definition:

* You define the projects within the organization to which the token gives access. You can limit the access to a custom selection of existing projects or select all current and future projects.
* You define the permissions granted by the token. Currently, you can only grant the Execute analysis permission but other permissions will be supported soon.

You can define any expiry date for your Scoped Organization Token, or no expiration. The different token statuses are:

* Active
* About to expire (in less that 7 days)
* Expired

{% hint style="info" %}
For security reasons, tokens without expiry date that have been inactive for 60 days will be automatically removed.
{% endhint %}

### Retrieving and viewing Scoped Organization Tokens

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Scoped Organization Tokens**. The list of tokens is displayed as illustrated below.

<figure><img src="broken-reference" alt="The configured Scoped Organization Tokens are listed through the Administration > Scoped Organization Tokens menu of your org"><figcaption></figcaption></figure>

3. In the list of tokens, locate the token you want to view and select the **Actions** menu at the end of the row.
4. In the menu, select **View details**. The token details are displayed as illustrated below.

<figure><img src="broken-reference" alt="Detailed view of a Scoped Organization Token with token information on the left and project scope on the right."><figcaption></figcaption></figure>

### Creating a Scoped Organization Token

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration > Scoped Organization Tokens**.
3. In the top right corner, select the **Create token** button.

<figure><img src="broken-reference" alt="To create a token, fill in the required fields and select the project scope option."><figcaption></figcaption></figure>

4. Enter the token name and description. Choose a name that accurately represents the token purpose.
5. In **Expires in**, select the token lifetime or select **No expiration**.
6. In **Projects this token can access**, select the option you want to use, either a custom selection of projects or all projects within the organization.\
   If you selected **Custom selection of projects**:
   1. Select the **Select projects** button. The **Projects scope** dialog opens.
   2. Select the projects to which the token will give access.as illustrated below.
   3. Close the dialog.

<figure><img src="broken-reference" alt="Click on a project in the list to select it. Its selection box is checked."><figcaption></figcaption></figure>

7. Select the **Generate token** button. A message pops up to notify the successful token generation.
8. Immediately copy the generated token from the notification message. Once you’ve left the notification, you won’t be able to view the token value any more.

<figure><img src="broken-reference" alt="Select the copy tool located at the right of the generated token to copy and then paste the token."><figcaption></figcaption></figure>

12. You can now close the notification.

### Revoking a Scoped Organization Token

When you revoke a Scoped Organization Token, it’s automatically deleted.

To revoke a Scoped Organization Token:

1. Retrieve your token as described above in [#retrieving-and-viewing-scoped-organization-tokens](#retrieving-and-viewing-scoped-organization-tokens "mention").
2. In the **Actions** menu, select **Revoke**. A confirmation dialog opens.
3. Confirm. The token disappears from the list of tokens.

### Modifying the scope of a Scoped Organization Token

You can modify the custom list of projects to which a Scoped Organization Token gives access.

{% hint style="warning" %}
You cannot modify the scope of a Scoped Organization Token configured for all current and future projects.
{% endhint %}

To modify the custom scope of a Scoped Organization Token:

1. Retrieve your token as described above in [#retrieving-and-viewing-scoped-organization-tokens](#retrieving-and-viewing-scoped-organization-tokens "mention").
2. In the **Actions** menu, select **View details**.&#x20;
3. Select the **Edit projects** button. The **Projects scope** dialog opens.
4. Change the project selection.
5. Select **Close**.

### Related pages

[#authenticate-to-api](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api#authenticate-to-api "mention")
