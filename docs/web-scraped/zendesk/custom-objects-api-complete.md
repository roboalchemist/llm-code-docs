# Source: https://developer.zendesk.com/documentation/custom-data/

# Zendesk Custom Objects API - Complete Reference

The Custom Objects API enables storage and management of business-specific data within Zendesk. Create custom data structures beyond standard Zendesk objects (tickets, users, organizations).

## Overview

### Custom Objects vs Legacy Custom Objects

**Custom Objects (Recommended)**
- Modern data structure support
- Native Zendesk relationships
- Integrated with triggers, views, Explore
- Recommended for new implementations
- Available across all Zendesk products

**Legacy Custom Objects**
- Stored in AWS infrastructure
- Primarily for existing implementations
- Limited relationship support
- New projects should use modern custom objects

## Core Concepts

### Custom Object Type
Defines the schema and structure for a type of custom object (like a database table).

**Properties:**
- `key` - Unique identifier for the object type
- `display_name` - Human-readable name
- `schema` - Field definitions
- `created_at`, `updated_at` - Timestamps

### Custom Object Records
Instances of a custom object type containing actual data.

### Relationships
Link custom objects to:
- Support tickets
- Users
- Organizations
- Other custom objects
- Multiple relationships per record

### Fields
Define custom object properties with types:
- Text (short strings)
- Long text (descriptions)
- Number (integer, decimal)
- Date/DateTime
- Dropdown (single select)
- Multiselect
- Boolean
- Record (relationships)

## API Endpoints

### Custom Object Types

```bash
GET /custom_objects              # List all custom object types
POST /custom_objects             # Create new custom object type
GET /custom_objects/{key}        # Get custom object type
PUT /custom_objects/{key}        # Update custom object type
DELETE /custom_objects/{key}     # Delete custom object type
```

**Create Custom Object Type Example:**

```bash
POST /custom_objects
{
  "custom_object": {
    "key": "product",
    "display_name": "Product",
    "description": "Product catalog",
    "schema": {
      "properties": {
        "name": {
          "type": "text",
          "title": "Product Name"
        },
        "sku": {
          "type": "text",
          "title": "SKU"
        },
        "price": {
          "type": "number",
          "title": "Price"
        }
      }
    }
  }
}
```

### Custom Object Records

```bash
GET /custom_objects/{type_key}/records              # List records
POST /custom_objects/{type_key}/records             # Create record
GET /custom_objects/{type_key}/records/{id}         # Get record
PUT /custom_objects/{type_key}/records/{id}         # Update record
DELETE /custom_objects/{type_key}/records/{id}      # Delete record
```

**Create Record Example:**

```bash
POST /custom_objects/product/records
{
  "custom_object_record": {
    "attributes": {
      "name": "Enterprise License",
      "sku": "ENT-001",
      "price": 9999
    }
  }
}
```

### Relationships

Link custom objects to tickets and other resources:

```bash
GET /tickets/{ticket_id}/custom_object_records      # Get related records
POST /tickets/{ticket_id}/custom_object_records     # Link record to ticket
DELETE /tickets/{ticket_id}/custom_object_records/{id}  # Unlink record
```

## Field Types & Validation

### Text Field
Short text strings (single line).

```json
{
  "type": "text",
  "title": "Product Name",
  "description": "Name of the product",
  "max_length": 255
}
```

### Long Text Field
Multi-line text content.

```json
{
  "type": "textarea",
  "title": "Description",
  "max_length": 5000
}
```

### Number Field
Integer or decimal values.

```json
{
  "type": "number",
  "title": "Quantity",
  "number_type": "integer"
}
```

### Date/DateTime Field
Calendar dates or timestamps.

```json
{
  "type": "date",
  "title": "Order Date"
}
```

### Dropdown (Single Select)
Predefined list of options.

```json
{
  "type": "dropdown",
  "title": "Status",
  "options": [
    {"value": "active", "label": "Active"},
    {"value": "inactive", "label": "Inactive"}
  ]
}
```

### Multiselect
Multiple selection from predefined options.

```json
{
  "type": "multiselect",
  "title": "Tags",
  "options": [
    {"value": "urgent", "label": "Urgent"},
    {"value": "vip", "label": "VIP"}
  ]
}
```

### Boolean Field
True/false values.

```json
{
  "type": "boolean",
  "title": "Is Active"
}
```

### Record Relationship
Link to other custom objects or Zendesk objects.

```json
{
  "type": "record",
  "title": "Related Account",
  "reference_target": "custom_object_account"
}
```

## Common Workflows

### Create Product Catalog

```bash
# 1. Define Product custom object type
POST /custom_objects
{
  "custom_object": {
    "key": "product",
    "display_name": "Product",
    "schema": {
      "properties": {
        "name": {"type": "text"},
        "sku": {"type": "text"},
        "category": {"type": "dropdown", "options": [...]},
        "price": {"type": "number"},
        "in_stock": {"type": "boolean"}
      }
    }
  }
}

# 2. Create product records
POST /custom_objects/product/records
{
  "custom_object_record": {
    "attributes": {
      "name": "Premium Widget",
      "sku": "WIDGET-001",
      "category": "widgets",
      "price": 99.99,
      "in_stock": true
    }
  }
}

# 3. Link product to ticket
POST /tickets/123/custom_object_records
{
  "custom_object_record": {
    "id": "product-456"
  }
}
```

