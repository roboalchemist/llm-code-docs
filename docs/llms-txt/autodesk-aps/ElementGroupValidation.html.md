# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/code_samples/ElementGroupValidation.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="elementgroup-validation-sample-workflow">
<h1>Elementgroup Validation Sample Workflow</h1>
<p>Validating data property names, units, and types used across elementgroups in a project is a valuable QA/QC process.
This sample automates this task using the AEC Data Model APIs.</p>
<p>See this code sample at <a class="reference external" href="https://github.com/autodesk-platform-services/aps-aecdatamodel-samples">AEC Data Model Samples git repository</a></p>
<p><strong>Note</strong>: This code sample requires .NET 6.</p>
<section id="before-you-begin">
<a href="#before-you-begin"><h2>Before You Begin</h2></a>
<ol>
<li>If you do not have an app registered, follow the procedure outlined in <a class="reference external" href="https://aps.autodesk.com/en/docs/oauth/v2/tutorials/create-app/">Create an App</a> to sign up for an APS account (if required) and obtain a Client ID for your app.</p>
<ul class="simple">
<li>Make sure that you add the following as the Callback URL: http://localhost:8080/api/auth/callback</li>
<li>Contact us to enable AEC Data Model API for your app and ACC hub.</li>
</ul>
</li>
<li>Install <a class="reference external" href="https://dotnet.microsoft.com/en-us/download">.NET 6</a></li>
<li>Clone or download the Git Repository. Itâs recommended to install GitHub desktop. To clone it via command line, use the following command (Terminal on MacOSX/Linux, Git Shell on Windows):</p>
<div class="highlight-default notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span> <span class="n">git</span> <span class="n">clone</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">autodesk</span><span class="o">-</span><span class="n">platform</span><span class="o">-</span><span class="n">services</span><span class="o">/</span><span class="n">aps</span><span class="o">-</span><span class="n">aecdatamodel</span><span class="o">-</span><span class="n">samples</span><span class="o">.</span><span class="n">git</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</li>
</ol>
</section>
<section id="setting-up-the-application">
<a href="#setting-up-the-application"><h2>Setting up the Application</h2></a>
<div class="highlight-default notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="n">Define</span> <span class="n">the</span> <span class="n">following</span> <span class="n">environment</span> <span class="n">variables</span><span class="p">:</span>

  <span class="n">Mac</span> <span class="n">OSX</span><span class="o">/</span><span class="n">Linux</span> <span class="p">(</span><span class="n">Terminal</span><span class="p">)</span>

    <span class="n">dotnet</span> <span class="n">restore</span>
    <span class="n">export</span> <span class="n">APS_CLIENT_ID</span><span class="o">=&lt;&lt;</span><span class="n">YOUR</span> <span class="n">CLIENT</span> <span class="n">ID</span> <span class="n">FROM</span> <span class="n">DEVELOPER</span> <span class="n">PORTAL</span><span class="o">&gt;&gt;</span>
    <span class="n">export</span> <span class="n">APS_CLIENT_SECRET</span><span class="o">=&lt;&lt;</span><span class="n">YOUR</span> <span class="n">CLIENT</span> <span class="n">SECRET</span><span class="o">&gt;&gt;</span>
    <span class="n">export</span> <span class="n">APS_CALLBACK_URL</span><span class="o">=</span><span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">localhost</span><span class="p">:</span><span class="mi">8080</span><span class="o">/</span><span class="n">api</span><span class="o">/</span><span class="n">auth</span><span class="o">/</span><span class="n">callback</span>

  <span class="n">Windows</span>

    <span class="n">dotnet</span> <span class="n">restore</span>
    <span class="nb">set</span> <span class="n">APS_CLIENT_ID</span> <span class="o">=&lt;&lt;</span><span class="n">YOUR</span> <span class="n">CLIENT</span> <span class="n">ID</span> <span class="n">FROM</span> <span class="n">DEVELOPER</span> <span class="n">PORTAL</span><span class="o">&gt;&gt;</span>
    <span class="nb">set</span> <span class="n">APS_CLIENT_SECRET</span> <span class="o">=&lt;&lt;</span><span class="n">YOUR</span> <span class="n">CLIENT</span> <span class="n">SECRET</span><span class="o">&gt;&gt;</span>
    <span class="nb">set</span> <span class="n">APS_CALLBACK_URL</span><span class="o">=</span><span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">localhost</span><span class="p">:</span><span class="mi">8080</span><span class="o">/</span><span class="n">api</span><span class="o">/</span><span class="n">auth</span><span class="o">/</span><span class="n">callback</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p>When using <a class="reference external" href="https://code.visualstudio.com">Visual Studio Code</a>, you can specify the environment variables listed above in a <em>.env</em> file in this folder, and run and debug the application directly from the editor.</p>
