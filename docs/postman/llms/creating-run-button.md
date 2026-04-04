# creating-run-button

Create a **Run in Postman** button to instantly bring your Postman collections into your user's environment. The **Run in Postman** button enables users to fork collections. You can embed the button in your website or a README to enable developers to interact with your API.

For example, you can click the following **Run in Postman** button to fork the Postman API collection.

![Run in Postman](https://run.pstmn.io/button.svg)

You can create the **Run in Postman** button from API specification formats like OpenAPI and RAML. First, convert the file to a collection by [importing it into Postman](/docs/getting-started/importing-and-exporting/importing-data/), or by generating a collection from your API in [the API Builder](/docs/design-apis/api-builder/develop-apis/adding-api-elements/#generate-a-new-collection-from-your-api-definition) or [Spec Hub](/docs/design-apis/specifications/generate-collections/).

## Create a Run in Postman button

You can create a **Run in Postman** button for any of your public collections from the [Postman API Network](/docs/collaborating-in-postman/public-api-network/public-api-network-overview/). Then you can embed the code where you'd like the button to display for your users. To create a **Run in Postman** button, the collection must only have HTTP requests. The **Run in Postman** button isn't available for other types of protocols.

Your collection must be in a public workspace. If your collection isn't in a public workspace, [change the workspace visibility to public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/#convert-an-existing-workspace-to-a-public-workspace) or [move the collection](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#move-elements-to-workspaces) to a public workspace.

To create a **Run in Postman** button, do the following:

1. Access the [Postman API Network](https://www.postman.com/explore/). If you're on a paid plan, you can click **API Network** in the Postman header, then select **View all public APIs**.
2. Click ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Create New** on the left and select ![Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Run in Postman button**.
3. Search for and select a public collection you want to share.
   - To replace the collection, click **Choose a different collection**.
4. (Optional) Select an environment.
5. Click **Next**.
6. Choose an embed code format that's HTML or Markdown friendly:
   - **HTML friendly** - This embed code uses JavaScript, HTML, and CSS, so you can customize the button for a website. You can [customize](/docs/publishing-your-api/run-in-postman/customize-run-button/) the embed code to dynamically create and update environments and add environment variables to a user's workspace.
   - **Markdown friendly** - This embed code uses Markdown, so you can display it in a README, blog, or other Markdown document.
7. Click ![Copy icon](https://assets.postman.com/postman-docs/aether-icons/action-copy-stroke.svg#icon) **Copy Code**.
   ![Create a Run in Postman button modal](https://assets.postman.com/postman-docs/v11/share-collection-run-in-postman-pan-v11.62.png)
8. Embed the code where you'd like the button to display, such as your organization's public API documentation.
   - You can also create a **Run in Postman** button from a collection. Click **Collections** in the sidebar of a public workspace, select ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions > Share** next to the collection you want to share. Then, click ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** and select **Run in Postman**.
9. ## Sample code snippets for the Run in Postman button

The embed code in Markdown or HTML format includes your collection's ID and URL. In the examples below, `:collection_id` is a placeholder for the ID and `:collection_url` is a placeholder for the URL. If you chose to include an environment in your button, the code will also have the `environment` parameter.

The following is an example of code to embed in Markdown format:

```markdown
[center class="width: 128px; margin: auto;"]
[img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;" role="img"\]](https://god.gw.postman.com/run-collection/:collection_id?action=collection%2Ffork&source=rip_markdown&collection-url=entityId=12959542-c8142d51-e97c-46b6-bd77-52bb66712c9a&entityType=collection&workspaceId=405e0480-49cf-463b-8052-6c0d05a8e8f3)
[/center]
```

The following is an example of code to embed in HTML format:

```html
<div class="postman-run-button"
data-postman-action="collection/fork"
data-postman-visibility="public"
data-postman-var-1=:collection_id
data-postman-collection-url=:collection_url
> 
</div>
<script type="text/javascript">
  (function (p,o,s,t,m,a,n) {
    !p[s] && (p[s]=function () { (p[t]||[]).push(arguments); });
    !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild((n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n
  })();
</script>
```

## Use a Run in Postman button

Click the **Run in Postman** button to open the page where you can fork the collection to your workspace. [Forking the collection](/docs/collaborating-in-postman/using-version-control/forking-elements/) into your workspace will enable you to contribute to the source collection using pull requests. You can also view the collection in a public workspace if you like and even import a copy of the collection using the links present on the screen. All collections shared with the new **Run in Postman** buttons come with [fork counts](/docs/collaborating-in-postman/using-version-control/forking-elements/#view-fork-information), that help you and your consumers understand how developers use the API.

![Fork collection for Run in Postman](https://assets.postman.com/postman-docs/fork-collection-for-run-in-postman.jpg)

Live **Run in Postman** buttons are automatically updated with changes in the original collection, so your consumers always get the most recent version of your collection without publishers having to manually update the collection's link.