# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/construct.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="api-constructs">
<h1>API Constructs</h1>
<img alt="../../../_images/construct01.png" src="../../../_images/construct01.png">
<p>This section defines important data constructs that you will come across in AEC Data Model API:</p>
<ul class="simple">
<li><strong>ElementGroup</strong>: A ElementGroup is a part of an AEC project that contains elements. Note that âModelâ or âDesignâ is sometimes used interchangeably with âElementGroupâ.</li>
<li><strong>Elements</strong>: An Element is a building block of elementGroup data. It represents an individual piece of an elementGroup such as a wall, window, or door without enforcing a rigid definition. The absence of a rigid definition allows the Element to be flexible to adapt to the different requirements of an elementGroup, now and in the future. The data contained in an Element gives it context by using Classification, Property, and Property Definition.</li>
<li><strong>Reference Property</strong>: A reference property describes the relationship between elements.</li>
<li><strong>Property</strong>: A Property is a well-defined granular piece of data that describes the Element. For example: Revit parameters and their values like area, volume, length, etc.</li>
<li><strong>Property Definition</strong>: A Property Definition provides detailed information about a Property. It contains metadata that gives context to the Property. For example: Unit, type, etc.</li>
</ul>
</section>


            <div class="clearer"></div>
          </div>