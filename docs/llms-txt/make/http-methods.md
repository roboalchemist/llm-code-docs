# Source: https://developers.make.com/api-documentation/getting-started/http-methods.md

# HTTP methods

Make API uses standard HTTP methods to interact with endpoints. The following table lists the available HTTP methods and shows examples of endpoints these methods can be used with.

| **HTTP method**                           | **Description**                                                                                                                                                                                                                                                                         |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <mark style="color:green;">`GET`</mark>   | <p>Retrieves a resource representation without modifying it.</p><p><em>Example:</em><br><a href="broken-reference"><code>/scenarios</code></a><br><em>returns all available Make scenarios</em></p>                                                                                     |
| <mark style="color:orange;">`POST`</mark> | <p>Creates a resource.</p><p><em>Example:</em><br><a href="broken-reference"><code>/scenarios</code></a><br><em>creates a scenario</em></p>                                                                                                                                             |
| <mark style="color:blue;">`PUT`</mark>    | <p>Updates a resource. If the resource does not exist yet, this method creates it.</p><p><em>Example:</em><br><a href="broken-reference"><code>/scenarios/{scenarioId}/custom-properties</code></a><br><em>sets custom properties data for a scenario with the specified ID</em></p>    |
| `PATCH`                                   | <p>Makes a partial update on a resource. Does not replace the entire resource.</p><p><em>Example:</em><br><a href="broken-reference"><code>/scenarios/{scenarioId}</code></a><br><em>updates properties (for example, scheduling or blueprint) of the scenario with a given ID</em></p> |
| <mark style="color:red;">`DELETE`</mark>  | <p>Removes a resource.</p><p><em>Example:</em><br><a href="broken-reference"><code>/scenarios/{scenarioId}</code></a><br><em>deletes the scenario with a given ID</em></p>                                                                                                              |
