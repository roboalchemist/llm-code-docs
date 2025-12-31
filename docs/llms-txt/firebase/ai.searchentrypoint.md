# Source: https://firebase.google.com/docs/reference/js/ai.searchentrypoint.md.txt

# SearchEntrypoint interface

Google search entry point.

**Signature:**  

    export interface SearchEntrypoint 

## Properties

|                                                        Property                                                         |  Type  |                                                                                                                                                                                                           Description                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [renderedContent](https://firebase.google.com/docs/reference/js/ai.searchentrypoint.md#searchentrypointrenderedcontent) | string | HTML/CSS snippet that must be embedded in a web page. The snippet is designed to avoid undesired interaction with the rest of the page's CSS.To ensure proper rendering and prevent CSS conflicts, it is recommended to encapsulate this `renderedContent` within a shadow DOM when embedding it into a webpage. See [MDN: Using shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM). |

## SearchEntrypoint.renderedContent

HTML/CSS snippet that must be embedded in a web page. The snippet is designed to avoid undesired interaction with the rest of the page's CSS.

To ensure proper rendering and prevent CSS conflicts, it is recommended to encapsulate this `renderedContent` within a shadow DOM when embedding it into a webpage. See [MDN: Using shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM).

**Signature:**  

    renderedContent?: string;

### Example

    const container = document.createElement('div');
    document.body.appendChild(container);
    container.attachShadow({ mode: 'open' }).innerHTML = renderedContent;