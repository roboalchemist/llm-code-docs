# Source: https://directus.io/docs/raw/guides/content/import-export.md

# Import & Export

> Learn to import and export multiple items stored as files using Directus.

The content module allows importing and exporting of multiple items from and to files respectively.

## Import Items

![Import items](/img/194f51c9-9d2d-4264-ad09-8142ff671aea.webp)

You can import JSON or CSV files into your collection as items.

To import Items from a file, navigate to the collection and click "Import / Export" in the sidebar. Click into the import search box. A file browser will open. Once a file has been selected, click on "Start Import" to import the items.

The items will now be in the collection, and the file itself will not be stored in the Directus project.

<callout icon="material-symbols:warning-rounded" color="warning">

The field headers in the imported file must match the field keys of the collection you're importing into. Otherwise, the column will be skipped.

</callout>

<callout icon="material-symbols:info-outline">

**Importing Relational Files**
It is possible to import relational field values as well. For this task, the user performing the import will need access
permissions for the related collection.

</callout>

<callout icon="material-symbols:info-outline">

**Import Error Handling**
During import operations, errors are collected up to the maximum defined by [`MAX_IMPORT_ERRORS`](/content/configuration/security-limits.md), after which the import is cancelled.

</callout>

## Export Items

![Export items](/img/6253cd72-005d-4551-b3fd-72acd33e47f6.webp)

When exporting items, the export items menu provides granular control over exactly which items and
fields are exported, how they are exported, and where they are exported.

To export items, follow the steps below, navigate to the desired collection and select "Import / Export" from the sidebar. Click on "Export Items" and the export items menu will appear. Select the desired format from CSV, JSON, XML, or YAML and click <icon name="material-symbols:download-for-offline">



</icon>

 to download the file.

## Export Items Menu

This menu provides granular control over exactly which items and fields are exported, how they are exported, and where
they are exported.

<table>
<thead>
  <tr>
    <th>
      Item
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Format
      </strong>
    </td>
    
    <td>
      Choose to export items as CSV, JSON, XML, or YAML.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Limit
      </strong>
    </td>
    
    <td>
      Set the maximum number of items to be exported.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Export Location
      </strong>
    </td>
    
    <td>
      Download the export file directly to your machine or to the file library.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Folder
      </strong>
    </td>
    
    <td>
      Choose the Folder to download to (if export location is the folder library).
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Sort Field
      </strong>
    </td>
    
    <td>
      Choose field to sort items by.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Sort Direction
      </strong>
    </td>
    
    <td>
      Choose to sort items in ascending or descending order.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Full-Text Search
      </strong>
    </td>
    
    <td>
      Limit exported Items to ones which matched as search results.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Filter
      </strong>
    </td>
    
    <td>
      Limit exported items with a filter.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Fields
      </strong>
    </td>
    
    <td>
      Add, remove, and re-order the item fields that will be exported.
    </td>
  </tr>
</tbody>
</table>
