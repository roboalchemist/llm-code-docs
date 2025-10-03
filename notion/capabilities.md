# Source: https://developers.notion.com/reference/capabilities

All integrations have associated capabilities which enforce what an integration can do and see in a Notion workspace. These capabilities when put together enforce which API endpoints an integration can call, and what content and user related information they are able to see. To set your integration's capabilities see the [Authorization](https://developers.notion.com/docs/authorization) guide or navigate to <https://www.notion.so/my-integrations>.
![474](https://files.readme.io/06dcfeb-Screen_Shot_2022-07-15_at_11.48.40_AM.png)
A screenshot of the capability configuration screen.
> ## 📘
> If an integration is added to a page, then the integration can access the page’s children
> When an integration receives access to a Notion page or database, it can read and write to both that resource and its children.
* * *
## [](https://developers.notion.com/reference/capabilities#content-capabilities)
Content capabilities affect how an integration can interact with [database objects](https://developers.notion.com/reference/database), [page objects](https://developers.notion.com/reference/page), and [block objects](https://developers.notion.com/reference/block) via the API. Additionally, these capabilities affect what information is exposed to an integration in API responses. To verify which capabilities are needed for an endpoint's desired behavior, please use the API references.
  * **Read content** : This capability gives an integration access to read existing content in a Notion workspace. For example, an integration with only this capability is able to call [Retrieve a database](https://developers.notion.com/reference/retrieve-a-database) , but not [Update database](https://developers.notion.com/reference/update-a-database).
  * **Update content** : This capability gives an integration permission to update existing content in a Notion workspace. For example, an integration with only this capability is able to call the [Update page](https://developers.notion.com/reference/patch-page) endpoint, but is not able to create new pages. 
  * **Insert content** : This capability gives an integration permission to create new content in a Notion workspace. This capability does not give the integration access to read full objects.  
For example an integration with only this capability is able to [Create a page](https://developers.notion.com/reference/post-page) but is not able to update existing pages. 


_It is possible for an integration to have any combination of these content capabilities._
* * *
## [](https://developers.notion.com/reference/capabilities#comment-capabilities)
Comment capabilities dictate how an integration can interact with the [comments](https://developers.notion.com/reference/comment-object) on a page or block.
  * **Read comments** : This capability gives the integration permission to [read comments](https://developers.notion.com/reference/retrieve-a-comment) from a Notion page or block.
  * **Insert comments** : This capability gives the integration permission to [insert comments](https://developers.notion.com/reference/create-a-comment) in a page or in an existing discussion.


* * *
## [](https://developers.notion.com/reference/capabilities#user-capabilities)
An integration can request different levels of user capabilities, which affect how [user objects](https://developers.notion.com/reference/user) are returned from the Notion API:
  * **No user information** : Selecting this option prevents an integration from requesting any information about users. User objects will not include any information about the user, including name, profile image, or their email address.
  * **User information without email addresses** : Selecting this option ensures that User objects will include all information about a user, including name and profile image, but omit the email address.
  * **User information with email addresses** : Selecting this option ensures that User objects will include all information about the user, including name, profile image, and their email address.


## [](https://developers.notion.com/reference/capabilities#capability-behaviors-and-best-practices)
An integration's capabilities will never supersede a user's. If a user loses edit access to the page where they have added an integration, that integration will now also only have read access, regardless of the capabilities the integration was created with.
For public integrations, users will need to re-authenticate with an integration if the capabilities are changed in the time since the user last authenticated with the integration. 
To learn more about setting your integration's capabilities refer to the [Authorization](https://developers.notion.com/docs/authorization) guide. 
In general, you want to request minimum capabilities that your integration needs in order to function. The fewer capabilities you request, the more likely a workspace admin will be able to install your integration.
For example: 
  * If your integration is solely bringing data into Notion (creating new pages, or adding blocks), your integration only needs **Insert content** capabilities. 
  * If your integration is reading data to export it out of Notion, your integration will only need **Read content** capabilities.
  * If your integration is simply updating a property on a page or an existing block, your integration will only need **Update content** capabilities.


