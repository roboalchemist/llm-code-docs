# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/trigger-external-api-actions.md

# 'Trigger External API' Actions

Similar to other action archetypes, 'Trigger External API' actions can be used in Case processes, and are used for when you need to automatically call out to another system, passing data to it and potentially getting the external system to pass updated custom data back into Enate.&#x20;

For information on how to configure 'Trigger External API' Actions check out this [Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/external-api-action-info-tab) section.&#x20;

Sometimes there can be a delay when waiting for the external system to respond. When that happens, i.e. when the ‘Trigger External API’ Action is waiting for information to come back from an external system, the Action info card will display in Work Manager as being in a state of 'Waiting'.&#x20;

![](https://gblobscdn.gitbook.com/assets%2F-MR4uErt41EMkGUOTvyd%2F-McU3cKMEIYWF9riB2uC%2F-McU6B2BgbLS_LpfgULK%2Fimage.png?alt=media\&token=4712f166-4ffb-4165-a0b4-99f2ffa2fdd3)

When the external system ultimately responds to Enate with the data update, it will be with a marker to say whether it has been successful OR unsuccessful:

#### Response with Successful Completion <a href="#response-with-successful-completion" id="response-with-successful-completion"></a>

If the system is responding to say it has been successful, the Action will automatically move to a state of 'Closed', with a Resolution Method of 'Done Successfully'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9WvQ6V0GYb5oTaxfz%2Fassets--MR4uErt41EMkGUOTvyd--Me4nXVVivC9tN5_y8Tc--Me4pmsGKb7y-1iaOoRl-image.png?alt=media\&token=eb9f0713-10d4-4afa-8996-9674d14743f1)

**Response with Unsuccessful Completion**

If the system is responding to say it has been unsuccessful, the Action move into a state of 'To Do', with a reason of 'Updated by Integration'. The external API can also respond with additional information regarding why it was unsuccessful. This information will display in the Info card of the Action in the 'Rejected Reason' section.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9X5nHvRThI7f88B2F%2Fassets--MR4uErt41EMkGUOTvyd--Me4W11a8zINusWiW0PH--Me4XiRtr6apeOq2V0iB-image.png?alt=media\&token=12d32879-6acb-42ae-bd0b-77d468d74d0d)

If the Action isn't successful because it did not complete within the time set for it ([configured in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/external-api-action-info-tab)), then it will moved to a state of 'To Do' with a reason of 'Timeout' and it will allocate to a Queue / human user based on the configured allocation rules.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9XBIc1A2Oa-VxdDV1%2Fassets--MR4uErt41EMkGUOTvyd--Me4V2NPSrNWSL9p2SGv--Me4VnDXPrKFxOsTeN8b-image.png?alt=media\&token=0c092438-7226-4092-9f86-088a917edf73)

Such unsuccessful Actions will now effectively behave as a standard manual action.

{% hint style="info" %}
Please note that the Case owner will NOT be notified in these situations.
{% endhint %}

### Automatic Retries <a href="#automatic-retries" id="automatic-retries"></a>

If the Action is not able to connect to the external system, it will automatically retry connecting for a certain number of times, depending on how your system has been configured in Builder (see [here](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern) for more information). You will also be shown an error message bar on the Action showing:

* when the error occurred
* when the system will retry establishing a connection automatically
* how many times the system has automatically retried establishing a connection, and&#x20;
* how many times the system will automatically retry establishing a connection.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9XShUwr41of83YG-Q%2Fimage.png?alt=media\&token=4ab525b8-1ed6-4c83-9f38-4e528415296e)

You are able to manually retry establishing a connection from here too, by clicking the 'Retry' link in the error message.

{% hint style="info" %}
Please note that when you do a manual retry, this will be counted as an attempted retry and will therefore be included in the number showing how many times the system has 'automatically' retried establishing a connection.
{% endhint %}

If the Action fails to establish a connection following the automatic retries (e.g. if the retry setting is set to 5 and the system fails to establish a connection following 5 automatic retries), it will move to a state of 'Closed' with a resolution method of 'Not Done Successfully'.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9XbhYQw2hJBzskPeH%2Fimage.png?alt=media\&token=89a88b3e-e29b-4570-aca7-4657f9885178)

{% hint style="info" %}
In *this* circumstance of the Action failing to establish connection with the external system, this will escalate to the Case Owner, highlighting in the Action section of the Case screen that this Action was Closed  - Not Done Successfully.
{% endhint %}

When the Action receives the required information, it will close automatically.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Me9UJHfUOeZd0weDdKL%2F-Me9Xhjxo1mG2dqg6KMX%2Fimage.png?alt=media\&token=5c0f485e-9799-47dc-b20d-47e866bdca36)

#### Adjusting the retry settings in Builder during / after retries have begun <a href="#adjusting-the-retry-settings-in-builder-during-after-retries-have-begun" id="adjusting-the-retry-settings-in-builder-during-after-retries-have-begun"></a>

If the automatic retry setting in Builder is changed *after* the system has automatically retried establishing a connection with an external system, the following will occur:

If, for example, the retry setting was originally set to 5 and the system automatically retried establishing a    connection 5 times but failed, the Action will have moved to a state of Closed with an error message showing a retry count of 5/5.&#x20;

If the retry setting then gets subsequently increased to anything above 5, for example 7, the error message will display a retry count of 5/7, but the system will NOT automatically retry establishing a connection for a 6th and 7th time as the Action is already closed.&#x20;

However, if the Action had not yet moved to a state of Closed because it had not yet reached the maximum number of automatic retries (e.g. it had only retried 4 times out of the 5), then increasing the retry setting to 7 means that the Action will automatically retry establishing connecting until the count has reached 7. &#x20;

Conversely, if you reduce the retry setting after retries have started, e.g. you're on retry 4 of 10 but then reduce the max down to 4, the system will still display 4 of 10 but will in fact be closed.
