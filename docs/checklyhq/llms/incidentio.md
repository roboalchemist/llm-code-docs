# Source: https://checklyhq.com/docs/integrations/incident-management/incidentio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Alerts to Incident.io

> Configure Incident.io integration to create and resolve incidents from Checkly alerts

Checkly integrates with [Incident.io](https://incident.io/) to monitor your alerts and create / resolve incidents in your Incident.io account. Let's get started!

1. Log in to Incident.io and navigate to **Alerts > Sources**, click **New Alert Source** and select "Checkly"."

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/incidentio/incident_io_step1.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=1805826743b29ca564857d13f045d42c" alt="incident.io integration step 1" width="1605" height="1130" data-path="images/docs/images/integrations/incidentio/incident_io_step1.png" />

2. Take note of the URL and API key that Incident.io provides you with, and head over to [Checkly > Alerts](https://app.checklyhq.com/alerts/settings), click **Add more channels** and select **Incident.io**.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/incidentio/incident_io_step2.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=9a643a79fef196ad097eec1a3de51473" alt="incident.io integration step 2" width="1605" height="1130" data-path="images/docs/images/integrations/incidentio/incident_io_step2.png" />

3. Copy and paste in the URL and API key and hit **Test Incident.io alert** to verify the connection. On the Incident.io side, you should now see a test alert pop up!

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/incidentio/incident_io_step3.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=02637e21a9ad89c4988abfd6760eb7c4" alt="incident.io integration step 3" width="1605" height="1130" data-path="images/docs/images/integrations/incidentio/incident_io_step3.png" />

4. We recommend one last step. Create a new custom attribute on the Incident.io side to grab the Checkly result link from the JSON payload. This will help reference what check result triggered an alert.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/incidentio/incident_io_step4.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=503c4c4ebbf5e45b3394166fcc77ca79" alt="incident.io integration step 4" width="1605" height="1130" data-path="images/docs/images/integrations/incidentio/incident_io_step4.png" />

5. Now you are all set up! When an alert is triggered, an incident will be created in Incident.io with the Checkly check result link attached.

<img src="https://mintcdn.com/checkly-422f444a/Shzx8VYv0RJK1Wbz/images/docs/images/integrations/incidentio/incident_io_step5.png?fit=max&auto=format&n=Shzx8VYv0RJK1Wbz&q=85&s=ab97b8e02c8153a4fed9ffdaf1387d3e" alt="incident.io integration step 5" width="1605" height="1130" data-path="images/docs/images/integrations/incidentio/incident_io_step5.png" />


Built with [Mintlify](https://mintlify.com).