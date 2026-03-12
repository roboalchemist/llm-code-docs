# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-data-integration-performance-tips/enable-weka-plugins-pdi-performance-tips-admin.md

# Enable Weka plugins

You can improve the startup performance of the PDI client by disabling plugins that you do not need. For example, the Weka plugins are disabled by default. The plugins are disabled by the presence of a `.kettle-ignore` file that is included by default in every Weka plugin folder, which prevents the Weka plugins from loading when PDI starts. To enable the Weka plugins, delete the `.kettle-ignore` files in the following directories and restart the PDI client:

* `data-integration/plugins/weka-forecasting`
* `data-integration/plugins/weka-scoring`
* `data-integration/plugins/weka-timeseriesForecasting`
