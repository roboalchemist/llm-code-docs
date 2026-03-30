# Source: https://docs.pentaho.com/pba/pentaho-user-console/modern-design/scheduler/block-scheduler-from-running.md

# Block Scheduler from running

Configure periods of time to block Scheduler from running, so that you can accommodate planned operations like system maintenance. You can block scheduler from running for a single period of time or on a recurring schedule.

## Block Scheduler a single time

To configure a single period of time for blocking Scheduler from running, complete the following steps:

1. Log into the Pentaho User Console.
2. Open Scheduler:&#x20;

   * If you are using the **Modern Design**, in the menu on the left side of the page, click **Scheduler**.&#x20;
   * If you are using the **Classic Design**, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Scheduler**.&#x20;

   **Scheduler** opens with the **Schedules tab** selected.
3. Click the **Blockout Times** tab.&#x20;
4. Click **New Blockout Time**. The Set a Blockout Time window opens.
5. In the **Blockout Plan** section, select **Single Time**.
6. In the **Start time** section, specify when the blockout begins by configuring the following options:
   * **Timezone**
   * **Start date**
   * **Start time** and **AM** or **PM**
7. In the **Define blockout duration** section, specify when the blockout ends by doing one of the following:
   * If you want to specify how long the blockout lasts before it ends, in the **Ends** box, select **By duration** and then specify the **Duration** in days, hours, and minutes.
   * If you want to specify the time for the blockout to end, in the **End time** box, select **At a specific time** and then specify the time in HH:MM format and select **AM** or **PM.**
8. Click **Create**. The blockout time is added to the Blockout Times table in the Blockout Times tab of Scheduler.

## Block Scheduler on recurring schedule

To configure regular intervals of time for blocking Scheduler from running, complete the following steps:

1. Log into the Pentaho User Console.
2. Open Scheduler:&#x20;

   * If you are using the **Modern Design**, in the menu on the left side of the page, click **Scheduler**.&#x20;
   * If you are using the **Classic Design**, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Scheduler**.&#x20;

   **Scheduler** opens with the **Schedules tab** selected.
3. Click the **Blockout Times** tab.&#x20;
4. Click **New Blockout Time**. The **Set a Blockout Time** window opens.
5. In the **Blockout Plan** section, select **Single Time**.
6. In the **Start time** section, specify when the blockout begins by configuring the following options:
   * **Timezone**
   * **Start date**
   * **Start time** and **AM** or **PM**
7. To specify when the blockout ends, in the **Define blockout duration** section, do one of the following:
   * If you want to specify how long the blockout lasts before it ends, in the **Ends** box, select **By duration** and then specify the **Duration** in days, hours, and minutes.
   * If you want to specify the time that the blockout duration ends, in the **End time** box, specify the time in HH:MM format and then select **AM** or **PM.**
8. Click **Create**. The blockout time is added to the Blockout Times table in the Blockout Times tab of Scheduler.
