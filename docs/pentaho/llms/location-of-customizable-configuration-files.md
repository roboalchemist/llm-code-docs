# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-the-pentaho-user-console/location-of-customizable-configuration-files.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-the-pentaho-user-console/location-of-customizable-configuration-files.md

# Location of customizable configuration files

## Mantle style CSS

This is the structural cascading style sheet for the Pentaho User Console. It inherits some elements from the `Widgets.css` file in the same directory, so you may need to look at that as well. Modifying these styles could have dramatic impact on Pentaho User Console rendering.

`pentaho/server/pentaho-server/tomcat/webapps/pentaho/mantle/MantleStyle.css`

## Theme-specific local and global style sheets for PUC

These directories contain style sheets and other theme materials for each Pentaho Server client tool.

| File Name           | Location                                                                              | Description                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `globalRuby.css`    | `/server/pentaho-server/pentaho-solutions/system/common-ui/resources/themes/ruby/`    | This is the main structural, theme-specific style sheet for the default theme for the User Console (Ruby).                    |
| `mantleRuby.css`    | `/server/pentaho-server/tomcat/webapps/pentaho/mantle/themes/ruby/`                   | This is the customizable presentation portion of the theme style sheet for the default theme for the User Console (Ruby).     |
| `globalCrystal.css` | `/server/pentaho-server/pentaho-solutions/system/common-ui/resources/themes/crystal/` | This is the main structural, theme-specific style sheet for an alternate theme for the User Console (Crystal).                |
| `mantleCrystal.css` | `/server/pentaho-server/tomcat/webapps/pentaho/mantle/themes/crystal/`                | This is the customizable presentation portion of the theme style sheet for an alternate theme for the User Console (Crystal). |

## Product-specific theme settings for Analyzer, Dashboard Designer, and Interactive Reports

These directories contain style sheets and other theme materials for each.

Set the `<cache>false</cache>` in `pentaho-solutions/system/common-ui/settings.xml` while customizing these plugins. Otherwise, the changes are not visible without a server restart.

| Product Name        | Location                                                                       | Description                                                 |
| ------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Analyzer            | `pentaho-solutions/system/analyzer/styles/themes/`                             | Style sheets and theming materials for Analyzer.            |
| Interactive Reports | `pentaho-solutions/system/pentaho-interactive-reporting/resources/web/themes/` | Style sheets and theming materials for Interactive Reports. |
| Dashboard Designer  | `pentaho-solutions/system/dashboards/resources/themes/`                        | Style sheets and theming materials for Dashboard Designer.  |
