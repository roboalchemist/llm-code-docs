# Source: https://docs.frigade.com/platform/flows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Flows

## What are Flows?

***

Flows are the main building blocks of Frigade. Flows are made up of one or more Steps that you want a user to take. A Flow can be a product tour, a checklist, a form, or any other onboarding experience you can imagine.

Flows comes with built-in content management, version control, and analytics to make it easier to build and collaborate on onboarding.

Users have their own state for each Flow (e.g. started, dismissed, completed), and it is automatically tracked by Frigade. Flows can also track Steps across groups of users, such as companies or teams.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=55e8bc703b8ab4b7eb2ab88744f0a7f6" data-og-width="3696" width="3696" data-og-height="2244" height="2244" data-path="images/platform/flow-detail-editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=2cabf0b9b2df7e673f82283d3f8a5438 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=a6be6a39ea113270cefe299fc4939ff3 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7635b4aba7fd32d96fb07a50cee8b829 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=0e027ab9110a817c968646ec1eda944a 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f7beeb294fba262b914a894c934e3047 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-editor.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=937924267315fd24fa96258d85494640 2500w" />
</Frame>

## User Lifecycle

Users can have state in Flows and in the Steps within a Flow. The lifecycle of a user's state in a Flow is as follows:

1. **Not started**: The user has not seen or engaged with the Flow.
2. **Started**: The user has seen the Flow and may have completed or skipped one or more Steps.
3. **Completed** or **Dismissed**: The user has completed or dismissed the Flow.

Once a Flow is completed or dismissed, it will remain in this state for the user unless the Flow is restarted via the SDK, API, or the **Reset in Flow** button in the Frigade Dashboard. This is true even if the Flow has new Steps added or a Step's state is reset.

## Frequently Asked Questions

***

<AccordionGroup>
  <Accordion title="How do I create a Flow?">
    You can create a Flow by tapping **Create Flow** from the navigation bar or from a component in the [component library](https://app.frigade.com/components/).
  </Accordion>

  <Accordion title="How do I edit a Flow?">
    Flows can be edited by clicking on the Flow name from the Flow overview page. From there, you can edit:

    * Version

    * Name and Description

    * Content (e.g. copy, assets, images)

    * Step logic (e.g. what actions mark a step complete)

    * Step order (e.g. what order content should be shown in)

    * User targeting logic (e.g. which users should see this Flow)

    * Status (e.g. whether the Flow is active or not)
  </Accordion>

  <Accordion title="How do I edit a Flow's YAML configuration?">
    You can edit a Flow's underlying YAML code by clicking the **Advanced Editor** toggle on the Flow detail page.

    <Note>The preview it will not reflect any custom styling you define in your own codebase.</Note>
  </Accordion>

  <Accordion title="How do I preview a Flow?">
    When using a Frigade pre-built UI, you can simply preview the Flow from the Editor tab of the Flow detail page. To see your Flow in your product, you can view your Flow in your staging or production environment.

    If you'd like, you can use targeting to only show it to teammates while building, and you can reset users in the **Users** tab to go through the Flow multiple times.

    <Frame caption="Preview your Flow in real-time in Frigade">
      <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=fc40523ed27e6c6ced0882293f0e7ecc" data-og-width="4598" width="4598" data-og-height="2410" height="2410" data-path="images/platform/editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e10b2892db864e36792081193d199be0 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7985c658200915d98ff903edbd812c34 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7bcbeebc8e05529ab0d9ebbf7e6ab55b 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8a02113fd5d1826db7f4f39444871c2b 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b8567865f7d8035a3d1b63fc83ffeffe 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=0884c324dc8a5a18b4d586b8fd93ebfc 2500w" />
    </Frame>

    <Note>The preview it will not reflect any custom styling you define in your own codebase.</Note>
  </Accordion>

  <Accordion title="What Flow types are there?">
    Frigade supports the following Flow types:

    * [Checklist](/component/checklist/carousel)
    * [Tour](/component/tour)
    * [Form](/component/form)
    * [Announcement](/component/announcement)
    * [Banner](/component/banner)
    * [Card](/component/inline-card)

    You can also build [custom Flows](/guides/custom) using the Frigade SDK.
  </Accordion>

  <Accordion title="Can a group share a Step of a Flow?">
    Yes. Sometimes you want any user in a group to complete a Step on behalf of all the other users in the group (e.g. add a credit card, install an SDK, etc.). This is supported in Frigade through [group properties](/sdk/hooks/group) and [completion criteria](/sdk/advanced/completing-a-step).
  </Accordion>
</AccordionGroup>
