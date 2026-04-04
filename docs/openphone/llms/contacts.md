# Source: https://www.quo.com/docs/mdx/guides/contacts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# External contacts

> Learn about working with contacts imported via the Quo API or native integrations.

## Understanding external contacts

External contacts are contacts that originate from outside the Quo app: either created through the Quo API or synced via native integrations (such as CRM or other connected platforms). These contacts allow you to centralize contact records from multiple sources within your Quo workspace.

### Key characteristics

<CardGroup cols={1}>
  <Card title="Distinct from app-created contacts">
    External contacts are separate from contacts created directly in the Quo app, with their own specific behaviors depending on how they were created.
  </Card>

  <Card title="Two sources, different behaviors">
    External contacts can come from two sources: the Quo API or native integrations and each has different editability rules within the Quo app.
  </Card>
</CardGroup>

### Editability by source

<CardGroup cols={2}>
  <Card title="API-created contacts" icon="code">
    Contacts created via the Quo API can be updated directly within the Quo app. You can also continue managing them programmatically through API endpoints.
  </Card>

  <Card title="Native integration contacts" icon="plug">
    Contacts synced from native integrations remain read-only within Quo. Any changes must be made in the source system and synced back to Quo.
  </Card>
</CardGroup>

### Important behaviors and limitations

<CardGroup cols={1}>
  <Card title="Preserving contact IDs">
    When you create a contact using the `POST /contacts` endpoint, it's essential to save the `id` returned in the response. This `id` will be required for all future API operations involving the contact.
  </Card>

  <Card title="Visibility in the Quo app">
    After creating an API contact, it will only appear in the Quo app—whether in the conversation list, contact list, or search results—if there's an associated conversation with a matching phone number.
  </Card>
</CardGroup>

## Contact field structure

Quo organizes contact information using two distinct field types. Understanding these is crucial for effective contact management.

<AccordionGroup>
  <Accordion title="Default fields" defaultOpen="true">
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

## Creating and managing contacts via API

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
    Update contacts either within the Quo app or programmatically using the `PATCH /contacts/:id` endpoint with the saved contact ID.
  </Step>
</Steps>

<Tip>
  Always validate phone numbers are in E.164 format (+1234567890) before creating or updating contacts to ensure proper functionality.
</Tip>
