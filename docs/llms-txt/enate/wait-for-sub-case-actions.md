# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/wait-for-sub-case-actions.md

# 'Wait for Sub Cases to Complete' Actions

A ‘Wait for Sub Cases to Complete’ Action will wait for a specific Sub Case to reach completion before allowing the Case to move on to the next Action.

You can tell that an Action is a ‘Wait for Sub Cases to Complete’ Action because it will say 'Action is waiting for Sub Case to complete' in the Action's info card.

Once a ‘Wait for Sub Cases to Complete’ Action has been launched AND the Sub Case it has been set to wait for has been launched (either manually or through a 'Start Case' Action), the ‘Wait for Sub Cases to Complete’ Action will move into a state of 'Waiting'.&#x20;

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-Mahf7s_DMYD56EJBY03%2F-MahjL3C13RNC2jFgHiy%2Fimage.png?alt=media\&token=7d6c2eb3-78c8-4b0a-a6c5-6c79a272dbba)

Once the Sub Case is completed, the 'Wait for Sub Cases to Complete' Action will close automatically.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F2lWsvg9v2BZeS9KzHNTU%2Fimage.png?alt=media\&token=34c14e3e-b53d-45b7-9be2-b2ec7a456ecf)

You will be notified of this in the timeline as well.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKRXWFgDwBMN9znQAFTsC%2Fimage.png?alt=media\&token=27e8765e-75a2-443a-9e3f-8f1edbac5ea4)

If the Sub Case the 'Wait for Sub Cases to Complete’ Action is set to wait for it not available - either because it has not been launched or because it was resolved before the ‘Wait for Sub Cases to Complete’ Action was launched, the ‘Wait for Sub Cases to Complete’ Action will enter a state of 'To Do' and be assigned to a Queue where a user will pick it up and decide how to proceed.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-M_tt8kvvrs8MMHHKag6%2F-M_ttFIUdXov1PCb7v2Z%2Fimage.png?alt=media\&token=abd4dab3-54ef-4172-930a-09775d9106cd)

If you then try to set the 'Waiting for Sub Case to Complete' Action to 'Waiting', the Action will close as the Sub Case it is set to wait for hasn't been launched.

If the Action is not in a 'Wait for Sub Cases to Complete' state and the Sub Case for which it is waiting has been completed, a message will appear as 'Sub Case is completed' in the Info Card.

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-Mahf7s_DMYD56EJBY03%2F-MahjJ5dRBh27P7pDi6T%2Fimage.png?alt=media\&token=cf9a40b1-9f4e-4195-ae20-6b17596a4c90)

If you manually Resolve a ‘Wait for Sub Case to Complete’ Action, the Action will be marked as Resolved without the Sub Case having completed.

{% hint style="info" %}
Please note that if your system has been configured to auto-close a 'Wait for Sub Case to complete' Action (see here for more information about how to do that) and the Sub Case the 'Wait for Sub Cases to Complete’ Action is set to wait for is not available - either because it has not been launched or because it was resolved before the ‘Wait for Sub Cases to Complete’ Action was launched, the ‘Wait for Sub Cases to Complete’ Action will automatically move to a state of Closed. You will be notified of this in the timeline.
{% endhint %}
