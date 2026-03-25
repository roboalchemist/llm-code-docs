# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration/debug-plugins.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration/debug-plugins.md

# Debug plugins

A good way to debug PDI plugins is to deploy the plugin, launch the PDI client, and connect the debugger to the PDI client JVM. This section explains how to debug a plugin in Eclipse.

1. Prepare the PDI client for debugging by starting the PDI client JVM, which allows debug sessions and these types of arguments to be passed into the PDI client JVM.

   ```java
   -Xdebug -Xnoagent -Djava.compiler=NONE -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=1044
   ```

   The address argument can be any free port on your machine. This example uses port `1044`.

   If you are using `Spoon.bat` or `spoon.sh` to launch the PDI client, create a copy of the file and edit it to include the debugging parameters to the Java options near the bottom of the file. If you are using a Mac app, add the JVM parameters to `VMOptions key of “Data Integration 64-bit.app/Contents/Info.plist”` or `“Data Integration 32-bit.app/Contents/Info.plist”` respectively.

   When you start PDI client, debuggers connect on port 1044.
2. Launch a debug session.
   1. Ensure that the PDI client is set up for debugging and running with the plugin deployed.
   2. Connect the Eclipse debugger by creating a debug configuration for your plugin project. From the **Run/Debug Configurations** menu, create a new configuration for **Remote Java Application.**
   3. Select your project, making sure the port matches the port configured in Step 1
   4. Decide whether you want to be able to kill the PDI client JVM from the debugger, then click **Apply** and **Debug**.

The debugger opens, stops at the breakpoints you set, and in-line editing of the plugin source is enabled.

![Eclipse debug dialog box](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-9b92b87d0eb8619877c47e182ee13c9a76c27865%2FExtend_Pentaho_Data_Integration_Eclipse_debug_dialog.png?alt=media)
