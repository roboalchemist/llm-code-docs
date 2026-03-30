# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/faq.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="frequently-asked-questions">
<h1>Frequently Asked Questions</h1>
<section id="why-cant-i-retrieve-data-from-my-models-using-the-aec-data-model-apis">
<a href="#why-cant-i-retrieve-data-from-my-models-using-the-aec-data-model-apis"><h2>Why canât I retrieve data from my models using the AEC Data Model APIs?</h2></a>
<p>It is possible that your models were not successfully extracted to the AEC Data Model due to the following reasons:</p>
<blockquote>
<div><ol class="arabic">
<li>You have not yet enabled your ACC Account to extract to AEC Data Model.</li>
<li>Your models are not Revit 2024 or later versions; as only Revit 2024 and later models are supported.</li>
<li>Your model is still being extracted to the AEC Data Model and may take some time. To get the status of your extraction, please follow the below steps:</p>
<ol class="arabic">
<li>After your model is successfully published to ACC Docs, note down the fileUrn you see for that model. You can find this fileUrn by clicking on the model to launch the viewer and selecting the value you see for entityid in the URL. Refer to file below.</li>
<li>Use the elementGroupExtractionStatus query and provide the fileUrn you previously noted along with the version number of your model.  Your request and response will be something like the following:</p>
<p><strong>Query:</strong></p>
<blockquote>
<div><dl>
<dt>query elementGroupExtractionStatus($fileUrn: ID!) {</dt><dd><dl class="docutils">
<dt>elementGroupExtractionStatus(fileUrn: $fileUrn) {</dt><dd><p>status
details</p>
</dd>
</dl>
<p>}</p>
</dd>
</dl>
<p>}</p>
</div></blockquote>
</li>
</ol>
<blockquote>
<div><p><strong>Query Variables:</strong></p>
<blockquote>
<div><dl class="docutils">
<dt>{</dt><dd><p>âfileUrnâ: â<a class="reference external" href="urn:adsk.wipstg:dm.lineage:rDygXWbaQHyO5viTsEdPYQ">urn:adsk.wipstg:dm.lineage:rDygXWbaQHyO5viTsEdPYQ</a>â</p>
</dd>
</dl>
<p>}</p>
</div></blockquote>
<p><strong>Response:</strong></p>
<blockquote>
<div><dl>
<dt>{</dt><dd><dl>
<dt>âdataâ: {</dt><dd><dl class="docutils">
<dt>âelementGroupExtractionStatusâ: {</dt><dd><p>âstatusâ: âSUCCESSâ,
âdetailsâ: âExtraction completed successfully.â</p>
</dd>
</dl>
<p>}</p>
</dd>
</dl>
<p>}</p>
</dd>
</dl>
<p>}</p>
</div></blockquote>
<p>The <code class="docutils literal notranslate"><span class="pre">elementGroupExtractionStatus</span></code> query can be found here: <a class="reference external" href="https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementgroupextractionstatus/">https://aps.autodesk.com/en/docs/aecdatamodel/v1/reference/queries/elementgroupextractionstatus/</a></p>
</div></blockquote>
</li>
<li>The query will promptly respond with one of three prebuilt status values: âIn_Progress,â âFailed,â or âSuccess.â</p>
<blockquote>
<div><ul class="simple">
<li>Success: Indicates you should be able to query the elementgroupsâ data using the AEC Data Model API.</li>
<li>In_Progress: Indicates your extraction to AEC Data Model is still in progress and you should check back again later. Larger models could take up to minutes/hour.</li>
<li>Failed: Indicates your extraction to AEC Data Model didnât succeed. This could be due to various reasons such as  your model was not Revit 2024 model or the backend may have run into an error due to either an unavailable service or unhandled exceptions.</li>
</ul>
<p>In cases of failure, we recommend submitting a Problem Report with the errors in your API response along with your Hub ID and Project ID.</p>
</div></blockquote>
</li>
<li>If you have uploaded your models of Revit 2024 or later versions to ACC Docs via Desktop Connecter, Docs API, and 3rd Party Plugins, then your models are not currently being extracted to AEC Data Model. This means that the data from these models is not accessible via the AEC Data Model API. This is a known limitation and we are actively working on resolving it.</li>
<li>The backend may have run into an error due to either an unavailable service or unhandled exceptions. In such instances, we recommend sharing the errors in your API response along with your Hub ID and Project ID to the support team through <a class="reference external" href="https://aps.autodesk.com/get-help">https://aps.autodesk.com/get-help</a>.</li>
</ol>
</div></blockquote>
</section>
<hr class="docutils">
<section id="why-is-filtering-elements-on-some-properties-not-working">
<a href="#why-is-filtering-elements-on-some-properties-not-working"><h2>Why is filtering elements on some properties not working?</h2></a>
<p>Most of the properties should be able to be resolved using referenceProperties and displayValue objects in our API. However, some properties that are enum properties are currently not supported for searching. Only âElement Contextâ enum property is supported for searching. For example, âproperty.name. Element Contextâ== Type (or Instance). This is a known limitation, and we are actively working on a solution. Please let us know where you are encountering this issue.</p>
</section>
<hr class="docutils">
<section id="how-to-maintain-refresh-tokens">
<a href="#how-to-maintain-refresh-tokens"><h2>How to maintain refresh tokens ?</h2></a>
<p>External Databases can be used to maintain refresh tokens by implementing scheduled tasks that automatically update and refresh the tokens at regular intervals. Refresh tokens serve the purpose of obtaining new three-legged tokens without requiring users to repeat the sign in process. These refresh tokens remain valid for 14 days. In this <a class="reference external" href="https://aps.autodesk.com/blog/maintaining-refresh-tokens-mongodb-triggers">blog</a>. You can find an approach that uses MongoDB to store the user tokens in a collection and automate the token refresh process. For more understanding of the refresh token process, please refer to the <a class="reference external" href="https://aps.autodesk.com/apis-and-services/authentication">Authentication API documentation</a>.</p>
</section>
<hr class="docutils">
<section id="how-to-query-data-from-elementgroups-hosted-in-regions-other-than-the-us">
<a href="#how-to-query-data-from-elementgroups-hosted-in-regions-other-than-the-us"><h2>How to query data from ElementGroups hosted in regions other than the US?</h2></a>
<p>For queries against data hosted in ACC hubs from regions other than the US, such as EMEA, you need to add the appropriate region header. If you donât specify a value in the header for other regions, the US region will be used as it is the default. For more information about how to specify the custom header value, refer to the <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/graphqlendpoint">GraphQL Endpoint</a> topic.</p>
<img alt="../../../_images/region_header.png" src="../../../_images/region_header.png">
<hr class="docutils">
</section>
</section>


            <div class="clearer"></div>
          </div>