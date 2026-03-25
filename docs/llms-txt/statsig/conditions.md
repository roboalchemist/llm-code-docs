# Source: https://docs.statsig.com/feature-flags/conditions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Feature Gate rule criteria

> Statsig feature gates contain a list of rules that are evaluated in order from top to bottom. This page describes in more detail how these rules are evaluated and lists all currently supported conditions.

Statsig feature gates contain a list of rules that are evaluated in order from top to bottom. The page describes in more detail how these rules are evaluated and lists all currently supported conditions.

## Rule Evaluation

The rules that you create are evaluated in the order they're listed. For each rule, the **criteria** or **conditions** determine which users *qualify* for the Pass/Fail treatments. The Pass percentage further determines the percentage of *qualifying* users that will be exposed to the new feature. The remaining *qualifying* users will see the feature disabled.

Suppose you set up your rules as shown below, the following flow chart illustrates how Statsig evaluates these rules.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/example-rules-gate.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=a00b929a6b656d594b72fc6143ee1622" alt="Example Rules Gate" width="1298" height="1029" data-path="images/conditions/example-rules-gate.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/rules-evaluation-flowchart.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=af57482197fe2f9cde5b947106254072" alt="Feature gate rules evaluation flowchart" width="3566" height="2264" data-path="images/conditions/rules-evaluation-flowchart.png" />
</Frame>

Note that as soon as a user qualifies based on the condition in a given rule, Statsig doesn't evaluate subsequent rules for this user. Statsig then picks the qualifying user to be in either the Pass or Fail group of that rule.

Also note that in the example, the third rule for **Remaining Folks** captures all users who don't qualify for previous two rules. If we were to remove this third rule, then only a subset of your users (users in pools 1 and 2) would qualify for this feature gate and for further analysis, not your total user base.

### Client vs Server SDKs

All of the following conditions work on both client and server SDKs. Client SDKs handle these conditions a bit more automatically for you - if you do not provide a userID, client SDKs rely on an auto-generated "stable identifier" which is persisted to local storage.
In addition, if you do not automatically set an IP or User Agent (UA), the client SDK will infer these attributes from the request IP and UA. Similarly, on mobile, the client SDK will automatically pass your app version and locale to the server so conditions using these attributes can be evaluated without having to set them explicitly.

### Stability

Evaluations at a given percentage are *stable* with respect to the unitID. For example, if the gate/config/experiment/layer has a unit type of "userID", and userID = 4 passes a condition at a 50% rollout, they will always pass at that 50% rollout. The same applies for `customIDs`, if the unit type of the entity is that `customID`. Want to reset that stability? See "Resalting" below.

### Resalting

Gate evaluations are stable for a given gate, percentage rollout, and user ID. This is made possible by the salt associated with a feature gate. If you want to reset a gate, triggering a reshuffle of users, you can "resalt" a gate from the dropdown menu in the top right of the feature gate details page.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/resalt-ui.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=852ddc9b0652ed8fd6d1840e6cb86986" alt="Resalt UI" width="608" height="364" data-path="images/conditions/resalt-ui.png" />
</Frame>

### Partial Rollouts

While 0% or 100% rollouts for gates are simply "on for users matching this rule"/"off for users matching this rule", each rule allows you to specify a percentage of qualifying users who should pass (see the new feature).
If you want to get [Pulse Results](/pulse/read-pulse) (metric movements caused by a feature), simply specifying a number between 0% and 100% will create a random allocation of users in Pass/Fail or "test"/"control" groups for a simple A/B test.
You can use this to validate that a new feature does not regress existing metrics as you roll it out to everyone. Statsig suggests a 2% -> 10% -> 50% -> 100% roll out strategy. Each progressive roll out will generate its own Pulse Results as shown below.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/metric-lifts.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=818567c274934264e35bb0a52beea6cd" alt="Metric Lifts" width="683" height="326" data-path="images/conditions/metric-lifts.png" />
</Frame>

### User Object Fields

Evaluation uses the set of properties defined in the [StatsigUser object](/concepts/user). There are a set of reserved top-level fields, but these keywords are reserved and recognized in the `custom` and `privateAttributes` maps as well.

For example, if you set `user.country`, `user.custom.country` OR `user.privateAttributes.country`, it will be used to evaluated a country condition in any of those places (and in that order! top level > custom > privateAttributes), case insensitively. So if user.country is not defined, but user.custom.COUNTRY is, that will be used to evaluate a country condition.

## Supported Conditions

### User ID

Usage: Simple lists of User IDs to explicitly target or exclude from a gate.

Supported Operators: `Any of, none of`

Example usage: Add yourself (or a small group like your team) when you just start building a new feature. Or exclude your designer until it's ready for their eyes.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/user-id-condition-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=75f289b4fca06f71faf8941c35881f43" alt="User ID condition example" width="1006" height="319" data-path="images/conditions/user-id-condition-example.png" />
</Frame>

### Email

Usage: Target based on the email of the user

Supported Operators: `any of, none of, contains any of, contains none of`

