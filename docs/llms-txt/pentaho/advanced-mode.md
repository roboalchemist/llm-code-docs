# Source: https://docs.pentaho.com/pba/semantic-model-editor/advanced-mode.md

# Advanced mode

Advanced mode is intended for expert users who are familiar with Mondrian XML syntax and want to create or modify semantic models by directly editing the underlying XML.

In Advanced mode, the Semantic Model Editor continuously validates XML content against the Mondrian XML Schema Definition (XSD). Any invalid XML is underlined in red. Validation errors may result from syntax issues, missing required elements or attributes, or incorrect element ordering as defined by the Mondrian schema. The model cannot be saved until all validation errors are resolved. To view details about a specific error, hover over the underlined XML to display a tooltip with the validation message.

{% hint style="info" %}
**Note:** If you edit a semantic model externally in Pentaho Analyzer and create a calculated measure for the semantic model, Pentaho Analyzer saves the calculated measure in the model's XML as a read-only structure. Read-only structures are visible in Semantic Model Editor but cannot be edited or deleted. In Advanced mode, Semantic Model Editor displays a read-only structure as gray text with grey highlighting.
{% endhint %}

## Advance mode functionality

<table><thead><tr><th width="158.888916015625"></th><th>Description</th></tr></thead><tbody><tr><td>Auto format</td><td>Clean ups XML by removing unnecessary spaces, tabs, and empty lines, and by applying consistent indentation.<br>To auto format XML, click <strong>Auto Format</strong>.</td></tr><tr><td>Find and replace</td><td><p>Enables you to find and replace XML in the editor.</p><p></p><p>To open the find and replace toolbar, place your cursor inside the editor and select <strong>Ctrl</strong> + <strong>F</strong>. </p><p></p><p>To switch between find-only and find and replace modes, expand and collapse the search box. </p></td></tr><tr><td>Auto complete</td><td><p>Suggests valid elements and attributes based on your current position in the schema. </p><p></p><p>To activate autocomplete, place your cursor inside the editor and select <strong>Ctrl</strong>+<strong>Space</strong> . </p><p></p><p>Suggestions are provided in the following scenarios.</p><ul><li><strong>Element entry</strong>: For the current parent, autocomplete suggests valid child elements. If the name is partially entered, suggestions are filtered to match the input.</li><li><strong>Attribute entry</strong>: For known elements, autocomplete suggests valid attributes for the element. Attributes already in use are excluded from suggestions because duplicate attributes are not allowed.</li><li><strong>Enumerated values</strong>: When the value of an attribute is defined as an enumeration, autocomplete suggests valid options.</li></ul></td></tr></tbody></table>
