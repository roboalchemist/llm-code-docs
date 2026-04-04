# Source: https://docs.pentaho.com/pdia-admin/administer/manage-the-pentaho-system/manage-the-pentaho-server/advanced-topics/customize-the-pentaho-server/change-the-pdi-home-directory-location.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-pdi-home-directory-location.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/manage-the-pentaho-system/manage-the-pentaho-server/customize-the-pentaho-server/change-the-pdi-home-directory-location.md

# Change the PDI home directory location

The default location for the Pentaho Data Integration home directory is the `.kettle` directory in your system user's home directory.

* Windows: `C:\Documents and Settings\example_user\.kettle`
* Linux: `~/.kettle)`

There will be a different `.kettle` directory, and therefore a different set of configuration files, for each system user that runs PDI.

The contents of this directory are listed in the following table:

| File                | Purpose                                                                        |
| ------------------- | ------------------------------------------------------------------------------ |
| `kettle.properties` | Main PDI properties file; contains global variables for low-level PDI settings |
| `shared.xml`        | Shared objects file                                                            |
| `db.cache`          | The database cache for metadata                                                |
| `repositories.xml`  | Connection details for PDI database or solution repositories                   |
| `.spoonrc`          | User interface settings, including the last opened transformation/job          |
| `.languageChoice`   | Default language for the PDI client tool                                       |

## Standalone PDI client tool deployments

You can specify a single, universal `.kettle` directory for all users by declaring a *KETTLE\_HOME* environment variable in your operating system. When declaring the variable, leave out the `.kettle` portion of it; this is automatically added by PDI.

`export KETTLE_HOME=/home/pentaho/examplepath/pdi`

## Pentaho Server deployments that run PDI content

If you followed a manual deployment or archive package installation path, you can set a system environment variable as explained above, but it must be declared before the Pentaho Server service starts. You can alternatively change the *CATALINA\_OPTS* system variable to include the -D flag for *KETTLE\_HOME*, or you can edit the script that runs the Pentaho Server and set the flag inline, as in this example from the `start-pentaho.sh script`:

`export CATALINA_OPTS="--Xms2048m -Xmx2048m -XX:MaxPermSize=256m -Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000" -DKETTLE_HOME=/home/pentaho/examplepath/pdi`

## Windows service modification

If you used the graphical utility to install the Pentaho Server, then you must modify the Java options flag that runs the Pentaho Server Tomcat service. Here is an example command that will change the value of *KETTLE\_HOME* to `C:\<examplepath>\pdi\.kettle`:

`tomcat8.exe //US//pentahobiserver ++JvmOptions -DKETTLE_HOME=C:\examplepath\pdi`
