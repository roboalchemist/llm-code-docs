# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/the-group-by-step-is-not-supported-in-a-single-threaded-transformation-engine.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/big-data-issues/the-group-by-step-is-not-supported-in-a-single-threaded-transformation-engine.md

# Group By step is not supported in a single threaded transformation engine

If you have a job that contains both a Pentaho MapReduce entry and a `Reducer` transformation with a Group by step, you may receive a `Step 'Group by' of type 'GroupBy' is not Supported in a Single Threaded Transformation Engine` error message. This error can occur if:

* An entire set of rows sharing the same grouping key are filtered from the transformation before the Group By step.
* The **Reduce single threaded** option in the Pentaho MapReduce entry's **Reducer** tab is selected.

To fix this issue, open the Pentaho MapReduce entry and deselect the **Reduce single threaded** option in the **Reducer** tab.
