# Source: https://directus.io/docs/raw/guides/extensions/app-extensions/layouts.md

# Source: https://directus.io/docs/raw/guides/content/layouts.md

# Layouts

> Learn to use layouts for viewing and interacting with items in a collection using Directus.

Layouts are customized mechanisms for viewing and interacting with the items in a collection.

## Adjust a Collection's Layout

![Layouts](/img/f801544a-adc8-4194-aee3-d15cf8bddd6a.webp)

To adjust an item's layout, navigate to the content and select the collection you wish to work with. In the page sidebar, click on "Layout Options". Then you can choose the desired layout type you want to use and customize it accordingly.

Layouts are tailored to work with specific data-models. For example, in order to work properly, the map layout requires
the collection have a map field configured and the calendar layout requires the collection have a datetime field configured.

Each layout presents data differently, so certain customizations may not be functional with certain layouts. For example,
the map layout displays each item as a pin on a map, so this layout has no controls for sorting.

Depending on the layout, the same control may be under layout options in the sidebar, the subheader, or on the page area
(and items themselves). For example, the table layout lets you set the field values displayed in the subheader while
the card layout lets you set field values displayed in the layout options menu.

### Customization Controls

Customization controls can be found in the following three locations:

- **Layout Options** — Located in the sidebar.
- **Subheader** — Located just below the page header and above the page area.
- **Page Area** — The center of the webpage, which displays all items.

These controls typically fall into three general categories.

<table>
<thead>
  <tr>
    <th>
      Category
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Styling and Formatting
    </td>
    
    <td>
      These are additional customizations to the way a layout displays such as the size of each Item, how images are cropped, etc.
    </td>
  </tr>
  
  <tr>
    <td>
      Field Values Displayed
    </td>
    
    <td>
      Most layouts allow you to choose which field value(s) are used to represent each item on the collection page. For example, with blog posts, it may be ideal to have the hero image, blog title, date, author, etc.
    </td>
  </tr>
  
  <tr>
    <td>
      Manual and Automatic Sorting
    </td>
    
    <td>
      Certain layouts may allow sorting items by value in ascending and descending order, drag-and-drop repositioning of items, etc.
    </td>
  </tr>
</tbody>
</table>

## Table Layout

![Table layout](/img/f801544a-adc8-4194-aee3-d15cf8bddd6a.webp)

This layout displays items in a tabular form, making it compatible with all kinds of items. This is the default
layout used in the content module.

### Layout Options

<table>
<thead>
  <tr>
    <th>
      Control
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
        Spacing
      </strong>
    </td>
    
    <td>
      Adjust the vertical space a row takes up.
    </td>
  </tr>
</tbody>
</table>

### Subheader

<table>
<thead>
  <tr>
    <th>
      Control
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
        Adjust Column Width
      </strong>
    </td>
    
    <td>
      Click and drag the column divider to resize as desired.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Add Field
      </strong>
    </td>
    
    <td>
      Select <icon name="material-symbols:add-circle-outline-rounded">
        
      </icon>
      
       in the page subheader and select the desired Field(s).
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Remove Field
      </strong>
    </td>
    
    <td>
      Select <icon name="material-symbols:arrow-drop-down-circle">
        
      </icon>
      
       in the column title and click <strong>
        "Hide Field"
      </strong>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Sort Items by Column
      </strong>
    </td>
    
    <td>
      Select <icon name="material-symbols:arrow-drop-down-circle">
        
      </icon>
      
       in the column title and sort ascending or descending.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Set Text Alignment
      </strong>
    </td>
    
    <td>
      Select <icon name="material-symbols:arrow-drop-down-circle">
        
      </icon>
      
       in the column title and set left, right, or center.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Toggle & Reorder Columns
      </strong>
    </td>
    
    <td>
      Click the column header, then drag-and-drop as desired.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Select All
      </strong>
    </td>
    
    <td>
      Click <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       in the selection column header.
    </td>
  </tr>
</tbody>
</table>

### Page Area

<table>
<thead>
  <tr>
    <th>
      Control
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
        Select Item(s)
      </strong>
    </td>
    
    <td>
      Click <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       in the selection column for the desired Item(s).
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Manually Sort Items
      </strong>
    </td>
    
    <td>
      Toggle <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       in the configured Sort column to drag and drop <icon name="material-symbols:drag-handle">
        
      </icon>
      
       Items.
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Manual Sorting Requires Configuration**<br />


