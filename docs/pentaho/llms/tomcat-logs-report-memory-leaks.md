# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp/pentaho-server-issues/tomcat-logs-report-memory-leaks.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-server-issues/tomcat-logs-report-memory-leaks.md

# Tomcat logs report memory leaks

When shutting down Tomcat, you may see some SEVERE-level warnings similar to the following messages:

```xml
Dec 17, 2010 10:18:19 AM org.apache.catalina.loader.WebappClassLoader clearReferencesJdbc
SEVERE: The web application [/pentaho] registered the JBDC driver [mondrian.olap4j.MondrianOlap4jDriver] but failed to unregister it when the web application was stopped. To prevent a memory leak, the JDBC Driver has been forcibly unregistered.
Dec 17, 2010 10:18:19 AM org.apache.catalina.loader.WebappClassLoader clearReferencesThreads
SEVERE: The web application [/pentaho] appears to have started a thread named [HSQLDB Timer @49cf9f] but has failed to stop it. This is very likely to create a memory leak.
Dec 17, 2010 10:18:19 AM org.apache.catalina.loader.WebappClassLoader clearReferencesThreads
SEVERE: The web application [/pentaho] appears to have started a thread named [MySQL Statement Cancellation Timer] but has failed to stop it. This is very likely to create a memory leak.
Dec 17, 2010 10:18:19 AM org.apache.catalina.loader.WebappClassLoader clearThreadLocalMap
SEVERE: The web application [/pentaho] created a ThreadLocal with key of type [java.lang.InheritableThreadLocal] (value [java.lang.InheritableThreadLocal@a1320e]) and a value of type [org.pentaho.platform.engine.security.session.TrustedSystemStartupSession] (value [org.pentaho.platform.engine.security.session.TrustedSystemStartupSession@111089b]) but failed to remove it when the web application was stopped. This is very likely to create a memory leak.
```

These warnings report problems with processes that are being removed while the Tomcat server is shutting down. However, they can be significant if you are restarting or redeploying the Pentaho Server web applications.

To avoid memory leak issues in redeployment, you should restart Tomcat rather than redeploying or restarting the web application with a live server.
