# Source: https://docs.pentaho.com/pba-ctools/cde-advanced-solutions/embedding-dashboards-built-with-requirejs.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-advanced-solutions/embedding-dashboards-built-with-requirejs.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/embedding-dashboards-built-with-requirejs.md

# Embedding dashboards built with RequireJS

You can embed a RequireJS dashboard as a sub-dashboard in an application without saving it as a widget. This direct method of embedding sub-dashboards into a main dashboard avoids possible conflicts from mismatching libraries which can occur when using widgets. With RequireJS, you no longer need to use widgets to embed sub-dashboards into an application.

In this tutorial, you will learn how to embed the dashboard within Pentaho Server or embed the dashboard using a server other than Pentaho. These instructions assume that you are familiar with the [main features in CDE](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/CTools/CDE%20dashboard%20overview/CDE%20dashboard%20overview=GUID-45B6F4DA-C45F-482D-AA7A-99BE0016F616=4=en=.md) and the basic steps of [creating a dashboard in CDE](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/CTools/CDE%20quick%20start%20guide/CDE%20quick%20start%20guide=GUID-4DBA97DB-6E34-4E20-8815-6332FB0D8626=3=en=.md). In addition, these instructions assume that you have [activated the CDE plugin](https://docs.pentaho.com/pba-ctools/10.2-ctools/activate-cde).

Follow instructions for the type of server that you are using:

* [Embedding within Pentaho Server](#embedding-within-pentaho-server)
* [Embedding in a server other than Pentaho](#embedding-in-a-server-other-than-pentaho)

## Embedding within Pentaho Server

This walk-through tutorial assumes you have completed the steps in the [Create a Dashboard Using RequireJS](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/create-a-dashboard-using-requirejs) section. In this tutorial, you will embed the dashboard created in that tutorial into an HTML page hosted within the Pentaho Server.

1. On your Desktop, create a folder named `Embed` to hold the three files we will create and upload to the Pentaho Server in this tutorial:
   * `main.html`
   * `includeDashboards.js`
   * `styles.css`
2. Use a text editor to create a new HTML file and save it as `main.html` in the `Embed` folder you just created. Copy the following HTML code to the file:

   ```xml
   <!DOCTYPE html>
   <html>
     <head>
       <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
       <title>Embedding CDE Dashboards with RequireJS</title>
       <link rel="stylesheet" type="text/css" href="../../repo/files/:public:Embed:styles.css"/>
      <script type="text/javascript" src="../../../plugin/pentaho-cdf-dd/api/renderer/cde-embed.js"></script>
     </head>
     <body>
       <div class="headerContainer">
         <header class="header">
           <a class="logo" href="http://www.pentaho.com/">
             <img src="http://www.pentaho.com/sites/all/themes/pentaho_resp/_media/logo-pentaho-new.svg" alt="Pentaho Logo">
           </a>
           <div class="titleHTML">
             <strong>Embedding CDE Dashboards with RequireJS</strong>
           </div>
         </header>
       </div>
       <div class="dashboardContainer">
         <div id="content1"></div>
         <div id="content2"></div>
         <script src="../../repo/files/:public:Embed:includeDashboards.js"></script>
       </div>
     </body>
   </html>
   ```

   * Line 7 loads the `cde-embed.js` resource, which contains all the RequireJS configurations to embed CDE dashboards into the HTML page.
   * Line 20 creates a div which contains two other divs, identified as `content1` and `content2`, in which two instances of the required dashboard class will be rendered.
   * Line 23 loads the `includeDashboards.js` file, which uses RequireJS to load the demoDashboard CDE dashboard as a JavaScript class. This file creates both instances and associates each one to its respective div and executes its render function.
3. Create the `includeDashboards.js` file and save it in the `Embed` folder. Copy the following JS code to the file:

   ```javascript
   require([
     "dash!/public/demoDashboard/demoDashboard.wcdf"
   ], function(SampleDash) {
     // Create two instances of the same dashboard that use distinct DOM elements
     (new SampleDash("content1")).render();
     (new SampleDash("content2")).render();
   });
   ```

   * The CDE dashboard is obtained via the CDE endpoint, `/pentaho/plugin/pentaho-cdf-dd/api/renderer/getDashboard`. The path field in the query string must contain the path to the CDE dashboard. Below is an example.

     ```javascript
     require([
       "/pentaho/plugin/pentaho-cdf-dd/api/renderer/getDashboard?path=/public/demoDashboard/demoDashboard.wcdf"
     ], function(SampleDash) { /* code */ });
     ```
   * This endpoint returns a RequireJS module which contains a class for a specific dashboard which is used to create new dashboard instances. You can also embed a dashboard using the simpler dash! RequireJS loader plugin, such as in the `includeDashboards.js` source code. Below is an example.

     ```javascript
     require([
       "dash!/public/demoDashboard/demoDashboard.wcdf"
     ], function(SampleDash) { /* code */ });
     ```
4. Create the `styles.css` file in the `Embed` folder. Copy the following CSS code to the file:

   ```css
   body {
     padding: 10px;
   }

   img {
     width: 300px;
     padding-bottom: 10px;
   }
   ```
5. Zip the `Embed` folder, and then use PUC to upload the compressed folder to the Pentaho Server’s `Public` folder.
6. Finally, review your work. From the **Public** > **Embed** folder, open the `main.html`​ file. The embedded dashboard should look similar to the image below.

   ![Embedded dashboard example](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-76f566669bcd5d8d0d3ec42c88e50c3b1ed965c0%2FEmbeddedCharts.png?alt=media)

## Embedding in a server other than Pentaho

In this walk-through tutorial, you will embed the dashboard created in the [Create a dashboard using RequireJS](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/create-a-dashboard-using-requirejs) tutorial into an HTML page running on a server that is not the Pentaho Server. This process requires the following steps:

* [Step 1: Save the embed folder](#step-1-save-the-embed-folder)
* [Step 2: Edit the settings XML files](#step-2-edit-the-settings-xml-files)
* [Step 3: Edit the Pentaho XML file](#step-3-edit-the-pentaho-xml-file)
* [Step 4: Edit the main XML file](#step-4-edit-the-main-html-file)
* [Step 5: Access the embedded dashboard](#step-5-access-the-embedded-dashboard)

**Note:** Python 3 must be installed to use this tutorial.

### Step 1: Save the embed folder

If you have not done so already, save the `Embed` folder from the [previous tutorial](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions) to your Desktop.

### Step 2: Edit the settings XML files

Enable Cross Origin Resource Sharing (CORS) in the Community Dashboard Framework (CDF), Community Dashboard Editor (CDE), and Community Data Access (CDA). While you need CDE to embed the dashboard, you will access it from a different server other than the Pentaho Server, so CORS must be enabled in CDF, CDE and CDA. Open the following CDF, CDE, and CDA `settings.xml` files in a text editor:

* For CDF: `server/pentaho-server/pentaho-solutions/system/pentaho-cdf/settings.xml`.
* For CDE: `server/pentaho-server/pentaho-solutions/system/pentaho-cdf-dd/settings.xml`.
* For CDA: `server/pentaho-server/pentaho-solutions/system/cda/settings.xml`.

Make the following replacements in each `settings.xml` file:

1. In all `settings.xml` files, find the line:

   ```xml
   <allow-cross-domain-resources>false</allow-cross-domain-resources>
   ```

   and then change it to:

   ```xml
   <allow-cross-domain-resources>true</allow-cross-domain-resources>
   ```
2. In the `settings.xml` file for CDF and CDA, find the line:

   ```xml
   <cross-domain-resources-whitelist><!--intentionally left blank --></cross-domain-resources-whitelist>
   ```

   and then change it to:

   ```xml
   <cross-domain-resources-whitelist>http://localhost:2777</cross-domain-resources-whitelist
   ```

### Step 3: Edit the Pentaho XML file

Open the `server/pentaho-server/pentaho-solutions/system/pentaho.xml` file in a text editor and make the following replacements:

1. Find the line:

   ```xml
   <cors-request-allowed>false</cors-request-allowed>
   ```

   and then change it to:

   ```xml
   <cors-request-allowed>true</cors-request-allowed>
   ```
2. Find the line:

   ```xml
   <cors-requests-allowed-domains><!-- allowed domains here --></cors-requests-allowed-domains>
   ```

   and then change it to:

   ```xml
   <cors-requests-allowed-domains>http://localhost:2777</cors-requests-allowed-domains>
   ```

### Step 4: Edit the main HTML file

Open the `main.html` file from the previous tutorial and make the following replacements:

1. Replace lines 6 and 7 with the three lines of code below. This example assumes the Pentaho Server is running locally on host localhost port 8080.

   ```xml
   <link rel="stylesheet" type="text/css" href="styles.css"/>
   <link rel="stylesheet" type="text/css" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css"/>
   <script type="text/javascript" src="http://localhost:8080/pentaho/plugin/pentaho-cdf-dd/api/renderer/cde-embed.js"></script>
   ```

   **Note:** Adding the Bootstrap link tag minimizes the risk that the arrow images will fail to load, which may result when using CORS and font-fetching in CSS files. Updating the HTML script tag allows the `cde-embed.js` resource to be loaded from the correct location.
2. Replace line 24 with the following line of code:

   ```xml
   <script src="includeDashboards.js"></script>
   ```

### Step 5: Access the embedded dashboard

Perform the following steps to start the embedded dashboard in Python and access it through its URL:

1. Stop and restart the Pentaho Server.
2. Since Python 3 is being used in this tutorial, open a shell or terminal and navigate to the `Embed` folder directory.
3. Start a local HTTP server on localhost port 2777 by issuing the following Python command:

   ```python
   python -m http.server 2777
   ```
4. Access the dashboard via the URL `http://localhost:2777/main.html`. After logging in using your Pentaho credentials, you should have access to the following content:

   ![Embedded CDE dashboards with RequireJS example](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-76f566669bcd5d8d0d3ec42c88e50c3b1ed965c0%2FEmbeddedCharts.png?alt=media)
