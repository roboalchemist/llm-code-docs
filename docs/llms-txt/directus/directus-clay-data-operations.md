# Source: https://directus.io/docs/raw/guides/integrations/clay/directus-clay-data-operations.md

# Data Operations

> Advanced techniques for working with Directus data in Clay, including filters, pagination, common use cases, and best practices.

This guide covers advanced techniques for working with Directus data in Clay, including filtering, field selection, pagination, and optimization strategies.

**← Back to Directus + Clay Overview**

## Working with Directus Data

### Understanding Filters

When retrieving data from Directus, you can use powerful filter operators to find exactly what you need.

**Filter syntax in Clay query parameters:**

- **Key:** `filter[field_name][operator]`
- **Value:** The comparison value

**Common operators:**

<table>
<thead>
  <tr>
    <th>
      Operator
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Example
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        _eq
      </code>
    </td>
    
    <td>
      Equals
    </td>
    
    <td>
      <code>
        filter[status][_eq]
      </code>
      
       → <code>
        published
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _neq
      </code>
    </td>
    
    <td>
      Not equals
    </td>
    
    <td>
      <code>
        filter[status][_neq]
      </code>
      
       → <code>
        draft
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _contains
      </code>
    </td>
    
    <td>
      Contains (case sensitive)
    </td>
    
    <td>
      <code>
        filter[title][_contains]
      </code>
      
       → <code>
        Guide
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _icontains
      </code>
    </td>
    
    <td>
      Contains (case insensitive)
    </td>
    
    <td>
      <code>
        filter[title][_icontains]
      </code>
      
       → <code>
        guide
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _in
      </code>
    </td>
    
    <td>
      In array
    </td>
    
    <td>
      <code>
        filter[status][_in]
      </code>
      
       → <code>
        draft,published
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _gt
      </code>
    </td>
    
    <td>
      Greater than
    </td>
    
    <td>
      <code>
        filter[views][_gt]
      </code>
      
       → <code>
        1000
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _lt
      </code>
    </td>
    
    <td>
      Less than
    </td>
    
    <td>
      <code>
        filter[price][_lt]
      </code>
      
       → <code>
        100
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _null
      </code>
    </td>
    
    <td>
      Is null
    </td>
    
    <td>
      <code>
        filter[deleted_at][_null]
      </code>
      
       → <code>
        true
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nnull
      </code>
    </td>
    
    <td>
      Is not null
    </td>
    
    <td>
      <code>
        filter[published_at][_nnull]
      </code>
      
       → <code>
        true
      </code>
    </td>
  </tr>
</tbody>
</table>

### Selecting Specific Fields

To improve performance and reduce data transfer, specify only the fields you need:

**In query parameters:**

- **Key:** `fields`
- **Value:** Comma-separated field names (e.g., `id,title,status,author`)

**Including related fields:**

- Use dot notation: `author.first_name,author.last_name`
- This pulls in data from related collections

### Sorting and Pagination

<field name="sort" type="string">

Field name (prefix with `-` for descending). Example: `-date_created` (newest first)

</field>

<field name="limit" type="number">

Maximum items to return (e.g., `50`)

</field>

<field name="offset" type="number">

Number of items to skip (e.g., `0`, `50`, `100`)

</field>

---

## Common Use Cases

<table>
<thead>
  <tr>
    <th>
      Use Case
    </th>
    
    <th>
      Scenario
    </th>
    
    <th>
      Steps
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        🛒 E-commerce Product Enrichment
      </strong>
    </td>
    
    <td>
      Enrich product data with inventory and pricing information
    </td>
    
    <td>
      1. Use <strong>
        Get Item from Collection
      </strong>
      
       to check if a product exists in Directus<br />
      
      2. Use <strong>
        Update Item in Collection
      </strong>
      
       to update stock levels from external sources<br />
      
      3. Use <strong>
        Get Related Item Details
      </strong>
      
       to pull supplier information
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        📝 Content Publication Workflow
      </strong>
    </td>
    
    <td>
      Automatically publish content when it's approved in Clay
    </td>
    
    <td>
      1. Use Directus webhooks to send draft content to Clay for review<br />
      
      2. Enrich content with SEO metadata and keyword research in Clay<br />
      
      3. Use <strong>
        Update Item in Collection
      </strong>
      
       to publish content back to Directus
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        👥 Lead Enrichment System
      </strong>
    </td>
    
    <td>
      Sync CRM data between Clay and Directus
    </td>
    
    <td>
      1. Use Directus webhooks to send new leads to Clay<br />
      
      2. Enrich leads with company data and contact information<br />
      
      3. Use <strong>
        Update Item in Collection
      </strong>
      
       to sync enriched data back<br />
      
      4. Use <strong>
        Get Related Item Details
      </strong>
      
       to pull company profiles
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        📋 Form Submission Processing
      </strong>
    </td>
    
    <td>
      Process form submissions and create records
    </td>
    
    <td>
      1. Use Directus webhooks to send form submissions to Clay<br />
      
      2. Use <strong>
        Get Item from Collection
      </strong>
      
       to check for existing records<br />
      
      3. Use <strong>
        Create Item in Collection
      </strong>
      
       to add new contacts<br />
      
      4. Use <strong>
        Update Item in Collection
      </strong>
      
       to update existing records
    </td>
  </tr>
</tbody>
</table>

---

## Troubleshooting

When working with Directus API through Clay, you may encounter various error codes. For a comprehensive list of Directus error codes and their meanings, refer to the [official Directus Error Codes documentation](https://directus.io/docs/guides/connect/errors).

### Common Issues

**Authentication Problems:**

- Verify your API token is valid and active
- Check that you're using the correct format: `Bearer YOUR_TOKEN`
- Ensure the token hasn't expired

**Collection and Field Issues:**

- Verify collection names match exactly (case-sensitive)
- Check that field names match your Directus schema
- Ensure proper permissions are set for collections

**Filter and Query Issues:**

- Use the correct format: `filter[field][operator]`
- Test filters in Directus admin panel first
- Check for special characters that need escaping

### Getting Help

If you encounter issues:

1. **For Directus-specific questions:** Ask for help in the [Directus Community](https://community.directus.io/)
2. **For Clay-specific questions:** Contact Clay support or check Clay's documentation
3. **For API connection issues:** Verify your Directus configuration and permissions

---

## Next Steps

- **Learn Clay Templates →** - Use Clay's pre-built templates
- **Learn Directus Webhooks →** - Set up real-time data sync
- **← Back to Overview**

## Additional Resources

- [Clay Documentation](https://clay.com/docs)
- [Directus Community](https://community.directus.io/)
