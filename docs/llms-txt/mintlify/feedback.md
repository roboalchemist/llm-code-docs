# Source: https://mintlify.com/docs/insights/feedback.md

# Feedback

> Monitor user satisfaction and feedback on your documentation.

<Info>
  To collect and view feedback, you must first enable feedback from the [Add-ons](https://dashboard.mintlify.com/products/addons) page in your dashboard.
</Info>

The feedback tab displays quantitative thumbs up and thumbs down votes your docs have received and any qualitative feedback that users have provided. Use this information to gauge the quality of your docs and make improvements.

Access the feedback tab by navigating to the **Insights** page in your [dashboard](https://dashboard.mintlify.com/products/insights).

## Feedback types

<Note>
  Contextual and code snippet feedback are in beta. To enable them for your documentation site, [contact our sales team](mailto:hahnbee@mintlify.com).
</Note>

The feedback tab displays information according to the feedback add-ons that you enable.

Enable your preferred feedback types:

<Frame>
  <img className="block dark:hidden pointer-events-none" src="https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-light.png?fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=ff03c179eaddde9d4beaa34ad4442ed4" alt="Screenshot of the feedback toggles in the Add-ons page." data-og-width="1858" width="1858" data-og-height="1280" height="1280" data-path="images/analytics/feedback-addons-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-light.png?w=280&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=5e00a3793a32cd57f8e7d5965e7b9adf 280w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-light.png?w=560&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=36b5e00676f2606df9d8feeda8c9a6ca 560w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-light.png?w=840&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=7a0503ac37a47cdce5bcae80bd825456 840w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-light.png?w=1100&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=3693b70c35e6bfc8254ce374da3045e4 1100w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-light.png?w=1650&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=1140090406ca56214c003bbd1dd9ece2 1650w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-light.png?w=2500&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=0baaafdf02988dff15d2f46e3a3d6a05 2500w" />

  <img className="hidden dark:block pointer-events-none" src="https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-dark.png?fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=56aba5d2a5f86e89d857246d381c989c" alt="Screenshot of the feedback toggles in the Add-ons page." data-og-width="1860" width="1860" data-og-height="1280" height="1280" data-path="images/analytics/feedback-addons-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-dark.png?w=280&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=6a48d95143402a1cdbdc19da30c78c40 280w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-dark.png?w=560&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=16b9d9396601be7910b6486014a97850 560w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-dark.png?w=840&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=0da6416eee65f1c4fa882ff98fbf134d 840w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-dark.png?w=1100&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=860259a0754cee019051a15882b0b0cf 1100w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-dark.png?w=1650&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=b2646ff1791a72b4039b6ac2909073a8 1650w, https://mintcdn.com/mintlify/HLPaFoXqJBOwTqBr/images/analytics/feedback-addons-dark.png?w=2500&fit=max&auto=format&n=HLPaFoXqJBOwTqBr&q=85&s=047d5ef95c24ed367aeb2acc9fcb5002 2500w" />
</Frame>

* **Thumbs rating only**: Simple thumbs up/down voting to gauge overall satisfaction with pages.
* **Code snippet feedback only**: Feedback specifically on code snippets.
* **Thumbs rating and contextual feedback**: Page voting plus detailed comments and reasons for ratings.
* **Thumbs rating and code snippet feedback**: Page voting plus feedback on code examples.
* **Thumbs rating, contextual, and code snippet feedback**: Complete feedback system with page voting, detailed comments, and code snippet feedback.

<Note>
  If you disable telemetry in your `docs.json` file, feedback features will not appear on your documentation pages, even if you enable them in your dashboard.
</Note>

## Managing feedback

For contextual and code snippet feedback, you can set the status of a piece of feedback and add internal notes to track your work resolving user feedback.

### Changing feedback status

Select the status beside a piece of feedback to mark it as **Pending**, **In Progress**, **Resolved**, or **Dismissed**.

Best practices for setting feedback statuses:

* **Pending**: Feedback is awaiting review.
* **In Progress**: Feedback has been validated and is being worked on.
* **Resolved**: Feedback has been resolved.
* **Dismissed**: Feedback has been dismissed as not actionable, irrelevant, or inaccurate.

### Filtering by status

Use the status filter to control which feedback is displayed. Clear a status to hide all feedback with that status. By default, all feedback is displayed.

### Adding internal notes

Click on a piece of feedback to add an internal note. These notes are only visible to people with access to your dashboard.

Use notes to add information for collaboration, link relevant support or engineering tickets, or remember any other useful information.

## Using feedback data

Review your feedback data to:

* **Identify successful content**: Pages with the most positive feedback show what works well in your documentation.
* **Prioritize improvements**: Pages with the most negative feedback indicate what content might need attention.
* **Take action**: Make documentation updates based on direct user feedback.
