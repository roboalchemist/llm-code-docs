# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/jms-consumer/before-you-begin-jms-consumer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/jms-consumer/before-you-begin-jms-consumer.md

# Before you begin

Before using the JMS Consumer step, be aware of the following conditions:

* You must be familiar with JMS messaging to use this step. Additionally, you must have a message broker, such as Apache ActiveMQ or IBM MQ, available before you configure this step.
* This step supports JMS 2.0 and requires [Apache ActiveMQ Artemis](https://activemq.apache.org/artemis/).
* If you need to use JMS 1.1 with ActiveMQ or Artemis, use the previous versions of the JMS Consumer and JMS Producer steps, also available in Pentaho version 8.1 and earlier.
* Place the IBM MQ client JAR for IBM MQ middleware in the following directories:

  * On the PDI client: `data-integration/plugins/pentaho-streaming-jms-plugin/lib`
  * On the Pentaho Server: `server/pentaho-server/pentaho-solutions/system/karaf/deploy`

  You need to locate the WebSphere® MQ classes for the JMS Java library from your IBM WebSphere® MQ installation. You can also find this library in your [IBM WebSphere MQ Client SupportPac](https://idaas.iam.ibm.com/idaas/mtfim/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:basicldapuser). The WebSphere® MQ Java library version that the PDI plugin steps were built against is 9.4.0.0. The library that you must have available for distribution into the PDI JMS plugin is `com.ibm.mq.allclient-9.4.0.0.jar`.  Because IBM licensing prevents us from distributing the library directly, you must add it to your PDI directories.&#x20;
* Place the JMS Library jar for the `ConnectionFactory` and other supporting classes in the following directories:
  * On the PDI client: `data-integration/plugins/pentaho-streaming-jms-plugin/lib`
  * On the Pentaho Server: `server/pentaho-server/pentaho-solutions/system/karaf/deploy`
* Set the OPT environment variable for your operating system.
  * **Linux or Unix**
    1. In a text editor, open the `...\data-integration\spoon.sh` file.
    2. Locate the line that defines the `OPT` variable:

       ```bat
       OPT="$OPT $PENTAHO_DI_JAVA_OPTIONS
       ```
    3. Append the following JVM option to the end of that line:&#x20;

       ```shellscript
       -Dcom.ibm.mq.cfg.useIBMCipherMappings=false
       ```
    4. Save and close the `...\data-integration\spoon.sh` file.
  * **Windows**
    1. In a text editor, open the `...\data-integration\Spoon.bat` file.
    2. Locate the line that defines the `OPT` variable:

       ```bat
       set OPT=%OPT% %PENTAHO_DI_JAVA_OPTIONS%
       ```
    3. Append the following JVM option to the end of that line:

       ```batch
       "-Dcom.ibm.mq.cfg.useIBMCipherMappings=false"
       ```
    4. Save and close the `...\data-integration\Spoon.bat` file.
