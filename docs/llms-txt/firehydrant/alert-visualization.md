# Source: https://docs.firehydrant.com/docs/alert-visualization.md

# Alert Visualization

Sometimes it's easier to see what an alert will do before it does it.

Setting up alerting can be a daunting task because you can feel like you're configuring in the unknown. For example, if an alert were to come in at 5pm on a Friday... who would it page? Which team(s) would respond? How many steps would there be?

We built our alert visualizer to help solve exactly that.

![](https://files.readme.io/02fb8d0f9c1bfbd27cfa3e11bd5bdbce35e5babf8673639ddad25a34f35c984c-CleanShot_2025-07-01_at_00.38.022x.png)

<br />

## Pick an event

Signals are the name for FireHydrant's events that can be converted into an alert. When FireHydrant receives a signal, we search for rules that match the payload, or dispatch directly a team, escalation policy, or schedule. To use the visualizer effectively, we recommend having Signals already received and processed by FireHydrant.

### Choose your event

![](https://files.readme.io/7798333bf41e38a0c43b91d3f14971b3ca771b2ccf708f4a82ffec4a0fc87b8c-CleanShot_2025-07-01_at_00.24.152x.png)

To visualize an existing alert, visit the "**Signals**" link in the navigation. Then click the "**Event Logs**" link in the left navigation. From there, click any of the Signals that FireHydrant has processed, scroll to the bottom of the drawer that appears, and click "**Visualize Alert Rules**"

![](https://files.readme.io/90099e002fa2ebca76864ef50c445981e99eb85cf3911fbca08897d1778065e6-CleanShot_2025-07-01_at_00.26.502x.png)

FireHydrant will render a DAG (directed acyclic graph) of your Signal's theoretical journey if it were to be received at the date and time selected. If multiple rules are matched, multiple paths will be presented.

### Drilling down

To drill into a route, you can click on the initial target to see which steps the alert will take and when. This enables confidence that your configuration will target the right people, at the right time.

<Image align="center" src="https://files.readme.io/c4d4c44249d0e027c2359398ffd4dd894836a32a6f83de7d8b30aeb3f26c5edb-viz-by-target.gif" />