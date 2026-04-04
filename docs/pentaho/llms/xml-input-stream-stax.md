# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/xml-input-stream-stax.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/xml-input-stream-stax.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/xml-input-stream-stax.md

# XML Input Stream (StAX)

The XML Input Stream (StAX) step reads data from XML files using the Streaming API for the XML (StAX) parser. This step is optimal for quickly processing large and complex data structures. Unlike the [Get Data from XML](http://wiki.pentaho.com/display/EAI/Get+Data+From+XML) step which uses in-memory processing and can require the purging of parts of files, the XML Input Stream (StAX) step moves the processing logic into the transformation. The step itself provides the raw XML data stream together with additional processing information.

This streaming step is recommended when you have limitations with other steps or need to parse XML when:

* You need fast data loads which are independent of the memory regardless of the file size
* You need flexibility in reading various parts of the XML file in different ways, and do not want to repeatedly parse the file.

Because the processing logic of some XML files can be complex, you should have a good knowledge of the existing Kettle steps when using this step.
