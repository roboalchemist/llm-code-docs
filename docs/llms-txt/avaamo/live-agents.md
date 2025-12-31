# Source: https://docs.avaamo.com/user-guide/live-agent-console/supervisor/live-agents.md

# Live agents

The `Live Agents` page enables real-time tracking of live agent availability for supervisors within the account. Supervisors can also override the live agent status if required.

This functionality allows supervisors to monitor the number of active, away, or offline live agents. By utilizing this information, supervisors can make informed decisions to optimize customer experiences by adjusting configurations based on the availability of live agents. For example, if an agent is marked as "away" or "offline", supervisors can adjust the configurations, reducing wait times and improving efficiency. See [Advanced Configurations](https://docs.avaamo.com/user-guide/live-agent-console/advanced-configurations), for more information.

### **View live agents**

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Analytics and Reporting icon -> Live Agents` page in the left navigation pane of the Supervisor interface to view the real-time status of all live agents.&#x20;
* By default, the page displays active live agents first, followed by agents who are currently away, and finally, those who are offline. Within each status category, the agents are listed in descending order based on their creation time, which implies that the last created live agent appears first in the list.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FIPLyH5HQc968G5Yeprnr%2FScreenshot%2007-08-2024%20at%2013.31.png?alt=media&#x26;token=99ee3793-c148-41ee-a3bc-7cf1e1f6b93e" alt=""><figcaption></figcaption></figure>

Each row contains the following information:

* Live agent name
* Current live agent status: Active agents are denoted by a green dot, an orange dot indicates the agent is away, and gray represents offline status.&#x20;
* Teams: Number of teams the live agent is associated with. Hover over the number to see the list of teams.
* Live agent email
* Actions: This section allows you to modify or override the current live agent status. See [Change live agent status](#change-live-agent-status), for more information.

### Change live agent status

Supervisors have the authority to override or modify the live agent status, providing them with the capability to address situations where a live agent may not be available, such as being on sick leave, but has not updated their status accordingly. This functionality is crucial to prevent instances where the live agent appears online while being unavailable, which could lead to a suboptimal customer experience.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FX3pF4kVMgFJnLwfzAnn2%2FScreenshot%2007-08-2024%20at%2013.28.png?alt=media&#x26;token=979c4e6c-ca21-42f0-ac54-43617af511f6" alt=""><figcaption></figcaption></figure>

**To change the live agent status**:

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Analytics and Reporting icon -> Live Agents` page in the left navigation pane of the Supervisor interface to view the real-time status of all live agents.&#x20;
* Search the live agent for which you wish to change the status. See [Search live agent](#search-live-agent), for more information.
* Click the Actions icon and select the required status to update the live agent status. See [Set live agent status](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/set-live-agent-status), for more information on live agent status and what they mean.

{% hint style="info" %}
**Note**: Modifying the status from Active to Offline has implications on concurrency settings. See [Advanced configurations](https://docs.avaamo.com/user-guide/live-agent-console/advanced-configurations), for more information.
{% endhint %}

### Search live agent

You can search for live agents using the search icon in the `Live Agents` page. To search the live agents, enter the desired text in the Search text box and press enter.

### Filter live agent by status

You can filter live agents by status using the status dropdown in the `Live Agents` page. Select the required status to filter and view the results.

### Enable translation for Live agents

Supervisors can enable or disable the live agent translation feature for live agents. This selective enablement is beneficial when live agents are trained in multiple languages, allowing them to effectively handle queries from end users. See [Live Agent Translation](https://docs.avaamo.com/user-guide/live-agent-console/live-agent/live-agent-translation), for more information.

This process helps supervisors manage the translation feature based on the specific language skills of their agents.

**To enable translation for live agents:**

* Click `Settings -> Avaamo Live Agent` in the Avaamo dashboard home page to view the Supervisor interface.
* Click `Analytics and Reporting icon -> Live Agents` page in the left navigation pane of the Supervisor interface to view the real-time status of all live agents.
* Click the Actions icon and choose either `Enable Live Agent Translation` or `Disable Live Agent Translation`**.** You can verify the status of the live agent translation in the `Enable Live Agent Translation` column.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FeBR1LJ5aUIzO7alXmUGJ%2FScreenshot%2023-08-2024%20at%2013.54.png?alt=media&#x26;token=5e8d1420-8433-4a68-bfb3-9dcc74fa29b8" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fy9mOMmuZNldd0neGvXuw%2FScreenshot%2023-08-2024%20at%2013.59.png?alt=media&#x26;token=019794e3-a4d8-4a2f-94ca-1371207dec6b" alt=""><figcaption></figcaption></figure>
