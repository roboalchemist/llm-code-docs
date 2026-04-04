# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/importing-and-updating-email-addresses-used-for-scheduling-from-data-sources.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/importing-and-updating-email-addresses-used-for-scheduling-from-data-sources.md

# Importing and updating email addresses used for scheduling from data sources

You can adjust and run sample transformations to import email addresses from LDAP or JDBC sources to be used for scheduling notifications from the Pentaho Server via the Pentaho User Console (PUC). Once you have initially imported the data, you can schedule the transformations to run periodically to update the email addresses based on the LDAP or JDBC sources.

You can find the following sample transformations in the `server/pentaho-server/pentaho-solutions/email-import-samples` directory:

* For LDAP sources: `LDAPEmailImportV3.ktr`
* For JDBC sources: `JDBCEmailImportV3.ktr`

You can also use an optional parameter defined for these transformations and a related column in the Pentaho email Hibernate database table to manage multiple sources. Using the parameter and related column helps to keep emails from different sources from interfering with each other. The transformations are designed to only act upon rows in the Hibernate table that match this optional parameter. Any inserts, deletions, or update only apply to those rows with the column that matches the parameter. For example, if you have multiple LDAP servers for different local or business units, such as LDAP-US, LDAP-EU, and LDAP-ASIA. You can adjust the transformation parameter for each one of these sources to import and maintain email addresses from each server without affecting the others.

## Import and update email addresses

{% tabs %}
{% tab title="Import and update from JDBC source" %}
Perform the following steps in the Pentaho Data Integration (PDI) client to adjust the sample JDBC transformation, then run the transformation to import the email addresses:

1. Open the sample `JDBCEmailImportV3.ktr` transformation in the PDI client.

   See the **Open a transformation** section in the **Pentaho Data Integration** document for details.
2. Select **Properties** from the menu that appears when you right-click in an empty area of the PDI client canvas.

   The **Transformation properties** dialog box opens.
3. Click the **Parameters** tab to access the `MANAGED_SOURCE` and `PENTAHO_BASE_URL` transformation parameters.
4. Specify a source of the email address data for the `MANAGED_SOURCE` parameter.

   As a best practice, you should use and maintain separate transformations for each source. For example, if you have multiple JDBC databases for different local or business units (such as `JDBC-US` and `JDBC-ASIA`), you should save a version of the `JDBCEmailImportV3` transformation per each source with `MANAGED_SOURCE` set to `JDBC-US` for one transformation and `MANAGED_SOURCE` set to `JDBC-ASIA` for the other transformation.
5. Specify the URL of your Pentaho User Console (PUC) for the `PENTAHO_BASE_URL` parameter.

   By default, in a standard installation, the URL for PUC is `http://localhost:8080/pentaho`, yet your Pentaho administrator can and may have configured it to be different from the default. Check with your Pentaho administrator if you are not sure of the URL used for your instance of PUC.
6. Click **OK** to close the **Transformation properties** dialog box.

   With the transformation parameters, you need to specify the related Pentaho email Hibernate database table columns before running the transformation.
7. Double click on the **JDBC Input** step in the transformation.

   The **Table input** step properties dialog box opens.
8. Specify the column names used for the email source, last names, and first names in your JDBC source with the SQL statements shown in the **SQL** text box.

   The column name specified for the email source should match the value you specified for the `MANAGED_SOURCE` parameter.
9. Click **OK** to save your specified values and close the **Table input** step properties dialog box.
10. Save the transformation as a filename specific to your JDBC source (`JDBCEmailImportForJDBC-US.ktr` for the `JDBC-US` managed source for example), then run the transformation.

    See the **Run your transformation** section in the **Pentaho Data Integration** document for details.

The email addresses from your JDBC source should now appear on the Email Groups page under the **Administration** perspective in your PUC instance. You can now use this same transformation to update the email addresses periodically by setting it up to run on a schedule. See the **Schedule a transformation or job** section in the **Pentaho Data Integration** document for details.
{% endtab %}

{% tab title="Import and update from LDAP source" %}
Perform the following steps in the Pentaho Data Integration (PDI) client to adjust the sample LDAP transformation, then run the transformation to import the email addresses:

1. Open the sample `LDAPEmailImportV3.ktr` transformation in the PDI client.

   See the **Open a transformation** section in the **Pentaho Data Integration** document for details.
2. Select **Properties** from the menu that appears when you right-click in an empty area of the PDI client canvas.

   The **Transformation properties** dialog box opens.
3. Click the **Parameters** tab to access the `MANAGED_SOURCE` and `PENTAHO_BASE_URL` transformation parameters.
4. Specify a source of the email address data for the `MANAGED_SOURCE` parameter.

   As a best practice, you should use and maintain separate transformations for each source. For example, if you have multiple LDAP servers for different local or business units (such as `LDAP-US` and `LDAP-ASIA`), you should save a version of the `LDAPEmailImportV3` transformation per each source with `MANAGED_SOURCE` set to `LDAP-US` for one transformation and `MANAGED_SOURCE` set to `LDAP-ASIA` for the other transformation.
5. Specify the URL of your Pentaho User Console (PUC) for the `PENTAHO_BASE_URL` parameter.

   By default, in a standard installation, the URL for PUC is `http://localhost:8080/pentaho`, yet your Pentaho administrator can and may have configured it to be different from the default. Check with your Pentaho administrator if you are not sure of the URL used for your instance of PUC.
6. Click **OK** to close the **Transformation properties** dialog box.

   With the transformation parameters, you need to specify the related Pentaho email Hibernate database table columns before running the transformation.
7. Double click on the **LDAP Input** step in the transformation.

   The **LDAP Input** step properties dialog box opens.
8. Click the **Fields** tab and specify the field names used for the email source, last names, and first names in your LDAP source.

   The field name specified for the email source should match the value you specified for the `MANAGED_SOURCE` parameter.
9. Click **OK** to save your specified values and close the **LDAP input** step properties dialog box.
10. Save the transformation as a filename specific to your LDAP source (`LDAPEmailImportForJDBC-US.ktr` for the `LDAP-US` managed source for example), then run the transformation.

    See the **Run your transformation** section in the **Pentaho Data Integration** document for details.

The email addresses from your LDAAP source should now appear on the Email Groups page under the **Administration** perspective in your PUC instance. You can now use this same transformation to update the email addresses periodically by setting it up to run on a schedule. See the **Schedule a transformation or job** section in the **Pentaho Data Integration** document for details.
{% endtab %}
{% endtabs %}
