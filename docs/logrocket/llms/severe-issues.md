# Source: https://docs.logrocket.com/docs/severe-issues.md

# Severe Issues

AI-recommended issues based on detection of significant user impact, with natural language descriptions

LogRocket uses machine learning and LLMs (large language models) to recommend certain issues that your team may consider to have a severe impact on your users. Our issue recommendation models are trained on data from LogRocket sessions and issues, and we use them to find user-impacting issues and then describe them with natural language titles.

The indicator that an issue is severe is a red siren icon. For these issues, a natural language title will replace the original technical issue title. Additionally, within the issue details view a sampling of issue events will have red sirens next to them denoting particularly good representations of the issue.

<Image align="center" alt="Siren icon indicates severe issue" border={true} caption="Siren icon indicates severe issue" src="https://files.readme.io/f336eaffb8cc05b7b2da61e3a5ba4c8f91aa09377d98e3c89d2271dd30f49c52-Severe_Issues_2.png" />

> 🚧 Severe Issues are not available for self-hosted installations
>
> Issues Severity is not yet available for self-hosted installations of LogRocket. For any further questions, contact [support@logrocket.com](mailto:support@logrocket.com).

## AI-driven Severity

Machine learning and LLM is used to find and describe issues that have a meaningful impact on your users. Issues considered severe are more likely to be associated with user frustration and may indicate that users were prevented from completing an in-app task. These issues have their titles updated with a natural language descriptive title. For example `Error • TypeError: Cannot read properties of undefined (reading 'destroy')` may get a natural language title of `Users unable to access or analyze data within selected time range`.

Issue severity is computed over a time range (e.g., last day, last week) and may change as you select different time ranges. An issue's severity rating is also more accurate when more data is available for it.

<Image align="center" alt={635} border={true} caption="Issue severity rating" title="Screenshot 2023-01-17 at 1.50.05 PM.png" src="https://files.readme.io/292db8434373ba8188c2ce7273d0caf66bbe2d0ad34b6ac073ad5321b6210f17-AI-driven_Severity.png" />

## Severity Filter

By default, LogRocket shows all issues sorted by severe first. To show only the severe issues, change the Severity filter from "Any Severity" to "Severe".

<Image align="center" alt={320} border={false} caption="Severity filter" title="Screenshot 2023-01-09 at 10.18.00 AM.png" src="https://files.readme.io/3ebaba3b1d244db8fccf8742e9c4aac06ec5d9499707d59ad4d1635355b5e8c3-Severity_Filter.png" />

## Severity in the Issue Details View

An issue's detail view will also display severity indicator in the header next to the title. Galileo also generates titles for severe issues to describe the issues in natural language. Severity is computed based on the last 30 days of data:

<Image align="center" alt="Header with issue severity score in Issue Detail view" border={true} caption="Header with issue severity rating in Issue Detail view" src="https://files.readme.io/df9d29300e812c1e7481507c667a375a1714b4653b3590b71d166a321878a28a-Severity_in_the_Issue_Details_View_1.png" />

The event list in the detail view will also display a severity rating indicating session events that are particularly good representations of the impactful problem. Events may be sorted by severity or time of occurrence in descending order.

<Image align="center" alt="Event list in Issue Detail View with event severity scores" border={true} caption="Event list in Issue Detail View with event severity rating" src="https://files.readme.io/f99bfce962ce11bd080e0ff6284f614c582e55df624252a30896e923744f6246-Severity_in_the_Issue_Details_View_2.png" />

## Severe Issues in Session Replay

In the session replay view, if an event in the recording is associated with an issue, a severity indicator and a link to the issue will be shown alongside the event. In this context, the severity indicator displays the degree of frustration associated with that event.

JavaScript Error issues will appear in the **Logs** pane:

<Image align="center" alt="Issue events in the Logs pane" border={true} caption="Issue events in the Logs pane" src="https://files.readme.io/4394044-severe-issue-in-logs.png" />

Network Error issue events will appear in the **Network** pane:

<Image align="center" alt="Issue events in the Network pane" border={false} caption="Issue events in the Network pane" src="https://files.readme.io/1853545ae00a04f75c2e3a7cb6a245a0eeb5f1fce9bea02818f644fb038f2697-Severe_Issues_in_Session_Replay_2.png" />

> 🚧 Network traffic is sampled before being treated as an Issue
>
> LogRocket samples network events before processing them as issues. Not all network errors will have an associated link to an issue and a severity rating.

All other issue types (Rage Clicks, Dead Clicks, Error States, Frustrating Network Requests) will appear in the **Event Timeline**:

<Image align="center" alt="Issue events in the event timeline" border={true} caption="Issue events in the event timeline" src="https://files.readme.io/886cabc7cd438ae6bc53beb8cad347e942afbc3f4d2bf85e4fa8781e83aaeeb0-Severe_Issues_in_Session_Replay_3.png" />

## Issues Digests

LogRocket delivers a weekly Issues Digest to your channel of choice - Email, Slack, Teams, or Webhook. [See how to Issues Digests](https://docs.logrocket.com/docs/issues-digests) work and are driven by Galileo AI.

## Making Severity Better

LogRocket's issue recommendations are constantly improving, and you can help! Use our [issue triage](https://docs.logrocket.com/docs/issues#grouping-issues) features to teach LogRocket that an issue is or is not severe.

For example, if you agree that a severe issue is severe, triaging it as "High" or "Low" impact will make those kinds of recommendations more likely in the future. If you don't think an issue should have been considered severe, triaging it as "Ignored" will make those kinds of recommendations less likely in the future. Similarly, if you think LogRocket should have recommended an issue but it didn't, triaging it as "High" or "Low" impact will make it more likely that similar issues are recommended in the future. And if you agree that LogRocket correctly decided not to recommend an issue, triaging it as "Ignored" will help to reinforce that behavior.

<Image align="center" alt="Issue triage popover" border={false} caption="Issue triage popover" src="https://files.readme.io/0d1bade297262fd85477fa807cb21ca2ef249059e23865bc69e22902bf283cbf-Making_Severity_Better.png" width="-1px" />

> 🚧 Changing issue group conditions may change severity rating
>
> Keep in mind that customizing grouping conditions may cause the triaged issue's severity rating to change.