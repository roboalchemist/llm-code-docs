# Source: https://directus.io/docs/raw/guides/integrations/clay/use-clay-templates-with-directus.md

# Templates

> Learn how to use Clay's pre-built HTTP API templates to connect with Directus for data enrichment and synchronization.

Clay provides pre-built templates for common operations with Directus. These templates appear as enrichment column options and handle all the API configuration for you.

**← Back to Directus + Clay Overview**

Follow these steps to use the pre-built Directus templates in Clay.

## Step 1: Set Up Authentication

Before using any templates, configure your Directus authentication in Clay:

1. **Go to your Clay account settings**
2. **Add a new HTTP API account**
3. **Set up the authorization header:**
  - **Key:** `Authorization`
  - **Value:** `Bearer YOUR_DIRECTUS_TOKEN_HERE`
4. **Name it "Directus"** for easy reference

> **💡 Tip:** Once created, you can select this account for all Directus API calls instead of manually entering headers each time.

## Step 2: Add a Directus Template

1. **In your Clay table, create a new enrichment column**
2. **Search for "directus" in the template search**
3. **Select the template that matches your operation:**

<table>
<thead>
  <tr>
    <th>
      Template
    </th>
    
    <th>
      Purpose
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Create Item in Collection
      </strong>
    </td>
    
    <td>
      Add new records to Directus
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Update Item in Collection
      </strong>
    </td>
    
    <td>
      Modify existing records in Directus
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Get Item from Collection
      </strong>
    </td>
    
    <td>
      Search and retrieve records from Directus
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Get Related Item Details
      </strong>
    </td>
    
    <td>
      Fetch relational data from Directus
    </td>
  </tr>
</tbody>
</table>

<callout color="warning" icon="material-symbols:warning">

**Important**<br />


The Directus templates use generic collection names (like "posts" or "users") as examples. You'll need to adapt these to match your specific Directus schema by replacing collection names, adjusting field names, and configuring filters based on your data structure.

</callout>

## Step 3: Configure the Template

Each template requires configuration specific to your Directus setup:

**Basic Configuration:**

<table>
<thead>
  <tr>
    <th>
      Setting
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
        Directus URL
      </strong>
    </td>
    
    <td>
      Your instance URL (e.g., <code>
        https://your-project.directus.app
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Collection Name
      </strong>
    </td>
    
    <td>
      Replace "posts" with your actual collection name
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Account
      </strong>
    </td>
    
    <td>
      Select the "Directus" account you created in Step 1
    </td>
  </tr>
</tbody>
</table>

**For GET operations, add query parameters:**

<field name="limit" type="number">

Maximum number of items to return (e.g., `10`)

</field>

<field name="fields" type="string">

Comma-separated field names (e.g., `id,title,status`)

</field>

<field name="filter[field][operator]" type="string">

Filter criteria (e.g., `filter[status][_eq]` with value `published`)

</field>

For more advanced filtering options and field selection techniques, see the [Working with Directus Data Operations](/guides/integrations/clay/directus-clay-data-operations) guide.

**For POST/PATCH operations, configure the body:**

- Map Clay columns to Directus field names
- Use the visual field mapper or write JSON directly
- Include all required fields for your collection

## Step 4: Map Your Data

Configure how Clay data maps to Directus fields:

1. **Click on field values** to open the column selector
2. **Select the Clay column** that contains your data
3. **Use formulas** if you need to transform data before sending
4. **Set static values** for fields that don't change (like `status: "draft"`)

**Example mapping for creating a blog post:**

```json
{
  "title": "{{Blog Post Title Column}}",
  "slug": "{{URL Slug Column}}",
  "content": "{{Post Content Column}}",
  "status": "draft",
  "author": "{{Author ID Column}}"
}
```

> **💡 Tip:** Use Clay's visual field mapper for easier configuration, or write JSON directly for more control.

## Step 5: Test and Run

1. **Test the enrichment on a single row first**
2. **Verify the results in your Directus instance**
3. **Check for any errors in Clay's response column**
4. **Once confirmed working, run on your full dataset**

---

## Next Steps

- **Learn about Directus Webhooks →** - Set up real-time data sync
- **Explore Advanced Data Operations →** - Filters, pagination, and best practices
- **← Back to Overview**

## Additional Resources

- [Clay Documentation](https://clay.com/docs)
- [Directus Community](https://community.directus.io/)
