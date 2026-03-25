# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/jar-file-conflict-in-kafka-consumer-step.md

# JAR file conflict in Kafka Consumer step

When using the Kafka Consumer step with HDP 3.x on AEL Spark, there is a known conflict with the JAR file `/usr/hdp/3.x/hadoop-mapreduce/kafka-clients-0.8.2.1.jar`

Use one of the following solutions to resolve the JAR conflict.

* On HDP 3.x do not set the **SPARK\_DIST\_CLASSPATH** variable before running the Adaptive Execution Layer daemon. Otherwise, there may be issues in other AEL components.
* Exclude the JAR file from the path on **SPARK\_DIST\_CLASSPATH** with the `spark-dist-classpath.sh` script. Create the script with any text editor and include the following code:

  ```xml
  #!/bin/sh
  ##
  ## helper script for setting up SPARK_DIST_CLASSPATH for AEL
  ## removes conflicting JAR files existing in HDP 3.x
  ## Using: call this the same way you use hadoop classpath, command, i.e.:
  ## export SPARK_DIST_CLASSPATH=$(spark-dist-classpath.sh)

  # grab hadoop classpath
  HCP=`hadoop classpath`

  ## expand it to grab all jar files
  (
    for entry in `echo "$HCP" | sed -e 's/:/\n/g'` ; do
       ## clean up dirs ending with *
       entryCleaned=`echo "$entry" | sed -e 's/\*$//'`
       ## if dir, expand it
       if test -d $entryCleaned ; then
         find $entryCleaned  
       else
         echo "$entry"
       fi 
    done 
  ) | grep -v kafka-clients-0.8.2.1.jar |  paste -s -d: 

  exit

  ```
