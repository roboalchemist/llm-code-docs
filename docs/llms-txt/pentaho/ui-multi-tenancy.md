# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/multi-tenancy/ui-multi-tenancy.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/multi-tenancy/ui-multi-tenancy.md

# UI multi-tenancy

Each of the major components within the Pentaho Platform have a theme engine which allows you to control the presentation style through CSS and other methods. The reporting tools also have support for templates which allow you to apply structure to the report.

* Pentaho User Console (PUC) includes themes.
* Pentaho Analyzer (PAZ) includes themes.
* Pentaho Report Designer includes templates.
* Pentaho Interactive Reports includes themes and templates.
* Pentaho Dashboard Designer includes themes and templates.

## Theming

When you integrate content for users, you may want to make it look like the application into which it is being integrated. Furthermore, in multi-tenanted environments, you may want a different theme for each tenant. How to create additional themes is covered in the [Make custom User Console themes](https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-the-pentaho-user-console/make-custom-user-console-themes) article. This section focuses on setting the theme for different tenants.

### Setting the theme per tenant

The Pentaho User Console will present the specified theme if the *pentaho-user-theme* session variable is present. The other components with the user console will default to the same theme name which the user console is presenting. Set the *pentaho-user-theme* attribute in the user session using one of the techniques described in the "Preparing for Multi-Tenancy" section. The value of the attribute should be the name of the theme you have configured.
