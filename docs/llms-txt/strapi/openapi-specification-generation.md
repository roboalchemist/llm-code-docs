# OpenAPI specification generation

Strapi provides a command-line tool to generate 

</Tabs>

You can also path an optional `--output` argument to specify the path and filename, as in the following example:

</Tabs>

### Specification structure and content

The generated OpenAPI specification follows the 

<div class="mermaid-download-link">
  <small>
    <i class="strapi-icons ph-fill ph-download" style={{color: "inherit;"}}></i>
    <a href="/example-openapi-spec.json"download="" target="_blank" title="Click to download a complete OpenAPI 3.1.0 specification file generated with example data extracted from a freshly installed Strapi project">Download an example of a complete specification file</a>
  </small>
</div>

<br/>

The generated OpenAPI specification includes all available API endpoints in your Strapi application, and information about these endpoints, such as the following:

- CRUD operations for all content types
- Custom API routes defined in your application
- Authentication endpoints for user management
- File upload endpoints for media handling
- Plugin endpoints from installed plugins

## Integrating with Swagger UI

With the following steps you can quickly generate a [Swagger UI](https://swagger.io/)-compatible page:

1. Generate a specification:

    </Tabs>

2. Update [the `/config/middlewares.js` configuration file](/cms/configurations/middlewares) with the following code:

    </Tabs>

    This will ensure the Swagger UI display from  is not blocked by Strapi's CSP policy handled by the [security middleware](/cms/configurations/middlewares#security).

3. Create a `public/openapi.html` file in your Strapi project to display the Swagger UI, with the following code:

    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <title>API Documentation</title>
        <link
          rel="stylesheet"
          type="text/css"
          href="https://unpkg.com/swagger-ui-dist@5.0.0/swagger-ui.css"
        />
      </head>
      <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@5.0.0/swagger-ui-bundle.js"></script>
        <script src="https://unpkg.com/swagger-ui-dist@5.0.0/swagger-ui-standalone-preset.js"></script>
        <script>
          window.onload = function () {
            SwaggerUIBundle({
              url: './swagger-spec.json',
              dom_id: '#swagger-ui',
              presets: [
                SwaggerUIBundle.presets.apis,
                SwaggerUIStandalonePreset
              ],
              layout: 'StandaloneLayout',
            });
          };
        </script>
      </body>
    </html>
    ```

4. Restart the Strapi server with `yarn develop` or `npm run develop` and visit the `/openapi.html` page. The Swagger UI should be displayed:

    ![Swagger UI example with Strapi OpenAPI specification](/img/assets/apis/swagger-open-api.png)