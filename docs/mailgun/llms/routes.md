# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/receive-forward-store/routes.md

# Routes

You can define a list of routes to handle incoming emails. This idea of routes is borrowed from MVC web frameworks like Django or Ruby on Rails. If a message matches a route expression, Mailgun can perform an action, such as forward the email, or store the email.

You can define routes visually by clicking the **Receiving** tab in the Control Panel, or programmatically using the [Routes API](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/routes). For more on setting up Routes, see  How Do I Setup a Route?.

A Route is a pair of **filter + action**. Each incoming message is passed to a filter expression, and if it evaluates to true, the action is executed.

Each Route can be assigned a priority, and are evaluated in the order of priority, with lower numbers having a higher priority. By default, all Routes are evaluated (even if a higher priority Route is triggered). To avoid this action, you can use a stop() action (see below).

**Route Properties**

| **Route** | **Description** |
|  --- | --- |
| `Priority` | Integer showing the priority of route execution. Lower numbers have higher priority. |
| `Filter` | Filters available in routes - match_recipient() match_header() catchall() (see Route Filters for description). |
| `Actions` | Type of action to take when a filter is triggered - forward() store() stop() (see below for description). |
| `Description` | Arbitrary string to describe the route (shown in the Control Panel UI) |


Info
The length of the **Filter** or **Action** fields cannot exceed 4k. If you need more actions or filters than is allowed under the 4k limit, you can add additional routes. Multiple routes with the same Filter expression are allowed. This will allow you to add many more Actions for the same Filter but spread across multiple route entries.