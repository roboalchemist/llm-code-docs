# Source: https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/users.md

# Users

In the **Profile Icon -> Settings ->** **Users** page, you view and manage all the users in the company. You can also define roles for each user.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5FBx4xhyoEO8IEaAquVo%2Fimage.png?alt=media&#x26;token=67e670b2-a254-4268-b736-b945c171bddd" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
**Key points**:&#x20;

* **Users** page is available only for users with the **Settings** role. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.
* You can create and manage users from the **Users** page, only when your company is not integrated with Active Directory (AD). If you sign-in to the Avaamo Platform using SSO, then since your company is configured with Active Directory (AD), all the users must be created and managed via AD. You must contact your AD administrator for further assistance to manage users. See [Identity provider](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers), for more information on SSO integration.&#x20;
* You can also add users to a **Group** and manage roles at the Group-level. See [Groups](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/groups), for more information.
* The roles displayed for the user are a union of all the roles assigned to the user and groups the user belongs to. Example: Consider that John Miller has a Development role and John Miller also belongs to a Group that has a Testing and Staging role. The roles displayed for John Miller is - Development, Testing, and Staging.&#x20;
  {% endhint %}

### Search users

In the **Users** page,&#x20;

* Select **Active** to view a list of all active users. This is the default view.&#x20;
* Select **Archived** to view a list of deleted users.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MTGkj4_gt0DO9QQ95D_%2F-MTGmUgBZehVJuInpcuL%2F5.6-archived-users.png?alt=media\&token=52186164-14e8-4a0e-9e11-7c229d746592)

The Users list in both the views is displayed in alphabetical order of the user name. You can use Pagination at the bottom to view and search users by name.

### Add new user

* In the **Users** page, click **Add new.**
* Specify the first name, last name, email, identity provider, and roles of the user and click **Submit.** Note that the email identifier must be unique. See [Roles and permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLkSMDskSUl6tTLGEGNhl%2Fimage.png?alt=media&#x26;token=846d1bb8-f937-4603-947b-31974112af15" alt=""><figcaption></figcaption></figure>

### Delete user

In the **Users** page, click three ellipse dots in the **Actions** column of the user to view the extended menu and click **Delete.**&#x20;

* If the user is the owner of any agents, then the following pop-up is displayed that allows you to delegate the ownership to a replacement user:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QMGiWoWdRubrVInqV%2F-M-QNX1eaX98TlW90H0C%2Fhowto-delete-user.png?alt=media\&token=b2ae4164-a14e-449b-9009-fa3493ed6e0c)

* Select the replacement user and click **Delete**.

### Edit user

In the **Users** page, click **Edit** in the Actions column of the user. The user details page is displayed. Edit the user details as required and click **Submit**.

{% hint style="info" %}
**Note**: A user can belong to multiple groups with different roles and each user can also have exclusive roles. In the **Edit Users** page, only roles assigned exclusively to the user are displayed as only these can be edited. If you wish to remove or add a role belonging to a group, then you must edit the Groups page. See [Groups](https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/users-and-permissions/groups), for more information. &#x20;
{% endhint %}

### Get user access token

In the **Users** page, click three ellipse dots in the **Actions** column of the user to view the extended menu and click **Access token**.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FK0z6djnZ6NcTZHIBVQmp%2FScreenshot%202022-07-18%20at%205.48.49%20PM.png?alt=media\&token=f26ac6a6-d3f8-4f86-9380-536178c36fc3)

This is used for APIs when user authentication is required. Using user access tokens is a standard recommended approach.&#x20;

* It provides stronger security as the access token is private and only the user with appropriate permissions can view the user access token.&#x20;
* There is a track of all changes made by the access-token owner captured in change and audit logs.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-QMGiWoWdRubrVInqV%2F-M-QO1DSL0-D065Xk2If%2Fhowto-user-access-token.png?alt=media\&token=e6f1b312-3f03-4892-b43c-ce81414348c1)

You can either use the access token that is already available or click **Regenerate Access Token** to generate a new one. See [Message API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/message-api#header), for an example of user token usage.

{% hint style="info" %}
**Note:** It is recommended to create service accounts for API access as user tokens may get invalidated if the user is archived or any user permission-related changes are made.
{% endhint %}