Example: Show new feature to people in the Statsig company with an authenticated @statsig.com email address

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/email-condition-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=85049593ee8febf36228c98165bea84e" alt="Email condition example" width="993" height="258" data-path="images/conditions/email-condition-example.png" />
</Frame>

### Everyone

Usage: Percentage rollout on the remainder of users that reach this condition. Think of it as "everybody else" - there could be a dozen other rules/conditions above it, but for everyone else, what percentage do you want to pass?

Supported Operators: `None. Percentage based only.`

Example usage: 50/50 rollout to A/B test a new feature. Or 0% to hide the feature for all people not matching a set of rules. Or 100% to show the feature to the remaining users who did not meet a condition above.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/everyone-5050-condition-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=47dc725a62251ca7199616ce171e336b" alt="Everyone 50/50 condition example" width="996" height="244" data-path="images/conditions/everyone-5050-condition-example.png" />
</Frame>

### App Version

Usage: User's on a particular version of your app/website will pass. Particularly useful for mobile app development, where a feature may not be fully ready (or maybe be broken) in a particular app version.

Supported Operators: `>=, >, <, <=, any of, none of`

Example: Turn off a feature for all users on app versions 3.0.0 through 3.1.0 as it was broken.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/disable-broken-versions-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=66e2f73a50af019d1b92dcabd521c75e" alt="Disable broken versions example" width="989" height="370" data-path="images/conditions/disable-broken-versions-example.png" />
</Frame>

### Browser Version

Usage: A particular version of a browser, parsed from the user agent. Should likely be combined with the browser name condition.

Supported Operators: `>=, >, <, <=, any of, none of`

Example: Turn off a feature for old versions of chrome which don't support a certain API

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/browser-name-version-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=010236bf0e0ef0dc7d20f7e172c70564" alt="Browser Name and Version Example" width="988" height="369" data-path="images/conditions/browser-name-version-example.png" />
</Frame>

### Browser Name

Usage: A particular browser, parsed from the user agent:
('Chrome',
'Chrome Mobile',
'Edge',
'Edge Mobile',
'IE',
'IE Mobile',
'Opera',
'Opera Mobile',
'Firefox',
'Firefox Mobile',
'Mobile Safari',
'Safari').
Often combined with the Browser Version condition.

Supported Operators: `>=, >, <, <=, any of, none of`

Example: Turn off a feature for old versions of chrome which don't support a certain API

To test: The Browser Name is inferred from the `userAgent`, but if you need to set it explicitly, you can set `browserName` in the user object.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/browser-name-version-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=010236bf0e0ef0dc7d20f7e172c70564" alt="Browser Name and Version Example" width="988" height="369" data-path="images/conditions/browser-name-version-example.png" />
</Frame>

### OS Version

Usage: A particular os version the user is on, parsed from the user agent. Should likely be combined with the Operating System condition.

Supported Operators: `>=, >, <, <=, any of, none of`

Example: Turn off a feature for versions of macOS which don't support a certain API

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/os-name-version-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=22a416999a85c8273df4d128850fe7f5" alt="OS name and version example" width="991" height="487" data-path="images/conditions/os-name-version-example.png" />
</Frame>

### Operating System

Usage: A particular operating system, parsed from the user agent:
('Android', 'iOS', 'Linux', 'Mac OS X', 'Windows').
Often combined with the OS Version condition.

Supported Operators: `any of, none of`

Example: Turn off a feature for versions of macOS which don't support a certain API

To test: The OS is inferred from the `userAgent`, but if you need to set it explicitly, you can set `deviceOS` in the user object.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/os-name-version-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=22a416999a85c8273df4d128850fe7f5" alt="OS name and version example" width="991" height="487" data-path="images/conditions/os-name-version-example.png" />
</Frame>

### Device Model

Usage: The device model of the mobile device the user is on.

Supported Operators: `any of, none of, is null, is not null, contains any of, contains none of, regex`

Example: Turn off a feature for older device models that your app does not support.

To test: The Device Model is automatically inferred by the SDK, but if you need to set it explicitly, you can set `deviceModel` in the user object.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/device-model-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=277ebe50d36871745dde75b0cbedb97d" alt="Device Model Example" width="992" height="269" data-path="images/conditions/device-model-example.png" />
</Frame>

### Country

Usage: A 2 letter country code, either passed as the user's country or determined by the IP address.

Supported Operators: `any of, none of`

Example: Show a cookie consent banner for users accessing your service from the EU.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/country-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=e47088528e47cebe90d1e45ae35c9e38" alt="Country example" width="990" height="278" data-path="images/conditions/country-example.png" />
</Frame>

### IP address

Usage: An IP address string

Supported Operators: `any of, none of`

