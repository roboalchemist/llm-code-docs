# Source: https://www.aptible.com/docs/core-concepts/security-compliance/compliance-frameworks/hipaa.md

# HIPAA

> Learn about achieving HIPAA compliance on Aptible

<Check>
  <Tooltip tip="This compliance framework's infrastructure controls/requirements are automatically satisfied when you deploy to a Dedicated Stack. See details below for more information.">Compliance-Ready</Tooltip>
</Check>

# Overview

Aptible’s story began with a focus on serving digital health companies. As a result, the Aptible platform was designed with HIPAA compliance in mind. It automates and enforces all the necessary infrastructure security and compliance controls, ensuring the safe storage and processing of HIPAA-protected health information and more.

# Achieving HIPAA on Aptible

<Steps>
  <Step title="Provision a Dedicated Stack to run your resources">
    <Info> Dedicated Stacks are available on [Production and Enterprise plans](https://www.aptible.com/pricing).</Info>
    Dedicated Stacks live on isolated infrastructure and are designed to support deploying resources with higher requirements— such as HIPAA. Aptible automates and enforces **100%** of the necessary infrastructure security and compliance controls for HIPAA compliance.
  </Step>

  <Step title="Execute a HIPAA BAA with Aptible">
    When you request your first dedicated stack, an Aptible team member will reach out to coordinate the execution of a Business Associate Agreement (BAA).
  </Step>

  <Step title="Show off your compliance" icon="party-horn">
    <Frame>
            <img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/screenshot-ui.6e552b45.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=808fec7d4bdbe090437f3de79c2e9d84" alt="" data-og-width="1312" width="1312" data-og-height="645" height="645" data-path="images/screenshot-ui.6e552b45.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/screenshot-ui.6e552b45.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=98222990b7b298db06819d861394b233 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/screenshot-ui.6e552b45.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=c472cd3b11210413d3f7cfd5a674b0e6 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/screenshot-ui.6e552b45.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=a4faa7ce0ab41cd983a448635e21a32f 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/screenshot-ui.6e552b45.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e322259925a417312fb26c56d15fe9b6 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/screenshot-ui.6e552b45.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=53175f739a22b10a2b0b2d859344a8dc 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/screenshot-ui.6e552b45.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=67875a8a778d9b4bda6079828d16ef39 2500w" />
    </Frame>

    The Security & Compliance Dashboard and reporting serves as a great resource for showing off HIPAA compliance. When a Dedicated Stack is provisioned, the HIPAA required controls will show as 100% - by default.

    <Accordion title="Understanding the HIPAA Readiness Score">
      The Health Insurance Portability and Accountability Act of 1996 (HIPAA) is a federal law that dictates US standards to protect sensitive patient health information from being disclosed without the patient’s consent or knowledge. The [US Department of Health and Human Services (HHS)](https://www.hhs.gov/hipaa/index.html) issued the HIPAA Privacy Rule to implement the requirements of HIPAA. The HIPAA Security Rule protects a subset of information covered by the Privacy Rule.

      The Aptible Security & Compliance Dashboard provides a HIPAA readiness score based on controls required for meeting the minimum standards of the regulation, labeled HIPAA Required, as well as addressable controls that are not required to meet the specifications of the regulation but are recommended as a good security practice, labeled HIPAA Addressable.

      ## HIPAA Required Score

      HIPAA prescribes certain implementation specifications as “required, “meaning you must implement the control to meet the regulation requirements. An example of such a specification is 164.308(a)(7)(ii)(A), requiring implemented procedures to create and maintain retrievable exact copies of ePHI. You can meet this specification with Aptible’s [automated daily backup creation and retention policy](/core-concepts/managed-databases/managing-databases/database-backups).

      The HIPAA Required score gives you a binary indicator of whether or not you’re meeting the required specifications under the regulation. By default, all resources hosted on a [Dedicated Stack](/core-concepts/architecture/stacks) meet the required specifications of HIPAA, so if you plan on processing ePHI, it’s a good idea to host your containers on a Dedicated Stack from day 1.

      ## HIPAA Addressable Score

      The HHS developed the concept of “addressable implementation specifications” to provide covered entities and business associates additional flexibility regarding compliance with HIPAA. In meeting standards that contain addressable implementation specifications, a covered entity or business associate will do one of the following for each addressable specification:

      * Implement the addressable implementation specifications;
      * Implement one or more alternative security measures to accomplish the same purpose;
      * Not implement either an addressable implementation specification or an alternative.

      The HIPAA Addressable score tells you what percentage of infrastructure controls you have implemented successfully to meet relevant addressable specifications per HIPAA guidelines.
    </Accordion>

    Add a `Secured by Aptible` badge and link to the Secured by Aptible page to show all the security & compliance controls implemented..

    <Frame>
            <img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/hipaa1.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=370a50fd056d2932d575103c2f5fe4b4" alt="" data-og-width="320" width="320" data-og-height="96" height="96" data-path="images/hipaa1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/hipaa1.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=32816d5c77a20233b0873741e42d1568 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/hipaa1.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=0b82d70aeb288966b2af6a9dd663f114 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/hipaa1.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=e03ba3e5ba900d9a068500cab4dd59c8 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/hipaa1.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=5dab9aed9c50ffa98dc433fded119086 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/hipaa1.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ebcf9f376682656059ebc51ce3d534d4 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/hipaa1.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=36adaffd6732f94820327fdbf46794b5 2500w" />
    </Frame>
  </Step>
</Steps>

# Keep Reading

<CardGroup cols={2}>
  <Card title="Read HIPAA Compliance Guide for Startups" icon="book" iconType="duotone" href="https://www.aptible.com/blog/hipaa-compliance-guide-for-startups">
    Gain a deeper understanding of HIPAA compliance
  </Card>

  <Card title="Explore HITRUST" icon="book" iconType="duotone" href="https://www.aptible.com/docs/core-concepts/security-compliance/compliance-frameworks/hitrust">
    Learn why Aptible is the leading platform for achieving HITRUST
  </Card>
</CardGroup>

***

# FAQ

<AccordionGroup>
  <Accordion title="How much does it cost to get started with HIPAA Compliance on Aptible?">
    To begin with HIPAA compliance on Aptible, the Production plan is required, priced at \$499 per month.

    This plan includes one dedicated stack, ensuring the necessary isolation and guardrails for HIPAA requirements. Additional resources are billed on demand, with initial costs typically ranging between 200.00 USD to 500.00 USD.

    Additionally, Aptible offers a Startup Program that provides monthly credits over the first six months.

    [For more details, refer to the Aptible Pricing Page.](https://www.aptible.com/pricing)
  </Accordion>
</AccordionGroup>
