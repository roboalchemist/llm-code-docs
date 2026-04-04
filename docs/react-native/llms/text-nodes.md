# Source: https://reactnative.dev/docs/text-nodes.md

# Text nodes

Text nodes represent raw text content on the tree (similar to [`Text`](https://developer.mozilla.org/en-US/docs/Web/API/Text) nodes on Web). They are not directly accessible via `refs`, but can be accessed using methods like [`childNodes`](https://developer.mozilla.org/en-US/docs/Web/API/Node/childNodes) on element refs.

***

## Reference[​](#reference "Direct link to Reference")

### Web-compatible API[​](#web-compatible-api "Direct link to Web-compatible API")

From [`CharacterData`](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData):

* Properties

  <!-- -->

  * [`data`](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/data)
  * [`length`](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/length)
  * [`nextElementSibling`](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/nextElementSibling)
  * [`previousElementSibling`](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/previousElementSibling)

* Methods
  <!-- -->
  * [`substringData()`](https://developer.mozilla.org/en-US/docs/Web/API/CharacterData/substringData)

From [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node):

* Properties

  <!-- -->

  * [`childNodes`](https://developer.mozilla.org/en-US/docs/Web/API/Node/childNodes)
  * [`firstChild`](https://developer.mozilla.org/en-US/docs/Web/API/Node/firstChild)
  * [`isConnected`](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected)
  * [`lastChild`](https://developer.mozilla.org/en-US/docs/Web/API/Node/lastChild)
  * [`nextSibling`](https://developer.mozilla.org/en-US/docs/Web/API/Node/nextSibling)
  * [`nodeName`](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeName)
  * [`nodeType`](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeType)
  * [`nodeValue`](https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeValue)
  * [`ownerDocument`](https://developer.mozilla.org/en-US/docs/Web/API/Node/ownerDocument)
    * ℹ️ Will return the [document instance](/docs/next/document-instances) where this component was rendered.
  * [`parentElement`](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentElement)
  * [`parentNode`](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentNode)
  * [`previousSibling`](https://developer.mozilla.org/en-US/docs/Web/API/Node/previousSibling)
  * [`textContent`](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent)

* Methods

  <!-- -->

  * [`compareDocumentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/compareDocumentPosition)
  * [`contains()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/contains)
  * [`getRootNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/getRootNode)
    * ℹ️ Will return a reference to itself if the component is not mounted.
  * [`hasChildNodes()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/hasChildNodes)
