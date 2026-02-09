# Work with API definitions in the Postman API Builder

You create the structure of your API using the _API definition_. The API definition can consist of one or multiple files. If your API doesn't have a definition, you can add an example definition, import a definition, or add a definition from a connected repository.

## Supported API definition formats

Postman supports the following API definition formats:

* OpenAPI versions 1.0, 2.0, 3.0, and 3.1
* RAML 0.8 and 1.0
* protobuf (protocol buffer) 2.0 and 3.0
* GraphQL
* WSDL 1.0 and 2.0

OpenAPI definitions can be JSON or YAML. RAML definitions must be YAML. Protobuf definitions are `.proto` files. GraphQL definitions can be JSON or GraphQL SDL. WSDL definitions must be XML.

## Add an example API definition

If your API doesn't have a definition, you can add an example definition that you can edit.

1. Click **APIs** in the sidebar and select an API.
2. Next to the API, click ![Image 1: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions**. Then select **Add definition > Author from scratch**. You can also select **create** under the API.
3. Select a definition type from the **Definition type** menu, then select a format from the **Definition format** menu.
4. To start with a sample definition, click **Use a boilerplate**.
5. Click **Create Definition**.

## Import an API definition

You can import a file into your API to define your API.

1. Click **APIs** in the sidebar and select an API to expand it.
2. Next to the API, click ![Image 2: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions**. Then select **Add definition > Import files**. You can also select **Import** under the API.
3. Select or drag the file you want to import. You can also import an API from a folder, a link, a code repository, or an API gateway. Learn more about [importing an API](/docs/design-apis/api-builder/importing-an-api/).

## Add an API definition from a connected repository

If your API is [connected to a Git repository](/docs/design-apis/api-builder/versioning-an-api/overview/#connecting-to-a-remote-git-repository), you can select a definition file in your repository and add it to your API.

1. Click **APIs** in the sidebar and select an API to expand it.
2. Next to the API, click ![Image 3: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions**. Then select **Add definition > Add from connected repository**.
3. Enter the file path (in the repository) of the definition file you want to add and click **Select**.

    ![Image 4: Selecting a definition file](https://assets.postman.com/postman-docs/v11/api-builder-select-definition-file-v11.jpg)

4. Click **Add Files**. The definition files you selected are added to your API. For OpenAPI 2.0 and 3.0 APIs, Postman scans for any dependent files referenced in the definition files and automatically adds them to your API.

## Edit an API definition file

To edit an API definition, click an API to expand it, then click **Definition**. Click the API's definition file to open it for editing.

You can also edit your definition from your API's overview. Under **Definition**, click **View files**.

The left pane of the editor displays an outline of your API definition. When you first open the editor, the top level nodes are expanded, and you can click a node to expand or collapse it. Select an element in the outline to jump to it in the editor. You can also click ![Image 5: Schema outline icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-schemaOutline-stroke.svg#icon) **(Hide/show) schema outline** to hide or show the outline.

![Image 6: Editing an API definition](https://assets.postman.com/postman-docs/v11/api-builder-edit-definition-v11.jpg)

In the API definition editor, you can click a `#ref` component and press **â** or **Ctrl** to jump to the reference location.

![Image 7: Jumping to a reference location](https://assets.postman.com/postman-docs/v11/api-builder-ref-jump-v11.70.png)

In the upper right of the editor, you can beautify, wrap, copy, and search content in the API definition.

As you edit your API definition, Postman displays a [live preview of your API's documentation](#view-live-documentation) and [identifies syntax errors](#validate-a-component-file).

Your teammates can't reuse components in a draft component file. [Publish a version of a component file](#version-and-publish-a-component-file) to allow your teammates to reference its components in their specifications.

To learn more, see [Troubleshoot vault secrets](#troubleshoot-vault-secrets).

## Work with multi-file API definitions

Your API definition can span multiple files and folders. This is called a _multi-file API definition_. Multi-file API definitions are supported in OpenAPI 2.0 and 3.0 APIs and protobuf 2.0 and 3.0 APIs.

A multi-file API definition consists of the following components:

* **API Definition** - The entire definition of the API, combining all files within it.
* **Files** - One or more files that specify the API definition.
* **Root file** - The top-level file that hosts the operations defined by the API. See below for more information on root files.
* **Folders** - You can create folders within an API definition to organize files. You can also add folders within folders.

Multi-file API definitions don't support the schema sync integration. Instead, use [API version control](/docs/design-apis/api-builder/versioning-an-api/overview/) to sync with a repository.

### About root files

An API definition's root file can reference other files in the API definition. If you made a tree diagram of the relationships between all files in an API definition, the root file would be the file at the top of the tree. When you [create a new API definition](/docs/design-apis/api-builder/creating-an-api/) or [import an API](/docs/design-apis/api-builder/importing-an-api/), Postman determines the root file based on the references across the files. API definitions don't support references which are external links or present within a separate API.

For OpenAPI 2.0 and 3.0 API definitions, Postman detects root files based on the content and references within files while importing or creating an API definition. You can't set a file as root for OpenAPI definitions. OpenAPI definitions can have one root file. If you delete the root file, Postman will recalculate the next candidate for the root file automatically.

For protobuf API definitions, while importing the API, Postman detects all files which have service definitions present in them and marks one as the root. You can set another file as root if there's more than one candidate for root file. Click ![Image 8: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to a `.proto` file in the sidebar and select **Mark as root**.

### Edit a multi-file API definition

To edit a multi-file API definition, select an API in the sidebar to expand it, then select **Definition**. If your definition has folders, select a folder in the sidebar to expand it and see its contents. Select a file to open it for editing.

### Add files and folders

You can add new files and folders to a multi-file API definition. In the sidebar, click ![Image 9: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to **Definition**, then select **Add file** or **Add folder**. If your API is [connected to a Git repository](/docs/design-apis/api-builder/versioning-an-api/overview/#connecting-to-a-remote-git-repository), select **Add file > Create new** to add a new file.

To add a new file or subfolder to a folder, click ![Image 10: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to a folder, then select **Add file** or **Add folder**. You can rearrange files and folders by dragging them in the sidebar. You can also rename or delete a file or folder by clicking ![Image 11: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions**.

When you add a file to a single-file OpenAPI 2.0 or 3.0 definition, or to a protobuf 2.0 or 3.0 definition, it's converted to a multi-file API definition. The existing definition file becomes the root file.

### Add files from a connected repository

If your API is [connected to a Git repository](/docs/design-apis/api-builder/versioning-an-api/overview/#connecting-to-a-remote-git-repository), you can add files from your repository.

1. Click **APIs** in the sidebar and select an API.
2. Click ![Image 12: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to **Definition** and select **Add file > Add from connected repository**.
3. Enter the file path (in the repository) of the definition file you want to add and click **Select**. You can select more than one file to add from the repository.

    ![Image 13: Selecting a definition file](https://assets.postman.com/postman-docs/v11/api-builder-select-files-from-git-v11.jpg)

4. Click **Add Files**.
    
    The definition files you selected are added to your API. For OpenAPI 2.0 and 3.0 APIs, Postman scans for any dependent files referenced in the definition files and automatically adds them to your API.

The **Add file > Add from connected repository** option isn't available for Git integrations added using Postman v10.17 or earlier. Instead, add the definition files to the schema directory in the repository. Alternately, you can [remove the Git integration](/docs/design-apis/api-builder/versioning-an-api/using-cloud-git-repo/#disconnecting-a-cloud-hosted-repository) and then [reconnect your API to the Git repository](/docs/design-apis/api-builder/versioning-an-api/overview/#connecting-to-a-remote-git-repository).

### Delete files and folders

To delete a definition file or folder, click ![Image 14: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to the item and select **Delete**. Deleting a file or folder doesn't affect other elements added to the API, such as collections.

You can restore a deleted definition file using the [**Changelog**](/docs/design-apis/api-builder/managing-apis/#use-the-changelog). Click ![Image 15: History icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-history-stroke.svg#icon) **Changelog** in the right sidebar, then click **Restore** below the definition file you want to restore.

If you connect your API to a Git repository, the changelog is replaced by the **Source Control** pane. Learn more about [API version control](/docs/design-apis/api-builder/versioning-an-api/overview/).

If your API is [connected to a Git repository](/docs/design-apis/api-builder/versioning-an-api/overview/#connecting-to-a-remote-git-repository), you have the option to remove or delete a file. Click ![Image 16: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to a file and select **Delete**, then choose an option:

* Click **Delete File** to delete the file from your API and your repository. The file will be deleted from your repository when you push changes from Postman.
* Click **Remove File** to remove the file from your API in Postman. The file won't be deleted from your repository.

    ![Image 17: Deleting a definition file](https://assets.postman.com/postman-docs/v11/api-builder-delete-file-v11.jpg)

**About definition IDs.** When you add a definition to an API, Postman assigns a definition ID to the API. You can view the definition ID by opening an API and clicking ![Image 18: Info icon](https://assets.postman.com/postman-docs/aether-icons/state-info-stroke.svg#icon) **Info** in the right sidebar. The definition ID acts as a container for all the definition files in the API. If you delete all the definition files, the definition ID itself isn't deleted. If you then add a new definition file, the definition ID remains the same as before.