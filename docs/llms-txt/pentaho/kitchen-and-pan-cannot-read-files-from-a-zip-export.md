# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/kitchen-and-pan-cannot-read-files-from-a-zip-export.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/kitchen-and-pan-cannot-read-files-from-a-zip-export.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/kitchen-and-pan-cannot-read-files-from-a-zip-export.md

# Kitchen and Pan cannot read files from a ZIP export

If you are trying to read either transformations from Pan or jobs from Kitchen from a ZIP export but are getting errors, you may have a syntax error in your Pan or Kitchen command.

ZIP files must be prefaced by an exclamation point (!) character. On Linux and other Unix-like operating systems, you must escape the exclamation point with a backslash (\\!) as in the following Kitchen example:

Windows:

`Kitchen.bat /file:"zip:file:///C:/Pentaho/PDI Examples/Sandbox/linked_executable_job_and_transform.zip!Hourly_Stats_Job_Unix.kjb"`

Linux:

`./kitchen.sh -file:"zip:file:////home/user/pentaho/pdi-ee/my_package/linked_executable_job_and_transform.zip\!Hourly_Stats_Job_Unix.kjb"`
