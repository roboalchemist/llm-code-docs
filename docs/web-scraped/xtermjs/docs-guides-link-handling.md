# Source: https://xtermjs.org/docs/guides/link-handling/

<div>

# [Link Handling](/docs/guides/link-handling/)

</div>

Clickable links may appear in the terminal output two ways:

-   Emitted using an explicit escape sequence (OSC 8).
-   Implicitly using something that looks a URL in the output, recognized using pattern matching. This requires the `web-links` addon.

## Setup

This is one way to handle both kinds of links.

``` highlight
function activateLink(event, uri) 
let linkHandler =  ,
  hover: (event, text, range) => ,
  leave: (event, text, range) => ,
  allowNonHttpProtocols: true
};

/* Detect links because of URL patterns. */
webLinksAddon = new WebLinksAddon(activateLink, linkHandler);
/* Handle explicit links using USC 8 escape sequences. */
xterm.options.linkHandler = linkHandler;
```

## Require modifier key

Terminal emulators that handle clicking on a link usually require a modifier to be pressed, to avoid unintentional window-opening. Commonly the `Ctrl` modifier (or on macOS the `Cmd` modifier) must be pressed.

``` highlight
function linkRequiresModifier() 
function isMac() 

// Replace activateLink above
function activateLink(event, uri) 
}
```

## Display URL on hovering

It might be helpful to show the full URL when hovering over a link, especially for links created by OSC 8 (which might not show the actual URL). This is safety feature commonly implemented in web browsers and mail readers.

``` highlight
let _linkPopup;
function removeLinkPopup = (event, text, range) 
}
function showLinkPopup(event, text, range) +Click to open link)`;
    popup.appendChild(e2);
  }
  const topElement = event.target.parentNode;
  topElement.appendChild(popup);
  const popupHeight = popup.offsetHeight;
  if (event.clientY + 25 + popupHeight > topNode.clientHeight) 
  _linkPopup = popup;
};

linkHandler.hover = showLinkPopup;
linkHandler.leave = removeLinkPopup;
```

Possible CSS styling for the hover popup:

``` highlight
div.xterm-link-popup 
```