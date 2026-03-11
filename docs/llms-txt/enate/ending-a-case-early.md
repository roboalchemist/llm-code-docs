# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/ending-a-case-early.md

# Ending a Case Early

## Overview

You also have the ability to end an individual Case early (if it is no longer needed) when you're setting up a Case process. This mean that at runtime the Case doesn't have to always continue until the end of the flow in order to close.

This is useful in circumstances where it is no longer relevant to complete the Case, for example it's no longer relevant to complete a New Starter Induction Case if the person is no longer joining the company.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtRMeF05iFQBL7dpkVmhS%2Fimage.png?alt=media&#x26;token=e7a8fb9d-7b32-4ecc-b358-7722b6ce0245" alt=""><figcaption></figcaption></figure>

At runtime in Work Manager, once an 'End Case' Action is reached in a process, no further Actions in the Case flow are triggered and the Case will Close.

## Configuring an End Case Action

To add this ability into your Case flow processes, you just need to add the new 'End Case' Action type into the relevant place in your Case process flow in Builder. Multiple 'End Case' Actions can be added to a Case flow, however note that:&#x20;

* they must be added at the end of a branch AND
* no other Actions can be added after it in the branch's flow.&#x20;

You should use End Case Actions in conjunction with a condition in your flow configuration. Watch this video for more information about how to configure an End Case Action:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM4MjA4Nw==>" %}

## Work Manager Impact

When a Case closes due to it reaching an End Case Action, the Case will display as being Closed with a reason of 'All relevant Actions completed'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVgk4hqZDG54oi5ViTySJ%2Fimage.png?alt=media&#x26;token=996f28d8-f5fa-49fa-bf19-aa0a26abcb13" alt=""><figcaption></figcaption></figure>

If a feedback window is configured for the Case, the Case will instead move to a Resolved state and will follow standard system logic i.e. it will sit in this status for a defined period of time during which the service recipient may respond and the Case may be reopened, either automatically upon receipt of a new incoming email or feedback within the time period, or manually by the agent.&#x20;

If the feedback window has completed without any further response, or if the Case does not have a feedback window, the Case will move to a state of fully 'Closed'.&#x20;

See this article for more information about how Cases are processed in Enate:

{% embed url="<https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/processing-a-case>" %}

{% hint style="info" %}
Note that End Case Actions will not be available to Work Manager users to manually create on an ad-hoc basis. Also, it is not possible to rework a Case from an End Case Action. &#x20;

Additionally, if a Case ends as a result of an End Case Action, this will have no impact on its linked work items and if a Sub-Case ends as a result of an End Case Action, this will have no impact on its parent Case.
{% endhint %}
