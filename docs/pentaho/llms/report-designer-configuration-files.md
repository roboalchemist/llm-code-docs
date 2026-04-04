# Source: https://docs.pentaho.com/pba-report-designer/report-designer-configuration-files.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/report-designer-configuration-files.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/report-designer-configuration-files.md

# Report Designer configuration files

Upon first launch, Report Designer creates a `.pentaho` directory in the current user's home directory, and populates it with the following subdirectories:

* **caches**

  Contains cached fonts, which speeds up report rendering
* **classic-engine**

  A cache directory that contains low-level options saved by the Pentaho Reporting engine
* **report-designer**

  Contains both the default Pentaho-supplied report samples and content, and user preferences for the Report Designer interface
* **report-design-wizard**

  Contains the default Pentaho-supplied Report Design Wizard templates
* **simple-jndi**

  Holds a single properties file that contains JNDI connection information. By default it has connection details for the Pentaho-supplied HSQLDB sample database

The following files contain various configuration options for Pentaho Reporting. The options are not particularly self-explanatory and their value limits are not obvious; therefore, you shouldn't change any options in these files unless you are following guidelines from Pentaho documentation or are assisted by a Pentaho support or consulting representative.

* **`pentaho/design-tools/report-designer/resources/report-designer.properties`**

  Contains options for the Report Designer client tool. It does not change any report options.
* **`pentaho/design-tools/report-designer/resources/classic-engine.properties`**

  Contains global report rendering options for reports generated locally from Report Designer. Some of these options can be overridden in individual reports.
* **`tomcat/webapps/pentaho/WEB-INF/classes/classic-engine.properties`**

  Contains global report rendering options for published reports that are generated on the Pentaho Server. Some of these options can be overridden in individual reports.
