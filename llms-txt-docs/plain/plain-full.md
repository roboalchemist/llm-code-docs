# Plain Documentation

Source: https://www.plain.com/docs/llms-full.txt

---

# Customer cards
Source: https://www.plain.com/docs/customer-cards

Live context straight from your own systems when helping customers.

Customer cards are a powerful feature in Plain that let you show information from your own systems while looking at a customer or thread in Plain. This makes sure you always have important context when helping customers.

Customer cards are configured on Plain (see how to [how to create one](/customer-cards/create-a-customer-card)) and requested by Plain from your APIs.

## High-level flow

<Note>
  For a more detailed description of the protocol, check out the [full
  spec](/customer-cards/protocol).
</Note>

1. A thread is viewed in Plain.

2. Plain fires a POST request to your API with:

   * The thread customer's `email`, `id` and, if set, `externalId`
   * The thread's `id` and, if set, `externalId`.
   * If the thread has a tenant, the tenant `id` and, if set, `externalId`.
   * The configured customer card `key`s

3. Your API responds with the JSON for each card

4. Cards are shown to the user in Plain.

Based on your customer card settings, Plain will send a request to your API like the below example:

<Snippet file="customer-cards/customer-cards-basic-request.mdx" />

Your API should then reply with a list of cards matching the requested keys where each card contains the components you want to display:

<Snippet file="customer-cards/customer-cards-basic-response.mdx" />

## UI Components

To define what each customer card should look like, you use the Plain UI components. All the components are documented in the [Plain UI Components](/ui-components/) section.

