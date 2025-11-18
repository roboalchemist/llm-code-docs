# Source: https://docs.asapp.com/changelog/messaging-insights-manager.md

# ASAPP Messaging Updates - Insights Manager

> New updates and improvements for ASAPP Messaging - Insights Manager

<Update label="2025 - Overflow Queue Routing">
  ## Overflow Queue Routing

  Administrators can redirect the traffic from one queue to another queue based on two different rules, namely: business hours and agent availability.

  **Business Hours Rule**

  The chat traffic from queue A is redirected to queue B when it is later than the open operating business hours for queue B.

  **Agent Availability Rule**

  The chat traffic from queue A is redirected to queue B when there is no available agent serving queue A.

  Queue Routing improves:

  * Reduce estimated wait time for end-customers
  * Support closed queues when it is a legal requirement

  <Note>
    Admins can choose to redirect traffic from Queue A to Queue B based on a rule configuration which is set by an ASAPP representative.
  </Note>
</Update>

<Update label="2025 - Bulk Close and Transfer Chats">
  ## Bulk Close and Transfer Chats

  ASAPP introduces bulk chat management features in Live Insights to help alleviate queues experiencing unusual activity or high traffic.

  These features include:

  * Bulk Transfer: Transfer all chats from one queue to another to redistribute traffic
  * Bulk Close: End all chats in a queue to quickly address unusual activity

  The features are accessible through dropdown menus and modal interfaces in Live Insights.

  <Accordion title="How it Works">
    ## How it Works

    <Frame>
      <img src="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/bulkchats.png?fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=ea9aa1e97b854fb9c365e68cef5559ce" data-og-width="1261" width="1261" data-og-height="923" height="923" data-path="images/messaging-platform/insights-manager/bulkchats.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/bulkchats.png?w=280&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=19702a646a8ecfe8cac66577006c537a 280w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/bulkchats.png?w=560&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=c69b2296fb78245fc029ebfecc89357b 560w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/bulkchats.png?w=840&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=a378b8ac584b6b9e2e81c0ab54a24bc8 840w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/bulkchats.png?w=1100&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=929bc77f42e5c409a6bd82ceb565f5ed 1100w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/bulkchats.png?w=1650&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=4c3d61f0a672c9496596751cbca3ee94 1650w, https://mintcdn.com/asapp/3gV5ovdpglqSwLMa/images/messaging-platform/insights-manager/bulkchats.png?w=2500&fit=max&auto=format&n=3gV5ovdpglqSwLMa&q=85&s=9a067b3cf918288e76857e7407387fe3 2500w" />
    </Frame>

    ### Bulk Chat Transfer

    A user sees a dropdown list and selects the “Transfer all chats” item from the dropdown menu.

    A queue selection modal appears to ask: “Select the queue which you want to transfer all chats to?” and they see a downdrop list of all the queue names and need to select a queue name and click transfer chats button.

    A toast message appears informing the user that all chats have been transferred.

    The end customer does not see a change on their side and assumes they are still waiting in a queue.

    ### Bulk Chat Closure

    A user clicks on the 3 dots in the upper right hand corner of the queue card they want to impact.

    The user sees a dropdown list and selects the “End all chats” item from the dropdown menu. A confirmation modal appears to ask: “Are you sure you want to end all chats in this queue?” and they need to select confirm/yes to complete the action of ending all chats.

    A toast message appears informing the user that all chats are ended.

    The end customer sees the normal “Conversation has  ended” component.
  </Accordion>
</Update>

<Update label="2025 - Grouping Data and Filtering">
  ## Data Access Control via SSO Groups

  Users are assigned to groups based on their SSO/SAML credentials, which determines their data access across Live Insights, Conversation Manager, and User Management.

  Organizations provide four attributes per user (BPO, Product, Role, Location) which ASAPP uses to construct group names and manage access:

  * BPO users see only chats they service
  * Workforce Management users see all chats, metrics and agents for their BPO
  * Agents see only their own chats and data
  * Managers see chats for their assigned teams

  ASAPP maintains the group structure to enable filtering and queue association. All filters are defined by user SSO attributes.
</Update>

