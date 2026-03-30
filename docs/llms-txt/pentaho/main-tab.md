# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-execute/options-mongodb-execute/main-tab.md

# Main tab

![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a075e285d052ca98720cc5f137534d33cc77c0b1%2FMain%20tab%20for%20Execute%20step.png?alt=media)

Use this tab to specify the connection string and command execution properties.

## Connection

To specify your connection, use the following:

| Option           | Description                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| String           | Enter a MongoDBconnection string URI. Both `mongodb://` and `mongodb+srv://` schemes are supported. his option supports variable substitution, and it can contain the output of the `Encr.bat/encr.sh` command. For more information on URI construction, please see MongoDB's [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/) information. |
| Test and Get DBs | Click to test the connection string and get the databases you are authorized to access.                                                                                                                                                                                                                                                                                                  |
| Database         | Select from the list of databases on which you want ot perform the commands.                                                                                                                                                                                                                                                                                                             |

## Command(s) source

There are a few options to run commands.

Select the **Script** option when you want to run static commands.

![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-18fa15a7c8f5501530316bf1e0fa05040ac50586%2FScript%20button%20for%20Execute%20step.png?alt=media)

| Option                         | Description                                                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Script                         | Enter the commands you want to execute in the text box. You can use multiple commands by separating them with semi-colons.                                                                                          |
| Execute for every row of input | Select this option to execute the command for each incoming row for the step. When selected, a question mark(?) wild card field substitution can be used to modify the commands that will be invoked with row data. |

Select the \*\*Field\*\* option when the run commands are specified on an incoming field.

![](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d7a451d2d23e87275388fe3460a009f3f316c0d6%2FField%20button%20for%20Execute%20step.png?alt=media)

| Option                     | Description                                                                   |
| -------------------------- | ----------------------------------------------------------------------------- |
| Name                       | The name of an incoming field that contains one or more commands to execute.  |
| Perform ? value substition | Select this option to perform a field name substitution before the step runs. |
