# Source: https://developers.webflow.com/data/docs/working-with-localization/localize-components.mdx

***

title: Localizing components
description: >-
How to use Component APIs to localize component definitions and component
instances in secondary locales
hidden: false
subtitle: >-
Learn how to use the Data API to localize component content and properties
across different locales.
max-toc-depth: 3
----------------

Components are reusable design elements that can be instanced across your site.

## Workflows

Webflow enables you to localize both a component definition and component instances via the Data API.

<CardGroup cols={2}>
  <Card
    title="Localize component definitions"
    href="#component-definitions"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Components.svg"
          alt="Component Definition Logo"
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Components.svg"
          alt="Component Definition Logo"
          className="block dark:hidden"
        />
      </>
    }
  >
    Localize the static content of a component definition across an **entire
    locale**
  </Card>

  <Card
    title="Localize component instances"
    href="#component-instances"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/PageBuilding.svg"
          alt="Component Definition Logo"
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/PageBuilding.svg"
          alt="Component Definition Logo"
          className="block dark:hidden"
        />
      </>
    }
  >
    Localize a component instance on a **specific page** by modifying its properties.
  </Card>
</CardGroup>

## Key concepts

To understand how to localize components, you'll need to understand the key concepts of components in Webflow.

<Tabs>
  <Tab title="Component definition">
    A component definition serves as the blueprint for a component. It contains the component's static content, like text and images, and defines the component's properties: customizable fields that allow for dynamic content. When you change a component definition, the updates apply to all instances of that component, unless an instance has a property override.

    A component definition contains two types of localizable content:

    * **Static content**: Text nodes, form elements, and nested component instances
    * **Property defaults**: Default text values for component properties

      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/f260ff5cfaea4ba95d769501590b4be09d6b0faa61c6753f18451fb5c51fc0d7/products/data/pages/Localization/assets/Component-Definition-Light.svg" alt="Component Definition" />
  </Tab>

  <Tab title="Component instance">
    A **component instance** is a live copy of a component definition placed on a page. While the definition acts as a template, an instance is the actual element that users see.

    By default, an instance inherits all content and property values directly from its component definition. If you change these in the definition, all instances update automatically.

    However, you can customize an instance by applying a **property override**. An override is a unique value for a property that applies only to a single instance. For example, if you have a "Job Card" component, you can use overrides to give each instance on your "Jobs" page a different title, description, and location.

    **You can only localize property overrides of a component instance.** To localize the default properties of a component, you need to update the component definition.

    <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/192b968932d408573ab17bb7beb30723fecf8d6a035f47bc400c75d2d3aebcda/products/data/pages/Localization/assets/Component-Instance-Light.svg" alt="Component Instance" />
  </Tab>
</Tabs>

### Localizable content

To completely localize your site, you'll need to localize all three types of component content.

| Content Type           | Scope                                                                  | Description                                                           |
| :--------------------- | :--------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| **Property Overrides** | Page-specific <br /><Badge minimal="true">Instance</Badge>             | Custom values applied to a single component instance.                 |
| **Property Defaults**  | Site-wide <br /><Badge minimal="true" intent="info">Definition</Badge> | Default values for properties, used by instances without an override. |
| **Static Content**     | Site-wide <br /><Badge minimal="true" intent="info">Definition</Badge> | Fixed text content that's part of the component's structure.          |

Some key points to remember when localizing component content:

* Property overrides only affect a specific component instance on a page
* Default properties affect all instances that don't have overrides
* Static content affects all instances across the site
* Only content bound to component properties can be overridden at the instance or per-page level

## Component definitions

Component definitions contain two types of localizable content:

<CardGroup cols={2}>
  <Card
    title="Static content"
    href="#localize-static-content"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/LayoutDashboard.svg"
          alt="Static Content Logo"
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/LayoutDashboard.svg"
          alt="Static Content Logo"
          className="block dark:hidden"
        />
      </>
    }
  >
    Text nodes, form elements, and nested component instances
  </Card>

  <Card
    title="Property defaults"
    href="#localize-default-properties"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/SiteBlank.svg"
          alt="Property Defaults Logo"
          className="hidden dark:block"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/SiteBlank.svg"
          alt="Property Defaults Logo"
          className="block dark:hidden"
        />
      </>
    }
  >
    Default values for component properties
  </Card>
</CardGroup>

### Localize static content

To localize static content, you'll first need to get the content of the selected component, and then update the content in a secondary locale.

<Steps>
  <Step title="List site components">
    Use the [List
    Components](/data/reference/pages-and-components/components/list) endpoint
    to get a list of all components on your site.
  </Step>

  <Step title="Get static content of a component">
    Use the [Get Component
    Content](/data/reference/pages-and-components/components/get-content)
    endpoint to get the static content of a selected component definition.
  </Step>

  <Step title="Update static content of a component">
    Use the [Update Component
    Content](/data/reference/pages-and-components/components/update-content)
    endpoint to update the static content of the selected component definition in a secondary locale.
  </Step>
