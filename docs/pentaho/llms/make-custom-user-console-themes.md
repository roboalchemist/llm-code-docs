# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-the-pentaho-user-console/make-custom-user-console-themes.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-the-pentaho-user-console/make-custom-user-console-themes.md

# Make custom User Console themes

The User Console's graphical interface is built on a CSS-based theme system. The sections below contain information for theme designers and developers.

## Understanding theme system basics

The CSS-based theme system enables you to change the look of the Pentaho Server. With this type of theme system, you can create or add your own themes by working with just a few key configuration files.

The style sheets that make up the look and feel of the User Console, Dashboard Designer, Analyzer, and Interactive Reports are mostly in one location. These styles and scripts combine to make the default system theme, Ruby. This theme is located in the Common UI plug-in directory: `pentaho/server/pentaho-server/pentaho-solutions/system/common-ui/resources/themes`.

Themes can be systemwide or local.

* **Systemwide**

  Common styles and scripts applied across the client tools of the entire Pentaho Server. For example, the style of the buttons used in the client tools are defined in the default systemwide Ruby theme. A modification to the buttons in the Ruby theme changes the way buttons look in all the client tools.
* **Local**

  Styles and scripts applied to a particular area, also known as context. Contexts include Pentaho Server plug-ins as well as the names of the top-level directories in the Pentaho WAR file. These theme resources only take effect in their particular area of the Pentaho Server client tools.

Any page that includes the `webcontext.js` script automatically contains all of the active theme's JavaScript and CSS files when shown by the Pentaho Server.

For example, the following theme, called `Crystal`, contains one CSS and JavaScript file:

```xml
<themes root-folder="style">
   <crystal display-name="Crystal" system="true">
    <file>crystalStyles.css</file>
    <file>crystalScripts.js</file>
   </crystal>
</themes>
```

When this theme is active, the following resources are added to the HTML page:

```xml
<script type="text/javascript" src="/pentaho/common-ui/themes/crystal/crystalStyles.js"></script>
<link rel="stylesheet" type="text/css" href="/pentaho/common-ui/themes/crystal/crystalStyles.css"/>
```

This automatic insertion of theme resources makes it possible to change themes without having to edit the main content HTML documents to include the theme resource's tag individually. The theme system can include any number of JavaScript and CSS files defined for your theme.

Although resources are automatically inserted, your CSS changes will not appear in the User Console until you start and restart the Pentaho Server. Every time you modify a theme along with any XML or CSS files, the Pentaho Server must be restarted before your changes can appear in the User Console.

You can add local styles in a similar fashion. The only requirement is for you to tell the system what context you need to load. You can tell the system what needs to be loaded by adding `?context=myPlugin` to the `webcontext.js` script where *myPlugin* is the name of your plug-in or root WAR folder:

```
<script type="text/javascript" src="webContext.js?context=*myPlugin*"></script>
```

## Creating a new theme

The best way to create a new theme is to copy an existing theme folder structure and modify it to make it your own. Make sure to duplicate the theme folder structure in both the `pentaho/server/pentaho-server/pentaho-solutions/system/common-ui` and `pentaho/server/pentaho-server/tomcat/webapps/pentaho/mantle/themes` directories when copying an existing theme.

On startup, the Pentaho Server searches for `themes.xml` files in every plug-in and root-level folder in the Pentaho WAR file. Multiple themes can be defined in the themes.xml files of each directory. Themes can be systemwide, local, or a combination of both. The following example defines both a systemwide and local theme named `Crystal`.

```xml
<themes root-folder="resources/themes">
    <crystal display-name="Crystal" system="true">
     <file>crystalStyles.css</file>
     <file>crystalScripts.js</file>
    </crystal>
    <crystal display-name="Crystal" system="true">
     <file>localCrystalStyles.css</file>
    </crystal>
</themes>
```

The `<themes>` node has a root-folder attribute. The value of this attribute is the name of the directory (relative to the Web application context) where your themes are stored. For WAR-based contexts, it is simply a directory name inside the WAR file. For example, if your theme is located under an accounting folder inside the structure of your Pentaho WAR file, the resources are loaded from the accounting/resources/themes folder of this structure.

Besides inserting the new `<themes>` node into the `themes.xml` files, you need to change the name of the `mantleTheme_name.css` file in the copied mantle theme folder structure to match your new theme name (*Theme\_name*). After changing this file name, re-edit the `themes.xml` file in `pentaho/server/biserveree/tomcat/webapps/pentaho/mantle` to include a reference to this new CSS file.

Plug-in resource loading is different than WAR-based loading. With this type of loading, the plug-in controls how resources are mapped to the URL. If the theme file from above was located in a plug-in called `accounting`, then the resources are accessed from the following URL: `pentaho/context/accounting/resources/themes/`. This kind of resource mapping is most commonly implemented in Pentaho Server plug-ins through static-path entries:

```xml
<static-paths>
    <static-path url="/accounting/resources" localFolder="resources"/>
</static-paths>
```

When you want your changes to appear, restart the Pentaho Server before opening the User Console.

## Setting the default theme

The default system theme is defined in the `pentaho-solutions/system/pentaho.xml` configuration file through the `<default-theme>` node. The Pentaho Server ships with Ruby as the default theme; changing the value to another theme name will set the default active theme for all User Console users.

## Switching console themes

If you have created an alternate theme or localized message bundle, you can switch to it through the **View** menu in the Pentaho User Console.

**Note:** You can prevent themes from appearing in this menu by adding a `hidden="true"` property to the theme node.

You can manually specify a theme for a specified page by including a **theme=** URL parameter. Only the requested page is affected. For example, the following URL loads the `Sapphire` theme systemwide and local themes if available:

```
http://localhost:8080/pentaho/Home?theme=sapphire
```

If either the systemwide or local debug theme is not found, the resources for the currently active theme are loaded instead, which is useful when testing new themes and for loading debug versions of scripts and styles.

It is also possible to set the session variable *pentaho-user-theme* to the desired theme name, which is usually done in a start-up action to have per-user themes in multi-tenancy scenarios.
