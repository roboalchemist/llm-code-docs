# Source: https://helm.sh/docs/plugins/

Title: Plugins Guide | Helm

URL Source: https://helm.sh/docs/plugins/

Markdown Content:
Plugins Guide | Helm
===============

[Skip to main content](https://helm.sh/docs/plugins/#__docusaurus_skipToContent_fallback)

🎉 Helm v4.0.0 is out! See the [Helm 4 Overview](https://helm.sh/docs/overview) for details!

[![Image 1: Helm Logo](https://helm.sh/img/helm.svg) **Helm**](https://helm.sh/)[Docs](https://helm.sh/docs)[Community](https://helm.sh/community)[Blog](https://helm.sh/blog)[Charts](https://artifacthub.io/)

[4.0.0](https://helm.sh/docs/plugins/)
*   [4.0.0](https://helm.sh/docs/plugins/)
*   [3.19.0](https://helm.sh/docs/v3/)
*   [2.17.0](https://helm.sh/docs/v2/)

[English](https://helm.sh/docs/plugins/#)
*   [English](https://helm.sh/docs/plugins/)
*   [Deutsch (German)](https://helm.sh/de/docs/plugins/)
*   [Ελληνικά (Greek)](https://helm.sh/el/docs/plugins/)
*   [Español (Spanish)](https://helm.sh/es/docs/plugins/)
*   [Français (French)](https://helm.sh/fr/docs/plugins/)
*   [日本語 (Japanese)](https://helm.sh/ja/docs/plugins/)
*   [한국어 (Korean)](https://helm.sh/ko/docs/plugins/)
*   [Português (Portuguese)](https://helm.sh/pt/docs/plugins/)
*   [Русский (Russian)](https://helm.sh/ru/docs/plugins/)
*   [Українська (Ukrainian)](https://helm.sh/uk/docs/plugins/)
*   [中文 (Chinese)](https://helm.sh/zh/docs/plugins/)

Search

*   [Docs Home](https://helm.sh/docs/)
*   [Helm 4 Overview](https://helm.sh/docs/overview)
*   [Full Changelog](https://helm.sh/docs/changelog)
*   [Introduction](https://helm.sh/docs/intro/) 
*   [How-to](https://helm.sh/docs/howto/) 
*   [Topics](https://helm.sh/docs/topics/) 
*   [Best Practices](https://helm.sh/docs/chart_best_practices/) 
*   [Chart Template Guide](https://helm.sh/docs/chart_template_guide/) 
*   [Plugins](https://helm.sh/docs/plugins/) 
    *   [Overview](https://helm.sh/docs/plugins/overview)
    *   [Using Plugins](https://helm.sh/docs/plugins/user/)
    *   [Developing Plugins](https://helm.sh/docs/plugins/developer/) 

*   [Helm Commands](https://helm.sh/docs/helm/) 
*   [Go SDK](https://helm.sh/docs/sdk/) 
*   [Frequently Asked Questions](https://helm.sh/docs/faq/) 
*   [Glossary](https://helm.sh/docs/glossary/)

*   [](https://helm.sh/)
*   [Docs](https://helm.sh/docs/)
*   Plugins

Version: 4.0.0

Plugins Guide
=============

This guide explains what Helm plugins are, how to use them, and how to build them.

[📄️Overview ----------- Helm Plugins allow users to extend the core feature set of Helm, without requiring every new feature to be written in Go and added to Helm core.](https://helm.sh/docs/plugins/overview)[📄️Using Plugins ---------------- For an overview of Helm Plugin concepts, how to read their structure, and how to understand what their configurations mean for you as a user, read the Plugins Overview.](https://helm.sh/docs/plugins/user/)[🗃️Developing Plugins --------------------- 3 items](https://helm.sh/docs/plugins/developer/)

[Edit this page](https://github.com/helm/helm-www/blob/main/docs/plugins/index.mdx)

[Previous Appendix: Go Data Types and Templates](https://helm.sh/docs/chart_template_guide/data_types)[Next Overview](https://helm.sh/docs/plugins/overview)

Helm Project

*   [Source code](https://github.com/helm/helm)
*   [Blog](https://helm.sh/blog)
*   [Events](https://www.cncf.io/community/kubecon-cloudnativecon-events/)
*   [Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md)

Charts

*   [Introduction](https://helm.sh/docs/intro)
*   [Chart tips & tricks](https://helm.sh/docs/howto/charts_tips_and_tricks)
*   [Developing Charts](https://helm.sh/docs/topics/charts)
*   [Search 800+ Charts](https://artifacthub.io/)

Development

*   [Slack (#helm-dev)](https://kubernetes.slack.com/messages/C51E88VDG)
*   [Contribution Guide](https://github.com/helm/helm/blob/main/CONTRIBUTING.md)
*   [Maintainers](https://github.com/helm/helm/blob/main/OWNERS)
*   [Weekly Meetings](https://github.com/helm/community/blob/main/communication.md#meetings)

Community

*   [GitHub Community](https://github.com/helm/community)
*   [Slack (#helm-users)](https://kubernetes.slack.com/)
*   [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes-helm)
*   [X](https://x.com/helmpack)

![Image 2: CNCF Logo](https://helm.sh/img/cncf-white.png)

We are a [Cloud Native Computing Foundation](https://www.cncf.io/) graduated project.

© Helm Authors 2026. Documentation distributed under [CC-BY-4.0.](https://creativecommons.org/licenses/by/4.0)

© 2026 The Linux Foundation. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage/).
