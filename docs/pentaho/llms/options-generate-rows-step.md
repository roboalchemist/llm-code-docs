# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/generate-rows/options-generate-rows-step.md

# Options

The Generate rows step has the following options:

| Option                           | Description                                                                                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Step Name**                    | Specify the unique name of the step on the canvas. The **Step name** is set to Generate rows by default.                                                                                                     |
| **Limit**                        | Specify the maximum number of rows that you want to generate.                                                                                                                                                |
| **Never stop generating rows**   | Select this check box when you want to keep generating rows. For example, you can use the output of this step for real-time use cases to drive recurring tasks like polling from a file, queue, or database. |
| **Interval in ms (delay)**       | Specify the interval, in milliseconds, between generated rows. The default is 5000.                                                                                                                          |
| **Current row time field name**  | Specify an optional name for the date field containing the time when the current row was generated. The default is now.                                                                                      |
| **Previous row time field name** | Specify an optional name for the date field containing the time when the previous row was generated. The default is five seconds ago.                                                                        |
