# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/get-started-with-the-sample-pdi-project.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/get-started-with-the-sample-pdi-project.md

# Get started with the sample PDI project

This project is for experienced Java developers who want to create customized PDI plugins. To help you get started, we provide a sample Eclipse-based project with detailed code-level documentation for:

* Extending Pentaho Data Integration (PDI) functionality
* Embedding the PDI engine into your own Java applications

**Note:** Unless specifically stated otherwise, developing custom plugins and extending or embedding PDI is not covered under the standard Pentaho customer support agreement.

## Download the sample project

Download the sample PDI project file to learn how to create customized PDI plugins. The sample PDI project file is distributed in a ZIP file named `kettle-sdk-plugin-assembly-10.2.0.0-<build number>.zip`.

**Note:** The sample PDI project is provided "as is" and is subject to the warranty disclaimer contained in the applicable project license. The sample project is informational only. Do not use the sample project in production.

Complete the following steps to download the sample project file.

1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
2. In the Pentaho card, click **Download**.

   The Downloads page opens.
3. In the **10.x** list, click **See all \<number> articles** to see the full list of **10.x** downloads.
4. On the **10.x** page, click **Pentaho 10.2 GA Release**.
5. Scroll to the bottom of the **Pentaho 10.2 GA Release** page.
6. In the file component section, navigate to the `SDK` folder.
7. Download the `kettle-sdk-plugin-assembly-10.2.0.0-<build number>.zip` file.

## Set up a development environment

We recommend adapting the sample PDI project to your development environment. The sample PDI project comes preconfigured as an Eclipse project, complete with dependencies to a stable release of PDI. If you are developing for a specific version of PDI, you must replace the dependency JAR files to match your version of PDI. The PDI classes and methods are stable for any major version of PDI, so you can safely replace the JAR files and develop for any PDI 9.x release.

## Get PDI sources

When developing with PDI (also known as the Kettle project to the open source community), it is helpful to have the Kettle sources close by. Including them in development projects makes it possible to trace and step through core PDI code, which helps when debugging your solution.

**Note:** It is not necessary to modify or compile any of the PDI sources when embedding or extending PDI. Including the PDI sources in your projects is optional and is not supported.

PDI source code is publicly available from the Pentaho GitHub repository at <https://github.com/pentaho/pentaho-kettle>.

PDI follows the standard project layout for GitHub repositories. The version currently in development is hosted in the trunk folder, patch branches are hosted in the branch folders, and released versions are tagged in the tags folder.

If you are developing for a specific version of PDI, for instance , it is important to check-out or export the corresponding tag. To check which version you need to match your installation, select **Help** > **About** from the PDI client menu.

The **Build version** shows you which tag to use to match your installation.

\
Attach source to PDI JAR files
------------------------------

If you checked out PDI sources, you may want to associate the source to the matching PDI JAR files against which you are compiling your plugin. This optional step may improve the debugging experience, as it allows you to trace into PDI core code.

\
Additional developer documentation
----------------------------------

**Javadoc**

The javadoc documentation reflects the most recent stable release of PDI and is available at <https://javadoc.pentaho.com/>.
