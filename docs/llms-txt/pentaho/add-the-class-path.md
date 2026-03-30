# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/hadoop-libraries-are-missing/add-the-class-path.md

# Add the class path

The following command will add the libraries to the classpath:

```
export **SPARK\_DIST\_CLASSPATH**=$(hadoop classpath)
```

You can add this command to the `daemon.sh` file so you do not have run this command every time you the start the AEL daemon.
