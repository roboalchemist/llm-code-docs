# Source: https://docs.venice.ai/overview/privacy.md

# Privacy

Nearly all AI apps and services collect user data (personal information, prompt text, and AI text and image responses) in central servers, which they can access, and which they can (and do) share with third parties, ranging from ad networks to governments. Even if a company wants to keep this data safe, data breaches happen [all the time](https://www.wired.com/story/wired-guide-to-data-breaches/), often unreported.

> The only way to achieve reasonable user privacy is to avoid collecting this information in the first place. This is harder to do from an engineering perspective, but we believe it’s the correct approach.

### Privacy as a principle

One of Venice’s guiding principles is user privacy. The platform's architecture flows from this philosophical principle, and every component is designed with this objective in mind.

#### Architecture

The Venice API replicates the same technical architecture as the Venice platform from a backend perspective.

**Venice does not store or log any prompt or model responses on our servers.** API calls are forwarded directly to GPUs running across a collection of decentralized providers over encrypted HTTPS paths.

<img src="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=dc109b987638ae5757c4987a971ae809" alt="Venice AI Privacy Architecture" data-og-width="2042" width="2042" data-og-height="812" height="812" data-path="images/privacy-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=280&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=73d83e285d8065397e72037b907d1509 280w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=560&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=43300078e2e65b024c97164342926b05 560w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=840&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=2994c6fd3f18dd7a18fff305ebb02e2d 840w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=1100&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=e819afb6dd5d785c5fbb176f4b2cb40e 1100w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=1650&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=03b65f4716d95c25ab92e4e733405bc8 1650w, https://mintcdn.com/veniceai/IFxWLBK8qRcf4Dhb/images/privacy-architecture.png?w=2500&fit=max&auto=format&n=IFxWLBK8qRcf4Dhb&q=85&s=863ab31cb8e886e2f2f67975c6a7fcab 2500w" />
