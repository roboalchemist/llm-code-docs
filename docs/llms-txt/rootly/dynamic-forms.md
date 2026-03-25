# Source: https://docs.rootly.com/configuration/dynamic-forms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic Forms

> Configure form variations that adapt based on incident properties like type, team, or severity to collect contextually relevant information.

Rootly's dynamic forms allow for more granularity based on different incident types, different teams, or different severities that require different versions of the same forms. You can access the dynamic forms by navigating to **Configuration >** [**Forms**](https://rootly.com/account/forms).

The Dynamic Forms feature is not enabled out-of-box, but if you’d like to try it out, reach out to your Rootly point of contact or support team. [Video Example of Use Case](https://www.loom.com/share/11b9503c6bd94043bfafc6cdd5166021?sid=35cd9955-d742-45f3-b99f-b2840b3e0a74)﻿

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/1.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=3d0bb8682de982812dde4dddcceed570" alt="Document image" width="899" height="437" data-path="images/dynamic-forms/1.webp" />
</Frame>

## Incident Property Field

The incident property is what is used to **base** the dynamic forms from. The options include Incident Type, Team, or Severity.

> This field is important as it drives the property in which you build your dynamic forms from

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/2.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=4441dab579af8dc7a89cd192a55f937c" alt="Document image" width="917" height="1560" data-path="images/dynamic-forms/2.webp" />
</Frame>

Once an incident property is selected, click `+ New Form Set` to create a dynamic form.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/3.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=a92ee5e0fd935528b851c1d0301e2c02" alt="Document image" width="905" height="696" data-path="images/dynamic-forms/3.webp" />
</Frame>

## **Creating Form Set**

* Name: Choose a unique name
* Use this form when \[incident type / team / severity]
* Then choose which default forms you would like to customize.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/4.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=81c1ad1f9e99cb48f341eed33256817e" alt="Document image" width="908" height="660" data-path="images/dynamic-forms/4.webp" />
</Frame>

### Example Use Case

One of the main use cases for this is when you want to give more granularity on different teams, incident types, or severities, but you want them to have different versions of the same form. For example, when the information I want to collect for the `security teams` incidents is different than the information I want to collect for the `infrastructure teams` incidents. But within that, within the `security teams` forms, I actually want certain fields different based on if it’s a SEV0 incident.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/5.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=055f58c89c87cbbfb4c8f9682563d64c" alt="Document image" width="904" height="610" data-path="images/dynamic-forms/5.webp" />
</Frame>

Click 'Create Form Set'

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/6.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=1755e3626a353c9c96cb01f028a0f728" alt="Document image" width="905" height="378" data-path="images/dynamic-forms/6.webp" />
</Frame>

Once created, you'll see the newly built 'Security Team Forms' on the left and the form types you wish to customize.

These new forms will only show when `Team` is `Security`

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/dynamic-forms/7.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=400a419649c0a6c068494e395eb1868d" alt="Document image" width="899" height="502" data-path="images/dynamic-forms/7.webp" />
</Frame>

Next, we need to get more granular and only show these forms when the `Team` is `Security` **AND** the `Severity` is a `SEV0`. To do this, click 'Configure' on the form type you would like to edit.

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/dynamic-forms/8.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=f40ec3901204dd45edf5045e5854619d" alt="Document image" width="897" height="428" data-path="images/dynamic-forms/8.webp" />
</Frame>

The form will start empty, minus your incident property field, which in this case is `Teams`.

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/dynamic-forms/9.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=95df90def86ca3bd18c8db72323edd25" alt="Document image" width="897" height="428" data-path="images/dynamic-forms/9.webp" />
</Frame>

Add any custom or built-in fields by clicking 'Add Fields'

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/10.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=20561ec89aec518c6b17b02143b7103e" alt="Document image" width="904" height="896" data-path="images/dynamic-forms/10.webp" />
</Frame>

When the required fields are selected, click 'Add Fields'.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/11.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=7e5250be0b06ffe5d610e92a977b6796" alt="Document image" width="912" height="1430" data-path="images/dynamic-forms/11.webp" />
</Frame>

Edit each field and choose when to display and/or require this field, at this stage you can add conditions.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/12.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=a9db12915d73fcd138c3d26d2532bbb3" alt="Document image" width="897" height="522" data-path="images/dynamic-forms/12.webp" />
</Frame>

Set the field to only display when the incident is a `SEV0` , and **REQUIRE** the field. Click Save once the conditions are defined.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/13.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=e8b7ff2f06c4d6dce726026cc5677422" alt="Document image" width="902" height="795" data-path="images/dynamic-forms/13.webp" />
</Frame>

### To Test

Create a new incident and set the team to `Security`

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/14.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=1870b74edac02232b6a14ee46f2f04e5" alt="Document image" width="904" height="429" data-path="images/dynamic-forms/14.webp" />
</Frame>

Once `<Security team>` is selected, the form will auto-refresh with the dynamic 'Security Team Form'

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/15.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=5c48ee9e2be336d957aa546105a1477c" alt="Document image" width="902" height="864" data-path="images/dynamic-forms/15.webp" />
</Frame>

### Removing An Existing Dynamic Form

Editing and deleting can be done by clicking on the ellipsis.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/16.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=8b96b99daa7724790030dee0999c1bb3" alt="Document image" width="912" height="512" data-path="images/dynamic-forms/16.webp" />
</Frame>

Only one property can be selected at a time. Removing the existing incident property selection will delete all existing dynamic forms. You will be prompted with a warning message prior.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/dynamic-forms/17.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=eeb86be0cad2647fc650db11d80340cd" alt="Document image" width="902" height="510" data-path="images/dynamic-forms/17.webp" />
</Frame>

### Want to use dynamic forms?

Yay! We can't wait! Please reach out to your Rootly point of contact or support team to request access.


Built with [Mintlify](https://mintlify.com).