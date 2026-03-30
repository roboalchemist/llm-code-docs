# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/stdfiltering.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="standard-filtering-capabilities">
<h1>Standard Filtering Capabilities</h1>
<p>The AEC Data Model API provides a set of standard filtering options to enable filtering expressions as a core capability. They provide a simpler method for applying commonly-used filters, and can be used either as an alternative to or combined with Advanced Filtering Capabilities RSQL.
These standard filtering options are available for ElementGroup and Element queries.</p>
</section>
<section id="supported-filtering-options">
<h1>Supported Filtering Options</h1>
<p><strong>Following are the standard filtering options supported in AEC Data Model GraphQL ElementGroup queries:</strong></p>
<div class="table-section"><table><thead><tr><th>Fields</th><th>Type of params</th><th>Sample ElementGroup Query Filter</th><th>Expected Response</th></tr></thead><tbody>
<tr class="row-even"><td>Name</td>
<td>String</td>
<td>ânameâ: âSnowdon Towers Sample</td>
<td>Returns elementGroups with name âSnowdon Towers Sample Architectural.rvt</td>
</tr>
<tr class="row-odd"><td>fileUrn</td>
<td>String</td>
<td>âfileUrnâ: â<a class="reference external" href="urn:adsk.wipstg:dm.lineage:u-ncDS7gX3ZhpB3rgZXKeQ">urn:adsk.wipstg:dm.lineage:u-ncDS7gX3ZhpB3rgZXKeQ</a>â</td>
<td>Returns elementGroups with file URN â<a class="reference external" href="urn:adsk.wipstg:dm.lineage:u-ncDS7gX3ZhpB3rgZXKeQ">urn:adsk.wipstg:dm.lineage:u-ncDS7gX3ZhpB3rgZXKeQ</a>â</td>
</tr>
<tr class="row-even"><td>createdBy</td>
<td>String</td>
<td>âcreatedByâ: â<a class="reference external" href="mailto:first.last%40autodesk.com">first<span>.</span>last<span>@</span>autodesk<span>.</span>com</a>â</td>
<td>Returns elementGroups created by the user with email â<a class="reference external" href="mailto:johndoer%40autodesk.com">johndoer<span>@</span>autodesk<span>.</span>com</a>â</td>
</tr>
<tr class="row-odd"><td>lastModifiedBy</td>
<td>String</td>
<td>âlastModifiedByâ: â<a class="reference external" href="mailto:first.last%40autodesk.com">first<span>.</span>last<span>@</span>autodesk<span>.</span>com</a>â</td>
<td>Returns elementGroups that were last modified by the user with email â<a class="reference external" href="mailto:johndoer%40autodesk.com">johndoer<span>@</span>autodesk<span>.</span>com</a>â</td>
</tr>
</tbody></table></div>
<p><strong>Following are the standard filtering options supported in AEC Data Model GraphQL Elements queries:</strong></p>
<div class="table-section"><table><thead><tr><th>Fields</th><th>Type of params</th><th>Sample Element Query Filter</th><th>Expected Response</th></tr></thead><tbody>
<tr class="row-even"><td>Name</td>
<td>String</td>
<td colspan="2"><p>ânameâ: â2.5" x 5" rectangular (Orange)â</td>
<td>Returns elements with name â2.5" x 5" rectangular (Orange)â</td>
</tr>
<tr class="row-odd"><td>nameWithComparator</td>
<td>{ âvalueâ: String, âcomparatorâ: Enum }</td>
<td colspan="2"><p>ânameWithComparatorâ: { âvalueâ: âWallâ, âcomparatorâ: âCONTAINSâ }</td>
<td>Returns elements whose name contains the string âWallâ</td>
</tr>
<tr class="row-even"><td rowspan="4"><p>properties</td>
<td rowspan="2"><p>{ ânameâ: String, âvalueâ: String, âvalueWithComparatorâ: { âvalueâ: String, âcomparatorâ: Enum } }</td>
<td colspan="2"><p>âpropertiesâ: { ânameâ: âElement Contextâ, âvalueâ: âInstanceâ }</td>
<td>Returns elements that are instances</td>
</tr>
<tr class="row-odd"><td colspan="2"><p>âpropertiesâ: { ânameâ: âFamily Nameâ, âvalueWithComparatorâ: { âvalueâ: âMainâ, âcomparatorâ: âSTARTS_WITHâ } }</td>
<td>Returns elements with a âFamily Nameâ that starts with the string âMainâ</td>
</tr>
<tr class="row-even"><td rowspan="2"><p>{ âidâ: String, âvalueâ: String, âvalueWithComparatorâ: { âvalueâ: String, âcomparatorâ: Enum } }</td>
<td colspan="2"><p>âpropertiesâ: { âidâ: âautodesk.revit.parameter:parameter.elementContext-1.0.0â, âvalueâ: âInstanceâ }</td>
<td>Returns elements that are instances</td>
</tr>
<tr class="row-odd"><td colspan="2"><p>âpropertiesâ: { âidâ: âautodesk.revit.parameter:parameter.elementContext-1.0.0â, âvalueWithComparatorâ: { âvalueâ: âInstanceâ, âcomparatorâ: âNOT_EQUALâ } }</td>
<td>Returns elements that are <strong>NOT</strong> instances</td>
</tr>
<tr class="row-even"><td>references</td>
<td>{ ânameâ: String, âreferenceIdâ: String }</td>
<td colspan="2"><p>âreferencesâ: { ânameâ: âTypeâ, âreferenceIdâ: âYWVjZX5JR1TYdWROM2Qxdâ }</td>
<td>Returns elements with a âTypeâ reference to the element with id âYWVjZX5JR1TYdWROM2Qxdâ</td>
</tr>
<tr class="row-odd"><td>CreatedBY</td>
<td>String</td>
<td colspan="2"><p>âcreatedByâ: â<a class="reference external" href="mailto:john.doer%40autodesk.com">john<span>.</span>doer<span>@</span>autodesk<span>.</span>com</a>â</td>
<td>Returns elements created by the user with email â<a class="reference external" href="mailto:john.doer%40autodesk.com">john<span>.</span>doer<span>@</span>autodesk<span>.</span>com</a>â</td>
</tr>
<tr class="row-even"><td>lastModifiedBy</td>
<td>String</td>
<td colspan="2"><p>âlastModifiedByâ: â<a class="reference external" href="mailto:john.doer%40autodesk.com">john<span>.</span>doer<span>@</span>autodesk<span>.</span>com</a>â</td>
<td>Returns elements that were last modified by the user with email â<a class="reference external" href="mailto:john.doer%40autodesk.com">john<span>.</span>doer<span>@</span>autodesk<span>.</span>com</a>â</td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>elementId</td>
<td rowspan="2"><p>String</td>
<td colspan="2" rowspan="2"><p>âelementIdâ: âYWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ34xQ1dia2xtV1JTcTJ4bklhdkN4YzhRXzEwâ</td>
<td rowspan="2"><p>Returns elements with id:</p>
<p>âYWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ34xQ1dia2xtV1JTcTJ4bklhdkN4YzhRXzEwâ</p>
</td>
</tr>
<tr class="row-even"></tr>
<tr class="row-odd"><td>revitElementId</td>
<td>String</td>
<td colspan="2"><p>ârevitElementIdâ: â1055109â</td>
<td>Returns elements with specified Revit Element Id: â1055109â</td>
</tr>
</tbody></table></div>
<p><strong>NOTE</strong>: The <strong>comparator</strong> Enum can be one of: <strong>CASE_SENSITIVE</strong>, <strong>CONTAINS</strong>, <strong>STARTS_WITH</strong>, <strong>ENDS_WITH</strong>, <strong>GREATER_THAN</strong>, <strong>GREATER_THAN_EQUAL_TO</strong>, <strong>LESS_THAN</strong>, <strong>LESS_THAN_EQUAL_TO</strong>, or <strong>NOT_EQUAL</strong>.</p>
</section>
<section id="compound-filtering-options">
<h1>Compound Filtering Options</h1>
<p>When multiple convenience fields are provided, the AND operator will be used to compare across fields.</p>
<p><strong>NOTE</strong>: having multiple properties or references with different names are considered to be different fields. This can be done by defining an array of properties or references, with each property or reference having a different name/id.</p>
<div class="table-section"><table><thead><tr><th>Query Type</th><th>Sample Element Query Filter</th><th>Expected Response</th></tr></thead><tbody>
<tr class="row-even"><td rowspan="2"><p>ElementGroup</td>
<td rowspan="2"><p>ânameâ: âTower Blueprints.rvtâ, âcreatedByâ: â<a class="reference external" href="mailto:first.last%40autodesk.com">first<span>.</span>last<span>@</span>autodesk<span>.</span>com</a>â</td>
<td rowspan="2"><p>Returns elementGroups with name âTower Blueprints.rvtâ and</p>
<p>created by the user with email â<a class="reference external" href="mailto:first.last%40autodesk.com">first<span>.</span>last<span>@</span>autodesk<span>.</span>com</a>â</p>
</td>
</tr>
<tr class="row-odd"></tr>
<tr class="row-even"><td rowspan="2"><p>Element</td>
<td rowspan="2"><p>ânameâ:  âHVAC Feedâ, âpropertiesâ: [{ ânameâ: âFamily Nameâ, âvalueâ: âLinear - 3/32" Trebuchet MSâ },</p>
<p>{ âidâ: âautodesk.revit.parameter:parameter.elementContext-1.0.0â, âvalueâ: âTypeâ}]</p>
</td>
<td rowspan="2"><p>Returns elements with name âHVAC Feedâ,</p>
<p>part of the âLinear - 3/32" Trebuchet MSâ family, and are types</p>
</td>
</tr>
<tr class="row-odd"></tr>
</tbody></table></div>
<p>The convenience fields can be used alongside RSQL to perform more powerful queries. (To see how the use the query field, refer to <a class="reference external" href="en/docs/aecdatamodel/v1/developers_guide/advanced-filtering/">Advanced Filtering Capabilities RSQL</a>).</p>
<div class="table-section"><table><thead><tr><th>Query Type</th><th>Sample Element Query Filter</th><th>Expected Response</th></tr></thead><tbody>
<tr class="row-even"><td rowspan="2"><p>Element</td>
<td rowspan="2"><p>ânameâ: âMiddle Flooringâ, âqueryâ: âproperty.name.Length &gt;= 2.0â</td>
<td rowspan="2"><p>Returns elements with name âMiddle Flooringâ and property âLengthâ having</p>
<blockquote>
<div><p>values greater than or equal to 2.0</p>
</div></blockquote>
</td>
</tr>
<tr class="row-odd"></tr>
</tbody></table></div>
</section>
<section id="matching-multiple-values">
<h1>Matching Multiple Values</h1>
<p>When multiple values for a single field are provided, the OR operator will be used to compare within the same field. This is useful when there are multiple acceptable values for a field. In these cases, provide a [String] as params instead of a single String.</p>
<div class="table-section"><table><thead><tr><th>Query Type</th><th>Sample Element Query Filter</th><th>Expected Response</th></tr></thead><tbody>
<tr class="row-even"><td rowspan="2"><p>ElementGroup</td>
<td rowspan="2"><p>âcreatedByâ: [â<a class="reference external" href="mailto:first.last%40autodesk.com">first<span>.</span>last<span>@</span>autodesk<span>.</span>com</a>â, â<a class="reference external" href="mailto:test%40autodesk.com">test<span>@</span>autodesk<span>.</span>com</a>â]</td>
<td rowspan="2"><p>Returns elementGroups created by the user with email â<a class="reference external" href="mailto:first.last%40autodesk.com">first<span>.</span>last<span>@</span>autodesk<span>.</span>com</a>ââ or</p>
<p>with email â<a class="reference external" href="mailto:test%40autodesk.com">test<span>@</span>autodesk<span>.</span>com</a>â</p>
</td>
</tr>
<tr class="row-odd"></tr>
<tr class="row-even"><td rowspan="2"><p>Element</td>
<td rowspan="2"><p>âcreatedByâ: [â<a class="reference external" href="mailto:john.doer%40autodesk.com">john<span>.</span>doer<span>@</span>autodesk<span>.</span>com</a>â, â<a class="reference external" href="mailto:test%40autodesk.com">test<span>@</span>autodesk<span>.</span>com</a>â],</p>
<p>âlastModifiedByâ: â<a class="reference external" href="mailto:john.doer%40autodesk.com">john<span>.</span>doer<span>@</span>autodesk<span>.</span>com</a>â</p>
</td>
<td rowspan="2"><p>Returns elements created by the user with email â<a class="reference external" href="mailto:test%40autodesk.com">test<span>@</span>autodesk<span>.</span>com</a>ââ or with email</p>
<p>â<a class="reference external" href="mailto:test%40autodesk.com">test<span>@</span>autodesk<span>.</span>com</a>â, and last modified by the user with email â<a class="reference external" href="mailto:first.last%40autodesk.com">first<span>.</span>last<span>@</span>autodesk<span>.</span>com</a>â</p>
</td>
</tr>
<tr class="row-odd"></tr>
</tbody></table></div>
<p><strong>NOTE:</strong> all String fields can accept a [String] instead, with the exception of property name, property id, reference name, and valueWithComparator value (see Compound Filters section). The nameWithComparator field can accept an array of name-comparator pairs as well, with each pair considered to be within the same field.</p>
</section>
<section id="standard-filtering-equivalent-of-rsql">
<h1>Standard Filtering Equivalent of RSQL</h1>
<p>For reference, the following are the convenience field equivalents of some common RSQL filters:</p>
<div class="table-section"><table><thead><tr><th>RSQL Filter</th><th>Standard Field Filter</th></tr></thead><tbody>
<tr class="row-even"><td>âmetadata.name==xâ</td>
<td>ânameâ: âxâ</td>
</tr>
<tr class="row-odd"><td>âmetadata.fileUrn==xâ</td>
<td>âfileUrnâ: âxâ</td>
</tr>
<tr class="row-even"><td>âmetadata.createdBy.email==xâ</td>
<td>âcreatedByâ: âxâ</td>
</tr>
<tr class="row-odd"><td>âmetadata.lastModifiedBy.email==xâ</td>
<td>âlastModifiedByâ: âxâ</td>
</tr>
<tr class="row-even"><td>âmetadata.elementId==xâ</td>
<td>âelementIdâ: âxâ</td>
</tr>
<tr class="row-odd"><td>âproperty.name.&lt;y&gt;==xâ</td>
<td>âpropertiesâ: [{ ânameâ: âyâ, âvalueâ: âxâ }]</td>
</tr>
<tr class="row-even"><td>âproperty.id.&lt;y&gt;==xâ</td>
<td>âpropertiesâ: [{ âidâ: âyâ, âvalueâ: âxâ }]</td>
</tr>
<tr class="row-odd"><td>âreference.&lt;y&gt;==xâ</td>
<td>âreferencesâ: [{ ânameâ: âyâ, âreferenceIdâ: âxâ }]</td>
</tr>
</tbody></table></div>
</section>
<section id="sample-queries">
<h1>Sample Queries</h1>
<p><strong>Querying for all elements that contain the word Pipes in their name:</strong></p>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "nameWithComparator": {"name": "Pipes", "comparator": "CONTAINS"}
    ...
}
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Querying all elements that have the following criteria:</strong></p>
<ul class="simple">
<li>Named 2.5" x 5" rectangular (Orange)</li>
<li>Are instances. This example uses the property id (autodesk.revit.parameter:parameter.elementContext-1.0.0), but the property name can be supplied instead</li>
<li>Are part of the Rectangular Mullion family. The example uses the property name (Family Name), but the property id can be supplied instead</li>
<li>Have a âTypeâ reference with the element with id YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ351LW5jRFM3Z1E2R2hwQjNyZ1pYS2VRX2UzPLIz</li>
<li>Were created by user <a class="reference external" href="mailto:first.last%40autodesk.com">first<span>.</span>last<span>@</span>autodesk<span>.</span>com</a></li>
</ul>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {
        "name": "2.5\" x 5\" rectangular (Orange)"
        "properties": [
            { "name": "Family Name", "value": "Rectangular Mullion" }
            { "id": "autodesk.revit.parameter:parameter.elementContext-1.0.0", "value": "Instance" }
        ]
        "references": { "name": "Type", "referencedId": "YWVjZX5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ351LW5jRFM3Z1E2R2hwQjNyZ1pYS2VRX2UzPLIz" }
        "createdBy": "first.last@autodesk.com"
    },
    ...
}
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="special-considerations-for-elementgroup-filters">
<h1>Special Considerations for ElementGroup Filters</h1>
<section id="fileurn">
<a href="#fileurn"><h2>fileUrn:</h2></a>
<p>This filter can only be used by itself and not be used in combination with any other filter.</p>
<p><strong>Accepted Sample Query:</strong></p>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "fileUrn": ["urn:adsk.wipstg:dm.lineage:u-ncDS7gX3ZhpB3rgZXKeQ", "urn:adsk.wipstg:dm.lineage:R8YVGN61QDaLElL0YSfkKg"]
    ...
}
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Rejected Sample Query:</strong></p>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "fileUrn": "urn:adsk.wipstg:dm.lineage:u-ncDS7gX3ZhpB3rgZXKeQ",
        "createdBy": "first.last@autodesk.com"
    ...
}
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="name">
<a href="#name"><h2>name:</h2></a>
<p>This filter can only be used with one value and can not support multiple values.</p>
<p><strong>Accepted Sample Query:</strong></p>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "name": "Snowdon Towers East.rvt",
        "createdBy": "first.last@autodesk.com"
    ...
}
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Rejected Sample Query:</strong></p>
<div class="highlight-graphql notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
    ...,
    "filter": {

        "name": ["Snowdon Towers East.rvt", "Snowdon Towers West.rvt"]
    ...
}
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
</section>


            <div class="clearer"></div>
          </div>