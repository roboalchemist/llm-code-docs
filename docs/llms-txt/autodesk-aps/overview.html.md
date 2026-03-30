# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/overview.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="aec-data-model-api">
<h1>AEC Data Model API</h1>
<img alt="../../../_images/devloper_guide01.png" src="../../../_images/devloper_guide01.png">
<p>The AEC Data Model API, is a GraphQL-based API that provides the ability to directly interact with granular AEC data in the cloud without the need of building custom plug-ins for the desktop authoring tools like Revit, Civil 3D, Plant3D and other AEC connected design applications.</p>
<p>At launch, the API is read-only for querying elements and their properties data from published Revit 2024 and later version models.</p>
<p>The value of the AEC Data Model extends beyond providing granular data. It offers an intuitive and consistent data navigation experience through tailored APIs within the AEC domain. With these APIs, you can seamlessly explore your Hub, Projects, Folders, Files, and delve deep into detailed AEC data, including elements and parameters.</p>
<p>The AEC Data Model is designed to cater to the entire AEC Project Lifecycle, from Conceptual Design to Construction and Operations. It is part of a family of Autodesk Data Models provided by Autodesk to cater to diverse industries. Similar data models are developed for the Manufacturing and Media &amp; Entertainment industries.</p>
<section id="about-aec-data-model">
<a href="#about-aec-data-model"><h2>About AEC Data Model</h2></a>
<p>AEC Data Model is a set of capabilities that breaks up monolithic AEC files, such as .rvt files, into valuable, granular data that are managed securely in the cloud platform. This granular, object-level data is then made accessible through easy-to-use APIs, resulting in good user experience.</p>
<p>Over time, the AEC Data Model API capabilities will be enhanced to enable developers to read, write, and extend subsets of models through cloud-based workflows through a single interface without the need to write custom plug-ins for individual desktop authoring applications. Our mission with the AEC Data Model is to support iterative and distributed customer workflows, spanning multiple experiences and capabilities, supporting the delivery of complex requirements of projects in todayâs growing industry. Enhancing the accessibility and interoperability of AEC data starts with structuring it so that it can be mapped and connected across systems, which is a key capability that our AEC Data Model APIs enable.</p>
<p>AEC Data Model is built on three design principles:</p>
<ul class="simple">
<li><strong>Extensible</strong>: This data model will allow you to add your own classifications to reflect their workflows by adding custom data using basic and common data currencies.</li>
<li><strong>Flexible</strong>:  Flexibility is achieved through the different ways in which data can be related and categorized. For instance, a glass wall in a conference room may be regarded as both a window and a wall, such that it can be included both in the window schedule and as a room in the buildingâs specifications.</li>
<li><strong>Federated</strong>:  In addition to Properties, the AEC Data Model can store other data models, such as Analytical and Structural Models, Issues, Drawings, and Requests for Information, although these data models are not yet included in this.</li>
</ul>
<p>To adhere to these principles, AEC Data Model has taken inspiration from the <a class="reference external" href="https://en.wikipedia.org/wiki/Entity_component_system">Entity Component System (ECS)</a> design concept, which is primarily used in game engines for its flexibility. As such, AEC Data Model introduces new concepts and constructs in a canonical form to encompass all of AEC design-and-make data, irrespective of the authoring application.</p>
</section>
<section id="common-uses">
<a href="#common-uses"><h2>Common uses</h2></a>
<p>The AEC Data Model API exposes these capabilities through a user-friendly GraphQL interface tailored to the AEC industry. You can programmatically:</p>
<blockquote>
<div><ul class="simple">
<li>Navigate to your ACC (Autodesk Construction Cloud) account(s)/hub(s), project(s), and design(s) to retrieve granular data such as elements, parameters, and their values.</li>
<li>Retrieve the different versions of a design and query for elements at specific design version.</li>
<li>Search for elements within a design or across designs within a project or hub using specified search criteria.</li>
<li>List all available property definitions in a design or project.</li>
<li>Query elements based on their properties such as Categories (doors, windows, pipes, etc.) OR Parameter Name + Value (Area, Volume, etc.).</li>
<li>Query for unique values of a parameter in a design.</li>
</ul>
</div></blockquote>
<p>The first instalment of the AEC Data API enables:</p>
<blockquote>
<div><ul class="simple">
<li>Automation of workflows like identifying anomalies within design files for better quality control, locating null/missing data.</li>
<li>Generation of quantity takeoffs, schedules, procurement dashboards, reports and so on.</li>
<li>Web apps to visualize and engage with granular elements - properties and compare changes between different versions of a design.</li>
</ul>
</div></blockquote>
</section>
<section id="next-steps">
<a href="#next-steps"><h2>Next steps</h2></a>
<p>Firstly, <strong>Activate</strong> your ACC account to enable extraction to the AEC Data Model. To do this, contact your ACC Account Administrator and request that they enable your account for the AEC Data Model by following the steps provided. For more information, see -  <a class="reference external" href="/en/docs/aecdatamodel/v1/developers_guide/onboarding">AEC Data Model Onboarding</a>.</p>
<ul class="simple">
<li>Get started with ourâ¯<a class="reference external" href="https://aps.autodesk.com/en/docs/aecdatamodel/v1/tutorials">How-to Guide</a> that are based on typical AEC Data Model API workflows.</li>
<li>Explore ourâ¯<a class="reference external" href="/en/docs/aecdatamodel/v1/code_samples/code-samples">Code Samples</a>â¯that provide more complex, fully functioning, Github-based example applications.</li>
<li>Refer to theâ¯<a class="reference external" href="/en/docs/aecdatamodel/v1/reference/graphqlendpoint">Reference Guide</a> section, which will give you in-depth information to refine and create your own custom solutions.</li>
</ul>
</section>
</section>
<section id="terms-of-service">
<h1>Terms of service</h1>
<p>AEC Data Model API is subject to <a class="reference external" href="https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services/forge-platform-web-services-api-terms-of-service">APS Terms of Services.</a></p>
</section>


            <div class="clearer"></div>
          </div>