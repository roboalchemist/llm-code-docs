# Storybook Documentation
# Source: https://storybook.js.org/docs/contribute/RFC
# Page: /docs/contribute/RFC

# RFC process

The RFC (Request for Comment) process is intended to provide a consistent and controlled path for new features to enter the project. It helps ensure that new features are well-designed, well-implemented, and well-tested, and they do not conflict with the project's overall direction and scope.

## 

Goal

Many changes, such as bug fixes and documentation improvements, can be implemented and reviewed via the normal GitHub pull request workflow. Some changes, however, are considered “substantial”, and we ask that these undergo a design process, solicit community input, and reach a consensus among the Storybook core team.

The purpose of the RFC (Request for Comment) process is to:

  * Provide a transparent system for proposing new feature ideas.
  * Establish a reliable and well-regulated process for introducing new features into the project.
  * Provide a way for the community to participate in developing new features.



### 

“Feature Request” vs. “RFC”

A _feature request_ is a straightforward and relatively informal way for Storybook users to suggest a new feature or enhancement to the project. While feature requests can provide valuable insights and ideas, they typically do not involve an in-depth design process or require consensus among the core team. Feature requests are usually open to discussion and may or may not be implemented based on factors like popularity, feasibility, and alignment with the project's goals.

On the other hand, an _RFC_ is a more formalized and structured process for proposing substantial changes or additions to the project. It involves following a defined set of steps to ensure that the proposed feature or modification receives proper consideration, design, and feedback. RFCs are typically used for changes that significantly impact the project, such as introducing new API functionality, removing existing features, or establishing new usage conventions. The RFC process aims to foster discussions, gather feedback from a wider audience, and reach consensus among the core team before integrating the proposed change into the project. Accepted RFCs are more likely to be implemented than regular feature requests.

## 

The RFC lifecycle

### 

1\. `Status: Proposed`

Open a new GitHub discussion in the [“RFC” category](https://github.com/storybookjs/storybook/discussions/new?category=rfc). Fill out the form as instructed.

_Details matter_ : RFCs that do not present convincing motivation, demonstrate a lack of understanding of the design's impact, or are disingenuous about the drawbacks or alternatives tend to be poorly received.

### 

2\. `Status: In review`

RFCs tend to remain in this stage for a while, giving the community and core team members time to weigh in. During this period, the author of an RFC should be prepared to revise the proposal, integrate feedback, and build consensus. RFCs that have broad support are much more likely to make progress than those that don't receive any comments.

Every week, the Storybook core team conducts a triage meeting to review open RFCs as part of the meeting's agenda. The event is publicly scheduled in the [Storybook Discord](https://discord.gg/storybook) and held in the [Storybook Discord's Watercooler channel](https://discord.com/channels/486522875931656193/486522876388704260). We invite the RFC author(s) and interested members of the community to participate and engage in a more detailed discussion of the RFC. If a core team member deems it necessary, they will be assigned as the "champion" of the RFC. The champion will collaborate with the RFC author and assist them throughout the RFC process.

### 

3\. `Status: accepted/rejected`

Eventually, the team will decide whether the RFC is a candidate for inclusion in Storybook. On the other hand, an RFC may be rejected by the team after a public discussion has settled and comments have been made summarizing the rationale for rejection.

## 

Implementing an accepted RFC

The author of an RFC is not obligated to implement it. Of course, the RFC author (like any other developer) is welcome to post an implementation for review after the RFC has been accepted. However, note that the “accepted” status does not indicate priority nor whether it’s being actively worked on.

If you are interested in implementing an "active" RFC, but cannot determine if someone else is already working on it, feel free to ask (e.g., by leaving a comment on the associated issue).

This RFC process took heavy inspiration from the RFC processes from [Rust](https://github.com/rust-lang/rfcs) and [Gatsby](https://www.gatsbyjs.com/contributing/rfc-process/).

**Learn more about contributing to Storybook**

  * RFC process for authoring feature requests
  * [Code](./code) for features and bug fixes
  * [Frameworks](./framework) to get started with a new framework
  * [Documentation](./documentation/documentation-updates) for documentation improvements, typos, and clarifications
  * [Examples](./documentation/new-snippets) for new snippets



Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/contribute/RFC.mdx)