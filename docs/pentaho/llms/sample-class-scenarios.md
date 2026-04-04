# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/sample-class-scenarios.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/sample-class-scenarios.md

# Sample class scenarios

For each of the following embedding scenarios, a sample class can be executed as a stand-alone Java application:

* Run Transformations
* Run Jobs
* Dynamically Build Transformations
* Dynamically Build Jobs

Each sample has an associated unit test. To run an individual sample, execute the following command:

```
mvn test -Dtest=<sample unit test class>
```

The following sections describe how to use these samples as templates for embedding PDI in your applications.

## Run transformations

The `org.pentaho.di.sdk.samples.embedding.RunningTransformations` class is an example of how to run a PDI transformation from Java code in a stand-alone application. This class sets parameters and executes the sample transformations in `pentaho/design-tools/data-integration/etl` directory. You can run a transform from its KTR file using `runTransformationFromFileSystem()` or from a PDI repository using `runTransfomrationFromRepository()`.

Consider the following general steps while trying to run an embedded transformation:

1. Initialize the Kettle environment.

   Always make the first call to `KettleEnvironment.init()` whenever you are working with the PDI APIs.
2. Prepare the transformation.

   The definition of a PDI transformation is represented by a [TransMeta](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/trans/TransMeta.html) object. You can load this object from a KTR file, a PDI repository, or generate it dynamically. To query the declared parameters of the transformation definition use `listParameters()`. To query the assigned values, use `setParameterValue()`.
3. Execute the transformation.

   An executable [Trans](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/trans/Trans.html) object is derived from the `TransMeta` object that is passed to the constructor. The `Trans` object starts, then executes asynchronously. To ensure that all steps of the `Trans` object have completed, call `waitUntilFinished()`.