Only available if you [configure a sort field](/guides/data-model/collections) in the collection's data model
settings.

</callout>

## Card Layout

![Card layout](/img/84b95785-0e36-4630-9fbe-975264837126.webp)

This tiled layout is ideal for collections that prioritize an image. This is the default
for both the user directory and
file library. It includes the following controls.

### Layout Options

<table>
<thead>
  <tr>
    <th>
      Control
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
        Image Source
      </strong>
    </td>
    
    <td>
      Set the field used as the display image.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Title
      </strong>
    </td>
    
    <td>
      Sets a display template to use as a title.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Subtitle
      </strong>
    </td>
    
    <td>
      Sets a display template to use as a subtitle.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Image Fit
      </strong>
    </td>
    
    <td>
      Set how an image fits inside the card.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Fallback Icon
      </strong>
    </td>
    
    <td>
      Set a default icon to display when an item has no image.
    </td>
  </tr>
</tbody>
</table>

### Subheader

<table>
<thead>
  <tr>
    <th>
      Control
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
        Card Size
      </strong>
    </td>
    
    <td>
      Toggle the card size as it appears in the page area.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Order Field
      </strong>
    </td>
    
    <td>
      Click to select the field you wish to order by from the dropdown menu.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Order Direction
      </strong>
    </td>
    
    <td>
      Toggle ascending and descending order.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Select All
      </strong>
    </td>
    
    <td>
      Click  ":icon{name="material-symbols:check-circle"} Select All" in the selection column header.
    </td>
  </tr>
</tbody>
</table>

### Page Area

<table>
<thead>
  <tr>
    <th>
      Control
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
        Select Item(s)
      </strong>
    </td>
    
    <td>
      Click ":icon{name="material-symbols:radio-button-unchecked"} in the selection column for the desired item(s).
    </td>
  </tr>
</tbody>
</table>

## Calendar Layout

![Calendar layout](/img/a967c260-3597-49c5-92d1-0f044ced44c5.webp)

This layout is ideal for collections with time-oriented data (e.g. events and appointments).

### Layout Options

<table>
<thead>
  <tr>
    <th>
      Control
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
        Display Template
      </strong>
    </td>
    
    <td>
      Set a mix of field values and text to represent items on the calendar.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Start Date Field
      </strong>
    </td>
    
    <td>
      Choose field to determine each item's beginning time on the calendar.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        End Date Field
      </strong>
    </td>
    
    <td>
      Choose field to determine each item's ending time on the calendar.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        First Day of The Week
      </strong>
    </td>
    
    <td>
      Defines the beginning of the week on the calendar.
    </td>
  </tr>
</tbody>
</table>

### Subheader

<table>
<thead>
  <tr>
    <th>
      Control
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
        Toggle Month and Year
      </strong>
    </td>
    
    <td>
      Move across time using the chevrons in the subheader.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Today
      </strong>
    </td>
    
    <td>
      Click to jump to the current date on the calendar.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Month Week Day List
      </strong>
    </td>
    
    <td>
      Adjust the time interval used to display items in the page area.
    </td>
  </tr>
</tbody>
</table>

### Page Area

<table>
<thead>
  <tr>
    <th>
      Control
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
        Select Item
      </strong>
    </td>
    
    <td>
      Click an item on the calendar to open its item page.
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Configuration Requirements**<br />


To use this layout, the collection will need at least one datetime [Field](/guides/data-model/fields) to set a start time,
but ideally two datetime Fields (to set a start time and end time).

</callout>

## Map Layout

![Calendar layout](/img/e0835568-a39e-452e-bec2-27bcc114bdd6.webp)

This layout is ideal for collections that emphasize geospatial data. It provides a world map, with items displayed as
points, lines, and other geometry.

### Layout Options

