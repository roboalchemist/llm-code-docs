# Source: https://screenshotone.com/docs/guides/emojis/

# How to render screenshots with different emoji styles

It might happen that you need to render screenshots with different emoji styles rather than the default emoji style provided by the ScreenshotOne API.

There are many emoji libraries out there that can help. For example, [emoji-js](https://www.npmjs.com/package/emoji-js) is a popular library that can be used to render emojis in different styles.

:::note
Whatever library you decided to use, or whatever emoji style you decided to use, make sure you do not violate any license of the emoji set you are using.

E.g. if you use [emojis provided by Twitter](https://github.com/twitter/twemoji), you must follow their license requirements.
:::

You can use it to replace emojis in the page with the desired style. E.g. you can replace all emojis with the emojis that look like Twitter emojis:

```js
const stylesheet = document.createElement("link");
stylesheet.href = "https://cdn.jsdelivr.net/npm/emoji-js@3.8.1/lib/emoji.min.css";
stylesheet.rel = "stylesheet";
document.head.appendChild(stylesheet);

const script = document.createElement("script");
script.onload = () => {
    // change to one you are interested in,
    // check the library documentation for the list of available emoji sets
    const img_set = "apple";

    const emoji = new window.EmojiConvertor();

    emoji.img_sets[img_set].path =
        `https://cdn.jsdelivr.net/npm/emoji-datasource-${img_set}@15.1.2/img/${img_set}/64/`;
    emoji.img_sets[img_set].sheet =
        `https://cdn.jsdelivr.net/npm/emoji-datasource-${img_set}@15.1.2/img/${img_set}/sheets/64.png`;
    emoji.img_set = img_set;

    emoji.replace_mode = "img";

    function replaceEmojisInTextNodes(node) {
        if (node.nodeType === Node.TEXT_NODE) {
            if (node.textContent && node.textContent.trim()) {
                const span = document.createElement("span");
                const replaced = emoji.replace_unified(node.textContent);
                span.innerHTML = replaced;

                if (replaced.trim() !== node.textContent.trim()) {
                    const parent = node.parentNode;
                    if (parent) {
                        while (span.firstChild) {
                            parent.insertBefore(span.firstChild, node);
                        }
                        parent.removeChild(node);
                    }
                }
            }
        } else if (node.nodeType === Node.ELEMENT_NODE) {
            if (node.tagName === "SCRIPT" || node.tagName === "STYLE") {
                return;
            }

            const childNodes = Array.from(node.childNodes);
            childNodes.forEach((child) => replaceEmojisInTextNodes(child));
        }
    }

    replaceEmojisInTextNodes(document.body);
};

script.src = "https://cdn.jsdelivr.net/npm/emoji-js@3.8.1/lib/emoji.min.js";
script.crossOrigin = "anonymous";

document.body.appendChild(script);
```

To use this script with the ScreenshotOne API, you can use `scripts` parameter to pass a script that will be executed on the page after it is loaded, and it will be rendered in the screenshot:

```
https://api.screenshotone.com/take?access_key=<your_access_key>&url=<your_url>&scripts=<your_script>
```

Where `<your_script>` is the URL-encoded script above.

E.g. like this:

```
https://api.screenshotone.com/take?access_key=<your_access_key>&url=https://example.com&scripts=const%20stylesheet%20%3D%20document.createElement%28%27link%27%29%3B%0Astylesheet.href%20%3D%20%27https%3A%2F%2Fcdn.jsdelivr.net%2Fnpm%2Femoji-js%403.8.1%2Flib%2Femoji.min.css%27%3B%0Astylesheet.rel%20%3D%20%27stylesheet%27%3B%0Adocument.head.appendChild%28stylesheet%29%3B%0A%0Aconst%20script%20%3D%20document.createElement%28%27script%27%29%3B%0Ascript.onload%20%3D%20%28%29%20%3D%3E%20%7B%0A%20%20%20%20%2F%2F%20change%20to%20one%20you%20are%20interested%20in%2C%20%0A%20%20%20%20%2F%2F%20check%20the%20library%20documentation%20for%20the%20list%20of%20available%20emoji%20sets%0A%20%20%20%20const%20img_set%20%3D%20%27apple%27%3B%0A%0A%20%20%20%20const%20emoji%20%3D%20new%20window.EmojiConvertor%28%29%3B%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20emoji.img_sets%5Bimg_set%5D.path%20%3D%20%60https%3A%2F%2Fcdn.jsdelivr.net%2Fnpm%2Femoji-datasource-%24%7Bimg_set%7D%4015.1.2%2Fimg%2F%24%7Bimg_set%7D%2F64%2F%60%3B%0A%20%20%20%20emoji.img_sets%5Bimg_set%5D.sheet%20%3D%20%60https%3A%2F%2Fcdn.jsdelivr.net%2Fnpm%2Femoji-datasource-%24%7Bimg_set%7D%4015.1.2%2Fimg%2F%24%7Bimg_set%7D%2Fsheets%2F64.png%60%3B%0A%20%20%20%20emoji.img_set%20%3D%20img_set%3B%0A%0A%20%20%20%20emoji.replace_mode%20%3D%20%27img%27%3B%0A%0A%20%20%20%20function%20replaceEmojisInTextNodes%28node%29%20%7B%0A%20%20%20%20%20%20%20%20if%20%28node.nodeType%20%3D%3D%3D%20Node.TEXT_NODE%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20%28node.textContent%20%26%26%20node.textContent.trim%28%29%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20const%20span%20%3D%20document.createElement%28%27span%27%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20const%20replaced%20%3D%20emoji.replace_unified%28node.textContent%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20span.innerHTML%20%3D%20replaced%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20%28replaced.trim%28%29%20%21%3D%3D%20node.textContent.trim%28%29%29%20%7B%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20const%20parent%20%3D%20node.parentNode%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20%28parent%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20while%20%28span.firstChild%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20parent.insertBefore%28span.firstChild%2C%20node%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20parent.removeChild%28node%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%20else%20if%20%28node.nodeType%20%3D%3D%3D%20Node.ELEMENT_NODE%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20%28node.tagName%20%3D%3D%3D%20%27SCRIPT%27%20%7C%7C%20node.tagName%20%3D%3D%3D%20%27STYLE%27%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20const%20childNodes%20%3D%20Array.from%28node.childNodes%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20childNodes.forEach%28child%20%3D%3E%20replaceEmojisInTextNodes%28child%29%29%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20replaceEmojisInTextNodes%28document.body%29%3B%0A%7D%3B%0A%0Ascript.src%20%3D%20%27https%3A%2F%2Fcdn.jsdelivr.net%2Fnpm%2Femoji-js%403.8.1%2Flib%2Femoji.min.js%27%3B%0Ascript.crossOrigin%20%3D%20%27anonymous%27%3B%0A%0Adocument.body.appendChild%28script%29%3B
```

In case you have any issues, do not hesitate to reach out to us at support@screenshotone.com.