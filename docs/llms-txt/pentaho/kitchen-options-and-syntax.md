# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-command-line-tools-to-run-transformations-and-jobs/kitchen-options-and-syntax.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-command-line-tools-to-run-transformations-and-jobs/kitchen-options-and-syntax.md

# Kitchen Options and Syntax

Kitchen runs jobs, either from a PDI repository (database or enterprise), or from a local file. The syntax for the batch file and shell script are shown below. All Kitchen options are the same for both.

**Note:** Windows systems use syntax with the forward slash (“/”) and colon (“:”). If spaces are present in the option values, use single quotes (“) and double quotes (“”) to keep spaces together, for example, "`-param:MASTER_HOST=192.168.1.3" "-param:MASTER_PORT=8181`"

```
kitchen.sh -option=value arg1 arg2 
```

```
kitchen.bat /option: value arg1 arg2 
```

| Switch        | Purpose                                                                                                                                                                                                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rep           | Enterprise or database repository name, if you are using one                                                                                                                                                                                                                                                    |
| user          | Repository username                                                                                                                                                                                                                                                                                             |
| pass          | Repository password                                                                                                                                                                                                                                                                                             |
| job           | The name of the job (as it appears in the repository) to launch                                                                                                                                                                                                                                                 |
| dir           | The repository directory that contains the job, including the leading slash                                                                                                                                                                                                                                     |
| file          | If you are calling a local KJB file, this is the filename, including the path if it is not in the local directory                                                                                                                                                                                               |
| level         | The logging level (Basic, Detailed, Debug, Rowlevel, Error, Nothing)                                                                                                                                                                                                                                            |
| logfile       | A local filename to write log output to                                                                                                                                                                                                                                                                         |
| listdir       | Lists the sub-directories within the specified repository directory                                                                                                                                                                                                                                             |
| listjob       | Lists the jobs in the specified repository directory                                                                                                                                                                                                                                                            |
| listrep       | Lists the available repositories                                                                                                                                                                                                                                                                                |
| export        | Exports all linked resources of the specified job. The argument is the name of a ZIP file.                                                                                                                                                                                                                      |
| norep         | Prevents Kitchen from logging into a repository. If you have set the KETTLE\_REPOSITORY, KETTLE\_USER, and KETTLE\_PASSWORD environment variables, then this option will enable you to prevent Kitchen from logging into the specified repository, assuming you would like to execute a local KTR file instead. |
| version       | Shows the version, revision, and build date                                                                                                                                                                                                                                                                     |
| param         | Set a named parameter in a **name=value** format. For example: **-param:FOO=bar**                                                                                                                                                                                                                               |
| listparam     | List information about the defined named parameters in the specified job.                                                                                                                                                                                                                                       |
| maxloglines   | The maximum number of log lines that are kept internally by PDI. Set to 0 to keep all rows (default)                                                                                                                                                                                                            |
| maxlogtimeout | The maximum age (in minutes) of a log line while being kept internally by PDI. Set to 0 to keep all rows indefinitely (default)                                                                                                                                                                                 |

```
sh kitchen.sh -rep=initech_pdi_repo -user=pgibbons -pass=lumburghsux -job=TPS_reports_2011
```

```
kitchen.bat /rep:initech_pdi_repo /user:pgibbons /pass:lumburghsux /job:TPS_reports_2011
```
