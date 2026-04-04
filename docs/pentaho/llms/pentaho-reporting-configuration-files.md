# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-reporting-performance-tips/pentaho-reporting-configuration-files.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-reporting-performance-tips/pentaho-reporting-configuration-files.md

# Pentaho Reporting configuration files

The following files contain various configuration options for Pentaho Reporting. The options are not particularly self-explanatory and their value limits are not obvious; therefore, you shouldn't change any options in these files unless you are following guidelines from Pentaho documentation or are assisted by Pentaho Support or a consulting representative.

| File                                                                         | Purpose                                                                                                                                                                 |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/pentaho/design-tools/report-designer/resources/report-designer.properties` | Contains options for the Report Designerclient tool. It does not change any report options                                                                              |
| `/pentaho/design-tools/report-designer/resources/classic-engine.properties`  | Contains global report rendering options for reports generated locally from Report Designer. Some of these options can be overridden in individual reports.             |
| `/tomcat/webapps/pentaho/WEB-INF/classes/classic-engine.properties`          | Contains global report rendering options for published reports that are generated on the Pentaho Server. Some of these options can be overridden in individual reports. |
