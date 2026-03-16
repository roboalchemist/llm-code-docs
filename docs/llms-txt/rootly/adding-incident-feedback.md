# Source: https://docs.rootly.com/incidents/managing-incidents/adding-incident-feedback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Incident Feedback

> Learn how to submit and manage incident feedback through both the Rootly web interface and Slack. Each user may submit feedback once per incident.

### Overview

Incident feedback helps teams capture what went smoothly during response and where improvements can be made.\
Rootly allows each user to submit **one feedback entry per incident**, either through Slack or the web interface, once the incident reaches **Mitigated** or **Resolved**.

Feedback becomes part of the incident record and is used in retrospectives, follow-up planning, and reliability improvements.

<Info>
  You can only submit feedback once per incident. If you need to update it, you may edit your existing entry through the web interface.
</Info>

***

### When Feedback Can Be Submitted

Feedback is available only after an incident has reached:

* **Mitigated** — customer impact has stopped
* **Resolved** — the root cause has been fixed

<Warning>
  If you attempt to submit feedback before the incident is Mitigated or Resolved, Rootly will block the submission and prompt you to try again later.
</Warning>

***

### Add Feedback Through the Web Interface

<Steps>
  <Step title="Open the Incident">
    Navigate to the incident where you want to leave feedback.
  </Step>

  <Step title="Find the Feedback Section">
    Scroll to the **Feedback** section on the incident page.\
    If no feedback exists yet, you will see an option to **Leave Feedback**.\
    If you have already submitted feedback, you can select **Edit**.

    <Frame>
            <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/feedback-1.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=a66aedd8abbd472436b5e4a778b56923" alt="Document image" width="898" height="393" data-path="images/incidents/feedback-1.webp" />
    </Frame>
  </Step>

  <Step title="Submit Your Feedback">
    Provide your:

    * Rating
    * Written comments
    * Optional anonymity setting

    Click **Submit** to finalize your feedback.
  </Step>
</Steps>

***

### Add Feedback Through Slack

Responders can also submit feedback directly in the incident’s Slack channel.

<Steps>
  <Step title="Run the Feedback Command">
    In the incident channel, type:

    `/incident feedback`

    or

    `/rootly feedback`

    Rootly will open a feedback submission modal.
  </Step>

  <Step title="Complete the Feedback Form">
    Enter:

    * A rating
    * Written comments
    * Optional anonymity preference

    <Frame>
            <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/feedback-2.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=d4966ecc1b5cdb81b94406ff9dc0a68b" alt="Document image" width="895" height="795" data-path="images/incidents/feedback-2.webp" />
    </Frame>
  </Step>

  <Step title="Submit the Feedback">
    Once submitted, your feedback is saved and can be viewed from the web interface.
  </Step>
</Steps>

<Info>
  Slack feedback commands must be run **inside the incident channel**, as Rootly identifies the incident using the channel ID.
</Info>

***

### What Happens After Feedback Is Submitted

After your feedback is recorded:

* It is linked to your user and the incident
* You cannot submit a second feedback entry
* You *can* edit your existing feedback through the web interface
* Anonymous feedback hides your identity from other responders and stakeholders
* Feedback becomes available for retrospectives and process improvement reviews

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="I can’t submit feedback yet">
    The incident may still be active.\
    Feedback is only available after **Mitigated** or **Resolved**.
  </Accordion>

  <Accordion title="The Slack command didn’t work">
    Ensure you ran the command **inside the incident channel**.\
    Commands executed elsewhere cannot be mapped to an incident.
  </Accordion>

  <Accordion title="I already submitted feedback but want to edit it">
    You can edit feedback at any time from the **web interface**.\
    Slack does not support editing after submission.
  </Accordion>

  <Accordion title="Anonymous feedback looks incorrect">
    Verify whether the **anonymous** checkbox was selected during submission.\
    You can change this setting by editing the feedback on the web.
  </Accordion>

  <Accordion title="The Slack modal didn’t appear">
    Confirm:

    * The incident is Mitigated or Resolved
    * You have permission to submit feedback
    * The Rootly Slack app has access to the channel
    * You are running the command in the correct incident channel
  </Accordion>
</AccordionGroup>

***

### Best Practices

* **Submit feedback as close to resolution as possible**\
  Context fades quickly; timely feedback is more accurate.

* **Be specific and actionable**\
  Comments such as “unclear ownership during triage” or “alert was noisy” help teams make targeted improvements.

* **Use anonymity when necessary**\
  Anonymous submissions can encourage more candid insights.

* **Incorporate feedback into retrospectives**\
  Reviewing user feedback alongside incident timelines provides richer context.

* **Automate reminders to leave feedback**\
  Many teams configure workflows that prompt responders to submit feedback immediately after the incident transitions to Resolved.

* **Encourage all responders to participate**\
  Broader participation leads to more comprehensive insights across teams and roles.


Built with [Mintlify](https://mintlify.com).