<p>In Microsoft Visual Studio, you can set the variables through Debug &gt; aps-aecdatamodel-samples Properties and add the three Environment variables as follows: APS_CLIENT_ID=&lt;<your client="" id="" from="" developer="" portal="">&gt;,APS_CLIENT_SECRET=&lt;<your client="" secret="">&gt;,APS_CALLBACK_URL=http://localhost:8080/api/auth/callback</your></your></p>
</section>
<section id="running-the-sample">
<a href="#running-the-sample"><h2>Running the Sample</h2></a>
<p>To run the sample, you need to execute the following command in the terminal:</p>
<div class="highlight-default notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span> <span class="n">dotnet</span> <span class="n">run</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p>Go to <a class="reference external" href="http://localhost:8080">http://localhost:8080</a>, and then select Go to sample for Elementgroups Validation Sample Workflow.</p>
<p><img alt="go to Elementgroups validation sample" src="https://user-images.githubusercontent.com/75683555/230185430-b92c3f69-cdbd-4d7a-a77a-fa39ea5df697.png"></p>
<p>Afterwards, youâll need to login with your Autodesk (ACC) account before proceeding with the next steps.</p>
</section>
<section id="workflow-description">
<a href="#workflow-description"><h2>Workflow Description</h2></a>
<ol>
<li>List all hubs</p>
<p>After login (top-right), click on <code class="docutils literal notranslate"><span class="pre">List</span> <span class="pre">Hubs</span></code> and take note of the hubId (<code class="docutils literal notranslate"><span class="pre">id</span></code>). <a class="reference external" href="https://github.com/autodesk-platform-services/aps-aecdatamodel-samples/blob/main/Controllers/HubsProjects.cs">See C# code</a>.</p>
<p><img alt="Step 1" src="../../../_images/hubs.png"></p>
</li>
<li>List all projects</p>
<p>Use the <code class="docutils literal notranslate"><span class="pre">HubId</span></code> from step 1 to list all projects and take note of the projectId (<code class="docutils literal notranslate"><span class="pre">id</span></code>). <a class="reference external" href="https://github.com/autodesk-platform-services/aps-aecdatamodel-samples/blob/main/Controllers/HubsProjects.cs">See C# code</a>.</p>
<p><img alt="Step 2" src="../../../_images/projects.png"></p>
</li>
<li>List all properties</p>
<p>This step uses <code class="docutils literal notranslate"><span class="pre">projectId</span></code>. Click on List all properties. <a class="reference external" href="https://github.com/autodesk-platform-services/aps-aecdatamodel-samples/blob/main/Controllers/ElementGroupValidation.cs">See C# code</a>.</p>
<p><img alt="Step 3" src="../../../_images/allproperties.png"></p>
<p>Query used in case no cursor is provided:</p>
<div class="highlight-default notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>
 elementGroupsByProject(projectId: $projectId) {
   pagination{
     pageSize
     cursor
   }
   results{
     name
     id
     propertyDefinitions{
       results{
         id
         name
         description
         specification
       }
     }
   }
 }
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p>Query used in case a valid cursor is provided:</p>
<div class="highlight-default notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>
 elementGroupsByProject(projectId: $projectId, pagination:{cursor:"cursor string here"}) {
   pagination{
     pageSize
     cursor
   }
   results{
     name
     id
     propertyDefinitions{
       results{
         id
         name
         description
         specification
       }
     }
   }
 }
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p>The variables are the same in both cases:</p>
<div class="highlight-default notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
  <span class="n">projectId</span> <span class="o">=</span> <span class="s2">"Your project ID"</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</li>
