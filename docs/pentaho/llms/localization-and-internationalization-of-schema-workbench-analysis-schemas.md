# Source: https://docs.pentaho.com/pba-schema-workbench/localization-and-internationalization-of-schema-workbench-analysis-schemas.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/localization-and-internationalization-of-schema-workbench-analysis-schemas.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/localization-and-internationalization-of-schema-workbench-analysis-schemas.md

# Localization and internationalization of analysis schemas

You can create internationalized message bundles for your analysis schemas and deploy them with the Pentaho Web application. This enables Analyzer to access localized schemas.

1. Edit your analysis schema and tokenize all values that you want to localize. Typically you would create variables for all caption and description values.

   `<Schema measuresCaption="%{foodmart.measures.caption}"> <Dimension name="Store" caption="%{foodmart.dimension.store.caption}" description="%{foodmart.dimension.store.description}"> <Hierarchy hasAll="true" allMemberName="All Stores" allMemberCaption="%{foodmart.dimension.store.allmember.caption =All Stores}" primaryKey="store_id" caption="%{foodmart.hierarchy.store.country.caption}" description="%{foodmart.hierararchy.store.country.description}> <Table name="store"/> <Level name="Store Country" column="store_country" uniqueMembers="true" caption="%{foodmart.dimension.store.country.caption}" description="%{foodmart.dimension.store.country.description}"/>`
2. Create localized `MondrianMessages.properties` files in the `/WEB-INF/classes/com/pentaho/messages/` directory inside of the Pentaho WAR, and define each token you used in the analysis schema.

   If you need further assistance in creating localized message bundles on the Pentaho Server, refer to Customize the Pentaho User Console.

   ```
   foodmart.measures.caption=Measures
   foodmart.dimension.store.country.caption=Store Country
   foodmart.dimension.store.name.property_type.column=store_type
   foodmart.dimension.store.country.member.caption=store_country
   foodmart.dimension.store.name.property_type.caption=Store Type
   foodmart.dimension.store.name.caption=Store Name
   foodmart.dimension.store.state.caption=Store State
   foodmart.dimension.store.name.property_manager.caption=Store Manager
   foodmart.dimension.store.name.property_storesqft.caption=Store Sq. Ft.
   foodmart.dimension.store.allmember.caption=All Stores
   foodmart.dimension.store.caption=Store
   foodmart.cube.sales.caption=Sales
   foodmart.dimension.store.city.caption=Store City
   foodmart.cube.sales.measure.unitsales=Unit Sales
   ```
3. Edit the `mondrian.properties` file in the `/pentaho/server/pentaho-server/pentaho-solutions/system/mondrian/` directory and add this line (or modify it if it's already there):

   ```
   mondrian.rolap.localePropFile=com.pentaho.messages.MondrianMessages

   ```
4. Save and close the file.
5. Restart the Pentaho Server.
6. Log in to the User Console with administration permissions, then click **Manage Data Sources**, then the **Add** button. Choose **Analysis** from the menu. Browse to import your file.
7. Edit your analysis data source by checking the option next to **Manually enter data source parameters**.
   1. If absent from the list of parameters, add one parameter called **DataSource** whose value is the name of the JDBC data source to use.
   2. Create a new parameter called **Locale** and enter the value for the language that you want to make available.
   3. Create a new parameter called **DynamicSchemaProcessor** with a value of `mondrian.i18n.LocalizingDynamicSchemaProcessor`.
   4. Create a new parameter called **UseContentChecksum** with a value of `true`.
8. In the User Console, go to **Tools** > **Refresh** > **Mondrian Schema Cache**.

Your analysis schemas will now be localized to whatever language is currently selected in the Pentaho User Console, if a message bundle for that locale was copied to the proper directory as explained above.
