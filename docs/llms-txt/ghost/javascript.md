# Source: https://docs.ghost.org/content-api/javascript.md

# Source: https://docs.ghost.org/admin-api/javascript.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Admin API JavaScript Client

> Admin API keys should remain secret, and therefore this promise-based JavaScript library is designed for server-side usage only. This library handles all the details of generating correctly formed urls and tokens, authenticating and making requests.

***

## Working Example

```js  theme={"dark"}
const api = new GhostAdminAPI({
  url: 'http://localhost:2368',
  key: 'YOUR_ADMIN_API_KEY',
  version: "v6.0",
});

api.posts.add({
    title: 'My first draft API post',
    lexical: '{"root":{"children":[{"children":[{"detail":0,"format":0,"mode":"normal","style":"","text":"Hello, beautiful world! 👋","type":"extended-text","version":1}],"direction":"ltr","format":"","indent":0,"type":"paragraph","version":1}],"direction":"ltr","format":"","indent":0,"type":"root","version":1}}'
});
```

## Authentication

The client requires the host address of your Ghost API and an Admin API key in order to authenticate.

* `url` - API domain, must not end in a trailing slash.
* `key` - string copied from the “Integrations” screen in Ghost Admin
* `version` - minimum version of the API your code works with

The `url` and `key` values can be obtained by creating a new `Custom Integration` under the Integrations screen in Ghost Admin.

<Frame>
  <img src="https://mintcdn.com/ghost/KePyCzI5-bxtjueF/images/custom-integration-settings.webp?fit=max&auto=format&n=KePyCzI5-bxtjueF&q=85&s=cda4a350d118c74c36bb9306cd7ddbbd" width="1400" height="1097" data-path="images/custom-integration-settings.webp" />
</Frame>

See the documentation on [Admin API authentication](/admin-api/#authentication) for more explanation.

## Endpoints

All endpoints & parameters provided to integrations by the [Admin API](/admin-api/) are supported.

```js  theme={"dark"}
// [Stability: stable]

// Browsing posts returns Promise([Post...]);
// The resolved array will have a meta property
api.posts.browse();
api.posts.read({id: 'abcd1234'});
api.posts.add({title: 'My first API post'});
api.posts.edit({id: 'abcd1234', title: 'Renamed my post', updated_at: post.updated_at});
api.posts.delete({id: 'abcd1234'});

// Browsing pages returns Promise([Page...])
// The resolved array will have a meta property
api.pages.browse({limit: 2});
api.pages.read({id: 'abcd1234'});
api.pages.add({title: 'My first API page'})
api.pages.edit({id: 'abcd1234', title: 'Renamed my page', updated_at: page.updated_at})
api.pages.delete({id: 'abcd1234'});

// Uploading images returns Promise([Image...])
api.images.upload({file: '/path/to/local/file'});
```

## Publishing Example

A bare minimum example of how to create a post from HTML content, including extracting and uploading images first.

```js  theme={"dark"}
const GhostAdminAPI = require('@tryghost/admin-api');
const path = require('path');

// Your API config
const api = new GhostAdminAPI({
    url: 'http://localhost:2368',
    version: "v6.0",
    key: 'YOUR_ADMIN_API_KEY'
});

// Utility function to find and upload any images in an HTML string
function processImagesInHTML(html) {
    // Find images that Ghost Upload supports
    let imageRegex = /="([^"]*?(?:\.jpg|\.jpeg|\.gif|\.png|\.svg|\.sgvz))"/gmi;
    let imagePromises = [];

    while((result = imageRegex.exec(html)) !== null) {
        let file = result[1];
            // Upload the image, using the original matched filename as a reference
            imagePromises.push(api.images.upload({
                ref: file,
                file: path.resolve(file)
            }));
    }

    return Promise
        .all(imagePromises)
        .then(images => {
            images.forEach(image => html = html.replace(image.ref, image.url));
            return html;
        });
}

// Your content
let html = '<p>My test post content.</p><figure><img src="/path/to/my/image.jpg" /><figcaption>My awesome photo</figcaption></figure>';

return processImagesInHTML(html)
    .then(html => {
        return api.posts
            .add(
                {title: 'My Test Post', html},
                {source: 'html'} // Tell the API to use HTML as the content source, instead of Lexical
            )
            .then(res => console.log(JSON.stringify(res)))
            .catch(err => console.log(err));

    })
    .catch(err => console.log(err));
```

## Installation

`yarn add @tryghost/admin-api`

`npm install @tryghost/admin-api`

### Usage

ES modules:

```js  theme={"dark"}
import GhostAdminAPI from '@tryghost/admin-api'
```

Node.js:

```js  theme={"dark"}
const GhostAdminAPI = require('@tryghost/admin-api');
```


Built with [Mintlify](https://mintlify.com).