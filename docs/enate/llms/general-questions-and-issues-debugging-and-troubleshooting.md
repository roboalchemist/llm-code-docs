# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/uipath/setting-up-enate-and-uipath-orchestrator-synchronization/general-questions-and-issues-debugging-and-troubleshooting.md

# General Questions and Issues, Debugging and Troubleshooting

The Bot is a User in the system and there are some constraints in using the robots.

* RPA Sync Interval between Enate and Uipath orchestrator is defined under General Settings in Enate Manager. By default, the value is 5 mins, but it is configurable.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-ouXYcY0HJoj8Xl%2F38.png?generation=1632305156605078\&alt=media)

* As of now, robots cannot work on Cases and Tickets. It only works on Actions. However, Robots can create tickets and Cases.
* Robots cannot access User management i.e., user information, User GUID’s etc.
* If you delete the Robots in the UiPath Orchestrator, they are not deleted in Enate.
* The password of the robots created via RPA Sync with the orchestrator cannot be manually changed in Enate.
* For some reason, the robot authentication fails and there is a need to reset the password.
  * First, check the password is working or not. There is a single line of code that needs to be written to extract the robot password for the bot synchronized between Enate and Uipath Orchestrator.

&#x20;**plainStr = new System.Net.NetworkCredential(string.Empty,secureStr).Password**

* This needs to be written inside an assign activity where plainstr is a string variable and securestr is the password output of Get Credentials.
* Once the password is obtained then open the swagger page and check if the authentication is working or not.
* If the Authentication is not working, then in the database update the PasswordLastChanged column to more than 30 days back in tblusers and after the RPA Sync Interval time Enate will reset the password for the robot and sync it with the Uipath orchestrator.
