# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/about_aecima_data_explorer.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <meta name="keywords" content="API, AEC Data Model, AEC DM, AECCIM, CIM, Autodesk, Forge"><section id="about-the-aec-data-model-explorer">
<h1>About the AEC Data Model Explorer</h1>
<p>The <a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">AEC Data Model Explorer</a> is an interactive browser-based user interface. It is designed for exploring and executing GraphQL queries against the AEC Data Model API. It includes an autocomplete feature, which automatically suggests potential fields as you type a query. The Autodesk AEC Data Model Beta connects to a test ACC Hub with sample Revit Models. A new <strong>Viewer</strong> option is now available in the latest GraphiQL explorer. This option allows you to preview the model based on the model ID also known as design URN.</p>
<p><strong>Note:</strong> AEC Data Model Explorer accesses your production data.</p>
<section id="using-aec-data-model-explorer">
<a href="#using-aec-data-model-explorer"><h2>Using AEC Data Model Explorer</h2></a>
<p>To use AEC Data Model Explorer with the API:</p>
<ul class="simple">
<li>Provision the client id âHKVjhUXySDGLGJimolxAgDdpoCuZLlqlâ to your ACC Hub using the steps mentioned <a class="reference external" href="https://tutorials.autodesk.io/#provision-access-in-other-products">here</a>.</li>
<li>Use your Autodeskâs credential to sign in toâ¯<a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">aecdatamodel-explorer.autodesk.io</a>.</li>
<li>Refer to the <a class="reference external" href="/en/docs/aecdatamodel/v1/tutorials/before_you_begin#step-3-sign-in-to-aec-data-model-explorer">Sign in to AEC Data Model Explorer</a> for detailed steps.</li>
<li>You can also clone the <a class="reference external" href="https://github.com/autodesk-platform-services/aps-aecdatamodel-explorer">AEC Data Model Explorer source code</a> to use with your own APS application.</li>
</ul>
</section>
<section id="user-interaction-elements">
<a href="#user-interaction-elements"><h2>User interaction elements</h2></a>
<p>This section describes the GUI elements of the explorer, such as panes, tabs, buttons, toggle button for viewer, etc.</p>
<section id="explorer-panes">
<h3>Explorer panes</h3>
<p>The following image illustrates the elements of Explorer pane. Refer to the table below for an explanation about the Panes.</p>
<img alt="User Interaction Elements in AEC Data Model Explorer. Refer to the table below for an explanation about explorer panes." src="../../../_images/aec_cim_xplorr_01.png">
<div class="table-section"><table><thead><tr><th>No.</th><th>Interaction Elements</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>1</td>
<td>Query Pane</td>
<td>The pane where you can author GraphQL queries and mutations.</td>
</tr>
<tr class="row-odd"><td>2</td>
<td>Query Variables &amp; Request Headers Pane</td>
<td>The pane where you can add and edit Query Variables or additional Request Headers.</td>
</tr>
<tr class="row-even"><td>3</td>
<td>Results Pane</td>
<td>Displays responses of the queries executed.</td>
</tr>
</tbody></table></div>
</section>
<section id="interactive-elements">
<h3>Interactive elements</h3>
<p>Following screenshot identifies important User Interaction (UI) elements of the explorer. Refer to the table below for an explanation of each UI element.</p>
<img alt="User Interaction Elements in AEC Data Model Explorer. Refer to the table below for an explanation about explorer panes." src="../../../_images/aec_cim_xplorr_02.png">
<div class="table-section"><table><thead><tr><th>No.</th><th>Interaction Elements</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>1</td>
<td>Documentation Explorer Button</td>
<td>Displays the user documentation pane.</td>
</tr>
<tr class="row-odd"><td>2</td>
<td>History Button</td>
<td>Displays history of queries recently sent in the left side of the screen.</td>
</tr>
<tr class="row-even"><td>3</td>
<td>Prettify Button</td>
<td>Reformats the query for readability.</td>
</tr>
<tr class="row-odd"><td>4</td>
<td>Play Button</td>
<td>Runs the query and displays response in the result pane.</td>
</tr>
<tr class="row-even"><td>5</td>
<td>Merge Button</td>
<td>Merges any GraphQL fragments into the query.</td>
</tr>
<tr class="row-odd"><td>6</td>
<td>Copy Button</td>
<td>Copies the query present in the Query Pane.</td>
</tr>
<tr class="row-even"><td>7</td>
<td>Project ID Input</td>
<td>Accepts the Project ID of a project to which the model is associated with.</td>
</tr>
<tr class="row-odd"><td>8</td>
<td>Model Viewer Toggle</td>
<td>Toggle button to show or hide the model viewer.</td>
</tr>
<tr class="row-even"><td>9</td>
<td>Voyager</td>
<td>Redirects to the Voyager interface to explore the schema structure.</td>
</tr>
<tr class="row-odd"><td>10</td>
<td>Settings Dialog</td>
<td>Displays configurations for the UI theme and Data Cache.</td>
</tr>
<tr class="row-even"><td>11</td>
<td>Short Keys Guide</td>
<td>Displays guide which breaks down keyboard shortcuts for quick functionalities.</td>
</tr>
<tr class="row-odd"><td>12</td>
<td>Re-fetch Button</td>
<td>Re-fetches the GraphQL Schema.</td>
</tr>
<tr class="row-even"><td>13</td>
<td>Request Headers Tab</td>
<td>The tab where you can add and edit additional Request Headers.</td>
</tr>
<tr class="row-odd"><td>14</td>
<td>Query Variables Tab</td>
<td>The tab where you can add and edit Query Variables.</td>
</tr>
</tbody></table></div>
<p><strong>Tip</strong>: You can view the user documentation of a particular term by holding Control (on Windows) or Command (on macOS) key on your keyboard and clicking the term. After clicking, the Documentation Explorer appears on the right side of the screen. You can also use the <strong>Viewer</strong> button to toggle the model preview.</p>
<p>After Documentation Explorer opens, you should see an image similar to the one following with the description of the fields in the table below it.</p>
<blockquote>
<div><img alt="../../../_images/aec_cim_xplorr_03.png" src="../../../_images/aec_cim_xplorr_03.png">
</div></blockquote>
<div class="table-section"><table><thead><tr><th>No.</th><th>Interaction Elements</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>1</td>
<td>Documentation Explorer Button</td>
<td>Displays the user documentation pane.</td>
</tr>
<tr class="row-odd"><td>2</td>
<td>Documentation Explorer</td>
<td>Displays user documentation on the fly when working with queries within the AEC Data Model Explorer.</td>
</tr>
<tr class="row-even"><td>3</td>
<td>Query Term</td>
<td>A valid schema term which can be described using the Query Pane Term Viewer.</td>
</tr>
<tr class="row-odd"><td>4</td>
<td>Query Pane Term Viewer</td>
<td>Using the keyboard short key and selecting a term, displays the definition of the respective term within the Query Pane.</td>
</tr>
</tbody></table></div>
</section>
</section>
<section id="sending-queries">
<a href="#sending-queries"><h2>Sending queries</h2></a>
<ol class="arabic">
<li>In the Query Pane, enter your query. As you enter the query, autocomplete assists you in completing the query.</li>
<li>In the Query Variables Pane, specify the variable and its value in JSON format.</p>
<p><strong>Note:</strong> The Query Variable Pane is collapsed by default, so click QUERY VARIABLES to expand the Query Variable Pane.</p>
</li>
<li>Click <strong>Play</strong> to send the query to the GraphQL server. The response is displayed in the pane on the right.</li>
</ol>
</section>
<section id="handling-token-expiration">
<a href="#handling-token-expiration"><h2>Handling token expiration</h2></a>
<p>The AEC Data Model Explorer handles access tokens transparently. If you are notified that the access token has expired, refresh the browser or close the browser and sign in again. If the problem persists, try clearing your browserâs cache before signing in again.</p>
</section>
</section>


            <div class="clearer"></div>
          </div>