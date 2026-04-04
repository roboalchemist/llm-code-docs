# Source: https://screenshotone.com/docs/guides/how-to-translate-and-render-a-website-as-a-screenshot/

# How to translate and render a website as a screenshot

It is possible to translate and take a screenshot of the translated website with ScreenshotOne because the API supports scripts via the `scripts` option.

You can use any translation API of your choice. But as an example, in this guide, I will go with Google Translate API.

## Get your Google Translate API key

To get your Google API key:

1. Go to [the API credentials page in Google Cloud Platform](https://console.cloud.google.com/apis/credentials).
2. Generate your API key and make sure you restrict it to using only for Google Translate.
3. Make sure you set budgets, and notifications, and follow other [best practices](https://cloud.google.com/blog/products/ai-machine-learning/four-best-practices-for-translating-your-website) for Google Translate.

## Write a script to translate your websites

You need to write a script that efficiently will check all text nodes on the website, batch them, and send requests efficiently to save your costs.

:::danger
Please, make sure to optimize the script for your use case and that it doesn't overuse your quota. It is an example script and ScreenshotOne is not responsible for you using it and causing any damage to your business by the script. Use it at your own risk.
:::

Here is an example script you can try and use as a basis, but I highly recommend writing yours for production and making sure it has retries and other necessary logic:

```javascript
const translateTextAsync = async (texts, targetLang, apiKey) => {
    const url = `https://translation.googleapis.com/language/translate/v2?key=${apiKey}`;
    const data = {
        q: texts,
        target: targetLang,
    };

    const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });

    if (!response.ok) throw new Error("Network response was not ok.");

    const json = await response.json();
    return json.data.translations.map((t) => t.translatedText);
};

const isVisible = (element) => {
    return element.offsetWidth > 0 && element.offsetHeight > 0;
};

const shouldTranslate = (node) => {
    return (
        node.nodeType === Node.TEXT_NODE &&
        node.nodeValue.trim() &&
        isVisible(node.parentElement) &&
        !isDescendantOf(node, ["script", "code"])
    );
};

const isDescendantOf = (node, tagNames) => {
    let parent = node.parentElement;
    while (parent && parent !== document.body) {
        if (tagNames.includes(parent.tagName.toLowerCase())) {
            return true;
        }
        parent = parent.parentElement;
    }
    return false;
};

const batchTranslate = async (nodes, targetLang, apiKey) => {
    let batch = [];
    let totalLength = 0;
    const results = [];

    for (const node of nodes) {
        const text = node.nodeValue.trim();
        if (text.length + totalLength > 5000 || batch.length >= 128) {
            // Translate current batch
            const translations = await translateTextAsync(
                batch,
                targetLang,
                apiKey
            );
            translations.forEach((translatedText, index) => {
                results.push({ node: nodes[index], translatedText });
            });

            // Reset for next batch
            batch = [text];
            totalLength = text.length;
        } else {
            batch.push(text);
            totalLength += text.length;
        }
    }

    // Translate remaining batch
    if (batch.length > 0) {
        const translations = await translateTextAsync(
            batch,
            targetLang,
            apiKey
        );
        translations.forEach((translatedText, index) => {
            results.push({
                node: nodes[nodes.length - batch.length + index],
                translatedText,
            });
        });
    }

    return results;
};

const translatePageContent = async (element, targetLang, apiKey) => {
    const textNodes = [];
    const walker = document.createTreeWalker(
        element,
        NodeFilter.SHOW_TEXT,
        {
            acceptNode: (node) => {
                return shouldTranslate(node)
                    ? NodeFilter.FILTER_ACCEPT
                    : NodeFilter.FILTER_REJECT;
            },
        },
        false
    );

    let node;
    while ((node = walker.nextNode())) {
        textNodes.push(node);
    }

    const translations = await batchTranslate(textNodes, targetLang, apiKey);
    translations.forEach(({ node, translatedText }) => {
        node.nodeValue = translatedText;
    });
};

// Replace with your actual API key
const apiKey = "<your API key>";
// Target language code (e.g., 'es' for Spanish)
const targetLang = "es";

translatePageContent(document.body, targetLang, apiKey)
    .then(() => console.log("Translation completed"))
    .catch((error) => console.error("Translation error:", error));
```

## Rendered translated websites

Once you have a working script, make sure you URL-encode it and then send it to ScreenshotOne when rendering a screenshot. You can use either POST or GET requests.

But in this example, I will share with you a GET request example:

```
https://api.screenshotone.com/take?access_key=<your API key>&url=https://example.com&scripts=<URL-encoded script>&delay=10
```

You can see the example.com website rendered in the Spanish language:

![The example.com website rendered in the Spanish language](example.com.spanish.jpeg)

I hope the guide helps you translate and render any HTML or website content, and have a nice day!