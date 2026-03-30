# with pnpm
pnpm add express
```

Then, add the following code in a `server.js` file:

```js theme={null}
// server.js

import express from 'express'
import { createTenantToken } from './search.js'

const server = express()

server.get('/token', async (request, response) => {
  const { id: patientId } = request.query
  const token = createTenantToken(patientId)
  return response.json({ token });
})

server.listen(3000, () => {
  console.log('Server is running on port 3000')
})
```

This code creates an endpoint at `http://localhost:3000/token` that accepts an `id` query parameter and returns a tenant token.

### Making a search

Now that we have an endpoint, you will use it to retrieve the tenant token in your front-end application. This guide uses [InstantSearch.js](/guides/front_end/front_end_integration) to create a search interface. You will use CDN links to include InstantSearch.js and the Meilisearch InstantSearch.js connector in your HTML file.

Create `client.html` file and insert this code:

```html theme={null}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@meilisearch/instant-meilisearch/templates/basic_search.css" />
  </head>
  <body>
    <div class="wrapper">
      <div id="searchbox" focus></div>
      <div id="hits"></div>
    </div>
  </body>
  <script src="https://cdn.jsdelivr.net/npm/@meilisearch/instant-meilisearch/dist/instant-meilisearch.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4"></script>
  <script>
    document.addEventListener('DOMContentLoaded', async () => {
      const patientId = 1 // Replace with the patient's ID
      const response = await fetch(`http://localhost:3000/token?id=${patientId}`)
      const { token } = await response.json()

      const search = instantsearch({
        indexName: 'appointments',
        searchClient: instantMeiliSearch(
          'https://edge.meilisearch.com',
          token
        ).searchClient
      })

      search.addWidgets([
        instantsearch.widgets.searchBox({
          container: "#searchbox"
        }),
        instantsearch.widgets.hits({
          container: "#hits",
          templates: {
          item: `
            <div>
              <div class="hit-name">
                    {{#helpers.highlight}}{ "attribute": "patient" }{{/helpers.highlight}}
              </div>
              <div class="hit-description">
                {{#helpers.highlight}}{ "attribute": "details" }{{/helpers.highlight}}
              </div>
            </div>
          `
          }
        })
      ])

      search.start()
    })
  </script>
</html>
```

Ta-da! You have successfully implemented a secure, multitenant search in your Node.js application. Users will only be able to search for documents that belong to them.

## Conclusion

In this guide, you saw how to implement secure, multitenant search in a Node.js application. You then created an endpoint to generate tenant tokens for each user. You also built a search interface with InstantSearch to make searches using the tenant token.

All the code in this guide is a taken from our [multitenacy example](https://tenant-token.meilisearch.com/?utm_campaign=oss\&utm_source=docs\&utm_medium=node-multitenancy) application. The code is available on [GitHub](https://github.com/meilisearch/tutorials/tree/main/src/tenant-token-tutorial).