# Source: https://docs.frigade.com/platform/targeting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Targeting

Use targeting to personalize Flows to different cohorts of users, seamlessly link multiple onboarding experiences together, and define completion criterias for a Step in a Flow.

## Flow targeting

***

You can optionally add targeting to every Flow you create. You can view and edit this targeting logic on the **Targeting** tab of the Flow detail page. The Flow targeting logic is used to determine who should see the Flow.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3ff629c1598a46737aad2579fcd342b1" alt="Flow Targeting" data-og-width="3456" width="3456" data-og-height="1926" height="1926" data-path="images/platform/flow-detail-audience.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6be15fee4c76d9da2cd14014ff762843 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=59a1aeb9087ce79ce5e731351740b43f 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6430d0069d4fb14ef1a4271bdee6c85f 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=25d1e7ec6bd9d9ffc8fd030b1a05a7f6 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5ad647ada4e6bf57add11f123df68e43 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=d05ba711ef7422ebb937b35ea9b75ad6 2500w" />
</Frame>

### Example use cases

Here are some common ways we see developers using Flow targeting:

* Only show a Flow to newly created accounts
* Show a Flow to users with a certain job function or user property
* Show a Flow to users who have taken a specific action in the product (e.g. an upsell once they use something 10 times)
* Show a Flow to users who have completed another Flow (e.g. a "next steps" Flow after a user completes an initial onboarding Flow)
* Show a Flow only after X days have passed since completing another Flow

<Note>Refer to the users [SDK](/sdk/hooks/user) and [API](/api-reference/users) for more info on using properties and events in targeting</Note>

## Step targeting

***

You can also leverage targeting logic within the Steps of a Flow by using the Advanced Editor.

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=614526d567e2202cecc1458859c34581" alt="Step visibility" className="rounded-lg" style={{border: '1px solid #D3D3D3',}} data-og-width="1639" width="1639" data-og-height="596" height="596" data-path="images/platform/flow-detail-yaml-step-visibility.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7fffa9c7035df77c5c64670f32af26b9 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=22ae0823c1ba68267b53f43d5c40c23b 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9723d7b4190517b5666fca65fa66e056 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=081169fc1a9b8a70c4717383eaf3f50c 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1b8e6f3daa1da0d9742c54e19fd5a090 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-yaml-step-visibility.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f801f71c7bbdc48acaa50c03b59f96b0 2500w" />
</Frame>

### Example use cases

Here are some common ways we see developers using Step targeting:

* Mark a Step complete based on a condition [using steps\[\].completionCriteria](/sdk/advanced/completing-a-step#automatically-marking-steps-complete)
* Show or hide a Step based on a condition [using steps\[\].visibilityCriteria](/component/tour#flow-configuration)
* Mark a Step started based on a condition [using steps\[\].startCriteria](/component/tour#flow-configuration)

## User props

***

All data you've made available to Frigade can be used in your targeting logic, including the properties below supported on [users](/sdk/hooks/user). You can also sync with your [existing analytics platform](/integrations/) to leverage [user properties and events](/sdk/hooks/user) you're already tracking.

<ParamField body="user.flow('<flowId>')">User Flow state (e.g. `COMPLETED_FLOW`)</ParamField>
<ParamField body="user.flowStep('<flowId>', '<stepId>')">User Flow Step state (e.g. `COMPLETED_STEP`)</ParamField>
<ParamField body="user.flowStepData('<flowId>', '<stepId>', '<fieldId>')">Data collected from in a specific step (e.g. form data)</ParamField>
<ParamField body="user.event('<eventId>').count">User event count</ParamField>
<ParamField body="user.property('<property>')">User properties</ParamField>
<ParamField body="user.propertyContains('<property>', '<searchString>')">User properties partial match (<Tooltip tip="Not case-sensitive. Returns true or false.">more</Tooltip>). It supports searching in strings, objects, and arrays.</ParamField>
<ParamField body="user.currentUrl()">Current URL of the user</ParamField>

## Group props

***

All data you've made available to Frigade can be used in your targeting logic, including the properties below supported on [groups](/sdk/hooks/group). You can also sync with your [existing analytics platform](/integrations/) to leverage [group properties and events](/sdk/hooks/group) you're already tracking

<ParamField body="group.property('<property>')">Group properties</ParamField>
<ParamField body="group.event('<eventId>').count">Group event count</ParamField>

## Boolean logic and operators

***

Supported operators are: `&&`, `||`, `==`, `!=`, `>`, `<`, `>=`, `<=`, `contains`, `!contains`,  `endsWith`, `!endsWith`, `startsWith`, `!startsWith`, `within`, `!within`

## Examples

***

Here are some examples of some of the most popular targeting logic we see developers using.

#### Relative dates

You can use relative dates in your targeting logic similar to how this is handled in [plain Javascript](https://stackoverflow.com/questions/7763327/how-to-calculate-date-difference-in-javascript).
For example, you can target users who are younger than at least 30 days:

```javascript  theme={"system"}
user.property('accountCreatedDate') within 30d
```

Or target users who are older than 30 days:

```javascript  theme={"system"}
user.property('accountCreatedDate') !within 30d
```

This behavior also works for targeting users who have completed a Flow within as certain time frame:

```javascript  theme={"system"}
user.flow('flow_i6kH7DjcbE6tiaQd') !within 4w
```

#### Property matching

Target a Flow to a user who has connected their bank account:

```javascript  theme={"system"}
user.property('bankAccountConnected') == true
```

#### Check if a property is present

Target a Flow to a user who has a job title:

```javascript  theme={"system"}
user.property('jobTitle') != null
```

#### Absolute dates

Target a Flow only for users signed up after a certain date:

```javascript  theme={"system"}
user.property('accountCreatedDate') > '2023-03-01 00:00:00'
```

#### Flow state

Target a Flow to a user who has completed another onboarding Flow already and has connected a bank account:

```javascript  theme={"system"}
user.flow('flow_i6kH7DjcbE6tiaQd') == 'COMPLETED_FLOW' && user.property('bankAccountConnected') == true`
```

Target a Flow when a Step in another Flow is completed:

```javascript  theme={"system"}
user.flowStep('flow_i6kH7DjcbE6tiaQd', 'my-step-id') == 'COMPLETED_STEP'
```

Target the output of a previous step in the same Flow:

```javascript  theme={"system"}
user.flowStepData('flow_i6kH7DjcbE6tiaQd', 'my-step-id', 'my-field-id') == 'some-value'
```

#### Event counts

If the event properties do not matter and you simply wish to see if a user has triggered an event, you can use the following expression:

```javascript  theme={"system"}
user.event('pageView').count > 0
```

Automatically trigger when a group/organization sends a specific event:

```javascript  theme={"system"}
group.event('connectedBankAccount').count > 0
```

#### Current URL

Target based on the current URL contains a specific string:

```javascript  theme={"system"}
user.currentUrl() contains 'example.com'
```

Target based on the current URL ends with a specific string:

```javascript  theme={"system"}
user.currentUrl() endsWith '?myParam=123'
```
