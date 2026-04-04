# Source: https://developers.webflow.com/mcp/reference/data/cms/fields.mdx

***

title: Fields
description: Create and update fields in CMS collections
--------------------------------------------------------

Create and update fields in CMS collections using the Fields tools. Fields define the data structure for collection items.

## Create static field

Create a new static field in a CMS collection (e.g., text, number, date, etc.).

**Tool:** `collection_fields_create_static`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Static field definition

    <Accordion title="+ Show 5 properties">
      <ParamField path="displayName" type="string" required={true}>
        Field name
      </ParamField>

      <ParamField path="slug" type="string" required={true}>
        Field slug
      </ParamField>

      <ParamField path="fieldType" type="string" required={true}>
        Type of field (text, number, date, etc.)
      </ParamField>

      <ParamField path="isRequired" type="boolean" required={false}>
        Whether the field is required
      </ParamField>

      <ParamField path="isUnique" type="boolean" required={false}>
        Whether values must be unique
      </ParamField>
    </Accordion>
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="POST /v2/collections/{collection_id}/fields" />

**Returns:** Created field object

***

## Create option field

Create a new option field in a CMS collection with predefined choices.

**Tool:** `collection_fields_create_option`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Option field definition

    <Accordion title="+ Show 4 properties">
      <ParamField path="displayName" type="string" required={true}>
        Field name
      </ParamField>

      <ParamField path="slug" type="string" required={true}>
        Field slug
      </ParamField>

      <ParamField path="options" type="array" required={true}>
        Array of option values
      </ParamField>

      <ParamField path="isRequired" type="boolean" required={false}>
        Whether the field is required
      </ParamField>
    </Accordion>
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="POST /v2/collections/{collection_id}/fields" example="OptionField" />

**Returns:** Created field object

***

## Create reference field

Create a new reference field in a CMS collection that links to items in another collection.

**Tool:** `collection_fields_create_reference`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Reference field definition

    <Accordion title="+ Show 4 properties">
      <ParamField path="displayName" type="string" required={true}>
        Field name
      </ParamField>

      <ParamField path="slug" type="string" required={true}>
        Field slug
      </ParamField>

      <ParamField path="referencedCollectionId" type="string" required={true}>
        ID of the referenced collection
      </ParamField>

      <ParamField path="isRequired" type="boolean" required={false}>
        Whether the field is required
      </ParamField>
    </Accordion>
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="POST /v2/collections/{collection_id}/fields" example="ReferenceField" />

**Returns:** Created field object

***

## Update field

Update properties of an existing field in a CMS collection.

**Tool:** `collection_fields_update`

<Card>
  <ParamField path="collection_id" type="string" required={true}>
    Unique identifier for the collection
  </ParamField>

  <ParamField path="field_id" type="string" required={true}>
    Unique identifier for the field
  </ParamField>

  <ParamField path="request" type="object" required={true}>
    Field update object with properties to modify
  </ParamField>
</Card>

<EndpointRequestSnippet endpoint="PATCH /v2/collections/{collection_id}/fields/{field_id}" />

**Returns:** Updated field object
