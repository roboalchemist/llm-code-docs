# Source: https://directus.io/docs/raw/tutorials/workflows/build-content-approval-workflows-with-custom-permissions.md

# Build Content Approval Workflows with Custom Permissions

> Learn how to configure roles and permissions for complex automations.

CRUDS permissions define what a role can and can't do to all items in a collection. Custom access permissions take
things a step further and let you define what a role can and can't do to each item in a collection, *based on its
field values*.

Workflows are when you use these permissions techniques to create structured stages to content or data creation. In
simplest terms, it is when you have two or more roles, and you give them different permissions at each stage in the
content creation process. This is common when using Directus as a
[Headless CMS](https://directus.io/solutions/headless-cms).

There are an infinite number of possible workflows you could configure. But for this recipe, we will configure a simple
workflow where `writers` and `editors` work together to create, co-edit and publish `articles`.

![A Workflow](/img/3ff1a63e-b54d-49b6-9088-3cc6d4d0d676.webp)

For this recipe, our workflow will have three stages, `draft`, `under review`, and `published`, which will be defined in
a `status` field.

<table>
<thead>
  <tr>
    <th>
      <code>
        status
      </code>
    </th>
    
    <th>
      <code>
        Author
      </code>
    </th>
    
    <th>
      <code>
        Editor
      </code>
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <em>
        Article is not yet created
      </em>
    </td>
    
    <td>
      Author can create new items in <code>
        articles
      </code>
      
      , but only with a status of <code>
        draft
      </code>
      
      .
    </td>
    
    <td>
      Editor cannot create new items in <code>
        articles
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        Draft
      </code>
    </td>
    
    <td>
      Author creates and edits the article. Then can set status to <code>
        under review
      </code>
      
       when ready.
    </td>
    
    <td>
      Editor has either read-only, or no permissions at all.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        Under Review
      </code>
    </td>
    
    <td>
      Author can edit the article's content, but not the <code>
        status
      </code>
      
       field.
    </td>
    
    <td>
      Editor can edit the article, as well as set status to <code>
        Draft
      </code>
      
       or <code>
        Published
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        Published
      </code>
    </td>
    
    <td>
      Author is no longer responsible for article, and has read-only permissions.
    </td>
    
    <td>
      Editor has permissions to update or delete the article.
    </td>
  </tr>
</tbody>
</table>

This whole workflow is created with permissions. All we need to do to create these stages is change the `author` and
`editor` permissions for each item in `articles` conditionally, based on the value of `status`.

![A Workflow](/img/0969ef65-6378-408a-a387-327c968e475e.webp)

## How-To Guide

<callout icon="material-symbols:info-outline">

To implement a workflow, you'll need:

- An understanding of [permissions](/guides/auth/access-control) and
filters in Directus.
- A collection with some kind of content. In this recipe, we'll use a collection called `articles`.
- A field on that collection to validate conditionally. We'll use a `status` field.
- Two *(or more)* roles that will work to author content. We'll use `writer` and `editor` roles.

</callout>

To create a structured workflow for `articles`, follow these steps.

1. First, [create a field](/guides/data-model/fields) to track the article status. We'll call this
field `status`, but it could be named anything.
2. [Create a field](/guides/data-model/fields) with a Dropdown Interface. Name it `status` and add
the stages *(draft, under review and published)* needed for your content creation process.
3. Next, create two roles: `author` and `editor`.
4. Finally, configure custom access permissions for each role based on the value of the `status` field.

  - For the `author` role:
  
    - Set a filter under **Create > Use Custom > Field Validation** to ensure the author can only create articles with
    a `draft` status.
    - Enable all read permissions.
    - Set a filter under **Update > Use Custom > Item Permissions** to ensure the user can update articles with a
    `draft` or `under review` status.
    - Set a filter under **Update > Use Custom > Field Validation** to ensure the user can only update article status
    to `under review`.
    - Keep delete permissions restricted.
    - Keep shares permissions restricted.
  - For the `editor` role:
  
    - Keep create permissions restricted.
    - Enable all read permissions.
    - Set a filter under **Update > Use Custom > Item Permissions** to ensure the user can only update articles with an
    `under review` status.
    - Set a filter under **Update > Use Custom > Field Validation** to ensure the user can only update status to
    `published`.
    - Keep delete permissions restricted.
    - Keep shares permissions restricted.

## Final Tips

This recipe covers one simple example of a workflow. As you move forward and created your own custom-tailored workflows,
just remember:

- You could use any number of roles.
- You could use any collection or relationally linked collections.
- You can add more stages in your workflow by adding more values to your `status` field.

Be sure to pay close attention to how you configure custom access permissions for workflows. Unintentional
misconfigurations can have side-effects.

In our simple `articles` workflow above, a minor misconfiguration in a co-editing workflow between two team members
*might* not be a big problem. But in other cases it can have big consequences. For example, let's imagine for a second
that:

- The `writer` and `editor` roles were `teacher` and `student` roles.
- The `articles` collection was instead a `tests` collection.
- The `status` field defined if the test was `not started`, `in progress`, or `submitted`.

A minor misconfiguration here could ruin academic integrity. Here's a few potential issues:

- students retake/re-edit their own submitted test.
- students take/edit/delete tests of other students.
- teachers modify the results of students that they like or don't like.
- *and beyond!*

When creating your own workflow, its a good idea to define each role involved, each stage in the workflow, and the
explicit set of permissions each role has at each stage.

<callout icon="material-symbols:info-outline">

Workflows can be further enhanced with custom [Interfaces](/guides/extensions/app-extensions/interfaces) as well as [flows](/guides/automate/flows).

</callout>
