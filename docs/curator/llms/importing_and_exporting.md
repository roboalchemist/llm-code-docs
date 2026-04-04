# Source: https://docs.curator.interworks.com/upgrading_migration/migration/importing_and_exporting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Importing and Exporting

> Manual backup and migration process for transferring Curator content between installations.

We provide a simple manual backup process that can help with migrating your Curator content from one
environment to another, or to the server as a backup so you don't lose all that hard work.

## Migration Via File

This method to migrate data involves downloading a file from the source Curator and uploading it to the destination
Curator. These files can be used as backups or a simple way to pass data to the Curator support team for debugging
your specific content.

***To export your Curator metadata:***

1. Login to the backend of your source Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to **Settings** > **Curator** > **Import/Export** section using the left-hand menu.
3. Check the necessary items you need to backup (or click 'Select All' at the top)
4. Click "Export" and this will download a file you can keep as a backup or use to import your settings
   to another Curator instance.

***To import your Curator metadata:***

1. Login to the backend of your destination Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to **Settings** > **Curator** > **Import/Export** section using the left-hand menu.
3. Click on the "Import" tab at the top.
4. Click the "Upload" icon (upwards arrow) to locate the JSON file you exported using the steps above, then
   click "Preview Import".
5. Check the necessary items you need (or click 'Include All' at the top)
6. Click the "Import" button to complete the import process.

## Migration Via API

This method to migrate data involves using Curator's REST API from the destination Curator to request data from the
source Curator. This option can be convenient because it requires fewer steps after the initial setup.

***Retrieve an API key:***

1. Login to the backend of your source Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to **Settings** > **Curator** > **API Keys** section using the left-hand menu.
3. Copy an API Key using the icon in the "ACTIONS" column. *Note: If the API Key has "Restrict Access" enabled, ensure
   the "export" endpoint in the "Portal Permissions" section is allowed.*

***To import your Curator metadata:***

1. Login to the backend of your destination Curator instance (e.g. `https://curator.example.com/backend`).
2. Navigate to **Settings** > **Curator** > **Import/Export** section using the left-hand menu.
3. Click on the "Import" tab at the top.
4. Click the "Use API" radio button.
5. Enter the source Curator's URL and API Key. *Note: After completing one import from the source Curator this info
   will be stored. The next time you need to migrate data you can simply select that stored data instead of re-entering
   it.*
6. Check the data types you'd like migrated. Every item of the selected types will be retrieved, but you can select
   specific items in the next page.
7. Click "Preview Import" at the bottom of the screen.
8. Check the necessary items you need (or click 'Include All' at the top)
9. Click the "Import" button to complete the import process.

## Permissions

Each backend user in Curator can be assigned permissions for handling certain content. If your user doesn't have
permissions to make changes to the content included in an import it will be filtered out of the data. You can
request these permissions be added by your Curator administrator or have them process the import.
