# Source: https://docs.avaamo.com/user-guide/ref/best-practices-parallel-development.md

# Agent Parallel development - Best practices

The following document highlights the best practice when multiple developers are engaged to develop a single agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Favaamo%2F-LyirFYEGdoosuWyNEij%2F-LyiuPinsHeJV11w6RlI%2F0.png?generation=1579187547543561\&alt=media)

Avaamo suggests the approach of each developer having their copy of the agent when they have to develop and collaborate on a single agent. See [Copy agent](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/make-a-copy), for more information.

The following lists recommended steps for agent parallel development:

1. Each developer pushes their skills (including the entities and javascript) into the store. See [Publish skills](https://docs.avaamo.com/user-guide/how-to/build-skills/manage-skill/publish-skill-to-skills-store), for more information.
2. A master copy of the agent can be composed of the skill store skills. See [Manage skill store](https://docs.avaamo.com/user-guide/how-to/manage-skills-store), for more information.
3. Integrated testing happens on the master copy. See [Test agents](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents), for more information.
4. The master copy of the agent is pushed to **Testing**. The testing agent gets pushed into Staging and the Staging agent gets pushed into the production. See [Agent life cycle](https://docs.avaamo.com/user-guide/how-to/plan-your-development-process-agent-life-cycle) and [Promote agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/promote-and-pull-updates), for more information.

## Merging Changes

This section lists steps that can be used to merge local changes to working copy in the agent in the following cases:

* [Merging changes in the shared entities](#merging-changes-in-the-shared-entities)
* [Merging changes in the shared Javascript](#merging-changes-in-the-shared-javascript)

### Merging changes in the shared entities

If two or more skills refer to the same entity and there are local changes to that entity in a working copy of the agent, then you must merge local changes to working copy in the agent manually.

It is recommended to:

* Use the entity export functionality to export entity values from the master copy and the working copy to do a diff. See [Export entity values](https://docs.avaamo.com/user-guide/how-to/build-agents/add-entity-types-to-agent/manage-entity-types#export), for more information.
* You can then do a **diff** and **merge** the changes.

{% tabs %}
{% tab title="On Mac" %}
`$diff file1.csv file2.csv`

The following lists a few recommended tools to use:

* FileMerge: This is a built-in tool that is installed as part of the Apple Developer tools.
* Visual Studio Code
  {% endtab %}

{% tab title="Windows" %}
The following lists a few recommended tools to use:

* Meld: You can use a visual diff tool such as Meld - <http://meldmerge.org/>
* Visual Studio Code
  {% endtab %}
  {% endtabs %}

### Merging changes in the shared JavaScript

If two or more skills refer to the same JS and there are local changes to that JS in a working copy of the agent, then you must merge local changes to a working copy in the agent manually.

It is recommended to:

* Save the content of the JavaScript into a local file from the master copy and the working copy.
* You can then do a **diff** and **merge** the changes.
