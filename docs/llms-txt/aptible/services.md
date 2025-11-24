# Source: https://www.aptible.com/docs/core-concepts/apps/deploying-apps/services.md

# Services

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/services-screenshot.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=4cdf448c42f8498f82319b49b20cd346" alt="" data-og-width="5120" width="5120" data-og-height="2560" height="2560" data-path="images/services-screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/services-screenshot.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=c934e8c1e781dd298fb831ee451afb7d 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/services-screenshot.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5af8be90984d1e5a8e887f18351e0844 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/services-screenshot.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=da94fb5fa5e69ba04f001c5533628349 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/services-screenshot.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=f3edffa564ebe0fb385e7ff91cd90bb6 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/services-screenshot.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=9813349276625948250289113f3572bd 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/services-screenshot.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=b3fd10b71338eec46d6e6a59917ea0d4 2500w" />

# Overview

Services determine the number of Containers of your App and the memory and CPU limits for your app. An app can have multiple services.

Services are defined one of two ways:

* **Single Implicit Service:** By default, the platform will create a single implicit cmd service defined by your image’s `cmd` or `ENTRYPOINT`.
* **Explicit Services:** Alternatively, you can define one or more explicit services using a Procfile. This allows you to specify a command for each service. Each service is scaled independently.

# FAQ

<AccordionGroup>
  <Accordion title="How do I define Services">
    See related guide

    <Card title="How to define Services" icon="book-open-reader" iconType="duotone" href="https://www.aptible.com/docs/how-to-guides/app-guides/define-services" />
  </Accordion>

  <Accordion title="Can Services be scaled indepedently?">
    Yes, all App Services are scaled independently
  </Accordion>
</AccordionGroup>
