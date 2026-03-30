# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/schedule-reports/set-relative-date-schedules/use-relative-date-scheduling.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/set-relative-date-schedules/use-relative-date-scheduling.md

# Use relative date scheduling

When you schedule a report that contains **startDate** and **endDate** parameters, the **Use Specific Date** (default) and **Use Relative Date** options display on the third panel of the scheduling wizard.

![New Schedule Use specific date dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-56face21d926d50133a404895f8ab2aa64a12792%2FPAZ%20New%20Schedule%20dialog%20box%20page3%20Specific.png?alt=media)

Choose the **Use Specific Date** option to specify the values of the start and end dates to use every time the report runs on the schedule.

Choose the **Use Relative Date** option to specify a time period relative to the day on which the report is run. The **Start Date** and **End Date** parameters are replaced by the **Timeframe** option parameters.

![New Schedule Use relative date](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-fbb2b0e17361b53cd99a7a2316d12a0facb3ce18%2FPAZ%20New%20Schedule%20dialog%20box%20page3%20Relative%20This.png?alt=media)

The descriptions of the **Timeframe** parameters are:

| Parameter | Description                                                                                                                                |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **This**  | The range from the start of the current **Unit** to today.                                                                                 |
| **Units** | The time period to use .                                                                                                                   |
| **Last**  | The amount of the date range in the units specified by the **Units** parameter.                                                            |
| **Value** | The size of the date range in the number of units specified in the **Units** parameter. This parameter displays when **Last** is selected. |

When using these options, the values of the **startDate** and **endDate** parameters are the start and end of the current (**This**) or **Last** full specified period (Week, Month, Quarter, for example). Those values are calculated each time the report runs relative to that date, allowing you to generate reports that contain data over progressively moving windows of time.
