# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/create-pentaho-dashboard-designer-templates.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/create-pentaho-dashboard-designer-templates.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/create-pentaho-dashboard-designer-templates.md

# Create Pentaho Dashboard Designer templates

Follow the directions below to create a new Pentaho Dashboard Designer template.

**Note:** You will have to migrate this template by hand if/when you upgrade Dashboard Designer because the template files will be stored in the Dashboard Designer plugin directory. The upgrade procedure that Pentaho provides does not typically cover customizations like this one, except to mention that they must be migrated by hand.

1. Stop the Pentaho Server.
2. Navigate to the `/pentaho/server/pentaho-server/pentaho-solutions/system/dashboards/templates/xul/` directory.
3. If you want to remove all templates that you know will never be used:
   1. You can safely delete their corresponding XUL files now.
   2. When you are done, also remove the corresponding files from the HTML sibling directory.
4. Copy the existing XUL file that most closely resembles the template layout you want to create, giving the new XUL file a name that starts with a two-digit number that represents the template's order in the hierarchy, followed by a short description of its dimensions.

   All Dashboard Designer templates follow this naming convention.
5. Create a `.properties` file that corresponds to the one you just copied in the previous step, and put one item in it: `<name=><Description here>`, where *Description here* represents the display name of this template.
6. Create a thumbnail graphic that fits the same dimensions as the other PNG thumbnails in this directory, and give it the same name as the previous two files, with a PNG extension.

   You should now have three new files, all with the same name, with three different extensions: `.xul`, `.properties`, and `.png`.
7. Edit the new `.xul` file and change the **box** attributes to match your template specifications:

   * A vbox node creates a column.
   * An hbox node creates a row.
   * A box element defines an individual panel in each row.
   * Both height and width define static widths in pixels.
   * The flex size attribute defines a percentage of the total width of the dashboard.**Note:** Ensure that each **box**, **vbox**, and **hbox** node has its own unique *id*.

   If you would like more extensive definitions of XUL elements, refer to the official XUL documentation: <http://developer.mozilla.org/en/XUL_Reference>.
8. Save and close all open files, then start the Pentaho Server.
9. Test your new template and adjust its configuration accordingly.

You now have a custom Dashboard Designer template deployed to your Pentaho Server. You must copy the template files by hand if you upgrade the Pentaho Server or Dashboard Designer in the future. You may want to back up your custom templates to a safe location right now just in case you forget to copy them over during a future upgrade.