### Order Management

Create linked Order and OrderItem custom objects:

```bash
# Order with items
POST /custom_objects/order/records
{
  "custom_object_record": {
    "attributes": {
      "order_number": "ORD-2024-001",
      "customer_name": "John Doe",
      "total_amount": 299.97,
      "order_date": "2024-02-14",
      "status": "pending"
    }
  }
}

# Items linked to order
POST /custom_objects/order_item/records
{
  "custom_object_record": {
    "attributes": {
      "order_id": "order-789",
      "product_id": "product-456",
      "quantity": 3,
      "unit_price": 99.99
    }
  }
}
```

### Customer Contact Database

```bash
POST /custom_objects/contact/records
{
  "custom_object_record": {
    "attributes": {
      "first_name": "Jane",
      "last_name": "Smith",
      "email": "jane@example.com",
      "phone": "+1-555-1234",
      "company": "ACME Corp",
      "contact_type": "vendor",
      "last_contact_date": "2024-02-10"
    }
  }
}
```

## Searching Custom Objects

### Search Records

```bash
GET /custom_objects/{type_key}/records?query=name%3AProduct

# Using advanced queries
GET /custom_objects/product/records?filter[price][gte]=100&filter[price][lte]=500
```

### Filtering & Sorting

```bash
# Filter by field value
GET /custom_objects/product/records?filter[category]=electronics&filter[in_stock]=true

# Sort results
GET /custom_objects/product/records?sort=-price

# Pagination
GET /custom_objects/product/records?limit=50&offset=0
```

## Integration with Zendesk Features

### Triggers
Create triggers that reference custom object data:

```
IF ticket subject contains [custom_object_field]
THEN create/update related custom object
```

### Automations
Time-based custom object operations:

```
IF ticket is stale
THEN update related order status to "abandoned"
```

### Explore Analytics
Report on custom object data alongside ticket metrics.

### Web Widget
Display custom object information in widget for context.

### Views & Reports
Filter and display tickets by related custom object properties.

## Relationships to Zendesk Objects

### Ticket Relationships

Link custom records to tickets:

```bash
# Link at ticket creation
POST /tickets
{
  "ticket": {
    "subject": "Support Request",
    "custom_object_records": [
      {"id": "product-123", "type": "product"}
    ]
  }
}

# Add relationship to existing ticket
POST /tickets/456/custom_object_records
{
  "custom_object_record": {
    "id": "order-789"
  }
}
```

### User Relationships

Link custom data to users/organizations.

### Activity Tracking

Create custom events in custom objects:

```bash
POST /custom_objects/order/records/{id}/timeline
{
  "event": {
    "type": "status_change",
    "timestamp": "2024-02-14T10:30:00Z",
    "actor": "agent-123",
    "details": {
      "from": "pending",
      "to": "processing"
    }
  }
}
```

## Best Practices

### Schema Design
- Use descriptive field names
- Define appropriate field types
- Add helpful descriptions
- Plan for future extensions

### Data Integrity
- Validate data before creation
- Enforce unique constraints where needed
- Use relationships for data consistency
- Clean up orphaned records

### Performance
- Index frequently filtered fields
- Use pagination for large result sets
- Cache custom object queries
- Batch operations where possible

### Security
- Restrict access via roles/permissions
- Audit sensitive field changes
- Validate user input
- Encrypt sensitive data

## Error Handling

**Common Error Responses:**

```json
{
  "error": "Invalid field type",
  "description": "Field 'price' must be of type 'number'"
}

{
  "error": "Record not found",
  "description": "Custom object record with id 'xyz' not found"
}

{
  "error": "Schema validation failed",
  "description": "Field 'required_field' is required"
}
```

## Limits & Quotas

- **Custom Object Types**: Up to 50 per account
- **Fields per Type**: Up to 50 fields
- **Records**: No hard limit (depends on plan)
- **Relationships**: Multiple per record supported
- **Query Results**: Default 50, max 100 per request

## Migration from Legacy

For existing custom objects:

1. Design new schema in modern custom objects
2. Create export of legacy data
3. Transform/import into new structure
4. Update integrations to use new API
5. Deactivate legacy custom objects

## Resources

- [Custom Objects API Reference](https://developer.zendesk.com/api-reference/custom-data/)
- [Getting Started Guide](https://developer.zendesk.com/documentation/custom-data/v2/getting-started-with-custom-objects)
- [Schema Definition Reference](https://developer.zendesk.com/documentation/custom-data/custom-objects-api/custom-objects-api/)
- [Zendesk Explore Integration](https://developer.zendesk.com/documentation/custom-data/)
