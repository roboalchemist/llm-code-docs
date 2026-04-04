# Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging

Title: Configuring Audit Logging :: Open Identity Platform Documentation

URL Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging

Markdown Content:
OpenAM supports the following types of audit event handlers:

OpenAM Audit Event Handlers| Audit Event Handler Type | Publishes to | How to Configure |
| --- | --- | --- |
| CSV | CSV files | ["Configuring CSV Audit Event Handlers"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#configuring-csv-audit-event-handlers) |
| Syslog | The syslog daemon | ["Configuring Syslog Audit Event Handlers"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#configuring-syslog-audit-event-handlers) |
| JDBC | A relational database | ["Implementing JDBC Audit Event Handlers"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#implementing-jdbc-audit-event-handlers) |
| Elasticsearch | An Elasticsearch store | ["Implementing Elasticsearch Audit Event Handlers"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#implementing-elasticsearch-audit-event-handlers) |
| JMS | JMS topics | ["Configuring JMS Audit Event Handlers"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#configuring-jms-audit-event-handlers) |

This section provides procedures for configuring each type of audit handler.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#configuring-csv-audit-event-handlers)Configuring CSV Audit Event Handlers

OpenAM’s default audit event handler is the comma-separated values (CSV) handler, which is already configured for the global Audit Logging Service. The global configuration is used to control audit logging in realms that do not have the Audit Logging Service added to them.

The following procedure describes how to configure a CSV audit event handler:

To Configure a CSV Audit Event Handler

1.   Log in to the OpenAM console as an administrator, navigate to Configure > Global Services, and then click Audit Logging.

2.   In the Event Handler Instances table, click Global CSV Handler.

3.   Under General Handler Configuration, verify that the Enabled box is checked.

4.   Select the topics for your audit logs. For a description of each topic, see ["Audit Log Topics"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#audit-log-topics).

5.   In the Log Directory field, override the default location of your logs if necessary. The default location is: `%BASE_DIR%/%SERVER_URI%/log/`.

It is very important that a different log directory be configured for each instance of the CSV audit event handler. If two instances are writing to the same file, it can interfere with log rotation and tamper-evident logs. 
6.   For File Rotation, configure how files are rotated once they reach a specified file size or time interval. Enter the following parameters:

    1.   For Rotation Enabled, keep the Enabled box check-marked. If disabled, OpenAM ignores log rotation and appends to the same file.

    2.   For Maximum File Size, enter the maximum size of an audit file before rotation.

Default: 100000000 bytes.

    3.   OPTIONAL. For File Rotation Prefix, enter an arbitrary string that will be prefixed to every audit log to identify it. This parameter is used when time-based or size-based rotation is enabled.

    4.   For File Rotation Suffix, enter a timestamp suffix based on the Java SimpleDateFormat that will be added to every audit log. This parameter is used when time-based or size-based log rotation is enabled.

Default: `-MM.dd.yy-kk.mm`.

    5.   For Rotation Interval, enter a time interval to trigger audit log file rotation in seconds. A negative or zero value disables this feature.

Default: -1

Any combination of the three rotation policies (maximum file size, periodic duration, and duration since midnight) can be implemented including none at all. 
    6.   For Rotation Times, enter a time duration after midnight to trigger file rotation, in seconds. For example, you can provide a value of `3600` to trigger rotation at 1:00 AM.

Negative durations are not supported. 

7.   For File Retention, determine how long log files should be retained in your system. Configure the following file retention parameters:

    1.   For Maximum Number of Historical Files, enter a number for allowed backup audit files.

Default: `-1`, which indicates an unlimited number of files and disables the pruning of old history files.

    2.   For Maximum Disk Space, enter the maximum amount of disk space that the total number of audit files can store. A negative or zero value indicates that this policy is disabled.

Default: `-1`, which indicates an unlimited amount of disk space.

    3.   For Minimum Free Space Required, enter the minimum amount of disk space required to store audit files. A negative or zero value indicates that this policy is disabled.

Default: `-1`, which indicates no minimum amount of disk space is required.

8.   For Buffering, configure if log events should be buffered in memory before they are written to the CSV file:

    1.   For Buffering Enabled, click the Enabled box to start audit event buffering.

The default buffer size is 5000 bytes.

When buffering is enabled, all audit events are put into an in-memory buffer (one per handled topic), so that the original thread that generated the event can fulfill the requested operation, rather than wait for I/O to complete. A dedicated thread (one per handled topic) constantly pulls events from the buffer in batches and writes them to the CSV file. If the buffer becomes empty, the dedicated thread goes to sleep until a new item gets added.

    2.   For Flush Each Event Immediately, click Enabled to write all buffered events before flushing.

When the dedicated thread accesses the buffer, it copies the contents to an array to reduce contention, and then iterates through the array to write to the CSV file. The bytes written to the file can be buffered again in Java classes and the underlying operating system.

When Flush Each Event Immediately is enabled, OpenAM flushes the bytes after each event is written. If the feature is disabled (default), the Java classes and underlying operation system determine when to flush the bytes.

9.   For Tamper Evident Configuration, set up the feature to detect any tampering of the audit logs.

When tamper evident logging is enabled, OpenAM generates an HMAC digest for each audit log event and inserts it into each audit log entry. The digest detects any addition or modification to an entry.

OpenAM also supports another level of tamper evident security by periodically adding a signature entry to a new line in each CSV file. The entry signs the preceding block of events, so that verification can establish if any of these blocks have been added, removed, or edited by some user.

    1.   Click Is Enabled to turn on the tamper evident feature for CSV logs.

    2.   In the Certificate Store Location field, enter the location of the keystore. You must manually create the keystore and place it in this location. You can use a simple script to create your Java keystore: [create-keystore.sh](https://doc.openidentityplatform.org/openam/_attachments/create-keystore.sh).

Default: `%BASE_DIR%/%SERVER_URI%/Logger.jks`

    3.   In the Certificate Store Password field, enter the certificate password.

    4.   In the Certificate Store Password (confirm), re-enter the certificate password.

    5.   In the Signature Interval field, enter a value in seconds for OpenAM to generate and add a new signature to the audit log entry.

Default: `900` (seconds)

10.   In the Audit Event Handler Factory field, keep the default class name for the audit event handler.

11.   Click Add to save your changes.

12.   On the Audit Logging page, click Save.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#configuring-syslog-audit-event-handlers)Configuring Syslog Audit Event Handlers

OpenAM can publish audit events to a syslog server, which is based on a widely-used logging protocol. You can configure your syslog settings on the OpenAM console.

The following procedure describes how to configure a Syslog audit event handler:

To Configure a Syslog Audit Event Handler

1.   Log in to the OpenAM console as an administrator, navigate to Configure > Global Services, and then click Audit Logging.

2.   In the Event Handler Instances section, click New.

3.   On the Select Audit Event Handler page, click Syslog, and then click Next.

4.   On the Add Audit Event Handler page, enter a name for your event handler. For example, `Syslog Audit Event Handler`.

5.   Under General Handler Configuration, verify that the Enabled box is checked.

6.   Select the topics for your audit logs. For a description of each topic, see ["Audit Log Topics"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#audit-log-topics).

7.   In the Server hostname field, enter the hostname or IP address of the receiving syslog server.

8.   In the Server port field, enter the port of the receiving syslog server.

9.   Select the Transport protocol for your configuration: `TCP` or `UDP`.

10.   In the Connection timeout field, enter the number of seconds to connect to the syslog server. If the server has not responded in the specified time, a connection timeout occurs.

11.   Select the syslog facility.

A syslog message includes a PRI field that is calculated from the facility and severity values. All topics set the severity to `INFORMATIONAL` but allow you to choose the facility:

Syslog Facilities| Facility | Description |
| --- | --- |
| AUTH | Security or authorization messages |
| AUTHPRIV | Security or authorization messages |
| CLOCKD | Clock daemon |
| CRON | Scheduling daemon |
| DAEMON | System daemons |
| FTP | FTP daemon |
| KERN | Kernel messages |
| LOCAL0 | Local use 0 (local0) |
| LOCAL1 | Local use 1 (local1) |
| LOCAL2 | Local use 2 (local2) |
| LOCAL3 | Local use 3 (local3) |
| LOCAL4 | Local use 4 (local4) |
| LOCAL5 | Local use 5 (local5) |
| LOCAL6 | Local use 6 (local6) |
| LOCAL7 | Local use 7 (local7) |
| LOGALERT | Log alert |
| LOGAUDT | Log audit |
| LPR | Line printer subsystem |
| MAIL | Mail system |
| NEWS | Network news subsystem |
| NTP | Network time protocol |
| SYSLOG | Internal messages generated by syslogd |
| USER | User-level messages |
| UUCP | Unix-to-unix-copy (UUCP) subsystem |
12.   In the Audit Event Handler Factory field, keep the default class name for the audit event handler.

13.   For Buffering Enabled, click the Enabled box to start audit event buffering.

When buffering is enabled, all audit events that get generated are formatted as syslog messsages and put into a queue. A dedicated thread constantly pulls events from the queue in batches and transmits them to the syslog server. If the queue becomes empty, the dedicated thread goes to sleep until a new item gets added. The default queue size is 5000.

14.   Click Add to save your settings.

15.   On the Audit Logging page, click Save.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#implementing-jdbc-audit-event-handlers)Implementing JDBC Audit Event Handlers

OpenAM supports audit logging to relational databases using the JDBC audit event handler. You can configure OpenAM to write to Oracle, MySQL, or other databases.

Before configuring the JDBC audit event handler, you must perform several steps to allow OpenAM to log to the database:

To Prepare for JDBC Audit Logging

1.   Create tables in the relational database in which you will write the audit logs. The SQL for Oracle and MySQL table creation is in the `audit.sql` file under `/path/to/tomcat/webapps/openam/WEB-INF/template/sql/db-type`.

If you are using a different relational database, tailor the Oracle or MySQL `audit.sql` file to conform to your database’s SQL syntax.

2.   JDBC audit logging requires a database user with read and write privileges for the audit tables. Do one of the following:

    *   Identify an existing database user and grant that user privileges for the audit tables.

    *   Create a new database user with read and write privileges for the audit tables.

3.   Obtain the JDBC driver from your database vendor. Place the JDBC driver `.zip` or `.jar` file in the container’s `WEB-INF/lib` classpath. For example, place the JDBC driver in `/path/to/tomcat/webapps/openam/WEB-INF/lib` if you use Apache Tomcat.

The following procedure describes how to configure a JDBC audit event handler. Perform the following steps after you have created audit log tables in your database and installed the JDBC driver in the OpenAM web container:

To Configure a JDBC Audit Event Handler

1.   Log in to the OpenAM console as an administrator, navigate to Configure > Global Services, and then click Audit Logging.

2.   In the Event Handler Instances section, click New.

3.   On the Select Audit Event Handler page, click JDBC, and then click Next.

4.   On the Add Audit Event Handler page, enter a name for your event handler. For example, `JDBC Audit Event Handler`.

5.   Under General Handler Configuration, verify that the Enabled box is checked.

6.   Select the topics for your audit logs. For a description of each topic, see ["Audit Log Topics"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#audit-log-topics).

7.   For Database Type, click one of the following:

    *   Oracle

    *   MySQL

    *   Other

8.   For JDBC Database URL, enter the URL for your database server. For example, `jdbc:oracle:thin@//host.example.com:1521/ORCL`.

9.   In the Database Driver Name field, enter the classname of the driver to connect to the datbase. For example, `oracle.jdbc.driver.OracleDriver` or `com.mysql.jdbc.Driver`.

10.   In the Database Username field, enter the username to authenticate to the database server.

This user must have read and write privileges for the audit tables.

11.   In the Database User Password field, enter the password used to authenticate to the database server. Then, re-enter the password in the Database User Password (confirm) field.

12.   In the Connection Timeout (seconds) field, enter the maximum wait time before failing the connection.

Default: 30 (seconds)

13.   In the Maximum Connection Idle Timeout (seconds) field, enter the maximum idle time in seconds before the connection is closed.

Default: 600 (seconds)

14.   In the Maximum Connection Time (seconds) field, enter the maximum time in seconds for a connection to stay open.

Default: 1800 (seconds)

15.   In the Minimum Idle Connections field, enter tne minimum number of idle connections allowed in the connection pool.

16.   In the Maximum Connections field, enter the maximum number of connections in the connection pools.

17.   In the Factory Class Name, enter the fully qualified class name of your custom JDBC audit event handler.

18.   Click Add to save your changes.

19.   On the Audit Logging page, click Save.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#implementing-elasticsearch-audit-event-handlers)Implementing Elasticsearch Audit Event Handlers

OpenAM supports audit logging to Elasticsearch 5.0. When you store OpenAM’s audit logs in an Elasticsearch data store, you can use Kibana to perform data discovery and visualization on your logs.

You can experiment with an Elasticsearch audit handler without enabling any Elasticsearch security features. However, for a more secure deployment, Open Identity Platform Community recommends that you use Elasticsearch Shield to require authentication to Elasticshield. Depending on your network topology, you might also want to configure SSL for Elasticsearch Shield.

Before configuring the Elasticsearch audit event handler, you must configure an Elasticsearch index with OpenAM’s audit schema:

To Prepare for Elasticsearch Audit Logging

Perform the following steps to prepare an Elasticsearch instance for storing OpenAM audit events.

These steps apply to Elasticsearch 5.0 only. Breaking changes in Elasticsearch 6.0 make it incompatible with the schemas provided in this version of OpenAM.

1.   Review the JSON file containing OpenAM’s audit schema. You can find the JSON file for the audit schema at the path `/path/to/tomcat/webapps/openam/WEB-INF/template/elasticsearch/audit.json`.

2.   Copy the `audit.json` file to the system where you will create the Elasticsearch index for OpenAM auditing.

In this example, you create an Elasticsearch index by executing an Elasticsearch REST API call using the `curl` command. Copy the `audit.json` file to a location that is accessible to the `curl` command you will run in the next step.

3.   Create an Elasticsearch index for OpenAM auditing as follows:

```
$ curl \
 --request POST \
 --header "Content-Type: application/json" \
 --data @audit.json \
 http://elasticsearch.example.com:9200/my_openam_audit_index
``` 
In this example, note the following:

    *   `elasticsearch.example.com` is the name of the host on which Elasticsearch runs.

    *   `9200` is the port number that you use to access Elasticsearch’s REST API.

    *   `my_openam_audit_index` is the name of the Elasticsearch index that you want to create.

To Configure an Elasticsearch Audit Event Handler

The following procedure describes how to configure an Elasticsearch audit event handler. Perform the following steps after you have created an Elasticsearch index for OpenAM audit logging:

1.   If your Elasticsearch deployment uses Elasticsearch Shield configured for SSL, import the CA certificate used to sign Elasticsearch node certificates into the Java keystore on the host that runs OpenAM. For example:

```
$ keytool \
 -import \
 -trustcacerts \
 -alias elasticsearch \
 -file /path/to/cacert.pem \
 -keystore $JAVA_HOME/jre/lib/security/cacerts
``` 
If you are running an OpenAM site, import the CA certificate on all the servers in your site.

2.   Log in to the OpenAM console as an administrator, navigate to Configure > Global Services, and then click Audit Logging.

3.   In the Event Handler Instances section, click New.

4.   On the Select Audit Event Handler page, click Elasticsearch, and then click Next.

5.   On the Add Audit Event Handler page, enter a name for your event handler. For example, `Elasticsearch Event Handler`.

6.   Under General Handler Configuration:

    1.   Verify that the Enabled box is checked.

    2.   Select the topics for your audit logs. For a description of each topic, see ["Audit Log Topics"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#audit-log-topics).

7.   Under Elasticsearch Configuration:

    1.   In the Server Hostname field, enter the hostname or IP address of the Elasticsearch server to which OpenAM should connect when writing audit logs.

    2.   In the Server Port field, enter the port number to access Elasticsearch’s REST API. The default port number is 9200.

    3.   If SSL is enabled in your Elasticsearch deployment, click the Enabled check box for SSL Enabled.

    4.   In the Elasticsearch Index field, specify the name of the index to be used for OpenAM audit logging. The index you specify in this field must be identical to the index you created in ["To Prepare for Elasticsearch Audit Logging"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#prepare-audit-logging-elasticsearch).

8.   If you have configured Elasticsearch Shield for user authentication, specify the name and password of an Elasticsearch user in the Username and Password fields under Authentication.

If you are not using Elasticsearch Shield for user authentication, you can leave these fields blank.

9.   Under Buffering, configure whether log events should be buffered in memory before they are written to the Elasticsearch data store:

    1.   For Buffering enabled, click the Enabled box to start audit event buffering.

When buffering is enabled, all audit events are put into an in-memory buffer (one per handled topic), so that the original thread that generated the event can fulfill the requested operation, rather than wait for I/O to complete. A dedicated thread (one per handled topic) constantly pulls events from the buffer in batches and writes them to Elasticsearch. If the buffer becomes empty, the dedicated thread goes to sleep until a new item gets added.

    2.   For Batch Size, specify the number of audit events that OpenAM pulls from the audit buffer when writing a batch of events to Elasticsearch. The default is 500 audit events.

    3.   For Queue Capacity, specify the maximum number of audit events that OpenAM can queue in this audit handler’s buffer. The default is 10000 audit events.

If the number of events to queue exceeds the queue capacity, OpenAM raises an exception and the excess audit events are dropped, and therefore not written to Elasticsearch.

    4.   For Write interval, specify how often OpenAM should write buffered events to Elasticsearch. The default interval is 250 milliseconds.

10.   In the Factory Class Name field under Audit Event Handler Factory, keep the default class name for the audit event handler.

11.   Click Add to add the Elasticsearch audit logging event handler to the Audit Logging Service.

12.   On the Audit Logging page, click Save to save your changes to the Audit Logging Service.

If you have configured the audit logging event handler correctly, OpenAM starts logging to Elasticsearch immediately after you have saved your changes to the Audit Logging Service.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#configuring-jms-audit-event-handlers)Configuring JMS Audit Event Handlers

OpenAM supports audit logging to a JMS message broker. JMS is a Java API for sending messages between clients using a publish and subscribe model as follows:

*   OpenAM audit logging to JMS requires that the JMS message broker supports using JNDI to locate a JMS connection factory. See your JMS message broker documentation to verify that you can make connections to your broker by using JNDI before attempting to implement an OpenAM JMS audit handler.

*   OpenAM acts as a JMS publisher client, publishing JMS messages containing audit events to a JMS _topic_. [[1](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#_footnotedef_1 "View footnote.")]

*   A JMS subscriber client, which is not part of the OpenAM software and must be developed and deployed separately from OpenAM, subscribes to the JMS topic to which OpenAM publishes audit events. The client then receives the audit events over JMS and processes them as desired.

Before configuring the JMS audit event handler, you must perform several steps to allow OpenAM to publish audit events as a JMS client:

To Prepare for JMS Audit Logging

1.   Obtain JNDI connection properties that OpenAM requires to connect to your JMS message broker. The specific connection properties vary depending on the broker. See your JMS message broker documentation for details.

For example, connecting to an Apache ActiveMQ message broker requires the following properties:

Example Apache ActiveMQ JNDI Connection Properties| Property Name | Example Value |
| --- | --- |
| `java.naming.factory.initial` | `org.apache.activemq.jndi.ActiveMQInitialContextFactory` |
| `java.naming.provider.url` | `tcp://localhost:61616` |
| `topic.audit` | `audit` |
2.   Obtain the JNDI lookup name of the JMS connection factory for your JMS message broker.

For example, for Apache ActiveMQ, the JNDI lookup name is `ConnectionFactory`.

3.   Obtain the JMS client `.jar` file from your JMS message broker vendor. Add the `.jar` file to OpenAM’s classpath by placing it in the `WEB-INF/lib` directory.

For example, place the JMS client `.jar` file in `/path/to/tomcat/webapps/openam/WEB-INF/lib` if you use Apache Tomcat.

The following procedure describes how to configure a JMS audit event handler.

If your JMS message broker requires an SSL connection, you might need to perform additional, broker-dependent configuration tasks. For example, you might need to import a broker certificate into OpenAM’s keystore, or provide additional JNDI context properties.

See your JMS message broker’s documentation for specific requirements for making SSL connections to your broker, and implement them as needed in addition to the steps in the following procedure.

Perform the following steps after you have installed the JMS client `.jar` file in the OpenAM web container:

To Configure a JMS Audit Event Handler

1.   Log in to the OpenAM console as an administrator, navigate to Configure > Global Services, and then click Audit Logging.

2.   In the Event Handler Instances section, click New.

3.   On the Select Audit Event Handler page, click JMS, and then click Next.

4.   On the Add Audit Event Handler page, enter a name for your event handler. For example, `JMS Event Handler`.

5.   Under General Handler Configuration:

    1.   Verify that the Enabled box is checked.

    2.   Select the OpenAM event handler topics[[1](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#_footnotedef_1 "View footnote.")] for your audit logs. For a description of OpenAM event handler topics, see ["Audit Log Topics"](https://doc.openidentityplatform.org/openam/admin-guide/chap-audit-logging#audit-log-topics).

6.   Under JMS Configuration:

    1.   In the Delivery Mode field, specify the JMS delivery mode.

With persistent delivery, the JMS provider ensures that messages are not lost in transit in case of a provider failure by logging messages to storage when they are sent. Therefore, persistent delivery mode guarantees JMS message delivery, while non-persistent mode provides better performance.

The default delivery mode is non-persistent delivery. Therefore, if your deployment requires delivery of every audit event to JMS subscriber clients, be sure to set the default configuration to `PERSISTENT`.

    2.   For Session Mode, use the default setting, `AUTO`, unless your JMS broker implementation requires otherwise. See your broker documentation for more information.

    3.   Specify properties that OpenAM will use to connect to your JMS message broker as key-value pairs in the JNDI Context Properties field. The format for properties is `[myPropertyName]=myPropertyValue`. For example, `[java.naming.provider.url]=tcp://localhost:61616`.

    4.   Specify the name of the JMS topic to which OpenAM will publish messages containing audit events.

Subscriber clients that process OpenAM audit events must subscribe to this topic.

    5.   Specify the JNDI lookup name of the JMS connection factory in the JMS Connection Factory Name field.

7.   Under Batch Events, configure whether log events should be batched before they are published to the JMS message broker:

    1.   For Batch enabled, click the Enabled box to start batch publishing of audit events. Audit events will be queued and published to the JMS message broker in batches.

If batch publishing is not enabled, OpenAM publishes audit events to the JMS message broker individually.

    2.   For Capacity, specify the maximum capacity of the publishing queue. Execution is blocked if the queue size reaches capacity.

    3.   For Max Batched, specify the maximum number of events to be delivered when OpenAM publishes the events to the JMS message broker.

    4.   For Thread Count, specify the number of worker threads OpenAM should use to process the batch queue.

    5.   Specify the batching timeout configuration as follows:

        *   For Insert Timeout, specify the amount of time, in seconds, for queued events to be transmitted to the JMS message broker.

        *   For Polling Timeout, specify the amount of time, in seconds, that worker threads wait for new audit events before becoming idle.

        *   For Shutdown Timeout, specify the amount of time, in seconds, that worker threads wait for new audit events before shutting down.

8.   In the Factory Class Name field under Audit Event Handler Factory, keep the default class name for the audit event handler.

9.   Click Add to add the JMS audit logging event handler to the Audit Logging Service.

10.   On the Audit Logging page, click Save to save your changes to the Audit Logging Service.

If you have configured the audit logging event handler correctly, OpenAM starts logging to JMS immediately after you have saved your changes to the Audit Logging Service.
