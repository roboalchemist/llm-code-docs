# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/administration/setup-requirements.md

# Enate System Setup Requirements / Whitelisting

## UserPilot Inline Help - Setup Requirements

With Enate you've got access to enhanced tooltips, explainers and inline help, plus content to let you know about new features when they appear. In order for these overlay explainers to show correctly in enate, you'll need to ensure that your company's security policy is set up to allow for the information to display (some companies policies can block this kind of information as a default).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-M__8PiT509Cms6Btwuu%2F-M__9PAzHeyUO2-N6xGA%2FUserpilot-Interactions.gif?alt=media\&token=20c41983-d6f7-402f-a131-2813822ce264)

Enate uses 'Userpilot' technology for its inline helpers to show. UserPilot uses Web Sockets to send data to client machines and requires that these work through any web proxies or firewalls that are configured within the customer environment. We've previously seen issues with the UserPilot Web Socket connection where proxies have been configured to perform SSL inspection against all traffic in the environment.&#x9;

### UserPilot Whitelisting requirements

UserPilot provides the following list of addresses whichit is recommended to be whitelisted in order for the inline helpers to show correctly:

* <https://uploads.userpilot.io>
* <https://api.userpilot.io>
* wss\://api.userpilot.io
* <https://find.userpilot.io>
* <https://find-x.userpilot.io>
* <https://find-y.userpilot.io>
* <https://find-z.userpilot.io>
* <https://find-w.userpilot.io>
* wss\://analytex.userpilot.io
* wss\://analytex-us.userpilot.io
* wss\://analytex-eu.userpilot.io
* wss\://analytex-in.userpilot.io
* <https://analytex.userpilot.io>
* <https://analytex-us.userpilot.io>
* <https://analytex-eu.userpilot.io>
* <https://analytex-in.userpilot.io>
* <https://reporting.userpilot.io>
* wss\://reporting.userpilot.io
* <https://playground.userpilot.io>
* <https://fonts.googleapis.com>
* <https://fonts.gstatic.com>
* <https://fonts.userpilot.io>
* <https://js.userpilot.io>
* <https://media.userpilot.io>
* <https://uploads.userpilot.io>
* <https://gifs.userpilot.io>
* <https://videos.userpilot.io>
* <https://js.userpilot.io>
* <https://deploy.userpilot.io>

Additionally, Enate requires that the following addresses are whitelisted to serve Enate specific media embedded within UserPilot experiences:

* <https://media.enate.net>
* <https://enate.cdn.spotlightr.com>

For further information on UserPilot security setup requirements, please see the following link: <https://docs.userpilot.com/article/152-faq-content-security-policy>

### Enate Academy Whitelisting&#x20;

If training users trying to access Enate Academy ([www.enate.academy](https://www.enate.academy)) are experiencing connectivity issues, it could be that your organization's IT security settings are blocking the site / its contents. In order to help with this, you should get the following Academy url's whitelisted:

* [https://www.enate.academy](https://www.enate.academyenatecommunity.docebosaas.comhttp/cdn1.dcbstatic.com/http://cdn2.dcbstatic.com/http://cdn3.dcbstatic.com/http://cdn4.dcbstatic.com/http://cdn5.dcbstatic.com/)
* [enatecommunity.docebosaas.com](https://www.enate.academyenatecommunity.docebosaas.comhttp/cdn1.dcbstatic.com/http://cdn2.dcbstatic.com/http://cdn3.dcbstatic.com/http://cdn4.dcbstatic.com/http://cdn5.dcbstatic.com/)
* [http://cdn1.dcbstatic.com/](https://www.enate.academyenatecommunity.docebosaas.comhttp/cdn1.dcbstatic.com/http://cdn2.dcbstatic.com/http://cdn3.dcbstatic.com/http://cdn4.dcbstatic.com/http://cdn5.dcbstatic.com/)
* [http://cdn2.dcbstatic.com/](https://www.enate.academyenatecommunity.docebosaas.comhttp/cdn1.dcbstatic.com/http://cdn2.dcbstatic.com/http://cdn3.dcbstatic.com/http://cdn4.dcbstatic.com/http://cdn5.dcbstatic.com/)
* [http://cdn3.dcbstatic.com/](https://www.enate.academyenatecommunity.docebosaas.comhttp/cdn1.dcbstatic.com/http://cdn2.dcbstatic.com/http://cdn3.dcbstatic.com/http://cdn4.dcbstatic.com/http://cdn5.dcbstatic.com/)
* [http://cdn4.dcbstatic.com/](https://www.enate.academyenatecommunity.docebosaas.comhttp/cdn1.dcbstatic.com/http://cdn2.dcbstatic.com/http://cdn3.dcbstatic.com/http://cdn4.dcbstatic.com/http://cdn5.dcbstatic.com/)
* [http://cdn5.dcbstatic.com/](https://www.enate.academyenatecommunity.docebosaas.comhttp/cdn1.dcbstatic.com/http://cdn2.dcbstatic.com/http://cdn3.dcbstatic.com/http://cdn4.dcbstatic.com/http://cdn5.dcbstatic.com/)

## PostHog - Feature Usage

Enate also uses some feature usage services to help us improve our software features based on how it's used. For this to work correctly, the following url should also be whitelisted:

* <https://eu.posthog.com>
