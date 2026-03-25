# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/creating-the-pentaho-web-package-visapi-custom-visualization-creation.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/creating-the-pentaho-web-package-visapi-custom-visualization-creation.md

# Create the Pentaho web package

In [Develop a visualization in a sandbox](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/walk-through-tutorial-cp-visapi), you developed a custom visualization and tested it in a controlled sandbox environment.

Excluding the sandbox-specific files, you can package the following files and the `css` folder:

* `package.json`
* `Model.js`
* `View.js`
* `clickD3.js`
* `config.js`

Any runtime client-side dependencies must also be provided to the platform. In the case of this tutorial, the only runtime dependency is the D3 library. The `@pentaho/visual-sandbox` is a development-time dependency. Dependencies can be provided separately in their own package or bundled together with your visualization. For packaging the tutorial visualization, you just need to ZIP your files and runtime dependencies. Do not include temporary files and development-time dependencies.

By using the `npm pack` command, you can ensure only your files and bundled dependencies are compressed in the resulting TGZ file, as shown in the following example:

```
# Package your files.
npm pack
```

With the web package in place, you can now deploy it. See [Deploying a visualization](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/deploying-a-visualization-cp-visapi) for further instructions.
