# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-pentaho-analyzer/localization.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-pentaho-analyzer/localization.md

# Localization

Perform the following steps to create localized message bundles for Pentaho Analyzer:

1. If the Pentaho Server is currently running, shut it down.
2. Make a copy of the `messages.properties` file in `pentaho-solutions/system/analyzer/resources/`.

   Name the copy according to the standard locale naming scheme defined earlier in this section.

   ```
   cp messages.properties messages_fr.properties
   ```
3. Translate the content of the new message bundle into the locale defined in its file name.
4. Edit the `messages_supported_languages.properties` file in `pentaho-solutions/system/analyzer/resources/` and add the new locale.

   ```
   fr=Francais
   ```

You now have a translated Analyzer message bundle for the Analyzer interface, not the OLAP data sources you use with Analyzer. For schema localization, refer to **Localization and internationalization of analysis schemas** in the **Pentaho Schema Workbench** document. To localize all web-based components on the Pentaho Server, refer to [Localize the Pentaho Server](https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-the-pentaho-user-console/localize-the-pentaho-server).
