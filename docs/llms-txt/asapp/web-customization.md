# Source: https://docs.asapp.com/agent-desk/integrations/web-sdk/web-customization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Customization

Once properly installed and configured, the ASAPP Chat SDK embeds two snippets of HTML markup into your host web page:

* [Chat SDK Badge](#badge "Badge")
* [Chat SDK iframe](#iframe "iframe")

This section details how these elements function. In addition, it describes how to [Customize the Chat UI](#customize-the-chat-ui "Customize the Chat UI"), [Dynamic Styling Configuration](#dynamic-styling-configuration), [Custom Icons](#custom-icons), and [Advanced Configuration Options](#advanced-configuration-options).

## Badge

The ASAPP Chat SDK Badge is the default interface element your customers can use to open or close the ASAPP Chat iframe.

When a user clicks on this element, it will trigger the [ASAPP('Show')](/agent-desk/integrations/web-sdk/web-javascript-api#show "'show'") or [ASAPP('Hide')](/agent-desk/integrations/web-sdk/web-javascript-api#hide"'hide'") APIs.

This toggles the display of the ASAPP Chat SDK iframe.

### Badge Markup

By default. the ASAPP Chat SDK Badge is inserted into your markup as a lightweight `button` element, with a click behavior that toggles the display of the [iframe](#iframe "iframe") element. ASAPP recommends that you use the default badge element so you can take advantage of our latest features as they become available.

However, if you wish to customize the badge, you can do so by either manipulating the CSS associated with the badge, or by hiding/removing the element from your DOM and toggling the display of the iframe using your own custom element. See the [Badge Styling](#asapp-badge-styling "ASAPP Badge Styling") section below for more details on customizing the appearance of the ASAPP Chat SDK Badge.

```html  theme={null}
<button id="asapp-chat-sdk-badge" class="asappChatSDKBadge examplecompany">
  <svg class="icon">...</svg>
  <svg class="icon">...</svg>
</button>
```

### ASAPP Badge Styling

You can customize the ASAPP Chat SDK Badge with CSS using the ID `#asapp-chat-sdk-badge` or classname `.asappChatSDKBadge` selectors. ASAPP recommends that you use [BadgeColor](/agent-desk/integrations/web-sdk/web-app-settings#display "Display").

The following snippet is an example of how you might use these selectors to customize the element to meet your brand needs:

```css  theme={null}
#asapp-chat-sdk-badge {
  background-color: rebeccapurple;
}
#asapp-chat-sdk-badge:focus,
#asapp-chat-sdk-badge:hover,
#asapp-chat-sdk-badge:active {
  -webkit-tap-highlight-color: rgba(102, 51, 153, 0.25);
  background-color: #fff;
}
#asapp-chat-sdk-badge .icon {
  fill: #fff;
}
#asapp-chat-sdk-badge:focus .icon,
#asapp-chat-sdk-badge:hover .icon,
#asapp-chat-sdk-badge:active .icon {
  fill: rebeccapurple;
}
```

### Custom Badge

You can hide the ASAPP Chat SDK Badge and provide your own interface for opening the ASAPP Chat SDK iframe.

* Set [BadgeType](/agent-desk/integrations/web-sdk/web-app-settings#display "Display") to none.
* Call [`ASAPP('show')`](/agent-desk/integrations/web-sdk/web-javascript-api#show "'show'") and/or [`ASAPP('hide')`](/agent-desk/integrations/web-sdk/web-javascript-api#hide "'hide'")  when your custom badge is clicked to open/close the iframe.
* In order to ensure that the Chat SDK is ready, ASAPP recommends to display your custom badge disabled/loading state at first and then utilize [onLoadComplete](/agent-desk/integrations/web-sdk/web-app-settings#onloadcomplete "onLoadComplete") to enable it.

**Example:**

In the code example below, the 'Chat with us' button is not clickable until you enable it using onLoadComplete.

Once enabled, a user can click the button to open the ASAPP SDK iframe.

Custom Button:

```html  theme={null}
<button id="asapp-custom-button" onclick="window.ASAPP(`Show`)" disabled>
  Chat with us
</button>
```

Load config example:

```javascript  theme={null}
<script>
    ASAPP('load', {
                <other configs>…,
                onLoadComplete: shouldDisplayWebChat => {
                    if(shouldDisplayWebChat){
                        document.getElementById('asapp-custom-button').disabled = false;
                    }
                },
 });
</script>
```

## iframe

The ASAPP Chat SDK iframe contains the interface that your customers will use to interact with the ASAPP platform.

The element is populated with ASAPP-provided functionality and styled elements, but the iframe itself is customizable to your brand's needs.

### iframe Markup

The SDK iframe is instantiated as a lightweight `<iframe>` element whose contents are delivered by the ASAPP platform.

ASAPP recommends using the default iframe sizing, positioning, and functionality so you can take advantage of our latest features as they become available.

However, if you wish to customize this element you can do so by applying functionality and styling to the frame itself. See the iframe Styling section below for details on available customizations.

The following code snippet is an example of the ASAPP Chat SDK iframe markup.

```html  theme={null}
<iframe
  id="asapp-chat-sdk-iframe"
  title="Customer Support | Chat Window"
  class="asappChatSDKIFrame"
  frameborder="0"
  src="https://sdk.asapp.com/..."
>
  ...
</iframe>
```

### iframe Styling

You can customize the ASAPP Chat SDK iframe by using the ID `#asapp-chat-sdk-iframe` or classname `.asappChatSDKIFrame` selectors.

The following snippet is an example of how you may want to use these selectors to customize the element to your brand.

```css  theme={null}
@media only screen and (min-width: 415px) {
  #asapp-chat-sdk-iframe {
    box-shadow: 0 2px 12px 0 rgba(35, 6, 60, 0.05), 0 2px 49px 0 rgba(102, 51, 153, 0.25);
  }
}
```

<Note>
  Modifying the sizing or positioning of the iframe is currently not supported.
  Change those properties at your own risk; a moved or resized iframe is not
  guaranteed to work with upcoming releases of the ASAPP platform
</Note>

## Customize the Chat UI

ASAPP will customize the Chat SDK iframe User Interface (UI) in close collaboration with design and business stakeholders. ASAPP will work within your branding guidelines to apply an appropriate color palette, logo, and typeface. There are two particularly technical requirements that we can assess early on to provide a more seamless delivery of requirements:

### 1. Chat Header Logo

The ASAPP SDK Team will embed your logo into the Chat SDK Header. Please provide your logo in the following format:

* SVG format
* Does not exceed 22 pixels in height
* Does not exceed 170 pixels in width
* Should not contain animations
* Should not contain filter effects

If you follow the above guidelines your logo will:

* display at the most optimal size for responsive devices
* sit well within the overall design
* display properly

### 2. Custom Typefaces

Using a custom typeface within the ASAPP Chat SDK requires detailed technical requirements to ensure that the client is performant, caching properly, and displaying the expected fonts. For the best experience, you should provide ASAPP with the following:

* The font should be available in any of the following formats: WOFF2, WOFF, OTF, TTF, and EOT.
* The font should be hosted in the same place that your own site's custom typeface is hosted.
* The same hosted font files should have an `Access-Control-Allow-Origin` that allows `sdk.asapp.com` or `*`.
* The files should have proper cache-control headers as well as GZIP compression. For more information on web font performance enhancements, ASAPP recommends the article: [Web Font Optimization](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/webfont-optimization), published by Google and Ilya Grigorik.
* You acknowledge that you will provide ASAPP with the URLs for each of the hosted font formats for use in a CSS @font-face declaration, hosted on sdk.asapp.com.
* If your font becomes unavailable for display, ASAPP will default to using [Lato](https://fonts.google.com/specimen/Lato), then Arial, Helvetica, or a default sans-serif font.

## Dynamic Styling Configuration

The ASAPP Chat SDK supports dynamic styling through configuration. This allows you to customize the appearance of various chat components without requiring CSS modifications.

### Incorporating Styling in the SDK

To dynamically apply styles based on the provided configuration, the SDK implements the following approach:

* **Extract Styling Configurations**: The SDK parses the `Chat.Styling` section of the configuration and identifies the defined styles for various elements.
* **Apply Styles Dynamically**: The SDK targets elements based on their class names and applies inline styles dynamically, ensuring that the defined styles are reflected in real-time.
* **Handle State-Based Styling**: Elements that support different states (e.g., button with default and focus styles) have event listeners added dynamically to switch styles when users interact with them.

### Configuration Schema

The enhanced configuration schema includes a `Chat` section that supports styling, icons, and features:

```json  theme={null}
{
  "Chat": {
    "Styling": {
      /* ChatStyling object */
    },
    "Icons": {
      /* ChatIcons object */
    },
    "Features": {
      /* ChatFeatures object */
    }
  }
}
```

### Styling Configuration

The `Chat.Styling` object allows you to customize the appearance of various chat elements:

#### Available Styling Options

**QuickReplies**: Customize quick reply buttons and their container

* `Container`: Scrollable container holding all quick reply buttons
* `Button`: Individual quick reply action buttons

<Accordion title="QuickReplies Example">
  ```json  theme={null}
  {
    "Chat": {
      "Styling": {
        "QuickReplies": {
          "Container": {
            "backgroundColor": "#f8f9fa",
            "padding": "12px",
            "borderRadius": "8px"
          },
          "Button": {
            "backgroundColor": "#5255e2",
            "color": "#ffffff",
            "border": "none",
            "borderRadius": "20px",
            "padding": "8px 16px",
            "fontSize": "14px",
            "fontWeight": "500"
          }
        }
      }
    }
  }
  ```
</Accordion>

**ChatInput**: Style chat input components

* `AttachmentButton.Icon`: Icon within the attachment button
* `SendButton.Icon.Disabled`: Send button icon in disabled state
* `SendButton.Icon.Enabled`: Send button icon in enabled state

<Accordion title="ChatInput Example">
  ```json  theme={null}
  {
    "Chat": {
      "Styling": {
        "ChatInput": {
          "AttachmentButton": {
            "Icon": {
              "fill": "#5255e2",
              "width": "20px",
              "height": "20px"
            }
          },
          "SendButton": {
            "Icon": {
              "Disabled": {
                "fill": "#cccccc",
                "opacity": "0.5"
              },
              "Enabled": {
                "fill": "#5255e2",
                "opacity": "1"
              }
            }
          }
        }
      }
    }
  }
  ```
</Accordion>

**EwtSheet**: Estimated Wait Time display styling

* `ProgressBar.Container`: Background container for progress bar
* `ProgressBar.Line`: Active progress indicator line
* `Content`: Main content area styling
* `SecondaryText`: Secondary description text
* `PrimaryText`: Primary time display text
* `TextContainer`: Wrapper for text elements
* `Button`: Action buttons in EWT sheet

<Accordion title="EwtSheet Example">
  ```json  theme={null}
  {
    "Chat": {
      "Styling": {
        "EwtSheet": {
          "ProgressBar": {
            "Container": {
              "backgroundColor": "#e9ecef",
              "borderRadius": "4px",
              "height": "8px"
            },
            "Line": {
              "backgroundColor": "#5255e2",
              "borderRadius": "4px",
              "transition": "width 0.3s ease"
            }
          },
          "Content": {
            "padding": "20px",
            "backgroundColor": "#ffffff",
            "borderRadius": "12px"
          },
          "PrimaryText": {
            "fontSize": "18px",
            "fontWeight": "600",
            "color": "#212529"
          },
          "SecondaryText": {
            "fontSize": "14px",
            "color": "#6c757d",
            "marginTop": "8px"
          },
          "TextContainer": {
            "textAlign": "center",
            "marginBottom": "16px"
          },
          "Button": {
            "backgroundColor": "#5255e2",
            "color": "#ffffff",
            "border": "none",
            "borderRadius": "6px",
            "padding": "10px 20px",
            "fontSize": "14px",
            "fontWeight": "500"
          }
        }
      }
    }
  }
  ```
</Accordion>

**ActionSheet**: Full screen modal action buttons

* `Buttons.Container`: Wrapper for all action buttons
* `Buttons.Primary`: Primary action button styling
* `Buttons.Secondary`: Secondary action button styling

<Accordion title="ActionSheet Example">
  ```json  theme={null}
  {
    "Chat": {
      "Styling": {
        "ActionSheet": {
          "Buttons": {
            "Container": {
              "display": "flex",
              "flexDirection": "column",
              "gap": "12px",
              "padding": "20px"
            },
            "Primary": {
              "backgroundColor": "#5255e2",
              "color": "#ffffff",
              "border": "none",
              "borderRadius": "8px",
              "padding": "12px 24px",
              "fontSize": "16px",
              "fontWeight": "600"
            },
            "Secondary": {
              "backgroundColor": "transparent",
              "color": "#5255e2",
              "border": "2px solid #5255e2",
              "borderRadius": "8px",
              "padding": "12px 24px",
              "fontSize": "16px",
              "fontWeight": "500"
            }
          }
        }
      }
    }
  }
  ```
</Accordion>

**NewQuestion**: New question prompt styling

* `Container`: Container for new question UI
* `Content.Text`: Text elements in prompt
* `Content.Icon`: Icon in new question UI

<Accordion title="NewQuestion Example">
  ```json  theme={null}
  {
    "Chat": {
      "Styling": {
        "NewQuestion": {
          "Container": {
            "backgroundColor": "#f8f9fa",
            "borderRadius": "12px",
            "padding": "16px",
            "border": "1px solid #dee2e6"
          },
          "Content": {
            "Text": {
              "fontSize": "14px",
              "color": "#495057",
              "fontWeight": "500"
            },
            "Icon": {
              "fill": "#5255e2",
              "width": "18px",
              "height": "18px"
            }
          }
        }
      }
    }
  }
  ```
</Accordion>

**ChatBanner**: Chat banner notifications

* `Container`: Banner container
* `Text`: Main banner text
* `Warning`: Warning variant styling
* `Error`: Error variant styling
* `Success`: Success variant styling
* `Icon`: Icon variant styling

<Accordion title="ChatBanner Example">
  ```json  theme={null}
  {
    "Chat": {
      "Styling": {
        "ChatBanner": {
          "Container": {
            "padding": "12px 16px",
            "borderRadius": "8px",
            "marginBottom": "12px",
            "display": "flex",
            "alignItems": "center",
            "gap": "8px"
          },
          "Text": {
            "fontSize": "14px",
            "fontWeight": "500",
            "lineHeight": "1.4"
          },
          "Warning": {
            "backgroundColor": "#fff3cd",
            "borderColor": "#ffeaa7",
            "color": "#856404"
          },
          "Error": {
            "backgroundColor": "#f8d7da",
            "borderColor": "#f5c6cb",
            "color": "#721c24"
          },
          "Success": {
            "backgroundColor": "#d1edff",
            "borderColor": "#bee5eb",
            "color": "#0c5460"
          },
          "Icon": {
            "width": "16px",
            "height": "16px",
            "flexShrink": "0"
          }
        }
      }
    }
  }
  ```
</Accordion>

**ChatMessagesView**: Chat messages display

* `ScrollView`: Chat view for chat messages

<Accordion title="ChatMessagesView Example">
  ```json  theme={null}
  {
    "Chat": {
      "Styling": {
        "ChatMessagesView": {
          "ScrollView": {
            "backgroundColor": "#ffffff",
            "padding": "16px",
            "overflowY": "auto",
            "maxHeight": "400px"
          }
        }
      }
    }
  }
  ```
</Accordion>

#### Styling Example

Here is a comprehensive example that combines multiple styling options:

```json  theme={null}
{
  "APIHostname": "sample.api.com",
  "AppId": "sampleAppId",
  "Language": "",
  "RegionCode": "",
  "CustomerId": "",
  "Display": {
    "Align": "right",
    "AlwaysShowMinimize": true,
    "BadgeColor": "#5255e2",
    "BadgeText": "",
    "BadgeType": "badge",
    "FrameDraggable": false,
    "FrameStyle": "default",
    "FrameTitle": null,
    "HideBadgeOnLoad": false,
    "Identity": "",
    "PrimaryColor": "#5255e2",
    "DarkColor": "#494a7c"
  },
  "Chat": {
    "Styling": {
      "QuickReplies": {
        "Container": {
          "backgroundColor": "#f8f9fa",
          "padding": "12px"
        },
        "Button": {
          "backgroundColor": "#5255e2",
          "color": "#ffffff",
          "borderRadius": "20px"
        }
      },
      "ChatInput": {
        "SendButton": {
          "Icon": {
            "Enabled": {
              "fill": "#5255e2"
            },
            "Disabled": {
              "fill": "#cccccc"
            }
          }
        }
      },
      "ChatBanner": {
        "Container": {
          "borderRadius": "8px",
          "padding": "12px"
        },
        "Success": {
          "backgroundColor": "#d1edff",
          "color": "#0c5460"
        }
      }
    }
  },
  "Intent": null,
  "Sound": true
}
```

## Custom Icons

The `Chat.Icons` section allows you to specify custom SVG path data for key icons used within the chat interface.

### Icon Configuration

The SDK supports using SVG `d` path data to create customizable icons. You only need to provide the `d` attribute value from your SVG:

```json  theme={null}
{
  "Chat": {
    "Icons": {
      "Minimize": "M 44 24 C 44 24.847656 43.308594 25.539062 42.460938 25.539062 L 5.539062 25.539062 C 4.691406 25.539062 4 24.847656 4 24 C 4 23.152344 4.691406 22.460938 5.539062 22.460938 L 42.460938 22.460938 C 43.308594 22.460938 44 23.152344 44 24 Z M 44 24",
      "Send": "M 2.289062 9.734375 C 1.773438 8.703125 1.957031 7.460938 2.746094 6.621094 C 3.539062 5.78125 4.765625 5.53125 5.832031 5.976562 L 44.332031 22.4375 C 45.347656 22.867188 46 23.859375 46 24.957031 C 46 26.054688 45.347656 27.050781 44.332031 27.476562 L 5.832031 43.9375 C 4.773438 44.390625 3.539062 44.136719 2.746094 43.296875 C 1.957031 42.453125 1.773438 41.210938 2.289062 40.183594 L 9.921875 24.964844 Z M 12.3125 26.339844 L 4.75 41.425781 L 40.042969 26.339844 Z M 40.042969 23.59375 L 4.75 8.507812 L 12.3125 23.59375 Z M 40.042969 23.59375",
      "NewQuestion": "M 16.5 33.601562 C 17.882812 33.601562 19 34.671875 19 36 L 19 39.601562 L 26.664062 34.082031 C 27.09375 33.765625 27.625 33.601562 28.164062 33.601562 L 39 33.601562 C 40.382812 33.601562 41.5 32.527344 41.5 31.199219 L 41.5 9.601562 C 41.5 8.273438 40.382812 7.199219 39 7.199219 L 9 7.199219 C 7.617188 7.199219 6.5 8.273438 6.5 9.601562 L 6.5 31.199219 C 6.5 32.527344 7.617188 33.601562 9 33.601562 Z M 4 9.601562 C 4 6.953125 6.242188 4.800781 9 4.800781 L 39 4.800781 C 41.757812 4.800781 44 6.953125 44 9.601562 L 44 31.199219 C 44 33.847656 41.757812 36 39 36 L 28.164062 36 L 18.5 42.960938 C 18.125 43.230469 17.613281 43.273438 17.1875 43.070312 C 16.757812 42.867188 16.5 42.457031 16.5 42 L 16.5 36 L 9 36 C 6.242188 36 4 33.847656 4 31.199219 Z M 4 9.601562",
      "ChatBanner": "your-custom-banner-icon-d-path-here"
    }
  }
}
```

### Available Icons

* **Minimize**: Icon for minimizing the chat window
* **Send**: Icon for the send button
* **NewQuestion**: Icon for starting a new question
* **ChatBanner**: Icon for chat banner notifications

<Note>
  Make sure to size your icons correctly. You may use an online SVG editor to
  resize your icons to meet the chat interface specifications.
</Note>

## Advanced Configuration Options

### Chat Features

The `Chat.Features` section controls the availability of specific chat features:

#### Estimated Wait Time (EWT)

Control whether the EWT feature is displayed:

```json  theme={null}
{
  "Chat": {
    "Features": {
      "EWT": {
        "enabled": true
      }
    }
  }
}
```

#### Focus Trap

Enable focus trap within the chat instance for better accessibility:

```json  theme={null}
{
  "Chat": {
    "Features": {
      "TrapFocus": true
    }
  }
}
```
