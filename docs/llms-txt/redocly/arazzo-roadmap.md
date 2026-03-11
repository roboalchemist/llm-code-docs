# Source: https://redocly.com/blog/arazzo-roadmap.md

I'm often asked about what Redocly is doing for Arazzo.
Even more so, after Lorna's blog post about [Arazzo linting](/blog/arazzo-linting).
This blog post summarizes our current and future plans.

## The backgroundâ¦

When Lorna joined Redocly, we discussed the OpenAPI community and she introduced me to the SIG-Workflows group.
Intrigued, I shared the link with Roman Hotsiy (our CTO).
We were surprised.
We had created a similar specification internally.

Why?
We developed a tool that does E2E API contract testing (I named it "Spot" as in "Spot problems before they stain").

Spot is Respect
Spot was renamed to Respect to stick with the "Re" naming convention.

For the tool to work, we needed to connect an OpenAPI document to a workflow to describe a sequence of requests.
Otherwise, sending requests to all operations is unlikely to be successful.

Rather than work on a closed specification, we decided to fully digest the Arazzo Specification and make contributions based on our *super-secret* (~Spot~ Respect) tool.
This decision has led to visible contributions from myself, Roman, and Dmytro to the Arazzo Specification, which was officially released two months ago.

## Data dependencies are productivity killers

Many API operations have data dependencies.
Data dependencies can be a pain to document.
Oftentimes, I think "domain experts" are people who understand the data dependencies between resources and
corresponding operations.

Ultimately, Arazzo is a mechanism for sharing domain knowledge.

This is why I believe Arazzo is the **most important specification released** since founding Redocly almost 7 years ago.

## Roadmap

This following list is how we think about the tools and uses of Arazzo.

This list is not the exact sequence in which we are executing them.

**Create and edit the Arazzo Description**

1. [Linter](/docs/cli/guides/lint-arazzo) (so someone can write or edit in IDE and get feedback if it is correct) -- â DONE
2. Configurable rules (so someone can write their own standards for enforcing consistency in Arazzo Document design) --  â DONE
3. Visual tool (Replay) to generate an Arazzo Description, so the user doesn't need to learn the spec and write in IDE -- ð§ IN PROGRESS
4. Visual tool (Replay) to import an Arazzo Description -- ð§ IN PROGRESS


**Uses of the Arazzo Description**

1. Visualize Arazzo into docs (*learn by reading*) -- â NOT STARTED
2. Human exploration of workflows using our Replay try it console (*learn by doing*) -- ð§ IN PROGRESS
3. Automated E2E test sequences following workflows (we have a tool named ~**Spot**~ **Respect**) --  â DONE
4. Generate integration/workflow code examples -- â NOT STARTED


Learn Arazzo
We launched a [learning center for Arazzo](/learn/arazzo/what-is-arazzo).

## Chip in

Interested in one of those items?
[Let us know how you'd like to help](/contact-us), and you might influence the priority of our roadmap.

Have ideas? Want to join the team? Check out our [careers page](/careers) for open positions. We're hiring developers, product designers, and more!