Example: Show a different about us page on [www.statsig.com](http://www.statsig.com) to people in a certain IP address range

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/matching-ip-addresses-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=b4fd79ec8fda17fd53ead9b2439b5fdf" alt="Matching IP Addresses example" width="987" height="257" data-path="images/conditions/matching-ip-addresses-example.png" />
</Frame>

### Passes Target gate

Usage: The condition passes if the referenced gate passes for the given user

Supported Operators: `gate_id`

Example: Only show feature X to people who also see feature Y: Only show a toggle to turn off ranking to people who also pass the new ranking algorithm gate.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/passes-target-gate.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=aeb3faccf3760755c64dbd31c0df4655" alt="Passes Target Gate" width="991" height="258" data-path="images/conditions/passes-target-gate.png" />
</Frame>

### Fails Target gate

Usage: Inverse of passes target gate: the condition passes if the referenced gate returns false for the given user

Supported Operators: `gate_id`

Example: Only show a new UI element to people who are not using the redesigned UI.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/fails-target-gate.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=ee259c5084839a890df447831147cbce" alt="Fails Target Gate" width="989" height="259" data-path="images/conditions/fails-target-gate.png" />
</Frame>

### User in Segment

Usage: The condition passes if the user passes the rules defining the referenced segment. See the [segments guide](/guides/using-environments) for more information on segments.

Supported Operators: `segment_id`

Example: Only show a new UI element to people who are not using the redesigned UI.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/in-segment.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=1cc9a500c1f0555c1f0af4d64785adfa" alt="In Segment" width="992" height="259" data-path="images/conditions/in-segment.png" />
</Frame>

### User not in Segment

Usage: The condition passes if the user fails the rules defining the referenced segment. See the [segments guide](/guides/using-environments) for more information on segments.

Supported Operators: `segment_id`

Example: Only show a feature to people who are not in the premium/paid tier.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/not-in-segment.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=ac058147a8dfce495b5c6aba81a59eb6" alt="Not In Segment" width="991" height="257" data-path="images/conditions/not-in-segment.png" />
</Frame>

### Environment Tier

Usage: The condition passes if the evaluation is happening in the given environment tier (development/staging/production). See the [environments guide](/guides/using-environments) for more information on environments.

Supported Operators: `development/staging/production/(other)`

Example: Only show a feature on development builds

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/development-environment-condition.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=93e7a6d8c5f1774ec6fd34e73331dfd2" alt="Development Environment Condition" width="993" height="259" data-path="images/conditions/development-environment-condition.png" />
</Frame>

### Custom Field

Usage: Specify the key in the custom object to fetch the value use on the left hand side of a comparison

Supported Operators:

* string: `any of, none of, contains any of, contains none of`
* number: `any of, none of, less than, greater than`
* version: `any of, none of, less than, greater than, less than or equal to, greater than or equal to`
* date: `before, after`

Example: Only show a feature to user's who have turned on dark mode, as marked by the custom object having "darkmode": true.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/custom-field.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=87ad0576cffc182709a260a154dbdea7" alt="Custom Field" width="1085" height="257" data-path="images/conditions/custom-field.png" />
</Frame>

### Unit ID

Usage: Select custom ids to explicitly target or exclude from a gate.

Supported Operators: `any of, none of, is null, is not null, contains any of, contains none of, regex`

Example: Add yourself (or a small group like your team) when you just start building a new feature.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/unit-id-example.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=5004e980f77520d5279a0a5459e021a0" alt="Unit ID example" width="1084" height="264" data-path="images/conditions/unit-id-example.png" />
</Frame>

### Time

Usage: Evaluate a gate relative to the current time

Supported Operators: `after time, before time`

Value: time (displayed and input on Console in your browser's local time, but converted to a unix timestamp for evaluation)

Example: Show the labor day sale banner on labor day

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/time-condition.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=2f53d6aed558b9d8f8532911675994a0" alt="Time condition" width="1085" height="372" data-path="images/conditions/time-condition.png" />
</Frame>

### Private Attributes

Usage: Any user field conditions, or custom field conditions, can be used via a private attribute. If you are targeting an email, but don't want it to be logged,
create an email condition, but put "email": "[xyz@email.com](mailto:xyz@email.com)" in the privateAttributes dictionary. For custom fields, create a custom field condition, but put the key/value pair in privateAttributes instead.
Remember that privateAttributes are used for evaluation only, and are not stored or kept on logEvents.

Supported Operators: dependent on the condition

Example: Only show a feature to 20 somethings, as marked by the privateAttributes object having "age": "20-29".

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/conditions/private-attributes.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=5260d73ff39a3c96df4a5a68d91c20a1" alt="Private attributes" width="1133" height="1005" data-path="images/conditions/private-attributes.png" />
</Frame>

## FAQs

<AccordionGroup>
  <Accordion title="Could users switch between control (fail) and test (pass) groups?">
    Once a user is exposed, they will be included in the analysis going forward. They saw the new feature and were affected. If the feature gate rules are modified or the user's attributes change in a way that the user no longer qualifies, they will stop receiving the new feature. However, they will continue to be counted for analysis. Once you roll out the feature, all users will see the new feature; alternatively, if you turn off the feature gate, all users will see the control (feature disabled). In either case (roll out or turn off), Statsig performs no further analysis.
  </Accordion>

  <Accordion title="How do overrides work? Are users included in overrides also included in the analysis?">
    When you add user IDs in the **Pass** or **Fail** lists of your feature gate, these users will see the appropriate treatment but will not be included in the analysis.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).