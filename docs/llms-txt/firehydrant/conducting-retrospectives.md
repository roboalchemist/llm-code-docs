# Source: https://docs.firehydrant.com/docs/conducting-retrospectives.md

# Conducting Retrospectives

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Plans
      </th>

      <th style={{ textAlign: "left" }}>
        Required Permissions
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        * All plans
        * Enterprise (collaboration features)
      </td>

      <td style={{ textAlign: "left" }}>
        * `Manage Incidents`
      </td>
    </tr>
  </tbody>
</Table>

This guide highlights some of the key features as well as how some of our customers conduct retrospectives on the FireHydrant platform

## Prerequisites

* At least one [Retrospective Template](https://docs.firehydrant.com/docs/retrospective-templates) should be configured
* Must have `Manage Incidents` permission, as filling out retrospective fields is modifying incident fields

## Collaboration Features

Enterprise customers have access to the collaboration features in FireHydrant's Retrospectives, which include seeing who's on the document looking at it at any moment as well as live cursor updates within freeform text boxes.

These features are handy for teams working through retrospectives together so that they can stay in sync!

<Image align="center" alt="Collaborative cursors in retros" border={false} caption="Collaborative cursors in retros" src="https://files.readme.io/c24bda239667009e3b606357292990a961b811c968e35656cc779d0aa5829c2b-CleanShot_2025-03-27_at_13.13.402x.png" width="650px" />

## Gathering Evidence

<Image align="center" border={false} caption="Example Retrospective view" src="https://files.readme.io/e744938076cb63b2eae53e42e5e3cdb608487c3df91976e5cb25d755852de56b-CleanShot_2025-09-10_at_15.36.322x.jpg" width="650px" />

FireHydrant has automatically logged all occurrences and accidents on the incident within the timeline. However, to differentiate the signal from the noise, responders will likely have been starring items as they come up (you can review this on [Incident Timeline](https://docs.firehydrant.com/docs/incident-timeline)).

When you reach the Retrospective view, all of the Starred items will be showing by default as they're key. If you want to browse all/other events and star more, you can clear out the "Starred" filter at the top of the timeline.

In addition, you may want to check that all of your Milestones are filled out with the correct timestamps (or aren't missing any data), and that all of the tasks and actions on your incident were correctly updated if they were/weren't done and by whom.

## Completing the Retrospective

FireHydrant's AI Copilot can draft answers to your retrospectives using all of the context it has gathered throughout the incident. To do this, simply click on ":sparkles: Draft with AI" button next to the question(s) you'd like the AI to attempt to answer.

<Image align="center" border={false} caption="FireHydrant AI Copilot answering questions with given context" src="https://files.readme.io/09d632b6e39a762a9b7d46b96c4d76fbc07cae0591acf551779f9a0651428ef3-CleanShot_2025-09-10_at_15.53.02.gif" width="650px" />

On top of answering the retrospective questions, you can attach additional retrospective templates at any given time and even add additional, ad-hoc questions.

<Image align="center" border={false} caption="Adding a question to the end of an already-attached template ad-hoc" src="https://files.readme.io/1e6d61927c25860ab8569aff0229d5043abfd5e3891b993ced07ba7c6f015a68-CleanShot_2025-09-10_at_15.57.552x.jpg" width="400px" />

Typically as a part of the incident review, users will also create and assign follow-up tickets. For this, FireHydrant has integrations with ticketing providers to automatically create linked tickets in external systems for tracking engineering work, while tying it back to the incident in FireHydrant.

For more information, visit:

* [Managing Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups)
* [Resources and Tasks Analytics](https://docs.firehydrant.com/docs/analytics-resources-and-tasks)

## Next Steps

* Once retrospectives are complete, it's time to [Preview & Export](https://docs.firehydrant.com/docs/preview-export-retrospectives) them.