# Source: https://docs.zapier.com/platform/reference/project-app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zapier integration structure for a project management app

> While you can't automate project work, you can automatically add tasks, create new projects, and keep track of progress via an app integration on Zapier.

To add a project management app integration in the Platform UI:

## Prerequisites

* A [Zapier account](https://zapier.com/sign-up).
* If you haven't used Zapier before, you'll want to learn the basics in our [Zapier Getting Started Guide](https://zapier.com/learn/zapier-quick-start-guide/).
* Familiarity with your app's API documentation and available endpoints.
* Review the [Platform UI Tutorial](/platform/quickstart/ui-tutorial).

## 1. Add triggers for common record types in each project

* Check out the [common record types](/platform/quickstart/must-have-triggers-and-actions#project-management) used as triggers by other project management apps.

* For apps with many record types, consider including a *New Activity* trigger, with options to let users choose which type of activity should trigger the Zap.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b34f31e26be51d5581f2a669c62c8d14.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=d59c530150415c3c95e7e44e506e584b" data-og-width="1447" width="1447" data-og-height="910" height="910" data-path="images/b34f31e26be51d5581f2a669c62c8d14.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b34f31e26be51d5581f2a669c62c8d14.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=753016cfd8da5bc5924a2c36dd9020a1 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b34f31e26be51d5581f2a669c62c8d14.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=fe75c61e9143b126b60623f9856a41d2 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b34f31e26be51d5581f2a669c62c8d14.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=21d07409ca10d16d94f48458927138c1 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b34f31e26be51d5581f2a669c62c8d14.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=eb1e1a0acf5e7dd683c8ec830081857d 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b34f31e26be51d5581f2a669c62c8d14.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2633c1fdbaff35a5195dfd6865590f5e 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b34f31e26be51d5581f2a669c62c8d14.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=bc3dcc1e50239169eeb6f917c0d5b3e1 2500w" />
</Frame>

![new activity trigger](https://cdn.zappy.app/)

* Build separate triggers for new and updated records. *Updated* triggers for project management apps are most useful as these updates affect work to be done. Users want to know if the task deadline changed, if details were added or the scope was redefined, or if someone completed something.

* It is strongly recommended to ensure that any trigger behavior encompasses all updates that are visible to a logged-in user in your app's user interface, independent of admin/creator permissions for a record type. Users expect to be able to automate off any record that is shared with them, regardless if they're an admin/creator or not. If this is not possible with your API, make this clear in the Trigger description. For example, for a *New Note* trigger, add help text such as “Triggers when the **connected** user account adds a note to a project.”

* Allow users to filter which records they want to trigger on. For example, a *New Task* trigger could trigger when tasks are added to any project *or* to one specific project. Include [dynamic dropdowns](/platform/build/field-definitions#dynamic-dropdown) ordered by the most recently added to fetch accounts, projects, lists, and other items users would want to filter.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fe08bdcbf666e8f2961f0c2b3932b460.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=66da98aca49ca5e647e9a31318ab5ef5" data-og-width="1203" width="1203" data-og-height="867" height="867" data-path="images/fe08bdcbf666e8f2961f0c2b3932b460.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fe08bdcbf666e8f2961f0c2b3932b460.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=836870162bf772e4810382dcc33d6761 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fe08bdcbf666e8f2961f0c2b3932b460.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=7b6d2b4b9125a6458022f3afcb28c3a6 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fe08bdcbf666e8f2961f0c2b3932b460.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=863b9c88bbefe26d8eed5660910e829c 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fe08bdcbf666e8f2961f0c2b3932b460.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=1587ca01b313f4c478119a979bd2097f 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fe08bdcbf666e8f2961f0c2b3932b460.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=866f65f89ce9ef011baaf36d3f754837 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fe08bdcbf666e8f2961f0c2b3932b460.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f83b64fad664f1b955b2e853aa6cfdca 2500w" />
</Frame>

* Project management records are linked to other records in your app. If the data is visible for that record in your app, users expect to see it in their Zap as well. For example, a “New Task” trigger should include details about the task's project too.

* Include both IDs for linked data in the response output so they can be mapped to your app's action steps, as well as human-readable data such as individual fields for project name and description.

* If your record API endpoint does not automatically return additional linked data beyond the ID or name of the record, add custom code to your trigger API call to fetch relevant data linked to the record as well.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f2f5450c1c7981b41a4d2234047bfaa.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=0820c0fbad5828b947fb62c30ef942e4" data-og-width="1256" width="1256" data-og-height="1178" height="1178" data-path="images/3f2f5450c1c7981b41a4d2234047bfaa.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f2f5450c1c7981b41a4d2234047bfaa.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=9f761de531787e04dab4b1953ffaa3f0 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f2f5450c1c7981b41a4d2234047bfaa.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=5d70faaab2237b6ab8d872a7b899e08d 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f2f5450c1c7981b41a4d2234047bfaa.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=33a095b5d8f0c6d37c36e787a3e063de 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f2f5450c1c7981b41a4d2234047bfaa.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=3b68a933802ab128eb971af384cdee15 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f2f5450c1c7981b41a4d2234047bfaa.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=94e2369948f8e6f577a92fa7c20b1385 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/3f2f5450c1c7981b41a4d2234047bfaa.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=ae305156a2db2b40df185e8b941d71cd 2500w" />
</Frame>

## 2. Include common search actions

* Users expect to have searches for top-level records available for project management integrations so they can add child-level details. For example, a Project can have many Tasks, and some projects may have the same or similar tasks. Users are more likely to want a *Find Project* search so they can add tasks to projects, rather than a Find Task search which may not return the precise item they need.

* Configure the search to find an existing record, returning it in the same format the trigger returns records to give a consistent experience and allow the data to be used in the same manner in later actions.

* Offer multiple search key and value options where applicable. For example, a *Find Project* search should let users search by project ID and name. The former is useful for searching based on data in previous steps, where the latter is useful to find projects with human input. Return exact matches first and provide help text to communicate to users how the search matches records to search terms.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/542be79e48ccbd6d12e43646690dcebb.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=f32df09e9d61315c1c223b2acf3d27d1" data-og-width="1044" width="1044" data-og-height="747" height="747" data-path="images/542be79e48ccbd6d12e43646690dcebb.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/542be79e48ccbd6d12e43646690dcebb.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=7bc5f94b34af295fe46a1b765d746e97 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/542be79e48ccbd6d12e43646690dcebb.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=576a6f7780b89115670ccac78833b6ae 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/542be79e48ccbd6d12e43646690dcebb.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=44001f4ceabbf68dfc2b175289d5d18d 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/542be79e48ccbd6d12e43646690dcebb.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=74af70a1bc40b66caff6eca928584271 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/542be79e48ccbd6d12e43646690dcebb.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=530b864e6f5018d8cb5f98cdcba7f7d3 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/542be79e48ccbd6d12e43646690dcebb.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=38b9f6676bfc8304dc3074c2b2ab935d 2500w" />
</Frame>

## 3. Include common create actions

* Check out the [common record types](/platform/quickstart/must-have-triggers-and-actions#project-management) other project management apps have create actions for.

* Add corresponding *Update* actions with available *Search* actions to make it easier for users to update the correct project record.

* Account for linked records in action input fields, so when your app's UI allows users to create a task and link it to existing projects, the same action is available via a Zap, via a [dynamic dropdown](/platform/build/field-definitions#dynamic-dropdown) to fetch linked record options and let users select them.

* Do not have a single action create multiple records. When a user creates a new task through Zapier, this should only create new tasks, and should not also create other linked records at the same time. Rather include a separate action to create the other linked record, along with a task update action to link the task after the other record is created. This reduces the chance for errors and record redundancy.

* Optionally link a [search connector](https://cdn.zappy.app/99829074f857d0938c0ba7b3c5e97e84.png) to linked record input fields if users need to have the Zap find the correct related record, and map the found ID to the input field. To add that user prompt you'll need to work in the [Platform CLI](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#search-powered-fields).

## 4. Test your triggers and actions

Make Zaps with the following criteria to ensure your app integration works as expected:

* Connect your integration with [other project management apps](https://zapier.com/apps/categories/project-management), to see if the data your integration returns blends well with our common apps. Companies frequently use integrations to copy tasks and projects across a blend of project management apps to keep track of work between teams.
* If your integration supports events or tasks with due dates, connect a Zap to popular [calendar or scheduling apps](https://zapier.com/apps/categories/calendar) to verify those dates can be added to other apps.
* If your integration has many nested items (such as projects containing sub-projects with tasks and sub-tasks), try setting up a few Zaps to see if the behavior across nested objects is the same as parent objects. Data returned should always be the same format; if your API doesn't enable access to nested objects, note that in the help text for that trigger/search/action.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