You can find example customer cards and an example API you can check out [team-plain/example-customer-cards](https://github.com/team-plain/example-customer-cards). Feel free to try these out in your workspace!

## Example cards

To demonstrate what you can build with customer cards we've built some examples you can view and which are open source.

[**Customer cards Examples →**](https://github.com/team-plain/example-customer-cards)

## Playground

The UI components playground lets you build and preview the component JSON needed to create a customer card. Use this to prototype a customer card before starting to build your integration.

[**Playground →**](https://app.plain.com/developer/ui-components-playground/)


# Create a customer card
Source: https://www.plain.com/docs/customer-cards/create-a-customer-card

Define the details of the customer card.

To create a customer card head to **Settings** → **Customer cards** and enter the following details:

* **Title**: this will be displayed as the title of the card so even if the card fails to load users know which card is
  errored.
* **Key**: the link between this config and your API. A key can only contain alphanumeric, hyphen, and underscore characters (regex: `[a-zA-Z0-9_-]+`)
* **Default time to live (seconds)**: by default how long Plain should cache customer cards. The minimum is 15 seconds, maximum is 1 year in seconds (31536000 seconds).
* **URL**: the URL of your API endpoint that will be built to return customer cards. It must start with `https://`.
* **Headers (optional)**: the headers Plain should pass along when making the request. While this is optional it is
  **highly recommended** to add authorization headers or other tokens that authenticate the request as your API may be
  returning customer data.

<Note>
  To get you started quickly, we've created a few example customer cards that you can configure and see how they look in your application. All example cards are available in our open-source repository:
  [team-plain/example-customer-cards](https://github.com/team-plain/example-customer-cards)

  Here is one you can try right now:

  * Title: e.g. "Usage"
  * Key: `usage`
  * Default time to live: `120`
  * URL: [https://example-customer-cards.plain.com/](https://example-customer-cards.plain.com/)
</Note>


# Examples
Source: https://www.plain.com/docs/customer-cards/examples





# Playground
Source: https://www.plain.com/docs/customer-cards/playground





# Protocol
Source: https://www.plain.com/docs/customer-cards/protocol

Learn how we request customer cards from your API and how to respond to these requests.

<Note>
  This page is intended for a technical audience that will be implementing a customer card API.

  Check out the [customer cards](/customer-cards) page for an overview of customer cards.
</Note>

Customer cards are not proactively loaded. They are just-in-time and pulled when required.
This means that if your APIs are slow then users of the Support App will see a loading spinner over the card.

The protocol is as follows:

1. When a user in Plain opens up a customer's page the cards are loaded.
2. Plain's backend figures out which cards can be returned from the cache and which cards need to be loaded. On the first
   load of the customer this would be all cards.
3. It calculates how many requests it needs to make (see [request deduplication](#request-deduplication) for
   details).
4. Your APIs are then called with the customer's details, so you can look up the customer's data in your systems
   (see [request](#request) section for details).
5. Your APIs then return customer cards that consist of [Plain UI components](/ui-components)
   (see [response](#response) section for details).
6. The cards are cached based on either an explicit TTL value in the response or the TTL in the card settings (see [caching](#caching)).
7. Cards are shown to the user in Plain.
8. Users can manually reload the card at any time in which case only that one card will be requested from your API.

A **few limits** to be aware of:

* Your API must **respond within 15 seconds**, or it will time out. See [retry strategy](#retry-strategy) for details on how timed-out requests are retried.
* You can configure a **maximum of 25 customer cards per workspace**.
* **Card keys must be unique within a workspace**. A key can only contain **alphanumeric**, **hyphen**, and **underscore** characters (regex: `[a-zA-Z0-9_-]+`).

## Request

Plain will make the following request to your backend:

* **Method**: `POST`
* **URL:** the URL you configured on customer cards settings page.
* **Headers:**
  * All the headers you provided on customer cards settings page. This should typically include authentication headers.
  * `Content-Type`: `application/json`
  * `Accept`: `application/json`
  * `Plain-Workspace-Id`: the ID of the workspace the customer is in. This is useful for logging or request routing.
  * `User-Agent`: `Plain/1.0 (plain.com; help@plain.com)`
  * `Plain-Request-Signature`: `XXX` (see [request signing](/request-signing) for details)
* **Body:**
  * `cardKeys`: an array of card keys being requested
  * `customer`: an object with the customer's core details
    * `id`: the id of the customer in Plain
    * `email`: the email of the customer
    * [`externalId`](https://www.plain.com/docs/graphql/customers/upsert) (optional): string if the customer has an `externalId`, otherwise it is `null`.
  * `thread` (optional): an object with the thread's details, if this customer card is being requested in the context of a thread
    * `id`: the id of the thread in Plain
    * `externalId` (optional): string if the thread has an `externalId`, otherwise it is `null`.

Example request body:

<Snippet file="customer-cards/customer-cards-request.mdx" />

### Request deduplication

If you configure multiple customer cards that have the same API details then Plain will batch them and make only one request.

The request deduplication logic for customer card configs is:

* The following config properties are ignored: Title, Card key, Default TTL
* **API URL:** Leading and trailing whitespaces are trimmed and then compared. **This is case sensitive**.
  * For example, these URLs would be considered **different**:
    * `https://api.example.com/cards`
    * `https://api.example.com/cards/`
    * `https://api.example.com/Cards`
* **API Headers:** Order of headers does not matter
  * **Header name:** Leading and trailing whitespaces are trimmed and then compared. **This is case insensitive**.
    * For example, these header names be considered **the same**:
      * `Authorization`
      * `AUTHORIZATION`
      * `   authorization   `
  * **Header value:** No processing done, compared as is (be careful with any extra whitespace characters)
    * For example, these header values would be considered **as different**:
      * `Bearer my-token`
      * `bearer my-token`
      * `   bearer my-token   `

## Response

<Warning>
  For each key requested a corresponding card **MUST** be returned in the response, otherwise an integration error will be returned for that card.

  Any extra cards in the response will be ignored.
</Warning>

Your API must respond with a **`200` status code** or the response body won't be processed and will be treated as an error.

The response body must be a JSON object with:

* `cards`: an array of cards. Every `cardKey` requested should have a corresponding `key` returned. Any extra returned
  cards will be ignored.
  * `key`: the requested key
  * `timeToLiveSeconds` (optional, nullable): can either be omitted or `null`. If provided it will override the default time to live value. This allows you to control caching on a case-by-case basis.
  * `components` (nullable): `null` to indicate that the card has no data or an array of [Plain UI Components](/ui-components/).

Example response body for a card cached for 1 hour:

<Snippet file="customer-cards/customer-cards-response.mdx" />

Example response body for a card that has no data and should not be displayed and TTL omitted:

<Snippet file="customer-cards/customer-cards-no-display-response.mdx" />

## Caching

We cache the responses we get from your APIs. This cache is controlled via two properties:

1. A time to live value (in seconds) in the customer card's settings. This can be changed under **Settings** → **Customer cards**. Any changes here will only apply to newly loaded customer cards.
2. An explicit time to live value (in seconds) in your API response with the key `timeToLiveSeconds`. This overrides the value from settings and allows your API to dynamically set the TTL using custom logic.

Any card that is past its expiry time will usually be deleted within a few minutes but no later than 48 hours after expiry.

## Retry strategy

Errors are classified into two categories:

1. **Retriable errors**: these are transient issues where retrying once is appropriate
2. **Integration errors**: these are typically programming or configuration errors. These errors won't be retried and cached for 5 minutes.

## Security

Plain supports [request signing](/request-signing) and [mTLS](/mtls) to verify that the request was made by Plain and not a third party.

### Retriable errors

The following errors are **retried once** after a **1-second delay**:

* HTTP `5xx` response status code
* HTTP `429` Too Many Requests response status code
* The request times out after 15 seconds.
* Plain fails to perform the request for some reason

Retriable errors are not cached, therefore if the cards are requested again via the Support App they will be re-requested.

### Integration errors

The following errors are **not retried**:

* All HTTP 4xx response status codes except for HTTP `429` Too Many Requests response status code
* A card key is missing in the response. For example, if `subscription-details` is requested but the `cards` array in the response doesn't have an element with the key `subscription-details`.
* The response body does not match the expected schema documented in [response](#response).

Integration errors are cached for 5 minutes and usually indicate a programming or configuration error.

Users can manually refresh a card in the UI, in which case the card will be requested again.


# API Explorer
Source: https://www.plain.com/docs/graphql/api-explorer





# Attachments
Source: https://www.plain.com/docs/graphql/attachments

How to upload attachments programmatically for messages and events in Plain.

This page outlines how to upload attachments programmatically.

At a high level to upload attachments you:

* Make an API call to get an an upload url and some metadata
* You then upload your file, and metadata to that upload url.
* Use the ID of the attachment you uploaded in other API calls (e.g. create a thread or send an email).

## Step by step guide

To try this, you will need an [API key](/graphql/authentication/) with the following permission:

* `attachment:create`

<Steps>
  <Step title="Creating an upload url">
    - `fileName` is the name under which the attachment will appear in the timeline
    - `fileSizeBytes` is the exact size of the attachment in bytes
    - `c_XXXXXXXXXXXXXXXXXXXXXXXXXX` is the customer id you are uploading the attachment for

    <Tabs>
      <Tab title="Typescript SDK">
        <Snippet file="typescript-sdk/create-attachment-url.mdx" />

        Which would console log something like this:

        <Snippet file="typescript-sdk/create-attachment-url-response.mdx" />
      </Tab>

      <Tab title="GraphQL">
        The GraphQL mutation to create an attachment upload URL is the following:

        <Snippet file="graphql/create-attachment-url.mdx" />
      </Tab>
    </Tabs>
  </Step>

  <Step title="Uploading the attachment">
    In the `AttachmentUploadUrl` we created in the previous step we get back 2 fields which are needed to actually upload our attachment:

    * `uploadFormUrl`: The URL to which to upload the file to
    * `uploadFormData`: A list of key, value pairs that have to be included in the data we upload along with the actual file data.

    With this information we can now upload our actual file to Plain. To do this we need to build a form (`multipart/form-data`) with the data contained in `uploadFormData` and submit it to the `uploadFormUrl`.

    Here is some example code showing how you would do this in the Browser and from a Node server:

    <Tabs>
      <Tab title="Browser">
        <Snippet file="attachments/upload-attachment-browser.mdx" />
      </Tab>

      <Tab title="Node">
        <Snippet file="attachments/upload-attachment-node.mdx" />
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Limitations

* A maximum of **100 attachments** can be added to a message
* The **combined** size of all attachments you add to a message cannot exceed the following limits based on attachment type:
  * **Email attachments**: 6MB
  * **Chat attachments**: 100MB
  * **Slack attachments**: 50MB
  * **Microsoft Teams attachments**: 50MB
  * **Discord attachments**: 50MB
  * **Thread discussion attachments**: 50MB
  * **Note attachments**: 50MB
* The following file extensions are not allowed as attachments:
  `
  bat, bin, chm, com, cpl, crt, exe, hlp, hta, inf, ins, isp, jse, lnk, mdb, msc, msi, msp, mst, pcd, pif, reg, scr, sct, shs, vba, vbe, vbs, wsf, wsh, wsl`
* Attachments uploaded, but never referenced by a message, will be
  **deleted after 24 hours**.
* Upload URLs are only **valid for 2 hours** after which a new URL needs to be created.


# Authentication
Source: https://www.plain.com/docs/graphql/authentication



Machine Users can have multiple API Keys to make it easy to rotate keys. Every API key also has fine grained permissions.

<Steps>
  <Step title="Create a machine user">
    Go to **Settings** → **Machine Users** and click "Add Machine User"

    A Machine User has two fields:

    * **Name:** This is just visible to you and could indicate the usage e.g. "Autoresponder"
    * **Public name:** This is the name visible to customers (if the Machine User interacts with customers) e.g. "Mr Robot"
  </Step>

  <Step title="Create an API Key">
    Click "Add API Key" and select the permissions you need. When making API calls, if you have insufficient permissions, the error should tell you which permissions you need.

    The relevant documentation will tell you which permissions are required for each feature.

    Once you've made an API key you should copy it and put it somewhere safe, as you will not be able to see it again once you navigate away.
  </Step>

  <Step title="Go build things 🚀">
    That's it! Now that you have an API key you can use this with our SDKs or within any API call as a header:

    ```text  theme={null}
    Authorization: Bearer plainApiKey_xxx
    ```
  </Step>
</Steps>


# Companies
Source: https://www.plain.com/docs/graphql/companies



Within Plain every customer can belong to one company. The company is infered automatically using the customer's email address. For example if their email address ends with "@nike.com" then their company will be automatically set to "Nike".

Companies allow you to prioritise and filter your support requests.

Additionally [tiers and SLAs](https://plain.support.site/article/tiers) can be associated with a company.

<Snippet file="shared/tenants-vs-teams.mdx" />


# Get companies
Source: https://www.plain.com/docs/graphql/companies/get-companies



You can get all companies you've interacted with in your workspace using the `companies` query. This endpoint supports [Pagination](/graphql/pagination).

For this query you need the following permissions:

* `company:read`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/get-companies.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/get-companies.mdx" />
  </Tab>
</Tabs>


# Update customer company
Source: https://www.plain.com/docs/graphql/companies/update-customer-company



Plain automatically derives a customer's company for you, but you can also update it manually.

The customer in question is identified by their id (ie `c_...`).

With regards to the company, you can either specify an existing company using the ID we've generated (ie `co_...`), or pass the company domain, which we'll use to derive the rest of the company's info.

If you wish to only remove the customer's associated company, then you can pass `null` as the `companyIdentifier`.

For this mutation you need the following permissions:

* `customer:edit`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/update-customer-company.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/update-customer-company.mdx" />
  </Tab>
</Tabs>


# Customers
Source: https://www.plain.com/docs/graphql/customers



Customers that reach out to you will automatically be created in Plain without requiring any API integration.

However, using our API to manage customers proactively can be helpful when you are optimizing your support workflow.

For example:

* You can [**put customers into groups**](/graphql/customers/customer-groups/) to better organize your support queue. For example, you could group customers by pricing tier (e.g. Free Tier, Teams, Enterprise)
* You can [**create customers**](/graphql/customers/upsert/) in Plain when they sign-up on your own site so that you can reach out to them proactively without waiting for them to get in touch.
* You can [**save your own customer's ID**](/graphql/customers/upsert) for use with [**customer cards**](/customer-cards/).


# Customer groups
Source: https://www.plain.com/docs/graphql/customers/customer-groups



Customer groups can be used to group and segment your customers. For example you could organise your customers by their tier "Free", "Growth, "Enterprise" or make use of groups to keep track of customers trialing beta features.

Customers can belong to one or many groups. You can filter customer threads by group, allowing you to quickly focus on a subset of them.

This guide will show you how to add customers to groups using the API. You can also do this with the UI in Plain if you prefer.

This guide assumes you've already created some customer groups in **Settings** → **Customer Groups**.

## Add a customer to groups

A customer can be added to a customer group using the `addCustomerToCustomerGroup` mutation.

Depending on what your customer groups are you may want to call this API at different times. For example if you are grouping them by their pricing tier you will want to do this every time their tier changes.

This operation requires the following permissions:

* `customer:create`
* `customer:edit`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/add-customer-to-group.mdx" />

    Running the above would console.log:

    <Snippet file="typescript-sdk/add-customer-to-group-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/add-customer-to-group.mdx" />

    If you prefer you can also use the customer group id instead of the key. You can do this like so:

    <Snippet file="graphql/add-customer-to-group-by-group-id.mdx" />
  </Tab>
</Tabs>

## Remove a customer from groups

A customer can be removed from a customer group by using the `removeCustomerFromGroup` mutation.

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/remove-customer-from-groups.mdx" />

    Which if successful will console.log `null`
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/remove-customer-from-groups.mdx" />

    If you prefer you can also use the customer group id instead of the key. You can do this like so:

    <Snippet file="graphql/remove-customer-from-groups-by-group-id.mdx" />
  </Tab>
</Tabs>


# Delete customers
Source: https://www.plain.com/docs/graphql/customers/delete



You can delete customers with the `deleteCustomer` API, you will find this name in both our API and our SDKs.

To delete a customer you will need the customer's ID from within Plain. You can get this ID in the UI by going to a thread from that customer and pressing the 'Copy ID' button from the customer details panel on the right, or via our [fetch API](/graphql/customers/get).

Deleting a customer will trigger an asynchronous process which causes all data (such as threads) associated with that customer to be deleted.

This operation requires the following permissions:

* `customer:delete`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/delete-customer.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/delete-customer.mdx" />
  </Tab>
</Tabs>


# Fetch customers
Source: https://www.plain.com/docs/graphql/customers/get



We provide a number of methods for fetching customers:

1. [Get customers](#get-customers) (To fetch more than one customer at a time)
2. [Get customer by ID](#get-customer-by-id)
3. [Get customer by email](#get-customer-by-email)

All of these endpoints require the following permissions:

* `customer:read`

## Get customers

Our API allows you to fetch customers as a collection using `getCustomers` in our SDKs or the `customers` query in GraphQL. In both cases this endpoint supports [Pagination](/graphql/pagination).

This is a very flexible endpoint which supports a variety of options for filtering and sorting, for full details try our [API explorer](https://app.plain.com/developer/api-explorer/) or [Typescript SDK](https://github.com/team-plain/typescript-sdk/).

<Tabs items={[ 'Typescript SDK', 'GraphQL']}>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/get-customers.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/get-customers.mdx" />
  </Tab>
</Tabs>

## Get customer by ID

If you already have the ID of a customer from within Plain or one of our other endpoints you can fetch more details about them using `getCustomerById` in our SDKs or the `customer` query in GraphQL.

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/get-customer-by-id.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/get-customer-by-id.mdx" />
  </Tab>
</Tabs>

## Get customer by email

To fetch a customer by email you can use `getCustomerByEmail` in our SDKs or the `customerByEmail` query in GraphQL.

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/get-customer-by-email.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/get-customer-by-email.mdx" />
  </Tab>
</Tabs>


# Upserting customers
Source: https://www.plain.com/docs/graphql/customers/upsert

Learn how to create and update customers programmatically.

Creating and updating customers is handled via a single API called `upsertCustomer`. You will find this name in both our API and our SDKs.

When you upsert a customer, you define:

1. The identifier: This is the field you'd like to use to select the customer and is one of
   * `emailAddress`: This is the customer's email address. Within Plain email addresses are unique to customers.
   * `customerId`: This is Plain's customer ID. Implicitly if you use this as an identifier you will only be updating the customer since the customer can't have an id unless it already exists.
   * `externalId`: This is the customer's id in your systems. If you previously set this it can be a powerful way of syncing customer details from your backend with Plain.
2. The customer details you'd like to use if creating the customer.
3. The customer details you'd like to update if the customer already exists.

When upserting a customer you will always get back a customer or an error.

## Upserting a customer

This operation requires the following permissions:

* `customer:create`
* `customer:edit`
* `customerGroup:read` (Typescript SDK only)
* `customerGroupMembership:read` (Typescript SDK only)

This will:

* Find a customer with the email '[donald@example.com](mailto:donald@example.com)' (the identifier).
* If a customer with that email exists will update it (see `onUpdate` below)
* Otherwise, it will create the customer (see `onCreate` below)

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/upsert-customer.mdx" />

    Running the above would console.log:

    <Snippet file="typescript-sdk/upsert-customer-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    The GraphQL mutation is the following:

    <Snippet file="graphql/upsert-customer.mdx" />
  </Tab>
</Tabs>

The value of the `result` type will be:

* `CREATED`: if a customer didn't exist and was created
* `UPDATED`: if a customer already existed AND the values being updated **were different**.
* `NOOP`: if a customer already existed AND the values being updated **were the same**


# Error codes
Source: https://www.plain.com/docs/graphql/error-codes

If you receive an error code as part of an API call, this is where you can look up what it means

#### `input_validation`

The provided input failed validation. See field errors for details.

#### `forbidden`

Permission denied.

#### `internal`

An internal server error. The request should be retried. If the error persists, please get in touch at [help@plain.com](mailto:help@plain.com)

#### `not_found`

An entity referenced in the request is not found. For example trying to create an issue for a customer that doesn't exist.

#### `not_yet_implemented`

The API is not yet implemented. If you think it should already be implemented please get in touch at [help@plain.com](mailto:help@plain.com)

***

#### `action_not_allowed_in_demo_workspace`

The performed action is not allowed for a demo workspace.

#### `attachment_file_size_too_large`

The attachment being uploaded exceeds the limit (6MB)

#### `attachment_file_type_not_allowed`

The file type is not allowed. Banned file types: `bat`, `bin`, `chm`, `com`, `cpl`, `crt`, `exe`, `hlp`, `hta`, `inf`, `ins`, `isp`, `jse`, `lnk`, `mdb`, `msc`, `msi`, `msp`, `mst`, `pcd`, `pif`, `reg`, `scr`, `sct`, `shs`, `vba`, `vbe`, `vbs`, `wsf`, `wsh`, `wsl`

#### `attachment_not_uploaded`

The attachment ID being referenced was created, but not uploaded. Upload the attachment and try again.

#### `cannot_assign_customer_to_user`

The user that the customer is being assigned to doesn't have a role that is capable of helping the customer. Assign the "Help customers" role to the user and try again.

#### `cannot_remove_only_admin_user`

Can't remove the last user with an admin role. Assign another user the admin role as well and try again.

#### `cannot_reply_to_unsent_email`

The email being replied to has yet to be sent. Wait until the email is sent and try again.

#### `cannot_update_field`

Some Custom Timeline Entry fields can't be updated but only created (such as `timestamp`). Delete the Custom Timeline Entry and recreate it if you want to update these fields.

#### `customer_already_exists_with_email`

A customer with this email already exists in the workspace and can't be created again.

#### `customer_already_exists_with_external_id`

A customer with this external id already exists in the workspace and can't be created again.

#### `customer_already_is_status`

An attempt to change a customer to a status that the customer already is was made.

#### `customer_already_marked_as_spam`

The customer has already been marked as spam and can't be marked as spam again.

#### `customer_card_config_key_already_exists`

A Customer Card config with this key already exists in the workspace and can't be created again.

#### `customer_is_marked_as_spam`

An action was attempted but cannot be performed as the customer is marked as spam.

#### `customer_is_not_marked_as_spam`

An action was attempted but cannot be performed as it requires the customer to be marked as spam.

#### `customer_status_cannot_be_changed_to_idle`

The customer's status cannot be changed to idle, see error for reason.

#### `customer_jwt_expired`

The customer's JWT has expired. Recreate the JWT and try again.

#### `customer_jwt_invalid`

The customer's JWT is in an invalid format. Fix the contents of the JWT and try again.

#### `customer_group_has_memberships`

The customer group has memberships and can't be deleted.

#### `customer_group_key_already_exists`

A customer group with this key already exists in the workspace and can't be created again.

#### `customer_session_challenge_invalid`

The provided customer challenge digits are invalid.

#### `domain_already_taken`

The domain in the support email address is already taken by a different workspace. Currently only one workspace can use a domain. If this is an issue, please contact [help@plain.com](mailto:help@plain.com).

#### `domain_cannot_be_public`

The domain in the support email address is considered public and cannot be used.

#### `insufficient_permissions`

The user doesn't have the required permissions to create an API key that has more permissions than the user itself.

#### `issue_already_open`

Issue is already in an open state and can't be opened.

#### `issue_already_resolved`

Issue is already in a resolved state and can't be resolved.

#### `issue_already_this_issue_type`

Issue is already the provided issue type and can't be changed to it.

#### `issue_already_this_priority`

Issue is already the provided priority and can't be changed to it.

#### `linear_issue_already_linked_to_issue`

Issue is already linked to the provided Linear issue and cannot be linked again.

#### `linear_organisation_cannot_be_authorised`

The Linear OAuth flow failed. Detailed reasoning is included in the error.

#### `mark_as_read_user_must_be_assigned_to_customer`

The user trying to mark the timeline as read isn't the user that is assigned to the customer. Assign the user to the customer and try again.

#### `roles_at_least_one_admin_required`

Can't remove the role for the user as it would leave no users with the admin role in the workspace. Assign another user the admin role as well and try again.

#### `too_many_customer_card_configs`

The maximum number of Customer Card configs has been reached for this workspace.

#### `too_many_webhook_targets`

The maximum number of webhook targets has been reached for this webhook.

#### `user_account_already_exists`

A User Account already exists for the current user.

#### `user_already_this_status`

User is already in this status can can't be changed to it.

#### `user_linear_integration_not_found`

A User does not have a Linear integration setup.

#### `workspace_app_key_not_found`

The workspace app key can't be found.

#### `workspace_app_public_key_required`

A workspace app key must be provided.

#### `workspace_app_required`

A workspace app must be provided.

#### `workspace_chat_not_enabled`

Chat is disabled so chat messages can't be sent.

#### `workspace_email_domain_not_configured`

Email domain settings aren't fully configured yet. Double check the email settings page.

#### `workspace_email_domain_not_set`

A support email is not configured in the email settings. Double check the email settings page.

#### `workspace_email_forwarding_not_configured`

Email forwarding settings aren't fully configured yet. Double check the email settings page.

#### `workspace_email_not_enabled`

Email is not enabled so emails can't be sent.

#### `workspace_invite_already_accepted`

The invite has already been accepted by the user.

#### `workspace_invite_email_already_invited`

The email trying to be invited already has an outstanding invite.

#### `workspace_invite_email_already_member_of_workspace`

The email trying to be invited is already a member of the workspace.

#### `workspace_invite_email_doesnt_match`

The user trying to accept the invite has a different email than the invite is for.

#### `workspace_support_email_address_conflict`

The entered support email address is already taken by a different workspace.

#### `workspace_user_email_already_used_as_support_email`

The provided email is already used as a support email.

#### `you_shall_not_pass`

🧙 User account signup is currently blocked.


# Error handling
Source: https://www.plain.com/docs/graphql/error-handling

GraphQL queries and mutations require different error handling.

This is because we expect:

* … **queries** to generally succeed, as the three most common issues are usually unauthenticated, forbidden, or an internal server error. In the case of unauthenticated and forbidden, the API keys are invalid, while internal server errors should be retried.

* … **mutations** to return errors regularly as part of the normal business flow due to invalid inputs. Errors include rich detail which can be used and displayed to an end user.

## Query errors

Query errors aren't modeled in the GraphQL schema, but rather use [GraphQL's error extensions](https://www.apollographql.com/docs/apollo-server/data/errors/).

If the query returns the value `null`, that typically indicates that the entity is not found (equivalent to an HTTP 404 in a REST API).

The list of error extensions that can be returned by queries:

* `GRAPHQL_PARSE_FAILED`: The GraphQL operation string contains a syntax error. The request should not be retried.
* `GRAPHQL_VALIDATION_FAILED`: The GraphQL operation is not valid against the schema. The request should not be retried.
* `BAD_USER_INPUT`: The GraphQL operation includes an invalid value for a field argument. The request should not be retried.
* `UNAUTHENTICATED`: The API key is invalid. The request should not be retried.
* `FORBIDDEN`: The API key is unauthorized to access the entity being queried. The request should not be retried.
* `INTERNAL_SERVER_ERROR`: An internal error occurred. The request should be retried. If this error persists, please get in touch at [help@plain.com](mailto:help@plain.com) and report the issue.

## Mutation errors

All mutations return with an `Output` type that follow a consistent pattern of having two optional fields,
one for the result and one for the error. If the error is returned then the mutation failed.

```tsx  theme={null}
type Example {
  data: String!
}

type ExampleOutput {
  # example is the result of the mutation, is only returned if the mutation succeeded
  example: Example
  # if error is returned then the mutation failed
  error: MutationError
}
```

Every `MutationError` has the following fields (assuming you included all these fields in your query):

* **message:** Usually meant to be read by a developer and not an end user.
* **type:** one of `VALIDATION`, `FORBIDDEN`, `INTERNAL`.
  * Where `VALIDATION` means input validation failed. See the fields for details on why the input was invalid.
  * Where `FORBIDDEN` means the user is not authorized to do this mutation. See `message` for details on which permissions are missing.
  * Where `INTERNAL` means an unknown internal server error occurred. Retry in this scenario and contact [help@plain.com](mailto:help@plain.com) if the error persists.
* **code:** a unique error code for each type of error returned. This code can be used to provide a localized or user-friendly error message. You can find the [list of error codes](/graphql/error-codes) documented.
* **fields:** an array containing all the fields that errored
  * **field:** the name of the input field the error is for.
  * **message:** an English technical description of the error. This error is usually meant to be read by a developer and not an end user.
  * **type:** one of `VALIDATION`, `REQUIRED`, `NOT_FOUND`.
    * Where `VALIDATION` means the field was provided, but didn't pass the requirements of the field. See the `message` on the field for details on why.
    * Where `REQUIRED` means the field is required. String inputs may be trimmed and checked for emptiness.
    * Where `NOT_FOUND` means the input field referenced an entity that wasn't found. For example, you tried to resolve an issue that doesn't exist/was deleted.

## Typescript SDK

If you are using the Typescript SDK, errors are handled and parsed for you and you don't need to worry about the distinction between queries and mutations.

You can see the [full error types in the code of the Typescript SDK](https://github.com/team-plain/typescript-sdk/blob/main/src/error.ts) (It's open source).

This is how you can access the error when using the SDK:

```tsx  theme={null}
import { PlainClient } from '@team-plain/typescript-sdk';

export async function createCustomer() {
  const client = new PlainClient({ apiKey: 'XXX' });

  const res = await client.upsertCustomer({
    identifier: {
      emailAddress: 'jane@gmail.com',
    },
    onCreate: {
      fullName: 'Jane Fargate',
      email: {
        email: 'jane@gmail.com',
        isVerified: true,
      },
    },
    onUpdate: {},
  });

  if (res.error) {
    console.error(res.error);
  } else {
    console.log(`Created customer with id=${res.data.customer.id}`);
  }
}
```


# Events
Source: https://www.plain.com/docs/graphql/events

Log important events to have the full picture of what happened in Plain.

When helping a customer it can be useful to have context about their recent activity in your product. For example, if someone is getting in touch about a 401 error, it could be important to know that they recently deleted an API key in their settings.

Events are created via the Plain API and you have full control of what they look like using Plain's UI components.

There are two types of events

* **[Customer events](/graphql/events/create-customer-event)**: these are created in every existing thread for a customer. When a a new thread is created (e.g. by an inbound communication, or by calling the [createThread](/graphql/threads/create) endpoint) the **25** most recent events are shown.
* **[Thread events](/graphql/events/create-thread-event)**: these events belong to a single thread, and only appear in a single thread's timeline.

## UI Components

To define what each event should look like, you use the Plain UI components. All the components are documented in the [Plain UI Components](/ui-components/) section.

### Playground

The UI Components Playground lets you build and preview the component JSON used to create an event. Use this to prototype an event before starting to build your integration.

[**UI Components Playground →**](https://app.plain.com/developer/ui-components-playground/)


# Create a customer event
Source: https://www.plain.com/docs/graphql/events/create-customer-event



<Info>
  A customer event will be created in all threads that belong to the provided customer ID. If you
  want an event to appear in a specific thread use a [thread
  event](/graphql/events/create-thread-event).
</Info>

To create an event you need a customer ID.

You can get this by [upserting a customer](/graphql/customers/upsert) in Plain, from data in webhooks or other API calls you made. If you want to test this, press **⌘ + K** on any thread and then "Copy customer ID" to get an ID you can experiment with.

In this example we'll be creating the following event:

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=f168c4372479e924f08c9a04f23e8150" alt="Example event" data-og-width="1972" width="1972" data-og-height="634" height="634" data-path="public/images/events-api-key-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=71673a4fc78badf3f2eb901068dc6980 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=d70f2f75494f1aa7b24e5cb2e62d60ba 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=c929bcc2c54f5f48b3a59962eb2a0d1b 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8e943249db6f0aa7ecd17df85bd3a995 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8d801c54aef04486236abea487cb7ea8 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=f9245da75ef5d680153e0d3a5477ec8e 2500w" /></Frame>

<Tabs>
  <Tab title="Typescript SDK">
    For this you'll need an API key with the following permissions:

    * `customerEvent:create`

    <Snippet file="typescript-sdk/create-customer-event.mdx" />

    Which would console.log:

    <Snippet file="typescript-sdk/create-customer-event-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    For this you'll need an API key with the following permissions:

    * `customerEvent:create`

    <Snippet file="graphql/create-customer-event.mdx" />
  </Tab>
</Tabs>


# Create a thread event
Source: https://www.plain.com/docs/graphql/events/create-thread-event



<Info>
  A thread event will only be created in the thread ID provided. If you want an event to appear in
  all threads for a customer please use a [customer
  event](/graphql/events/create-customer-event).
</Info>

To create a thread event you need a thread ID.

You can get this by [creating a thread](/graphql/threads/create) in Plain, from data in webhooks or other API calls you made. If you want to test this, press **⌘ + K** on any thread and then "Copy thread ID" to get an ID you can experiment with.

In this example we'll be creating the following event:

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=f168c4372479e924f08c9a04f23e8150" alt="Example event" data-og-width="1972" width="1972" data-og-height="634" height="634" data-path="public/images/events-api-key-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=71673a4fc78badf3f2eb901068dc6980 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=d70f2f75494f1aa7b24e5cb2e62d60ba 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=c929bcc2c54f5f48b3a59962eb2a0d1b 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8e943249db6f0aa7ecd17df85bd3a995 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8d801c54aef04486236abea487cb7ea8 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/events-api-key-example.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=f9245da75ef5d680153e0d3a5477ec8e 2500w" /></Frame>

<Tabs>
  <Tab title="Typescript SDK">
    For this you'll need an API key with the following permissions:

    * `threadEvent:create`
    * `threadEvent:read`
    * `thread:read`
    * `customer:read`

    <Snippet file="typescript-sdk/create-thread-event.mdx" />

    Which would console.log:

    <Snippet file="typescript-sdk/create-thread-event-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    For this you'll need an API key with the following permissions:

    * `threadEvent:create`
    * `threadEvent:read`

    <Snippet file="graphql/create-thread-event.mdx" />
  </Tab>
</Tabs>


# Introduction
Source: https://www.plain.com/docs/graphql/introduction

An overview of Plain's GraphQL API.

Plain is built with this very GraphQL API we expose to you. This means that there are **no limitations** in what can be done via the API vs the UI.

These docs just highlight the most interesting and most used APIs. If you want to do something beyond what is documented here, please [reach out to us](mailto:help@plain.com) or explore our [schema](/graphql/schema) on your own!

## Key details

Our API is compatible with all common GraphQL clients with the following details:

* **API URL:** `https://core-api.uk.plain.com/graphql/v1`
* **Allowed method**: POST
* **Required headers:**
  * `Content-Type: application/json`
  * `Authorization: Bearer YOUR_TOKEN` where the token is your API key. See [authentication](/graphql/authentication/) for more details.
* **JSON body:**
  * `query`: the GraphQL query string
  * `variables`: a JSON object of variables used in the GraphQL query
  * `operationName`: the name of your GraphQL operation (this is just for tracking and has no impact on the API call or result)

If you'd like to use the **GraphQL schema to generate types** for your client code you can fetch the schema
from: `https://core-api.uk.plain.com/graphql/v1/schema.graphql`

## Your first API call

In this example, we're going to get a customer in your workspace by their email address. You can find a customer's email on the right-hand side when looking at one of their threads in Plain.

You will need an API key with the `customer:read` permission. See [authentication](/graphql/authentication/) for details on how to get an API key

<Tabs>
  <Tab title="CURL">
    You'll need to set two shell variables:

    * `PLAIN_TOKEN`: The API key
    * `PLAIN_CUSTOMER_EMAIL`: The email of the customer you want to fetch

    ```shell  theme={null}
    PLAIN_TOKEN=XXX
    PLAIN_CUSTOMER_EMAIL=XXX
    curl -X POST https://core-api.uk.plain.com/graphql/v1 \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $PLAIN_TOKEN" \
      -d '{"query":"query customerByEmail($email: String!) { customerByEmail(email: $email) { id fullName updatedAt { iso8601 } } }","variables":{"email":"'"$PLAIN_CUSTOMER_EMAIL"'"},"operationName":"customerByEmail"}'
    ```
  </Tab>

  <Tab title="Typescript SDK">
    This assumes you've installed our Typescript SDK.

    <Steps>
      <Step title="Install the SDK">`npm install @team-plain/typescript-sdk `</Step>

      <Step title="Set up the code">
        Make sure to replace the api key and email in the code:

        <Snippet file="typescript-sdk/first-api-call.mdx" />
      </Step>

      <Step title="Run it">`node script.js `</Step>
    </Steps>
  </Tab>
</Tabs>


# Labels
Source: https://www.plain.com/docs/graphql/labels



Labels are a light-weight but powerful way to categorise threads, consisting of label text coupled with an icon. Each thread can have multiple labels.

They can be added manually or programmatically. For example when a contact form is submitted, you could automatically add a label to the corresponding thread with the issue category they selected, so that you know upfront why they are getting in touch.

The available labels you can apply are defined by your label types. Label types can be created and managed in your settings (**⌘ + K** and then search for "Manage labels").

When you want to stop a label being available you can archive a label type. Archived label types are kept on existing threads in order to avoid losing valuable historic data.

Label changes can also be a starting point for integrations [via our webhooks](/webhooks/thread-labels-changed). This lets you build workflows triggered by the addition of a label.


# Add labels
Source: https://www.plain.com/docs/graphql/labels/add



You can add multiple labels to a thread with a call to `addLabels`. Label type IDs passed to this endpoint should not be archived, we return a validation error with code `cannot_add_label_using_archived_label_type` for any which are submitted.

If a label type you provide is already added to the thread we will return a validation error with code `label_with_given_type_already_added_to_thread`.

You can retrieve label type IDs in the Plain UI settings by hovering over a label type and selecting 'Copy label ID' from the overflow menu.

This operation requires the following permissions:

* `label:create`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/add-labels.mdx" />

    This will output:

    <Snippet file="typescript-sdk/add-labels-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/add-labels.mdx" />
  </Tab>
</Tabs>


# Remove labels
Source: https://www.plain.com/docs/graphql/labels/remove



You can remove labels from a thread with a call to `removeLabels`. Label IDs for this call can be retrieved by fetching a thread with the API.

This operation requires the following permissions:

* `label:delete`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/remove-labels.mdx" />

    Which if successful will console log `null`.
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/remove-labels.mdx" />
  </Tab>
</Tabs>


# Messaging
Source: https://www.plain.com/docs/graphql/messaging



We provide various methods to message your customers with the Plain API. You can use this to reach out proactively, build an autoresponder or even to handle things like waiting list access.

<CardGroup cols={2}>
  <Card title="Send emails" icon="paper-plane-top" href="/graphql/messaging/send-email">
    Send a new email in a thread ignoring previous communications.
  </Card>

  <Card title="Reply to emails" icon="paper-plane-top" href="/graphql/messaging/reply-email">
    Use this to reply to an existing inbound email in a thread.
  </Card>

  <Card title="Reply to thread" icon="reply" href="/graphql/messaging/reply-email">
    Reply to a thread automatically using the best channel.
  </Card>
</CardGroup>


# Reply to emails
Source: https://www.plain.com/docs/graphql/messaging/reply-email



You can reply to an inbound email with the `replyToEmail` API.

<Tabs>
  <Tab title="Typescript SDK">
    This operation requires the following permissions:

    * `email:create`
    * `email:read`
    * `attachment:download`

    <Snippet file="typescript-sdk/reply-email.mdx" />
  </Tab>

  <Tab title="GraphQL">
    This operation requires the following permissions:

    * `email:create`
    * `email:read`

    <Snippet file="graphql/reply-email.mdx" />
  </Tab>
</Tabs>


# Reply to threads
Source: https://www.plain.com/docs/graphql/messaging/reply-to-thread



You can reply to a thread using the `replyToThread` mutation, as long as the thread's communication channel is either `API`, `CHAT`, `EMAIL`, `SLACK` or 'MS\_TEAMS'. This information is available in the thread as the `channel` field.

If it is not possible to reply to a thread, you will get the mutation error code [`cannot_reply_to_thread`](/graphql/error-codes#cannot_reply_to_thread) and a message indicating why.

This operation requires the following permission:

* `thread:reply`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/reply-to-thread.mdx" />

    Where `res.data` is:

    <Snippet file="typescript-sdk/reply-to-thread-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/reply-to-thread.mdx" />
  </Tab>
</Tabs>

## Impersonation

<Note>
  Impersonation is exclusively available in our `Grow` plan. You can see all available plans in our
  [pricing page](https://www.plain.com/pricing).
</Note>

This feature allows you to bring native messaging between your customers and Plain, straight into your own product]\([https://plain.support.site/article/headless-portal-overview](https://plain.support.site/article/headless-portal-overview)).

With impersonation, you can reply to a thread on behalf of one of your customers: impersonated messages will show up as if they were sent by the customers themselves.

In order to impersonate a customer, provide the `impersonation` parameter in the `replyToThread` mutation, specifying the identifier of the customer you want to impersonate. You can pick any of the available customer identifiers (`emailAddress`, `customerId` or `externalId`)

```graphql  theme={null}
{
  "impersonation": {
    "asCustomer": {
      "customerIdentifier": {
        "emailAddress": "blanca@example.com"
      }
    }
  }
}
```

<Note>
  Impersonation is only possible for `API`, `CHAT`, `EMAIL` and `SLACK` threads (based on the thread's `channel` field).
</Note>

The customer message will be processed differently based on the thread's channel:

* `SLACK`: the message will appear in Slack as a new message from the impersonated customer, including their name and any other customer details
* `API` and `EMAIL`: the message will be sent as an email with the impersonated customer's email address as the "From" address, making it appear as if they sent the email directly
* `CHAT`: the message will appear in the thread as coming directly from the impersonated customer, with their name and avatar displayed

When replying to an `EMAIL` or `API` thread, you can optionally add 'Cc' and 'Bcc' recipients by using the `channelSpecificOptions` parameter:

```graphql  theme={null}
{
  "channelSpecificOptions": {
    "email": {
      // For CC'd recipients
      "additionalRecipients": [
        {
          "email": "peter@example.com",
          "name": "Peter"
        },
      ],
      // For BCC'd recipients
      "hiddenRecipients": [
        {
          "email": "finance@example.com"
        }
      ]
    }
  }
}
```

This operation requires the following permissions:

* `thread:reply`
* `customer:impersonate`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/reply-to-thread-impersonation.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/reply-to-thread-impersonation.mdx" />
  </Tab>
</Tabs>


# Send new emails
Source: https://www.plain.com/docs/graphql/messaging/send-email



As well as creating outbound emails in the UI you can also send them with the `sendNewEmail` API. This is useful for proactively reaching out about issues.

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/send-email.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/send-email.mdx" />
  </Tab>
</Tabs>


# Pagination
Source: https://www.plain.com/docs/graphql/pagination



Our GraphQL API follows the [Relay pagination spec](https://relay.dev/graphql/connections.htm).

When fetching collections from our API you can control how much data is returned. We will return 25 records per request by default and the maximum page size is 100 records.

We support two forms of page control arguments:

1. Forward pagination with `after` (cursor) & `first` (numeric count)
2. Reverse pagination with `before` (cursor) & `last` (numeric count)

Note that these must not be mixed, e.g performing a query with values for first & before will result in a validation error.

Endpoints which return paginated results will return a `pageInfo` object along with a `totalCount` field which allows you to make subsequent calls with page controls. Using the `getCustomers` API as an example this would look as follows:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/page-info-after.mdx" />

    Notice how we use the cursor information from the first page to fetch the second page. The returned `pageInfo` looks as follows:

    <Snippet file="typescript-sdk/page-info-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    This will fetch a subsequent page of 50 entries by passing in the `endCursor` from an initial query.

    <Snippet file="graphql/page-info-after.mdx" />
  </Tab>
</Tabs>


# Schema
Source: https://www.plain.com/docs/graphql/schema



If you need the schema programmatically for code generation or if you just want to read the schema you can view the [raw GraphQL schema](https://core-api.uk.plain.com/graphql/v1/schema.graphql).

You can also use the [API Explorer](https://app.plain.com/developer/api-explorer/) to learn about our API schema. This is the easiest way of discovering everything possible with the GraphQL API.

[**View API Explorer →**](https://app.plain.com/developer/api-explorer/)


# Tenants
Source: https://www.plain.com/docs/graphql/tenants



Tenants allow you to structure your customers in Plain in the same way as they are structured in your product.

For example if within your product customers are organised in a 'team' then you would create one tenant per team in your product. A tenant has an `externalId` so that you can map it back to an entity in your database.

Customers can belong to multiple tenants.

For advanced integrations with Plain you can specify a tenant when creating a thread. This is useful when building a support portal in your product as it allows you to fetch threads specific to a team in your product.

Additionally [tiers and SLAs](https://plain.support.site/article/tiers) can be associated with a tenant.

<Snippet file="shared/tenants-vs-teams.mdx" />


# Add customers to tenants
Source: https://www.plain.com/docs/graphql/tenants/add-customers



You can add a customer to multiple tenants.

When selecting the customer you can chose how to identify them. You can use the customer's email, externalId or id.

For this mutation you need the following permissions:

* `customer:edit`
* `customerTenantMembership:create`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/add-customer-to-tenants.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/add-customer-to-tenants.mdx" />
  </Tab>
</Tabs>


# Get tenants
Source: https://www.plain.com/docs/graphql/tenants/get



We provide two of methods for fetching tenants:

1. [Get tenants](#get-tenants) to fetch more than one tenant at a time.
2. [Get tenant by ID](#get-tenant-by-id)

For all of these queries you need the following permissions:

* `tenant:read`

### Get tenants

Our API allows you to fetch teanants as a collection using `getTenants` in our SDKs or the `tenants` query in GraphQL. In both cases this endpoint supports [Pagination](/graphql/pagination).

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/get-tenants.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/get-tenants.mdx" />
  </Tab>
</Tabs>

### Get tenant by ID

If you know the tenant's ID in Plain you can use this method to fetch the tenant. Generally speaking it's preferable to use [upsert](./upsert) when you have the full details of the tenant.

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/get-tenant-by-id.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/get-tenant-by-id.mdx" />
  </Tab>
</Tabs>


# Remove customers to tenants
Source: https://www.plain.com/docs/graphql/tenants/remove-customers



You can remove customers from multiple tenants in one API call.

When selecting the customer you can chose how to identify them. You can use the customer's email, externalId or id.

For this mutation you need the following permissions:

* `customer:edit`
* `customerTenantMembership:delete`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/remove-customer-from-tenants.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/remove-customer-from-tenants.mdx" />
  </Tab>
</Tabs>


# Set customer tenants
Source: https://www.plain.com/docs/graphql/tenants/set-customer-tenants



You can also set all tenants for a customer. Unlike the more specific add or remove mutations this is useful if you are sycing tenants and customers with Plain.

For this mutation you need the following permissions:

* `customer:edit`
* `customerTenantMembership:create`
* `customerTenantMembership:delete`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/set-customer-tenants.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/set-customer-tenants.mdx" />
  </Tab>
</Tabs>


# Upserting tenants
Source: https://www.plain.com/docs/graphql/tenants/upsert



When upserting a tenant you need to specify an `externalId` which matches the id of the tenant in your own backend.

For example if your product is structured in teams, then when creating a tenant for a team you'd use the team's id as the `externalId`.

To upsert a tenant you need the following permissions:

* `tenant:read`
* `tenant:create`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/upsert-tenant.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/upsert-tenant.mdx" />
  </Tab>
</Tabs>


# Threads
Source: https://www.plain.com/docs/graphql/threads



Threads are the core of Plain's data model and equivalent to tickets or conversations in other support platforms. When you use Plain to help a customer you assign yourself to a thread and then mark the thread as `Done` once you're done helping.

Threads are automatically created when a new email is received but can also be created via the API (when a customer submits a contact form for example).

Threads have [a status](https://plain.support.site/article/statuses) and can be assigned to multiple users.

Threads belong to one customer but can contain multiple email threads and customers.

An example thread looks like this:

<Note>
  The below is only showing a subset fields a thread has. Since our API is a GraphQL API you decide
  which fields you need when you make API requests. Use our [API
  explorer](https://app.plain.com/developer/api-explorer) to discover the full schema of threads.
</Note>

<Snippet file="typescript-sdk/threads-response.mdx" />


# Assignment
Source: https://www.plain.com/docs/graphql/threads/assignment



Threads can be assigned to users or machine users. The latter is useful if you want a bot to handle or are building a complex automation of some kind.

### Assigning a thread

To assign threads you need an API key with the following permissions:

* `thread:assign`
* `thread:read`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/assign-thread.mdx" />

    Where `res.data` is the full thread:

    <Snippet file="typescript-sdk/assign-thread-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/assign-thread.mdx" />
  </Tab>
</Tabs>

## Unassigning threads

To unassign threads you need an API key with the following permissions:

* `thread:unassign`
* `thread:read`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/unassign-thread.mdx" />

    Where `res.data` is the full thread like with assignment.
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/unassign-thread.mdx" />
  </Tab>
</Tabs>


# null
Source: https://www.plain.com/docs/graphql/threads/autoresponders



Plain provides native [workspace level auto-responses](https://plain.support.site/article/auto-responses), however for more complex cases you may want to implement your own custom autoresponder.

To achieve this you can set up endpoint(s) to be notified of one or more [webhooks](/webhooks) from Plain. We would typically recommend listening for the [thread created](/webhooks/thread-created) webhook as this will allow you the option of responding to any Thread whether it was created via email, Slack or a contact form.

If you want to only reply to emails, you can use the [email received](/webhooks/thread-email-received) webhook. This will trigger for all emails, not just the first one in a thread, so you should check the `isStartOfThread` field provided in the webhook payload to ensure you only reply to the first message.

<Warning>
  Note that if you subscribe to both `thread.thread_created` and `thread.email_received` you may
  receive two events for the same email, since we create a new thread for emails which don't belong
  to an existing thread. In order to avoid replying to the same message twice please check the
  `isStartOfThread` field in the `thread.email_received` payload.
</Warning>

Once you have received an event and decided how to respond you can use the `replyToThread` mutation to send a reply back to the customer. See our [API explorer](https://app.plain.com/developer/api-explorer/) or [Typescript SDK](https://github.com/team-plain/typescript-sdk/) for more details.


# Create threads
Source: https://www.plain.com/docs/graphql/threads/create



Creating a thread is useful in scenarios where you want to programmatically start a support interaction.

You can do this in many different scenarios but the most common use-cases are when a contact form is submitted or when you want to provide proactive support off the back of some event or error happening in your product.

A thread is created with an initial 'message' composed out of [UI components](/ui-components). You have full control over the structure and appearance of the message in Plain.

To create a thread you need a `customerId`. You can get a customer id by [creating the customer](/graphql/customers/upsert) in Plain first.

<Tabs>
  <Tab title="Typescript SDK">
    Since the Typescript SDK expands a lot of fields you will need an API key with the following permissions:

    * `label:create`
    * `label:read`
    * `labelType:read`
    * `machineUser:read`
    * `customer:read`
    * `user:read`
    * `thread:create`
    * `thread:edit`
    * `thread:read`
    * `threadField:create`
    * `threadField:update`
    * `threadField:read`

    <Snippet file="typescript-sdk/create-thread.mdx" />

    Where `result.data` is:

    <Snippet file="typescript-sdk/create-thread-response.mdx" />
  </Tab>

  <Tab title="GraphQL">
    To create a thread, you need an API key with the following permissions:

    * `thread:create`
    * `thread:read`

    <Snippet file="graphql/create-thread.mdx" />
  </Tab>
</Tabs>


# Changing status
Source: https://www.plain.com/docs/graphql/threads/status-changes



Threads can be in one of 3 statuses:

* `Todo`
* `Snoozed`
* `Done`

When you log into Plain you can filter threads by these statuses.

When threads are created they default to `Todo`.

To change a threads status you need an API key with the following permissions:

* `thread:edit`
* `thread:read`

### Mark thread as `Done`

When any activity happens in a thread, it will move back to `Todo`.

Unlike traditional ticketing software, we expect a ticket to move between `Todo` and `Done` a number of times in the course of helping a customer. This will not break or influence any metrics. `Done` in Plain means "I'm done for now, there is nothing left for me to do".

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/mark-thread-as-done.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/mark-thread-as-done.mdx" />
  </Tab>
</Tabs>

### Snooze thread

You can snooze threads for a duration of time defined in seconds.

When any activity happens in a thread, it will be automatically unsnoozed and move to `Todo`. Otherwise threads will be unsnoozed when the timer runs out.

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/snooze-thread.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/snooze-thread.mdx" />
  </Tab>
</Tabs>

### Mark thread as `Todo`

This is useful if you mistakenly marked a thread as `Done` or snoozed a thread and want to unsnooze it. Otherwise just write a message or do what you want to do and the thread will be automatically moved back to do **Todo**.

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/mark-thread-as-todo.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/mark-thread-as-todo.mdx" />
  </Tab>
</Tabs>


# Thread fields
Source: https://www.plain.com/docs/graphql/threads/thread-fields



Thread fields allow you to extend Plain's thread data model. The thread fields which you want to support have to conform to a schema configured in **Settings** → **Thread fields**.

Thread fields can be nested and be either a boolean, text or a string enum.

Thread fields can be required. When they are required, their value must be set in order for the thread to be marked as done.

For interacting with thread fields via the API, every field has a `key` defined in its schema. Keys make it possible to quickly refer to a thread field without having to know its ID in the schema. For example if you have a field called "Product Area" the key you might choose for the key to be `product_area`.

### Upsert a thread field

To upsert a thread field you need an API key with the following permissions:

* `threadField:create`
* `threadField:update`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/upsert-thread-field.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/upsert-thread-field.mdx" />
  </Tab>
</Tabs>

### Delete a thread field

To delete a thread field you need an API key with the following permissions:

* `threadField:delete`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/delete-thread-field.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/delete-thread-field.mdx" />
  </Tab>
</Tabs>


# Tiers & SLAs
Source: https://www.plain.com/docs/graphql/tiers



Within Plain you can organise [companies](https://plain.support.site/article/companies) and [tenants](https://plain.support.site/article/tenants) into Tiers. Tiers should match your pricing tiers (e.g. "Enterprise", "Pro", "Free", etc.).

This allows you to prioritise and filter your support requests by tier.

Tiers also add support for defining [SLAs](https://plain.support.site/article/tiers) so you can enforce a first-response time for different support tiers within your product or pricing.

Typically, tiers are created via the UI in Plain and then tenants and companies are added and removed via the API when this happens in your product so Plain is in sync.


# Add companies and tenants to tiers
Source: https://www.plain.com/docs/graphql/tiers/add-members



You can add multiple tenants and companies to a tier in a single mutation.

Companies and tenants can only be in a single tier.

For this mutation you need the following permissions:

* `tierMembership:read`
* `tierMembership:create`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/add-members-to-tier.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/add-members-to-tier.mdx" />
  </Tab>
</Tabs>


# Get tiers
Source: https://www.plain.com/docs/graphql/tiers/get



For all of these queries you need the following permission:

* `tier:read`

## Get tiers

Our API allows you to fetch tiers as a collection using `getTiers` in our SDKs or the `tiers` query in GraphQL. In both cases this endpoint supports [Pagination](/graphql/pagination).

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/get-tiers.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/get-tiers.mdx" />
  </Tab>
</Tabs>

### Get tier by ID

If you know the tiers's ID in Plain you can use this method to fetch the tier.

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/get-tier-by-id.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/get-tier-by-id.mdx" />
  </Tab>
</Tabs>


# Remove companies and tenants to tiers
Source: https://www.plain.com/docs/graphql/tiers/remove-members



You can remove companies and tenants from the tiers they are part of manually in the UI or via the API.

For this mutation you need the following permissions:

* `tierMembership:read`
* `tierMembership:delete`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/remove-members-from-tier.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/remove-members-from-tier.mdx" />
  </Tab>
</Tabs>


# Update company tier
Source: https://www.plain.com/docs/graphql/tiers/update-company-tier



If you want to explicitly set the tier for a company you can do so using this mutation. If instead you want to add many companies to a tier at once, you can use the [add members mutation](./add-members).

For this mutation you need the following permissions:

* `tierMembership:read`
* `tierMembership:create`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/update-company-tier.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/update-company-tier.mdx" />
  </Tab>
</Tabs>


# Update tenant tier
Source: https://www.plain.com/docs/graphql/tiers/update-tenant-tier



If you want to explicitly set the tier for a tenant you can do so using this mutation. If instead you want to add many companies to a tier at once, you can use the [add members mutation](./add-members).

For this mutation you need the following permissions:

* `tierMembership:read`
* `tierMembership:create`

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/update-tenant-tier.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/update-tenant-tier.mdx" />
  </Tab>
</Tabs>


# Typescript SDK
Source: https://www.plain.com/docs/graphql/typescript-sdk





# mTLS
Source: https://www.plain.com/docs/mtls



All outbound requests made to your **webhook targets** and **customer card endpoints** include a client TLS certificate which you can verify to achieve mutual authentication.

This certificate is self-signed. In order to verify it, we provide our CA's certificate (in PEM format), which you will need to add to your server/truststore:

```
-----BEGIN CERTIFICATE-----
MIIDDzCCAfegAwIBAgIUPLCyLvion+WDNw0V8HAZEZL5VjswDQYJKoZIhvcNAQEL
BQAwFjEUMBIGA1UEAwwLUGxhaW5NdGxzQ0EwIBcNMjQxMDEwMDkwMzMzWhgPMjEy
NDA5MTYwOTAzMzNaMBYxFDASBgNVBAMMC1BsYWluTXRsc0NBMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvikyF2YpU4zEYUWVYMc5P07CPQgtP6Agoia9
mElydDTReTXW9Rle0apHKNS8OUk8S6qtA5raEh8VT2HOZBUTZb16A1vl54be+LK7
imm7csEsU+FbHbfx9rRbisESu6Mkvf5qklovgcg5UfI4IrmQK3POB6pMBCcmdjyZ
udbx6YSrV5LZLth7Gxq9lcPuwzzpv2DWZTr1GGAQ46UNLXNo4+4IQYtgjThRAl4m
IBbezmiXqpi9N/7ay+P9kb4TZDQohentJu/1+y6Bj8Mxk86kq0KLlYfrEbm86lGp
mJ8s3R5luh98muRT4NdKeoHGf96UAqUq21i00TDJ/PklqardWQIDAQABo1MwUTAd
BgNVHQ4EFgQUlYHkn4D7QBvBudbhtq2M+f8CzpAwHwYDVR0jBBgwFoAUlYHkn4D7
QBvBudbhtq2M+f8CzpAwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOC
AQEAMMLZc8zu7AqP+c2Pms6kRkp9Wr/C6QmXMuhHC98RZL1VcmZhE2P0lg/t644o
prYX8yf7Z2SRZgNb2s8oekPpuI2U2WFC4eam1dK5kS4ux7IgaXZkuB8DyZVSo1WO
KeIb2IYmXZ6hflnFNsTRjhe/Bkb7uVVw5jMaPfxWqPmeHtgUIIoh7nYj+ZnqV5Jz
FQFDb+dZzZDol/Wa3XKm7w96MrX/tanAKTygIkXyjqCrjxTI26latBQV2OPADrRO
uagGFG2G0o56wC8LTJdmceZfWYmVBLawSibj75Av8fwHgXK+XAi05m2GuVOQAfLq
yuMQLHrNDReQDB1tylx13b6meg==
-----END CERTIFICATE-----
```

<Info>
  If you serve your API through AWS API Gateway, you can easily do this by [enabling mTLS and
  uploading the
  certificate](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html)
  above as the truststore.
</Info>


# Request signing
Source: https://www.plain.com/docs/request-signing



We sign outbound requests we make to your target URLs with a HMAC signature using a shared secret key. This allows you to verify that the request was made by Plain and not a third party.

## How to verify

Your workspace has a global HMAC secret, this secret can be viewed and (re)generated by workspace admins in **Settings** → **Request signing**.

If you have a HMAC secret set up, when you receive a request from Plain you will see a header `Plain-Request-Signature` with the HMAC signature.
You can verify this signature by hashing the request body with your HMAC secret and comparing it to the signature in the header.

**The signature is a HMAC-SHA256 hash of the request body, encoded as a hexadecimal string.**

### Node example

```javascript  theme={null}
const crypto = require('crypto');

// You may need to stringify the request body if you are using a library that parses it to a javascript object
const requestBody = JSON.stringify(request.body);

const incomingSignature = request.headers['Plain-Request-Signature'];
const expectedSignature = crypto
  .createHmac('sha-256', '<HMAC SECRET>')
  .update(requestBody)
  .digest('hex');

if (incomingSignature !== expectedSignature) {
  return response.status(403).send('Forbidden');
}
```


# UI Components
Source: https://www.plain.com/docs/ui-components



UI components are a way of describing some UI when creating threads or [events](https://plain.support.site/article/events) or building [customer cards](https://plain.support.site/article/customer-cards).

For example - this is a button that links to Stripe.

```json  theme={null}
{
  "componentLinkButton": {
    "linkButtonUrl": "http://stripe.com/",
    "linkButtonLabel": "View in Stripe"
  }
}
```

and it looks like this:

<Frame>
    <img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5a0db8257af49456ee808657eb879aa1" alt="Example button linking to stripe" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-link-button-stripe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=c4f5a9fb7cd1357583e6f68c9afa251b 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=75c3c76d540688cb7276261d2c0ecdcc 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=ad7deba75cbc80982acc0b7150bd4431 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=bef34edd15d3df00fd541e7a9d665731 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=a2c3a5e142c9424b86aa3749a1525701 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button-stripe.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=e7660842d3d6ed1fcbec384b252a8575 2500w" />
</Frame>

In the GraphQL API schema, we have two separate unions for Custom Timeline Entry Components and Customer Card
Components, but both unions share the same types therefore they can be treated as the same.

To see UI components in action you can experiment with them in the [UI components playground](https://app.plain.com/developer/ui-components-playground/)


# Badge
Source: https://www.plain.com/docs/ui-components/badge

Useful for statuses or when you need to attract attention to something.

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-badge.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=abe7478ec1dc7351f4f83f5ccbb6d1e6" alt="Example badges" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-badge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-badge.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=1c19909ef5b2edb1d09659a02797461e 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-badge.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8f8c1c9dbfa4ed10b4e9d68b54c83d13 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-badge.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=89d8c6823e057e0278da06c60a7140d1 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-badge.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=489b862d414eb0e696402358872cfcb6 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-badge.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=10734c219e4e548a03f7d11440583902 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-badge.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=2f7bcc1dc8bbd927d66d1f231e8356fd 2500w" /></Frame>

A badge has the following properties:

* `badgeLabel`: the text that should be displayed on the badge
* `badgeColor`: one of `GREY`, `GREEN`, `YELLOW`, `RED`, `BLUE`

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-badge.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-badge.mdx" />
  </Tab>
</Tabs>


# Container
Source: https://www.plain.com/docs/ui-components/container

Useful when you need to create a bit of structure.

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=0004c23b00a957648fc806df44b36c9a" alt="Example container" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-container.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=f06050e39d008bd20637613a6f24b70b 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=30fc9ef139fac29d52e45fee8eb4b0cb 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=bf34459725c80bed6fb0b53f539a78af 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=1a0720f29972fc7b46cab78cb7edf7ea 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=a3f93995d1ffd932ad709c8bf5dc3074 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=18ea07314d952e4aa1b6ca903bef573c 2500w" /></Frame>

A container has the following properties:

* `containerContent` (min 1): an array of components.

Allowed components within a Container are:

* [Badge](/ui-components/badge)
* [CopyButton](/ui-components/copy-button)
* [Divider](/ui-components/divider)
* [LinkButton](/ui-components/link-button)
* [Row](/ui-components/row)
* [Spacer](/ui-components/spacer)
* [Text](/ui-components/text)
* [PlainText](/ui-components/plain-text)

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-container.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-container.mdx" />
  </Tab>
</Tabs>


# CopyButton
Source: https://www.plain.com/docs/ui-components/copy-button

Useful if you have any IDs or other details you want to copy for use in messages or outside of Plain.

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5bd714d7543fdbf68cd0fcaaa083e8c4" alt="Example copy button" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-copy-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=3fe1ffdc916132f41747f147d7d2b776 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8ec044f8c1dea26db21619ee9f96e8ed 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=d46c23227f0c4eb6c9652ac89f24a37b 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=20cf5bb3f6465048c002ae636e7e2f71 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=4029bf2e012a22dd444ad5f7c0044ad3 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5999b3cef45c547e413aa4ee8d185096 2500w" /></Frame>

A copy button has the following properties:

* `copyButtonTooltipLabel` (optional): the text that should be displayed on hover. Defaults to the value if not
  provided.
* `copyButtonValue`: the value that should be copied to the user's clipboard after clicking the button

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-copy-button.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-copy-button.mdx" />
  </Tab>
</Tabs>


# Divider
Source: https://www.plain.com/docs/ui-components/divider

Useful when you need a bit of structure.

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-divider.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=485fb9eb03e1e3b75005c867540520fe" alt="Example divider" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-divider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-divider.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=b6074a001e984253fe109f85d6f8b9d0 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-divider.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=e16130cebf2304db36ef113a101994c3 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-divider.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=9be6645eabcc9a355e5e0f6cf44f33ae 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-divider.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=cb98a0a23dab4da2431c1736051a1060 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-divider.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=20d3bc062836d999ed5a7ebebcfef393 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-divider.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=b6d2f3b4b6d4a824a9a887fac403eab8 2500w" /></Frame>

A divider has the following properties:

* `dividerSpacingSize` (optional): the spacing the divider should have before and after the component. One of `XS`, `S`,
  `M`, `L`, `XL`. Defaults to `S`.

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-divider.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-divider.mdx" />
  </Tab>
</Tabs>


# LinkButton
Source: https://www.plain.com/docs/ui-components/link-button

Useful when you want to link somewhere external (e.g. your own admin tool or payment provider)

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=9346d0a520f270eb3fdd8bb93410433e" alt="Example link button" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-link-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=6c712d7f62b7d3aaf362f4d323672085 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=33b619c8914000b05a0969f61396b227 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=1524d18f379c910d4b3460ce47ef4360 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=69054deede26c6a569e4a5a262cb6d90 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=29097c1c067ef743824daf2d0e65fd74 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-link-button.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=70076d91ad89876ae0f1c10d1ce25b44 2500w" /></Frame>

A link button has the following properties:

* `linkButtonLabel`: the text of the button
* `linkButtonUrl`: the URL the button should open in a new tab

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-link-button.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-link-button.mdx" />
  </Tab>
</Tabs>


# PlainText
Source: https://www.plain.com/docs/ui-components/plain-text

Useful when you want to show any text that should not have any formatting (is not Markdown). If you want markdown please use [Text](/ui-components/text).

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=c3b25fca68dd58308a79128904ee16b8" alt="Example link button" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-plain-text.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=cf15eca8cc5d5e2b58b8995622c4108c 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=595d8edc4dd88bf4a1a7762ec18c8540 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5b6c590c08bc94c3f374cf07310c55c9 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=240514eced321a6b141dcd7c2e9b6625 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=fd59d1a5000113cead2414bb690a9ab0 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=c227c92d97fc1b292bd6e8313e0db1d2 2500w" /></Frame>

The plain text component has the following properties:

* `plainText`: the plain text
* `plainTextSize` (optional): one of `S`, `M`, `L`, defaults to `M`
* `plainTextColor` (optional): one of `NORMAL`, `MUTED`, `SUCCESS`, `WARNING`, `ERROR`, defaults to `NORMAL`

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-plain-text.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-plain-text.mdx" />
  </Tab>
</Tabs>


# Row
Source: https://www.plain.com/docs/ui-components/row

Useful when you need to show two things next to each-other.

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=6ce2bf713d71187a30586c634d3bdcfc" alt="Example row" data-og-width="1664" width="1664" data-og-height="636" height="636" data-path="public/images/ui-component-row.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=920dff4f7347ed43b75a60ce23ee92a0 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=6032633c171f82101d8ba39f8c4ac276 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=9a076c96015d9a4bbf570e02fb98ec08 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8ecd1afc79f1022fa2c963d69e6a5c0d 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=81f7e53adb543dbb7f99c3d456f99e65 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=2d92c0a5437188bb3e418ed91c506430 2500w" /></Frame>

The row component has the following properties:

* `rowMainContent` (min 1): an array of row components
* `rowAsideContent` (min 1): an array of row components

The following components can be used in a row:

* [Badge](/ui-components/badge)
* [CopyButton](/ui-components/copy-button)
* [Divider](/ui-components/divider)
* [LinkButton](/ui-components/link-button)
* [Spacer](/ui-components/spacer)
* [Text](/ui-components/text)
* [PlainText](/ui-components/plain-text)

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-row.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-row.mdx" />
  </Tab>
</Tabs>


# Spacer
Source: https://www.plain.com/docs/ui-components/spacer



<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-spacer.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=78d1e68c020b90ebb29cf098007f24e4" alt="Example spacer" data-og-width="1664" width="1664" data-og-height="526" height="526" data-path="public/images/ui-component-spacer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-spacer.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=2d0c73a584c8902a71199ca12469c6b0 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-spacer.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=24988f9db188b4626a4ef142419b0e70 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-spacer.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=dc8cc4375801adb13035c5c3fc519d00 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-spacer.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=d37fe0bb6ce4f2ac46e5417d5d731e5e 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-spacer.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=73d2536826eff1a44eb567d0cc04aa27 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-spacer.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=4f80998e3ce902edce6bf10ceda70105 2500w" /></Frame>

A link button has the following properties:

* `spacerSize`: the amount of space the component should take up. One of `XS`, `S`, `M`, `L`, `XL`.

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-spacer.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-spacer.mdx" />
  </Tab>
</Tabs>


# Text
Source: https://www.plain.com/docs/ui-components/text



<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5e22ab88c83d86088afaffa9c0387cca" alt="Example text" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-text.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=9a94b857b76cab657116c6c7ced35a23 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=2ef2faba55d5bd2156ed9a1677a2f983 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=99ec373848a5159a1ad129d44a5aee4f 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=e78285aa9c8ec2e65fa34ae39d5c653a 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=cc568e2b9891bda887eaf3b37f735cfa 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=997532481a6eef89e0847aa462e3b22a 2500w" /></Frame>

The text component has the following properties:

* `text`: the text. Can include a subset of markdown (bold, italic, and links).
* `textSize` (optional): one of `S`, `M`, `L`, defaults to `M`
* `textColor` (optional): one of `NORMAL`, `MUTED`, `SUCCESS`, `WARNING`, `ERROR`, defaults to `NORMAL`

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-text.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-text.mdx" />
  </Tab>
</Tabs>


# Webhooks
Source: https://www.plain.com/docs/webhooks



Webhooks allow you to get notified about events happening in your Plain workspace. You can react to these events in many ways, such as:

* Assigning threads to users based on business requirements (urgency, customer value, recurrency, etc.)
* Creating an AI-powered auto-responder
* Categorising threads by adding labels based on the their content
* Triggering internal incidents (by identifying patterns in inbound messages)
* Tracking metrics from your customer support team

## Receiving events from Plain

Events happening in your workspace ('Plain events') are delivered as Webhook requests.

In order to receive webhook requests, you need a **publicly available HTTPS** endpoint. Plain will make
an `HTTP POST` request to this endpoint whenever an event you are interested in occurs.

Once your endpoint is ready, you may create a *webhook target* in Plain. A webhook target tells Plain what events you
are interested in and where to send those events.

You can create it by going to **Settings** → **Webhooks**, then clicking on '+ Add webhook target'

Then, you need to choose a name (e.g. 'Customer notifications'), the URL of your webhook endpoint, the events you want
to receive and whether you want to enable it straight away.

You can create up to **25 webhook targets** per workspace.

<Warning>
  Plain events may contain Personally Identifiable Information (PII). If you want to test webhooks
  with a production workspace, take the necessary precautions to avoid leaking PII to untrusted
  parties.
</Warning>

<Note>
  We have created a repository where you will find instructions on how to create a webhook endpoint
  using different programming languages. You can find it
  [here](https://github.com/team-plain/webhooks-resources/tree/main/servers).
</Note>

## Security

Webhook requests are always sent through HTTPS.

If you want, you can include basic authentication credentials in your webhook target's URL (`https://username:password@example.com`) which will then be sent along the webhook request in an `Authorization` header:

```text  theme={null}
Authorization: Basic cGxhaW46cm9ja3M=
```

Plain also supports [request signing](/request-signing) and [mTLS](/mtls) to verify that the request was made by Plain and not a third party.

## Delivery semantics

Plain guarantees **at-least-once** delivery of webhook requests. As such, you should make sure your webhook endpoint is idempotent. The `id` field in the [webhook request body](#body) can be used as an idempotency key.

## Handling webhook requests

Plain considers a webhook request to be successfully delivered if your endpoint returns a **2xx** HTTP status code. The contents of the response body are ignored.

Any other HTTP status code will be considered a failure, **including redirects**, which are explicitly forbidden.

## Retry policy

When a webhook request fails, Plain will keep retrying it during the **\~5 days** after the first request. The delay between
retries is set by the following table:

| Retry # | Delay | Approximate time since first attempt |
| ------- | ----- | ------------------------------------ |
| 1       | 10s   | 10s                                  |
| 2       | 30s   | 40s                                  |
| 3       | 5m    | 6m                                   |
| 4       | 30m   | 36m                                  |
| 5       | 1h    | 1.5h                                 |
| 6       | 3h    | 4.5h                                 |
| 7       | 6h    | 10.5h                                |
| 8       | 12h   | 22.5h                                |
| 9       | 1d    | 2d                                   |
| 10      | 1d    | 3d                                   |
| 11      | 1d    | 4d                                   |
| 12      | 1d    | 5d                                   |

Plain keeps track of all the webhook delivery attempts and their results. Each webhook request
includes [some metadata](#webhook-metadata) that you can use in order to know which delivery attempt it is currently
being processed.

## The webhook request

Webhook requests are sent as an `HTTP POST` request to the webhook target URL.

### Headers

* `Accept`: `application/json`
* `Content-Type`: `application/json`
* `User-Agent`: `Plain-Webhooks/1.0 (plain.com; help@plain.com)`
* `Plain-Workspace-Id`: The ID of the workspace where the Plain event originated
* `Plain-Webhook-Target-Id`: The ID of the webhook target this webhook request is being sent to
* `Plain-Webhook-Target-Version`: The [version](/webhooks/versions.mdx) of the webhook target this webhook request is being sent to
* `Plain-Webhook-Delivery-Attempt-Id`: The ID of the delivery attempt. It will be different on every delivery attempt
* `Plain-Webhook-Delivery-Attempt-Number`: The current delivery attempt number (starts at 1)
* `Plain-Webhook-Delivery-Attempt-Timestamp`: The time at which the delivery attempt was made. In UTC and formatted as
  ISO8601. E.g. `1989-10-28T17:30:00.000Z`
* `Plain-Event-Type`: The Plain event's type
* `Plain-Event-Id`: The ID of the Plain event. It remains the same across all of the delivery attempts

An additional `Authorization` header is sent if the webhook target URL contains authentication credentials.

### Body

The request body is a `JSON` object with the fields below.

The JSON schema for Plain the webhook request body can be found [here](https://core-api.uk.plain.com/webhooks/schema/latest.json).

| Field             | Type     | Description                                                                                              |
| ----------------- | -------- | -------------------------------------------------------------------------------------------------------- |
| `id`              | `string` | The ID of the Plain event. It remains the same across all of the delivery attempts                       |
| `type`            | `string` | The Plain event's type                                                                                   |
| `webhookMetadata` | `object` | Metadata associated with the webhook request. See [Webhook Metadata](#webhook-metadata) for more details |
| `timestamp`       | `string` | The Plain event's timestamp. In UTC and formatted as ISO8601. E.g. `1989-10-28T17:30:00.000Z`            |
| `workspaceId`     | `string` | The ID of the workspace where the Plain event originated                                                 |
| `payload`         | `object` | The Plain event's payload [(Example)](/webhooks/thread-created);                                         |

### Webhook Metadata

All the following fields are also sent as [HTTP headers](#headers).

| Field                             | Type     | Description                                                                                                                                             |
| --------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `webhookTargetId`                 | `string` | The ID of the webhook target this webhook request is being sent to. This is the ID that you will find under **Settings -> Webhooks** in the Support App |
| `webhookTargetVersion`            | `string` | The [version](/webhooks/versions.mdx) of the webhook target this webhook request is being sent to.                                                      |
| `webhookDeliveryAttemptId`        | `string` | The ID of the delivery attempt. It will be different on every delivery attempt                                                                          |
| `webhookDeliveryAttemptNumber`    | `string` | The current delivery attempt number (starts at 1)                                                                                                       |
| `webhookDeliveryAttemptTimestamp` | `string` | The time at which the delivery attempt was made. In UTC and formatted as ISO8601. E.g. `1989-10-28T17:30:00.000Z`                                       |


# Customer created
Source: https://www.plain.com/docs/webhooks/customer-created



This event is fired when a new customer is created in your workspace.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/customer-created.mdx" />


# Customer deleted
Source: https://www.plain.com/docs/webhooks/customer-deleted



This event is fired when a customer is deleted from your workspace.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/customer-deleted.mdx" />


# Customer Group Membership Changed Event
Source: https://www.plain.com/docs/webhooks/customer-group-membership-changed



This event is fired whenever a customer is added or removed from a customer group.

The `changeType` field allows you to know what kind of change has occurred. It can be one of the following:

* `ADDED`: a customer group membership was added
* `REMOVED`: a customer group membership was removed

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/customer-group-changed.mdx" />


# Customer updated
Source: https://www.plain.com/docs/webhooks/customer-updated



This event is fired when a customer is updated in your workspace. You can expect this event:

* when a customer is marked as spam
* when a customer is un-marked as spam
* when the details of a customer are updated

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/customer-updated.mdx" />


# Thread assignment transitioned
Source: https://www.plain.com/docs/webhooks/thread-assignment-transitioned



This event is fired when the assignee of a thread changes or a thread is unassigned.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-assignment-transitioned.mdx" />


# Chat received
Source: https://www.plain.com/docs/webhooks/thread-chat-received



This event is fired when a chat message from a customer is received.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-chat-received.mdx" />


# Chat sent
Source: https://www.plain.com/docs/webhooks/thread-chat-sent



This event is fired when a chat message is sent to a customer in a thread.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-chat-sent.mdx" />


# Thread created
Source: https://www.plain.com/docs/webhooks/thread-created



This event is fired when a new thread is created in your workspace.

You can subscribe to this event if you want to build an [autoresponder](/graphql/threads/autoresponders).

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-created.mdx" />


# Email received
Source: https://www.plain.com/docs/webhooks/thread-email-received



This event is fired when an email is received in your workspace.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-email-received.mdx" />


# Email sent
Source: https://www.plain.com/docs/webhooks/thread-email-sent



This event is fired when an email is sent in your workspace.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-email-sent.mdx" />


# Thread Field created
Source: https://www.plain.com/docs/webhooks/thread-field-created



This event is fired when a new thread field is created in your workspace.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-field-created.mdx" />


# Thread Field deleted
Source: https://www.plain.com/docs/webhooks/thread-field-deleted



This event is fired when a thread field is deleted in your workspace.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-field-deleted.mdx" />


# Thread Field updated
Source: https://www.plain.com/docs/webhooks/thread-field-updated



This event is fired when a thread field is updated in your workspace.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-field-updated.mdx" />


# Thread labels changed
Source: https://www.plain.com/docs/webhooks/thread-labels-changed



This event is fired when labels are added to or removed from a thread.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-labels-changed.mdx" />


# Note created
Source: https://www.plain.com/docs/webhooks/thread-note-created



This event is fired when a note is created in a thread.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-note-created.mdx" />


# Thread priority changed
Source: https://www.plain.com/docs/webhooks/thread-priority-changed



This event is fired when the priority of a thread changes.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

```json  theme={null}
{
  "timestamp": "2023-10-19T21:20:07.612Z",
  "workspaceId": "w_01GST0W989ZNAW53X6XYHAY87P",
  "payload": {
    "eventType": "thread.thread_priority_changed",
    "previousThread": {
      "id": "th_01HD44FHMCDSSWE38N14FSYV6K",
      "customer": {
        "id": "c_01HD44FHDPG82VQ4QNHDR4N2T0",
        "email": {
          "email": "peter@example.com",
          "isVerified": false,
          "verifiedAt": null
        },
        "externalId": null,
        "fullName": "Peter Santos",
        "shortName": "Peter",
        "markedAsSpamAt": null,
        "markedAsSpamBy": null,
        "customerGroupMemberships": [],
        "createdAt": "2023-10-19T14:12:25.142Z",
        "createdBy": {
          "actorType": "system",
          "system": "email_inbound_handler"
        },
        "updatedAt": "2023-10-19T21:18:12.863Z",
        "updatedBy": {
          "actorType": "user",
          "userId": "u_01H1V4NA10RMHWFBXB6A1ZBYRA"
        }
      },
      "title": "Unable to tail logs",
      "previewText": "Hey, I am currently unable to tail the logs of the service svc-8af1e3",
      "priority": 3,
      "externalId": null,
      "status": "TODO",
      "statusChangedAt": "2023-10-19T21:18:12.862Z",
      "statusChangedBy": {
        "actorType": "user",
        "userId": "u_01H1V4NA10RMHWFBXB6A1ZBYRA"
      },
      "statusDetail": null,
      "assignee": null,
      "assignedAt": null,
      "labels": [],
      "firstInboundMessageInfo": {
        "timestamp": "2023-10-19T14:12:25.733Z",
        "messageSource": "EMAIL"
      },
      "firstOutboundMessageInfo": null,
      "lastInboundMessageInfo": {
        "timestamp": "2023-10-19T14:12:25.733Z",
        "messageSource": "EMAIL"
      },
      "lastOutboundMessageInfo": null,
      "supportEmailAddresses": ["help@example.com"],
      "createdAt": "2023-10-19T14:12:25.266Z",
      "createdBy": {
        "actorType": "system",
        "system": "email_inbound_handler"
      },
      "updatedAt": "2023-10-19T21:18:12.862Z",
      "updatedBy": {
        "actorType": "user",
        "userId": "u_01H1V4NA10RMHWFBXB6A1ZBYRA"
      }
    },
    "thread": {
      "id": "th_01HD44FHMCDSSWE38N14FSYV6K",
      "customer": {
        "id": "c_01HD44FHDPG82VQ4QNHDR4N2T0",
        "email": {
          "email": "peter@example.com",
          "isVerified": false,
          "verifiedAt": null
        },
        "externalId": null,
        "fullName": "Peter Santos",
        "shortName": "Peter",
        "markedAsSpamAt": null,
        "markedAsSpamBy": null,
        "customerGroupMemberships": [],
        "createdAt": "2023-10-19T14:12:25.142Z",
        "createdBy": {
          "actorType": "system",
          "system": "email_inbound_handler"
        },
        "updatedAt": "2023-10-19T21:18:12.863Z",
        "updatedBy": {
          "actorType": "user",
          "userId": "u_01H1V4NA10RMHWFBXB6A1ZBYRA"
        }
      },
      "title": "Unable to tail logs",
      "previewText": "Hey, I am currently unable to tail the logs of the service svc-8af1e3",
      "priority": 1,
      "externalId": null,
      "status": "TODO",
      "statusChangedAt": "2023-10-19T21:18:12.862Z",
      "statusChangedBy": {
        "actorType": "user",
        "userId": "u_01H1V4NA10RMHWFBXB6A1ZBYRA"
      },
      "statusDetail": null,
      "assignee": null,
      "assignedAt": null,
      "labels": [],
      "firstInboundMessageInfo": {
        "timestamp": "2023-10-19T14:12:25.733Z",
        "messageSource": "EMAIL"
      },
      "firstOutboundMessageInfo": null,
      "lastInboundMessageInfo": {
        "timestamp": "2023-10-19T14:12:25.733Z",
        "messageSource": "EMAIL"
      },
      "lastOutboundMessageInfo": null,
      "supportEmailAddresses": ["help@example.com"],
      "createdAt": "2023-10-19T14:12:25.266Z",
      "createdBy": {
        "actorType": "system",
        "system": "email_inbound_handler"
      },
      "updatedAt": "2023-10-19T21:20:07.612Z",
      "updatedBy": {
        "actorType": "user",
        "userId": "u_01H1V4NA10RMHWFBXB6A1ZBYRA"
      }
    }
  },
  "id": "pEv_01HD4WYPDWSGNHMETTVVGYHDQY",
  "webhookMetadata": {
    "webhookTargetId": "whTarget_01HD4400VTDJQ646V6RY37SR7K",
    "webhookDeliveryAttemptId": "whAttempt_01HD4XAYFTYXRYMHJ0HGR2FN3D",
    "webhookDeliveryAttemptNumber": 4,
    "webhookDeliveryAttemptTimestamp": "2023-10-19T21:26:49.082Z"
  },
  "type": "thread.thread_priority_changed"
}
```


# Thread SLA status transitioned
Source: https://www.plain.com/docs/webhooks/thread-service-level-agreement-status-transitioned



This event is fired when the status of an SLA linked to a thread changes.

As part of the `serviceLevelAgreementStatusDetail` field threads can have a status with the following values:

| Status            | Description                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PENDING`         | When the timer on the SLA is counting down but has not met the `IMMINENT_BREACH` threshold                                                                                                              |
| `IMMINENT_BREACH` | For SLAs where an alert has been set up to notify the team before it breaches. The SLA will be in this status after the alert period and before the SLA breaches                                        |
| `BREACHING`       | Applies to SLAs while their conditions are not met e.g if a thread with a first response time (FRT) SLA has not been replied to after the time period specified                                         |
| `ACHIEVED`        | A thread where the SLA conditions were met e.g a thread was replied to within the FRT SLA period                                                                                                        |
| `BREACHED`        | A thread where the SLA conditions were not met (and so entered `BREACHING`) but action has been taken that would have resolved the SLA e.g a thread breached the FRT SLA, but then first reply was sent |
| `CANCELLED`       | An SLA which no longer applies e.g if a thread is marked as done with no reply the SLA is cancelled since we don't want it to affect metrics                                                            |

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-service-level-agreement-status-transitioned.mdx" />


# Slack message received
Source: https://www.plain.com/docs/webhooks/thread-slack-message-received



This event is fired when a Slack message is received in your workspace.

If the message is edited in Slack, this webhook will not fire again.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-slack-message-received.mdx" />


# Slack message sent
Source: https://www.plain.com/docs/webhooks/thread-slack-message-sent



This event is fired when a Slack message is sent in your workspace.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-slack-message-sent.mdx" />


# Thread status transitioned
Source: https://www.plain.com/docs/webhooks/thread-status-transitioned



This event is fired when the status of a thread changes.

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/thread-status-transitioned.mdx" />


# Webhooks and Typescript
Source: https://www.plain.com/docs/webhooks/typescript



Our [TypeScript SDK](https://github.com/team-plain/typescript-sdk) provide utilities to [verify the webhook signature](https://www.plain.com/docs/request-signing#request-signing) and parse the webhook body into a typed object.

```typescript  theme={null}
import express from 'express';

import {
  PlainWebhookSignatureVerificationError,
  PlainWebhookVersionMismatchError,
  verifyPlainWebhook,
} from '@team-plain/typescript-sdk';

// Plain HMAC Secret. You can find this in Plain's settings.
const PLAIN_SIGNATURE_SECRET = process.env.PLAIN_SIGNATURE_SECRET;
if (!PLAIN_SIGNATURE_SECRET) {
  throw new Error('PLAIN_SIGNATURE_SECRET environment variable is required');
}

const app = express();
app.use(express.text());

app.post('/handler', function (req: Express.Request, res: Express.Response) {
  // Please note that you must pass the raw request body, exactly as received from Plain,
  const payload = req.body;

  // Plain's computed signature for the request.
  const signature = req.get('Plain-Request-Signature');

  const webhookResult = verifyPlainWebhook(payload, signature, secret);
  if (webhookResult.error instanceof PlainWebhookSignatureVerificationError) {
    res.status(401).send('Failed to verify the webhook signature');
    return;
  }

  if (webhookResult.error instanceof PlainWebhookVersionMismatchError) {
    // The SDK is not compatible with the received webhook version.
    // This can happen if you upgrade the SDK but not the webhook target, or vice versa.
    // We recommend setting up alerts to notify you when this happens.
    // Consult https://plain.com/docs/webhooks/versions for more information.
    console.error('Webhook version mismatch:', webhookResult.error.message);

    // Respond with a non-2XX status code to trigger a retry from Plain.
    res.status(400).send('Webhook version mismatch');
    return;
  }

  if (webhookResult.error) {
    // Unexpected error. Most likely due to an error in Plain's webhook server or a bug in the SDK.
    // Treat this as a 500 response from Plain.
    console.error('Unexpected error:', webhookResult.error.message);
    res.status(500).send('Unexpected error');
    return;
  }

  // webhookResult.data is now a typed object.
  const webhookBody = webhookResult.data;

  // You can use the eventType to filter down to a specific event type
  if (webhookBody.payload.eventType === 'thread.thread_created') {
    console.log(`Thread created: ${webhookBody.payload.thread.id}`);
  }

  // Respond with a 200 status code.
  res.status(200).send('Webhook received');
});
```

We strongly recommend verifying the webhook signature before processing the webhook body. This ensures that the webhook was sent by Plain and not a malicious third party. However, if you want to skip the verification, you can use the [`parsePlainWebhook` function](https://plain-typescript-sdk-docs.vercel.app/functions/parsePlainWebhook.html) instead.


# Webhook Versions
Source: https://www.plain.com/docs/webhooks/versions



Every [webhook target](https://www.plain.com/docs/webhooks#receiving-events-from-plain) in Plain is associated with a specific version. The webhook version defines the schema of the payload that Plain sends to your endpoint. By specifying a version, you ensure that the payload format remains consistent, even as Plain evolves and introduces changes to the webhook schema.

**Benefits of Versioning**:

* **Consistency**: Your endpoint always receives payloads in the same format.
* **Control**: You decide when to adopt new schema changes.
* **Stability**: Prevents unexpected breaking changes due to schema updates.

## Available Versions

We recommend always using the latest version of the webhook payload schema to benefit from new features and improvements. Below are the currently available versions:

### `2024-09-18` (Latest)

Our first official versioned webhook payload schema.

* **What's New**:
  * Introduction of webhook versioning.
  * Improved forward-compatibility schema definitions for payloads.
  * Microsoft Teams events.
  * New thread status details.
* [View JSON Schema](https://core-api.uk.plain.com/webhooks/schema/2024-09-18.json)
* **TypeScript SDK Compatibility**: Version `>= 5.0.0`

### `unversioned`

The legacy webhook payload schema before versioning was implemented.

* [View JSON Schema](https://core-api.uk.plain.com/webhooks/schema/unversioned.json)
* **TypeScript SDK Compatibility**: Versions `>= 4.8.0` and `< 5.0.0`

## How to Upgrade to the Latest Version

Upgrading to the latest webhook version involves updating your code to handle the new schema and changing your webhook target settings in Plain.

### Step 1: Update Your Code

Modify your code to handle both the old and new webhook payload versions during the transition period. This ensures uninterrupted processing of events.

**Handle Version Mismatch (TypeScript SDK Users):**

If you're using our TypeScript SDK, you can update your code to throw an error when receiving an old version. This will cause Plain to retry the request later, ideally after you've updated the webhook target version in the Plain dashboard. For more details, refer to our [retry policy](https://www.plain.com/docs/webhooks#retry-policy).

See the [TypeScript SDK Example](#typescript-sdk-example) for implementation details.

Deploy this updated code, and fast follow with Step 2.

### Step 2: Update the Webhook Target in Plain

After deploying your updated code, change the version of your webhook target in Plain to the new version. This ensures that all future webhook events are sent using the latest schema.

### Step 3: Revert Temporary Code Changes

Once you have confirmed that your application is successfully processing events with the new version, you can remove the code that handles both old and new versions. Your code can now exclusively handle the latest webhook payload schema.

<Info>
  Ensure that your webhook handling code is **idempotent** and can gracefully handle **duplicate
  events**. Plain's webhook delivery is **at least once**, meaning the same event might be delivered
  multiple times. Refer to our [delivery
  semantics](https://www.plain.com/docs/webhooks#delivery-semantics) for more
  information.
</Info>

## TypeScript SDK Example

Below is an example of how to handle webhook version mismatches using our TypeScript SDK:

```typescript  theme={null}
import { verifyPlainWebhook, PlainWebhookVersionMismatchError } from '@team-plain/typescript-sdk';

// The same approach works for `parsePlainWebhook`
const webhookResult = verifyPlainWebhook(payload, signature, secret);

if (webhookResult.error instanceof PlainWebhookVersionMismatchError) {
  // Received a webhook with an old version
  // Return a non-2XX response to trigger a retry
  throw new Error('Skipping older version');
}

// proceed with the rest of your error handling logic
```

**Explanation**:

* **Version Mismatch Handling**: By checking if the error is an instance of `PlainWebhookVersionMismatchError`, you can determine if the payload is on the old version. This could happen if an event is sent during the time between your code deployment and the webhook target version update in Plain.
* **Triggering a Retry**: Throwing an error or returning a non-2XX HTTP response tells Plain to retry the webhook delivery later. After you update the webhook target version in Plain, the failed event will be resent with the new schema.

## Identifying the Webhook Version in Received Payloads

If you receive a webhook payload and are unsure which version it is using, you can identify the version by checking:

* **Headers**: The `Plain-Webhook-Target-Version` header indicates the version of the webhook target for which this request is intended.
* **Payload Metadata**: Within the [webhook metadata](https://www.plain.com/docs/webhooks#webhook-metadata) in the payload body, the `webhookTargetVersion` field specifies the version of the webhook target for this request.

This information helps you determine how to parse and handle the webhook payload according to its schema version.

## Best Practices and Recommendations

* **Monitor Logs**: After upgrading, monitor your logs and error tracking systems for any issues related to webhook processing.
* **Stay Informed**: Keep an eye on our documentation and [change log](https://www.plain.com/changelog) for future updates or changes to the webhook schema.

If you have any questions or need assistance, please reach out to us at **[help@plain.com](mailto:help@plain.com)**.


