# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-command-line-tools-to-run-transformations-and-jobs/export-content-from-repositories-with-command-line-tools.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-command-line-tools-to-run-transformations-and-jobs/export-content-from-repositories-with-command-line-tools.md

# Export Content from Repositories with Command-Line Tools

To export repository objects into XML format, using command-line tools instead of exporting repository configurations from within the PDI client, use named parameters and command-line options when calling Kitchen or Pan from a command-line prompt.

The following is an example command-line entry to execute an export job using Kitchen:

```
call kitchen.bat /file:C:\Pentaho_samples\repository\repository_export.kjb
"/param:rep_name=PDI2000" "/param:rep_user=admin" "/param:rep_password=password"
"/param:rep_folder=/public/dev"
"/param:target_filename=C:\Pentaho_samples\repository\export\dev.xml"
```

| Parameter            | Description         |
| -------------------- | ------------------- |
| **rep\_folder**      | Repository Folder   |
| **rep\_name**        | Repository Name     |
| **rep\_password**    | Repository Password |
| **rep\_user**        | Repository Username |
| **target\_filename** | Target Filename     |

It is also possible to use obfuscated passwords with Encr, the command line tool for encrypting strings for storage/use by PDI. The following is an example command-line entry to execute a complete command-line call for the export in addition to checking for errors:

```
@echo off
ECHO This an example of a batch file calling the repository_export.kjb

cd C:\Pentaho\pdi-ee-<filepath>--check--</filepath>10.2.0>\data-integration

call kitchen.bat /file:C:\Pentaho_samples\repository\repository_export.kjb "/param:rep_name=PDI2000"
"/param:rep_user=admin" "/param:rep_password=password" "/param:rep_folder=/public/dev"
"/param:target_filename=C:\Pentaho_samples\repository\export\dev.xml"

if errorlevel 1 goto error
echo Export finished successful.
goto finished

:error
echo ERROR: An error occurred during repository export.
:finished
REM Allow the user to read the message when testing, so having a pause
pause
```
