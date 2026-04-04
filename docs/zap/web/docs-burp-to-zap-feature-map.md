# Source: https://www.zaproxy.org/docs/burp-to-zap-feature-map/

Title: Burp to ZAP Feature Map

URL Source: https://www.zaproxy.org/docs/burp-to-zap-feature-map/

Markdown Content:
![Image 1: ZAP to Burp](https://www.zaproxy.org/img/burp2zap.png)

Burp Suite is a popular commercial web app pentesting tool. It provides a free (closed source) Community edition and a paid for Professional edition. Many people are unaware that ZAP provides most of the features available in both the Professional and Community editions of Burp.

It should be noted that ZAP is not intended to be a Burp clone and as such has a different way of working. ZAP and Burp features may well not provide exactly the same functionality - in some cases Burp may provide more options but in other cases ZAP may exceed Burp’s capabilities.

An ongoing series of blog posts show how to use ZAP to solve some of the [PortSwigger labs](https://www.zaproxy.org/tags/portswigger-lab/).

### Feature Map [](https://www.zaproxy.org/docs/burp-to-zap-feature-map/#feature-map)

A mapping from Burp features to their ZAP equivalents. All Burp features are available in the Professional edition but some features are not available in the Community edition, or are throttled like the Intruder.

| Burp Feature | Community | Notes | ZAP Equivalent(s) |
| --- | --- | --- | --- |
| Collaborator | ❌ |  | [OAST Support Add-on](https://www.zaproxy.org/docs/desktop/addons/oast-support/) |
| Comparer | ✓ |  | [Diff](https://www.zaproxy.org/docs/desktop/addons/diff/) |
| Decoder | ✓ |  | [Encoder](https://www.zaproxy.org/docs/desktop/addons/encode-decode-hash/) |
| DOM Invader | ✓ |  | [Eval Villian Add-on](https://www.zaproxy.org/docs/desktop/addons/eval-villain/) |
| Extender | ✓ |  | [Marketplace](https://www.zaproxy.org/addons/) , [Scripts](https://www.zaproxy.org/docs/desktop/start/features/scripts/) |
| Intercept | ✓ |  | [Breakpoints](https://www.zaproxy.org/docs/desktop/start/features/breakpoints/) |
| Intruder | ✓ | Throttled | [Fuzzer](https://www.zaproxy.org/docs/desktop/addons/fuzzer/) |
| Live scan | ❌ |  | [ATTACK Mode](https://www.zaproxy.org/docs/desktop/start/features/modes/) |
| Project Files | ❌ |  | [Session Files](https://www.zaproxy.org/docs/desktop/ui/dialogs/persistsession/) |
| Proxy | ✓ |  | [Proxy](https://www.zaproxy.org/docs/desktop/start/features/intercept/) |
| Repeater | ✓ |  | [Manual Request Editor](https://www.zaproxy.org/docs/desktop/addons/requester/dialogs/) , [Requester Add-on](https://www.zaproxy.org/docs/desktop/addons/requester/) |
| Scanner | ❌ |  | [Active Scanner](https://www.zaproxy.org/docs/desktop/start/features/ascan/) |
| Sequencer | ✓ |  | [Token Generation and Analysis](https://www.zaproxy.org/docs/desktop/addons/token-generator/) |
| Target | ✓ |  | [Contexts](https://www.zaproxy.org/docs/desktop/start/features/contexts/) |

### ZAP Missing Features [](https://www.zaproxy.org/docs/burp-to-zap-feature-map/#zap-missing-features)

The following significant features are available in Burp but currently not in ZAP:

*   HTTP Host Header manipulation 
    *   due to limitations in the current ZAP networking stack it was not possible to manipulate some part of the HTTP header 
        *   **Update:** this is now possible programmatically but not in the desktop UI - this is being worked on so this restriction will be removed

### Burp Missing Features [](https://www.zaproxy.org/docs/burp-to-zap-feature-map/#burp-missing-features)

The following significant features are available in ZAP but currently not in Burp:

*   [Automation Framework](https://www.zaproxy.org/docs/automate/automation-framework/)
*   [The Heads Up Display (HUD)](https://github.com/zaproxy/zap-hud)
