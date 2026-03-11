# Source: https://directus.io/docs/raw/guides/ai/mcp/local-mcp/tools.md

# Source: https://directus.io/docs/raw/guides/ai/mcp/tools.md

# Source: https://directus.io/docs/raw/guides/ai/assistant/tools.md

# Tools

> Reference of all tools available to AI Assistant for interacting with your Directus instance.

AI Assistant uses tools to perform actions on your behalf. Each tool handles a specific type of operation within Directus.

<callout color="info" icon="material-symbols:security">

**Tools use your existing user permissions.** Users without admin access won't see Admin Only tools. If you can't access a collection or perform an action in Directus, the AI can't either.

</callout>

## System Tools

These tools interact with your Directus instance via API to manage content, files, and schema.

<table>
<thead>
  <tr>
    <th>
      Tool
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:database-search-outline">
        
      </icon>
      
       <strong>
        Schema
      </strong>
    </td>
    
    <td>
      Explore collections, fields, and relationships (read-only)
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:box-outline">
        
      </icon>
      
       <strong>
        Items
      </strong>
    </td>
    
    <td>
      Create, read, update, and delete items in your collections
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:folder-outline">
        
      </icon>
      
       <strong>
        Files
      </strong>
    </td>
    
    <td>
      Manage file metadata, import from URLs, organize uploads
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:folder-open-outline">
        
      </icon>
      
       <strong>
        Folders
      </strong>
    </td>
    
    <td>
      Create and organize folder structures for files
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:play-arrow-outline">
        
      </icon>
      
       <strong>
        Trigger Flow
      </strong>
    </td>
    
    <td>
      Execute manual flows on demand
    </td>
  </tr>
</tbody>
</table>

### Admin Only

<callout color="warning" icon="material-symbols:warning">

Be careful when using these tools as deleting or modifying schema can result in data loss.

</callout>

<table>
<thead>
  <tr>
    <th>
      Tool
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:database-outline">
        
      </icon>
      
       <strong>
        Collections
      </strong>
    </td>
    
    <td>
      Create, modify, and delete collections (database tables)
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:variable-add-outline">
        
      </icon>
      
       <strong>
        Fields
      </strong>
    </td>
    
    <td>
      Add, configure, and remove fields within collections
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:hub-outline">
        
      </icon>
      
       <strong>
        Relations
      </strong>
    </td>
    
    <td>
      Set up relationships between collections
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:bolt-outline">
        
      </icon>
      
       <strong>
        Flows
      </strong>
    </td>
    
    <td>
      Create and manage automation workflows
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-muted" name="material-symbols:offline-bolt-outline">
        
      </icon>
      
       <strong>
        Operations
      </strong>
    </td>
    
    <td>
      Configure individual steps within flows
    </td>
  </tr>
</tbody>
</table>

---

## Page Context Tools

<callout color="primary" icon="material-symbols:lightbulb">

Page Context tools let the AI work directly with what's on your screen. They are only available when editing data and may not be available on all pages. Approval modes cannot be changed for Page Context tools.

</callout>

<table>
<thead>
  <tr>
    <th>
      Tool
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
        Read Form Values
      </strong>
    </td>
    
    <td>
      Read current field values from the form on screen
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Set Form Values
      </strong>
    </td>
    
    <td>
      Update field values on the current form
    </td>
  </tr>
</tbody>
</table>

---

## Tool Behavior

### Approval Modes

Each tool can be configured with one of three approval modes:

<table>
<thead>
  <tr>
    <th>
      Mode
    </th>
    
    <th>
      Behavior
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <icon className="text-success" name="material-symbols:check">
        
      </icon>
      
       <strong>
        Always Allowed
      </strong>
    </td>
    
    <td>
      Execute immediately without asking
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-warning" name="material-symbols:approval-delegation">
        
      </icon>
      
       <strong>
        Needs Approval
      </strong>
    </td>
    
    <td>
      Show approval dialog before executing (default)
    </td>
  </tr>
  
  <tr>
    <td>
      <icon className="text-error" name="material-symbols:block">
        
      </icon>
      
       <strong>
        Disabled
      </strong>
    </td>
    
    <td>
      Tool is hidden from AI and not loaded into context
    </td>
  </tr>
</tbody>
</table>

Tool approval settings are stored locally in your browser and are unique to you. They won't sync to your Directus instance or affect other users.

<callout color="primary" icon="material-symbols:lightbulb">

**Disable unused tools to reduce costs.** Disabled tools are not sent to the AI provider, reducing token usage. If you only manage content, disable schema and flow tools.

</callout>

### Default Settings

All tools default to **Ask** mode. Nothing executes without your explicit approval until you change the settings.

### Configuring Tools

![Tool configuration panel showing approval modes](/img/ai-chat-tool-menu-open-cropped.png)

1. Open the settings menu (gear icon) in the chat header
2. Search for specific tools
3. Click a tool and select an approval mode from the dropdown
4. Settings persist in your browser

## Next Steps

<card-group>
<card icon="material-symbols:lightbulb" title="Tips & Best Practices" to="/guides/ai/assistant/tips">

Get the most out of AI Assistant.

</card>

<card icon="material-symbols:security" title="Security" to="/guides/ai/assistant/security">

Access control and data protection.

</card>
</card-group>
