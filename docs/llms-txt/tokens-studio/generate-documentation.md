# Source: https://docs.tokens.studio/figma/generate-documentation.md

# Generate documentation

## Generate documentation

Generating a documentation is a feature that requires a Pro licenseDocumenting tokens for your consumers can be a time-consuming task. We've added the ability to generate a living documentation sheet, with tokens applied so the applied values change whenever the token value itself changes.

### How to Use

1. **Access the feature:** Navigate to the "Tools" menu in the plugin's footer when on the Tokens tab. Select "Generate documentation".
2. **Configure your settings:**
   * **Token set (required):** Choose "All" or select an individual token set. You can type to search for your set name. *Note: "All" might take a while, depending on the amount of tokens you have.*
   * **Token name starts with:** An optional string filter. If entered, the plugin only generates tokens that begin with this name.
   * **Regex Mode:** You can enable Regex mode by clicking the ⁠\* icon inside the input. This allows for advanced filtering, such as ⁠(color|font).\* to generate documentation for both groups at once.
   * **Apply active theme values:** On by default. This configures whether the plugin should automatically apply the currently selected theme values after generating the frames. If on, tokens will appear with their resolved values immediately. You might want to turn this off if you intend to apply a different theme config later.

{% hint style="warning" %}
Make sure you do not have a layer selected, as otherwise we will attempt to use this layer as a template (see below)
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FVxo3fEZz39mun3G8lpln%2Fgenerate-doc.png?alt=media&#x26;token=2ea6710c-1bf9-415d-8455-6baba7df9c52" alt=""><figcaption></figcaption></figure>

### Different modes of operation <a href="#different-modes-of-operation" id="different-modes-of-operation"></a>

There's two ways how you can use this, one is by not having a layer selected, and the other mode is by having a layer selected.

1. **No layer selected: Use our pre-defined template -** If you do not have any layer selected, we will use our pre-defined template to generate documentation. Use this if you just want to get started or are happy with what's generated.
2. **With a layer selected: Use this layer as a template -** If you select a Figma layer (Frame) before clicking generate, we will use that layer as your template. This allows you to create your very own documentation style.\
   \
   To make your template dynamic, you must name the layers inside your frame with special **double underscore (⁠\_\_)** prefixes. The plugin looks for these names to know where to insert data or apply styles.

### Layer Naming Reference

**Documentation Tokens (Text Layers Only)**

Use these names on Text Layers to display metadata as text. The plugin will replace the layer's text content.

* `__tokenName`: Displays the token name (e.g., ⁠**color.primary.500**)
* ⁠`__value`: Displays the final resolved value (e.g., &#x2060;**#3366CC** or ⁠**16px**).
* ⁠`__tokenValue`: Displays the raw value, including aliases or math (e.g., **⁠{brand.blue}** or **⁠{size.base} \* 2**).
* ⁠`__description`: Displays the token description text.

**Property Tokens (Visual Properties)**

Use these names on Any Layer (Rectangles, Frames, Text) to apply the token's value to the layer's visual properties.

* **Color:** ⁠
  * `__fill`
  * ⁠`__border`
  * `⁠__borderColor`
* **Dimensions:** ⁠
  * `__width`
  * `__height`
  * `__sizing`
  * `⁠__minWidth`
  * `⁠__maxWidth`
  * `⁠__minHeight`
  * `⁠__maxHeight`
* **Spacing:**
  * `__spacing`
  * `⁠__itemSpacing`
  * `⁠__verticalPadding`
  * `⁠__horizontalPadding`
  * `⁠__paddingTop`
  * `⁠__paddingRight`
  * `⁠__paddingBottom`
  * `⁠__paddingLeft`
* **Border:** ⁠
  * `__borderRadius⁠`
  * `__borderRadiusTopLeft (etc.)`
  * `__borderWidth`
  * `⁠__borderWidthTop (etc.)`
* **Typography:**
  * `__typography` (applies full style)
  * ⁠`__fontFamilies`
  * `⁠__fontWeights`
  * `⁠__fontSizes`
  * `⁠__lineHeights`
  * `⁠__letterSpacing`
  * `⁠__paragraphSpacing`
  * `⁠__textCase`
  * `⁠__textDecoration`
* **Effects:**
  * \_\_boxShadow
  * ⁠\_\_backgroundBlur
  * \_\_opacity
* **Others:**
  * ⁠`__composition`
  * ⁠`__asset`
  * ⁠`__visibility`
  * ⁠`__rotation`
  * `__x`, `⁠__y`
