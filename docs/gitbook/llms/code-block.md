# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/creating-content/blocks/code-block.md

# Source: https://gitbook.com/docs/documentation/zh/creating-content/blocks/code-block.md

# Source: https://gitbook.com/docs/documentation/fr/creating-content/blocks/code-block.md

# Source: https://gitbook.com/docs/creating-content/blocks/code-block.md

# Code blocks

You can add code to your GitBook pages using code blocks.

When you add a code block, you can choose to [set the syntax](#set-syntax...), [show line numbers](#with-line-numbers), [show a caption](#with-caption), and [wrap the lines](#wrap-code). It’s also easy to [copy the contents of a code block to the clipboard](#copying-the-code), so you can use it elsewhere

A code block may be useful for:

* Sharing configurations
* Adding code snippets
* Sharing code files
* Showing usage examples of command line utilities
* Showing how to call API endpoints
* And much more!

### Example of a code block

{% code title="index.js" overflow="wrap" lineNumbers="true" %}

```javascript
‌import * as React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, window.document.getElementById('root'));
```

{% endcode %}

You can also combine code blocks with a [tabs block](https://gitbook.com/docs/creating-content/blocks/tabs) to offer the same code example in multiple different languages:

{% tabs %}
{% tab title="JavaScript" %}

```javascript
let greeting = function (name) {
  console.log(`Hello, ${name}!`);
};
greeting("Anna");
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
greeting = lambda {|name| puts "Hello, #{name}!"}
greeting.("Anna")
```

{% endtab %}

{% tab title="Elixir" %}

```elixir
greeting = fn name -> IO.puts("Hello, #{name}!") end
greeting.("Anna")
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
You can make code blocks [span the full width of your window](https://gitbook.com/docs/creating-content/blocks/..#full-width-blocks) by clicking on the **Options menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjYRg42UtM4u1pHmJl4Ln%2Fdrag%20-%20dark.svg?alt=media&#x26;token=4c219b2b-37d2-449e-9130-19b6ba3d38d2" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FaS1QvPIBVYwhpFTGcPBN%2Foptions-menu.svg?alt=media&#x26;token=3ee40bbf-f4fb-41fa-aa30-306b559cbe88" alt="The Options menu icon in GitBook"></picture> next to the block and choosing **Full width**.
{% endhint %}

### Code block options <a href="#options" id="options"></a>

When you click on the **Options menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjYRg42UtM4u1pHmJl4Ln%2Fdrag%20-%20dark.svg?alt=media&#x26;token=4c219b2b-37d2-449e-9130-19b6ba3d38d2" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FaS1QvPIBVYwhpFTGcPBN%2Foptions-menu.svg?alt=media&#x26;token=3ee40bbf-f4fb-41fa-aa30-306b559cbe88" alt="The Options menu icon in GitBook"></picture> next to the code block, or the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> in the block itself, you’ll see a number of options you can set.

#### Set syntax… <a href="#set-syntax" id="set-syntax"></a>

You can set the syntax in your code block to any of the supported languages. This will enable syntax highlighting in that language, too.

{% hint style="info" %}
We use [Prism](https://github.com/PrismJS/prism) for syntax highlighting. You can use [Test Drive Prism](https://prismjs.com/test.html#language=markup) to check which languages Prism supports. If you notice a mismatch between GitBook and Prism, there’s a chance we’re a version or two behind. We’ll catch up soon!
{% endhint %}

{% code title="filename.txt" %}

```
// Some code
```

{% endcode %}

#### With line numbers <a href="#with-line-numbers" id="with-line-numbers"></a>

This will toggle line numbers for your code on and off.

Showing line numbers is useful when the code represents the contents of a file as a whole, or when you have long code blocks with lots of lines. Hiding line numbers is useful for snippets, usage instructions for command line or terminal expressions and similar scenarios.

#### With caption

This will toggle a caption that sits at the top of the block, above your lines of code.

The caption is often the name of a file as shown in [our example above](#example-of-a-code-block), but you can also use it as a title, description, or anything else you’d like.

#### Wrap code

This will toggle code wrapping on and off, so long lines of code will wrap to all be visible on the page at once.

Wrapping lines is useful when your code is long and you want to avoid having the viewer scroll back and forth to read it. If you toggle **Wrap code** on, you may also want to show line numbers — this will make it easier to read the code and understand where new lines start.

#### Expandable

This will toggle showing the code in full (when the toggle is off) or a collapsed window of the code which the user can expand (when the toggle is on).

The collapsed view defaults to showing 10 lines of code with an button to expand to show the full code block. If there are less than 10 lines of code, all the content will be shown.

### Code block actions

As well as the options above, you can also change the language the code block displays, and copy your code instantly.

#### Copy the code <a href="#copying-the-code" id="copying-the-code"></a>

Hover over a code block and a number of icons will appear. Click the middle icon to copy the contents of the code block to your clipboard.

### Representation in Markdown

````markdown
{% code title="index.js" overflow="wrap" lineNumbers="true" %}

```javascript
‌import * as React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, window.document.getElementById('root'));
```

{% endcode %}
````
