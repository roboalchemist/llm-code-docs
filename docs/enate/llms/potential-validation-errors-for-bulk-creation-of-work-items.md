# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/appendix/potential-validation-errors-for-bulk-creation-of-work-items.md

# Potential Validation Errors for Bulk Creation of Work Items

| **Error Area**                                                                     | **Description**                                                                                       |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Status Error**                                                                   |                                                                                                       |
| "not\_valid": "Data not valid or Something went wrong"                             | When wrong information is input into a cell, so work items are not able to be created                 |
| "completed": "Completed"                                                           | When work items are successfully created                                                              |
| "in\_progress": "In progress"                                                      | When work item creation is in progress                                                                |
| **Error**                                                                          |                                                                                                       |
| "1": "Uploaded file is not a \*.xls or \*.xlsx file"                               | When the upload file format is other than .xls or .xlsx file                                          |
| "3": "Workbook has multiple worksheets. Only first sheet will be processed"        | When the same file has multiple sheets of work data to be processed                                   |
| "5": "Master Process Instance not live"                                            | When the process instance is not live or the versions are draft                                       |
| "101": "Worksheet is missing the required column '{{v0}}'"                         | When the excel sheet does not have required column to process work items                              |
| "102": "Column '{{v0}}' is of type '{{v1}}' which is not supported in Bulk Create" | When we use unsuported dat types like Entity relastionship , Table                                    |
| "103": "No field found to link Column '{{v0}}' to"                                 | When Validate bulk create api is not able to map the column data with the system data                 |
| "200": "Creation of a schedule-driven Case is not supported"                       | When a Case is linked to schedules and use the Case in the excel                                      |
| "300": "Title is not unique in file"                                               | When uploaded file has same title for multiple work items in the file                                 |
| "301": "Title is not unique"                                                       | When uploaded file has same title that is already created in system                                   |
| "302": "Value is blank and column is required"                                     | When there are no input values for mandatory fields                                                   |
| "303": "Value in not valid for data type '{{v0}}'"                                 | When custom field cannot input the particular data or data is not related to custom field             |
| "304": "No person could be found from email address"                               | When we input a wrong email id or email id is not present in the system                               |
| "305": "Customer not found or you do not have permission to see it"                | When we input a wrong Customer name or we don’t access to create work items under particular customer |
| "306": "Contract not found under Customer or you do not have permission to see it" | When we input a wrong Contract name or we don’t access to create work items under particular customer |
| "307": "Service not found under Contract or you do not have permission to see it"  | When we input a wrong service name or we don’t access to create work items under particular Contract  |
| "308": "Process not found under Service or you do not have permission to see it"   | When we input a wrong Process name or we don’t access to create work items under particular service   |
| "309": "Ticket Category not found"                                                 | When we input wrong tickect category value                                                            |
| "310": "Value is not valid for list"                                               | When the input value doesn’tmatch the configured list/Multi level List data                           |
| **UI ERROR**                                                                       |                                                                                                       |
| "1001": "There are no valid items to process."                                     | Where there is no data to process in excel                                                            |
| "1002": "All valid items have been processed."                                     | When all the valid work items are created                                                             |
| "file\_upload\_limit": "{{name}} is bigger than the server limit ({{limit}})"      | When the uploaded file size is larger than the system configured upload limit                         |
| "file\_upload\_failure": "Failed to upload file"                                   | when file upload is failed                                                                            |
