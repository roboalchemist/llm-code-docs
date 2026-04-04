# Source: https://docs.logrocket.com/docs/impose-session-limit.md

# Impose Session Limit

Available to Pro and Enterprise Customers

Since session quota is shared by all projects within a LogRocket organization, the "Impose Session Limit" toggle allows you to set a monthly limit for an individual project. Once the imposed limit is reached, LogRocket will stop recording new sessions for that project until the organization's monthly quota is reset. You can view your quota reset date on the Plans page within Settings.

# Configuration

This setting can be toggled on and off by users with the **Admin** role in your organization. It can be found by navigating to the desired project and clicking *"Settings" > "Recording Settings"*.

<Image align="center" border={true} src="https://files.readme.io/81c68414be2624615099e309a87aa2c407177744c97cd7bc59290e3b6a136d72-Impose_Session_Limit.png" className="border" />

# Troubleshooting

If a specific project stops recording sessions, it's best to verify whether any of the following are true:

1. The organization's monthly session quota has been reached
2. The project has reached its imposed session limit
3. "Pause Recording" is toggled on

<br />