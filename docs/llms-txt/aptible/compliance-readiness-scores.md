# Source: https://www.aptible.com/docs/core-concepts/security-compliance/security-compliance-dashboard/compliance-readiness-scores.md

# Compliance Readiness Scores

The performance of the security controls in the Security & Compliance Dashboard affects your readiness score towards regulations and frameworks like HIPAA and HITRUST. These scores tell you how effectively you have implemented infrastructure controls to meet these frameworks’ requirements.

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/f48c11f-compliance-visibility-scores-all.png?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=ab18cf480d9e9960131766d0cd166b7f" alt="Image" data-og-width="3578" width="3578" data-og-height="1108" height="1108" data-path="images/f48c11f-compliance-visibility-scores-all.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/f48c11f-compliance-visibility-scores-all.png?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=871f1bee4b2a7e40525341c883d3e20d 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/f48c11f-compliance-visibility-scores-all.png?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=1b19bc6da070a378e35845a64ac54fd3 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/f48c11f-compliance-visibility-scores-all.png?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=16220e84297d41352673d98f6f23a4d0 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/f48c11f-compliance-visibility-scores-all.png?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=43690123e67fd33ea1775887da01c5c9 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/f48c11f-compliance-visibility-scores-all.png?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=26505fe3a08de0586a9b4c7291fb197b 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/f48c11f-compliance-visibility-scores-all.png?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=b2df054a8fd71f910309819658b46a56 2500w" />

Aptible has mapped the controls visualized in the Dashboard to HIPAA and HITRUST requirements.

# HIPAA Readiness Score

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

# HITRUST-CSF Readiness Score

The [HITRUST Common Security Framework (CSF) Certification](https://hitrustalliance.net/product-tool/hitrust-csf/) is a compliance framework based on ISO/IEC 27001. It integrates HIPAA, HITECH, and a variety of other state, local, and industry frameworks and best practices. Independent assessors award this certification when they find that an organization has achieved certain maturity levels in implementing the required HITRUST CSF controls.

HITRUST CSF is unique because it allows customers to inherit security controls from the infrastructure they host their resources on if the infrastructure provider is also HITRUST CSF certified, enabling you to save time and resources when you begin your certification process. Aptible is HITRUST certified, meaning you can fully inherit up to 30% of security controls implemented and managed by Aptible and partially inherit up to 50% of security controls.

The Aptible Security & Compliance Dashboard provides a HITRUST readiness score based on controls required for meeting the standards of HITRUST CSF regulation. The HITRUST score tells you what percentage of infrastructure controls you have successfully implemented to meet relevant HITRUST guidelines.