4. Evaluate the outcome.

   After the `Trans` object completes, you can access the result using `getResult()`. The [Result](http://javadoc.pentaho.com/kettle530/kettle-core-5.3.0.0-javadoc/org/pentaho/di/core/Result.html) object can be queried for success by evaluating `getNrErrors()`. This method returns zero (0) on success and a non-zero value when there are errors. To get more information, [retrieve the transformation log lines](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/obtain-logging-information).
5. Shutdown listeners.

   When the transformations have completed, call `KettleEnvironment.shutdown()` to ensure the proper shutdown of all kettle listeners.

## Run jobs

The `org.pentaho.di.sdk.samples.embedding.RunningJobs` class is an example of how to run a PDI job from Java code in a stand-alone application. This class sets parameters and executes the job in `etl/parametrized_job.kjb`. You can run the job from the `.kjb` file using `runJobFromFileSystem()` or from a repository using `runJobFromRepository()`.

Consider the following general steps while trying to run an embedded job:

1. Initialize the Kettle environment.

   Always make the first call to `KettleEnvironment.init()` whenever you are working with the PDI APIs.
2. Prepare the job.

   The definition of a PDI job is represented by a [JobMeta](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/job/JobMeta.html) object. You can load this object from a KTB file, a PDI repository, or generate it dynamically. To query the declared parameters of the job definition use `listParameters()`. To set the assigned values use `setParameterValue()`.
3. Execute the job.

   An executable [Job](http://javadoc.pentaho.com/kettle/org/pentaho/di/job/Job.html) object is derived from the `JobMeta` object that is passed to the constructor. The `Job` object starts, then executes in a separate thread. To wait for the job to complete, call `waitUntilFinished()`.
4. Evaluate the outcome.

   After the `Job` completes, you can access the result using `getResult(`). The [Result](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/job/Job.html) object can be queried for success using `getResult()`. This method returns `true`on success and `false` on failure. To get more information, [retrieve the job log lines](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/obtain-logging-information).
5. Shutdown listeners.

   When the transformations have completed, call `KettleEnvironment.shutdown()` to ensure the proper shutdown of all Kettle listeners.

## Dynamically build transformations

The `org.pentaho.di.sdk.samples.embedding.GeneratingTransformations` class is an example of a dynamic transformation. This class generates a transformation definition and saves it to a KTR file.

Consider the following general steps while trying to dynamically build a transformation:

1. Initialize the Kettle environment.

   Always make the first call to `KettleEnvironment.init()` whenever you are working with the PDI APIs.
2. Create and configure a transformation definition object

   A transformation definition is represented by a [TransMeta](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/trans/TransMeta.html) object. Create this object using the default constructor. The transformation definition includes the name, the declared parameters, and the required database connections.
3. Populate the `TransMeta` object with transformation steps

   The data flow of a transformation is defined by steps that are connected by hops. Perform the following tasks to populate the object with a transformation step:

   1. Create the step by instantiating its class directly and configure it by using its `get` and `set` methods.

      Transformation steps reside in sub-packages of `org.pentaho.di.trans.steps`.

      To use the Get File Names step, create an instance of [org.pentaho.di.trans.steps.getfilenames.GetFileNamesMeta](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/trans/steps/getfilenames/GetFileNamesMeta.html) and use its `get` and `set` methods to configure it.
   2. Obtain the step ID string.

      Each PDI step has an ID that can be retrieved from the PDI [plugin registry](http://javadoc.pentaho.com/kettle/org/pentaho/di/core/plugins/PluginRegistry.html).

      A simple way to retrieve the step ID is to call `PluginRegistry.getInstance().getPluginId(StepPluginType.class, theStepMetaObject)`.
   3. Create an instance of `org.pentaho.di.trans.step.StepMeta` by passing the step ID string, the name, and the configured step object to the constructor.

      An instance of `StepMeta` encapsulates the step properties, as well as controls the placement of the step on the PDI client (Spoon) canvas and connections to hops.
   4. Once the `StepMeta` object has been created, call `setDrawn(true)` and `setLocation(x,y)` to make sure the step appears correctly on the PDI client canvas.
   5. Add the step to the transformation, by calling `addStep()` on the transformation definition object.
4. Connect the hops.

   Once steps have been added to the transformation definition, they need to be connected by hops. To create a hop, create an instance of [org.pentaho.di.trans.TransHopMeta](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/trans/TransHopMeta.html), passing in the From and To steps as arguments to the constructor. Add the hop to the transformation definition by calling `addTransHop()`.

After all steps have been added and connected by hops, the transformation definition object can be serialized to a KTR file by calling `getXML()` and opening it in the PDI client for inspection. The sample class `org.pentaho.di.sdk.samples.embedding.GeneratingTransformations` generates the following example transformation:

![Dynamically building a transformation example](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-2a21eaed5cb95380e94260b7ead7f1ea3868da6d%2FEmbed_PDI_Dynamically_Build_transformation_example.png?alt=media)

## Dynamically build jobs

The `org.pentaho.di.sdk.samples.embedding.GeneratingJobs` class is an example of a dynamic job. This class generates a job definition and saves it to a KJB file.

Consider the following general steps while trying to dynamically build a job:

1. Initialize the Kettle environment.

   Always make the first call to `KettleEnvironment.init()` whenever you are working with the PDI APIs.
2. Create and configure a job definition object.

   A job definition is represented by a [JobMeta](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/job/JobMeta.html) object. Create this object using the default constructor. The job definition includes the name, the declared parameters, and the required database connections.
3. Populate the `JobMeta` object with job entries.

   The control flow of a job is defined by job entries that are connected by hops. Perform the following tasks to populate the object with a job entry:

   1. Create the entry by instantiating its class directly and configure it by using its `get` and `set` methods.

      Job entries reside in sub-packages of `org.pentaho.di.job.entries`.

      Use the File Exists job entry, create an instance of [org.pentaho.di.job.entries.fileexists.JobEntryFileExists](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/job/entries/fileexists/JobEntryFileExists.html), and use `setFilename()` to configure it. The **Start** entry is implemented by [org.pentaho.di.job.entries.special.JobEntrySpecial](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/job/entries/special/JobEntrySpecial.html).
   2. Create an instance of [org.pentaho.di.job.entry.JobEntryCopy](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/job/entry/JobEntryCopy.html) by passing the entry created in the previous step to the constructor.

      An instance of `JobEntryCopy` encapsulates the properties of an entry, as well as controls the placement of the entry on the PDI client canvas and connections to hops.
   3. Once created, call `setDrawn(true)` and `setLocation(x,y)` to make sure the entry appears correctly on the PDI client canvas.
   4. Add the entry to the job by calling `addJobEntry()` on the job definition object.

      It is possible to place the same entry in several places on the canvas by creating multiple instances of `JobEntryCopy` and passing in the same entry instance.
4. Connect the hops.

   Once entries have been added to the job definition, they need to be connected by hops. To create a hop, create an instance of `[org.pentaho.di.job.JobHopMeta](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/job/JobHopMeta.html)`, by passing in the From and To entries as arguments to the constructor. Configure the hop consistently. Configure it as a green or red hop by calling `setConditional()`and `setEvaluation(true/false)`. If it is an unconditional hop, call `setUnconditional()`. Add the hop to the job definition by calling `addJobHop()`.

After all entries have been added and connected by hops, the job definition object can be serialized to a KJB file by calling `getXML()`, and opened in the PDI client for inspection. The sample class `org.pentaho.di.sdk.samples.embedding.GeneratingJobs` generates the following example job:

![Dynamically building a job example](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-846042acf70074f70fb0424c308900501ccb4d48%2FEmbed_PDI_Dynamically_Build_Job_example.png?alt=media)
