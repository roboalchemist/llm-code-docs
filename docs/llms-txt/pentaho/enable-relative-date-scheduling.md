# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/schedule-reports/set-relative-date-schedules/enable-relative-date-scheduling.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/set-relative-date-schedules/enable-relative-date-scheduling.md

# Enable relative date scheduling

Perform the following steps to enable relative date scheduling:

1. Navigate to the `server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes` directory and open the `classic-engine.properties` file with any text editor.
2. Add the following parameters to the `classic-engine.properties` file:

   | Parameter                                                                     | Description                                                                       |
   | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
   | `org.pentaho.reporting.engine.classic.core.scheduler.startDateRangeParamName` | The report parameter for the start of the date range.                             |
   | `org.pentaho.reporting.engine.classic.core.scheduler.endDateRangeParamName`   | The report parameter for the end of the date range.                               |
   | `org.pentaho.reporting.engine.classic.core.scheduler.fiscalYearStart`         | The report parameter for the first day of the fiscal year (Default is January 1). |
3. Save and close the `classic-engine.properties` file.
4. Restart the Pentaho Server.

Relative date scheduling is enabled.
