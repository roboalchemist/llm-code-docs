# Source: https://www.apollographql.com/docs/graphos/platform/schema-management/proposals.md

# Schema ProposalsAs your supergraph schema grows, managing changes becomes more difficult.
Assessing the impact of subgraph schema changes on composition and client operations becomes more complex.
Once schema design changes are agreed upon, implementing them during subgraph development poses another challenge.These challenges grow when updating multiple subgraph schemas simultaneously and collaborating across teams.
Schema development can stall without the clear cross-team communication needed to understand, verify, and track changes.## Schema proposals for schema change managementGraphOS schema proposals provide centralized schema change management.
The centralized proposal process fosters collaboration and strengthens schema governance:- Subgraph developers can propose changes in the context of the supergraph using automated checks and reviewer feedback for validation.
- Graph consumers can actively participate by commenting on, reviewing, and approving proposals.
- Graph owners and governance teams can use proposals to set standards and ensure only approved changes are published.This increased coordination improves design decisions and accountability, streamlining development cycles.## Benefits of native schema change managementManaging schema changes directly in GraphOS Studio provides the following benefits:- The proposal process uses GraphOS [schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks)—including [schema linting](https://www.apollographql.com/docs/graphos/platform/schema-management/linting)—at every step.
  * This minimizes the likelihood of errors and inconsistencies.
  * It also offers an immediate understanding of the changes' impacts on composition and client operations.
- Editing, reviewing, and approving changes in GraphOS allows for GraphQL-aware schema diffing.
  * For example, GraphOS diffs additions of new fields and types in the [proposals editor](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/create#edit-subgraph-schemas) as new fields and types, regardless of formatting.
  * In contrast, GraphQL-naive text diffing may not understand and diff changes unless they're conventionally formatted.
- Centralizing the schema change process consolidates a comprehensive audit trail of discussions and schema changes.## How schema proposals workTeam members [create](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/create), [review](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/review), and [approval](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/review/#approvals) schema proposals in GraphOS Studio. After approval, the team implements the proposal—including resolvers and any supporting code changes— before publishing the schema changes to GraphOS.Schema proposals—even [approved](https://www.apollographql.com/docs/graphos/delivery/schema-proposals/#proposal-statuses) ones—don't deploy any changes to your graph. Once a proposal is approved, your team must [implement and publish the changes](https://www.apollographql.com/docs/graphos/delivery/schema-proposals/implementation).[Org and graph admins](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles/#organization-wide-member-roles) can [configure schema checks](https://www.apollographql.com/docs/graphos/platform/schema-management/checks/#proposals-checks) to ensure an organization only publishes changes approved through a proposal.Before diving into schema proposal workflow, it's helpful to understand proposal statuses.### Proposal statusesStatus
Automatic or  manually set
Description##### DraftAutomatic at proposal creation but can be  manually resetDefault status upon creation until the proposal is ready for review.##### Open for feedbackManualSignals the proposal is ready for review.- If default reviewers are configured, they become assigned for review.##### ApprovedAutomaticSignals the minimum number of reviewers has approved the proposal.- If you've required default reviewer approval, at least one approval must be from a default reviewer.##### ImplementedAutomaticSignals all the proposal's changes have been&#x20;
published.&#x20;
&#x20;\- Implemented proposals can't receive further revisions.  -
Their status can't be updated.##### ClosedManualSignals the proposal is suspended or abandoned.&#x20;
&#x20;\- Closed proposals can't receive further revisions.  - You
can reopen a proposal by setting the status to  Draft or Open for feedback.A proposal doesn't have to progress linearly from **Draft** to **Implemented**. For example, it may be **Closed** before returning to **Draft** and continuing through the process.Though not a status, you may see a **Conflict** indicator next to a proposal's status.
[Learn more about proposal conflicts.](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/implement#resolve-proposal-conflicts)### Proposal workflowSchema proposal statuses enable the following end-to-end schema change management workflow:```mermaid
graph LR
    subgraph Draft ["Proposal creation"]
    direction LR
    Creation["Start proposal"]
    DraftStatus(("Draft status"))
    Edit["Edit subgraphs, lint, <br/> save, and check changes"]
    Request["Request reviews"]
    Creation -->  DraftStatus --> Edit --> Request
    end
    class DraftStatus secondary;
    class DraftStatus CircleSize50;
``````mermaid
graph LR
    subgraph Open4Feedback ["Proposal review"]
    direction LR
    Feedback((Open for <br/>feedback <br/> status))
    Feedback1["Receive feedback "]
    Feedback2["Address feedback "]
    Approvals["Receive<br/>minimum approvals"]
    Feedback --> Feedback1 --> Feedback2 --> Approvals
    end
    class Feedback secondary;
    class Feedback CircleSize50;
``````mermaid
graph LR
    subgraph Approved ["Proposal implementation"]
    direction LR
    ApprovedStatus((Approved <br/> status))
    Fetch["Fetch proposal and <br> implement locally"]
    Push["Run checks on <br> local changes"]
    Check[["GraphOS <br/> schema checks"]]
    ApprovedStatus --> Fetch --> Push --> Check
    end
    class ApprovedStatus secondary;
    class ApprovedStatus CircleSize50;
    class Check tertiary;
``````mermaid
graph LR
    subgraph Implemented ["Proposal publication"]
    direction LR
    Checks[["Schema checks <br/> pass"]]
    Publish["Publish schema <br/> to GraphOS"]
    Monitor[["GraphOS matches <br/> changes to proposals"]]
    ImplementedStatus((Implemented <br/> status))
    Checks --> Publish --> Monitor --> ImplementedStatus
    end
    class ImplementedStatus secondary;
    class ImplementedStatus CircleSize50;
    class Checks,Monitor tertiary;
```##### Legend```mermaid
graph TB
  Status((Proposal <br/> status))
  User["User action"]
  Automated[["Automated <br/> GraphOS action"]]
  class Status secondary;
  class Automated tertiary;
  User:::padding
  classDef padding padding-left:5em, padding-right:5em
```## Next stepsSchema proposal default configurations let you start using proposals out of the box. If you want to fine-tune your graph's proposal process, check out [Configure proposals](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/configure). Configurations include permissions, approval requirements, email notifications, and more.To learn more about each stage in the process, refer to the following articles:- [Propose changes](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/create/)
- [Review proposals](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/review)
- [Implement proposals](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/implement) (covers both implementation and publication)
