# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/xml-output-cp/options-xml-output-step/content-tab-xml-output-step-options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/xml-output-cp/options-xml-output-step/content-tab-xml-output-step-options.md

# Content tab

![Content tab in the PDI XML Output transformation step properties](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-87da9fe2bee3aa85b896e4261544e036e5835b7d%2FssPentahoXMLOutputContentTab.png?alt=media)

Use the **Content** tab to include the following options for the output XML file.

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Option</td><td>Description</td></tr><tr><td><strong>Zipped</strong></td><td>Select this option if you want the XML file to be stored in a ZIP archive.</td></tr><tr><td><strong>Encoding</strong></td><td>Specify the file encoding to use. Leave blank to use the default encoding on your system. To use Unicode, specify <code>UTF-8</code> or <code>UTF-16</code>. On first use, PDI searches your system for available encodings. The encoding specified is noted in the header of the output XML file.</td></tr><tr><td><strong>Namespace</strong></td><td>Specify the default namespace, which is a collection of names that can be used for uniquely named elements and attributes. A runtime check occurs that ensures the URI of the default namespace is a valid URI. A runtime error stops the transformation and logs an error if the URI is invalid.</td></tr><tr><td><strong>Parent XML element</strong></td><td>Select the name of the root element in the XML document.</td></tr><tr><td><strong>Row XML element</strong></td><td>Select the name of the row element to use in the XML document.</td></tr><tr><td><strong>Split every ... rows</strong></td><td>Specify the maximum number of rows of data to generate to a single XML file before another file is created.</td></tr><tr><td><strong>Omit null values from XML output</strong></td><td><p>Select this option to exclude elements containing null values from the output XML file. Clear this option to include elements containing null values in the output XML file. You can specify another value to replace null with the <strong>Null</strong> field in the <strong>Fields</strong> tab.For example, you may have the <code>&#x3C;data1></code> and <code>&#x3C;data2></code> elements as part of <code>&#x3C;Rows></code>, and <code>&#x3C;data2></code> contains a null value. If you select <strong>Omit null values from XML output</strong>, then the <code>&#x3C;data2></code> element does not appear in <code>&#x3C;Rows></code> in the output XML file, as shown in the following sample output:</p><pre class="language-xml"><code class="lang-xml">&#x3C;?xml version='1.0' encoding='UTF-8'?>
&#x3C;Rows xmlns="namespace&#x26;">
&#x3C;Row>&#x3C;data1>ABCD&#x3C;/data1> &#x3C;/Row>
&#x3C;/Rows>

</code></pre><p>If you clear <strong>Omit null values from XML output</strong>, then the <code>\<data2></code> element does appear in <code>\<Rows></code> in the output XML file, as shown in the following sample output:</p><pre class="language-xml"><code class="lang-xml">\<?xml version='1.0' encoding='UTF-8'?>
\<Rows xmlns="namespace&">
\<Row>\<data1>ABCD\</data1> \<data2/>\</Row>
\</Rows>

</code></pre></td></tr></tbody></table>
