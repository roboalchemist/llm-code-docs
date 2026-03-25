# Source: https://docs.pentaho.com/pba-ctools/activate-cde.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/activate-cde.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/activate-cde.md

# Activate CDE

In Pentaho Enterprise Edition 5.4 and higher, CTools is installed for you. Follow the steps below to activate your Community Dashboard Editor (CDE) plugin.

**Note:** For Pentaho Community Edition 5.4 and higher, no activation is required.

To activate the CDE plugin, you will need to change the configuration of several XML files in the Pentaho solutions folder as described below. Verify that you have the appropriate permissions to read, write, and execute commands in the specified directories in the instructions.

These instructions should be executed after the Pentaho Server has been stopped.

## Modify the plugin and settings XML files

1. Log on to the machine on which you will host the Pentaho Server.
2. Locate the `pentaho-solutions/system/pentaho-cdf-dd` and open the `plugin.xml` file in a text editor.
3. Locate the following two commented blocks in this file and remove the comment tags from these blocks.

   ```xml
   <operation>
       <id>EDIT</id>
       <perspective>wcdf.edit</perspective>
   </operation>
   ```

   ```xml
   <overlays>
       <overlay id="launch" resourcebundle="content/pentaho-cdf-dd/lang/messages">
           <button id="launch_new_cde" label="${Launcher.CDE}" command="Home.openFile('${Launcher.CDE}', '${Launcher.CDE_TOOLTIP}', 'api/repos/wcdf/new');$('#btnCreateNew').popover('hide');"/>
       </overlay>
       <overlay id="startup.cde_dashboard"  resourcebundle="content/pentaho-cdf-dd/lang/messages" priority="1">
           <menubar id="newmenu">
               <menuitem id="new-cde_dashboard" label="${Launcher.CDE}" command="mantleXulHandler.openUrl('${Launcher.CDE}','${Launcher.CDE_TOOLTIP}','api/repos/wcdf/new')" />
           </menubar>
       </overlay>
   </overlays>
   ```
4. Save your changes.
5. Locate the `pentaho-solutions/system/pentaho-cdf-dd` and open the `settings.xml` file in a text editor.
6. Locate the block at the end of the file, `Defining the new-toolbar-button` and remove the comments tags from this block.

   ```xml
   <new-toolbar-button>1,New CDE Dashboard,CDE Dashboard,api/repos/wcdf/new</new-toolbar-button>
   ```
7. Save your changes.
8. Restart the Pentaho Server.

## Verify your Community Dashboard Editor (CDE) activation

To verify CDE is activated, do the following.

1. Log on to the Pentaho User Console:
   1. Launch a Web browser and enter the URL of the Pentaho Server.

      The page loads an introductory screen with a **Login** section.
   2. Enter your user name and password and click **Login**.

      ![Pentaho User Console Login](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-d36ad7045c31a6f0854f76cf8e973eb1599ac788%2FPUC_Login_Hitachi.png?alt=media)

      You are now logged into the User Console and ready to start creating and running reports and dashboards.
2. From the Home page, click the **Create New** button.
3. From the menu that displays, select the **New CDE Dashboard** option.

You can now begin creating your first CDE dashboard.

## See also

* [CDE Dashboard Overview](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-dashboard-overview)
* [CDE Quick Start Guide](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide)
