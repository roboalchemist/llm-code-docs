# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/schedule-reports/schedule-a-report/quartz-cron-attributes.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/schedule-a-report/quartz-cron-attributes.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/schedule-a-report/quartz-cron-attributes.md

# Quartz cron attributes

The Quartz cron engine supports a seven-attribute time declaration with many possible values. The number format is the same for every expression, even if the values are different: it must be listed as seconds, minutes, hours, day of month, month, day of week, then the year. A space separates each attribute.

These are the possible values for each attribute: 0 to 59 for seconds and minutes, 0 to 23 for hours, 1 to 31 for days, 1 to 12 for months, 1 to 7 for day of week, and a four-digit year. Alternatively, you can use three-letter values for the day of week (SUN, MON, TUE, WED, THU, FRI, SAT). However, three-letter values for the month (JAN, FEB, etc.) are not supported. For months, use numbers 1-12.

An Asterisk (\*) indicates "all values," so an asterisk in the minute field would mean that the report runs once every minute. You can specify a range of values with the Dash (-) operator, and you can specify multiple individual values with a comma. If you need to omit a value in the day of month and day of week field from a cron job, you can use the Question Mark (?) character to indicate that this value does not matter. If you need to split values, you can do so with the Slash (/) character: this operator literally means "every," so 0/15 would mean "Every 15." In the day of month field, you can use the Hashtag (#) character to indicate a certain instance of a day of the month. For example, the second Friday of the month would be 6#2.

You can use a capital L in the day of month and day of week field to indicate "Last," as in the last day of the week or month. A capital W in the day of month attribute means "Weekday," which only encompasses Monday through Friday. The W character can only be specified when the day-of-month is a single day, not a range or list of days.

Most of these values can be combined to accommodate unusual cron schedules.

| Attribute    | Conditionals and Operators |
| ------------ | -------------------------- |
| Seconds      | , - \* /                   |
| Minutes      | , - \* /                   |
| Hours        | , - \* /                   |
| Day of month | , - \* ? / L W             |
| Month        | , - \* /                   |
| Day of week  | , - \* ? / L #             |
| Year         | , - \* /                   |

Here is how you would execute a report at 10:15 AM on the last Friday of every month.

```
0 15 10 ? * 6L *
```
