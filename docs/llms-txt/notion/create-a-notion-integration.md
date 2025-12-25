# Build your first integration

Make your first request to the Notion API.

## Integration overview

In this guide, we’re going to build an [internal Notion integration](https://developers.notion.com/docs/getting-started#internal-integrations) that can create a new database in your Notion workspace via a web form.

![Demo web app that creates new databases in your Notion workspace.](https://files.readme.io/55d7b4b-dbform.png)

Demo web app that creates new databases in your Notion workspace.

Internal integrations are a good entry point to building integrations because they have a simpler [authorization](https://developers.notion.com/docs/authorization) flow than [public integrations](https://developers.notion.com/docs/getting-started#public-integrations).

Before diving in, let’s quickly review Notion integrations. Integrations define how the public API can programmatically interact with your Notion workspace. They need to be authorized (i.e., given explicit permission) to make any changes your workspace.

All integration types use Notion’s public API to make requests to update a Notion workspace. The specific use case for each integration can vary greatly, from using Notion as a CMS for a blog, to [tracking Github issues](https://github.com/makenotion/notion-sdk-js/tree/main/examples/notion-github-sync), to [sending emails](https://github.com/makenotion/notion-sdk-js/tree/main/examples/database-email-update) in response to Notion changes.

This guide is just one introductory example of what you can build with Notion’s public API.

## Today’s goals

This guide will demonstrate how to build an HTML form that will [create a new Notion database](https://developers.notion.com/reference/create-a-database) when submitted.

By the end of this guide, we’ll have a functional app that looks like this:

![Database form UI.](https://files.readme.io/36a22d6-dbform.png)

Database form UI.

The completed [sample code](https://github.com/makenotion/notion-sdk-js/tree/main/examples/web-form-with-express) includes additional examples beyond what’s covered in this guide, including forms to:

- [Add a new page](https://developers.notion.com/reference/post-page) to the database
- [Add content](https://developers.notion.com/reference/patch-block-children) to the new page
- [Add a comment](https://developers.notion.com/reference/create-a-comment) to the page content

### Requirements

To follow along with this guide, you will need:

- A [Notion account](https://www.notion.so/signup). To be a [Workspace Owner](https://www.notion.so/help/add-members-admins-guests-and-groups) in the workspace you’re using. You can create a new workspace for testing purposes otherwise.
- Knowledge of HTML and JavaScript. We’ll use [Express.js](https://expressjs.com/) for a server, as well.
- [npm and Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed locally to use the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) and [Express.js](https://expressjs.com/)

> **SDK usage is recommended, but not required**
>
> The [sample code](https://github.com/makenotion/notion-sdk-js/tree/main/examples/web-form-with-express) shown below uses the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) to make Notion API requests.
>
> Using the SDK for JavaScript is not required to build a Notion integration, but many JavaScript & TypeScript developers prefer it due to its ease of use.

## Getting started

### Create your integration in Notion

The first step to building any integration (internal or public) is to create a new integration in Notion’s integrations dashboard: [<https://www.notion.com/my-integrations>](https://www.notion.so/profile/integrations).

1. Click `+ New integration`.

![Image 2](https://files.readme.io/402cf3d-new_integrations_1.png)

2. Enter the integration name and select the associated workspace for the new integration.

![Image 3](https://files.readme.io/aef3bab-new_integrations_2.png)

### Get your API secret

API requests require an API secret to be successfully authenticated. Visit the `Configuration` tab to get your integration’s API secret (or “Internal Integration Secret”).

![Image 4](https://files.readme.io/7ec836a-integrations_3.png)

> **👍 Keep your API secret a secret!**
>
> Any value used to authenticate API requests should always be kept secret. Use environment variables and avoid committing sensitive data to your version control history.
>
> If you do accidentally expose it, remember to “refresh” your secret.

### Give your integration page permissions

To give your integration page permissions, go to the `Permissions` tab and click on the `Allow` button for all page types.

![Image 5](https://files.readme.io/fc3e200-allow_page_permissions.png)
```

# Giving Your Integration Page Permissions

The database that we’re about to create will be added to a parent Notion page in your workspace. For your integration to interact with the page, it needs explicit permission to read/write to that specific Notion page.

To give the integration permission, you will need to:

1. Pick (or create) a Notion page.
2. Click on the button with the `+ Add Connections` icon in the top-right corner of the page.
3. Scroll down to `+ Add Connections`.
4. Search for your integration and select it.
5. Confirm the integration can access the page and all of its child pages.

![Give your integration permission to add a database to a page.](https://files.readme.io/fefc809-permissions.gif)

Your integration can now make API requests related to this Notion page and any of its children.

If you are building a public integration, use the authorization instructions included in the [Authorization guide](https://developers.notion.com/docs/authorization#public-integration-auth-flow-set-up) instead.

> 🚧 Double-check your page access
>
> If your API requests are failing, confirm you have given the integration permission to the page you are trying to update. This is a common cause of API request errors.

---

## Setting up the Demo Locally

In this example, we’ll have three key files:

- `index.html`, which will contain our client-side markdown (HTML).
- `client.js`, which will contain our client-side JavaScript code.
- `server.js`, which will contain our server-side JavaScript code. This file contains all the endpoints to make requests to Notion’s public API, as well as to serve the `index.html` file. ([More on that below.](#step-3-importing-the-notion-sdk-serverjs))

All of the sample code is available in [GitHub](https://github.com/makenotion/notion-sdk-js/tree/main/examples/web-form-with-express).

> 📘 Various examples are available
>
> This integration includes frontend code, but integrations can be server-side only as well. See more examples of different integration use cases in [GitHub](https://github.com/makenotion/notion-sdk-js/tree/main/examples).

### Clone Demo Repo

To run this project locally, clone the repo and install its dependencies ([Express.js](https://expressjs.com/en/starter/installing.html), [dotenv](https://www.npmjs.com/package/dotenv), and [Notion’s SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)):

```sh
# Clone this repository locally
git clone https://github.com/makenotion/notion-sdk-js.git

# Switch into this project
cd notion-sdk-js/examples/web-form-with-express/

# Install the dependencies
npm install
```

### Environment Variables

In your `.env` file, add the following variables:

```sh
NOTION_KEY=<your-notion-api-key>
NOTION_PAGE_ID=<parent-page-id>
```

Add the API secret you retrieved in `Getting Started` to `NOTION_KEY`, as well as a page ID (`NOTION_PAGE_ID`) for the page that you gave the integration permission to update.

> 👍 How database IDs work
>
> When using the API to [create a database](https://developers.notion.com/reference/create-a-database), the parent of a database must be a Notion page or a [wiki](https://www.notion.so/help/wikis-and-verified-pages) database. To get the ID of the page, locate the 32-character string at the end of the page’s URL.

As a best practice, add `.env` to your `.gitignore` file to ensure you don’t accidentally share these personalized values.

### Running the Project Locally

To run this project locally, you will need to enter the following command in your terminal:

```sh
npm start
```

Next, let’s look at how our database form works.

---

## Creating a New Database

### Step 1: Adding a Database Form (`index.html`)

In our `index.html` file, we need a form for the user to create a new database and an area for the API response to be displayed. This is how the user will initiate a public API request.

![App design for creating a database.](https://files.readme.io/76077fd-new_database.png)

![Rendered app design for creating a database.](https://files.readme.io/c73de3e-dbform.png)

The corresponding [HTML elements](https://github.com/makenotion/notion-sdk-js/blob/main/examples/web-form-with-express/views/index.html#L40) related to creating a database are shown below:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">

    <!-- Import the webpage's client-side javascript file -->
    <script src="/client.js" defer></script>
  </head>
  <body>
    ...
      <table>
        ...
        <tr>
          <td>
            <h3>1. Create a new database</h3>
            <!-- Form to create a database -->
            <form id="databaseForm">
              <label for="dbName">Database name</label>
              <input type="text" id="dbName" />
              <input type="submit" />
            </form>
          </td>
          <!-- Empty table cell to append the API response to -->
          <td id="dbResponse"></td>
        </tr>
        ...
      </table>
    </main>
    ...
  </body>
</html>
```

In terms of what’s rendered in the `<body>`, notice the `<form>` element and an empty table cell with the ID `dbResponse`. The latter is where we’ll append the Notion API response information.

The database form includes two inputs:

- A text input for the database name
- A submit input to submit the form

Also of note: the `client.js` file is included in the document’s `<head>` tag, which allows us to apply client-side JavaScript to interact with these HTML elements.

### Step 2: Handling the Form Submission (`client.js`)

In `client.js`, we can write a function to describe what should happen when the database form is submitted. In short, we want to make a request to `/databases` endpoint in `server.js` to then make an API request to Notion. The actual Notion API request will happen server-side to avoid exposing our API secret in the client. (In other words, it’s more secure!)

```js
// Assign the database form to a variable for later use
const dbForm = document.getElementById("databaseForm");
// Assign the empty table cell to a variable for later use
const dbResponseEl = document.getElementById("dbResponse");

// Add a submit handler to the form
dbForm.onsubmit = async function (event) {
  event.preventDefault()

// Get the database name from the form
  const dbName = event.target.dbName.value
  const body = JSON.stringify({ dbName })

// Make a request to /databases endpoint in server.js
  const newDBResponse = await fetch("/databases", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body,
  })
  const newDBData = await newDBResponse.json()

// Pass the new database info and the empty table cell
// to a function that will append it.
  appendApiResponse(newDBData, dbResponseEl)
}

```

In this code block, we select the form element using its ID attribute with `getElementById()`. Next, we attach an async function to the `onsubmit` event that will make a request to our local server’s `/databases` endpoint. (This endpoint will be described below in our `server.js` code.) The function is asynchronous because we need to wait for a response from our server before proceeding.

The response is then appended to our `index.html` document. ([More on this below.](#step-5-displaying-the-response-indexhtml))

### Step 3: Importing the Notion SDK (`server.ts`)

Let’s start by looking at our `server.ts` file without the Notion-related endpoints:

```ts
require("dotenv").config();
const express = require("express");
const app = express();

// Notion SDK for JavaScript
const { Client } = require("@notionhq/client");
const notion = new Client({ auth: process.env.NOTION_KEY });

// http://expressjs.com/en/starter/static-files.html
app.use(express.static("public"));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function(request, response) {
  response.sendFile(__dirname + "/views/index.html");
});

// 
```
```

# Step 1: Initialize the Notion Client

```jsx
const { Client } = require("@notionhq/client");
const notion = new Client({ auth: process.env.NOTION_KEY });
```

We can now make requests to Notion's API in this file without having to worry about authentication again.

## Step 2: Create a Database with a Single Data Source

```typescript
app.post("/databases", async function (request, response) {
  const pageId = process.env.NOTION_PAGE_ID;
  const title = request.body.dbName;

  try {
    // Notion API request!
    const newDb = await notion.databases.create({
      parent: {
        type: "page_id",
        page_id: pageId,
      },
      title: [
        {
          type: "text",
          text: {
            content: title,
          },
        },
      ],
      initial_data_source: {
        properties: {
          Name: {
            title: {},
          },
        },
      },
    });
    response.json({ message: "success!", data: newDb });
  } catch (error) {
    response.json({ message: "error", error });
  }
});
```

`app.post()` indicates this endpoint is for POST requests, and the first argument (`"/databases"`) indicates this function corresponds to requests made to the `/databases` path, as we did in our client-side code above.

To create a new database with one data source, we’ll use the [Create a database](https://developers.notion.com/reference/create-a-database) endpoint:

```typescript
await notion.databases.create({...options})
```

To use this endpoint, we need to pass the parent page ID in the body parameters. This page ID is the one already set in the environment variables. The page ID **must** be included in this request.

```typescript
const pageId = process.env.NOTION_PAGE_ID;
...
try {
  const newDb = await notion.databases.create({
    parent: {
      type: "page_id",
      page_id: pageId,
    },
		...
}
```

(Note: Environment variables can only be accessed in `server.js`, not `client.js`.)

In this example, the title of the database should also be set. The title was provided in the form the user submitted, which we can access from the request’s body (`request.body.dbName`).

```typescript
try {
  const newDb = await notion.databases.create({
    parent: {...},
    title: [
      {
        type: "text",
        text: {
          content: title, // Include the user's title in the request
        },
      },
    ],
    // ...
}
```

Finally, we need to describe the [data source's properties](https://makenotion.github.io/notion-sdk-js/reference/property-object). The properties represent the columns in a data source (or the “schema”, depending on which terminology you prefer.)

In this case, our data source will have just one column called “Name”, which will represent the page names of its child pages:

```typescript
try {
  const newDb = await notion.databases.create({
    parent: {...},
    title: [...],
    properties: {
      Name: {
        title: {},
      },
    },
  })
...

```

Finally, assuming the request works, we can return the response from Notion’s API back to our original fetch request in `client.js`:

```javascript
...
response.json({ message: "success!", data: newDb });
```

If it doesn’t work, we’ll return whatever error message we get from Notion’s API:

```javascript
try {
...
} catch (error) {
  response.json({ message: "error", error });
}
```

Now that we have our new database, the response can be added to the HTML document via the client-side JavaScript (`client.js`).

## Step 3: Displaying the Response

Let’s first look at an example of the object the `/databases` endpoint responds with, which includes the [object](https://makenotion.github.io/notion-sdk-js/reference/object) that gets returned from the Notion API when we create a new database:

```json
{
  "message": "success!",
  "data": { // from Notion
    "object": "database",
    "id": "e604f78c-4145-4444-b7d5-1adea4fa5d08",
    "cover": null,
    "icon": null,
    "created_time": "2023-07-18T20:56:00.000Z",
    "created_by": { "object": "user", "id": "44b170f0-16ac-47cf-aaaa-8f2eab66hhhh" },
    "last_edited_by": {
      "object": "user",
      "id": "44b170f0-16ac-47cf-gggg-8f2eab6rrrra"
    },
    "last_edited_time": "2023-07-18T20:56:00.000Z",
    "title": [
      {
        "type": "text",
        "text": [Object],
        "annotations": [Object],
        "plain_text": "test db",
        "href": null
      }
    ],
    "description": [],
    "is_inline": false,
    "data_sources": [
      {
        "id": "a2216f7f-574f-4ae7-8df9-9eb8a65ec62d",
        "name": "..."
      }
    ],
    "parent": {
      "type": "page_id",
      "page_id": "e7261079-9d30-4313-9999-14b29880gggg"
    },
    "url": "<https://www.notion.so/e604f78c414548c6b7d51adea4fadddd>",
    "public_url": null,
    "archived": false,
    "in_trash": false
  },
}
```

The most important information here (for our purposes) is the data source ID (`data.data_sources[0].id`). The ID will be required to make API requests to the [Create a page](https://developers.notion.com/reference/post-page) endpoint, which is the next form in our completed demo’s UI.

Knowing this JSON structure, let’s now look at how `appendApiResponse()` works:

```jsx
const dbForm = document.getElementById("databaseForm");
// Empty table cell where we'll display the API response
const dbResponse = document.getElementById("dbResponse");

// Appends the API response to the UI
const appendApiResponse = function (apiResponse, el) {
  // Add success message to UI
  const newParagraphSuccessMsg = document.createElement("p")
  newParagraphSuccessMsg.innerHTML = "Result: " + apiResponse.message
  el.appendChild(newParagraphSuccessMsg)

  // See browser console for more information if there's an error
  if (apiResponse.message === "error") return

  // Add ID of Notion item (db, page, comment) to UI
  const newParagraphId = document.createElement("p")
  newParagraphId.innerHTML = "ID: " + apiResponse.data.id
  if ("data_sources" in apiResponse.data) {
    // Include the initial data source ID for database responses.
    // Pages must identify which data source under a database they live under.
    newParagraphId.innerHTML += "; Data Source ID: " + apiResponse.data.data_sources[0].id
  }
  el.appendChild(newParagraphId)

  // Add URL of Notion item (db, page) to UI
  if (apiResponse.data.url) {
    const newAnchorTag = document.createElement("a")
    newAnchorTag.setAttribute("href", apiResponse.data.url)
    newAnchorTag.innerText = apiResponse.data.url
    el.appendChild(newAnchorTag)
  }
}

```

`appendApiResponse(res, form)` accepts two parameters: the response (shown above) and the HTML element where we will append the response — in this case, an empty table cell next to the database form.

In this function, we first add a paragraph element to show the response message (i.e., whether it was a success or the error):

```jsx
const newParagraphSuccessMsg = document.createElement("p")
newParagraphSuccessMsg.innerHTML = "Result: " + apiResponse.message
el.appendChild(newParagraphSuccessMsg)
```

Then, we do the same with the database ID & data source ID after confirming the response was not an error:

```jsx
if (apiResponse.message === "error") return

// Add ID of database and data source to UI
const newParagraphId = document.createElement("p")
newParagraphId.innerHTML = "Database ID: " +
  apiResponse.data.id + "; Data Source ID" + apiResponse.data.data_sources[0].id
el.appendChild(newParagraphId)
```

Finally, if the response has a URL, we display that too with an anchor (```<a>``` tag. This allows the user to visit the database directly in Notion.

```jsx
if (apiResponse.data.url) {
  const newAnchorTag = document.createElement("a")
  newAnchorTag.setAttribute("href", apiResponse.data.url)
  newAnchorTag.innerText = apiResponse.data.url
  el.appendChild(newAnchorTag)
}
```

(Note: This function will be reused by other forms. Not all responses have a ```url``` property, which is why we check for it.)

Once this is done, our HTML document is updated and the form submission is officially complete.

## Step 4: Handling the Form's POST Request

Staying in `server.ts`, we can add the following code that will be invoked when the database form makes a POST request to `/databases`:

```typescript
app.post("/databases", async function (request, response) {
  const pageId = process.env.NOTION_PAGE_ID;
  const title = request.body.dbName;

  try {
    // Notion API request!
    const newDb = await notion.databases.create({
      parent: {
        type: "page_id",
        page_id: pageId,
      },
      title: [
        {
          type: "text",
          text: {
            content: title,
          },
        },
      ],
      initial_data_source: {
        properties: {
          Name: {
            title: {},
          },
        },
      },
    });
    response.json({ message: "success!", data: newDb });
  } catch (error) {
    response.json({ message: "error", error });
  }
});
```

`app.post()` indicates this endpoint is for POST requests, and the first argument (`"/databases"`) indicates this function corresponds to requests made to the `/databases` path, as we did in our client-side code above.

Next, we can actually interact with the Notion API.

To create a new database with one data source, we’ll use the [Create a database](https://developers.notion.com/reference/create-a-database) endpoint:

```typescript
await notion.databases.create({...options})
```

To use this endpoint, we need to pass the parent page ID in the body parameters. This page ID is the one already set in the environment variables. The page ID **must** be included in this request.

```typescript
const pageId = process.env.NOTION_PAGE_ID;
...
try {
  const newDb = await notion.databases.create({
    parent: {
      type: "page_id",
      page_id: pageId,
    },
		...
}
```

(Note: Environment variables can only be accessed in `server.js`, not `client.js`.)

In this example, the title of the database should also be set. The title was provided in the form the user submitted, which we can access from the request’s body (`request.body.dbName`).

```typescript
try {
  const newDb = await notion.databases.create({
    parent: {...},
    title: [
      {
        type: "text",
        text: {
          content: title, // Include the user's title in the request
        },
      },
    ],
    // ...
}
```

Finally, we need to describe the [data source's properties](https://makenotion.github.io/notion-sdk-js/reference/property-object). The properties represent the columns in a data source (or the “schema”, depending on which terminology you prefer.)

In this case, our data source will have just one column called “Name”, which will represent the page names of its child pages:

```typescript
try {
  const newDb = await notion.databases.create({
    parent: {...},
    title: [...],
    properties: {
      Name: {
        title: {},
      },
    },
  })
...

```

Finally, assuming the request works, we can return the response from Notion’s API back to our original fetch request in `client.js`:

```javascript
...
response.json({ message: "success!", data: newDb });
```

If it doesn’t work, we’ll return whatever error message we get from Notion’s API:

```javascript
try {
...
} catch (error) {
  response.json({ message: "error", error });
}
```

Now that we have our new database, the response can be added to the HTML document via the client-side JavaScript (`client.js`).

## Step 5: Displaying the Response

Let’s first look at an example of the object the `/databases` endpoint responds with, which includes the [object](https://makenotion.github.io/notion-sdk-js/reference/object) that gets returned from the Notion API when we create a new database:

```json
{
  "message": "success!",
  "data": { // from Notion
    "object": "database",
    "id": "e604f78c-4145-4444-b7d5-1adea4fa5d08",
    "cover": null,
    "icon": null,
    "created_time": "2023-07-18T20:56:00.000Z",
    "created_by": { "object": "user", "id": "44b170f0-16ac-47cf-aaaa-8f2eab66hhhh" },
    "last_edited_by": {
      "object": "user",
      "id": "44b170f0-16ac-47cf-gggg-8f2eab6rrrra"
    },
    "last_edited_time": "2023-07-18T20:56:00.000Z",
    "title": [
      {
        "type": "text",
        "text": [Object],
        "annotations": [Object],
        "plain_text": "test db",
        "href": null
      }
    ],
    "description": [],
    "is_inline": false,
    "data_sources": [
      {
        "id": "a2216f7f-574f-4ae7-8df9-9eb8a65ec62d",
        "name": "..."
      }
    ],
    "parent": {
      "type": "page_id",
      "page_id": "e7261079-9d30-4313-9999-14b29880gggg"
    },
    "url": "<https://www.notion.so/e604f78c414548c6b7d51adea4fadddd>",
    "public_url": null,
    "archived": false,
    "in_trash": false
  },
}
```

The most important information here (for our purposes) is the data source ID (`data.data_sources[0].id`). The ID will be required to make API requests to the [Create a page](https://developers.notion.com/reference/post-page) endpoint, which is the next form in our completed demo’s UI.

Knowing this JSON structure, let’s now look at how `appendApiResponse()` works:

```jsx
const dbForm = document.getElementById("databaseForm");
// Empty table cell where we'll display the API response
const dbResponse = document.getElementById("dbResponse");

// Appends the API response to the UI
const appendApiResponse = function (apiResponse, el) {
  // Add success message to UI
  const newParagraphSuccessMsg = document.createElement("p")
  newParagraphSuccessMsg.innerHTML = "Result: " + apiResponse.message
  el.appendChild(newParagraphSuccessMsg)

  // See browser console for more information if there's an error
  if (apiResponse.message === "error") return

  // Add ID of Notion item (db, page, comment) to UI
  const newParagraphId = document.createElement("p")
  newParagraphId.innerHTML = "ID: " + apiResponse.data.id
  if ("data_sources" in apiResponse.data) {
    // Include the initial data source ID for database responses.
    // Pages must identify which data source under a database they live under.
    newParagraphId.innerHTML += "; Data Source ID: " + apiResponse.data.data_sources[0].id
  }
  el.appendChild(newParagraphId)

  // Add URL of Notion item (db, page) to UI
  if (apiResponse.data.url) {
    const newAnchorTag = document.createElement("a")
    newAnchorTag.setAttribute("href", apiResponse.data.url)
    newAnchorTag.innerText = apiResponse.data.url
    el.appendChild(newAnchorTag)
  }
}

```

`appendApiResponse(res, form)` accepts two parameters: the response (shown above) and the HTML element where we will append the response — in this case, an empty table cell next to the database form.

In this function, we first add a paragraph element to show the response message (i.e., whether it was a success or the error):

```jsx
const newParagraphSuccessMsg = document.createElement("p")
newParagraphSuccessMsg.innerHTML = "Result: " + apiResponse.message
el.appendChild(newParagraphSuccessMsg)
```

Then, we do the same with the database ID & data source ID after confirming the response was not an error:

```jsx
if (apiResponse.message === "error") return

// Add ID of database and data source to UI
const newParagraphId = document.createElement("p")
newParagraphId.innerHTML = "Database ID: " +
  apiResponse.data.id + "; Data Source ID" + apiResponse.data.data_sources[0].id
el.appendChild(newParagraphId)
```

Finally, if the response has a URL, we display that too with an anchor (```<a>``` tag. This allows the user to visit the database directly in Notion.

```jsx
if (apiResponse.data.url) {
  const newAnchorTag = document.createElement("a")
  newAnchorTag.setAttribute("href", apiResponse.data.url)
  newAnchorTag.innerText = apiResponse.data.url
  el.appendChild(newAnchorTag)
}
```

(Note: This function will be reused by other forms. Not all responses have a ```url``` property, which is why we check for it.)

Once this is done, our HTML document is updated and the form submission is officially complete.

## Testing the Feature

Let’s see the final results of testing this new feature:

![Submitting the database form and visiting the Notion URL from the response.](https://files.readme.io/e58e2ed-newdb.gif)

The database form is submitted and the response from Notion's API is appended to our UI. 🎉 We can click the link to visit the new database in Notion and confirm it worked as expected.

As a next step, the new data source ID can be copied and pasted into the page form below it to create a new page in the data source. We can also use the page ID that the page form returns to add content to the page or comment on it using the block and comment forms.

We won’t cover the code for page, blocks, or comment forms here, but the code is all included in the [source code](https://github.com/makenotion/notion-sdk-js/blob/main/examples/web-form-with-express/views/index.html) for reference. It works the same as the
```

# Integration overview

In this guide, we’re going to build an [internal Notion integration](/docs/getting-started#internal-integrations) that can create a new database in your Notion workspace via a web form.

![Demo web app that creates new databases in your Notion workspace.](https://files.readme.io/55d7b4b-dbform.png)

Internal integrations are a good entry point to building integrations because they have a simpler [authorization](/docs/authorization) flow than [public integrations](/docs/getting-started#public-integrations).

Before diving in, let’s quickly review Notion integrations. Integrations define how the public API can programmatically interact with your Notion workspace. They need to be authorized (i.e., given explicit permission) to make any changes your workspace.

All integration types use Notion’s public API to make requests to update a Notion workspace. The specific use case for each integration can vary greatly, from using Notion as a CMS for a blog, to [tracking Github issues](https://github.com/makenotion/notion-sdk-js/tree/main/examples/notion-github-sync), to [sending emails](https://github.com/makenotion/notion-sdk-js/tree/main/examples/database-email-update) in response to Notion changes.

This guide is just one introductory example of what you can build with Notion’s public API.

## Today’s goals

This guide will demonstrate how to build an HTML form that will [create a new Notion database](/reference/create-a-database) when submitted.

By the end of this guide, we’ll have a functional app that looks like this:

![Database form UI.](https://files.readme.io/36a22d6-dbform.png)

The completed [sample code](https://github.com/makenotion/notion-sdk-js/tree/main/examples/web-form-with-express) includes additional examples beyond what’s covered in this guide, including forms to:

- [Add a new page](/reference/post-page) to the database
- [Add content](/reference/patch-block-children) to the new page
- [Add a comment](/reference/create-a-comment) to the page content

### Requirements

To follow along with this guide, you will need:

- A [Notion account](https://www.notion.so/signup).
- To be a [Workspace Owner](https://www.notion.so/help/add-members-admins-guests-and-groups) in the workspace you’re using. You can create a new workspace for testing purposes otherwise.
- Knowledge of HTML and JavaScript. We’ll use [Express.js](https://expressjs.com/) for a server, as well.
- [npm and Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed locally to use the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) and [Express.js](https://expressjs.com/)

> 📘SDK usage is recommended, but not required
> 
> The [sample code](https://github.com/makenotion/notion-sdk-js/tree/main/examples/web-form-with-express) shown below uses the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) to make Notion API requests.
> 
> Using the SDK for JavaScript is not required to build a Notion integration, but many JavaScript & TypeScript developers prefer it due to its ease of use.

## Getting started

### Create your integration in Notion

The first step to building any integration (internal or public) is to create a new integration in Notion’s integrations dashboard: [<https://www.notion.com/my-integrations>](https://www.notion.so/profile/integrations).

1. Click `+ New integration`.

![Image 2](https://files.readme.io/402cf3d-new_integrations_1.png)

2. Enter the integration name and select the associated workspace for the new integration.

![Image 3](https://files.readme.io/aef3bab-new_integrations_2.png)

### Get your API secret

API requests require an API secret to be successfully authenticated. Visit the `Configuration` tab to get your integration’s API secret (or “Internal Integration Secret”).

![Image 4](https://files.readme.io/7ec836a-integrations_3.png)

> 👍Keep your API secret a secret!
> 
> Any value used to authenticate API requests should always be kept secret. Use environment variables and avoid committing sensitive data to your version control history.
> 
> If you do accidentally expose it, remember to “refresh” your secret.

### Give your integration page permissions

The database that we’re about to create will be added to a parent Notion page in your workspace. For your integration to interact with the page, it needs explicit permission to read/write to that specific Notion page.

To give the integration permission, you will need to:

1. Pick (or create) a Notion page.
2. Click on the `...` More menu in the top-right corner of the page.
3. Scroll down to `+ Add Connections`.
4. Search for your integration and select it.
5. Confirm the integration can access the page and all of its child pages.

![Give your integration permission to add a database to a page.](https://files.readme.io/fefc809-permissions.gif)

Your integration can now make API requests related to this Notion page and any of its children.

If you are building a public integration, use the authorization instructions included in the [Authorization guide](/docs/authorization#public-integration-auth-flow-set-up) instead.

> 🚧Double-check your page access
> 
> If your API requests are failing, confirm you have given the integration permission to the page you are trying to update. This is a common cause of API request errors.

---

## Setting up the demo locally

In this example, we’ll have three key files:

- `index.html`, which will contain our client-side markdown (HTML).
- `client.js`, which will contain our client-side JavaScript code.
- `server.js`, which will contain our server-side JavaScript code. This file contains all the endpoints to make requests to Notion’s public API, as well as to serve the `index.html` file. ([More on that below.](#step-3-importing-the-notion-sdk-serverjs))

All of the sample code is available in [GitHub](https://github.com/makenotion/notion-sdk-js/tree/main/examples/web-form-with-express).

> 📘Various examples are available
> 
> This integration includes frontend code, but integrations can be server-side only as well. See more examples of different integration use cases in [GitHub](https://github.com/makenotion/notion-sdk-js/tree/main/examples).

### Clone demo repo

To run this project locally, clone the repo and install its dependencies ([Express.js](https://expressjs.com/en/starter/installing.html), [dotenv](https://www.npmjs.com/package/dotenv), and [Notion’s SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)):

```sh
# Clone this repository locally
git clone https://github.com/makenotion/notion-sdk-js.git

# Switch into this project
cd notion-sdk-js/examples/web-form-with-express/

# Install the dependencies
npm install
```

### Environment variables

In your `.env` file, add the following variables:

```sh
NOTION_KEY=<your-notion-api-key>
NOTION_PAGE_ID=<parent-page-id>
```

Add the API secret you retrieved in `Getting Started` to `NOTION_KEY`, as well as a page ID (`NOTION_PAGE_ID`) for the page that you gave the integration permission to update.

> 👍How database IDs work
> 
> When using the API to [create a database](/reference/create-a-database), the parent of a database must be a Notion page or a [wiki](https://www.notion.so/help/wikis-and-verified-pages) database. To get the ID of the page, locate the 32-character string at the end of the page’s URL.
> 
> ![The page ID is highlighted.](https://files.readme.io/7e8a54d-notion-page-url.png)

As a best practice, add `.env` to your `.gitignore` file to ensure you don’t accidentally share these personalized values.

### Running the project locally

To run this project locally, you will need to enter the following command in your terminal:

```sh
npm start
```

Next, let’s look at how our database form works.

---

## Creating a new database

### Step 1: Adding a database form (`index.html`)

In our `index.html`, we will add a form that allows users to fill out details about creating a new database. Then, once submitted, the form will trigger a request to the Notion API to create the database.

#### HTML structure

```html
<!DOCTYPE html>
<html lang="en-US">
<head>

    <title>Database Form</title>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="styles.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    
</head>
<body>

    <form action="#" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required="">
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required="">
        
        <label for="description">Description:</label>
        <textarea id="description" name="description" required=""></textarea>
        
        <button type="submit">Submit</button>
    </form>
    
</body>
</html>
```

#### JavaScript logic

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    const form = document.getElementById('database-form');

    // Create an event listener for the 'submit' event
    form.addEventListener('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Make a POST request to the Notion API
        fetch('/api/database', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                description: document.getElementById('description').value
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(`Database created successfully: ${data.message}`);
        })
        .catch(error => console.error('Error creating database:', error));
    });
});
```

This code will submit the form data to the `/api/database` endpoint, which handles the creation of a new database. The `/api/database` endpoint is where the Notion API expects to receive the request.

### Step 2: API integration

Now that we have our form working, we need to set up the API side of things. As mentioned earlier, the Notion API expects a POST request with JSON data.

#### Express.js server setup

```javascript
const express = require('express');
const app = express();
const dotenv = require('dotenv');
const { v4 as uuid } = require('uuid');
const fs = require('fs');
const jwt = require('jsonwebtoken');
const moment = require('moment');
const db = require('./database');

app.use(express.json());

// Function to generate a unique database ID
function generateId() {
    return uuid().toString().slice(1, 36);
}

// Function to check if a token is valid
function isValidToken(token) {
    try {
        const decoded = jwt.decode(token);
        if (decoded.email !== process.env.NOTION_USER_EMAIL) {
            throw new Error('Invalid token');
        }
        return true;
    } catch (error) {
        return false;
    }
}

// Function to create a new database
async function createDatabase(db, token) {
    if (!isValidToken(token)) {
        return Promise.reject(new Error('Invalid token'));
    }

    const now = moment().format('YYYY-MM-DD HH:mm:ss');
    const id = await db.create({ name: req.body.name, email: req.body.email, description: req.body.description, created_at: now });
    const url = `/${now}_${id}`;
    fs.writeFileSync(__dirname + '/redirect.html', `<h1>Welcome to your new database!</h1><p>Access your new database at <a href="${url}">${url}</a>.</p>`);
    return { message: `Database created successfully: ${id}` };
}

// Route for creating a new database
app.post('/api/database', async (req, res) => {
    try {
        const token = req.headers.authorization || '';
        if (!token.startsWith('Bearer ') && !isValidToken(token)) {
            res.status(401).json({ message: 'Unauthorized' });
            return;
        }

        const data = req.body;
        const result = await createDatabase(db, token);
        res.json(result);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```

In this server code:
- We define a `generateId()` function to create a unique database ID.
- We set up a route to handle creating a new database, which checks if the token is valid.
- We use the Notion API to create the database and send a redirect to the newly created database.

### Step 3: Importing the Notion SDK

In the `server.js` file, we import the Notion SDK and configure the connection settings.

```javascript
const { connect } = require('notion-sdk');
const config = require('../config');

connect(config.api_url, config.token, (err, client) => {
    if (err) {
        console.error(err);
        process.exit(1);
    }
    global.client = client;
});
```

We then initialize the global `client` variable with the Notion SDK instance.

### Step 4: Serving the form

Finally, we serve the form and redirect the user to the newly created database once the database is created.

```javascript
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.post('/api/database', async (req, res) => {
    try {
        const token = req.headers.authorization || '';
        if (!token.startsWith('Bearer ') && !isValidToken(token)) {
            res.status(401).json({ message: 'Unauthorized' });
            return;
        }

        const data = req.body;
        const result = await createDatabase(db, token);
        res.json(result);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```

In this final code:
- We define two routes: one for serving the form and another for creating a new database.
- After the database is created, we redirect the user to the database.

### Step 5: Testing locally

To test everything, run the server using:

```sh
node server.js
```

Then visit the URL provided by the server in your browser. You should see a form. Fill out the fields and click the 'Submit' button. You should see a success message displayed.

### Step 6: Deploying to production

Once you’ve tested locally, you can deploy your integration to production. The deployment process typically involves setting up a serverless infrastructure like AWS Lambda or deploying the application to a cloud platform like Heroku or Render.

Deploying a Notion integration involves updating the integration in Notion’s integrations dashboard with the new API secret and page permissions, as well as ensuring the correct environment variables are set for the server.

For more detailed deployment instructions, refer to Notion’s documentation on integrating APIs with their services.

---

## Wrapping up

This guide demonstrated how to use Notion’s API (via the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)) to build an internal integration. With this demo app, users can programmatically create a new database in their Notion workspace by filling out a form in the app UI and making a request to Notion’s public API — the [Create a database](https://developers.notion.com/reference/create-a-database) endpoint.

As a reminder, this example includes client-side code to allow for user interactions via a GUI (graphical user interface). Notion integrations do not require a UI, however. What you build is completely up to you!

To see examples of server-side-only integrations, test out the sample apps in the SDK’s [GitHub repo](https://github.com/makenotion/notion-sdk-js/tree/main/examples).

## Next steps

To learn more about authorizing API requests or to learn how to add an auth flow to your public integration, read the [Authorization guide](https://developers.notion.com/docs/authorization) next.

### Additional resources

- [Reference documentation](https://developers.notion.com/reference/intro)
- [JavaScript client](https://github.com/makenotion/notion-sdk-js)
- [Postman collection](https://www.postman.com/notionhq/)
- [TypeScript starter template](https://github.com/makenotion/notion-sdk-typescript-starter)
- [FAQs](https://developers.notion.com/page/frequently-asked-questions)
- [Slack developer community](https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg)
```

# Creating a Database with Notion's API

## Overview

We're building a web application that allows users to create databases and display the responses from Notion's API. This application will be built in three stages:

1. **Stage 1**: Create a database and display its contents.
2. **Stage 2**: Handle the form submission and send a request to the server.
3. **Stage 3**: Use the Notion SDK to make an API request.

## Stage 1: Create a Database

The first step is to create a database. We'll do this by selecting a form and adding a new database with a single field for the database name.

### HTML Elements

The corresponding HTML elements for creating a database are:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    ...
<!-- Import the webpage's stylesheet -->
<link rel="stylesheet" href="/style.css">

<!-- Import the webpage's client-side javascript file -->
<script src="/client.js" defer></script>
  </head>
  <body>
    ...
      <table>
        ...
        <tr>
          <td>
            <h3>1. Create a new database</h3>
<!-- Form to create a database -->
<form id="databaseForm">
  <label for="dbName">Database name</label>
  <input type="text" id="dbName"/>
  <input type="submit"/>
</form>
          </td>
        <!-- Empty table cell to append the API response to -->
          <td id="dbResponse"></td>
        </tr>
        ...
      </table>
    </main>
    ...
  </body>
</html>
```

### JavaScript

The JavaScript code for handling the form submission is in `client.js`:

```javascript
// Assign the database form to a variable for later use
const dbForm = document.getElementById("databaseForm");
// Assign the empty table cell to a variable for later use
const dbResponseEl = document.getElementById("dbResponse");

// Add a submit handler to the form
dbForm.onsubmit = async function (event) {
  event.preventDefault()
// Get the database name from the form
  const dbName = event.target.dbName.value
  const body = JSON.stringify({ dbName })

// Make a request to /databases endpoint in server.js
  const newDBResponse = await fetch("/databases", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body,
  })
  const newDBData = await newDBResponse.json()

// Pass the new database info and the empty table cell
// to a function that will append it.
  appendApiResponse(newDBData, dbResponseEl)
}
```

## Stage 2: Handle the Form Submission

In `client.js`, we handle the form submission by preventing the default behavior of the form, fetching the database name from the form, making a request to the Notion API, and appending the response to the HTML document.

### JavaScript

```javascript
// Assign the database form to a variable for later use
const dbForm = document.getElementById("databaseForm");
// Assign the empty table cell to a variable for later use
const dbResponseEl = document.getElementById("dbResponse");

// Add a submit handler to the form
dbForm.onsubmit = async function (event) {
  event.preventDefault()

// Get the database name from the form
  const dbName = event.target.dbName.value
  const body = JSON.stringify({ dbName })

// Make a request to /databases endpoint in server.js
  const newDBResponse = await fetch("/databases", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body,
  })
  const newDBData = await newDBResponse.json()

// Pass the new database info and the empty table cell
// to a function that will append it.
  appendApiResponse(newDBData, dbResponseEl)
}
```

## Stage 3: Import the Notion SDK

To use the Notion SDK, we need to import it into `server.ts`. We initialize a new Notion Client instance and set the `auth` option to the Notion API secret.

### TypeScript

```typescript
const { Client } = require("@notionhq/client");
const notion = new Client({ auth: process.env.NOTION_KEY });
```

## Stage 4: Handle the Form's POST Request

In `server.ts`, we handle the `POST` request to `/databases` and create a new database with a data source.

### TypeScript

```typescript
app.post("/databases", async function (request, response) {
  const pageId = process.env.NOTION_PAGE_ID;
  const title = request.body.dbName;

  try {
    // Notion API request!
    const newDb = await notion.databases.create({
      parent: {
        type: "page_id",
        page_id: pageId,
      },
      title: [
        {
          type: "text",
          text: {
            content: title,
          },
        },
      ],
      initial_data_source: {
        properties: {
          Name: {
            title: {},
          },
        },
      },
    });
    response.json({ message: "success!", data: newDb });
  } catch (error) {
    response.json({ message: "error", error });
  }
});
```

## Stage 5: Displaying the Response

After creating the database, we display the response in the HTML document.

### JavaScript

```javascript
// ...

response.json({ message: "success!", data: newDb });
```

## Conclusion

By following these steps, we've completed our web application's creation of databases and display of API responses. This project demonstrates the capabilities of Notion's API and how they can be integrated into a web application.
```

# Creating a Database in Notion Using an Express Server

This guide demonstrates how to create a simple web application using Node.js and Express.js that exposes an API endpoint. The API endpoint provides a way to create a new database in Notion.

## Table of Contents

*   [Integration overview](#integration-overview)
*   [Today’s goals](#todays-goals)
    *   [Requirements](#requirements)
*   [Getting started](#getting-started)
    *   [Create your integration in Notion](#create-your-integration-in-notion)
    *   [Get your API secret](#get-your-api-secret)
    *   [Give your integration page permissions](#give-your-integration-page-permissions)
*   [Setting up the demo locally](#setting-up-the-demo-locally)
    *   [Clone demo repo](#clone-demo-repo)
    *   [Environment variables](#environment-variables)
    *   [Running the project locally](#running-the-project-locally)
*   [Creating a new database](#creating-a-new-database)
    *   [Step 1: Adding a database form (`index.html`)](#step-1-adding-a-database-form-indexhtml)
    *   [Step 2: Handling the form submission (`client.js`)](#step-2-handling-the-form-submission--clientjs)
    *   [Step 3: Importing the Notion SDK (`server.ts`)](#step-3-importing-the-notion-sdk-serverts)
    *   [Step 4: Handling the form’s POST request (`server.ts`)](#step-4-handling-the-forms-post-request-serverts)
    *   [Step 5: Displaying the response (`index.html`)](#step-5-displaying-the-response-indexhtml)
*   [Testing the feature](#testing-the-feature)
*   [Wrapping up](#wrapping-up)
*   [Next steps](#next-steps)
    *   [Additional resources](#additional-resources)

## Integration overview

The integration provides a way to create a new database in Notion using a RESTful POST request. The request includes the following fields:

| Field | Description |
|-------|-------------|
| `name` | Name of the database |
| `description` | Description of the database |
| `visibility` | Visibility level of the database (public, private, or invite-only) |
| `template_id` | Template ID of the database |
| `parent_id` | Parent database ID (for hierarchical organization) |
| `notion_url` | URL of the Notion page associated with the database |

## Today’s goals

### Requirements

1.  **Database creation**: Create a new database with the specified fields.
2.  **Permission management**: Give the integration page permission to create databases.

## Getting started

### Create your integration in Notion

1.  Go to the **Settings** > **Integrations**.
2.  Click **Add Integration**.
3.  Select **Express Server** and click **Add**.
4.  Enter a name for your integration.

### Get your API secret

1.  Go to the **Settings** > **API Keys**.
2.  Click **Secrets**.
3.  Copy your API secret.

### Give your integration page permissions

1.  Go to the **Settings** > **Pages**.
2.  Click **Permissions**.
3.  Scroll down to **Add a page…**.
4.  Select your integration and check the box to give it permission to create databases.

## Setting up the demo locally

### Clone demo repo

1.  Clone the demo repository using the command line:
    ```bash
    git clone https://github.com/makenotion/notion-app.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd notion-app
    ```

### Environment variables

1.  Create a `.env` file in the root directory of the project.
2.  Add the following environment variables:
    ```
    # Set your API secret
    NOTION_API_SECRET=your_secret_here
    # Set your Notion workspace ID
    NOTION_WORKSPACE_ID=your_workspace_id
    # Set your Notion database template ID
    NOTION_DATABASE_TEMPLATE_ID=your_template_id
    # Set your Notion workspace currency
    NOTION_WORKSPACE_CURRENCY=USD
    # Set your Notion workspace locale
    NOTION_WORKSPACE_LOCALE=en_US
    # Set your Notion workspace time zone
    NOTION_WORKSPACE_TIME_ZONE=UTC
    ```

### Running the project locally

1.  Install Node.js and npm:
    ```bash
    npx install -g node@latest npm
    ```
2.  Start the Express server:
    ```bash
    npm run start
    ```
3.  Open a web browser and navigate to http://localhost:3000 to view the application.

## Creating a new database

### Step 1: Adding a database form (`index.html`)

```html
<html lang="en-US" dir="ltr"><head>
    
    
    <title>Create a database | Notion Developer Docs</title>
    
    
    
    
    
    
    
    
    
    
    
  </head>
  <body>
    <div id="app"><div class="Layout" data-v-5d98c3a5=""><span tabindex="-1" data-v-0f60ec36=""></span><a href="#VPContent" class="VPSkipLink visually-hidden" data-v-0f60ec36=""> Skip to content </a><header class="VPNav" data-v-5d98c3a5="" data-v-ae24b3ad=""><div class="VPNavBar has-sidebar top" data-v-ae24b3ad="" data-v-ccf7ddec=""><div class="wrapper" data-v-ccf7ddec=""><div class="container" data-v-ccf7ddec=""><div class="title" data-v-ccf7ddec=""><div class="VPNavBarTitle has-sidebar" data-v-ccf7ddec="" data-v-ab179fa1=""><a class="title" href="/" data-v-ab179fa1=""><img class="VPImage logo" src="/images/logo.png" alt="" data-v-8426fc1a=""><span data-v-ab179fa1="">Docs</span></a></div></div><div class="content" data-v-ccf7ddec=""><div class="content-body" data-v-ccf7ddec=""><div class="VPNavBarSearch search" data-v-ccf7ddec=""><div id="docsearch"><button type="button" class="DocSearch DocSearch-Button" aria-label="Search"><span class="DocSearch-Button-Container"><span class="vp-icon DocSearch-Search-Icon"></span><span class="DocSearch-Button-Placeholder">Search</span></span><span class="DocSearch-Button-Keys"><kbd class="DocSearch-Button-Key"></kbd><kbd class="DocSearch-Button-Key">K</kbd></span></button></div></div><nav aria-labelledby="main-nav-aria-label" class="VPNavBarMenu menu" data-v-ccf7ddec="" data-v-7f418b0f=""><span id="main-nav-aria-label" class="visually-hidden" data-v-7f418b0f="">Main Navigation</span><a class="VPLink link VPNavBarMenuLink" href="/" tabindex="0" data-v-7f418b0f="" data-v-9c663999=""><span data-v-9c663999="">Welcome</span></a><a class="VPLink link VPNavBarMenuLink active" href="/guide/introduction" tabindex="0" data-v-7f418b0f="" data-v-9c663999=""><span data-v-9c663999="">Guide</span></a><a class="VPLink link VPNavBarMenuLink" href="/reference/introduction" tabindex="0" data-v-7f418b0f="" data-v-9c663999=""><span data-v-9c663999="">Reference</span></a><a class="VPLink link VPNavBarMenuLink" href="/faq" tabindex="0" data-v-7f418b0f="" data-v-9c663999=""><span data-v-9c663999="">FAQ</span></a><a class="VPLink link VPNavBarMenuLink" href="/help" tabindex="0" data-v-7f418b0f="" data-v-9c663999=""><span data-v-9c663999="">Help</span></a></nav><div class="VPNavBarAppearance appearance" data-v-ccf7ddec="" data-v-e6aabb21=""><button class="VPSwitch VPSwitchAppearance" type="button" role="switch" title="Switch to dark theme" aria-checked="false" data-v-e6aabb21="" data-v-d1f28634="" data-v-1d5665e3=""><span class="check" data-v-1d5665e3=""><span class="icon" data-v-1d5665e3=""><span class="vpi-sun sun" data-v-d1f28634=""></span><span class="vpi-moon moon" data-v-d1f28634=""></span></span></span></button></div><div class="VPSocialLinks VPNavBarSocialLinks social-links" data-v-ccf7ddec="" data-v-0394ad82="" data-v-7bc22406=""><a class="VPSocialLink no-icon" href="https://github.com/makenotion/notion-app" aria-label="github" target="_blank" rel="noopener" data-v-7bc22406="" data-v-f80f8133=""></a><a class="VPSocialLink no-icon" href="https://discord.gg/nQn7BWM6E4" aria-label="discord" target="_blank" rel="noopener" data-v-7bc22406="" data-v-f80f8133=""></a><a class="VPSocialLink no-icon" href="https://twitter.com/MakeNotionDev" aria-label="twitter" target="_blank" rel="noopener" data-v-7bc22406="" data-v-f80f8133=""></a><a class="VPSocialLink no-icon" href="https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg" aria-label="slack" target="_blank" rel="noopener" data-v-7bc22406="" data-v-f80f8133=""></a></div><div class="VPFlyout VPNavBarExtra extra" data-v-ccf7ddec="" data-v-d0bd9dde="" data-v-b6c34ac9=""><button type="button" class="button" aria-haspopup="true" aria-expanded="false" aria-label="extra navigation" data-v-b6c34ac9=""><span class="vpi-more-horizontal icon" data-v-b6c34ac9=""></span></button><div class="menu" data-v-b6c34ac9=""><div class="VPMenu" data-v-b6c34ac9="" data-v-e7ea1737=""><div class="group" data-v-d0bd9dde=""><div class="item appearance" data-v-d0bd9dde=""><p class="label" data-v-d0bd9dde="">Appearance</p><div class="appearance-action" data-v-d0bd9dde=""><button class="VPSwitch VPSwitchAppearance" type="button" role="switch" title="Switch to dark theme" aria-checked="false" data-v-d0bd9dde="" data-v-d1f28634="" data-v-1d5665e3=""><span class="check" data-v-1d5665e3=""><span class="icon" data-v-1d5665e3=""><span class="vpi-sun sun" data-v-d1f28634=""></span><span class="vpi-moon moon" data-v-d1f28634=""></span></span></span></button></div></div></div><div class="group" data-v-d0bd9dde=""><div class="item social-links" data-v-d0bd9dde=""><div class="VPSocialLinks social-links-list" data-v-d0bd9dde="" data-v-7bc22406=""><a class="VPSocialLink no-icon" href="https://github.com/makenotion/notion-app" aria-label="github" target="_blank" rel="noopener" data-v-7bc22406="" data-v-f80f8133=""></a><a class="VPSocialLink no-icon" href="https://discord.gg/nQn7BWM6E4" aria-label="discord" target="_blank" rel="noopener" data-v-7bc22406="" data-v-f80f8133=""></a><a class="VPSocialLink no-icon" href="https://twitter.com/MakeNotionDev" aria-label="twitter" target="_blank" rel="noopener" data-v-7bc22406="" data-v-f80f8133=""></a><a class="VPSocialLink no-icon" href="https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg" aria-label="slack" target="_blank" rel="noopener" data-v-7bc22406="" data-v-f80f8133=""></a></div></div></div></div></div></div><button type="button" class="VPNavBarHamburger hamburger" aria-label="mobile navigation" aria-expanded="false" aria-controls="VPNavScreen" data-v-ccf7ddec="" data-v-e5dd9c1c=""><span class="container" data-v-e5dd9c1c=""><span class="top" data-v-e5dd9c1c=""></span><span class="middle" data-v-e5dd9c1c=""></span><span class="bottom" data-v-e5dd9c1c=""></span></span></button></div></div></div></div><div class="divider" data-v-ccf7ddec=""><div class="divider-line" data-v-ccf7ddec=""></div></div></div></header><div class="VPLocalNav has-sidebar" data-v-5d98c3a5="" data-v-a6f0e41e=""><div class="container" data-v-a6f0e41e=""><button class="menu" aria-expanded="false" aria-controls="VPSidebarNav" data-v-a6f0e41e=""><span class="vpi-align-left menu-icon" data-v-a6f0e41e=""></span><span class="menu-text" data-v-a6f0e41e="">Menu</span></button><div class="VPLocalNavOutlineDropdown" style="--vp-vh: 0px;" data-v-a6f0e41e="" data-v-17a5e62e=""><button data-v-17a5e62e="" class=""><span data-v-17a5e62e="" class="menu-text">On this page</span><span data-v-17a5e62e="" class="vpi-chevron-right icon"></span></button></div></div></div><aside class="VPSidebar" data-v-5d98c3a5="" data-v-575e6a36=""><div class="curtain" data-v-575e6a36=""></div><nav class="nav" id="VPSidebarNav" aria-labelledby="sidebar-aria-label" tabindex="-1" data-v-575e6a36=""><span class="visually-hidden" id="sidebar-aria-label" data-v-575e6a36=""> Sidebar Navigation </span><div class="group" data-v-575e6a36=""><section class="VPSidebarItem level-0 collapsible has-active" data-v-575e6a36="" data-v-b8d55f3b=""><div class="item" role="button" tabindex="0" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><h2 class="text" data-v-b8d55f3b="">Introduction</h2><div class="caret" role="button" aria-label="toggle section" tabindex="0" data-v-b8d55f3b=""><span class="vpi-chevron-right caret-icon" data-v-b8d55f3b=""></span></div></div><div class="items" data-v-b8d55f3b=""><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/introduction" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Overview</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/login" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Login</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/database" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Database</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/documents" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Documents</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/comments" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Comments</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/forms" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Forms</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/user-groups" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">User groups</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/collaboration" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Collaboration</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/authentication" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Authentication</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/permissions" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Permissions</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/workspaces" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Workspaces</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/teams" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Teams</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/projects" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Projects</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/tasks" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Tasks</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/pages" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Pages</p></a></div></div><div class="VPSidebarItem level-1 is-link is-active has-active" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/databases" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Databases</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/media" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Media</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/social-media" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Social media</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/external-data" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">External data</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/embedded-docs" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Embedded docs</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/voice-notes" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Voice notes</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/sync" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Sync</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/troubleshooting" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">Troubleshooting</p></a></div></div><div class="VPSidebarItem level-1 is-link" data-v-b8d55f3b=""><div class="item" data-v-b8d55f3b=""><div class="indicator" data-v-b8d55f3b=""></div><a class="VPLink link link" href="/guide/faq" data-v-b8d55f3b=""><p class="text" data-v-b8d55f3b="">FAQ</p></a></div></div></div></section></div></nav></aside><div class="VPContent has-sidebar" id="VPContent" data-v-5d98c3a5="" data-v-1428d186=""><div class="VPDoc has-sidebar has-aside" data-v-1428d186="" data-v-39a288b8=""><div class="container" data-v-39a288b8=""><div class="aside" data-v-39a288b8=""><div class="aside-curtain" data-v-39a288b8=""></div><div class="aside-container" data-v-39a288b8=""><div class="aside-content" data-v-39a288b8=""><div class="VPDocAside" data-v-39a288b8="" data-v-3f215769=""><div class="VPDocAsideOutline has-outline" role="navigation" data-v-3f215769="" data-v-935f8a84=""><div class="content" data-v-935f8a84=""><div class="outline-marker" data-v-935f8a84="" style="top: 33px; opacity: 0;"></div><div class="outline-title" role="heading" aria-level="2" data-v-935f8a84="">On this page</div><nav aria-labelledby="doc-outline-aria-label" data-v-935f8a84=""><span class="visually-hidden" id="doc-outline-aria-label" data-v-935f8a84=""> Table of Contents for current page </span><ul class="root" data-v-935f8a84="" data-v-d0ce1cdc=""><li data-v-d0ce1cdc=""><a data-v-d0ce1cdc="" class="outline-link" href="#creating-a-new-database" title="Creating a new database">Creating a new database</a></li><li data-v-d0ce1cdc=""><a data-v-d0ce1cdc="" class="outline-link" href="#step-1-adding-a-database-form-indexhtml" title="Step 1: Adding a database form (&quot;index.html&quot;)">Step 1: Adding a database form ("index.html")</a></li><li data-v-d0ce1cdc=""><a data-v-d0ce1cdc="" class="outline-link" href="#step-2-handling-the-form-submission--clientjs" title="Step 2: Handling the form submission  (&quot;client.js&quot;)">Step 2: Handling the form submission  ("client.js")</a></li><li data-v-d0ce1cdc=""><a data-v-d0ce1cdc="" class="outline-link" href="#step-3-importing-the-notion-sdk-serverts" title="Step 3: Importing the Notion SDK (&quot;server.ts&quot;)">Step 3: Importing the Notion SDK ("server.ts")</a></li><li data-v-d0ce1cdc=""><a data-v-d0ce1cdc="" class="outline-link" href="#step-4-handling-the-forms-post-request-serverts" title="Step 4: Handling the form’s POST request (&quot;server.ts&quot;)">Step 4: Handling the form’s POST request ("server.ts")</a></li><li data-v-d0ce1cdc=""><a data-v-d0ce1cdc="" class="outline-link" href="#step-5-displaying-the-response-indexhtml" title="Step 5: Displaying the response (&quot;index.html&quot;)">Step 5: Displaying the response ("index.html")</a></li></ul></nav></div></div><div class="spacer" data-v-3f215769=""></div></div></div></div></div><div class="content" data-v-39a288b8=""><div class="content-container" data-v-39a288b8=""><main class="main" data-v-39a288b8=""><div style="position:relative;" class="vp-doc _guide_databases" data-v-39a288b8=""><div><h1 id="creating-a-database" tabindex="-1">Creating a database <a class="header-anchor" href="#creating-a-database" aria-label="Permalink to &quot;Creating a database&quot;">​</a></h1><p>Use the <code>/database</code> endpoint to create a new database in Notion.</p><p>For example, the following JSON would create a database named "My New Database".</p><div class="language-json vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">json</span><pre class="shiki shiki-themes github-light github-dark vp-code"><code><span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">{</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">  "name"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">"My New Database"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">,</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">  "description"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">"This is my new database."</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">,</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">  "visibility"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">"public"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">,</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">  "template_id"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">"1f0000000000000"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">,</span></span>
<span class="line"><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">  "parent_id"</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark