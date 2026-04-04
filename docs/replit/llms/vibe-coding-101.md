# Source: https://docs.replit.com/tutorials/vibe-coding-101.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Vibe coding 101: from idea to published app

> Learn how to go from an idea to a published application using Replit Agent, featuring an interactive map visualization project.

export const AiPrompt = ({children}) => {
  return <CodeBlock className="relative block font-sans whitespace-pre-wrap break-words">
      <div className="pr-7">
        {children}
      </div>
    </CodeBlock>;
};

export const YouTubeEmbed = ({videoId, title = "YouTube video", startAt}) => {
  if (!videoId) {
    return null;
  }
  let url = "https://www.youtube.com/embed/" + videoId;
  if (startAt) {
    url = url + "?start=" + startAt;
  }
  return <Frame>
      <iframe src={url} title={title} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>
    </Frame>;
};

This tutorial walks you through the "vibe coding" process on Replit—taking an idea from concept to a fully published application. This tutorial will build an interactive map visualization of San Francisco parks, pulling in external data and using modern frameworks. You'll see how to leverage [Replit Agent](/replitai/agent) for initial development, refinements and debugging.

<YouTubeEmbed videoId="2v5Fs7Xr11Y" />

## The vibe coding philosophy

Vibe coding is less about writing every line of code and more about guiding AI tools with your vision and domain knowledge. It's an iterative process of prompting, reviewing, and refining.

Key takeaways from the video:

* **Conceptualize First**: Start with a clear idea of what you want to build. Visualizing the end product helps, especially when prompting AI.
* **Domain Knowledge is Power**: Knowing relevant frameworks (like Leaflet.js for maps) or data sources (like OpenStreetMap) significantly improves AI-generated results.
* **Iterative Development**: Expect to debug and refine. AI tools are powerful, but they're collaborators, not magic wands.

## Project: San Francisco parks map

The goal is to build an interactive map displaying parks and public spaces in San Francisco.

**Problem Statement**: The goal is an interactive map to discover parks and public spaces in San Francisco.
**Solution**: An interactive tool using Leaflet.js and OpenStreetMap data.
**Key lessons**:

* Prompting AI effectively.
* Processing external data.
* Debugging and handling errors.

## Building with Replit Agent

Replit Agent can scaffold entire projects, set up environments, and generate initial code.

<Steps>
  <Step title="Crafting the Initial Prompt">
    A good prompt is specific. We tell Agent:

    * The goal: "Help me create a minimalist maps app to visualize San Francisco's parks."
    * Key technologies: "You should use leaflet for map visualization and fetch data from OpenStreetMap."
    * Specific data types from OpenStreetMap (after research): Natural formations (woods, beaches, islets, cave entrances) and leisure locations (parks, gardens).

    <AiPrompt>
      Help me create a minimalist maps app to visualize San Francisco's parks. You should use leaflet for map visualization and fetch data from OpenStreetMap. Include the following OpenStreetMap data types for San Francisco: natural formations (woods, beaches, islet, cave entrance) and leisure (park, gardens).
    </AiPrompt>

    To learn more about how to write effective prompts, check out [this article](tutorials/effective-prompting).
  </Step>

  <Step title="Attaching a Mockup">
    Visual aids help Agent understand the desired layout and features. A simple sketch or mockup can be attached directly to the prompt.

    <Frame>
      <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/wireframe.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c67dc8c30de1d2fe85de17a49b8a9ec1" alt="Wireframe sketch of the maps app" data-og-width="5120" width="5120" data-og-height="2828" height="2828" data-path="images/tutorials/vibe-coding-101/wireframe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/wireframe.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=cf9dc4a4b042b21a4ed9ce54233d4854 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/wireframe.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=3460d1594f8932353f121511bc309316 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/wireframe.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d379e3c0433c87bf0d4ae903e009ff2c 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/wireframe.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=ce1755dd148a0ad6e73a564b11c39a47 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/wireframe.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=dd14b5c3575ab1337c579596bb0db1a1 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/wireframe.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=6c7f662a41afef6c50a8d85e6078b381 2500w" />
    </Frame>
  </Step>

  <Step title="Agent's Process">
    1. **Plan Creation**: [Agent](/replitai/agent) outlines the steps it will take. Review and approve this plan.

       <Frame>
         <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/agent-plan.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=e25c35ce8054f2ccb02bc8eeb607c23e" alt="Replit Agent plan creation" data-og-width="5120" width="5120" data-og-height="2828" height="2828" data-path="images/tutorials/vibe-coding-101/agent-plan.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/agent-plan.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c213f7ced9e7429c260a6d36b8fe4897 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/agent-plan.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=bdd1d5197fb393476c11ced89380e3fc 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/agent-plan.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=67679fa7a75c95b2732d34b99a93db62 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/agent-plan.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9928c751dcfe0215a724b189b73acfd3 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/agent-plan.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=76913a40aa4e6b342dc67d8768fdc221 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/agent-plan.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9fa426a4567c26d7c0fe9039b34ce832 2500w" />
       </Frame>
    2. **Visual Preview**: Agent streams a visual preview of the app's UI.

       <Frame>
         <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/visual-preview.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=1d3fc339176c1fdf0cc73621109c162b" alt="Replit Agent visual preview" data-og-width="5120" width="5120" data-og-height="2828" height="2828" data-path="images/tutorials/vibe-coding-101/visual-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/visual-preview.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b1872a3869c568a406174a9e9063627a 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/visual-preview.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=0d7016dc64bf614da4ea2155e6eb92c5 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/visual-preview.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=328c3237ad022ae52adc9d0c2da8c457 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/visual-preview.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=1dcae85f2b62a35ad2c3ca5fb602fd36 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/visual-preview.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=3f955c5eb946039844010f02862d7d2f 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/visual-preview.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=5af4f954457dfab503967458cbc5fd08 2500w" />
       </Frame>
    3. **Environment Setup**: Agent configures the development environment, installing necessary languages and packages—no manual setup required.
    4. **Building the App**: Agent writes the code for the front end and back end.
    5. **Checkpoints**: Agent creates checkpoints ([Git commits](/replit-workspace/workspace-features/version-control)) so you can roll back if something goes wrong.
  </Step>

  <Step title="Debugging with Agent">
    Errors happen. Use the browser's DevTools (specifically the Console and Network tabs) to find error messages.

    * **Observe**: The map loaded, but no data points appeared.
    * **Investigate**: The console showed an error: "Failed to fetch map features error cannot read properties of undefined reading natural."
    * **Inform Agent**: Paste the error message directly into the chat with Agent. Agent will attempt to debug and fix the issue.

      <Frame>
        <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/console-debug.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b21be49b94e56aea8b6e15ceabd55926" alt="Browser console showing an error" data-og-width="5120" width="5120" data-og-height="2828" height="2828" data-path="images/tutorials/vibe-coding-101/console-debug.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/console-debug.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=577fa5d7fa2c42005919b2a5e030246c 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/console-debug.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=591072d6687bdf5d8777125d2f677b56 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/console-debug.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=f02a9e210235621325e981b06ba65761 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/console-debug.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d2305aa4a2b156b133dbdbb40ee095e0 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/console-debug.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=8630e9145bf48fddc33709f35080cbc2 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/console-debug.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d66e0a2ed2474b0f910811865baf3756 2500w" />
      </Frame>

    In the video, Agent identified an issue with parsing the Overpass API response and added robust error handling, which resolved the problem.
  </Step>
</Steps>

## Refining with Fast mode

Once Agent builds the MVP, use [Fast mode](/replitai/fast-mode) for smaller, more targeted edits and refinements. Fast mode is optimized for quick changes.

