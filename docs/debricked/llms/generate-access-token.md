# Source: https://docs.debricked.com/product/administration/generate-access-token.md

# Generate access token

{% hint style="info" %}
**Only users with administration rights can generate access tokens.**
{% endhint %}

Access tokens are a secure way of performing automated integrations with OpenText Core SCA. They are safer compared to using a username and password, and their typical use cases include GitLab, Bitbucket, and API integrations, which are not tied to a particular user, but rather to a repository or a project.

To generate a new access token:

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FInv2DNUVWRa2zegl2mhq%2Faccess%20token%20generation.png?alt=media&#x26;token=4e8e3642-cba9-48bf-94c0-79d877b894d6" alt=""><figcaption></figcaption></figure>

1. Go to **Admin tools** on the left side menu.
2. Type your password to go to administrative mode.
3. In the **Access Tokens** tab, click the **+Create** button.
4. Type the description. If needed, select the **Admin** box which gives access to more actions, such as performing scans.
5. Click **Generate.**
6. Copy the generated token.

To generate a new access token for an Enterprise:

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FskhKr5xQyQaOroK6MixK%2FAccessToken1.png?alt=media&#x26;token=f96267af-5943-43dc-aa85-1a3c64b3a5d8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FjFKL0ixnrIqGd9JUvsU8%2Fimage.png?alt=media&#x26;token=7f1a1fe5-b94a-42d2-9954-935fafe2abd2" alt=""><figcaption></figcaption></figure>

1. Go to **Admin tools** on the left side menu.
2. Type your password to go to administrative mode.
3. In the Access token tab, click the **+Create** button.
4. Type the description.
5. Select the repositories and user roles from the drop-down.
6. Click **Generate**.
7. Copy the generated token.

{% hint style="info" %}
**Save the token before closing the window as you can only view this token once.**
{% endhint %}

### Export access token details

You can export the filtered and visible access token details in the table to a CSV file. To do so, click **Export Table** located at the top-right corner of the table. *For more information, refer to the* [*Export table data*](https://docs.debricked.com/product/administration/repositories/export-table-data) *topic.*

### Token access scope

#### Freemium & Premium

For 'Freemium' and 'Premium' accounts, the following two access scopes are available:

* Admin tokens - Always give access to all repositories, both already existing and those created in the future.
* User tokens - When creating a token, the new token gets **User** access (equivalent to [Reviewer in RBAC](https://docs.debricked.com/product/users/role-based-access-control-enterprise#userroles)) to every existing repository at the time of token creation.

#### Enterprise (with Role-Based Access Control (RBAC))

For Enterprise accounts, the access scope of access tokens can be configured granularly with different scopes for individual repositories. The access granted by the various scopes is equivalent to that provided by our RBAC user roles.

For repositories created or integrated after the generation of the token, access will be based on the default role, which can be configured by a company admin.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2F5nlgtVArRVP8t9UQDwBo%2Fimage.png?alt=media&#x26;token=55db13f4-bb8b-4382-a27c-91c6b65e061e" alt=""><figcaption></figcaption></figure>

*For more information on the available user roles, their access and how to set the default role, see* [*Role-Based Access Control (Enterprise)*](https://docs.debricked.com/product/administration/users/role-based-access-control-enterprise)*.*
