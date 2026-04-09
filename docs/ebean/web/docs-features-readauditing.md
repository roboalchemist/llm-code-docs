# Source: https://ebean.io/docs/features/readauditing

Title: Read Auditing | Ebean

URL Source: https://ebean.io/docs/features/readauditing

Markdown Content:
Overview
--------

ReadAudit is a feature where read access is logged for auditing purposes. You can annotation entity beans with @ReadAudit and then read events on these beans (queries and hits in L2 cache) are logged.

An implementation of the ReadAuditPrepare interface is typically required. The readAuditPrepare.prepare() method is expected to populate the ReadEvent with user context information (user id, user ip address etc).

Limitations
-----------

SqlQuery queries are currently not logged to the read audit log (RawSql queries are included in read auditing).

Getting started
---------------

### Step 1: Add @ReadAudit

Add @ReadAudit annotation to all the entity beans that should have read auditing.

@ReadAudit
@Entity
@Table(name = "customer")
public class Customer {
...

### Step 2: Implement ReadAuditPrepare

If you skip this step and don't supply a ReadAuditPrepare implementation a 'no op' implementation is used and the user context information (user id, user ip address etc) is left unpopulated.

class MyReadAuditPrepare implements ReadAuditPrepare {

  @Override
  public void prepare(ReadEvent event) {

    // get user context information typically from a
    // ThreadLocal or similar mechanism

    String currentUserId = ...;
    event.setUserId(currentUserId);

    String userIpAddress = ...;
    event.setUserIpAddress(userIpAddress);

    event.setSource("myApplicationName");

    // add arbitrary user context information to the
    // userContext map
    event.getUserContext().put("some", "thing");
  }
}

### Step 3: Register ReadAuditPrepare implementation

The implementation of ReadAuditPrepare can be automatically detected if classpath scanning is on (just like entity beans are found etc). That is, if scanning is on you don't need to explicitly register the ReadAuditPrepare implementation and instead it will be found and instantiated.

If scanning is not used or the ReadAuditPrepare implementation has dependencies and its instantiation should be performed externally to Ebean then you can register it explicitly with the DatabaseConfig.

// example code explicitly registering the ReadAuditPrepare implementation

MyReadAuditPrepare readAuditPrepare = ...;

DatabaseConfig config = new DatabaseConfig();
...

// register explicitly here
config.setReadAuditPrepare(readAuditPrepare);

...
Database database = DatabaseFactory.create(config);

### Step 4: Configure logging

The default implementation of ReadAuditLogger logs query plan entries to `io.ebean.ReadAuditQuery` and read events to `io.ebean.ReadAudit`. The query plans contain the full SQL and having these logged separately means that the read events don't need to include the full SQL executed and instead the bean type and query key can be used to reference/lookup the associated SQL. This reduces the bulk/size of the read event logs.

Below in logback xml configuration is 2 appenders. `READAUDIT_QUERY_LOG` for logging the query plans and `READAUDIT_LOG` for logging the read bean events.

<!-- LOGBACK configuration: separate loggers for the read auditing -->

<appender name="READAUDIT_QUERY_LOG" class="ch.qos.logback.core.rolling.RollingFileAppender">
  <File>log/readAuditQuery.log</File>
  <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
    <FileNamePattern>log/readAuditQuery.log.%d{yyyy-MM-dd}</FileNamePattern>
    <MaxHistory>90</MaxHistory>
  </rollingPolicy>
  <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
    <pattern>%d{HH:mm:ss.SSS} %msg%n</pattern>
  </encoder>
</appender>

<appender name="READAUDIT_LOG" class="ch.qos.logback.core.rolling.RollingFileAppender">
  <File>log/readAudit.log</File>
  <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
    <FileNamePattern>log/readAudit.log.%d{yyyy-MM-dd}</FileNamePattern>
    <MaxHistory>90</MaxHistory>
  </rollingPolicy>
  <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
    <pattern>%d{HH:mm:ss.SSS} %msg%n</pattern>
  </encoder>
</appender>

<logger name="io.ebean.ReadAuditQuery" level="TRACE" additivity="false">
  <appender-ref ref="READAUDIT_QUERY_LOG"/>
</logger>

<logger name="io.ebean.ReadAudit" level="TRACE" additivity="false">
  <appender-ref ref="READAUDIT_LOG"/>
</logger>

Optional: ReadAuditLogger implementation
----------------------------------------

If the default logging does not suit you can implement ReadAuditLogger to control how the events are logged. Log to a message queue, direct to a data store etc.

Query.setDisableReadAuditing()
------------------------------

For a specific query you can explicitly exclude it from the read auditing. The typical use case for this is where the query is used internally in the application to populate a cache or process bulk data and where you don't want that to go into the read audit log.