<table>
<thead>
  <tr>
    <th>
      Control
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
        Basemap
      </strong>
    </td>
    
    <td>
      Choose the map provider used for the collection.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Geospatial Field
      </strong>
    </td>
    
    <td>
      Select the geospatial field type to display on screen: <ul>
        <li>
          Map JSON Point: Supports latitude-longitude based, single-point locations.
        </li>
        
        <li>
          Map Geometry: Supports geometric areas such as lines and polygons.
        </li>
      </ul>
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Display Template
      </strong>
    </td>
    
    <td>
      Choose the fields displayed when hovering over an item on the map.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Cluster Nearby Data
      </strong>
    </td>
    
    <td>
      Toggle whether or not nearby items get clustered into a single pin.
    </td>
  </tr>
</tbody>
</table>

### Subheader

There is no Subheader on the Map Layout.

### Page Area

<table>
<thead>
  <tr>
    <th>
      Control
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
        Zoom
      </strong>
    </td>
    
    <td>
      Click <icon name="material-symbols:add">
        
      </icon>
      
       and <icon name="material-symbols:remove">
        
      </icon>
      
       in the upper left hand corner of the page area to zoom in and out.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Find my Location
      </strong>
    </td>
    
    <td>
      Click <icon name="material-symbols:my-location">
        
      </icon>
      
       to zoom into your current location on the map.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Reframe
      </strong>
    </td>
    
    <td>
      Click the square in the upper left-hand corner to resize and reframe the map area.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Select Item
      </strong>
    </td>
    
    <td>
      Click a single item to enter its item page.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Select Items
      </strong>
    </td>
    
    <td>
      Click and drag to select multiple items at once, opening the item page.
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Configuration Requirements**<br />


To use this Layout, the collection must have a map field configured.

</callout>

## Kanban Layout

![Kanban layout](/img/0a02d810-079d-4257-83ec-d4bdd9f28d58.webp)

This layout is ideal for collections that serve as project management tools or to-do lists, where each item represents a
task, because it groups items onto columns according to their status (e.g. "Not Started", "In Progress", "Under
Review", "Complete", or any other status defined).

### Layout Options

<table>
<thead>
  <tr>
    <th>
      Control
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
        Group By
      </strong>
    </td>
    
    <td>
      Select the field used to define item status. See below for details.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Card Title
      </strong>
    </td>
    
    <td>
      Choose the field use to serve as the title for each kanban board.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Card Text
      </strong>
    </td>
    
    <td>
      Choose a field to display additional text on each item.
    </td>
  </tr>
</tbody>
</table>

### Layout Options > Advanced

<table>
<thead>
  <tr>
    <th>
      Control
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
        Card Tags
      </strong>
    </td>
    
    <td>
      Choose a tag field to be displayed on the item.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Card Date
      </strong>
    </td>
    
    <td>
      Choose a datetime field to be displayed on each item.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Card Image
      </strong>
    </td>
    
    <td>
      Choose an image field to be displayed on each item.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Card Image Fit
      </strong>
    </td>
    
    <td>
      Toggle whether the image fit is cropped.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Card User
      </strong>
    </td>
    
    <td>
      Choose the user created field to display their avatar in the bottom right corner.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Show Ungrouped
      </strong>
    </td>
    
    <td>
      Toggle display of a column containing Items with no assigned status.
    </td>
  </tr>
</tbody>
</table>

### Subheader

There is no Subheader for the Kanban Layout.

### Page Area

<table>
<thead>
  <tr>
    <th>
      Control
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
        Create Task and Assign Status
      </strong>
    </td>
    
    <td>
      Click <icon name="material-symbols:add">
        
      </icon>
      
       in a status column and the item page will open.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Sort Panels
      </strong>
    </td>
    
    <td>
      Drag and drop items to reposition or change task status.
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Add Status Panel
      </strong>
    </td>
    
    <td>
      Click <icon name="material-symbols:add-box">
        
      </icon>
      
       and add a group name (i.e. new status column).
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Edit or Delete Status Column
      </strong>
    </td>
    
    <td>
      Click <icon name="material-symbols:more-horiz">
        
      </icon>
      
       and then click <icon name="material-symbols:edit">
        
      </icon>
      
       to edit or <icon name="material-symbols:delete">
        
      </icon>
      
       to delete.
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Configuration Requirements**<br />


To make this layout work, you will need to configure an appropriate status [field](/guides/data-model/fields) on the
collection, then identify this field under "Group By" in the Layout Options menu.

</callout>
