# Source: https://directus.io/docs/raw/guides/extensions/app-extensions/interfaces.md

# Source: https://directus.io/docs/raw/guides/data-model/interfaces.md

# Interfaces

> Manage your data effectively with Directus fields. Discover various field types, interfaces, validations, and relationships to perfectly suit your data modeling needs.

Interfaces are how users interact with fields in <product-link product="editor">



</product-link>

. Each interface supports specific data types and configurations.

## Text & Numbers

### Input

![A standard form text input](/img/02d2521b-8e5a-4a2f-8663-729c77f00493.webp)

A standard form input.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        String
      </code>
      
      , <code>
        Text
      </code>
      
      , <code>
        UUID
      </code>
      
      , <code>
        Integer
      </code>
      
      , <code>
        Big Integer
      </code>
      
      , <code>
        Float
      </code>
      
      , <code>
        Decimal
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Length
    </td>
    
    <td>
      Used to limit number of characters in the database.
    </td>
  </tr>
  
  <tr>
    <td>
      Soft Limit
    </td>
    
    <td>
      Used to limit the number of characters within the Data Studio.
    </td>
  </tr>
  
  <tr>
    <td>
      Trim
    </td>
    
    <td>
      Toggle to trim whitespace at start and end of the value.
    </td>
  </tr>
  
  <tr>
    <td>
      Masked
    </td>
    
    <td>
      Toggle to hide the typed value with • values.
    </td>
  </tr>
  
  <tr>
    <td>
      Cleared Value
    </td>
    
    <td>
      Toggle to save cleared value as an empty string.
    </td>
  </tr>
  
  <tr>
    <td>
      Slugify
    </td>
    
    <td>
      Toggle to make the entered value URL safe.
    </td>
  </tr>
</tbody>
</table>

### Autocomplete Input (API)

![An autocomplete form text input that shows a dropdown list of options based on a search query](/img/02d2521b-8e5a-4a2f-8663-729c77f00493.webp)

A search input that will populate dropdown choices by making a request to a given URL.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        String
      </code>
      
      , <code>
        Text
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      URL
    </td>
    
    <td>
      The request URL with dynamic <code>
        {{ value }}
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      Results Path
    </td>
    
    <td>
      The returned object path using dot notation containing an array with search results.
    </td>
  </tr>
  
  <tr>
    <td>
      Text Path
    </td>
    
    <td>
      The value within each object that displays for each search result.
    </td>
  </tr>
  
  <tr>
    <td>
      Value Path
    </td>
    
    <td>
      The value within each object that is stored for each search result.
    </td>
  </tr>
  
  <tr>
    <td>
      Trigger
    </td>
    
    <td>
      Select between <code>
        throttle
      </code>
      
       and <code>
        debounce
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      Rate
    </td>
    
    <td>
      The delay in <code>
        milliseconds
      </code>
      
       used for the trigger.
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Throttle vs Debounce**
Throttle and debounce are very similar. Debounce will wait until a period of 'silence' has happened before making the request, while throttle will keep making requests at most 1 call every period. Period is set in the 'rate' configuration for this interface.

</callout>

### Block Editor

![Showcase of the block editor with example blocks](/img/0344b52f-aa52-4a57-9f8c-2a9c4fa0b10e.webp)

Allows users to create and edit content using blocks. These blocks represent individual pieces of content, such as text,
images, videos, buttons, and more, that can be assembled and re-arranged within a flexible layout.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        JSON
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Toolbar
    </td>
    
    <td>
      Allows for customization of visible formatting options.
    </td>
  </tr>
  
  <tr>
    <td>
      Root Folder
    </td>
    
    <td>
      Default folder to store uploaded files. Does not affect existing files.
    </td>
  </tr>
</tbody>
</table>

### Code

![A code editor input](/img/a07b7361-671f-48ca-944f-acefa2bbe1e1.webp)

Code editor for pre-formatted text.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        String
      </code>
      
      , <code>
        Text
      </code>
      
      , <code>
        JSON
      </code>
      
      , <code>
        Geometry (All)
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Language
    </td>
    
    <td>
      Language for syntax highlighting. Can be set when type is not <code>
        JSON
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      Line Number
    </td>
    
    <td>
      Toggle to show line numbers.
    </td>
  </tr>
  
  <tr>
    <td>
      Line Wrapping
    </td>
    
    <td>
      Toggle to wrap text to prevent horizontal scrolling.
    </td>
  </tr>
  
  <tr>
    <td>
      Template
    </td>
    
    <td>
      Preset value that the user can add to the field value by clicking "Fill with Template Value".
    </td>
  </tr>
</tbody>
</table>

### Textarea

![A standard form textarea input](/img/1b66cfc0-785d-40ed-adf3-9ce90441142b.webp)

