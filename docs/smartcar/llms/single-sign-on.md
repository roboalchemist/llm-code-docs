# Source: https://smartcar.com/docs/getting-started/dashboard/single-sign-on.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Single Sign-on (SSO)

> Smartcar offers SSO through your identity provider (IdP) for Enterprise customers.

## About SSO with Smartcar

Our Dashboard supports SSO integrations with popular identity providers
including:

* Okta
* Microsoft Azure AD
* Google Workspace
* OneLogin
* Ping Identity
* ADFS
* Custom SAML 2.0 providers

To set up SSO for your organization's Dashboard accounts, you'll need to:

1. Be an Owner for an existing Team on an Enterprise plan
2. Verify your domain
3. Configure your identity provider

The following section will guide you through each step of this process.

## Setting up SSO

On Dashboard navigate to **Team settings > Security** and select **Enable SSO**

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=25cb9f378d60084f216d0c8341d0d846" alt="" data-og-width="1417" width="1417" data-og-height="517" height="517" data-path="images/dashboard/sso/enable-sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b877b06d48922a99f9bb92b3e8f4efc4 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e61a60c77fa33f873a1db2e3fe57ed81 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d59d2cd95e627bfacab7173d91d4c67b 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=cecb3e19007e9f33df5e7b8b8ac4b6fe 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=524b58a248c8701af8283b5a9ce92d3d 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6d9aa3c05e1d6e9612691b8055f40528 2500w" />
</Frame>

You’ll be redirected to start the SSO configuration process.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d2163f376519a4a27ccedd07910091e1" alt="" data-og-width="1061" width="1061" data-og-height="705" height="705" data-path="images/dashboard/sso/verify-domain-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=83581ff2b0559a69d2b2b2ab370549a8 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e2510c784e807c1b340da2bbc082e786 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=16b463970552e8d9a47a8e1d1dc833d6 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f4d3c7240ae3d77080f6de659b6fcf6c 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4ec6364f91acfd734dda45554a3e0408 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7d74cc03530fd081ee1738ff37bcbc77 2500w" />
</Frame>

Depending on your DNS provider, you'll receive instructions on how to verify your domain.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8a522104b3e4c392add44c7b7670a8b5" alt="" data-og-width="516" width="516" data-og-height="1016" height="1016" data-path="images/dashboard/sso/verify-domain-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=fb506b211830b3657f537a6416f0e911 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f0c5752093458dea14d516858189d9f9 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f348dc19bd86c34cca8fe03ee909c346 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=11cc2649d63e9031eaa1658b494ffb88 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ce55ea6c6cbbe1c0734ff7588b02d610 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3c389d53c4e0fe9484667d5b49549482 2500w" />
</Frame>

Once your domain is verified, you’ll be able to select your Identity Provider
(IdP).

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=cc58d3e1c79ea46ba0ac7d0879cc2f8c" alt="" data-og-width="1145" width="1145" data-og-height="486" height="486" data-path="images/dashboard/sso/select-idp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d729fbaa9b48bdb3d6aefef2bfa9b34e 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=fd53922bfdccd7ea2b2c61b697890790 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c850e9b64b9a01bc5e8c765912d0229f 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e3e368a3b8a496a0ee7adc2ee1138d33 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=86c92b78a1966b299f3c221dc1cbacf5 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a1c9ed66aff7e8378e11d1a6cd34a925 2500w" />
</Frame>

You'll be provided a guide on how to get set up based on your IdP.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5b175cde2bc4e00277c17b3d63a84e53" alt="" data-og-width="1058" width="1058" data-og-height="588" height="588" data-path="images/dashboard/sso/config-idp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c0b1bea8be73031103dfbc8429d135bd 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=daac4db2d45418bb324ef5fca7447e4c 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8c7331c3ed3011fb2e8d77d8b0a865cf 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0047a406d29b6bf7bfb09a7cbf3b73de 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1bf560fd843ac8b5867d8df632b6929f 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=050664254b62d1b1db1b7096e2b2729c 2500w" />
</Frame>

Once you’ve got everything configured, you’ll be prompted to test SSO.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2dc072fb8b8c9b3dd933091bb0ffa8a7" alt="" data-og-width="1058" width="1058" data-og-height="366" height="366" data-path="images/dashboard/sso/test-sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7464494f6b5eed426690448ff4b5caaa 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0decc9519c098999c40340a8f81f4b69 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ce699b5e204863e02f7c98467880a90b 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8d5a5db32d3a5a91b8d5674031b5e7ec 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6e1b36599829f751db351b712de0eefc 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b5958057a9435dfc4e4f3c2d1c015716 2500w" />
</Frame>

<br />

<Tip>
  If you exit the flow at any time before finalizing your configuration, you
  can jump back in from Dashboard.
</Tip>

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4e8f44f02059878dce36912a5dde0519" alt="" data-og-width="1076" width="1076" data-og-height="626" height="626" data-path="images/dashboard/sso/sso-config-pending.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dbb3f3e5dee8f79067f30b60a5ff7c84 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a858f0b128121c9d4d3c374b2dcd15de 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=25b14426cafd0b438a88fa6e4e5bee0c 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9faf2ed7404f98a270ec2ee18bf09c64 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=959f81303a64f4921223f039cc8c39f5 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c19d9c97584ed8e2b21a212be243a86f 2500w" />
</Frame>

## Disabling SSO

If you have SSO configured, the Team Owner can disable it from **Team
settings > Security**.

<Warning>
  Disabling SSO will require you to go through the whole setup process
  again.
</Warning>

## Inviting team members with SSO enabled

Once enabled, you’ll need to add members to your team through your identity
provider. Invites via the Dashboard will be disabled while SSO is enabled.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=cd408514ef3a7e8e46a7b2368e02901e" alt="" data-og-width="875" width="875" data-og-height="285" height="285" data-path="images/dashboard/sso/invite-with-sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7a938fc9e64e07750d4c5d03a4fc5068 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4cdf56ef26632ba9b9ea5d9143cba134 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e156364b2a42d2c7823c960113c18db8 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=50dcc0576cb4ea96daa32a42fa793cc1 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=296d66de91680940b072231d77454b16 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=891f8b7fc43e673b75638f3e352c52b0 2500w" />
</Frame>

When a newly added member has signed in via SSO, they will have the Viewer role
by default. Other team members with the appropriate role can promote these
members as needed.

<Note>
  If a user creates a Dashboard account with their email prior to being added
  to your IdP, they will be added to their own Team initially. When they are
  added to your IdP they will be able to switch Teams in Dashboard.
</Note>

## A note on aliased emails

If members of your team have Dashboard accounts using email aliases prior to
enabling SSO e.g. [rover+thebest@dog.com](mailto:rover+thebest@dog.com), once SSO is enabled for your Team and
they’re added to your IdP, their login will be tied to their non-aliased email
address e.g. [rover@dog.com](mailto:rover@dog.com).

SSO is only available on the **Enterprise** plan, please reach out to your Account Manager for more details.
