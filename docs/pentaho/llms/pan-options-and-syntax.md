# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-command-line-tools-to-run-transformations-and-jobs/pan-options-and-syntax.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-command-line-tools-to-run-transformations-and-jobs/pan-options-and-syntax.md

# Pan Options and Syntax

Pan runs transformations, either from a PDI repository (database or enterprise) or a local file. The syntax for the shell script and batch file are shown below. All Pan options are the same for both.

**Note:** Windows systems use syntax with the forward slash (“`/`”) and colon (“`:`”). If spaces are present in the option values, use single quotes (`“`) and double quotes (`“”`) to keep spaces together, for example, `"-param:MASTER_HOST=192.168.1.3" "-param:MASTER_PORT=8181"`

```
pan.sh -option=value arg1 arg2
```

```
pan.bat /option: value arg1 arg2
```

For example:

```
sh pan.sh -rep=initech_pdi_repo -user=pgibbons -pass=lumburgh -trans=TPS_reports_2011
```

```
pan.bat /rep:initech_pdi_repo /user:pgibbons /pass:lumburgh /trans:TPS_reports_2011
```

| Switch        | Purpose                                                                                                                                                                                                                                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| rep           | Enterprise repository name.                                                                                                                                                                                                                                                                            |
| user          | Repository username.                                                                                                                                                                                                                                                                                   |
| pass          | Repository password.                                                                                                                                                                                                                                                                                   |
| trans         | The name of the transformation you want to launch.                                                                                                                                                                                                                                                     |
| dir           | The repository directory that contains the transformation, including the leading slash.                                                                                                                                                                                                                |
| file          | If you are calling a local KTR file, this is the filename, including the path if it is not located in the local directory.                                                                                                                                                                             |
| level         | Set the logging level: Basic, Detailed, Debug, Rowlevel, Error, Nothing.                                                                                                                                                                                                                               |
| logfile       | The logging file path to write to.                                                                                                                                                                                                                                                                     |
| listdir       | List the directories in the specified repository.                                                                                                                                                                                                                                                      |
| listtrans     | List the transformations in the specified repository directory.                                                                                                                                                                                                                                        |
| listrep       | List the available repositories.                                                                                                                                                                                                                                                                       |
| exprep        | Export all repository objects to one XML file.                                                                                                                                                                                                                                                         |
| norep         | Prevent Pan from logging into a repository. If you have set the KETTLE\_REPOSITORY, KETTLE\_USER, and KETTLE\_PASSWORD environment variables, then this option will enable you to prevent Pan from logging into the specified repository, assuming you would like to execute a local KTR file instead. |
| safemode      | Run in safe mode, which enables extra checking.                                                                                                                                                                                                                                                        |
| version       | Show the version, revision, and build date.                                                                                                                                                                                                                                                            |
| param         | Set a named parameter in a *name=value* format. For example: *-param:Foo=bar*                                                                                                                                                                                                                          |
| listparam     | List information about the defined named parameters in the specified transformation.                                                                                                                                                                                                                   |
| metrics       | Gather metrics during execution.                                                                                                                                                                                                                                                                       |
| maxloglines   | Set the maximum number of log lines that are kept internally by PDI. Set to 0 to keep all rows (default).                                                                                                                                                                                              |
| maxlogtimeout | Set the maximum age (in minutes) of a log line while being kept internally by PDI. Set to 0 to keep all rows indefinitely (default).                                                                                                                                                                   |