</Steps>

#### List site components

Use the [List Components](/data/reference/pages-and-components/components/list) endpoint to get a list of all components on your site.

{/* While this endpoint does provide details about each component definition, it doesn't show where the components are actually being used. The [Get Page Content API](https://developers.webflow.com/data/reference/pages-and-components/pages/get-content) response will show you which components are instanced on a given page. */}

##### Request

<CodeBlocks>
  ```curl cURL
  curl -G https://api.webflow.com/v2/sites/<SITE_ID>/components \
       -H "Authorization: Bearer <token>" \
       -d limit=100 \
       -d offset=0
  ```

  ```javascript Node.js
  const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
  const components = await client.components.list("YOUR_SITE_ID");
  ```
</CodeBlocks>

##### Response

The endpoint returns a `components` array with the details of each component definition on your site. The response also includes a `pagination` object for pagination through results over the 100 item limit.

{/* <!-- vale off --> */}

<div>
  <Card>
    <EndpointSchemaSnippet endpoint="GET /sites/:site_id/components" selector="response.body" />
  </Card>

  <CodeBlocks>
    ```json title="Response"
    {
      "components": [
        {
          "id": "1fa6f97b-84f7-2db3-29cb-1275161e432f",
          "name": "Navbar"
        },
        {
          "id": "9fa3a9c4-87d4-19b0-95f7-1b0b099f82a0",
          "name": "Footer"
        },
        {
          "id": "db278ae3-20d1-6657-c0c9-083a38fbc2c4",
          "name": "Locale dropdown"
        },
        {
          "id": "d2de2e85-bab1-8dbb-1648-2bbedc5417dd",
          "name": "Hero"
        },
        {
          "id": "fd06c181-43b2-e1c0-9d7f-0b332cd9905b",
          "name": "Card"
        },
        {
          "id": "33666cc8-031a-c160-37ec-654c05d48750",
          "name": "Job Card"
        },
        {
          "id": "d2154999-bbdb-8145-1152-53511d5c3f70",
          "name": "Button"
        }
      ],
      "pagination": {
        "limit": 100,
        "offset": 0,
        "total": 7
      }
    }
    ```
  </CodeBlocks>
</div>

{/* <!-- vale on --> */}

#### Get static content from the primary locale

Retrieve existing static content from the primary locale for a specific component. Send a <Badge intent="success">GET</Badge> request to the [get component content](/data/reference/pages-and-components/components/get-content) endpoint, and include the component `id` in the request path.

<br />

##### Request

<CodeBlocks>
  ```curl cURL
  curl -G https://api.webflow.com/v2/sites/<SITE_ID>/components/<COMPONENT_ID>/dom \
       -H "Authorization: Bearer <token>" \
       -d limit=100 \
       -d offset=0
  ```

  ```javascript Node.js
  const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
  const content = await client.components.getContent(
    "YOUR_SITE_ID",
    "YOUR_COMPONENT_ID"
  );
  ```
</CodeBlocks>

<br />

##### Response

The response contains a `nodes` array with the component's static content. Each node includes a `type` property that defines its content type.

{/* <!-- vale off --> */}

<div>
  <Card>
    <EndpointSchemaSnippet endpoint="GET /sites/:site_id/components/:component_id/dom" selector="response.body" />
  </Card>

  <CodeBlocks>
    ```json title="Get Component Content response example"
    {
      "componentId": "33666cc8-031a-c160-37ec-654c05d48750",
      "nodes": [
        {
          "type": "text",
          "id": "dca4e42f-0d46-0c2a-420f-6496321fec8b",
          "text": {
            "html": "<div class=\"text-block-2\">NEW&nbsp;OPPORTUNITY</div>",
            "text": "NEW OPPORTUNITY"
          },
          "attributes": {}
        },
        {
          "type": "component-instance",
          "id": "d2154999-bbdb-8145-1152-53511d5c3f73",
          "componentId": "d2154999-bbdb-8145-1152-53511d5c3f70",
          "propertyOverrides": [
            {
              "propertyId": "d9e0fd5c-e7f7-d25a-fdc4-3741ec86fc43",
              "type": "Plain Text",
              "label": "Button Text",
              "text": {
                "text": "Apply Now"
              }
            }
          ]
        }
      ],
      "pagination": {
        "limit": 100,
        "offset": 0,
        "total": 2
      }
    }
    ```
  </CodeBlocks>
</div>

{/* <!-- vale on --> */}

##### Node types

<br />

