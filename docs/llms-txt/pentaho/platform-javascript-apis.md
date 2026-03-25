# Source: https://docs.pentaho.com/pdia-admin/administer/platform-javascript-apis.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/pentaho-developer-center-overview-cp/platform-javascript-apis.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis.md

# Platform JavaScript APIs

You can develop your own JavaScript components for Pentaho using our Platform JavaScript APIs. These APIs standardize across the Pentaho platform in such areas as data and visualization, but also on lower-level areas, such as configuration, localization and services. It also shares key platform information and services with JavaScript components.

The APIs are organized into the following groups:

* **Visualization**

  A unified way to visualize data across the Pentaho suite.
* **Data**

  Abstractions for data exchange among components, applications and data sources.
* **Type**

  Out-of-the-box features such as class inheritance, metadata support, validation and serialization.
* **Core**
  * **Environment**

    Platform environmental information.
  * **Modules**

    Metadata about the Pentaho JavaScript modules.
  * **Configuration**

    JavaScript modules configured by third-parties.
  * **Debugging>**

    Debugging level of JavaScript modules.
  * **Localization>**

    Loading of `i18n` resource bundles.
  * **Theming**

    Coordination of registration and application for visual themes.
  * **Language Support**

    API building blocks for JavaScript.

See [Visualization API](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp) for a walk-through tutorial that guides you through the creation of a custom visualization for the Pentaho platform.

After you develop your visualization, you can create its web package and deploy the package to a Pentaho product via an OSGi container as detailed in the following articles:

* [Pentaho web package](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/pentaho-web-package-visapi-cp)
* [OSGi artifacts deployment](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/osgi-artifacts-deployment-visapi-reference)
