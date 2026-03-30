# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/internal-variables.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables/internal-variables.md

# Internal variables

The following variables are always defined:

| Variable Name                     | Sample Value          |
| --------------------------------- | --------------------- |
| **Internal.Kettle.Build.Date**    | `2010/05/22 18:01:39` |
| **Internal.Kettle.Build.Version** | `2045`                |
| **Internal.Kettle.Version**       | `4.3`                 |

These variables are defined in a transformation:

| Variable Name                                    | Sample Value                                        |
| ------------------------------------------------ | --------------------------------------------------- |
| **Internal.Transformation.Filename.Directory**   | `D:\Kettle\samples`                                 |
| **Internal.Transformation.Filename.Name**        | `Denormaliser - 2 series of key-value pairs.ktr`    |
| **Internal.Transformation.Name**                 | `Denormaliser - 2 series of key-value pairs sample` |
| **Internal.Transformation.Repository.Directory** | `/`                                                 |

These are the internal variables that are defined in a job:

| Variable Name                         | Sample Value             |
| ------------------------------------- | ------------------------ |
| **Internal.Job.Filename.Directory**   | `file:///home/matt/jobs` |
| **Internal.Job.Filename.Name**        | `Nested jobs.kjb`        |
| **Internal.Job.Name**                 | `Nested job test case`   |
| **Internal.Job.Repository.Directory** | `/`                      |

These variables are defined in a transformation running on a slave server, executed in clustered mode:

| Variable Name                            | Sample Value                         |
| ---------------------------------------- | ------------------------------------ |
| **Internal.Slave.Transformation.Number** | `0..<cluster size-1> (0,1,2,3 or 4)` |
| **Internal.Cluster.Size**                | `<cluster size> (5)`                 |

**Note:** In addition to the above, there are also System parameters, including command line arguments. These can be accessed using the [Get System Info](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/get-system-info) step in a transformation.

**Note:** Additionally, you can specify values for variables in the Execute a transformation dialog box. If you include the variable names in your transformation they will appear in this dialog box.
