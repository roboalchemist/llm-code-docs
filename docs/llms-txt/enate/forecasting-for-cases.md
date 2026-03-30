# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/forecasting-for-cases.md

# Forecasting for Cases

### Overview <a href="#overview" id="overview"></a>

For users on v2024.1, they will be able to use the forecasting feature to provide more accurate estimated efforts for work items, enabling you to plan resource requirements more effectively.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTY5NTg1MQ==>" %}

In the long term, this data can be collated and fed back to admin users to adjust estimated effort timers and to provide more accurate forecasting for future work volumes.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvYu2IZLWf97qZhW7HKNF%2Fimage.png?alt=media&#x26;token=f2546618-a6fc-4dd1-a5bf-4404a2d37c53" alt=""><figcaption></figcaption></figure>

### How to use 'Forecasting' <a href="#how-to-use-forecasting" id="how-to-use-forecasting"></a>

Once the 'Forecasting' feature has been switched on, a new ‘Effort Estimation’ tab will appear in Cases in Work Manager.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F1296463846-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8xJkS0SKlesb8bmVBtGc%252Fuploads%252FLcrJP0VJlGg4kAY1Kh36%252Fimage.png%3Falt%3Dmedia%26token%3D1cc56faf-d835-4c13-ae54-761ca7ab600d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=a853b182&#x26;sv=1" alt=""><figcaption></figcaption></figure>

Here you'll see a summary of the estimated effort for the whole Case, a breakdown of the estimated effort for Actions or Sub Cases that make up the Case, and a breakdown of the estimated effort for Actions or Sub Cases that have not been created yet.

#### Case Effort Summary <a href="#case-effort-summary" id="case-effort-summary"></a>

The 'Case Effort Summary' section is where a user can change the estimated time for the Case. It also provides other useful metrics for the Case.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F076Y9o6GftPK7jbqjQOC%2Fimage.png?alt=media&#x26;token=ea15329e-c2b6-431a-aa06-04fdf2614ee8" alt=""><figcaption></figcaption></figure>

