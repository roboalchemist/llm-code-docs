# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/amazon-emr/lzo-support.md

# LZO support

LZO is a compression format supported by Amazon EMR. It is required for running AEL on EMR. To configure for LZO compression, you will need to add several properties.

1. Follow the instructions available here to install the Linux LZO compression library from the command line: <https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.6.1/bk_command-line-installation/content/install_compression_libraries.html>
2. Navigate to the `data-integration/adaptive-execution/config/` directory and open the `application.properties` file.
3. Add the following properties:
   * `spark.executor.extraClassPath= /usr/lib/hadoop-lzo/lib/hadoop-lzo.jar`
   * `spark.driver.extraClassPath = /usr/lib/hadoop-lzo/lib/hadoop-lzo.jar`
4. Append the following properties to include `-Djava.library.path=/usr/lib/hadoop-lzo/lib/native` at the end of each line:
   * **sparkExecutorExtraJavaOptions**
   * **sparkDriverExtraJavaOptions**
5. Save and close the file.
