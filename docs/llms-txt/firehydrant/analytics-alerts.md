# Source: https://docs.firehydrant.com/docs/analytics-alerts.md

# Alerting Analytics

<Image align="center" width="650px" src="https://files.readme.io/6b55047-CleanShot_2024-04-25_at_17.33.312x.png" />

FireHydrant offers key Alerting metrics to help responders understand the overall health of their monitoring and teams.

## Alert baseline metrics

The baseline metrics show the total number of alerts, acknowledgments, and incidents that resulted from these alerts. We also calculate the <Glossary>MTTA</Glossary> and <Glossary>MTTR</Glossary> metrics of Alerts.

These metrics are calculated across all alerts according to the configured filter at the top of the page. You can adjust and finetune the filter by various parameters, including specific components, teams, [matching Rules](https://docs.firehydrant.com/docs/signals-alert-rules), and more.

## Analytics funnel

<Image alt="Alerting Funnel" align="center" width="650px" src="https://files.readme.io/ee13c8e-CleanShot_2024-04-25_at_17.49.412x.png">
  Alerting Funnel
</Image>

The funnel helps understand the number of Alerts the team receives vs. acknowledges and how many of them actually become incidents.

A funnel with a large mouth and skinny spout suggests that responders are receiving a lot of false alarms that do not turn into incidents. The more cylindrical/uniform the funnel parts are, the healthier the signal-to-noise ratio is.

## Time and day heatmap

<Image alt="Time and Day Heatmap" align="center" width="650px" src="https://files.readme.io/9e7a20f-CleanShot_2024-04-25_at_18.04.12.png">
  Time and Day Heatmap
</Image>

The time and day heatmap shows you which days and times of day you are receiving the most alerts.

This can help you determine, e.g., whether it was only a specific, temporary event that led to a cluster of alerts this last month or whether there is a recurring event at a specific time of the week liable to cause problems.

## Alerts grouped by entity

<Image alt="Alerts table grouped by various entities" align="center" width="650px" src="https://files.readme.io/81230d8-CleanShot_2024-04-25_at_17.58.352x.png">
  Alerts table grouped by various entities
</Image>

The final table on the page shows all of the baseline metrics above, but split out according to the grouped entity. The default grouping is set to **Teams**, but you can change the grouping to see how the baseline stats by **Rules**, **Services**, **Environments**, **Tags**, and more.