# Source: https://www.quo.com/docs/mdx/guides/contacts.md

# Integration contacts

> Learn more about working with contacts via the Quo API.

## Understanding integration contacts

Integration contacts are contacts that are created and managed through the Quo API. They provide a programmatic way to import contact records from external sources into your Quo workspace.

### Key characteristics

<CardGroup cols={1}>
  <Card title="Distinct from app contacts">
    Integration contacts are separate from contacts created directly in the Quo app, with their own specific behaviors and management flow.
  </Card>

  <Card title="API-first management">
    These contacts are designed to be managed exclusively through API endpoints, enabling automated contact management and integration with your existing systems. They cannot be modified or deleted within Quo.
  </Card>
</CardGroup>

### Important behaviors and limitations

<CardGroup cols={1}>
  <Card title="Preserving contact IDs">
    When you create an integration contact using the `POST /contacts` endpoint, it's essential to save the `id` returned in the response. This `id` will be required for all future operations involving the contact.
  </Card>

  <Card title="Visibility in the Quo app">
    After creating an integration contact, it will only appear in the Quo app—whether in the conversation list, contact list, or search results—if there's an associated conversation with a matching phone number.
  </Card>

  <Card title="Read-only status">
    At present, integration contacts are read-only within the Quo app. To make any updates or changes to an integration contact, you will need to use the `PATCH /contacts/:id` endpoint.
  </Card>
</CardGroup>

## Contact field structure

Quo organizes contact information using two distinct field types. Understanding these is crucial for effective contact management.

<AccordionGroup>
  <Accordion title="Default fields" defaultOpen={true}>
    Every contact in Quo includes these predefined fields:

    * First Name
    * Last Name
    * Role
    * Company
    * Emails
    * Phone Numbers

    These fields maintain consistent properties across all contacts and form the foundation of contact information.
  </Accordion>

  <Accordion title="Custom fields">
    Custom fields allow for flexible, user-defined contact properties. Supported data types include:

    * Address
    * Boolean
    * Date
    * Multi-select
    * Number
    * String
    * URL

    <Note>
      **Managing Custom Fields:** Custom field definitions can only be modified within the Quo app. The API does not currently support creating or editing custom field definitions.
    </Note>
  </Accordion>
</AccordionGroup>

## Creating and managing contacts

Follow these steps to effectively create and manage contacts through the API:

<Steps>
  <Step title="Retrieve custom fields">
    First, call the `GET /contact-custom-fields` endpoint to retrieve your workspace's custom contact field definitions.
  </Step>

  <Step title="Prepare contact data">
    Structure your contact data according to both default and custom fields:

    ```json  theme={null}
    {
      "defaultFields": {
        "firstName": "John",
        "lastName": "Doe",
        "phoneNumbers": [
          {
            "name": "primary",
            "value": "+1234567890"
          }
        ]
      },
      "customFields": {
        // Include any custom field values here
      }
    }
    ```
  </Step>

  <Step title="Create the contact">
    Use the `POST /contacts` endpoint to create the contact and store the returned contact ID for future operations.
  </Step>

  <Step title="Manage the contact">
    Use the saved contact ID with the `PATCH /contacts/:id` endpoint for any future updates to the contact's information.
  </Step>
</Steps>

<Tip>
  Always validate phone numbers are in E.164 format (+1234567890) before creating or updating contacts to ensure proper functionality.
</Tip>
