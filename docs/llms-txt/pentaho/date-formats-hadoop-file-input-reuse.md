# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/select-an-engine-hadoop-file-input/using-the-hadoop-file-input-step-on-the-pentaho-engine-cp/options-hadoop-file-input-reuse/fields-tab-hadoop-file-input-reuse/date-formats-hadoop-file-input-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hadoop-file-input-cp-main-page/options-hadoop-file-input-reuse/fields-tab-hadoop-file-input-reuse/date-formats-hadoop-file-input-reuse.md

# Date formats

Use the following table to specify date formats. For further information on valid date formats used in this step, view the [Date Formatting Table](http://wiki.pentaho.com/display/Reporting/Date+Formatting+Table).

| Letter | Date of Time Component | Presentation      | Examples                                       |
| ------ | ---------------------- | ----------------- | ---------------------------------------------- |
| G      | Era designator         | Text              | `AD`                                           |
| y      | Year                   | Year              | `1996` or `96`                                 |
| M      | Month in year          | Month             | `July`, `Jul`, or `07`                         |
| w      | Week in year           | Number            | `27`                                           |
| W      | Week in Month          | Number            | `2`                                            |
| D      | Day in year            | Number            | `189`                                          |
| d      | Day in month           | Number            | `10`                                           |
| F      | Day of week in month   | Number            | `2`                                            |
| E      | Day in week            | Text              | `Tuesday` or `Tue`                             |
| a      | am/pm marker           | Text              | `PM`                                           |
| H      | Hour in day (0-23)     | Number 0          | n/a                                            |
| k      | Hour in day (1-24)     | Number 24         | n/a                                            |
| K      | Hour in am/pm (0-11)   | Number 0          | n/a                                            |
| h      | Hour in am/pm (1-12)   | Number 12         | n/a                                            |
| m      | Minute in hour         | Number 30         | n/a                                            |
| s      | Second in minute       | Number 55         | n/a                                            |
| S      | Millisecond            | Number 978        | n/a                                            |
| z      | Time zone              | General time zone | `Pacific Standard Time`, `PST`, or `GMT-08:00` |
| Z      | Time zone              | RFC 822 time zone | `-0800`                                        |