Textarea input for longer plain text.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Text
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Soft Limit
    </td>
    
    <td>
      Used to limit the number of characters within the Data Studio.
    </td>
  </tr>
</tbody>
</table>

### WYSIWYG

![A What You See Is What You Get (WYSIWYG) form input that has a toolbar for formatting](/img/262f71a7-8cc8-4402-85b9-b80dbc2a60ba.webp)

The What You See Is What You Get (WYSIWYG) editor provides a text area with rich formatting options in the toolbar.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Text
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Toolbar
    </td>
    
    <td>
      Allows for customization of visible formatting options
    </td>
  </tr>
  
  <tr>
    <td>
      Folder
    </td>
    
    <td>
      Default folder to store uploaded files. Does not affect existing files.
    </td>
  </tr>
  
  <tr>
    <td>
      Soft Limit
    </td>
    
    <td>
      Used to limit the number of characters within the Data Studio.
    </td>
  </tr>
  
  <tr>
    <td>
      Static Access Token
    </td>
    
    <td>
      Token appended to asset URLs when displaying in the editor.
    </td>
  </tr>
  
  <tr>
    <td>
      Custom Formats
    </td>
    
    <td>
      JSON array of formatting that is passed to the <code>
        style_formats
      </code>
      
       config option of the WYSIWYG editor instance. <a href="https://www.tiny.cloud/docs/demo/format-custom/" rel="nofollow">
        TinyMCE Documentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      Options Override
    </td>
    
    <td>
      JSON object to override the default config option of the WYSIWYG editor instance. <a href="https://www.tiny.cloud/docs/configure/" rel="nofollow">
        TinyMCE Documentation
      </a>
    </td>
  </tr>
</tbody>
</table>

### Markdown

![A markdown text editor with a toolbar with formatting options. Edit and preview tabs.](/img/b41d6822-35ab-48db-ada9-dd3a723a5c52.webp)

Markdown text editor with formatting options in the toolbar. You can switch between Edit and Preview modes.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Text
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Toolbar
    </td>
    
    <td>
      Allows for customization of visible formatting options.
    </td>
  </tr>
  
  <tr>
    <td>
      Root Folder
    </td>
    
    <td>
      Default folder to store uploaded files. Does not affect existing files.
    </td>
  </tr>
  
  <tr>
    <td>
      Static Access Token
    </td>
    
    <td>
      Token appended to asset URLs when displaying in the editor.
    </td>
  </tr>
  
  <tr>
    <td>
      Soft Limit
    </td>
    
    <td>
      Used to limit the number of characters within the Data Studio.
    </td>
  </tr>
  
  <tr>
    <td>
      Custom Blocks
    </td>
    
    <td>
      Each block adds an icon to the toolbar, and wraps the cursor in specific characters.
    </td>
  </tr>
</tbody>
</table>

### Tags

![A standard form text input where user can select, add, and remove tags.](/img/510231f2-4336-4071-bf41-7c9d4193cca3.webp)

A text input that allows users to apply any number of tags. When adding new tag, press Enter to save the tag. To remove an existing tag simply click on the tag under the input.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        JSON
      </code>
      
      , <code>
        CSV
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Presets
    </td>
    
    <td>
      Preset tags that the user can select.
    </td>
  </tr>
  
  <tr>
    <td>
      Alphabetize
    </td>
    
    <td>
      Toggle to force tags to display in alphabetical order.
    </td>
  </tr>
  
  <tr>
    <td>
      Allow Other
    </td>
    
    <td>
      Toggle to allow users to add new tags.
    </td>
  </tr>
  
  <tr>
    <td>
      Whitespace
    </td>
    
    <td>
      Force whitespace to be removed or replaced with hyphens or underscores.
    </td>
  </tr>
  
  <tr>
    <td>
      Capitalization
    </td>
    
    <td>
      Force tags to be stored as lowercase, uppercase, or title case.
    </td>
  </tr>
</tbody>
</table>

## Selection

### Toggle

![A toggle form input with label named "Enabled"](/img/532c82dd-c851-4874-b596-597421dfc3cd.webp)

A checkbox input that allows user to toggle boolean values.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Boolean
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Default Value
    </td>
    
    <td>
      <code>
        true
      </code>
      
      , <code>
        false
      </code>
      
      , <code>
        null
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Icon On
    </td>
    
    <td>
      Icon that shows whenever the toggle is enabled.
    </td>
  </tr>
  
  <tr>
    <td>
      Icon Off
    </td>
    
    <td>
      Icon that shows whenever the toggle is disabled.
    </td>
  </tr>
  
  <tr>
    <td>
      Color On
    </td>
    
    <td>
      Color of the icon whenever the toggle is enabled.
    </td>
  </tr>
  
  <tr>
    <td>
      Color Off
    </td>
    
    <td>
      Color of the icon whenever the toggle is disabled.
    </td>
  </tr>
  
  <tr>
    <td>
      Label
    </td>
    
    <td>
      The text displayed to the user beside the toggle.
    </td>
  </tr>
