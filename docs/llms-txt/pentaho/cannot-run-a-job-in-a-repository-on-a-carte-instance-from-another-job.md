# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/cannot-run-a-job-in-a-repository-on-a-carte-instance-from-another-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/cannot-run-a-job-in-a-repository-on-a-carte-instance-from-another-job.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/cannot-run-a-job-in-a-repository-on-a-carte-instance-from-another-job.md

# Cannot run a job in a repository on a Carte instance from another job

If you run a Job on a Carte instance and the repository information does not seem available, and further jobs and transformations cannot be loaded after the job runs a child job, then you may see an error similar to the following message:

```
RepositoriesMeta - Reading repositories XML file: <HOME>/.kettle/repositories.xml
General - I couldn't find the repository with name 'singleDiServerInstance'
(...)
Secondary - Could not execute job specified in a repository since we're not connected to one
(...)
```

Perform the steps below to run jobs in a repository on a Carte instance from another job:

1. Using an editor, open the `<HOME>/.kettle/repositories.xml` file on the server where the Carte instance is located.
2. Add a new `<repository>` element to it or append the current content with the name `singleDiServerInstance`, as shown in the following code block:

   ```xml
   <repository>
       <id>PentahoEnterpriseRepository</id>
       <name>singleDiServerInstance</name>
       <description/>
       <is_default>false</is_default>
       <repository_location_url>http://localhost:8080/pentaho</repository_location_url>
       <version_comment_mandatory>N</version_comment_mandatory>
   </repository>
   ```
3. Save and close the file.

You can now run jobs in a repository on a Carte instance from another job.