</ol>
  <script>var surveyServerUrl="https://developer-dev.api.autodesk.com/forge-private-beta/survey"; var machineAdd=""; fetch('https://api.ipify.org?format=json') .then(response=>response.json()) .then(data=>{ machineAdd=data.ip}); var myHeaders=new Headers(); myHeaders.append("Content-Type", "application/json"); function submitYes(source){ var data={ fields:{ "Page Title": document.title, "Section": findNearestHeading(source.form), "Page URL": window.location.href, "Was this section useful?": "Yes", "Address" : machineAdd}}; var raw=JSON.stringify(data); var requestOptions={ method: 'POST', headers: myHeaders, body: raw, redirect: 'follow'}; source.form.innerHTML='Thank You!'; fetch(`${surveyServerUrl}/survey-responses`, requestOptions) .then(response=>response.text()) .then(result=>console.log(result)) .catch(error=>console.log('error', error));}; var lastID, userEmail; function submitNo(source){ var data={ fields:{ "Page Title": document.title, "Section": findNearestHeading(source.form), "Page URL": window.location.href, "Was this section useful?": "No", "Address" : machineAdd}}; var raw=JSON.stringify(data); var requestOptions={ method: 'POST', headers: myHeaders, body: raw, redirect: 'follow'}; if (!userEmail){ var emailProfile=document.getElementsByClassName('adskf__profile-email')[0]; if (emailProfile !=null){ userEmail=emailProfile.textContent;} else{ userEmail="";}} console.log("userEmail: " + userEmail); source.form.innerHTML='<span>Thank You. What could make this more useful?</span><br>' + '<textarea></textarea><br>' + 'Your Email (optional): <input type="text" value="' + userEmail + '"><br>' + '<input class="submit-button" type="button" value="Submit" onclick="submitFeedback(this)">'; fetch(`${surveyServerUrl}/survey-responses`, requestOptions) .then(response=>response.text()) .then(result=>{ console.log(result); lastID=JSON.parse(result).id; console.log(lastID);}) .catch(error=>console.log('error', error));}; function submitFeedback(source){ userEmail=source.form.getElementsByTagName("input")[0].value; var data={ records: [{ "id": lastID, fields:{ "Email": source.form.getElementsByTagName("input")[0].value, "What could make this more useful?": source.form.getElementsByTagName("textarea")[0].value}}]}; var raw=JSON.stringify(data); var requestOptions={ method: 'PUT', headers: myHeaders, body: raw, redirect: 'follow'}; source.form.innerHTML='Thank You.'; fetch(`${surveyServerUrl}/survey-responses`, requestOptions) .then(response=>response.text()) .then(result=>console.log(result)) .catch(error=>console.log('error', error));}; function findNearestHeading(sourceForm){ var h1, h2, h3; var nodes=document.querySelectorAll('h1, h2, h3, form'); for (var i=0; i < nodes.length; i++){ if (nodes[i].nodeName=="H1"){ h1=nodes[i].textContent; h2=h3=null;} if (nodes[i].nodeName=="H2"){ h2=nodes[i].textContent; h3=null;} if (nodes[i].nodeName=="H3") h3=nodes[i].textContent; if (nodes[i]==sourceForm) break;} h1=h1 && (h2 || h3) ? h1 + " / " : h1 || ""; h2=h2 && h3 ? h2 + " / " : h2 || ""; h3=h3 || ""; var section=h1 + h2 + h3; console.log(section); return section;}; function checkEnter(e){ e=e || event; var txtArea=/textarea/i.test((e.target || e.srcElement).tagName); return txtArea || (e.keyCode || e.which || e.charCode || 0) !==13;}</script><style>.mini-survey{ font-family: sans-serif; font-size: 90%; padding: 8px; display: block; border-radius: 4px; width: max-content; margin-top: 10px !important; opacity: .75; border: 1px solid #ccc;} .mini-survey span{ margin-right: 4px;} .mini-survey input{ font-family: sans-serif; font-size: 98%; margin-right: 4px; width: unset !important;} .mini-survey input[type=button]{ border: 0;} .mini-survey input[type=button]{ border: 1px solid #666 !important; border-radius: 4px; padding: 6px; min-width: 50px;} .mini-survey input[type=button]:hover, .mini-survey .submit-button:hover{ background-color: #5f60ff; color:#fff; border-color: #5f60ff !important; font-weight: bold;} .mini-survey .submit-button{ background-color: rgb(231, 231, 231); margin-top: 5px; border: 1px solid #666; padding: 4px; min-width: 70px !important;} .mini-survey textarea{ font-family: sans-serif; font-size: 98%; margin: 4px 0; width: 300px; height: 60px} .divider-survey{ border-top: 1px solid #ccc; border-bottom: 1px solid #ccc; margin: auto; text-align: center; background-color: unset; border-radius: unset; width: unset;} .QSISlider{ display: none !important;}</style><form class="mini-survey" onkeypress="return checkEnter(event)"><span>Was this section useful?</span><input type="button" value="Yes" onclick="submitYes(this)"><input type="button" value="No" onclick="submitNo(this)"></form></section>
</section>


            <div class="clearer"></div>
          </div>