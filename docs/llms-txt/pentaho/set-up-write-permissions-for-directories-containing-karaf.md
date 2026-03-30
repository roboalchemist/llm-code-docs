# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/set-up-write-permissions-for-directories-containing-karaf.md

# Set up write permissions for directories containing Karaf

Your users may experience performance issues when launching Kitchen or Pan unless you set up some variables specific to Karaf. You will need to set these up on individual workstations for users of Kitchen and Pan. Setting these variables makes sure that Kitchen and Pan launch as quickly as they did for 5.x. You can use these variables for Pentaho Report Designer, which also uses Karaf.

## Issue description

Previously, non-admin users would need to have write permissions for the directories where they installed Pentaho client tools. If they had read and execute permissions only, their client tools would fail for two reasons:

* A `data/cache` folder could not be created
* Contents in the `karaf/etc` folder could not be modified

**Note:** This same issue happened when trying to deploy a Pentaho Server within a Yarn cluster.

## Solution: Define -D variables for Karaf

As of 6.1.0.1, if a non-admin user is deploying a client tool with Karaf or executing a MapReduce job in Hadoop where their File System Level user only has read and execute permissions, the Karaf deployable content is written to a temporary directory where the user has write access. In this case, Karaf deploys to the user’s home directory OR a global tmp directory based on the file system. This deployment is used for this execution only and is deleted on exit of the application.

Two variables are used together specifically for Karaf deployments, one defines the location and the other allows for directory cleanup:

* Location: `-Dpentaho.karaf.root.copy.dest.folder=*/my/karaf/dir*`

  If you are defining this variable, the final directory should not exist yet. When the client is started, it will create the ending directory you have specified in the variable.
* Directory cleanup: `-Dpentaho.karaf.root.transient=true`
  * `True` forces the karaf folder to delete itself on exit of the application.
  * `False` allows the deployed files to stay in this location and be reused for a later execution.\
    You can gain faster performance by using the following the Karaf variables guidelines in workstation environments to improve deployment speeds for Karaf enabled applications. It enables users to reuse the deployed Karaf content instead of re-deploying for each execution.

Below is an example of how to configure these variables to leverage Karaf. You will need to define your system variable and then add `-D` parameters to Spoon and/or PRD.

### Define system variable

An Administrator will need to define the following system variable with the file system **PENTAHO\_KARAF\_ROOT**. The `dir` directory should not already exist, the executed application needs to create this directory on initial execution. For example:

`export PENTAHO_KARAF_ROOT=/my/karaf/dir`

### Add -D parameters to PDI client and/or PRD

For this **PENTAHO\_KARAF\_ROOT** variable to be used by the application, the following **–D** parameters need to be added to PDI client and/or PRD. Files such as Kitchen and Pan will reference these parameters from Spoon.

These **–D** parameters with their values are needed:

```
-Dpentaho.karaf.root.copy.dest.folder=$PENTAHO_KARAF_ROOT 
-Dpentaho.karaf.root.transient=false
```

In Spoon and PRD, these parameters need to be added to the java OPT location in the `spoon.sh` or `spoon.bat` files. Typically, these changes should only be applied to client tools.
