# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/schedules/schedule-reports/manage-schedules/prevent-scheduling-by-setting-blockout-times.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/manage-schedules/prevent-scheduling-by-setting-blockout-times.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/schedules/schedule-reports/manage-schedules/prevent-scheduling-by-setting-blockout-times.md

# Prevent Scheduling by Setting Blockout Times

From the Pentaho User Console, you can set up specific times on the server to block the running of schedules, which helps you perform administrative functions, such as system maintenance or managing server traffic during peak usage times.

1. From the User Console **Home** menu, click **Schedules**

   The Schedules page appears.
2. Click the **Create Blockout Time** button.

   The Blockout Time dialog box appears.

   ![New Schedule Blockout Time dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-e783a19332ffe876492d30d6048c9b9692358590%2FssBaservNewSchedBlockTime.png?alt=media)
3. Enter values in the **Recurrence**, **Start Time**, and **Duration** or**End Time** fields to block out specific times.
4. Click **OK**. If **Run Once** is selected in the **Recurrence** field, a dash displays under the **Start Time** and **End Time** fields in the blockout list, until the blockout time passes.

Your blockout time is set up and no schedules will run on the Pentaho Server during that time. Anyone can view a list of blocked out times when they are creating schedules.
