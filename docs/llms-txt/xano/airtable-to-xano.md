# Source: https://docs.xano.com/the-database/migrating-your-data/airtable-to-xano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Airtable To Xano

## Why migrate from Airtable to Xano?

### Scalability & Limits

At the time this document was last updated, Airtable's published pricing models offer a maximum of 500,000 records per base, and 1,000 GB of file storage.

Xano's database does not have a record limit, or a limit on file storage. We can scale infinitely to meet your data needs.

### Performance & Capability

Airtable themselves say that it is not intended to use their platform for an application backend.

> For this reason, it is important to note that Airtable is not intended to be a backend hosting service/real-time database like Heroku, Parse, Firebase, or MongoDB. Instead, Airtable is primarily designed for use cases where all users will be directly interacting within the Airtable UI. *From* [***Troubleshooting Airtable base performance***](https://support.airtable.com/docs/troubleshooting-airtable-performance)

Airtable says this is because as the volume of requests to your Airtable base increases, it may not be able to perform as expected under such load.

Xano is built from the ground up to be a capable, scalable, and secure backend solution.

***

## Migrating Airtable data to Xano

<Frame>
  <iframe src="https://demo.arcade.software/lHChGvdpBrYMZldVzAGA?embed" title="https://demo.arcade.software/lHChGvdpBrYMZldVzAGA?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" />
</Frame>

<Steps>
  <Step title="Head to the database and click '+ Add table'">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/15987831-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=990292db033eb36c5d9f2bb83accaf77" width="118" height="45" data-path="images/15987831-image.jpeg" />
    </Frame>
  </Step>

  <Step title="In the new table menu, choose Import Data > Import From Airtable">
    &#x9;
  </Step>

  <Step title="Provide your Airtable personal access token">
    You can generate a personal access token in Airtable by heading to your account settings, and from there visiting the **Developer Hub**.

    Choose **Personal Access Tokens** from the left-side navigation, and create a token with the following scopes:

    ```
    data:base.read
    schema:base.read
    ```
  </Step>

  <Step title="Select the tables and/or views you want to import into Xano, and confirm your selection">
    &#x9;
  </Step>
</Steps>

***

## Rebuilding Automations

While there is no direct migration of your Airtable automations to Xano, we want to make it as easy as possible to rebuild. Please see the table and linked resources below for common Airtable -> Xano functionality translations. Click on the Xano Function name to be taken to Xano's documentation, or review the video examples provided.

| Airtable Function      | Xano Function                                                                            | Video Example                                 |
| ---------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------- |
| Create Record          | [Add Record](/the-function-stack/functions/database-requests/add-record)                 | [Video Example](https://youtu.be/k0GpUdsRkL0) |
| Update record          | [Edit record](/the-function-stack/functions/database-requests/edit-record)               | [Video Example](https://youtu.be/rTeJamc_MYE) |
| Find records           | [Query all records](/the-function-stack/functions/database-requests/query-all-records)   | [Video Example](https://youtu.be/-XjcXEtPNmk) |
| Conditional logic      | [Conditional statement](/the-function-stack/functions/data-manipulation/conditional)     | [Video Example](https://youtu.be/QR4UJ2GpYDo) |
| Repeating group        | [For each loop](/the-function-stack/functions/data-manipulation/loops)                   | [Video Example](https://youtu.be/AGe5JN0rZ2M) |
| At scheduled time      | [Background task](/the-function-stack/building-with-visual-development/background-tasks) | [Video Example](https://youtu.be/SDXWVhBGKmQ) |
| Link to another record | [Table reference](/the-database/database-basics/field-types#table-reference)             | [Video Example](https://youtu.be/z-TwxiQOIBs) |
| Lookup                 | [Addons](/the-function-stack/functions/database-requests/query-all-records#using-addons) | [Video Example](https://youtu.be/z-TwxiQOIBs) |


Built with [Mintlify](https://mintlify.com).