| Node type            | Description                                                                                                                                                                                                                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `text`               | Represents text content. Including headings, [text blocks](https://help.webflow.com/hc/en-us/articles/33961346059027-Use-text-blocks-in-Webflow), [rich text](https://help.webflow.com/hc/en-us/articles/33961256808467-Rich-text-element-overview), form labels, and other text content on a page. |
| `image`              | Represents static images on a page. It contains alt text details for accessibility and the `assetId` for fetching the actual image resource.                                                                                                                                                        |
| `text-input`         | Represents a `textinput` and `textarea` fields on a form.                                                                                                                                                                                                                                           |
| `select`             | Represents a select field and its options on a form.                                                                                                                                                                                                                                                |
| `submit-button`      | Represents a submit button on a form. It contains the button text and waiting text of the button.                                                                                                                                                                                                   |
| `search-button`      | Represents the button text of a search button on a [site search element](https://help.webflow.com/hc/en-us/articles/33961242348179-Site-search).                                                                                                                                                    |
| `component-instance` | Represents a component instance on a page. Learn more about [localizing components](/data/docs/working-with-localization/localize-components) in the guide.                                                                                                                                         |

<br />

##### Node properties

<div>
  <div>
    Each node type has a specific structure and properties that define the
    content it contains. However, all nodes will have `id`, `type`, and
    `attributes` properties.
  </div>

  <Card>
    <ParamField path="id" type="string" required={true}>
      Node UUID
    </ParamField>

    <ParamField path="type" type="enum" required={true}>
      The type of the node.
    </ParamField>

    <ParamField path="attributes" type="map from strings to strings" required={false}>
      The custom attributes of the node
    </ParamField>
  </Card>
</div>

<br />

##### Node properties by type

Each node type has a unique structure for accessing component content.

For example, a `text` node contains a `text` object, which includes `html` and `text` properties. These properties provide context for strings that can be localized. See the tabs below for the specific properties for each node type.

<br />

{/* <!-- vale off --> */}

<Tabs>
  <Tab title="Text">
    <div>
      <Card>
        <ParamField path="id" type="string" required={true}>
          Node UUID
        </ParamField>

        <ParamField path="type" type="enum" required={true}>
          The type of the node. `text`
        </ParamField>

        <ParamField path="text" type="object" required={true}>
          The text content of the node

          <Accordion title="+ Show 2 properties">
            <ParamField path="html" type="string" required={true}>
              The HTML content of the node
            </ParamField>

            <ParamField path="text" type="string" required={true}>
              The text content of the node
            </ParamField>
          </Accordion>
        </ParamField>

        <ParamField path="attributes" type="map from strings to strings" required={false}>
          The custom attributes of the node
        </ParamField>
      </Card>

      <CodeBlocks>
        ```json title="Text node example"
        {
          "id": "a245c12d-995b-55ee-5ec7-aa36a6cad623",
          "type": "text",
          "text": {
            "html": "<h1>Don't Panic!</h1>",
            "text": "Don't Panic!"
          },
          "attributes": {}
        },
        {
          "id": "a245c12d-995b-55ee-5ec7-aa36a6cad627",
          "type": "text",
          "text": {
            "html": "<span data-w-id=\"b3107...\">$9.99</span>",
            "text": "$9.99"
          },
          "attributes": {}
        }
        ```
      </CodeBlocks>
    </div>

    <Note title="Nested HTML tags">
      The `text.html` property may contain nested HTML tags with `data-w-id` attributes (e.g., `data-w-id="some-unique-identifier"`). Retain these identifiers when updating page content in secondary locales to preserve custom attributes and links on inner HTML elements.
    </Note>
  </Tab>

  <Tab title="Image">
    <div>
      <Card>
        <ParamField path="id" type="string" required={true}>
          Node UUID
        </ParamField>

        <ParamField path="type" type="enum" required={true}>
          The type of the node. `image`
        </ParamField>

        <ParamField path="image" type="object" required={true}>
          The image content of the node

          <Accordion title="+ Show 2 properties">
            <ParamField path="alt" type="string" required={true}>
              The alt text for the image
            </ParamField>

            <ParamField path="assetId" type="string" required={true}>
              The ID of the asset for the image
            </ParamField>
          </Accordion>
        </ParamField>

        <ParamField path="attributes" type="map from strings to strings" required={false}>
          The custom attributes of the node
        </ParamField>
      </Card>

      ```json title="Image node example"
      {
        "id": "a245c12d-995b-55ee-5ec7-aa36a6cad629",
        "type": "image",
        "image": {
          "alt": "Marvin, the Paranoid Android",
          "assetId": "659595234426a9fcbad57043"
        },
        "attributes": {}
      }
      ```
    </div>

    <Warning title="Updating images isn't supported by the API">
      Currently, the API returns `image` nodes in the response body of a <Badge intent="success">GET</Badge> static contnet request. However, updating images isn't supported by the API. To update images, you'll need to update the image asset in the Webflow designer.
    </Warning>
  </Tab>

  <Tab title="Text Input">
    <div>
      <Card>
        <ParamField path="id" type="string" required={true}>
          Node UUID
        </ParamField>

        <ParamField path="type" type="enum" required={true}>
          The type of the node. `text-input`
        </ParamField>

        <ParamField path="placeholder" type="string" required={false}>
          The placeholder text for the input field
        </ParamField>

        <ParamField path="attributes" type="map from strings to strings" required={false}>
          The custom attributes of the node
        </ParamField>
      </Card>

      ```json title="Text input node example"
      {
        "id": "a245c12d-995b-55ee-5ec7-aa36a6cad642",
        "type": "text-input",
        "placeholder": "Enter something here...",
        "attributes": {}
      }
      ```
    </div>
  </Tab>

  <Tab title="Select">
    <div>
      <Card>
        <ParamField path="id" type="string" required={true}>
          Node UUID
        </ParamField>

        <ParamField path="type" type="enum" required={true}>
          The type of the node. `select`
        </ParamField>

        <ParamField path="choices" type="list of objects" required={true}>
          The choices for the select field

          <Accordion title="+ Show 2 properties">
            <ParamField path="value" type="string" required={true}>
              The value of the choice
            </ParamField>

            <ParamField path="text" type="string" required={true}>
              The text of the choice
            </ParamField>
          </Accordion>
        </ParamField>

        <ParamField path="attributes" type="map from strings to strings" required={false}>
          The custom attributes of the node
        </ParamField>
      </Card>

      ```json title="Select node example"
      {
        "id": "a245c12d-995b-55ee-5ec7-aa36a6cad635",
        "type": "select",
        "choices": [
          {
            "value": "choice-1",
            "text": "First choice"
          },
          {
            "value": "choice-2",
            "text": "Second choice"
          }
        ],
        "attributes": {}
      }
      ```
    </div>
  </Tab>

  <Tab title="Submit Button">
    <div>
      <Card>
        <ParamField path="id" type="string" required={true}>
          Node UUID
        </ParamField>

        <ParamField path="type" type="enum" required={true}>
          The type of the node. `submit-button`
        </ParamField>

        <ParamField path="value" type="string" required={true}>
          The text content of the button
        </ParamField>

        <ParamField path="waitingText" type="string" required={false}>
          The text content of the button while submitting
        </ParamField>

        <ParamField path="attributes" type="map from strings to strings" required={false}>
          The custom attributes of the node
        </ParamField>
      </Card>

      ```json title="Submit button node example"
      {
        "id": "a245c12d-995b-55ee-5ec7-aa36a6cad671",
        "type": "submit-button",
        "value": "Submit",
        "waitingText": "Submitting...",
        "attributes": {}
      }
      ```
    </div>
  </Tab>

  <Tab title="Component Instance">
    <div>
      <Card>
        <ParamField path="id" type="string" required={true}>
          Node UUID
        </ParamField>

        <ParamField path="type" type="enum" required={true}>
          The type of the node. `component-instance`
        </ParamField>

        <ParamField path="componentId" type="string" required={true}>
          The ID of the component
        </ParamField>

        <ParamField path="propertyOverrides" type="array" required={false}>
          The property overrides for the component instance

          <Accordion title="+ Show 4 properties">
            <ParamField path="propertyId" type="string" required={true}>
              The ID of the property
            </ParamField>

            <ParamField path="type" type="string" required={true}>
              The type of the property
            </ParamField>

            <ParamField path="label" type="string" required={true}>
              The label of the property
            </ParamField>

            <ParamField path="text" type="object" required={true}>
              The text content of the property

              <Accordion title="+ Show 2 properties">
                <ParamField path="html" type="string" required={false}>
                  The HTML content of the property
                </ParamField>

                <ParamField path="text" type="string" required={false}>
                  The text content of the property
                </ParamField>
              </Accordion>
            </ParamField>
          </Accordion>
        </ParamField>
      </Card>

      <CodeBlocks>
        ```json title="Component instance node example"
        {
          "id": "a245c12d-995b-55ee-5ec7-aa36a6cad631",
          "type": "component-instance",
          "componentId": "6258612d1ee792848f805dcf",
            "propertyOverrides": [
              {
                "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad633",
              "type": "Plain Text",
              "label": "Catchphrase",
              "text": {
                "html": null,
                "text": "Don't Panic!"
              }
              },
              {
                "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad635",
              "type": "Rich Text",
              "label": "Tagline",
              "text": {
                "html": "<div><p>Always know where your towel is.</p></div>",
                "text": null
              }
            }
          ]
        }
        ```
      </CodeBlocks>
    </div>

    ##### Nested component instances

    A nested component instance is a component instance that's permanently included within another component's definition.

    For example, a Job Card component might always include a Button component as part of its design. This Button will be a nested component instance that has its own properties, which can be overridden in the Job Card's definition.

    <div>
      <div>
        <Frame>
          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/942180afed092b4f6508afb2e526e08b1aa62b81f299138b5437c22872dbf613/products/data/pages/Localization/assets/NestedComponent.png" alt="Nested component instance" />
        </Frame>

        <div>
          The <Badge intent="info">Apply Now</Badge> button is a nested component
          instance that has its own properties. In the Button instance, the "button
          text" property is overridden from its default value of "Click here" to
          "Apply Now." This is indicated by the blue overlay on the "Button Text"
          label. Now that the button text property is overridden, it's localizable.
        </div>
      </div>

      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/18b1f812066a7876279fc90285a16439683374c33ce92de886f383e6dd07a038/products/data/pages/Localization/assets/ButtonProps.png" alt="Nested component instance" />
    </div>
  </Tab>
</Tabs>

{/* <!-- vale on --> */}

#### Update static content

After translating the content you received from your earlier request, update it with the [update component content endpoint](/data/reference/pages-and-components/components/update-content), passing the target `localeId` as a query parameter and the translated `nodes` in the request body.

You only need to include the `nodeId` and the content property for that specific node type.

##### Request

<CodeBlocks>
  ```curl cURL
  curl -X POST https://api.webflow.com/v2/sites/<SITE_ID>/components/<COMPONENT_ID>/dom?localeId=<SECONDARY_LOCALE_ID> \
       -H "Authorization: Bearer <token>" \
       -H "Content-Type: application/json" \
       -d '{
         "nodes": [
          {
            "nodeId": "dca4e42f-0d46-0c2a-420f-6496321fec8b",
            "text": "<div class=\"text-block-2\">NUEVA&nbsp;OPORTUNIDAD</div>"
          },
          {
            "nodeId": "d2154999-bbdb-8145-1152-53511d5c3f73",
            "propertyOverrides": [
              {
                "propertyId": "d9e0fd5c-e7f7-d25a-fdc4-3741ec86fc43",
                "text": "Aplicar ahora"
              }
            ]
          }
        ]
       }'
  ```

  ```javascript Node.js
  const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
  await client.components.updateContent("YOUR_COMPONENT_ID", {
    localeId: "SECONDARY_LOCALE_ID",
    nodes: [
      {
        nodeId: "dca4e42f-0d46-0c2a-420f-6496321fec8b",
        text: '<div class="text-block-2">NUEVA&nbsp;OPORTUNIDAD</div>',
      },
      {
        nodeId: "d2154999-bbdb-8145-1152-53511d5c3f73",
        propertyOverrides: [
          {
            propertyId: "d9e0fd5c-e7f7-d25a-fdc4-3741ec86fc43",
            text: "Aplicar ahora",
          },
        ],
      },
    ],
  });
  ```
</CodeBlocks>

##### Response

A successful response will return an object with and `error` property with an empty array.

### Localize default properties

Component properties are typed variables that make component content dynamic and customizable per instance. When content is bound to a property, each component instance can have different values for that property.

Component definitions can store **default values** for properties, which are used as fallbacks when instances don't have property overrides. To localize the default values follow the steps below.

<Steps>
  <Step title="List site components">
    Use the [List
    Components](/data/reference/pages-and-components/components/list) endpoint
    to get a list of all components on your site.
  </Step>

  <Step title="Get component properties">
    Use the [Get Component
    Properties](/data/reference/pages-and-components/components/get-properties)
    endpoint to get the default properties of the selected component definition.
  </Step>

  <Step title="Update component properties">
    Use the [Update Component
    Properties](/data/reference/pages-and-components/components/update-properties)
    endpoint to update the default properties of the selected component
    definition.
  </Step>
</Steps>

#### List site components

Use the [List Components](/data/reference/pages-and-components/components/list) endpoint to get a list of all components on your site.

{/* While this endpoint does provide details about each component definition, it doesn't show where the components are actually being used. The [Get Page Content API](https://developers.webflow.com/data/reference/pages-and-components/pages/get-content) response will show you which components are instanced on a given page. */}

##### Request

<CodeBlocks>
  ```curl cURL
  curl -G https://api.webflow.com/v2/sites/<SITE_ID>/components \
       -H "Authorization: Bearer <token>" \
       -d limit=100 \
       -d offset=0
  ```

  ```javascript Node.js
  const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
  const components = await client.components.list("YOUR_SITE_ID");
  ```
</CodeBlocks>

##### Response

The endpoint returns a `components` array with the details of each component definition on your site. The response also includes a `pagination` object for pagination through results over the 100 item limit.

{/* <!-- vale off --> */}

<div>
  <Card>
    <EndpointSchemaSnippet endpoint="GET /sites/:site_id/components" selector="response.body" />
  </Card>

  <CodeBlocks>
    ```json title="Response"
    {
      "components": [
        {
          "id": "1fa6f97b-84f7-2db3-29cb-1275161e432f",
          "name": "Navbar"
        },
        {
          "id": "9fa3a9c4-87d4-19b0-95f7-1b0b099f82a0",
          "name": "Footer"
        },
        {
          "id": "db278ae3-20d1-6657-c0c9-083a38fbc2c4",
          "name": "Locale dropdown"
        },
        {
          "id": "d2de2e85-bab1-8dbb-1648-2bbedc5417dd",
          "name": "Hero"
        },
        {
          "id": "fd06c181-43b2-e1c0-9d7f-0b332cd9905b",
          "name": "Card"
        },
        {
          "id": "33666cc8-031a-c160-37ec-654c05d48750",
          "name": "Job Card"
        },
        {
          "id": "d2154999-bbdb-8145-1152-53511d5c3f70",
          "name": "Button"
        }
      ],
      "pagination": {
        "limit": 100,
        "offset": 0,
        "total": 7
      }
    }
    ```
  </CodeBlocks>
</div>

{/* <!-- vale on --> */}

#### Get component properties

Retrieve component property definitions and their default values using the [Get Component Properties](/data/reference/pages-and-components/components/get-properties) endpoint.

##### Request

<CodeBlocks>
  ```curl cURL
  curl -G https://api.webflow.com/v2/sites/<SITE_ID>/components/<COMPONENT_ID>/properties \
       -H "Authorization: Bearer <token>"
  ```

  ```javascript Node.js
  const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
  const properties = await client.components.getProperties("YOUR_COMPONENT_ID");
  ```
</CodeBlocks>

##### Response

The response will return an object with the `componentId`, `properties`, and `pagination` properties. Each property will have a type and text property, which contains the property's default text value.

<div>
  <Card>
    <EndpointSchemaSnippet endpoint="GET /sites/:site_id/components/:component_id/properties" selector="response.body" />
  </Card>

  {/* <!-- vale off --> */}

  <CodeBlocks>
    ```json title="Response"
    {
      "componentId": "33666cc8-031a-c160-37ec-654c05d48750",
      "properties": [
        {
          "propertyId": "ecce29ad-f890-3428-1e29-5232054f8932",
          "type": "Plain Text",
          "label": "Title",
          "text": {
            "text": "Job Title"
          }
        },
        {
          "propertyId": "b0e6e289-f003-51df-07c2-387775f9a267",
          "type": "Plain Text",
          "label": "Department",
          "text": {
            "text": "Department"
          }
        },
        {
          "propertyId": "a0c19de3-e501-89ae-0a69-45b95dbe1dd6",
          "type": "Plain Text",
          "label": "Description",
          "text": {
            "text": "Apply if you are an expert in delaying tasks, have perfected the art of avoiding work, and mastered the subtle skill of looking busy while accomplishing nothing."
          }
        },
        {
          "propertyId": "d0b64214-eb68-fa04-3c93-26f8be2df466",
          "type": "Plain Text",
          "label": "Location",
          "text": {
            "text": "Location"
          }
        },
        {
          "propertyId": "aaeb508c-75ad-c326-ff4d-c607620dc41a",
          "type": "Plain Text",
          "label": "Contract Type",
          "text": {
            "text": "Contract Type"
          }
        },
      ],
      "pagination": {
        "limit": 100,
        "offset": 0,
        "total": 5
      }
    }
    ```
  </CodeBlocks>

  {/* <!-- vale on --> */}
</div>

##### Property types

Component properties can be of different types:

* **Plain Text** - Single-line text without HTML formatting
* **Rich Text** - Multi-line text with HTML formatting support
* **Alt Text** - Alternative text for images

#### Update component properties

Localize component property default values using the [Update Component Properties](/data/reference/pages-and-components/components/update-properties) endpoint. Provide a `properties` array with each of the property IDs and the translated strings in the `text` field. You must pass the `localeId` of the secondary locale you want to update as a query parameter.

##### Request

<CodeBlocks>
  ```curl cURL
  curl -X POST https://api.webflow.com/v2/sites/<SITE_ID>/components/<COMPONENT_ID>/properties?localeId=<SECONDARY_LOCALE_ID> \
       -H "Authorization: Bearer <token>" \
       -H "Content-Type: application/json" \
       -d '{
         "properties": [
           {
             "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad623",
             "text": "Guía del autoestopista galáctico"
           },
           {
             "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad627",
             "text": "<div><h3>¡No entres en pánico!</h3><p>Siempre sabe dónde está tu toalla.</p></div>"
           }
         ]
       }'
  ```

  ```javascript Node.js
  const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
  await client.components.updateProperties("YOUR_COMPONENT_ID", {
    localeId: "SECONDARY_LOCALE_ID",
    properties: [
      {
        propertyId: "a245c12d-995b-55ee-5ec7-aa36a6cad623",
        text: "Guía del autoestopista galáctico",
      },
      {
        propertyId: "a245c12d-995b-55ee-5ec7-aa36a6cad627",
        text: "<div><h3>¡No entres en pánico!</h3><p>Siempre sabe dónde está tu toalla.</p></div>",
      },
    ],
  });
  ```

  {/* <!-- vale on --> */}
</CodeBlocks>

##### Response

A successful response will return an object with and `error` property that contains an empty array.

## Component instances

When you add a component to a page, you create an **instance**. To customize the content of an instance, you can override the default properties of that instance. **Only overridden properties can be localized via the properties endpoints.**

### Identify component instances on pages

Component instances appear in the page content response as `component-instance` nodes. To get page content, use the [Get Page Content](/data/reference/pages-and-components/pages/get-content) endpoint.

##### Request

<EndpointRequestSnippet endpoint="GET /pages/:page_id/dom" />

##### Response

The response will return a list of nodes. Any `component-instance` type nodes will have a `propertyOverrides` array with a list of available properties to localize. If a property hasn't been overridden on the instance, it won't be included in the `propertyOverrides` array.

Each object in the `propertyOverrides` array will have the following properties:

<div>
  <Card>
    <ParamField path="propertyId" type="string" required={true}>
      The unique identifier for the property being overridden.
    </ParamField>

    <ParamField path="type" type="'Plain Text' | 'Rich Text'" required={true}>
      The type of the property.
    </ParamField>

    <ParamField path="label" type="string" required={true}>
      The user-defined label for the property.
    </ParamField>

    <ParamField path="text" type="object" required={true}>
      An object containing the overridden text content.

      <Accordion title="+ properties">
        <ParamField path="html" type="string | null">
          The HTML content for "Rich Text" properties. This will be `null` for "Plain Text" properties.
        </ParamField>

        <ParamField path="text" type="string | null">
          The plain text content for "Plain Text" properties. This will be `null` for "Rich Text" properties.
        </ParamField>
      </Accordion>
    </ParamField>
  </Card>

  {/* <!-- vale off --> */}

  <CodeBlocks>
    {/* <!-- vale on --> */}

    ```json title="Response" {8-27}
    {
      "pageId": "658205daa3e8206a523b5ad4",
      "nodes": [
        {
          "id": "a245c12d-995b-55ee-5ec7-aa36a6cad631",
          "type": "component-instance",
          "componentId": "6258612d1ee792848f805dcf",
          "propertyOverrides": [
            {
              "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad633",
              "type": "Plain Text",
              "label": "Title",
              "text": {
                "html": null,
                "text": "Custom Hero Title"
              }
            },
            {
              "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad635",
              "type": "Rich Text",
              "label": "Description",
              "text": {
                "html": "<div><p>Page-specific description text</p></div>",
                "text": null
              }
            }
          ]
        }
      ]
    }
    ```
  </CodeBlocks>
</div>

In this example, the component instance has overridden two properties ("Title" and "Description") with page-specific values. Any other properties defined in the component will use their default values from the component definition.

### Update component instance

To localize a component instance, create a new `nodes` array, and include an object with the `nodeId` of the component instance and a `propertyOverrides` array. Each item in the array should have the `propertyId` and `text` of the property overrides for the secondary locale.

##### Request

<CodeBlocks>
  ```curl cURL
  curl -X POST https://api.webflow.com/v2/pages/<PAGE_ID>/dom?localeId=<SECONDARY_LOCALE_ID> \
       -H "Authorization: Bearer <token>" \
       -H "Content-Type: application/json" \
       -d '{
         "nodes": [
           {
             "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad631",
             "propertyOverrides": [
               {
                 "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad633",
                 "text": "Título personalizado del héroe"
               },
               {
                 "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad635",
                 "text": "<div><p>Texto de descripción específico de la página</p></div>"
               }
             ]
           }
         ]
       }'
  ```

  ```javascript Node.js
  const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
  await client.pages.updateStaticContent("YOUR_PAGE_ID", {
    localeId: "SECONDARY_LOCALE_ID",
    nodes: [
      {
        nodeId: "a245c12d-995b-55ee-5ec7-aa36a6cad631",
        propertyOverrides: [
          {
            propertyId: "a245c12d-995b-55ee-5ec7-aa36a6cad633",
            text: "Título personalizado del héroe",
          },
          {
            propertyId: "a245c12d-995b-55ee-5ec7-aa36a6cad635",
            text: "<div><p>Texto de descripción específico de la página</p></div>",
          },
        ],
      },
    ],
  });
  ```
</CodeBlocks>

##### Response

A successful response will return an object with and `error` property with an empty array.

## Complete component localization workflow

Here's a complete example demonstrating component localization across definitions and instances:

<CodeBlocks>
  ```javascript Node.js
  const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });

  // Example `translations` object holding the localized content for the secondary locale
  async function localizeComponentDefinition(
    siteId,
    componentId,
    secondaryLocaleId,
    translations
  ) {
    // 1. Get component content structure in primary locale
    const contentData = await client.components.getContent(siteId, componentId);

    // 2. Get component properties for a given component definition
    const propertiesData = await client.components.getProperties(
      siteId,
      componentId
    );

    // 3. Update static content in component definition
    if (translations.staticContent) {
      const staticUpdates = {
        nodes: contentData.nodes
          .filter((node) => translations.staticContent[node.id])
          .map((node) => {
            const update = { nodeId: node.id };
            if (node.type === "text") {
              update.text = translations.staticContent[node.id];
            } else if (node.type === "text-input") {
              update.placeholder = translations.staticContent[node.id];
            }
            return update;
          }),
      };

      await client.components.updateContent(siteId, componentId, {
        localeId: secondaryLocaleId,
        nodes: staticUpdates.nodes,
      });
    }

    // 4. Update component properties
    if (translations.properties) {
      const propertyUpdates = {
        properties: propertiesData.properties
          .filter((prop) => translations.properties[prop.propertyId])
          .map((prop) => ({
            propertyId: prop.propertyId,
            text: translations.properties[prop.propertyId],
          })),
      };

      await client.components.updateProperties(siteId, componentId, {
        localeId: secondaryLocaleId,
        properties: propertyUpdates.properties,
      });
    }
  }

  // Example `propertyTranslations` object holding the localized content for the secondary locale
  async function localizeComponentInstance(
    pageId,
    instanceNodeId,
    secondaryLocaleId,
    propertyTranslations
  ) {
    // Update component instance property overrides on a specific page
    const instanceUpdates = {
      nodes: [
        {
          nodeId: instanceNodeId,
          propertyOverrides: Object.entries(propertyTranslations).map(
            ([propertyId, text]) => ({
              propertyId,
              text,
            })
          ),
        },
      ],
    };

    await client.pages.updateStaticContent(pageId, {
      localeId: secondaryLocaleId,
      nodes: instanceUpdates.nodes,
    });
  }
  ```
</CodeBlocks>

## Best practices

* **Preserve HTML structure** - Always maintain `data-w-id` attributes in HTML content. These identifiers preserve custom styling, animations, and links across locales. Example:
  ```html
  // Original: "<p>Price: <span data-w-id=\"b310743e-a1ac-8409-c039-d3b594afb816\">$10</span></p>"
  // Localized: "<p>Precio: <span data-w-id=\"price-123\">$10</span></p>"
  ```
* **Batch operations** - Update multiple properties or nodes in single requests when possible (up to 1000 nodes per request)
* **Pagination** - Use `limit` and `offset` parameters in GET requests to retrieve all nodes/properties for components with extensive content
* **Content inheritance** - Only update content that needs localization; unchanged content inherits from the primary locale
* **Test in Webflow** - Verify localized content displays correctly across all component instances in Webflow. Refresh the canvas to see API changes reflected

## FAQ

<AccordionGroup>
  <Accordion title="What's the difference between component definition and instance localization?">
    Component definition localization affects all the base static content that
    lives in each instance of that component across your site, while instance
    localization only affects the specific component instance on a particular
    page through property overrides.
  </Accordion>

  <Accordion title="Can I localize read-only components?">
    No, read-only components (like those from Workspace Libraries) can't be
    updated via the APIs. These components are marked with `readonly: true` in
    the List Components response.
  </Accordion>

  <Accordion title="Do component property updates affect existing instances?">
    Yes, updating component definition property defaults affects all instances
    that don't have property overrides for those specific properties. Instances
    with overrides maintain their custom values and won't be affected by changes
    to the component definition.
  </Accordion>

  <Accordion title="Why are some component instances missing from page content?">
    In the primary locale, all component instances appear in the Get Page
    Content response. In secondary locales, only component instances with
    property overrides are included, providing a focused view of customized
    content that differs from the default component definition.
  </Accordion>

  <Accordion title="Can I update both static content and properties in one request?">
    No, static content and properties require separate API calls. Use the Update
    Component Content endpoint for static content and Update Component
    Properties for property values.
  </Accordion>

  <Accordion title="What happens if I don't preserve data-w-id attributes?">
    If you omit `data-w-id` attributes when updating HTML content, you may lose
    custom attributes or links that were applied to those elements in Webflow.
    Always preserve these identifiers exactly as they appear in the original
    content.
  </Accordion>
</AccordionGroup>
