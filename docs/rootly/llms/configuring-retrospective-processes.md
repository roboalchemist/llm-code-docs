# Source: https://docs.rootly.com/retrospectives/configuring-retrospective-processes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Retrospective Processes

> Retrospectives have configurable, customizable processes, made up of steps, to allow a right-sized retrospective based on severity, type, or teams involved in an incident.

# Process Defaults

A retrospective process is a series of steps that will be applied to an incident and guide responders through a retrospective. Rootly provides a default retrospective process with generalized steps that will work for many use cases. No configuration is required, the [default steps](/retrospectives/configuring-process-steps) will be applied to all incidents.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/configuring-retrospectives/1.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=414828750df3e034abcfd082fdfa2b74" alt="Document image" width="902" height="235" data-path="images/configuring-retrospectives/1.webp" />
</Frame>

# Customized Process

For more opinionated incident practices, retrospective processes can be created, customized, and applied to incidents meeting specific requirements. The ability to scale retrospective processes based on the severity, team, or type of incident allows programs to right-size their retrospective process and support responders regardless of what kind of incident occurs.

The following incident attributes can be used to apply custom processes:

* Severity
* Type
* Team

Processes can also be configured to be required or auto skipped based upon the same incident attributes.

* Required retrospective processes are not able to be skipped by responders.
* Auto-skipped processes are skipped by default, but have the option to be reinstated at responder discretion.

<Frame>
    <img src="https://mintcdn.com/rootly/OVd58onR8faXRZwf/images/configuring-retrospectives/2.webp?fit=max&auto=format&n=OVd58onR8faXRZwf&q=85&s=3b2f6da07ddb694e9c6a1dec5b9a5100" alt="Document image" width="905" height="1315" data-path="images/configuring-retrospectives/2.webp" />
</Frame>

<Note>
  Note: by default, retrospective processes have the option to be skipped on a per-incident basis by responders via the button at the bottom of the retrospective tab.
</Note>

Examples:

**SEV1 incident example**

Apply a more rigorous process that requires the following steps:

* Gather information
* Hold retrospective meeting
* Peer review of generated document
* Publish retrospective document

Each of these steps have automatically: assigned step owners based upon incident role, relative due dates and owner reminders.

**SEV3 incident example**

Apply a flexible, light weight process with the following optional, skippable steps:

* information gathering
* self facilitated team retrospective meeting


Built with [Mintlify](https://mintlify.com).