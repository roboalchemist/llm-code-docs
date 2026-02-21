# Source: https://docs.wiremock.io/dynamic-state/create-stateful-set.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Stateful Endpoint Set

> Assisted Creation of Stateful Mock APIs

The **Create Stateful Endpoint Set** feature in WireMock Cloud automates the creation of pre-configured stateful stubs. This allows for quick setup of RESTful API mocks with built-in request-response handling and state management across multiple HTTP methods.

Using this feature, WireMock Cloud automatically generates:

* **GET, POST, PUT, and DELETE** stubs for the specified resource
* A **default 404 response** for unmatched requests

This feature requires the **REST mock API template**.  It is not available in the Unstructured / Blank mock API template.

## How It Works

You provide:

1. Create a new **REST mock API**

2. Click the **Stateful Set** button near the bottom of the stub list:

   <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-button.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=bdb444a4900e081d9faa1a4b7903a416" alt="Stateful set button" data-og-width="284" width="284" data-og-height="112" height="112" data-path="images/dynamic-state/stateful-set-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-button.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d389c4b02fa737ff0fdeb85431352b4c 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-button.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=489169c41792cf6861c40a2fe2ac5251 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-button.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=566e5bdf490344ce35e1202757c3f7b7 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-button.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=bb121c5b7edc21f5b00fd5b1af806527 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-button.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=cbd77bc77f43c682ab98768905d44daa 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-button.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f2478e96479b53f07f1f0859b00ecb50 2500w" />

3. Supply a **POST endpoint page** (e.g., `/users`):

   <img src="https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-post-endpoint.png?fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=6570667c041646b57ad381620c53183e" alt="Stateful set post endpoint" data-og-width="751" width="751" data-og-height="847" height="847" data-path="images/dynamic-state/stateful-set-post-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-post-endpoint.png?w=280&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=10b0ef660e6cc3968e3792058cdecf69 280w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-post-endpoint.png?w=560&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=83fe61fa684847174d59caf96a48ed1c 560w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-post-endpoint.png?w=840&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=43a994f38b462ce35b070476b110a943 840w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-post-endpoint.png?w=1100&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=d285ac4f1123b60a83d63b6ecd82d4c9 1100w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-post-endpoint.png?w=1650&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=9cb44329c3430a0d8d0606da468eded1 1650w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-post-endpoint.png?w=2500&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=f87d0d6ac62b0fcec1b7760d4739e345 2500w" />

4. Provide a **sample request body** for the `POST`
   e.g.:

   ```json  theme={null}
   {
       "firstName": "Betty",
       "lastName": "Boop",
       "organization": "Finance"
   }
   ```

   <img src="https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-request-body.png?fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=bc93e618c80ec2ea7984833b1cfd3493" alt="Stateful set request body" data-og-width="746" width="746" data-og-height="844" height="844" data-path="images/dynamic-state/stateful-set-request-body.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-request-body.png?w=280&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=775b2b0a6d954619c8db8f788889da40 280w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-request-body.png?w=560&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=c84786d36d1c69ece3660003df4cd6bd 560w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-request-body.png?w=840&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=25f18ab02ebe512b8f5c130baf3b61b7 840w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-request-body.png?w=1100&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=902a58994229609bd3d22a8cec1b88e7 1100w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-request-body.png?w=1650&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=af322209eb950d1bda3477e86bc787be 1650w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-request-body.png?w=2500&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=48b85b4e25f94f2ccfab5923ca53eccf 2500w" />

5. Input a **correlated sample response body** for the given request body
   e.g.:

   ```json  theme={null}
   {
       "contactId": "4",
       "firstName": "Betty",
       "lastName": "Boop",
       "organization": "Finance",
       "created_utc": "2025-02-28T15:58:35Z"
   }
   ```

   <img src="https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-response-body.png?fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=116c320dce89308d8a2477f09630253c" alt="Stateful set response body" data-og-width="743" width="743" data-og-height="842" height="842" data-path="images/dynamic-state/stateful-set-response-body.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-response-body.png?w=280&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=e0182ff92607cf9c1befc4389a2bc78c 280w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-response-body.png?w=560&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=03078e664d6b12a3077bc82fb6de2afd 560w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-response-body.png?w=840&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=8262c31cdddd588cb5bbf1f851d9dbf1 840w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-response-body.png?w=1100&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=d508daa3d390965e275880ab366f7d1d 1100w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-response-body.png?w=1650&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=6a274d99578a216874077207c45354ea 1650w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-response-body.png?w=2500&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=886b3d5e62542daa2f5d11d5744bccb8 2500w" />

6. At the bottom of the dialog, select which operations you'd like stubs to be created for:

   <img src="https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-select-operations.png?fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=6341e315ef848b13183bcdb9f5908d38" alt="Stateful set target operation selection" data-og-width="743" width="743" data-og-height="508" height="508" data-path="images/dynamic-state/stateful-set-select-operations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-select-operations.png?w=280&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=799b2c7c7ad78fcb2944dc9055cb316e 280w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-select-operations.png?w=560&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=766d46c80e92a0ce53d98a909180539d 560w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-select-operations.png?w=840&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=2cd56384d9c26f0001e69f95a790a58c 840w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-select-operations.png?w=1100&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=46a98511a486e4ccd3c144bd730f4817 1100w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-select-operations.png?w=1650&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=30a1e06643de0911eae80b9511fd0f98 1650w, https://mintcdn.com/wiremockinc/-wllCbfV1T1IIu-9/images/dynamic-state/stateful-set-select-operations.png?w=2500&fit=max&auto=format&n=-wllCbfV1T1IIu-9&q=85&s=872c43f0884cc90dac1e0e77f5608461 2500w" />

7. Click the **Create Stateful set** button:

   <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-create-button.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=5d953dda682ca12d446938cfba917f46" alt="Create Stateful set button" data-og-width="201" width="201" data-og-height="58" height="58" data-path="images/dynamic-state/stateful-set-create-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-create-button.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ab1665310cab591bc8460c092cc0916c 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-create-button.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=9414c01d475787dd70744857e5224427 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-create-button.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=3dcd4c2b1bb21b35bce85f6af4752198 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-create-button.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d2cd2adfbc5a0f8afe1894f84e2c1bb6 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-create-button.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=5a2b360fd9e490d3a37b3b26d1d36d93 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/dynamic-state/stateful-set-create-button.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=7f583e9ba8b75dd482fc3179bd1e2547 2500w" />

New stubs will be created that are automatically configured with stateful functionality.

* A **POST** stub that creates a new resource in the mock API's stateful memory
* A **GET** stub that lists all of the resources stored in the mock API's stateful memory
* A **GET** stub that retrieves a stored resource by its identifier
* A **PUT** stub that updates the stored data of a resource
* A **DELETE** stub that removes the stored resource
* A **DELETE** stub that removes all stored resources from the mock API's stateful memory
* A fallback **404 response** for unknown requests

You will want to further modify the stubs to better simulate the API's real-world stateful behavior.
