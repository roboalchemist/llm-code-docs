# Source: https://docs.firehydrant.com/docs/analytics-resources-and-tasks.md

# Resources and Tasks

The Resources and Tasks subpage focuses on metrics around your retrospectives, action items, and team statistics.

## Retrospective Completion

What happens after an incident is just as important as what happens during an incident. Retrospectives are valuable as they lead to learning, shared accountability, and continuous improvement. This chart provides insight into your Retrospective habits after incidents are resolved. Add additional filters to see how different assigned teams might have other rituals or to see different frequencies based on an incident's severity.

![RetroCompletionChart.png](https://support.firehydrant.com/hc/article_attachments/12439955719700)

### Summary Cards Explained

* **Incidents Resolved.** This card shows the number of incidents resolved during the selected date range within the filtering criteria. We calculate this using the Resolved milestone occured\_at timestamp. We are omitting any GAME DAY, MAINTENANCE, or UNSET.
* **Retrospectives Started**. This card shows the number of retrospectives started during the selected date range within the filtering criteria. We measure this using the Retrospected started milestone occured\_at timestamp. We are omitting any GAME DAY, MAINTENANCE, or UNSET.
* **Retrospectives Completed**. This card shows the number of retrospectives completed during the selected date range within the filtering criteria. We measure this using the Retrospected Completed milestone occured\_at timestamp. We are omitting any GAME DAY, MAINTENANCE, or UNSET.

### Chart Explained

Based on your selected resolution, the stacked line graph lets you see these critical milestones over time. Using this chart, you can see how timely and diligent your teams are in having Retrospectives. Hover over each node in the chart to see the numerical value for the resolution group.

## New Incidents by Team

Understanding which teams are most often assigned to incidents is critical to your organization's culture and your product's success. This chart provides an overview of which teams are at risk of burnout from their sheer involvement in incidents and highlights potential single sources of failure. In either case, you can use this information to understand better how your teams are working and what support they might need.

For this chart, we are looking specifically at the Active Incidents in your organization. This means that we will pull in the data for an incident that has been in an Active milestone state, between Started and Resolved, within the given date range.

![NewIncidentsbyTeamChart.png](https://support.firehydrant.com/hc/article_attachments/12439957857940)

### Summary Cards Explained

* **Top Impacted Teams**. This card looks at the teams assigned to the most incidents in the given time frame. We do not include the 'None assigned' category represented in the pie chart in this count. 'None assigned' is when an incident does not have a functionality/service attached at the query time. To help you focus on what matters, we limit this view to the top 10 impacted infrastructure components.
* **Incidents Displayed**. This card is a count of Active Incidents based on set query parameters. Active Incidents have started before or during the date range and do not have to be resolved to be included in this count. We do not include GAMEDAY or MAINTENANCE incidents in this total.

### Chart Explained

Identify when teams are assigned ownership of an incident. Depending on your selection, this stacked bar chart tracks team assignments against a daily, weekly, or monthly resolution. You can see how many incidents each team has been assigned, determining if the impact is spread evenly or if a subset of teams is significantly impacted. The time variable can indicate that a team needs to slow in shipping or can serve as a starting point to dig into other root causes that could lead to an influx in incidents. You may even see a senior team consistently assigned ownership simply because they have the most experience in your codebase. Use this chart to start conversations, help foster blameless retrospectives and drive accountability for tackling root causes.

## Task and Follow-up Completion

What happens after an incident is just as important as what happens during an incident. Tasks and Follow-Ups are great tools for accountability and joint responsibility. Add additional filters to see how different assigned teams might have other rituals or to see different frequencies based on an incident's severity.

![TaskFollowUpCompletionChart.png](https://support.firehydrant.com/hc/article_attachments/12439959244948)

### Summary Cards Explained

* **Tasks/Follow-ups Created.** This card shows the number of tasks or follow-ups created during the specified date range. We are omitting tasks or follow-ups associated with incidents marked as GAME DAY or MAINTENANCE. We also exclude tasks or follow-ups that were Canceled. This card will change based on your selection in the Action Item drop-down.
* **Tasks/Follow-ups Completed.** This card shows the number of tasks or follow-ups completed during the specified date range. Tasks and Follow-ups are identified as completed based on their done status and last updated\_at timestamp. We are omitting tasks or follow-ups associated with incidents marked as GAME DAY or MAINTENANCE. This card will change based on your selection in the Action Item drop-down.

### Chart Explained

How often have you looked into a bug to find a lingering #TODO memo inline? See the burndown of action items in this stacked line chart, comparing the number of tasks created versus the number of tasks completed. While this is a simple metric, it can help engage conversations around: "Are we creating meaningful follow-ups?" and "Are we holding people accountable for completing the follow-ups?" Over time, use this data to see if it positively impacts overall system performance or even other metrics, such as MTTM or MTTR.