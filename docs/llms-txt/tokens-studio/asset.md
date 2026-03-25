# Source: https://docs.tokens.studio/manage-tokens/token-types/asset.md

# Asset

## Asset - Token Type

Asset Tokens define the location of assets to style the fill or stroke of a design element as a URL.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FmNWZuSwPaQvfvtsRmtDI%2Ftokens-asset-form-empty-2-01.png?alt=media&#x26;token=ef53c517-cae8-44bc-aa80-f337fa9f7d56" alt=""><figcaption><p>Creating a new Asset Token in the Tokens Studio Plugin for Figma.</p></figcaption></figure>

***

### Design decisions

Asset Tokens define the location of assets that are stored outside of your Design Tool, and when applied to a design element, the asset will fill the layer.

For example, a product photo across several pages on a marketing website.

When it comes time to change your assets, you can update the Asset Token in the Tokens Studio Plugin and the changes will be applied across your entire design system with just a couple of clicks.

***

### Possible values

An Asset Token can reference any URL or path to an asset file, such as:

* URLs pointing to images or icons hosted online.
* Local file paths if working within a local environment.

The image source needs to have its own CORS (Cross-Origin Resource Sharing) validation.

* Some websites already have that implemented (e.g. Unsplash).
* You can put your images behind a CORS proxy if needed.

→ More information on CORS can be found [here](https://medium.com/nodejsmadeeasy/a-simple-cors-proxy-for-javascript-applications-9b36a8d39c51).

### Values that reference another Token

When trying to reference another Token as the Value for an Asset Token, you will see Tokens in the dropdown list that are:

* Living in Token Sets that are currently active.
  * In the left menu on the plugin's Tokens page, **a checkmark is visible next to the Token Set name.**
* Token Type is compatible:
  * The same = `asset`

However, like all Token Types, you can "force" a reference by manually entering the Token Name between curly brackets.&#x20;

For example `{token.name.here}`

{% hint style="info" %}
The value will show a broken reference until the originating Token Set is marked as enabled.
{% endhint %}

*Jump to the guide on Token Values with References by selecting the card below to learn more.*

{% content-ref url="../token-values/references" %}
[references](https://docs.tokens.studio/manage-tokens/token-values/references)
{% endcontent-ref %}

***

### Apply Asset Tokens

&#x20;You can apply an Asset Token to fill the background of text, polygonal shape, and frame layers in Figma when the Token is applied.&#x20;

With one or more elements selected in Figma, click on the name of your chosen Asset Token in the Plugin to instantly apply its value.&#x20;

Once a Token has been applied, it will remain attached until you manually remove it.&#x20;

***

### W3C DTCG Token Format

`Asset` is not yet an official Token Type in the W3C DTCG specifications, but there is mention of a 'File' Token Type under consideration ([8.8 Additional Types](https://tr.designtokens.org/format/#additional-types)).

***

### Transforming Tokens

Engineers typically transform Tokens used in code with [Style Dictionary](https://styledictionary.com/), which is tool-agnostic. Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

When transforming **Asset Tokens**, there are **no specific configurations** to be aware of.&#x20;

Running the SD-Transforms pre-processor as part of the generic package will prep your Asset Tokens for Style Dictionary.

→ [SD-Transforms Read-Me Doc, Using the preprocessor](https://github.com/Tokens-studio/sd-transforms/?tab=readme-ov-file#using-the-preprocessor)

***

### Resources

Mentioned in this doc:

* CORS information - [Medium Article, Sandeep - NodejsMadeEasy](https://medium.com/nodejsmadeeasy/a-simple-cors-proxy-for-javascript-applications-9b36a8d39c51)
* SD-Transforms - [Read Me](https://github.com/tokens-studio/sd-transforms#readme)
* Style Dictionary - <https://styledictionary.com/>
* Design Tokens Community Group - [W3C Draft](https://tr.designtokens.org/format/)
* Design Tokens Community Group - [8.8 Additional Token Types](https://tr.designtokens.org/format/#additional-types)

#### Figma resources:

* Design in Figma - [Working with images in Figma](https://www.figma.com/best-practices/working-with-images-in-figma/)
* Design in Figma - [Adjust the properties of an asset](https://help.figma.com/hc/en-us/articles/360041098433-Adjust-the-properties-of-an-image)

#### CSS resources:

* MDN Web Docs - [Images](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_images)

#### Community resources:

* Katie Cooper demo's Asset Tokens during the How to Leverage Tokens Studio to level up your Design System presentation - [YouTube](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_images)

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Token Type Asset](https://github.com/tokens-studio/figma-plugin/labels/token%20type%20asset%20token)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* Asset token enhancements (to include icons) - \[Feature Request]\(# Asset token enhancements)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
