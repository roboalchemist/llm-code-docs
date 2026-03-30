# Source: https://directus.io/docs/raw/guides/content/visual-editor.md

# Visual Editor

> The Directus visual editor module allows you to visually edit the content of your website directly in-place.

<div style="padding:56.33% 0 0 0;position:relative;">
<iframe src="https://player.vimeo.com/video/1068823628?badge=0&autopause=0&player_id=0&app_id=58479" frameBorder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Directus-Visual-Editor-Preview">



</iframe>
</div>

<script src="https://player.vimeo.com/api/player.js">



</script>

Making use of the visual editor requires some effort on the part of web developers through two separate but related aspects. These are the [Frontend Library](/guides/content/visual-editor/frontend-library), and the [Studio Module](/guides/content/visual-editor/studio-module) built into Directus.

The library sets up the connection between your website and your Directus instance. The studio module is then used to render your website within the Directus Studio, make changes in place, and then render those changes as they are made.

The visual editor behaves similarly to Live Preview in that it renders content in an iFrame, but with a few important differences.

<collapsible className="mt-2" name="differences">
<table>
<thead>
  <tr>
    <th>
      
    </th>
    
    <th>
      Live Preview
    </th>
    
    <th>
      Visual Editor
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Entry Point
      </strong>
    </td>
    
    <td>
      Item Form
    </td>
    
    <td>
      Website rendered in Visual Editor module
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Motivation
      </strong>
    </td>
    
    <td>
      Users want to view unpublished data
    </td>
    
    <td>
      Users want to edit elements on their website directly in place and see changes immediately
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Scope
      </strong>
    </td>
    
    <td>
      Limited to editing/viewing a single item of a collection at a time
    </td>
    
    <td>
      Users can navigate through the website freely and edit any linked item on a page without navigating to the applicable collection
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Setup
      </strong>
    </td>
    
    <td>
      Web developers need to implement a preview on their website to ensure that unpublished can be safely viewed
    </td>
    
    <td>
      Web developers need to use the Visual Editing library to connect to the visual editor and set the <code>
        data-directus
      </code>
      
       attribute on the elements they want to be editable
    </td>
  </tr>
</tbody>
</table>
</collapsible>