</tbody>
</table>

### Datetime

![A date picker input. User can select a calendar date and input a time. ](/img/b5ba6fb2-0e24-408a-b4c5-78c898558293.webp)

Date picker input that allows user to select a date and time.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        DateTime
      </code>
      
      , <code>
        Date
      </code>
      
      , <code>
        Time
      </code>
      
      , <code>
        Timestamp
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Include Seconds
    </td>
    
    <td>
      Show seconds in the interface.
    </td>
  </tr>
  
  <tr>
    <td>
      Use 24-Hour Format
    </td>
    
    <td>
      Use 24 hour time system.
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Handling Timezones**

- `Timestamp` normalizes values to UTC and returns them in ISO 8601 format with the `Z` suffix (e.g. 2024-01-15T09:00:00.000Z).
- `DateTime` stores values without timezone information and returns them in ISO 8601 format (e.g. 2024-01-15T10:00:00). The stored value depends on the database vendor's format and database timezone, while the returned value is dependent on the server's `TZ` environment variable.

System fields `date_created` and `date_updated` use `Timestamp`.

</callout>

### Repeater

![A repeater field](/img/7bc91592-707a-4e61-8eca-667a1ecf8e8f.webp)

![A repeater field, open](/img/f2675394-689a-485f-9627-39992a97c30d.webp)

A repeating group of fields. You can use any field in a repeater, except for relational, presentation, or group fields. The value is stored as a JSON array of objects.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        JSON
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Template
    </td>
    
    <td>
      Label shown in the repeater items using display templates. Defaults to <code>
        {{ title }}
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      "Create New" Label
    </td>
    
    <td>
      Label for the button to create a new item below the field in the editor. Defaults to "Create New".
    </td>
  </tr>
  
  <tr>
    <td>
      Sort
    </td>
    
    <td>
      Method of sorting the items groups within the repeater.
    </td>
  </tr>
  
  <tr>
    <td>
      Edit Fields
    </td>
    
    <td>
      The configuration for fields within the repeater.
    </td>
  </tr>
</tbody>
</table>

Each field in a repeater has further configuration options.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Field
    </td>
    
    <td>
      Unique name for the field - used as the property key and in the repeater's <code>
        template
      </code>
      
       option.
    </td>
  </tr>
  
  <tr>
    <td>
      Type
    </td>
    
    <td>
      Data type of property values.
    </td>
  </tr>
  
  <tr>
    <td>
      Interface
    </td>
    
    <td>
      The interface to use for the field.
    </td>
  </tr>
  
  <tr>
    <td>
      Interface Options
    </td>
    
    <td>
      Option configuration for the selected interface.
    </td>
  </tr>
  
  <tr>
    <td>
      Display
    </td>
    
    <td>
      The display to use for the preview on each item.
    </td>
  </tr>
</tbody>
</table>

### Map

![An interactive map interface that shows a single point on the east coast of the United States. Map has buttons for zoom, search, and full screen.](/img/e8d96531-7a23-4516-af4d-4180b778ef84.webp)

