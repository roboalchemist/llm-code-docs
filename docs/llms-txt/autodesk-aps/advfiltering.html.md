# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/advfiltering.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="advanced-filtering-using-rsql">
<h1>Advanced Filtering Using RSQL</h1>
<p>AEC Data Model APIâs filtering expressions are influenced by the RESTful Service Query Language (RSQL), which is used to define filter expressions to limit the results for REST endpoints. Theâ¯filterâ¯query string parameters used with the AEC Data Model API endpoints require filter expressions similar to RSQL.</p>
<p>For more information, see <a class="reference external" href="https://github.com/jirutka/rsql-parser">RSQL grammar and syntax</a>.</p>
<p>Benefits of using RSQL are listed as follows:</p>
<ul class="simple">
<li>Provides a simple and easily understandable method of defining query filters.</li>
<li>Makes complex query definitions more effective than the other query languages such as GraphQL.</li>
<li>Can be extended using custom operators.</li>
</ul>
</section>
<section id="supported-operators">
<h1>Supported operators</h1>
<p><strong>Following are the operators supported in AEC Data Model GraphQL queries, with some examples:</strong></p>
<div class="table-section"><table><thead><tr><th class="head"><p>Actors</p></th>
<th class="head"><p>Type of params</p></th>
<th class="head"><p>Operation</p></th>
<th class="head"><p>Operator</p></th>
<th class="head"><p>Note</p></th>
</tr></thead><tbody>
<tr class="row-even"><td rowspan="9"><p>property name-value</td>
<td rowspan="6"><p>String</td>
<td rowspan="4"><p>Equality (case-insensitive):</p>
<p>Equality (case-sensitive)</p>
</td>
<td rowspan="4"><p>==</p>
<p>=caseSensitive=</p>
</td>
<td rowspan="6"><p>When comparing values or keys that contain spaces, it is necessary to enclose both
the left-hand side (LHS) and the right-hand side (RHS) in single quote</p>
<ul class="simple">
<li>ââproperty.name.Element Nameâ==NameOfElementâ</li>
<li>âproperty.name.category==âAreaââ</li>
</ul>
</td>
</tr>
<tr class="row-odd"></tr>
<tr class="row-even"></tr>
<tr class="row-odd"></tr>
<tr class="row-even"><td>InEquality</td>
<td>!=</td>
</tr>
<tr class="row-odd"><td>contains, startsWith, endsWith</td>
<td>=contains=, =startsWith=, =endsWith=</td>
</tr>
<tr class="row-even"><td>number, DateTime</td>
<td>==, !=, &lt;, &gt;, &lt;=, &gt;=</td>
<td></td>
<td>Float comparison values need to be specified using decimal digits.</td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>Boolean</td>
<td>Equality</td>
<td>==</td>
<td></td>
</tr>
<tr class="row-even"><td>Inequality</td>
<td>!=</td>
<td></td>
</tr>
<tr class="row-odd"><td>property name</td>
<td>String</td>
<td>Exact match</td>
<td>==</td>
<td></td>
</tr>
<tr class="row-even"><td rowspan="9"><p>property id-value</td>
<td rowspan="6"><p>String</td>
<td rowspan="4"><p>Equality (case-insensitive):</p>
<p>Equality (case-sensitive)</p>
</td>
<td rowspan="4"><p>==</p>
<p>=caseSensitive=</p>
</td>
<td rowspan="6"><p>Properties with enum values can be searched by property id-value, where the value must be provided as
the exact name of the enum</p>
<ul class="simple">
<li><dl class="docutils">
<dt>âproperty.id.autodesk.revit.parameter:parameter.elementContext-1.0.0==Instanceâ</dt><dd><p>where âInstanceâ is the name</p>
</dd>
</dl>
</li>
<li>âproperty.id.autodesk.revit.parameter:parameter.elementContext-1.0.0!=Instanceâ</li>
</ul>
</td>
</tr>
<tr class="row-odd"></tr>
<tr class="row-even"></tr>
<tr class="row-odd"></tr>
<tr class="row-even"><td>InEquality</td>
<td>!=</td>
</tr>
<tr class="row-odd"><td>contains, startsWith, endsWith</td>
<td>=contains=, =startsWith=, =endsWith=</td>
</tr>
<tr class="row-even"><td>number, DateTime</td>
<td>==, !=, &lt;, &gt;, &lt;=, &gt;=</td>
<td></td>
<td>Float comparison values need to be specified using decimal digits.</td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>Boolean</td>
<td>Equality</td>
<td>==</td>
<td></td>
</tr>
<tr class="row-even"><td>Inequality</td>
<td>!=</td>
<td></td>
</tr>
<tr class="row-odd"><td>property id</td>
<td>String</td>
<td>Exact match</td>
<td>==</td>
<td></td>
</tr>
<tr class="row-even"><td rowspan="3"><p>metadata</p>
<p>(On elementGroups)</p>
</td>
<td rowspan="3"><p>DateTime</td>
<td rowspan="3"><p>==, !=, &lt;, &gt;, &lt;=, &gt;=</td>
<td rowspan="3"></td>
<td rowspan="3"><p>Supported ISO 8601 formats (precision supported up to seconds):</p>
<ul class="simple">
<li>offset: 2020-01-20T15:00:00.000-07:00</li>
<li>UTC: 2020-01-20T22:00:00.000Z</li>
</ul>
</td>
</tr>
<tr class="row-odd"></tr>
<tr class="row-even"></tr>
</tbody></table></div>
</section>
<section id="compound-operations">
<h1>Compound operations</h1>
<p>Following is the list of supported compound operators, such as AND and OR operations:</p>
<ul class="simple">
<li>âproperty.name.categoryâ=contains=âPipesâ and âproperty.name.Element Nameâ=contains=âHVAC FM Boiler Feedâ.</li>
<li>Order of operations is Supported</li>
</ul>
<blockquote>
<div><ul class="simple">
<li>(property.name.category==Walls or property.name.category==Windows) and property.name.Length&gt;5.0.</li>
</ul>
</div></blockquote>
</section>
<section id="examples">
<h1>Examples</h1>
<p><strong>Following filters are supported for all elements queries:</strong></p>
<div class="table-section"><table><thead><tr><th>Filter type</th><th>Query</th><th>Expectation</th></tr></thead><tbody>
<tr class="row-even"><td>Property exists by name</td>
<td>âproperty.name==Perimeterâ</td>
<td>Returns elements with <cite>Perimeter</cite> property (case-sensitive).</td>
</tr>
<tr class="row-odd"><td>Property does not exist by name</td>
<td>âproperty.name!=Perimeterâ</td>
<td>Returns elements without the property <cite>Perimeter</cite> (case-sensitive).</td>
</tr>
<tr class="row-even"><td>By range</td>
<td>âproperty.name.area &gt;= 100 and property.name.area &lt; 200â</td>
<td>Returns elements with property area in the provided range.</td>
</tr>
<tr class="row-odd"><td>By name and value</td>
<td>âproperty.name.category==Areaâ</td>
<td>Returns elements with the property <cite>category</cite> equal to <cite>Area</cite> (case-insensitive).</td>
</tr>
<tr class="row-even"><td></td>
<td>ââproperty.name.Element Nameâ==âHVAC Feedââ</td>
<td>Returns elements with name âHVAC Feedâ (case insensitive).</td>
</tr>
<tr class="row-odd"><td></td>
<td>âproperty.name.Length &gt;= 2.0</td>
<td>Returns elements with property Length having values greater or equal to 2.0.</td>
</tr>
<tr class="row-even"><td>By multiple values</td>
<td>ââproperty.name.Family Nameâ==âRectangular Mullionâ or
âproperty.name.Family Nameâ==âWindow-Fixedââ</td>
<td>Returns elements with property âFamily Nameâ having values âRectangular Mullionâ or âWindow-Fixedâ.
(all value comparisons are not case-sensitive).</td>
</tr>
<tr class="row-odd"><td>Property exists by id</td>
<td>âproperty.id==autodesk.revit.parameter:curveElemLength-1.0.0â</td>
<td>Returns elements with property of id âautodesk.revit.parameter:curveElemLength-1.0.0â.</td>
</tr>
<tr class="row-even"><td>By id and value</td>
<td>âproperty.id.autodesk.revit.parameter:curveElemLength-1.0.0&gt;3.0â</td>
<td>Returns elements with property of id âautodesk.revit.parameter:curveElemLength-1.0.0â having values greater than 3.0</td>
</tr>
<tr class="row-odd"><td></td>
<td>âproperty.id.autodesk.revit.parameter:parameter.elementContext-1.0.0==Instanceâ</td>
<td>Returns elements with property of id âautodesk.revit.parameter:parameter.elementContext-1.0.0â with value âInstanceâ</td>
</tr>
<tr class="row-even"><td>By metadata (elements)</td>
<td>âmetadata.createdBy.email== <a class="reference external" href="mailto:First.Last%40autodesk.com">First<span>.</span>Last<span>@</span>autodesk<span>.</span>com</a>â</td>
<td>Returns elements with the <cite>createdBy</cite> user metadata with the email address.</td>
</tr>
<tr class="row-odd"><td></td>
<td>âmetadata.lastModifiedBy.email== <a class="reference external" href="mailto:First.Last%40autodesk.com">First<span>.</span>Last<span>@</span>autodesk<span>.</span>com</a>â</td>
<td>Returns elements with the <cite>lastModifiedBy</cite> user metadata with the email address.</td>
</tr>
<tr class="row-even"><td></td>
<td>âmetadata.elementId==âYWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ34xQ1dia2xtV1JTcTJ4bklhdkN4YzhRXzEwââ</td>
<td>Returns elements with id âYWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ34xQ1dia2xtV1JTcTJ4bklhdkN4YzhRXzEwâ</td>
</tr>
<tr class="row-odd"><td></td>
<td>âmetadata.revitElementId==â1055109ââ</td>
<td>Returns elements with specified Revit Element Id:  â1055109â</td>
</tr>
<tr class="row-even"><td>Inequality</td>
<td>âproperty.name.room!=1â</td>
<td>Returns elements of property âroomâ that does not have value 1.</td>
</tr>
<tr class="row-odd"><td>Wild card (starts with)</td>
<td>âproperty.name.room=startsWith=boilerâ</td>
<td>Returns elements that have property name âroomâ beginning with value âboilerâ (case-sensitive)</td>
</tr>
<tr class="row-even"><td rowspan="2"><p>by metadata,
where Date/Time is
greater than,less than or range</td>
<td>âmetadata.createdOn&gt;=2020-01-20T14:00:00Z and metadata.createdOn&lt;2020-12-20T14:00:00Zâ</td>
<td>Returns elements with createdOn metadata in the provided range</td>
</tr>
<tr class="row-odd"><td>âmetadata.lastModifiedOn&gt;2020-01-01T01:00:00Z and
metadata.lastModifiedOn&lt;2020-12-01T01:00:00Zâ</td>
<td>Returns elements with lastModifiedOn metadata in the provided range</td>
</tr>
</tbody></table></div>
<p><strong>Following filters are only supported for getting elements in an elementGroup:</strong></p>
<div class="table-section"><table><thead><tr><th>Filter type</th><th>Query</th><th>Expectation</th></tr></thead><tbody>
<tr class="row-even"><td>Wild card (ends with and contains)</td>
<td>âproperty.name.room=endsWith=boilerâ
âproperty.name.room=contains=Fire</td>
<td>Returns elements which have property name âroomâ ending with value âboilerâ (case insensitive).
Returns elements which have property âroomâ containing value âFireâ (case insensitive)</td>
</tr>
<tr class="row-odd"><td>case-sensitivity</td>
<td>âproperty.name.comment=caseSensitive=Verticalâ</td>
<td>Returns elements which have property âcommentâ with value âVerticalâ (case-sensitive check on âVerticalâ)</td>
</tr>
</tbody></table></div>
<p><strong>Following filters are supported for all elementGroups queries:</strong></p>
<div class="table-section"><table><thead><tr><th>Filter type</th><th>Query</th><th>Expectation</th></tr></thead><tbody>
<tr class="row-even"><td>By metadata (elementGroups)</td>
<td>âmetadata.createdOn&gt;=2020-01-20T14:00:00Z and metadata.createdOn&lt;2020-12-20T14:00:00Zâ</td>
<td>Returns elementGroups with createdOn metadata in the provided range.</td>
</tr>
<tr class="row-odd"><td rowspan="5"></td>
<td>âmetadata.lastModifiedOn&gt;2020-01-01T01:00:00Z and metadata.lastModifiedOn&lt;2020-12-01T01:00:00Zâ</td>
<td>Returns elementGroups with lastModifiedOn metadata in the provided range.</td>
</tr>
<tr class="row-even"><td>âmetadata.createdBy.email== <a class="reference external" href="mailto:First.Last%40autodesk.com">First<span>.</span>Last<span>@</span>autodesk<span>.</span>com</a>â</td>
<td>Returns elementGroups with the <cite>createdBy</cite> user metadata with the email address.</td>
</tr>
<tr class="row-odd"><td>âmetadata.lastModifiedBy.email== <a class="reference external" href="mailto:First.Last%40autodesk.com">First<span>.</span>Last<span>@</span>autodesk<span>.</span>com</a>â</td>
<td>Returns elementGroups with the <cite>lastModifiedBy</cite> user metadata with the email address.</td>
</tr>
<tr class="row-even"><td>âmetadata.name==âSnowdon Towers Sample Architectural.rvtââ</td>
<td>Returns elementGroups with name âSnowdon Towers Sample Architectural.rvtâ</td>
</tr>
<tr class="row-odd"><td>âmetadata.fileUrn==â<a class="reference external" href="urn:adsk.wipprod:dm.lineage:mgQk-s7vRy2I6BL7Ed1IYw">urn:adsk.wipprod:dm.lineage:mgQk-s7vRy2I6BL7Ed1IYw</a>ââ</td>
<td>Returns elementGroups with specified file urn.</td>
</tr>
</tbody></table></div>
</section>
<section id="special-considerations-for-elementgroup-filters">
<h1>Special Considerations for ElementGroup Filters</h1>
<section id="metadata-fileurn">
<a href="#metadata-fileurn"><h2>metadata.fileUrn:</h2></a>
<p>This filter can only be used by itself and not be used in combination with any other filter.</p>
<p><strong>Accepted Sample Query:</strong></p>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "query": "metadata.fileUrn=='urn:adsk.wipstg:dm.lineage:u-ncDS7gX3ZhpB3rgZXKeQ' or metadata.fileUrn=='urn:adsk.wipstg:dm.lineage:R8YVGN61QDaLElL0YSfkKg'"
    ...
}
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Rejected Sample Query:</strong></p>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "query": "metadata.fileUrn=='urn:adsk.wipstg:dm.lineage:u-ncDS7gX3ZhpB3rgZXKeQ' and metadata.createdBy.email=='first.last@autodesk.com'"
    ...
}
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "query": "metadata.fileUrn=='urn:adsk.wipstg:dm.lineage:u-ncDS7gX3ZhpB3rgZXKeQ'"
        "createdBy": "first.last@autodesk.com"
    ...
}
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="metadata-name">
<a href="#metadata-name"><h2>metadata.name:</h2></a>
<ul class="simple">
<li>This filter can only be used with one value and can not support multiple values (including coupling with convenience filter for name).</li>
<li>This filter can not be used with ORs, only ANDs are supported.</li>
</ul>
<p><strong>Accepted Sample Query:</strong></p>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "query": "metadata.name=='Snowdon Towers East.rvt' and metadata.createdBy.email=='first.last@autodesk.com'"
    ...
}
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "query": "metadata.name=='Snowdon Towers East.rvt'",
        "createdBy": "first.last@autodesk.com"
    ...
}
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Rejected Sample Query:</strong></p>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "query": "metadata.name=='Snowdon Towers East.rvt'",
        "name": "Snowdon Towers West.rvt"
    ...
}
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "query": "metadata.name=='Snowdon Towers East.rvt' or metadata.createdBy.email=='first.last@autodesk.com'"
    ...
}
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
</section>


            <div class="clearer"></div>
          </div>