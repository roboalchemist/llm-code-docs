# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/xml-input-stream-stax/element-blocks-example.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/xml-input-stream-stax/element-blocks-example.md

# Element blocks example

This example parses the `XML Input Stream (StAX) Test 2 - Element Blocks.xml` file which has two main sample data blocks: Analyzer Lists and Products. The data blocks are separated by splitting the parent XML path to levels using Switch / Case steps. This separation could also be performed by the **string contains** option of the Switch / Case step or by using other steps. In more complex processing, you should use mappings (sub-transformations) for the different data blocks so they are clearly represented.

Here is the XML sample with different element blocks:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ProductInformation ExportTime="2010-11-23 23:56:40"
    ExportContext="german" ContextID="german" WorkspaceID="Test" id="1"
    parent="0">
    <AnalyzerResult>
        <AnalyzerLists>
            <AnalyzerList name="items.added">
                <AnalyzerElement ItemID="product?id=123456"
                    ProductID="123456" />
                <AnalyzerElement ItemID="product?id=789"
                    ProductID="789" />
            </AnalyzerList>
            <AnalyzerList name="items.deleted">
                <AnalyzerElement ItemID="product?id=111111"
                    ProductID="111111" />
                <AnalyzerElement ItemID="product?id=222222"
                    ProductID="222222" />
            </AnalyzerList>
            <AnalyzerList name="items.dummy_test">
                <AnalyzerElement ItemID="product?id=test1"
                    ProductID="test1" />
                <AnalyzerElement ItemID="product?id=test2"
                    ProductID="test2" />
            </AnalyzerList>
        </AnalyzerLists>
        <AnalyzerDummyTest>
            <AnalyzerDummyTest name="Dummy not processed" />
        </AnalyzerDummyTest>
    </AnalyzerResult>
    <Products>
        <Product id="123456" name="Product A">
            <MetaData>
                <Value AttributeID="AttrA">false</Value>
                <Value AttributeID="AttrB">true</Value>
                <Value AttributeID="AttrShortName">
                    Product A Short Name
                </Value>
                <Value AttributeID="AttrLongName">
                    Product A Long Name
                </Value>
            </MetaData>
        </Product>
        <Product id="789" name="Product B">
            <MetaData>
                <Value AttributeID="AttrA">true</Value>
                <Value AttributeID="AttrB">false</Value>
                <Value AttributeID="AttrShortName">
                    Product B Short Name
                </Value>
                <Value AttributeID="AttrLongName">
                    Product B Long Name
                </Value>
            </MetaData>
        </Product>
    </Products>
</ProductInformation>
```

A preview of the step looks like the image below, depending on the selected fields:

![Step preview](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-1cf6359c373ef6c934a4f7af7ca58175595e2c17%2FXML_StAX_StepPreview.png?alt=media)

Note that you can see the original streaming information, elements, and attributes from the XML file, and other helpful fields like the **element level**.

The transformation looks like the image below:

![Example transformation](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d86378c18eaea8327fd4a0ddcb0606e5bb97a453%2FXML_StAX_Transform.png?alt=media)

The result for the Analyzer List block looks like this:

![Analyzer lists results](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6bf831203774ab5f98923c6b6c5766342b1b579a%2FXML_StAX_AnalyzerLists.png?alt=media)

The result for the Products block (split into two separate data streams for the end system) looks like the image below:

![Products results](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-7370e631fa49dd368766f00582ad1cb692066167%2FXML_StAX_ProductsBlock.png?alt=media)
