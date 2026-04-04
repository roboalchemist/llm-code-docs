# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/custom-content-security-policy-settings.md

# Custom Content Security Policy Settings

You can configure your company's CSP directives controlling resource loading and enhanced security via the custom content security policy settings in Builder.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FU2RafyzGR37GiBhVAEvb%2Fimage.png?alt=media&#x26;token=d89ccf5b-5830-4956-925e-b3e80c9868df" alt=""><figcaption></figcaption></figure>

The Content Security Policy section can be found in the Settings area of Builder.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1GjbYKZS91Piw9sxYYJX%2Fimage.png?alt=media&#x26;token=11132f0d-cf66-4994-acfe-0eece05b1815" alt=""><figcaption></figcaption></figure>

### Supported CSP Directives

The CSP directives that you can configure are listed below:

| <p><br>default-src</p> | Default policy for loading content such as JavaScript, Images, CSS, Fonts, AJAX requests, Frames, HTML5 Media, and Object resources. |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| connect-src            | Valid sources for XMLHttpRequest, WebSocket, and EventSource connections                                                             |
| font-src               | Valid sources for fonts                                                                                                              |
| frame-src              | Valid sources for nested browsing contexts loading using elements such as \<frame> and \<iframe>                                     |
| img-src                | Valid sources for images                                                                                                             |
| object-src             | Valid sources for \<object>, \<embed>, and \<applet> elements                                                                        |
| script-src             | Valid sources for JavaScript                                                                                                         |
| style-src              | Valid sources for stylesheets                                                                                                        |
| manifest-src           | Valid sources for web app manifests                                                                                                  |
| prefetch-src           | Valid sources for \<link rel='prefetch'> elements                                                                                    |
| worker-src             | Valid sources for Worker, SharedWorker, or ServiceWorker scripts                                                                     |
| media-src              | Valid sources for \<audio> and \<video> elements                                                                                     |

You can add and remove values for each directive whenever you need.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FR4aS59q3aIeWFXrLYeN4%2Fimage.png?alt=media&#x26;token=73628607-b0a6-4854-9f72-3775c3592a4b" alt=""><figcaption></figcaption></figure>

When you have added directive values, you will see a generated CSP header in the Policy Preview field at the foot of the Content Security Policy section.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjyZoV2xTqEEWrDTEU2Eo%2Fimage.png?alt=media&#x26;token=8abb93dc-141b-4d87-96c8-1ac03c2e78ab" alt=""><figcaption></figcaption></figure>
