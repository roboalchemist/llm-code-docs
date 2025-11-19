# Source: https://grafbase.com/docs/platform/schema-proposals.md

# Schema Proposals

Schema changes are high stakes, they may expose the wrong data, or expose it in confusing or inefficient ways to the client. They may not be consistent with the rest of the API schema, they may be missing important directives. Schema Proposals are a workflow to design, discuss, review and approve changes to subgraph schemas before they can be published. They are a design and governance tool.

Users and teams interact with proposals from three different angles:

- As author, you create and edit proposals, submit them for review, and iterate on them.
- As reviewer, you are notified of new proposals, you can comment on them, request changes, approve or reject them.
- As subgraph implementer, you can publish new subgraph versions containing changes from approved proposals.

Proposals are typically authored by the teams that own the subgraphs (in which case the author and subgraph implementer would be the same), other teams, product designers, or client teams who need changes to the GraphQL schema. Reviewers are typically subgraph owners, team leads, or members of teams managing cross-cutting concerns like authorization or API conventions.

## Walkthrough

The following steps follow a typical schema proposal along its lifecycle. Each step is prefixed with the personas who would be involved in that step.

1. **(Author)** Create a new Schema Proposal in the Proposals tab.

![Create a proposal](/images/docs/schema-proposals/create-proposal.png)

2. **(Author)** The proposal is created. It is in draft mode, nobody has been notified yet at this point.

![Proposal created](/images/docs/schema-proposals/proposal-created.png)

3. **(Author)** Edit, create, delete subgraph schemas. Save the changes.

![Editing a proposal](/images/docs/schema-proposals/editing-a-proposal.png)

4. **(Author)** Submit the proposal for review.

![Submitting a proposal for review](/images/docs/schema-proposals/submitting-a-proposal-for-review.png)

5. **(Reviewers)** The reviewers are notified. They can comment on the proposal, request changes, approve or reject it.

![Reviewing a proposal](/images/docs/schema-proposals/reviewing-a-proposal.png)

6. **(Author and reviewers)** The proposal is iterated on.

![Iterating on a proposal](/images/docs/schema-proposals/iteration.png)

7. **(Reviewers)** The reviewers approve or reject the proposal. Once all required reviewers have approved or rejected, the proposal transitions to the approved or rejected state.

![Approving a proposal](/images/docs/schema-proposals/approve.png)

8. **(Subgraph implementer)** New subgraph versions containing changes from any approved proposal can be published. [Schema checks](https://grafbase.com/docs/platform/schema-checks.md) ensure that only approved changes can be published.

## Configuration

By default, schema proposals are not enforced in schema checks and there are no configured reviewers. These options and more can be configured in the Settings tab, under Graph, then Proposals.

## Automatic rebasing

Each time the proposal is edited and changes saved, the proposal is automatically and transparently rebased on top of the latest published version of each subgraph schema. Schema proposals are better thought of as a set of diffs rather than full schema strings. When you start a new edit on an existing proposal, the schema you see is the latest version, with the current diff for the proposal applied on top of it.