<AccordionGroup>
  <Accordion title="Improving Map Styling">
    The initial map was functional but could look better.
    **Prompt to Agent**: "Can you use a more minimalist carto style for OpenStreetMap? Carto lite."

    This relies on knowing that "Carto lite" is a known theme for Leaflet maps.
  </Accordion>

  <Accordion title="Adding Dark Mode">
    A common refinement is adding a dark mode.
    **Prompt to Agent**: "Can you add a dark mode to my app and use, carto dark for the map in the dark mode?"

    <Frame>
      <img src="https://mintcdn.com/replit/_Y3y7Jf58i1OzvJs/images/tutorials/vibe-coding-101/dark-mode-agent.png?fit=max&auto=format&n=_Y3y7Jf58i1OzvJs&q=85&s=12d594b5478d9b427e621da59cfb4d97" alt="Replit Agent implementing dark mode" data-og-width="5120" width="5120" data-og-height="2828" height="2828" data-path="images/tutorials/vibe-coding-101/dark-mode-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/_Y3y7Jf58i1OzvJs/images/tutorials/vibe-coding-101/dark-mode-agent.png?w=280&fit=max&auto=format&n=_Y3y7Jf58i1OzvJs&q=85&s=f422de8f933782385167d394fdfede49 280w, https://mintcdn.com/replit/_Y3y7Jf58i1OzvJs/images/tutorials/vibe-coding-101/dark-mode-agent.png?w=560&fit=max&auto=format&n=_Y3y7Jf58i1OzvJs&q=85&s=101946a0846b4d01115fc00c4b94ad27 560w, https://mintcdn.com/replit/_Y3y7Jf58i1OzvJs/images/tutorials/vibe-coding-101/dark-mode-agent.png?w=840&fit=max&auto=format&n=_Y3y7Jf58i1OzvJs&q=85&s=d2f07a73f59c0c2ca298c0330687e4a6 840w, https://mintcdn.com/replit/_Y3y7Jf58i1OzvJs/images/tutorials/vibe-coding-101/dark-mode-agent.png?w=1100&fit=max&auto=format&n=_Y3y7Jf58i1OzvJs&q=85&s=40ef9ab41593d9e1cfa9f83cac13e59c 1100w, https://mintcdn.com/replit/_Y3y7Jf58i1OzvJs/images/tutorials/vibe-coding-101/dark-mode-agent.png?w=1650&fit=max&auto=format&n=_Y3y7Jf58i1OzvJs&q=85&s=2f1dc3822f9dd2329a56951cae9bee11 1650w, https://mintcdn.com/replit/_Y3y7Jf58i1OzvJs/images/tutorials/vibe-coding-101/dark-mode-agent.png?w=2500&fit=max&auto=format&n=_Y3y7Jf58i1OzvJs&q=85&s=cd9a0dc07fb59a4399ecc3fc4099098d 2500w" />
    </Frame>

    Agent will:

    * Read files for context.
    * Make changes to necessary files (e.g., theme providers, styles).
    * Restart the app to apply changes.
  </Accordion>

  <Accordion title="Iterative Debugging with Agent">
    Adding dark mode involved several iterations:

    1. Initial implementation had a toggle that worked for the map but then disappeared.
       **Feedback**: "The toggle theme button works for the map, but it disappears when clicked. The theme toggle should be in the side nav and the theme should be applied to the side nav."
    2. Issues with multiple toggle buttons and incorrect component references (`side nav` vs. `sidebar`).
       **Feedback & Guidance**: "Now there are two toggle themes. One controls the map, the other controls the side nav. Make them into one in the side. Now and update the CSS."
       When Agent made an incorrect assumption (e.g. `SideNav` component), explicitly pointing it to the correct file (`@Sidebar`) helps.
    3. Final fix to ensure the dark mode toggle in the sidebar correctly toggled the map theme to Carto Dark.
       **Feedback**: "Now the dark mode toggle in @Sidebar does not toggle the map to carto dark."

    This process highlights the "conversation" aspect of vibe coding. Be descriptive and guide the AI.
  </Accordion>
</AccordionGroup>

## Publishing your application

Replit makes publishing straightforward.

1. Select the **[Publish](/cloud-services/deployments/about-deployments)** button.
2. Agent suggests a publishing configuration (e.g., app name, build and run commands). Review and confirm.
3. If your app uses API keys or other sensitive information, store them in **[Secrets](replit-workspace/workspace-features/secrets)**. Agent will use these securely.
4. Select **Publish**. Replit bundles your app and makes it live on the web.

   <Frame>
     <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/deploy.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9634d8cb1f712a5f12be15989d690fdb" alt="Replit deployment screen" data-og-width="5120" width="5120" data-og-height="2828" height="2828" data-path="images/tutorials/vibe-coding-101/deploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/deploy.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d9bca19d9a05ae7e91218abfd814eb7c 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/deploy.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d0c9cf148977a5a10f2064eb17051e9d 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/deploy.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=438b4b3a8ef68c132e10146fddc76c13 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/deploy.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=65959104c1d3e154f5c65ccb8b0fc12c 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/deploy.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=40ed3858c9499863bbd409f6bac27b1f 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/vibe-coding-101/deploy.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=3096f0d1b961dd586da86f845380a49f 2500w" />
   </Frame>

Your published app will have a public URL (e.g., `park-mapper.replit.app`). Changes made in your development environment won't affect the published version until you click **Republish**.

## Recap and next steps

This tutorial went from an idea to a published interactive map application without writing a single line of code manually. Replit Agent was used for the heavy lifting, with Fast mode for refinements, leveraging domain knowledge and an iterative debugging process.

**Potential Next Steps for the Park Mapper App**:

* Add a [database](category/storage-and-databases) to store park data persistently (avoiding re-fetch on every load).
* Allow users to save or favorite parks.
* Implement advanced filtering.
* Improve styling and add custom icons for map markers.
* Enhance mobile responsiveness (e.g., ensuring filters are accessible on mobile).

Vibe coding is about iterating, experimenting, and guiding AI to bring your ideas to life. Don't be afraid of errors; they are part of the process!
