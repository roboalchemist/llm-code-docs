# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/examples/see-it-in-action.md

# See it in action

It is assumed that you have set up your system for data lineage. If you have not already done so, see [Setup](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/setup) for data lineage.

1. Save a transformation which contains a step you want to explore with the analyzer. (In the sample, use the Table Input step).
2. Connect a remote debugger to PDI on port 5005. Enter a breakpoint in your step analyzer's implementation.
3. Execute your transformation from PDI.

   You should hit your breakpoint when the step you are exploring is assessed by the transformation analyzer.

The execution will generate a GraphML file (along with an execution profile) for the transformation. You can find these files in `data-integration/pentaho-lineage-output/<Date of execution>/original/path/to/the/file/`. You can use a tool such as yEd to view the GraphML files.

**Note:** Working with yEd can be difficult. We have created a configuration for yEd to help ease the pain of viewing these graphs which you can access here: [https://github.com/pentaho/pentaho-engineering-samples/tree/master/Supplementary Files/yED Configuration Files](https://github.com/pentaho/pentaho-engineering-samples/tree/master/Supplementary%20Files/yED%20Configuration%20Files) Read the `readme.txt` file for help.

**Note:** In yEd, you will need to apply a layout to view the graph properly. Otherwise, all of the nodes will overlap each other.
