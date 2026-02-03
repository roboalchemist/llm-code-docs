# Publish documentation in Postman

Publishing your documentation makes it publicly available to anyone with the link to the documentation. Publish your documentation to help people around the world learn how to use your collection or interact with your public API.

Public documentation automatically includes details for each request or endpoint in the published collection, along with sample code in various client languages. As you update your collection, the published documentation automatically stays in sync with your latest changes. There's no need to publish the documentation again after making changes.

Your public documentation includes the **Run in Postman** button ![Image 1: Run in Postman button](https://assets.postman.com/postman-docs/run-in-postman-button-icon.jpg#icon) so users can interact with your collection or API directly in Postman. For an example, check out the [Postman API documentation](https://documenter.getpostman.com/view/12959542/UV5XjJV8) which was published from a Postman Collection.

## Make your documentation public

To publish [documentation](/docs/publishing-your-api/document-a-collection/), it must be part of a collection. You can publish documentation for any collections you've created or have permission to edit.

Publishing is only supported for collections with HTTP requests. Also, you can't publish a collection that has been added to an API. Instead, you can [publish a version of the API in the Postman API Builder](/docs/design-apis/api-builder/versioning-an-api/api-versions/). A published version includes the API's definition and collections.

To publish the documentation for a collection, do the following:

1. Click **Collections** in the sidebar, and then select your collection.
2. From the collection's **Overview** tab, click **View complete documentation**.
3. Click **Publish** to navigate to the **Publish Documentation** interface.

![Publish documentation](https://assets.postman.com/postman-docs/v11/documentation-publish-button-v11.jpg)

## Update publication settings

In the **Publish Documentation** interface, change any publication settings as needed.

### Content

Select the content that you want to publish with your docs:

* **Version** - This defaults to **CURRENT**. You can't create versions or releases for collections in Postman v10 and later, but you can [publish versions of an API in the Postman API Builder](/docs/design-apis/api-builder/versioning-an-api/api-versions/).
* **Environment** - Select an [environment](/docs/publishing-your-api/document-a-collection/#associate-environments-with-documentation) to publish environment variables with your documentation.

  The shared values of all variables are published with your documentation, so make sure they don't contain sensitive information such as passwords or tokens.

### URL

Select a [custom domain](/docs/publishing-your-api/custom-doc-domains/) from the **Custom domain** dropdown list where you want to publish your documentation.

### Appearance

Select the appearance settings for your published docs. You can preview any changes you make in the sample layouts in this section before you publish your docs.

* **Default layout** - Select a default layout style for your documentation. **Double column** displays sample code in a column next to the documentation. **Single column** displays sample code inline beneath each request. Your documentation uses this layout by default, but users can select a preferred layout style.
* **Default Theme** - Select a light or dark theme for your documentation. You can also choose to use the system theme. Your documentation uses the selected theme by default, but users can switch between themes.
* **Logo** - By default, public documentation uses your [team logo](/docs/administration/managing-your-team/team-settings/#customize-your-teams-branding). You can also select a custom logo for each theme (light and dark):
  * To add a logo, click the edit icon ![Image 2: Edit icon](https://assets.postman.com/postman-docs/documentation-edit-icon-v8-10.jpg#icon) and click **Upload**. Drag and drop an image file, or select an image file. Drag the handles to adjust the part of the image you want to display, then click **Upload**.
  * To delete a logo, click the edit icon ![Image 3: Edit icon](https://assets.postman.com/postman-docs/documentation-edit-icon-v8-10.jpg#icon) and click **Delete**.
  You can use different logos for each collection you publish. Logos must be 2 MB or less in size and must be in JPEG or PNG format. The logo can be any aspect ratio (square or rectangle.)
* **Colors** - You can customize the colors (in hex format) for each theme (light and dark):
  * **Header background** - Specify a color for the header at the top of the documentation window.
  * **Code background** - Specify a color for sample code blocks.
  * **Highlight** - Specify a color for hyperlinks.

### SEO

Add metadata to your documentation to make it more discoverable on the web.

* **Title** - Add a title for your documentation (60 characters or less). The title appears in web searches and in browser tabs.
* **Description** - Add a brief description to let users know what your documentation is about (160 characters or less). You can also add relevant keywords to help users find your documentation when searching the web.

### Preview your documentation

To preview your documentation using the current settings, click **Preview Documentation**. The preview automatically updates as you change settings.

If Postman detects a possibly sensitive token or other secret, a warning appears at the top of the preview window. Postman also highlights the token so you can remove it from the documentation before publishing.

### Publish your documentation

When you're finished changing settings, click **Publish** to publish your documentation.

* **Postman Free, Basic, and Professional plans** - You can optionally select a [public workspace](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) to move the collection to. This makes the collection discoverable on the [Postman API Network](https://www.postman.com/explore). When you're ready, click **Publish**. You can view your public documentation at the provided URL.
* **Postman Enterprise plans** - Your [Community Manager](/docs/administration/roles-and-permissions/#team-roles) controls the Postman elements your team makes public. Enter a note for your Community Manager and click **Request Publish**. When your request is approved, you'll receive an email notification with a link to the public documentation. To retract your publish request, [change the pending publication settings](#change-publication-settings) and click **Retract request**.

![Published documentation example](https://assets.postman.com/postman-docs/v11/documentation-published-docs-v11.jpg)

## Share your public docs

To share your public documentation, share the published URL with your team members, other users, or the community. If you have forgotten the URL of your published documentation, you can get it at any time.

1. Click **Collections** in the sidebar, and then select your collection.
2. From the collection's **Overview** tab, click **View complete documentation**.
3. Click **Published**, and then click **Copy published link**.

![Copy published link](https://assets.postman.com/postman-docs/v11/documentation-published-link-v11.jpg)

If your collection is in a public workspace, others can search for and find your collection on the [Postman API Network](https://www.postman.com/explore), along with its documentation. If you haven't already moved your collection to a public workspace, you can do so at any time by [changing the publication settings](#change-publication-settings).

By sharing your documentation with the Postman API Network, you increase the visibility of your API to a wider range of consumers in the Postman community. Learn more about [public workspaces](/docs/collaborating-in-postman/using-workspaces/public-workspaces/).

## Change publication settings

Change the publication settings for your documentation to update your documentation's look or make your collection public. You can change the publication settings at any time after publishing your documentation.

1. Click **Collections** in the sidebar and click **View complete documentation**.
2. Click **Published** at the upper right, and then click **Edit published documentation**.

![Edit published documentation](https://assets.postman.com/postman-docs/v11/documentation-edit-published-docs-v11.jpg)

1. Click **Edit settings**, and then change the [publication settings](#make-your-documentation-public) as needed.
2. Click **Save and republish**.

## Unpublish your docs

If you no longer want your documentation to be publicly available, you can unpublish it.

1. Click **Collections** in the sidebar and click **View complete documentation**.
2. Click **Published** at the upper right, and then click **Edit published documentation**.
3. Click **Unpublish**.

If you change your mind, you can [publish your documentation](#make-your-documentation-public) again at any time.

![Unpublish documentation](https://assets.postman.com/postman-docs/v11/documentation-unpublish-v11.jpg)