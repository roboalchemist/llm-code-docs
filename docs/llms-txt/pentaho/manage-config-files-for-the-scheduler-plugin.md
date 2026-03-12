# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/manage-config-files-for-the-scheduler-plugin.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/manage-config-files-for-the-scheduler-plugin.md

# Manage config files for the Scheduler plugin

The following configuration files for using the Scheduler plugin with LDBC and LDAP should only be customized by someone with the necessary qualifications and experience.

## settings.xml

This file is located in the `pentaho-server/pentaho-solutions/system/scheduler-plugin` directory and contains properties that you can use to control the plugin cache for development purposes. In most cases, it is best not to modify any of the properties for `cache-messages`, `max-age`, or `cache` elements.

It also contains a section for defining the data source to be used for email group administration purposes in order to import existing emails and groups under the `email-source` element.

Example:

```
<email-source>pentaho</email-source>
```

Valid value for the `email-source` element:

| Valid values | Description                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| jdbc         | Uses a JDBC data source to import emails and groups.                                                                             |
| ldap         | Uses an LDAP data source to import emails and groups.                                                                            |
| pentaho      | Does not import emails and groups. Instead, you can create emails and groups using the email group administration module in PUC. |

The configuration properties for the JDBC and LDAP data sources are located in the `applicationContext-email-import.properties` file.

## applicationContext-email-import.properties

This file is located in the `pentaho-server/pentaho-solutions/system/scheduler-plugin` directory and contains the configuration properties for the JDBC and LDAP data sources. These data sources can be changed in the `settings.xml` file under the `email-source` element.

**Note:** Only someone with sufficient understanding of JDBC and LDAP should make changes to this file.

File location: `pentaho-server/pentaho-solutions/system/scheduler-plugin`

The password is encrypted using the `Encr` utility. The `Encr.bat` and `Encr.sh` files are located in the same directory as the startup script for Pentaho Server.

The `emails-imported` property defines whether emails have already been imported. If `true`, then no more emails are imported. After initial import, this property is automatically set to `true`. If more imports are done from a different data source, then this property needs to be set back to `false`.

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><p>Example based on a JDBC data source.</p><p>The actual query depends on the source RDBMS.</p><p>Prerequisites:</p><ul><li>The correct JDBC driver must be in the classpath for the JDBC configuration to work.</li><li>In the example, the &#x3C;datasource>.emails-query must return first name, last name, and email in that order. Field names in the output are dependent on the table columns that are imported.</li></ul><p>JDBC example:</p><pre><code>jdbc.emails-query=SELECT firstName, lastName, email FROM public.emails ORDER BY email ASC
</code></pre></td></tr></tbody></table>

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><p>Example based on a LDAP data source.</p><p>Prerequisites:</p><ul><li>Attributes required for LDAP must be in the following order: &#x3C;firstName>,&#x3C;lastName>,&#x3C;email>.</li></ul><p>LDAP example:</p><pre><code>ldap.required-attributes=&#x3C;firstName>,&#x3C;lastName>,&#x3C;email>
</code></pre></td></tr></tbody></table>

For more information about JDBC, see \[<https://www.oracle.com/java/technologies/javase/javase-tech-database.html]\\(https://www.oracle.com/java/technologies/javase/javase-tech-database.html)>

For more information about LDAP, see <https://ldap.com/>

## quartz.properties

This file is located in the `pentaho-server/pentaho-solutions/system/scheduler-plugin/quartz` directory and is the properties file for the open source job scheduling framework, Quartz. Refer to the official Quartz documentation at <http://www.quartz-scheduler.org/documentation/>.
