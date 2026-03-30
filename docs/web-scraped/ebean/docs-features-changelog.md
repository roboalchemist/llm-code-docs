# Source: https://ebean.io/docs/features/changelog

Title: ChangeLog | Ebean

URL Source: https://ebean.io/docs/features/changelog

Markdown Content:
Overview
--------

Change log provides a built-in mechanism for logging changes (insert, update and delete events). There are 4 interfaces that we can optionally implement to control the various parts of the mechanism. By default, we can annotate entity beans with `@ChangeLog` and get the changes logged in JSON format to a logger.

There is overlap with `@History` which is a database centric approach. Unlike `@ChangeLog``@History` is transactional and can NOT be bypassed.

Caveats
-------

SqlUpdate, CallableSql and bulk updates via Update are not included in the change log.

Getting started
---------------

### Step 1: Decide default for inserts

Inserts can default to being included in the change log or not and this will depend on the application. It is good to think about this up front as when we annotate the entity beans with @ChangeLog we can choose to override the default behaviour.

By default inserts are included. `DatabaseConfig.setChangeLogIncludeInserts(boolean)` can be used to control the default behaviour. This can also be set via application.properties.

ebean.changeLogIncludeInserts=false

### Step 2: Add @ChangeLog

Add `@ChangeLog` annotation to all the entity beans that should have change logging on.

@ChangeLog
@Entity
public class Address {
...

/**
 * Only include updates if specific properties are changed.
 */
@ChangeLog(updatesThatInclude = {"name","dateOfBirth"})
@Entity
public class Customer {
...

/**
 * Override the default behaviour for inserts - INCLUDE, EXCLUDE or DEFAULT.
 * In this case exclude inserts from the change log.
 */
@ChangeLog(inserts = ChangeLogInsertMode.EXCLUDE)
@Entity
public class Customer {
...

### Step 3: Implement ChangeLogPrepare

If we skip this step and don't supply a ChangeLogPrepare implementation a 'no op' implementation is used and the user context information (user id, user ip address etc) is left unpopulated.

Typically we implement ChangeLogPrepare obtaining the user context information such as user id and user ip address, setting that on the change set. Returning true indicates that the processing continues and the changeSet is passed to the ChangeLogListener in a background thread.

If we want logging to occur in the foreground we can invoke the logging in prepare method and return false (and this means the change set is not passed to the ChangeLogListener in a background thread).

class MyChangeLogPrepare implements ChangeLogPrepare {

  @Override
  public boolean prepare(ChangeSet changes) {

    // get user context information typically from a
    // ThreadLocal or similar mechanism

    String currentUserId = ...;
    changes.setUserId(currentUserId);

    String userIpAddress = ...;
    changes.setUserIpAddress(userIpAddress);

    changes.setSource("myApplicationName");

    // add arbitrary user context information to the
    // userContext map
    changes.getUserContext().put("some", "thing");

    return true;
  }
}

### Step 4: Register ChangeLogPrepare implementation

The implementation of ChangeLogPrepare can be automatically detected if classpath scanning is on (just like entity beans are found). That is, if scanning is on we don't need to explicitly register the ChangeLogPrepare implementation and instead it will be found and instantiated.

If scanning is not used or the ChangeLogPrepare implementation has dependencies and its instantiation should be performed externally to Ebean then we register it explicitly with DatabaseConfig.

// example code explicitly registering the ChangeLogPrepare implementation

MyChangeLogPrepare changeLogPrepare = ...;

DatabaseConfig config = new DatabaseConfig();
...
// register explicitly here
config.setChangeLogPrepare(changeLogPrepare);

Database database = DatabaseFactory.create(config);
...

### Step 5: Configure logging

The default implementation of ChangeLogListener logs events to `io.ebean.ChangeLog`. Typically, we would look to configure logging such that these logs go to a separate log.

Below in logback xml configuration an appender `CHANGE_LOG` for logging the change events to this separate log.

<appender name="CHANGE_LOG" class="ch.qos.logback.core.rolling.RollingFileAppender">
  <File>log/changeLog.log</File>
  <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
    <FileNamePattern>log/changeLog.log.%d{yyyy-MM-dd}</FileNamePattern>
    <MaxHistory>90</MaxHistory>
  </rollingPolicy>
  <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
    <pattern>%d{HH:mm:ss.SSS} %msg%n</pattern>
  </encoder>
</appender>

<logger name="io.ebean.ChangeLog" level="TRACE" additivity="false">
  <appender-ref ref="CHANGE_LOG"/>
</logger>
