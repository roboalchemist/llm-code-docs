# Content-type Builder

From the 
  
</IdentityCard>

## Overview

  </Tabs>
3. Click the **Finish** button in the dialog.
4. Click the **Save** button in the Content-Type Builder navigation.

#### Fields

From the table that lists the fields of your content-type, you can:
- Click on the 

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_richtextblocks.svg" /> Rich Text (Blocks) {#rich-text-blocks}

The Rich Text (Blocks) field displays an editor with live rendering and various options to manage rich text. This field can be used for long written content, even including images and code.

</Tabs>

:::strapi React renderer
If using the Blocks editor, we recommend that you also use the 

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_date.svg" /> Date {#date}

The Date field can display a date (year, month, day), time (hour, minute, second) or datetime (year, month, day, hour, minute, and second) picker.

</Tabs>
 
#### <img width="28" src="/img/assets/icons/v5/ctb_password.svg" /> Password

The Password field displays a password field that is encrypted.

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_media.svg" /> Media {#media}

The Media field allows to choose one or more media files (e.g. image, video) from those uploaded in the Media Library of the application.

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_relation.svg" /> Relation {#relation}

The Relation field allows to establish a relation with another content-type, that must be a collection type.

There are 6 different types of relations:

- <img width="25" src="/img/assets/icons/v5/ctb_relation_oneway.svg" /> One way: Content-type A *has one* Content-type B
- <img width="25" src="/img/assets/icons/v5/ctb_relation_1to1.svg" /> One-to-one: Content-type A *has and belong to one* Content-type B
- <img width="25" src="/img/assets/icons/v5/ctb_relation_1tomany.svg" /> One-to-many: Content-type A *belongs to many* Content-type B
- <img width="25" src="/img/assets/icons/v5/ctb_relation_manyto1.svg" /> Many-to-one: Content-type B *has many* Content-type A
- <img width="25" src="/img/assets/icons/v5/ctb_relation_manytomany.svg" /> Many-to-many: Content-type A *has and belongs to many* Content-type B
- <img width="25" src="/img/assets/icons/v5/ctb_relation_manyway.svg" /> Many way: Content-type A *has many* Content-type B

:::info Multi relations and single relations
Relations where at least one side can reference several entries are called multi relations. In the Content-type Builder, this includes one-to-many, many-to-one, many-to-many, and many-way relations. These relations appear as multi-select fields in the Content Manager and return arrays from the REST, GraphQL, and Document Service APIs; while single relations (one-way and one-to-one relations) return a single linked entry (see [Managing relations with API requests](/cms/api/rest/relations) for more information).
:::

</Tabs>

:::tip Modeling nested page hierarchies
To model a navigable tree of pages:
1. Add a `Page` collection type with a "Slug" (UID) and (optionally) an "Order" (Integer) field to control sibling ordering.
2. Create a Relation field from `Page` to `Page` and choose *Many-to-one* so each page can set its "Parent page". Strapi automatically provides the inverse "Children pages" relation.
3. When reading data, populate `children` recursively to load the tree. Keep the recursion depth small to avoid large responses.

<details>
<summary>Example</summary>
```json title="Populate nested children for a page tree"
{
  populate: {
    children: {
      fields: ['title', 'slug'],
      populate: {
        children: {
          fields: ['title', 'slug'],
        },
      },
    },
  },
}
```
</details>

The same populate pattern works with GraphQL or the Document Service API (see [Understanding populate guide](/cms/api/rest/guides/understanding-populate#populate-several-levels-deep-for-specific-relations)).
:::

#### <img width="28" src="/img/assets/icons/v5/ctb_boolean.svg" /> Boolean {#boolean}

The Boolean field displays a toggle button to manage boolean values (e.g. Yes or No, 1 or 0, True or False).

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_json.svg" /> JSON {#json}

The JSON field allows to configure data in a JSON format, to store JSON objects or arrays.

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_email.svg" /> Email {#email}

The Email field displays an email address field with format validation to ensure the email address is valid.

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_password.svg" /> Password {#password}

The Password field displays a password field that is encrypted.

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_enum.svg" /> Enumeration {#enum}

The Enumeration field allows to configure a list of values displayed in a drop-down list.

</Tabs>

:::caution
Enumeration values should always have an alphabetical character preceding any number as it could otherwise cause the server to crash without notice when the GraphQL plugin is installed.
:::

#### <img width="28" src="/img/assets/icons/v5/ctb_uid.svg" /> UID {#uid}

The UID field displays a field that sets a unique identifier, optionally based on an existing other field from the same content-type.

</Tabs>

:::tip
The UID field can be used to create a slug based on the Attached field.
:::

#### <img width="28" src="/img/assets/icons/v5/ctb_richtext.svg" /> Rich Text (Markdown) {#rich-text-markdown}

The Rich Text (Markdown) field displays an editor with basic formatting options to manage rich text written in Markdown. This field can be used for long written content.

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_component.svg" /> Components {#components}

Components are a combination of several fields. Components allow to create reusable sets of fields, that can be quickly added to content-types, dynamic zones but also nested into other components.

When configuring a component through the Content-type Builder, it is possible to either:

- create a new component by clicking on *Create a new component* (see [Creating a new component](#new-component)),
- or use an existing one by clicking on *Use an existing component*.

</Tabs>

#### <img width="28" src="/img/assets/icons/v5/ctb_dz.svg" /> Dynamic zones {#dynamiczones}

Dynamic zones are a combination of components that can be added to content-types. They allow a flexible content structure as once in the Content Manager, administrators have the choice of composing and rearranging the components of the dynamic zone how they want.

</Tabs>

After configuring the settings of the dynamic zone, its components must be configured as well. It is possible to either choose an existing component or create a new one.

:::caution
When using dynamic zones, different components cannot have the same field name with different types (or with enumeration fields, different values).
:::

#### Custom fields

[Custom fields](/cms/features/custom-fields) are a way to extend Strapi’s capabilities by adding new types of fields to content-types or components. Once installed (see [Marketplace](/cms/plugins/installing-plugins-via-marketplace) documentation), custom fields are listed in the _Custom_ tab when selecting a field for a content-type.

Each custom field type can have basic and advanced settings. The  lists available custom fields, and hosts dedicated documentation for each custom field, including specific settings.

### Deleting content-types

Content types and components can be deleted through the Content-type Builder. Deleting a content-type automatically deletes all entries from the Content Manager that were based on that content-type. The same goes for the deletion of a component, which is automatically deleted from every content-type or entry where it was used.

1. In the  Content-type Builder sub navigation, click on the name of the content-type or component to delete.
2. In the edition interface of the chosen content-type or component, click on the  **Edit** button on the right side of the content-type's or component's name.
3. In the edition window, click on the **Delete** button.
4. In the confirmation window, confirm the deletion.
5. Click on the **Save** button in the Content-type Builder sub navigation.

:::caution
Deleting a content-type only deletes what was created and available from the Content-type Builder, and by extent from the admin panel of your Strapi application. All the data that was created based on that content-type is however kept in the database. For more information, please refer to the related .
:::