# Source: https://docs.base44.com/documentation/using-your-workspaces/adding-workspace-skills.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing workspace skills

> Create and manage AI skills that guide how the AI chat builds apps in your workspace.

Skills are saved instruction sets that shape how the AI chat builds your apps. They activate when needed so the AI can follow your rules and best practices automatically across your workspace.

Workspace skills apply to every app in the workspace for anyone who can work in that workspace. This helps you keep design patterns, copy rules, and data practices consistent, no matter which app you are building.

<Frame caption="Adding skills to your workspace">
    <img src="https://mintcdn.com/base44/iHCf9ociy48e4sKc/images/skills.png?fit=max&auto=format&n=iHCf9ociy48e4sKc&q=85&s=93733be9af2309710eb6c23191fade99" alt="Adding skills to your workspace" width="3186" height="910" data-path="images/skills.png" />
</Frame>

You can use skills to give the AI specialized abilities for different kinds of work, such as:

* **Design skill:** Help the AI think like a designer by applying layout logic, spacing rules, hierarchy, and component best practices as it builds your UI.
* **Copy skill:** Help the AI focus on clear headlines, product descriptions, landing pages, and in-app text that match your tone and goals.
* **Data skill:** Help the AI behave like an analyst, interpret metrics, spot patterns, and reason about decisions using your structured data.

The AI chat decides when to use a skill based on what you type and the skill’s description and instructions. The AI can invoke relevant skills automatically, but it usually works best if you mention the skill or its purpose directly in your prompt, such as “Apply our accessibility skill to this flow” or “Use our brand-guidelines skill for this page.”

<Warning>
  You need a Builder plan or higher to add skills to your workspace.
</Warning>

***

## Adding a workspace skill

You can create skills from scratch or start from built-in presets.

<Note>
  Each workspace can have up to 100 skills. If you reach this limit, you must delete an existing skill before adding a new one.
</Note>

<Frame caption="Adding a skill to your workspace">
    <img src="https://mintcdn.com/base44/qVVHT2-sFHbNjxme/images/addskill-2.png?fit=max&auto=format&n=qVVHT2-sFHbNjxme&q=85&s=22a06afab24d3047f6fd01ee4b12ccfc" alt="Adding a skill to your workspace" width="3186" height="910" data-path="images/addskill-2.png" />
</Frame>

**To add a workspace skill:**

1. Click your profile icon at the top-right of Base44.
2. Click **Settings**.
3. Under **Workspace**, click **Skills**.
4. Click **Add skill**.
5. In the **Add skill or start from scratch** window, choose how you want to start:
   * **Start from scratch:** Create a completely custom skill.
   * **Preset skill:** Under **Presets**, click **Add** on a template.
6. In the **Skill name** field, enter a short, recognizable name, such as `brand-guidelines` or `checkout-copy-style`.
7. In the **Description** field, describe when the AI should use this skill. For example, explain which pages or tasks it applies to, or which team or brand it belongs to.
8. In the **Instructions** field, add the step-by-step rules the AI should follow when the skill activates. Treat this like training a new team member, with clear headings, examples, and priorities.
9. (Optional) Click **Refine & review** to have the AI refine and adjust the skill description and instructions while keeping your intent.
10. In the **Review your skill** window, compare the refined version with your original text:
    * Click **Back to original** if you prefer your original version.
    * Click **Save skill** to save the refined version, or **Cancel** to close the review window without saving changes.
11. Click **Add skill** to add the skill to your workspace.

***

## Turning a workspace skill on or off

You can temporarily disable a skill without deleting it. When a skill is off, the AI ignores its rules during conversations.

**To turn a workspace skill on or off:**

1. Click your profile icon at the top-right of Base44.
2. Click **Settings**.
3. Under **Workspace**, click **Skills**.
4. Click the toggle on the relevant skill to enable or disable that skill.

***

## Editing or deleting a workspace skill

Update a skill when your guidelines change, or delete it if you no longer need it.

<Frame caption="Editing a skill in a workspace">
    <img src="https://mintcdn.com/base44/0rhIc2EaMZdkowWe/images/editskill.png?fit=max&auto=format&n=0rhIc2EaMZdkowWe&q=85&s=a25362456cafc6195d749ff20c7b21f0" alt="Editing a skill in a workspace" width="3162" height="864" data-path="images/editskill.png" />
</Frame>

**To edit or delete a workspace skill:**

1. Click your profile icon at the top-right of Base44.
2. Click **Settings**.
3. Under **Workspace**, click **Skills**.
4. Next to the relevant skill, click the **More actions** icon.
5. Choose what you want to do:
   * **Edit Skill:** Open the skill editor to make changes. You can update the **Skill name**, **Description**, or **Instructions**, and optionally click **Refine & review** again to have the AI improve your updates before you save.
   * **Delete Skill:** Remove the skill from your workspace.

***

## FAQs

Click a question below to learn more about workspace skills.

<AccordionGroup>
  <Accordion title="When does the AI use a workspace skill?">
    The AI decides whether to use a skill based on your prompt and the skill’s description and instructions. It can invoke relevant skills automatically when they match what you are trying to do.

    For best results, mention the skill or its purpose directly in your prompt, such as “Apply our accessibility skill to this form.”
  </Accordion>

  <Accordion title="Do workspace skills apply to all apps in my workspace?">
    Yes. Workspace skills are available to the AI chat in every app in that workspace for anyone who can work in that workspace.
  </Accordion>

  <Accordion title="How do workspace skills relate to MCP connections?">
    Workspace skills define shared rules and best practices for how the AI builds apps in a specific workspace.

    MCP connections are configured once per account and let the AI chat use external tools and live data across all the apps and workspaces your account can access.

    [Learn how to add MCP connections.](/documentation/account-and-billing/setting-up-a-custom-mcp)
  </Accordion>

  <Accordion title="What happens if I delete a workspace skill?">
    When you delete a skill, the AI chat no longer uses its rules in any app in that workspace. You need to recreate the skill if you want to restore those guidelines in the future.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).