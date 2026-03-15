# Source: https://docs.firehydrant.com/docs/team-support-hours.md

# Team Support Hours

Typically, FireHydrant enables teams who want to be notified during on-call shifts at any time of day. However, there are cases where FireHydrant Signals is used like a ticketing or triage system that only alerts during set working hours.

**Team Support Hours** allow setting a maximum alert priority during and outside of these working hours. For example, if a high-priority alert comes in during support hours, it will remain high and notify as usual, but if it comes in outside of work hours, it may be downgraded to low priority to avoid unnecessarily waking up responders.

## Configuring Support Hours

<Image align="center" width="650px" src="https://files.readme.io/07dd71a49a70c20b7e17bab21d8d4ad2938c1c63e057967a3af12fce3e45c9f9-CleanShot_2025-01-14_at_12.17.282x.png" />

Support hours are configured per team. Head to any team you'd like to set up and go to the **Support Hours** tab. On this page, click "Set up support hours".

On this next page, you can configure working hours on a per-day basis. By default, weekdays are checked and weekends are unchecked. On top of setting start/end times on each day, you can also set the maximum priority during those hours. These default to **High**.

Besides the per-day configurations, you can also set the following preferences:

* **Off-hours Max Prirority**: any alert coming in outside of the above configured hours will be downgraded to this priority
* **Bypass Threshold**: any alert coming in above the set level will bypass support hours and behave as a normal alert.
* **Time Zone**: configure the support hours timezone.

## Other Considerations

Currently, any alerts that are downgraded outside of support hours aren't automatically upgraded at the start of the next hours. If this capability is important to you, reach out to your support or account team.

<br />