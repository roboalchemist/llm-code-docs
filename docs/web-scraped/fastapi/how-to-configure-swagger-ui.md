# Source: https://fastapi.tiangolo.com/how-to/configure-swagger-ui/

# Configure Swagger UI[&para;](#configure-swagger-ui)

You can configure some extra [Swagger UI parameters](https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/).

To configure them, pass the `swagger_ui_parameters` argument when creating the `FastAPI()` app object or to the `get_swagger_ui_html()` function.

`swagger_ui_parameters` receives a dictionary with the configurations passed to Swagger UI directly.

FastAPI converts the configurations to **JSON** to make them compatible with JavaScript, as that's what Swagger UI needs.

## Disable Syntax Highlighting[&para;](#disable-syntax-highlighting)

For example, you could disable syntax highlighting in Swagger UI.

Without changing the settings, syntax highlighting is enabled by default:

But you can disable it by setting `syntaxHighlight` to `False`:

Python 3.9+

...and then Swagger UI won't show the syntax highlighting anymore:

## Change the Theme[&para;](#change-the-theme)

The same way you could set the syntax highlighting theme with the key `"syntaxHighlight.theme"` (notice that it has a dot in the middle):

Python 3.9+

That configuration would change the syntax highlighting color theme:

## Change Default Swagger UI Parameters[&para;](#change-default-swagger-ui-parameters)

FastAPI includes some default configuration parameters appropriate for most of the use cases.

It includes these default configurations:

Python 3.8+

👀 Full file preview

Python 3.8+

You can override any of them by setting a different value in the argument `swagger_ui_parameters`.

For example, to disable `deepLinking` you could pass these settings to `swagger_ui_parameters`:

Python 3.9+

## Other Swagger UI Parameters[&para;](#other-swagger-ui-parameters)

To see all the other possible configurations you can use, read the official [docs for Swagger UI parameters](https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/).

## JavaScript-only settings[&para;](#javascript-only-settings)

Swagger UI also allows other configurations to be **JavaScript-only** objects (for example, JavaScript functions).

FastAPI also includes these JavaScript-only `presets` settings:

`presets: [
    SwaggerUIBundle.presets.apis,
    SwaggerUIBundle.SwaggerUIStandalonePreset
]
`

These are **JavaScript** objects, not strings, so you can't pass them from Python code directly.

If you need to use JavaScript-only configurations like those, you can use one of the methods above. Override all the Swagger UI *path operation* and manually write any JavaScript you need.