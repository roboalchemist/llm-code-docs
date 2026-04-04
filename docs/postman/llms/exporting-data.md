# Export data from Postman

You can export your Postman data, including collections, environments, global variables, and data dumps, as JSON files. You can import these files back into any Postman instance, share them with others, or use them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) or [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

## Export collections

1. Click **Collections** in the sidebar.
2. Click ![Image 1: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to a collection, then select **More > Export**.
3. (Optional) Invite teammates or click **Copy Collection Link** to share the collection.
4. Select the export format (**Collection v2** or **Collection v2.1**) for the collection.
5. Click **Export JSON** to download the generated JSON file.

## Export environments

1. Click **Environments** in the sidebar.
2. Click ![Image 2: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to an environment, then **Export**. The file will download automatically.

## Export data dumps

You can export a bulk data dump of all your collections and environments in Postman. You can then import the data into any Postman instance. If you are on a team, only Team Admins and Super Admins can export bulk data.

To export a data dump, do the following:

1. Click your avatar in the Postman header, then click **Settings**.
2. Click the **Account** tab, then **Export Data**.
3. Click **Export Data**, then select the data types you want to export. You can export collections, environments, or both.

    ![Image 3: Export data dump](https://assets.postman.com/postman-docs/v10/import-export-data-dump-request-confirm-v10-16a.jpg)

When the export is ready, you'll get an email with a link to download the bulk data file. The download is available for two days, after which it expires.

### Import a data dump into Postman

After exporting a data dump file, you can import it into any Postman instance. You must unzip the data dump file before importing it.

Unzipping the data dump file results in a folder with a unique name. Inside you'll find a subfolder for each data type you chose to export, with individual JSON files for each exported collection and environment. You'll also find an `archive.json` file that lists the IDs of all exported collections and environments.

To import the data dump into Postman, do the following:

1. In a workspace, click **Import** in the sidebar.
2. Drag the unzipped data dump folder into the import window.
3. Select the environments and collections you want to import, then click **Import**.

Learn more about [importing data into Postman](/docs/getting-started/importing-and-exporting/importing-data/).