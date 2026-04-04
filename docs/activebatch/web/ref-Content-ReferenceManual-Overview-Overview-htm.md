# Source: https://documentation.activebatch.com/ref/Content/ReferenceManual/Overview/Overview.htm

Title: ActiveBatch - Overview

URL Source: https://documentation.activebatch.com/ref/Content/ReferenceManual/Overview/Overview.htm

Markdown Content:
ActiveBatch is a distributed workflow automation and Job scheduling system that allows you to execute repetitive tasks, called Jobs, to run in an unattended or background mode.This means that you do not have to log in to Windows or remain logged in for your non-interactive Jobs to execute.When a Job is submitted to ActiveBatch for processing, that script or program is said to become a batch Job. Batch Jobs allow for work to be scheduled and the results of the Job to be analyzed. Batch Jobs also offer the potential of utilizing your machines during their off-hours when interactive usage is typically at its lowest.

#### With ActiveBatch you can:

*   Execute workflows (Jobs and/or Plans) across Windows and non-Windows systems in a secure, reliable and efficient manner.

*   Create three different Job types - Process, Script and Jobs Library.

    *   The Process Job type allows you to specify the name of a script file or executable that you wish to run.

    *   The Script Job type allows you to add or edit a script that you wish to execute, where the script contents are stored in the ActiveBatch backend database. ActiveBatch is scripting language independent (you can run any script type) as long as the required scripting language is installed on a machine where your Jobs will run.

    *   The Jobs Library Job type allows scriptless integration using ActiveBatch's proven and reliable Job steps for frequently performed actions. For example, to manage FTP operations, there is a Managed File Transfer category of Job steps (e.g., file upload, download, etc.). The use of Jobs Library Job steps means you can utilize built-in facilities rather than having to write your own script. Many Job steps are platform independent. This means the same step logic can be used on different platforms such as Windows or Linux.

*   Utilize our Service Library object that includes various adapters, including the REST Adapter (V2) that lets you integrate with third-party REST API's.

*   Define Folders to organize the various ActiveBatch objects into an easily understood hierarchy (e.g., place all your FTP Jobs in an appropriately named Folder).

*   Define Plans to create a workspace for your Jobs and other ActiveBatch objects. You can optionally specify the order (e.g., sequentially) that Jobs should run in - for Jobs that are nested within a Plan. Think of a Plan as a wrapper around multiple Jobs and/or nested Plans that share a common purpose. For example, assume there are three Jobs in a Plan that must run sequentially. The first Job downloads a file from an FTP server. The second Job processes the file, and the third Job archives the file. After the Plan and its Jobs are created, you can configure the trigger mechanism (how the Plan will start) - for example, via a Schedule.

*   Create shareable objects to minimize the overall maintenance of your ActiveBatch environment. For example, Schedule objects can be shared among multiple Jobs that run on the same dates, and Queue objects can be shared among Jobs that need to run on the same Execution Agent systems.

*   Configure variables to allow for data passing between related Jobs and Plans, and to soft-code object properties in the event they should change. Variable values can be constant (the value is the same unless changed) or active (the value is retrieved from one of many built-in data sources). Variables have hierarchical global or local scope. Constant and active variables are resolved by the Job Scheduler, before the Job is dispatched to a system where it will run. ActiveBatch also supports runtime (execution) variables, mainly used when configuring a Jobs Library Job type. Execution variables are resolved while the Job is running.

*   Implement highly available scheduling and execution of workflows. ActiveBatch offers a high availability add-in solution for the Job Scheduler, and Microsoft Clusters are also supported. On a more granular Job level, there is support for automatic restart/failover and checkpoint recovery.

*   Run the ActiveBatch Health Service feature which offers recommendations on how to optimize your Job Scheduler environment.

*   Utilize the features that support many Microsoft and non-Microsoft technologies including .Net Assemblies, Java, Enterprise Java Beans, Active Directory, LDAP, executable images, database stored procedures and functions as well as the previously mentioned integrated built-in Jobs Library.

*   Use the Date Arithmetic feature to calculate dates (for example, to pass in as a Job's input parameter). Included is a Date Arithmetic Tester utility to test your date arithmetic expressions.

*   Create fiscal year(s) and tag dates for scheduling purposes, using the Date Arithmetic Admin utility.

*   Define Jobs with constraints (dependencies). Constraints include: Job Instance, File, Variable, Resource, and Date/Time. For example, a file constraint can be configured to prevent a Job from running until a specific file is present. Or you can specify a date/time that a Job should not run on, to prevent it from executing should a trigger occur.

*   Trigger Jobs or Plans for execution based on a schedule (including fiscal and business), and/or system/application events. Event triggers include WMI, file and FTP file triggers, Web Services, E-Mail, MSMQ, JMS, Twitter, VMware, Oracle DB and others. As an event trigger example, a Job can trigger when a file arrives in a directory being monitored by ActiveBatch. Some event triggers require separate licensing.

*   Execute a Job on a specific machine or a class of machines.

*   Execute a Job on a virtual machine in which a specific machine is chosen based on workload or other characteristics.

*   Utilize Scheduling Analytics and SmartScheduling which allows policy-based provisioning of virtualized machines (in either a private or public cloud) based on a predictive historical analysis of scheduled Jobs and Plans, in addition to an on-demand model that allows for supply of resources to be provisioned based on real-time demand.

*   Enable Heuristic Queue Allocation (HQA) for Generic Queues which allows predictive machine learning and artificial intelligence technologies when determining the best machine to use for any given scheduled workflow.

*   Run Windows Jobs interactively (that need a desktop) by using a separate built-in application named AbatIDH(Interactive Desktop Helper).

*   Retrieve Plan and Job history individually or within the context of a Plan run (so related Job instances can be viewed together). Plan and Job instances are easily retrieved using the “Instances” view and all instances are accurate based on the properties and their values at the time the instance was instantiated.

*   Obtain a complete audit trail of a Job instance including a log of the output of the Job. Auditing is also extended to the management of ActiveBatch objects. For example, each time a modification is made to an object, an audit is produced as well as a revision id. Auditing policies can be specified to ensure proper information is captured and company compliance with any regulations (for example, Sarbanes-Oxley) can be enforced.

*   Specify Service Level Agreement (SLA), run-time monitoring and alert capability to ensure that Jobs run properly and as expected. Alerts can send e-mail, trigger events, write to the event log, and so on. ActiveBatch supports Microsoft System Center Operations Manager and several other monitoring systems for its alert options.

*   Maintain multiple ActiveBatch environments (e.g. Development, Test and Production), and use the built-in Change Management application to compare and promote objects from one environment to another.

*   Use Template and Instance Reporting to report on instance or template data.

*   Graph various performance and Job processing metrics using the ActiveBatch Dashboard.

*   Use the built-in Service Manager to stop, start, and otherwise manage ActiveBatch services within the AbatConsole UI.

*   Manage your licenses using the License Manager.

Spotted a typo or can’t find help on a certain subject? Reach out to the Documentation team at [docsupport@redwood.com](mailto:docsupport@redwood.com?subject=ActiveBatch%20Documentation%20Feedback)