Show and set geospatial data on an interactive map. Mapping data is stored as [GeoJSON](https://geojson.org/).

<callout icon="material-symbols:info-outline">

**Maps Provider**
By default, Directus will use [OpenStreetMap](https://www.openstreetmap.org) to display your mapping data.

[By entering a Mapbox API key](/configuration/general#mapbox), you can enhance the platform's mapping experience.

</callout>

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <ul>
        <li>
          <strong>
            <code>
              Point
            </code>
          </strong>
          
          : A single location on a map.
        </li>
        
         <li>
          <strong>
            <code>
              LineString
            </code>
          </strong>
          
          : A series of points on a map connected in a line.
        </li>
        
         <li>
          <strong>
            <code>
              Polygon
            </code>
          </strong>
          
          : An area of a map drawn by selecting vertices.
        </li>
        
         <li>
          <strong>
            <code>
              Multipoint
            </code>
          </strong>
          
          : A series of disconnected points on a map.
        </li>
        
         <li>
          <strong>
            <code>
              MultiLineString
            </code>
          </strong>
          
          : A series of <code>LineString</code> objects.
        </li>
        
         <li>
          <strong>
            <code>
              MultiPolygon
            </code>
          </strong>
          
          : A series of <code>Polygon</code> objects.
        </li>
        
         <li>
          <strong>
            <code>
              Geometry (All)
            </code>
          </strong>
          
          : An series of <code>Point</code>, <code>LineString</code> and <code>Polygon</code> objects.
        </li>
        
         <li>
          <strong>
            <code>
              JSON
            </code>
          </strong>
          
          : A <code>Geometry (All)</code> object stored as JSON.
        </li>
        
         <li>
          <strong>
            <code>
              String
            </code>
          </strong>
          
          : A <code>Geometry (All)</code> object stored a string of characters.
        </li>
        
         <li>
          <strong>
            <code>
              Text
            </code>
          </strong>
          
          : A <code>Geometry (All)</code> object stored as Text.
        </li>
        
         <li>
          <strong>
            <code>
              CSV
            </code>
          </strong>
          
          : A <code>Geometry (All)</code> object stored as comma-separated values.
        </li>
      </ul>
    </td>
  </tr>
  
  <tr>
    <td>
      Default View
    </td>
    
    <td>
      The default location and zoom settings on the map to show by default
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Database Support**
Your database must support geospatial data or have a geospatial plugin installed, such as PostGIS or SpatiaLite, to fully utilize mapping functionality with Directus.

</callout>

### Color

![A text input for color hex codes that allows user to select color modes ](/img/6429c983-5a72-4e77-aa8e-df816a0348d0.webp)

A color picker interface that allows users to input color codes and convert between different color modes.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        String
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Opacity
    </td>
    
    <td>
      Enable opacity values to be adjusted by the user.
    </td>
  </tr>
  
  <tr>
    <td>
      Preset Colors
    </td>
    
    <td>
      Preset colors that users can select.
    </td>
  </tr>
</tbody>
</table>

### Dropdown

![A select input with a dropdown of options.](/img/370efb9d-83de-4830-a33c-7de3a2e6e246.webp)

Input that allows the user to select a value from a dropdown list of options.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        String
      </code>
      
      , <code>
        Integer
      </code>
      
      , <code>
        Big Integer
      </code>
      
      , <code>
        Float
      </code>
      
      , <code>
        Decimal
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Choices
    </td>
    
    <td>
      Options for the dropdown. Each option contains text that is displayed to the user and a value that is stored.
    </td>
  </tr>
  
  <tr>
    <td>
      Allow Other
    </td>
    
    <td>
      Allow user to enter custom values other than preset values.
    </td>
  </tr>
  
  <tr>
    <td>
      Allow None
    </td>
    
    <td>
      Allow user to deselect an option.
    </td>
  </tr>
</tbody>
</table>

### Dropdown (Multiple)

![A select input where user can select multiple options from a dropdown.](/img/888f1cb3-b88c-4fd4-b7cf-c8c7b4ddbf9a.webp)

Input that allows user to select multiple values from a list of options.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        JSON
      </code>
      
      , <code>
        CSV
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Choices
    </td>
    
    <td>
      Options for the dropdown. Each option contains text that is displayed to the user and a value that is stored.
    </td>
  </tr>
  
  <tr>
    <td>
      Allow Other
    </td>
    
    <td>
      Allow user to enter custom values other than preset values.
    </td>
  </tr>
  
  <tr>
    <td>
      Allow None
    </td>
    
    <td>
      Allow user to deselect an option.
    </td>
  </tr>
</tbody>
</table>

### Icon

![A select input with a dropdown grid of icon choices.](/img/e33d72e2-2f3c-4c18-8446-b40d07ecc1b8.webp)

Allow the user to select from a list of icons. Icons are from the [Google Material Symbols](https://fonts.google.com/icons) library and cannot be swapped for another library.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        String
      </code>
    </td>
  </tr>
</tbody>
</table>

### Checkboxes

![A form input with multiple checkboxes.](/img/7a7d6ff7-8931-4a44-8ccf-1f3a7d0f04d1.webp)

Input that allows user to select multiple checkboxes.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        JSON
      </code>
      
      , <code>
        CSV
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Choices
    </td>
    
    <td>
      Options for the checkboxes. Each option contains text that is displayed to the user and a value that is stored.
    </td>
  </tr>
  
  <tr>
    <td>
      Allow Other
    </td>
    
    <td>
      Allow user to enter custom values other than preset values.
    </td>
  </tr>
  
  <tr>
    <td>
      Color
    </td>
    
    <td>
      Color of the checkboxes.
    </td>
  </tr>
  
  <tr>
    <td>
      Icon On/Off
    </td>
    
    <td>
      Icons shown whenever a checkbox is checked/unchecked.
    </td>
  </tr>
  
  <tr>
    <td>
      Items Shown
    </td>
    
    <td>
      Number of checkboxes before a 'Show More' toggle is shown.
    </td>
  </tr>
</tbody>
</table>

### Checkboxes (Tree)

![A form input with a nested tree of multiple parent and child checkboxes.](/img/3a4950bb-da45-4814-95a6-eff7ae14fab8.webp)

Nested tree of checkboxes that can be expanded or collapsed.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        JSON
      </code>
      
      , <code>
        CSV
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Choices
    </td>
    
    <td>
      Options for the checkboxes. Each option contains text that is displayed to the user and a value that is stored, along with any child options.
    </td>
  </tr>
  
  <tr>
    <td>
      Choice Children
    </td>
    
    <td>
      Child checkboxes nested below the current choice.
    </td>
  </tr>
  
  <tr>
    <td>
      Value Combining
    </td>
    
    <td>
      Controls what value is stored when nested selections are made. <code>
        All
      </code>
      
      , <code>
        Branch
      </code>
      
      , <code>
        Leaf
      </code>
      
      , <code>
        Indeterminate
      </code>
      
      , <code>
        Exclusive
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Understanding Value Combining Options**
In a Checkboxes (Tree) interface, checkboxes can exist within a parent checkbox. Value combining determines the final value when selecting items in a tree.

- `All` returns all checked values.
<collapsible className="mt-2" name="examples">
<table>
<thead>
  <tr>
    <th>
      Selection
    </th>
    
    <th>
      Final Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [child1]
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [child1, child2, parent]
      </code>
    </td>
  </tr>
</tbody>
</table>
</collapsible>
- `Branch` returns the top-most values that are selected.
<collapsible className="mt-2" name="examples">
<table>
<thead>
  <tr>
    <th>
      Selection
    </th>
    
    <th>
      Final Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [child1]
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [parent]
      </code>
    </td>
  </tr>
</tbody>
</table>
</collapsible>
- `Leaf` returns the deepest values that are selected
<collapsible className="mt-2" name="examples">
<table>
<thead>
  <tr>
    <th>
      Selection
    </th>
    
    <th>
      Final Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [child1]
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [child1, child2]
      </code>
    </td>
  </tr>
</tbody>
</table>
</collapsible>
- `Indeterminate` returns checked items, and always returns a parent when one or more children are selected.
<collapsible className="mt-2" name="examples">
<table>
<thead>
  <tr>
    <th>
      Selection
    </th>
    
    <th>
      Final Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [child1, parent]
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [child1, child2, parent]
      </code>
    </td>
  </tr>
</tbody>
</table>
</collapsible>
- `Exclusive` returns either the parent or child elements, but not both.
<collapsible className="mt-2" name="examples">
<table>
<thead>
  <tr>
    <th>
      Selection
    </th>
    
    <th>
      Final Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [parent]
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [child1]
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <icon name="material-symbols:check-box-outline">
        
      </icon>
      
       <code>
        parent
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child1
      </code>
      
      <br />
      
        <icon name="material-symbols:check-box">
        
      </icon>
      
       <code>
        child2
      </code>
    </td>
    
    <td>
      <code>
        [child1, child2]
      </code>
    </td>
  </tr>
</tbody>
</table>
</collapsible>
</callout>

### Radio Buttons

![A radio button form input with different options to select](/img/d9cb554c-d24b-44b5-a0a1-f28187542f34.webp)

Radio button input that allows users to select a single value from multiple choices.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        String
      </code>
      
      , <code>
        Integer
      </code>
      
      , <code>
        Big Integer
      </code>
      
      , <code>
        Float
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Choices
    </td>
    
    <td>
      Options for the radio buttons. Each option contains text that is displayed to the user and a value that is stored.
    </td>
  </tr>
  
  <tr>
    <td>
      Allow Other
    </td>
    
    <td>
      Allow user to enter custom values other than preset values.
    </td>
  </tr>
</tbody>
</table>

## Relational

### File

![A file type form input where user can pick from three options: "Upload File From Device", "Choose Files from Library", "Import File from URL"](/img/b7582b34-f741-48e4-9095-64b2d0995cdf.webp)

Upload a single file of any mime-type, choose an existing file from the [file library](/guides/files/manage), or import a file from a URL.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        UUID
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Root Folder
    </td>
    
    <td>
      Folder for the uploaded files. Does not affect the location of existing files.
    </td>
  </tr>
  
  <tr>
    <td>
      Allowed MIME Types
    </td>
    
    <td>
      File type extensions allowed by this interface. Will not override global FILES_MIME_TYPE_ALLOW_LIST defined in your env.
    </td>
  </tr>
</tbody>
</table>

### Image

![An image form input where user can pick from three options: "Upload File From Device", "Choose Files from Library", "Import File from URL"](/img/b673b63d-75e0-4763-96fb-47263da2193a.webp)

Upload a single image file, choose an existing image from the [file library](/guides/files/manage), or import an image from a URL.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        UUID
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Root Folder
    </td>
    
    <td>
      Folder for the uploaded files. Does not affect the location of existing files.
    </td>
  </tr>
  
  <tr>
    <td>
      Crop to Fit
    </td>
    
    <td>
      Crop the image as needed when displaying the image.
    </td>
  </tr>
</tbody>
</table>

### Files

![A file type form input where user can select and upload multiple files.](/img/aaca7ac1-ae3d-458b-8b5b-e4747a236cf0.webp)

Upload multiple files, choose existing files from the [file library](/guides/files/manage), or import files from URL.

When this field is added to a collection, Directus will create a Many to Many (M2M) junction collection on your behalf.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Alias
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Folder
    </td>
    
    <td>
      Folder for the uploaded files. Does not affect the location of existing files.
    </td>
  </tr>
  
  <tr>
    <td>
      Display Template
    </td>
    
    <td>
      Display templates are used to represent an item in relationship fields - for example to show the value of the <code>
        Title
      </code>
      
       field.
    </td>
  </tr>
  
  <tr>
    <td>
      Allowed MIME Types
    </td>
    
    <td>
      File type extensions allowed by this interface. Will not override global FILES_MIME_TYPE_ALLOW_LIST defined in your env.
    </td>
  </tr>
</tbody>
</table>

### Builder (M2A)

![A form interface that allows users to create a relationship from the current item by selecting different items from multiple, distinct Collections.](/img/df84bd0b-cdba-4920-bc3c-493928b763a7.webp)

Create relationships between the current item and multiple items from any number of other collections in a many-to-any (M2A) interface.

When this field is added to a collection, Directus will create a Many to Many (M2M) junction collection on your behalf.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Alias
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Related Collections
    </td>
    
    <td>
      Which collections should items be selected from.
    </td>
  </tr>
  
  <tr>
    <td>
      Allow Duplicates
    </td>
    
    <td>
      Allow users to add the same Item multiple times.
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:school-outline" color="secondary" to="/tutorials/getting-started/create-reusable-blocks-with-many-to-any-relationships">

Read our tutorial on using a Builder (M2A) to create reusable page components.

</callout>

### Many To Many

![A form interface that allows users to select multiple different items from a single collection. Buttons for "Create New" and "Add Existing".](/img/010f9c29-a4b1-4463-bc72-7106f41ef4a8.webp)

Create relationships between the current item and many different items from a single collection.

When this field is added to a collection, Directus will create a Many to Many (M2M) junction collection on your behalf.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Alias
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Related Collection
    </td>
    
    <td>
      Which collection should items be selected from.
    </td>
  </tr>
  
  <tr>
    <td>
      Layout
    </td>
    
    <td>
      How to present items in the editor. <code>
        List
      </code>
      
      , <code>
        Table
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Junction Fields Location
    </td>
    
    <td>
      Where in the editor the relational field should be added. <code>
        Top
      </code>
      
      , <code>
        Bottom
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Allow Duplicates
    </td>
    
    <td>
      Allow users to add the same Item multiple times.
    </td>
  </tr>
  
  <tr>
    <td>
      Filter
    </td>
    
    <td>
      Filter the list of items a user can select.
    </td>
  </tr>
  
  <tr>
    <td>
      Item link
    </td>
    
    <td>
      Toggle visible link to the item.
    </td>
  </tr>
</tbody>
</table>

### One to Many

![A form interface that allows users to select multiple items from a single collection. Buttons for "Create New" and "Add Existing".](/img/63dcee0a-9ee7-4328-bd6b-bd85cc4660c9.webp)

Create a relationship between the current item and many items from a single collection.

When this field is added to a collection, Directus will create a corresponding Many to One field on the related collection on your behalf.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Alias
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Related Collection
    </td>
    
    <td>
      Which collection should items be selected from.
    </td>
  </tr>
  
  <tr>
    <td>
      Foreign Key
    </td>
    
    <td>
      Name of field in related collection to be created.
    </td>
  </tr>
  
  <tr>
    <td>
      Layout
    </td>
    
    <td>
      How to present items in the editor. <code>
        List
      </code>
      
      , <code>
        Table
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Display Template
    </td>
    
    <td>
      Display templates are used to represent an item in relationship fields - for example to show the value of the <code>
        Title
      </code>
      
       field.
    </td>
  </tr>
  
  <tr>
    <td>
      Filter
    </td>
    
    <td>
      Filter the list of items a user can select.
    </td>
  </tr>
  
  <tr>
    <td>
      Item link
    </td>
    
    <td>
      Toggle visible link to the item.
    </td>
  </tr>
</tbody>
</table>

### Tree View

![A form interface that shows multiple parent and child items from the same collection. Buttons for "Create New" and "Add Existing".](/img/aa6b991e-7c5b-459d-ae9a-7e3f7ffc4fb1.webp)

A special One to Many interface that allows users to create and manage recursive relationships between items from the same collection.

The Tree View interface is only available on self-referencing (recursive) relationships.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Alias
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Related Collection
    </td>
    
    <td>
      Which collection should items be selected from.
    </td>
  </tr>
  
  <tr>
    <td>
      Foreign Key
    </td>
    
    <td>
      Name of field in related collection to be created.
    </td>
  </tr>
  
  <tr>
    <td>
      Display Template
    </td>
    
    <td>
      Display templates are used to represent an item in relationship fields - for example to show the value of the <code>
        Title
      </code>
      
       field.
    </td>
  </tr>
  
  <tr>
    <td>
      Filter
    </td>
    
    <td>
      Filter the list of items a user can select.
    </td>
  </tr>
</tbody>
</table>

### Many to One

![A form interface that allows a user to select a single item from a collection."](/img/202ad6d5-b5cd-4592-a9b7-f26c79702fae.webp)

Create a relationship between the current item and a single item from single collection.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Alias
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Related Collection
    </td>
    
    <td>
      Which collection should items be selected from.
    </td>
  </tr>
  
  <tr>
    <td>
      Display Template
    </td>
    
    <td>
      Display templates are used to represent an item in relationship fields - for example to show the value of the <code>
        Title
      </code>
      
       field.
    </td>
  </tr>
  
  <tr>
    <td>
      Filter
    </td>
    
    <td>
      Filter the list of items a user can select.
    </td>
  </tr>
</tbody>
</table>

### Translations

![A form interface with two columns and two fields per column - "Title" and "Content". One column contains the English translation for each field. Second column contains the French translation for each field.](/img/6641341c-c9ba-483e-bd6f-17d8275abb21.webp)

Special relational interface designed specifically to handle translations. When this field is added to a collection a Languages Collection will be created by Directus on your behalf if it does not already exist.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Alias
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Languages Collection
    </td>
    
    <td>
      Which collection to use for language selection.
    </td>
  </tr>
  
  <tr>
    <td>
      Language Indicator Field
    </td>
    
    <td>
      The field from your <code>
        languages
      </code>
      
       collection that identifies the language to the user.
    </td>
  </tr>
  
  <tr>
    <td>
      Language Direction Field
    </td>
    
    <td>
      The field from your <code>
        languages
      </code>
      
       collection that identifies the text direction for a selected language.
    </td>
  </tr>
  
  <tr>
    <td>
      Default Language
    </td>
    
    <td>
      Default language to use.
    </td>
  </tr>
  
  <tr>
    <td>
      Use Current User Language
    </td>
    
    <td>
      Default to the current users language.
    </td>
  </tr>
</tbody>
</table>

## Presentation

### Header

![header interface showing help text and action buttons](/img/header-interface.png)

A configurable header section that provides rich page headers with titles, subtitles, contextual help information and intertactive action buttons within collections. Can be positioned anywhere in the form layout to guide users and provide quick access to relevant actions.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Title
    </td>
    
    <td>
      Title text displayed at the top of the header section.
    </td>
  </tr>
  
  <tr>
    <td>
      Icon
    </td>
    
    <td>
      Icon displayed beside the button label.
    </td>
  </tr>
  
  <tr>
    <td>
      Color
    </td>
    
    <td>
      Color of the icon displayed when using an icon.
    </td>
  </tr>
  
  <tr>
    <td>
      Subtitle
    </td>
    
    <td>
      Optional subtitle text displayed below the title for additional context. Note this can contain dynamic values.
    </td>
  </tr>
  
  <tr>
    <td>
      Help
    </td>
    
    <td>
      Rich text content providing contextual guidance to users. Supports formatting, images, and can be translated.
    </td>
  </tr>
  
  <tr>
    <td>
      Help Display
    </td>
    
    <td>
      Controls how help content is displayed. Options may include inline, collapsible, or modal views.
    </td>
  </tr>
  
  <tr>
    <td>
      Enable Help Translations
    </td>
    
    <td>
      Toggle to enable multilingual support for the help content.
    </td>
  </tr>
  
  <tr>
    <td>
      Links
    </td>
    
    <td>
      Configure action buttons/links. Each can trigger a flow or open a URL, with customizable labels, icons, and button types.
    </td>
  </tr>
</tbody>
</table>

### Divider

![A horizontal divider between two form fields](/img/7eb81773-59d7-46cb-95cd-6b50d8ef4bdf.webp)

A horizontal divider to separate fields into different sections.

### Button Links

![A group of two buttons. One primary button. One default button.](/img/c88411d7-c4a9-44e8-8a55-78e84de7dbd2.webp)

Group of one or more buttons that can trigger a manual flow, or hyperlink to a preset or dynamic URL. Each button link has the following configuration:

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Label
    </td>
    
    <td>
      Label for the button.
    </td>
  </tr>
  
  <tr>
    <td>
      Icon
    </td>
    
    <td>
      Icon displayed beside the button label.
    </td>
  </tr>
  
  <tr>
    <td>
      Type
    </td>
    
    <td>
      The colors used by the button. <code>
        Primary
      </code>
      
      , <code>
        Normal
      </code>
      
      , <code>
        Info
      </code>
      
      , <code>
        Success
      </code>
      
      , <code>
        Warning
      </code>
      
      , <code>
        Danger
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Action Type
    </td>
    
    <td>
      Toggles whether the button will be used to run a flow, or open a hyperlink.
    </td>
  </tr>
  
  <tr>
    <td>
      URL
    </td>
    
    <td>
      URL to send the user to when the button is clicked. You can use field values from the item to create the URL dynamically.
    </td>
  </tr>
  
  <tr>
    <td>
      Flow
    </td>
    
    <td>
      Flow to be run when the button is clicked. The flow must have a manual trigger and be configured for the relevant collection.
    </td>
  </tr>
</tbody>
</table>

### Notice

![A standard warning notice in yellow with a hazard icon.](/img/eff79b29-a12a-46b3-b01a-a0a329064f76.webp)

An alert or notice interface to notify users of important information.

## Groups

### Accordion

![An accordion interface that allows use to expand and collapse different fields.](/img/774bc56b-adb5-44a2-8e65-69e770321977.webp)

User-controlled showing and hiding of fields within the group by clicking on each field.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Accordion Mode
    </td>
    
    <td>
      Toggle whether only one section can be open at a time.
    </td>
  </tr>
  
  <tr>
    <td>
      Start
    </td>
    
    <td>
      <code>
        All Closed
      </code>
      
      , <code>
        First Opened
      </code>
    </td>
  </tr>
</tbody>
</table>

### Detail Group

![A group of form fields that are currently hidden behind a toggle.](/img/f1d62298-5cce-41b5-9655-1014b97a6aac.webp)

![A group of form fields that are currently visible but can be hidden behind a toggle.](/img/9eec605f-af7b-4c39-a65a-73ad7440ed0b.webp)

User-controlled showing and hiding of sub-groups by clicking on the group header.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Alias
      </code>
    </td>
  </tr>
</tbody>
</table>

### Raw Group

![A group of form fields](/img/d03eef30-f983-4efb-aac3-ebf120294516.webp)

Interface that groups multiple fields together in the data model, with no visual distinction.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Alias
      </code>
    </td>
  </tr>
</tbody>
</table>

## Other

### Collection Item Dropdown

![A collection item field](/img/89863252-f709-4ddb-97b6-d298b01b05e5.webp)

Dropdown to select an item from an existing collection.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        JSON
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Collection
    </td>
    
    <td>
      Which collection should the item be selected from.
    </td>
  </tr>
  
  <tr>
    <td>
      Display Template
    </td>
    
    <td>
      Display templates are used to represent an item in relationship fields - for example to show the value of the <code>
        Title
      </code>
      
       field.
    </td>
  </tr>
  
  <tr>
    <td>
      Filter
    </td>
    
    <td>
      Filter the list of items a user can select.
    </td>
  </tr>
</tbody>
</table>

### Collection Item Dropdown (Multiple)

![A collection multiple item field](/img/b2cfb9dc-d9f2-4edf-a014-1ec1e8e7102e.webp)

Dropdown to select multiple items from an existing collection.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        JSON
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Collection
    </td>
    
    <td>
      Which collection should the items be selected from.
    </td>
  </tr>
  
  <tr>
    <td>
      Display Template
    </td>
    
    <td>
      Display templates are used to represent an item in relationship fields - for example to show the value of the <code>
        Title
      </code>
      
       field.
    </td>
  </tr>
  
  <tr>
    <td>
      Filter
    </td>
    
    <td>
      Filter the list of items a user can select.
    </td>
  </tr>
</tbody>
</table>

### Hash

![Form text input that shows the value is securely hashed.](/img/6b62272a-8a1e-4bed-be6d-3cf614bb2f48.webp)

Text input that allows users to hash the value on save. The Directus APIs can be used to [verify the hash](/api/utilities#verify-a-hash).

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Hash
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Masked
    </td>
    
    <td>
      Toggle raw value visibility before save.
    </td>
  </tr>
</tbody>
</table>

### Slider

![A slider input](/img/4fd92002-5f86-4e61-91f9-1169df4d6268.webp)

Range input that allows users to select a number with an interactive slider.

<table>
<thead>
  <tr>
    <th>
      Configuration
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Types
    </td>
    
    <td>
      <code>
        Integer
      </code>
      
      , <code>
        Decimal
      </code>
      
      , <code>
        Big Integer
      </code>
      
      , <code>
        Float
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Minimum Value
    </td>
    
    <td>
      Minimum value that can be set by the user.
    </td>
  </tr>
  
  <tr>
    <td>
      Maximum Value
    </td>
    
    <td>
      Maximum value that can be set by the user.
    </td>
  </tr>
  
  <tr>
    <td>
      Step Interval
    </td>
    
    <td>
      Specify the size of each increment (or step) of the slider control.
    </td>
  </tr>
  
  <tr>
    <td>
      Always show value
    </td>
    
    <td>
      Toggle visibility of the numeric value below the slider.
    </td>
  </tr>
</tbody>
</table>
