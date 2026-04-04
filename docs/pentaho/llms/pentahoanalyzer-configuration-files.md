# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips/pentahoanalyzer-configuration-files.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips/pentahoanalyzer-configuration-files.md

# PentahoAnalyzer configuration files

The following files contain various configuration options for Pentaho Analyzer. The options are not particularly self-explanatory and their value limits are not obvious; therefore, you shouldn't change any options in these files unless you are following guidelines from Pentaho documentation or are assisted by a Pentaho support or consulting representative.

| File                                                                                   | Purpose                                                                                                                                           |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/pentaho/server/pentaho-server/pentaho-solutions/system/mondrian/mondrian.properties` | Contains low-level configuration options for the PentahoAnalyzer(Mondrian) engine.                                                                |
| `/pentaho/server/pentaho-server/pentaho-solutions/system/analyzer/analyzer.properties` | Contains low-level configuration options for Pentaho Analyzer. These are not options that can be set through Analyzer's graphical user interface. |
