# Source: https://docs.snowflake.com/en/migrations/sma-docs/use-cases/sma-checkpoints-walkthrough/snowpark-checkpoints-execution-guide/collection.md

# Snowpark Migration Accelerator: Collection

To follow the collection process, please proceed with the steps outlined below:

1. Open the collection workload in VS Code to begin the process.
2. Generate checkpoints using the `checkpoints.json` file.

To generate checkpoints, you can perform one of the following actions:

1. Generate checkpoints by accepting the suggested message:
2. Execute the “Snowflake: Load All Checkpoints” command:

   Once all checkpoints are successfully loaded, your files should appear as shown below:
3. Run the Python file to execute the checkpoints collection process.

When running a Python file that includes checkpoints, a folder named `snowpark-checkpoints-output` will be created, containing the collection results.

The `checkpoints_collection_results.json` file contains the consolidated results of the collection process.

```json
{
  "results": [
    {
      "timestamp": "2025-05-05 15:06:43",
      "file": "sample.py",
      "line_of_code": 57,
      "checkpoint_name": "sample$BBVOC7$df1$1",
      "result": "PASS"
    },
    {
      "timestamp": "2025-05-05 15:06:53",
      "file": "sample.py",
      "line_of_code": 57,
      "checkpoint_name": "sample$BBVOC7$df2$1",
      "result": "PASS"
    },
    {
      "timestamp": "2025-05-05 15:06:58",
      "file": "sample.py",
      "line_of_code": 57,
      "checkpoint_name": "sample$BBVOC7$df3$1",
      "result": "PASS"
    }
  ]
}
```

The `snowpark-checkpoints-output` folder should be copied into the validation workload to grant access to the collection results. For details on how to proceed with the validation process, refer to the [Validation Section](https://app.gitbook.com/o/-MB4z_O8Sl--Tfl3XVml/s/6on4bNAZUZGzMpdEum8X/~/changes/499/use-cases/sma-checkpoints-walkthrough/snowpark-checkpoints-execution-guide/validation).
