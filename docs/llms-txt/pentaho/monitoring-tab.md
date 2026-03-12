# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/monitor-performance/monitoring-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring/monitor-performance/monitoring-tab.md

# Monitoring tab

Pentaho Data Integration provides you with a tool for tracking the performance of individual steps in a transformation. By helping you identify the slowest step in the transformation, you can fine-tune and enhance the performance of your transformations.

You enable the step performance monitoring in the Transformation Properties dialog box:

1. Right-click in the workspace that is displaying your transformation and select **Transformation Settings**.

   You can also access the Transformation Properties dialog box, by pressing CTRL T.
2. In the dialog box, select **Enable step performance monitoring?**

![Transformation Properties Dialog Box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d94a33f9c385001195d5823f02a2e556c1cda525%2FTransformationProperties_Monitoring.png?alt=media)

Step performance monitoring may cause memory consumption problems in long-running transformations. By default, a performance snapshot is taken for all the running steps every second. This is not a CPU-intensive operation and, in most instances, does not negatively impact performance unless you have many steps in a transformation or you take a lot of snapshots (several per second, for example). You can control the number of snapshots in memory by changing the **Maximum number of snapshots in memory** value. In addition, if you run in Spoon locally you may consume a fair amount of CPU power when you update the JFreeChart graphics under the **Performance** tab. Running in "headless" mode (Kitchen, Pan, Pentaho Server \[slave server], Carte, Pentaho BI platform, and so on) does not have this drawback and should provide you with accurate performance statistics.