* 'Total Case Estimated Effort' effort shows the total estimated time that the Case is estimated to take. This can be updated by a user with a more accurate estimate.
  * It is the sum of the ‘Estimated’ effort of all the created work and the Actions (and Sub Case Actions) that make up the Case and the and the 'Effort for Work Not Yet Created' value
  * The field will will initially show the manual ‘[Initial Estimated Effort Per Record](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)’ value from Builder (if there is one) multiplied by the [record count](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
    * If the ‘Record Count’ gets updated, the ‘Estimated Effort’ for the Case that has not been updated by a Work Manager user will be updated to reflect the change in record count.
  * Once the Case is in a state of Resolved or Closed, its estimated effort can no longer be changed.
  * Note that increasing this value will increase the ‘Effort for Work Not Yet Created’ estimate and vice versa.
* ‘Total Case Actual Effort’ effort shows the amount of time that has been spent working on the Case Effort for Work Not Yet Created.
  * It is the sum of the 'Actual' effort for all the created Actions and Sub Cases that make up the Case, taken from their respective Time Trackers.
* ‘Total Case Remaining Effort’ shows the amount of time estimated to be left on the Case.
  * It is the sum of the 'Total Remaining Effort' effort for all the created Actions and Sub Cases that make up the Case AND the estimated remaining time for work that has yet to be created (therefore it might not always equal the 'Case Estimated' effort minus the 'Case Actual' effort).

Changing the 'Estimated' effort value for a Case has the following effects:

* Automatic update to the[ 'Effort for Work Not Yet Created' estimated value](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases#effort-for-work-not-yet-created). This is because the ‘Estimated Effort’ for the Case is a calculated value made up of the sum of the ‘Estimated’ effort of all the created work and the Actions (and Sub Case Actions) that make up the Case and the and the 'Effort for Work Not Yet Created' value.
  * Increasing the 'Estimated' effort for a Case increases the 'Effort for Work Not Yet Created' value by the same amount
  * Decreasing the 'Estimated' effort for a Case decreases the 'Effort for Work Not Yet Created' value by the same amount

#### Effort Breakdown for Created Work <a href="#effort-breakdown-for-created-work" id="effort-breakdown-for-created-work"></a>

The 'Effort Breakdown for Created Work' section is where a user can change the estimated time for the individual created Actions (and Sub Cases) that make up the Case. It also shows other useful metrics for each of the created Actions (and Sub Cases) that make up the Case.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F1296463846-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8xJkS0SKlesb8bmVBtGc%252Fuploads%252Fcnl0uwHUp7VMtMmKE9yY%252Fimage.png%3Falt%3Dmedia%26token%3D480399c4-1766-46b6-95c9-635bf60a6ad8&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=29471a23&#x26;sv=1" alt=""><figcaption></figcaption></figure>

Note that once an Action is in a state of Resolved or Closed, its estimated effort can no longer be changed.

As Actions (and Sub Cases) get created, the estimated effort for them will be taken from the Estimated effort value from the Work Not Yet Created section below.

**Action Breakdown**

For each Action, you'll see:

* A link to each Action
* 'Estimated' effort that shows the total estimated time that the Action is estimated to take. This can be updated by a user with a more accurate estimate.
  * The field will will initially show the manual ‘[Initial Estimated Effort Per Record](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)’ value from Builder multiplied by the [record count](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
    * If the ‘Record Count’ gets updated, the ‘Estimated Effort’ for any running Actions that have not been updated by a Work Manager user will be updated to reflect the change in record count.
  * Increasing this value will decrease the ‘Work Not Yet Created’ estimate and vice versa and therefore might affect the total 'Case Estimated' effort
  * Note that once an Action is in a state of Resolved or Closed, its estimated effort can no longer be changed.
* ‘Actual’ effort shows the amount of time that has so far been spent working on that Action
  * The value is taken from the Time Tracker of the Action.
* ‘Estimated Remaining’ shows the amount of time estimated to be left on the Action.
  * It is calculated by subtracting the 'Actual' effort for the Action from the 'Estimated' effort.
* The due date of the Action
  * You'll also see a 'Start By' value if the 'Actual' effort is currently zero. This value show when is the absolute latest that the Action can be started by in order to meet its due date.
* The status of the Action

Changing the 'Estimated' effort value for an Action has the following effects:

* Automatic update to the 'Effort for Work Not Yet Created' estimated value for the Case.
* Possible automatic update to the 'Estimated' effort for the whole Case

Details:

* Decreasing the 'Estimated' effort for an Action increases the 'Effort for Work Not Yet Created' value for the Case by the same amount (leaving the 'Estimated' effort for the whole Case the same).
* Increasing the 'Estimated' effort for an Action decreases the 'Effort for Work Not Yet Created' value for the Case by the same amount. This may or may not affect the 'Estimated' effort for the overall Case.
  * If the updated ‘Estimated Effort’ on an Action doesn't increase by enough to cause the ‘Effort for Work Not Yet Created’ value for the Case to go below 0, the 'Estimated' effort for the Case will not be affected
    * Example: let's say that the 'Estimated' effort for Action 1 is 2 hours, the estimated 'Effort for Work Not Yet Created' is 1 hour and the 'Estimated Effort' for the Case is 3. A user decides that Action 1 is going to take 1 hour more and so updated the 'Estimated' effort for Action 1 from 2 to 3 hours. 'Effort for Work Not Yet Created' will decrease from 1 hour to 0 and the 'Estimated' effort for the Case will not change - it will stay at 3 hours.
  * If the updated ‘Estimated Effort’ on an Action increases enough to cause the ‘Effort for Work Not Yet Created’ value for the Case to go below 0, the difference should be added to the ‘Estimated Effort’ of the overall Case.
    * Example: let's say that a Case only has one Action created for it called Action 1. The 'Estimated' effort for Action 1 is 2 hours, the estimated 'Effort for Work Not Yet Created' is 0 and therefore the 'Estimated Effort' for the whole Case is 2 hours. A user decides that Action 1 is going to take 1 hour more and so updates the 'Estimated' effort for Action 1 from 2 to 3 hours. Because 'Effort for Work Not Yet Created' is 0, the 'Estimated' effort for the overall Case is therefore going to increase by 1 hour from 2 to 3 hours.
    * Example 2: let's say that a Case only has one Action created for it called Action 1. The 'Estimated' effort for Action 1 is 2 hours, the estimated 'Effort for Work Not Yet Created' is 1 hour and therefore the 'Estimated Effort' for the whole Case is 3 hours. A user decides that Action 1 is going to take 2 more hours and so updates the 'Estimated' effort for Action 1 from 2 to 4 hours, causing the 'Effort for Work Not Yet Created' to decrease by 1 hour from 1 to 0 (decreasing as far as it can). The "remaining" 1 hour will effectively be added to the total 'Estimated' effort of the Case that will increase by 1 hour to from 3 to 4 hours.

**Sub Case Breakdown**

If a Sub Case gets created, you'll see:

* A link to the Sub Case if you have permission to access it (otherwise you'll just see the name and reference number of the Sub Case with no link)
* A Sub Case "total" row with the following:
  * 'Estimated' effort shows the total estimated time that the Sub Case is estimated to take. This can be updated by a user with a more accurate estimate.
    * It is the sum of the ‘Estimated’ effort of all the created and yet-to-be created Actions that make up the Sub Case.
    * The field will initially show the manual ‘[Initial Estimated Effort Per Record](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)’ value from Builder multiplied by the [record count](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
      * If the ‘Record Count’ gets updated, the ‘Estimated Effort’ for the Sub Case that has not been updated by a Work Manager user will be updated to reflect the change in record count.
    * Once a Sub Case is in a state of Resolved or Closed, its estimated effort can no longer be changed.
    * Note that increasing this value will increase the ‘Work Not Yet Created’ estimate for the Sub Case and vice versa.
  * ‘Actual’ effort shows the amount of time that has so far been spent working on the Sub Case.
    * It is the sum of the 'Actual' effort for all the created Actions that make up the Sub Case, taken from their respective Time Trackers.
  * ‘Estimated Remaining’ shows the amount of time estimated to be left on the Sub Case.
    * It is the sum of the 'Estimated Remaining' effort for all the created Actions that make up the Sub Case AND the estimated remaining time for work that has yet to be created for that Sub Case (therefore it might not always equal the 'Sub Case Estimated' effort minus the 'Sub Case Actual' effort)
    * The due date of the Sub Case
    * The status of the Sub Case
* A row for each Sub Case Action with the following:
  * 'Estimated' effort shows the total estimated time that the Sub Case Action is estimated to take. This can be updated by a user with a more accurate estimate.
    * The field will will initially show the manual ‘[Initial Estimated Effort Per Record](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/estimated-effort-enhancements)’ value from Builder multiplied by the [record count](https://docs.enate.net/whats-new/2024.1/2024.1-changes-overview/new-feature-forecasting-feature-for-cases/record-count-enhancements)
      * If the ‘Record Count’ gets updated, the ‘Estimated Effort’ for any running Sub Case Actions that have not been updated by a Work Manager user will be updated to reflect the change in record count.
    * Increasing this value will decrease the ‘Work Not Yet Created’ Sub Case estimate and vice versa and therefore might affect the total 'Sub Case Estimated' effort
    * Once an Action is in a state of Resolved or Closed, its estimated effort can no longer be changed.
  * ‘Actual’ effort shows the amount of time that has so far been spent working on that Sub Case Action
    * The value is taken from the Time Tracker of the Sub Case Action.
  * ‘Estimated Remaining’ shows the amount of time estimated to be left on the Sub Case Action.
    * It is calculated by subtracting the 'Actual' effort for the Sub Case Action from the 'Estimated' effort.
  * The due date of the Sub Case Action
    * You'll also see a 'Start By' value if the 'Actual' effort is currently zero. This value show when is the absolute latest that the Sub Case Action can be started by in order to meet its due date.
  * The status of the Sub Case Action
* A row for 'Sub Case Work Note Yet Created' with the following:
  * 'Estimated' effort shows how much effort is estimated to be needed to complete the Sub Case Actions that have not yet been created for that Sub Case. This can be updated by a user with a more accurate estimate.
    * Changing this estimate will affect the total 'Sub Case Estimated' effort and might affect the effort estimate for the overall Case

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F1296463846-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8xJkS0SKlesb8bmVBtGc%252Fuploads%252F2WtIv48Khiu9x4nLa0vG%252Fimage.png%3Falt%3Dmedia%26token%3D07b13647-afaa-482c-bbf8-b0be5aa8761e&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6df3f1bd&#x26;sv=1" alt=""><figcaption></figcaption></figure>

Changing the 'Estimated' effort value for a Sub Case Action has the following effects:

* Automatic update to the 'Effort for Work Not Yet Created' estimated value for the Sub Case.
* Possible automatic update to the 'Estimated' effort for the whole Sub Case
* Possible automatic update to the 'Estimated' effort for the whole parent Case.

Details:

* Decreasing the 'Estimated' effort for a Sub Case Action increases the 'Effort for Work Not Yet Created' value for the Sub Case by the same amount (leaving the 'Estimated' effort for the whole Sub Case the same and therefore having no impact on the 'Estimated' effort for the whole parent Case).
* Increasing the 'Estimated' effort for a Sub Case Action decreases the 'Effort for Work Not Yet Created' value for the Sub Case by the same amount. This may or may not affect the 'Estimated' effort for the overall Case.
  * If the updated ‘Estimated Effort’ on a Sub Case Action doesn't increase by enough to cause the ‘Effort for Work Not Yet Created’ value for the Sub Case to go below 0, the 'Estimated' effort for the Sub Case will not be affected (and therefore the 'Estimated' effort for the whole parent Case will not be affected).
    * Example: let's say that a Sub Case only has one Action created for it called Sub Case Action 1. The 'Estimated' effort for Sub Case Action 1 is 2 hours and the estimated 'Effort for Work Not Yet Created' for the Sub Case is 1 hour, therefore the 'Estimated Effort' for the Sub Case is 3 hours. A user decides that Sub Case Action 1 is going to take 1 hour more and so updates the 'Estimated' effort for Sub Case Action 1 from 2 to 3 hours, causing the 'Effort for Work Not Yet Created' for the Sub Case to decrease from 1 hour to 0. The 'Estimated' effort for the Sub Case will not change - it will stay at 3 hours (and therefore the 'Estimated' effort for the whole parent Case will not be affected).
  * If the updated ‘Estimated Effort’ on a Sub Case Action increases enough to cause the ‘Effort for Work Not Yet Created’ value for the Sub Case to go below 0, the difference should be added to the ‘Estimated Effort’ of the overall Sub Case, (and therefore might impact the 'Estimated' effort for the whole parent Case).
    * Example: let's say that a Sub Case only has one Action created for it called Sub Case Action 1. The 'Estimated' effort for Sub Case Action 1 is 2 hours and the estimated 'Effort for Work Not Yet Created' for the Sub Case is 0, therefore the 'Estimated' effort for the overall Sub Case is 2 hours. A user decides that Sub Case Action 1 is going to take 1 more hour and so updates the 'Estimated' effort for Sub Case Action 1 from 2 to 3 hours. Because 'Effort for Work Not Yet Created' for the Sub Case is 0, the 'Estimated' effort for the Sub Case is going to increase by 1 hour from 2 to 3 hours.
      * If there is enough time in the 'Effort for Work Not Yet Created' of the parent Case, this 1 hour increase might be taken from there, therefore there will be no impact on the 'Estimated' effort for the whole parent Case.
      * If there is isn't enough time in the 'Effort for Work Not Yet Created' of the parent Case, this 1 hour increase will result in an increase in the the 'Estimated' effort for the whole parent Case.
    * Example 2: let's say that a Sub Case only has one Action created for it called Sub Case Action 1. The 'Estimated' effort for Sub Case Action 1 is 2 hours and the estimated 'Effort for Work Not Yet Created' for the Sub Case is 1 hour, therefore the 'Estimated' effort for the overall Sub Case is 3 hours. A user decides that Sub Case Action 1 is going to take 2 more hours and so updated the 'Estimated' effort for Sub Case Action 1 from 2 to 4 hours, causing the 'Effort for Work Not Yet Created' for the Sub Case to decrease as much as it can - here it will decrease by 1 hour to from 1 to 0. The "remaining" 1 hour will effectively be added to the total 'Estimated' effort of the Sub Case that will increase by 1 hour from 3 to 4 hours.
      * If there is enough time in the 'Effort for Work Not Yet Created' of the parent Case, this 1 hour increase might be taken from there, therefore there will be no impact on the 'Estimated' effort for the whole parent Case.
      * If there is isn't enough time in the 'Effort for Work Not Yet Created' of the parent Case, this 1 hour increase will result in an increase in the the 'Estimated' effort for the whole parent Case.

#### Effort for Work Not Yet Created <a href="#effort-for-work-not-yet-created" id="effort-for-work-not-yet-created"></a>

The 'Effort for Work Not Yet Created' section shows how much effort is estimated to be needed to complete Actions (and Sub Cases Actions) that have not yet been created for this Case.

It is calculated by subtracting the sum of the 'Estimated' effort for created work from the 'Estimated' effort for the Case. Therefore, increasing the 'Effort for Work Not Yet Created' will increase the effort estimate for the overall Case and vice versa.

As Actions (and Sub Cases) get created, the estimated effort for them will be taken from the 'Estimated Effort for Work Not Yet Created' value.

Once the Case is in a state of Resolved or Closed, the 'Effort for Work Not Yet Created' can no longer be changed.

<figure><img src="https://docs.enate.net/~gitbook/image?url=https%3A%2F%2F1296463846-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8xJkS0SKlesb8bmVBtGc%252Fuploads%252FZO0iZKS9meBe6c1Gddtg%252Fimage.png%3Falt%3Dmedia%26token%3D607ac07a-137e-48df-a68b-adaf65cf1176&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=46bdfea5&#x26;sv=1" alt=""><figcaption></figcaption></figure>
