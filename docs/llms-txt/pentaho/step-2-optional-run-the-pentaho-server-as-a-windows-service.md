# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-5-configure-pentaho-settings-for-jboss/add-jboss-logging/configure-and-start-the-pentaho-server-after-manual-installation/configure-the-pentaho-server-for-windows/step-2-optional-run-the-pentaho-server-as-a-windows-service.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/configure-and-start-the-pentaho-server-after-manual-installation/configure-the-pentaho-server-for-windows/step-2-optional-run-the-pentaho-server-as-a-windows-service.md

# Step 2: (Optional) Run the Pentaho Server as a Windows service

Optionally, you can create a Tomcat task to run the Pentaho Server as a Windows service. For more information, see: [Tomcat Windows service how-to documentation](https://tomcat.apache.org/tomcat-8.0-doc/windows-service-howto.html).

You will need to use the following settings in the GUI application that appears when you run `tomcat8w.exe` to configure the service:

| Tab                     | Field                                                                                                                                                                                                                          | Recommended Value                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| **Startup**             | **Working Path**                                                                                                                                                                                                               | Add `bin` to the end of the path. For example: `C:\pentaho\server\pentaho-server\tomcat\bin` |
| **Java**                | **Initial Memory Pool**                                                                                                                                                                                                        | *2048*                                                                                       |
| **Maximum Memory Pool** | *6144*                                                                                                                                                                                                                         |                                                                                              |
| **Java Option**         | <p>Add the following items:</p><ul><li><strong>-DDI\_HOME</strong></li><li><strong>-Dfile.encoding</strong></li><li><strong>-Djava.library.path</strong></li><li><strong>-Dpentaho.license.information.file</strong></li></ul> |                                                                                              |

The following examples are possible values for the Java options:

* `**-DDI\_HOME**=*C:\\pentaho\\server\\pentaho-server\\pentaho-solutions\\system\\kettle*`
* `**-Dfile.encoding**=*utf8*`
* `**-Djava.library.path**=*&lt;complete\_path&gt;\\server\\pentaho-server\\pentaho-solutions\\native-lib\\win64*`
* `**-Dpentaho.license.information.file**=*%PENTAHO\_LICENSE\_INFORMATION\_PATH%*`

  You must set the **PENTAHO\_LICENSE\_INFORMATION\_PATH** environment variable to point to the `.elmLicInfo.plt` file:

  **PENTAHO\_LICENSE\_INFORMATION\_PATH**=`<complete_path>\.elmLicInfo.plt`