<Update label="2024 - Live Insights Metrics">
  ## Live Insights Metrics

  Two new monitoring features were added to Live Insights:

  * Average First Response Time metric in queue cards tracks customer wait time for initial agent response
  * SLA column in conversation tables shows if response times meet service level agreements

  <Frame>
    <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bed027eb-466d-190c-9173-154d3eb33cd6.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=d6e9db035a6f1d296a0ae034fbd60965" data-og-width="1600" width="1600" data-og-height="902" height="902" data-path="image/uuid-bed027eb-466d-190c-9173-154d3eb33cd6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bed027eb-466d-190c-9173-154d3eb33cd6.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=20318611241a82c806b238fb96766d55 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bed027eb-466d-190c-9173-154d3eb33cd6.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=a762c4b4bc013b33e51234611fad139b 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bed027eb-466d-190c-9173-154d3eb33cd6.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7d13f4af00c43d678855669d647d5df6 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bed027eb-466d-190c-9173-154d3eb33cd6.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=17b1e7c4889f09a26a404d7f812463c9 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bed027eb-466d-190c-9173-154d3eb33cd6.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=049b28fa574473ae5f699c272a9f7ff6 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-bed027eb-466d-190c-9173-154d3eb33cd6.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=e76de371bfbec34f85a13ea274420b64 2500w" />
  </Frame>

  These additions help workforce managers monitor capacity and meet contractual SLA commitments.

  <Accordion title="How it Works">
    ## How it Works

    Workforce management team monitors two key live metrics which are not present in ASAPP's Live Insights.

    Some organizations require that the First Response time be within 2 minutes. In order to monitor whether they're meeting this SLA they have a metric named 'Average First Response Time' (definition: the average time consumers wait for the first human response in a conversation).

    ASAPP will add a metric named 'Average First Response Time' to each queue card in Live Insights.

    <Note>
      The metric is calculated as 'Average First Response Time'= queue wait time + agent time to first response
    </Note>

    Organizations can monitor which chats have a response time longer than 2 minutes. ASAPP will add a response time column in the conversations tab within the queue card found in Live Insights. The calculation will be Response time= SLA (2 minutes)- response time.

    <Frame>
      <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-abb8b24f-933e-71f5-69b3-9ccfd5ba2ca7.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c03f5b94444817c732fb3ec9a908be2c" data-og-width="1600" width="1600" data-og-height="854" height="854" data-path="image/uuid-abb8b24f-933e-71f5-69b3-9ccfd5ba2ca7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-abb8b24f-933e-71f5-69b3-9ccfd5ba2ca7.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=231f8228b358c56e9e5a91406003868e 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-abb8b24f-933e-71f5-69b3-9ccfd5ba2ca7.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=c1ee65d95d24e627c0410150a2556c0e 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-abb8b24f-933e-71f5-69b3-9ccfd5ba2ca7.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=5dbc4cbb8ebd77042462ef638940fa27 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-abb8b24f-933e-71f5-69b3-9ccfd5ba2ca7.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=2fb8f59fb7289eb22519d9d1db2592f4 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-abb8b24f-933e-71f5-69b3-9ccfd5ba2ca7.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=a45b6c3f752510d73072e29f29a9dc70 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-abb8b24f-933e-71f5-69b3-9ccfd5ba2ca7.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=066a4ea299c117776d91d49028561e66 2500w" />
    </Frame>
  </Accordion>
</Update>

<Update label="2024 - Team and Location tables for Live Insights">
  ## Team and Location tables for Live Insights

  Live Insights now offers a Team and a Locations tab with filtering options that helps to oversee the management of teams and agents. Each tab shows the size and occupancy of each result.

  Customers assign staff to their queues from various sites/BPOs, which complicates tracking the real-time performance of their agents for administrators. They lack visibility into agent behaviors, outages, and staffing levels across different geographic locations.

  Additionally, supervisors are sometimes required to provide hourly updates on agent status (active, on lunch, etc.), necessitating an easy method for accessing this information. The additional teams and location tabs in insights manager make the administrators task of managing their teams across various locations easier and more efficient.

  <Frame>
    <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d3598481-1963-4e8a-702e-ba299ce584f2.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=bc171fdbec62937f250ce4dbb5731292" data-og-width="1600" width="1600" data-og-height="999" height="999" data-path="image/uuid-d3598481-1963-4e8a-702e-ba299ce584f2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d3598481-1963-4e8a-702e-ba299ce584f2.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3a15b2ee83ea4ad1ef4b44f45287945e 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d3598481-1963-4e8a-702e-ba299ce584f2.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=82ea8f310d35170cb333a9fbda40b33e 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d3598481-1963-4e8a-702e-ba299ce584f2.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=851c2ad4347935f6616f94fddf21cabd 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d3598481-1963-4e8a-702e-ba299ce584f2.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=85d220b0675d7674c034d1bea8f19b51 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d3598481-1963-4e8a-702e-ba299ce584f2.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=92dda6392e9c9b86cf7cb26a052c90d8 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-d3598481-1963-4e8a-702e-ba299ce584f2.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=81c8c2cea40abb4c10d8aca1d242f238 2500w" />
  </Frame>

  <Accordion title="How It Works">
    ## How It Works

    Supervisors can track the following:

    ### Live Insights

    * **Team Tab**
    * **Locations Tab**

    ### Procedure

    The administrator can see a list of agents after they have clicked into a particular queue, then selected Performance from the left-hand panel and clicked into the Agents icon on the right-hand panel.

    They can further oversee results by performance metrics of the current day and filter both the agent list and metrics by any of the following attributes:

    1. **Agent Name**
    2. **Location**
    3. **Team**
    4. **Status**

    <Frame>
      <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dac80f45-73af-d191-2570-4d26c5a62949.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=2fa8397b0fd4e206c665fd3c48dab3da" data-og-width="1600" width="1600" data-og-height="999" height="999" data-path="image/uuid-dac80f45-73af-d191-2570-4d26c5a62949.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dac80f45-73af-d191-2570-4d26c5a62949.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=f3c5a16ec4e902c25953a113301da2c8 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dac80f45-73af-d191-2570-4d26c5a62949.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=faf1414bbf433c3044a1302f641b1ac1 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dac80f45-73af-d191-2570-4d26c5a62949.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e503e3993cbf4b9a7e9181c0a6b17f14 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dac80f45-73af-d191-2570-4d26c5a62949.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=db9b9e267ab94eb5522531b3f0b38ce9 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dac80f45-73af-d191-2570-4d26c5a62949.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a808ce5ed629ac85cb026b49b621257a 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-dac80f45-73af-d191-2570-4d26c5a62949.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=9e1d9711865a42822e7bc4c959cce081 2500w" />
    </Frame>

    ### Management Capabilities

    **Filtering by location**

    Each location provides updates of performance and agents names.

    **Filtering by site**

    Each administrator can provide an hourly update of how many agents are active, on lunch, or in a different state as well as view corresponding metrics

    ### Feature Configuration

    All information on which location and teams an agent belongs to is sourced through the SSO integration with ASAPP. Customers that require any changes to the data should change the respective attribute being passed to ASAPP.

    Please contact your ASAPP representative for further information.
  </Accordion>
</Update>
