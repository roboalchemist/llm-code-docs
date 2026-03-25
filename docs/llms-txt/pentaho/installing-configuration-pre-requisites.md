# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/installing-configuration-pre-requisites.md

# Installing configuration pre-requisites

Before you can configure Pentaho Data Mastering, you must install the container that contains the following run-time pre-requisites:

* The Docker runtime
* The Docker-Compose tool
* Other system configurations (rsyslog config and other tools required by Pentaho Data Mastering containers)

**CAUTION:**

Do not run the following command to install the pre-requisites container more than one time. Running the command more than once creates duplicate files, which causes the Docker runtime to stop working.

Run the following command to install the pre-requisites container:

```
$ bash /opt/mdm/prerequisites.sh
```

After you have installed configuration pre-requisites, see [Setting environmental variables](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/setting-environmental-variables).
