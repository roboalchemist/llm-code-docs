# Source: https://docs.pentaho.com/pba-metadata-editor/apply-metadata-properties-and-concepts-in-pentaho-metadata-editor-cp/apply-properties.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/apply-metadata-properties-and-concepts-in-pentaho-metadata-editor-cp/apply-properties.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/apply-metadata-properties-and-concepts-in-pentaho-metadata-editor-cp/apply-properties.md

# Apply properties

All physical and some business objects in the metadata model have a set of required properties. These properties are set automatically on creation of the object, and are not removable (although you can change their value). The purpose for required properties is to disallow users from getting into a predicament where they have removed a property that is integral to the SQL generation process. For example, if a physical table did not have a Target Table property set, the SQL generator will cause errors, because it cannot access the correct physical table to query.

If you set a parent concept on the physical table, and the parent concept and the physical table both have the same property, the physical table does not recognize the parent concept's value for that property. This is because the physical table already has the property as part of its self concept, and the self concept always overrides the parent concept. Since you cannot remove a required property, the parent concept's property will never be recognized at the physical level.

To override a physical object's required property, set a parent concept at the business model or business view level. Since you can override the inherited properties, the parent concept at the business level takes priority.

All physical metadata objects, the business categories and the business model have required properties. You can see what's required for each by referring to [Required properties per business object](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/metadata-properties-reference#required-properties-per-business-object).

**Note:** There are two sets of properties that change how the typical inheritance is accomplished: required properties and the default concept.

## Use the properties editor

The Business Table Properties dialog box for every business object has two additional lists to the right of the **Subject** list. These lists are related to concept editing. The two additional lists are the **Properties** list, and **Settings**, and they operate in the same way regardless of the object to which you are applying metadata.

![Business Table Properties dialog box](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-3552ed7c23302eb9d594431161bdf959b704d698%2F39_properties.png?alt=media)

### Properties list

The middle panel in the Properties dialog box is the **Properties** list. This is the list of currently applied metadata properties for the object that is selected in the **Subject** list. The properties are sorted into their appropriate categories for organization. At the top of the **Properties** list, there are two icons. The Plus Sign is for adding new metadata properties to this business table's self concept. The X icon is for removing properties from the self concept. Note that the remove button is disabled until a property is selected in the **Properties** list.

There are four ways a property can show up in the **Properties** list:

1. The property is a default property for the associated business object, and thus cannot be removed.
2. The property was inherited from the business object's physical ancestor.
3. The property has been set as part of the self concept.
4. The property has been set as part of the object's parent concept.

The following color codes alert you to what concept level is in use:

* Yellow icon: This property is inherited from the object's physical ancestor.
* Blue icon: Pentaho sets the property on the object's own concept. This could be overriding an inherited property.
* Orange icon: This property is set as a result of the parent concept applied to the object.
* Purple icon: This is a special icon reserved for security properties.

### Property settings

**Settings** shows the property name and the associated value for that property in a scrolling list. The properties are displayed in the properties editor in the same order as they appear in the **Properties** list. If you click on a property in the **Properties** list, the properties editor scrolls to locate the property in the editor. In the properties editor, you can set or modify the values of the properties applied to the business object.

There are icons in the upper right corner next to any property whose value can be overridden. If you want to modify a property by overriding its inherited value, you must first click the Override icon. To cancel an override, click the Override icon again.

## Add a property

Before you add a new property to a business object, make sure that the object you want to apply the new property to is selected in the **Subject** list.

Perform the following steps to add a property:

1. In the Properties dialog box, click **Add** next to **Available**.

   The Add New Property dialog box appears. You are prompted with a list of [property choices](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/metadata-properties-reference) to apply.
2. Select a property.
3. Click **OK**.

The property is now available for you to modify in the property editor.

## Remove a property

Perform the following steps to remove a property:

**Note:** If you want to remove inherited or parent concept properties, you must edit the inherited business object or the parent concept.

1. In the **Properties** list, select the property you want to remove.
2. Click the X icon to remove the property.

<br>
