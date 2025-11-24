# Source: https://docs.asapp.com/agent-desk/digital-agent-desk/agent-sso.md

# Agent SSO

> Learn how to use Single Sign-On (SSO) to authenticate agents and admin users to the Digital Agent Desk.

ASAPP recommends for our customers to use SSO to authenticate agents and admin users to our applications.

In this scenario:

1. ASAPP is the Service Provider (SP) with the customer acting as the Identity Provider (IDP).
2. The customer's authentication system performs user authentication using their existing customer credentials.
3. ASAPP supports Service Provider Initiated SSO. Customers will provide the SSO URL to the agents and admins.
4. The URL points to the customer's SSO service, which will authenticate the users via their authentication system.
5. Once the user is authenticated, the customer's SSO service will send a SAML assertion, which includes some user information to ASAPP's SSO service.
6. ASAPP uses the information inside the SAML assertion to identify the user and redirect them to the appropriate application.

The diagram below illustrates the IDP-initiated SSO flow.

<Frame>
  <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/AgentDeskSSO.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=a83cfb8e033901f910b424ec7830b5b3" data-og-width="1879" width="1879" data-og-height="964" height="964" data-path="images/messaging-platform/digital-agent-desk/AgentDeskSSO.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/AgentDeskSSO.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=04abf46e0d3efd08d93daff199c5c427 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/AgentDeskSSO.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=cb1ade9ef4308282976862a77f88ff22 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/AgentDeskSSO.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=bf2856be940e57d9e6dce32b03f100ff 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/AgentDeskSSO.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=7cd747751a57e7303fd15d8821b37a0b 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/AgentDeskSSO.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=3bda0631c972ba90bb3da05d12bfc332 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/messaging-platform/digital-agent-desk/AgentDeskSSO.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=4d6920e086c5b61a7913084ceaa9d75d 2500w" />
</Frame>

## Configuring Single Sign-On via SAML

### Environments

ASAPP supports SSO in non-production and production environments. It is strongly recommended that customers configure SSO in both environments as well.

### Exchange of SAML metadata

Both ASAPP and the customer generate their respective SAML metadata and send the metadata files to one another. The metadata will be different for each environment, therefore they need to be generated once per environment.

Sample metadata file content:

```json  theme={null}
<EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
entityID="https://auth.asapp.com/auth/realms/hudson">
    <SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="false"
        protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol
urn:oasis:names:tc:SAML:1.1:protocol http://schemas.xmlsoap.org/ws/2003/07/secext">
    <KeyDescriptor use="encryption">
     <dsig:KeyInfo xmlns:dsig="http://www.w3.org/2000/09/xmldsig#">
      <dsig:KeyName>REDACTED</dsig:KeyName>
      <dsig:X509Data>
       <dsig:X509Certificate>REDACTED</dsig:X509Certificate>
      </dsig:X509Data>
     </dsig:KeyInfo>
    </KeyDescriptor>
 <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
Location="https://auth.asapp.com/auth/realms/hudson/broker/hudson-saml/endpoint"/>
 <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:unspecified
 </NameIDFormat>
 <AssertionConsumerService
      Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
  Location="https://auth.asapp.com/auth/realms/hudson/broker/hudson-saml/endpoint/clients/asapp-saml"
        index="1" isDefault="true" />
     </SPSSODescriptor>
</EntityDescriptor>
```

### SAML Profile Configuration

Next, ASAPP and the customer configures their respective SSO service with each other's SAML profile. This can be achieved by importing the SAML metadata into the SSO service (if it supports a metadata import feature).

### SAML Attributes Configuration

SAML Attributes are key-value fields within the SAML message (also called SAML assertion) that is being sent from the Identity Provider (IDP) to the Service Provider (SP).

ASAPP requires the following fields to be included with the SAML assertion

| **Attribute Name** | **Required** | **Description**                                                                                                                                                                                                                        | **Example**                                 |
| :----------------- | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ |
| userId             | yes          | user's unique identifier used for authentication. Can be a unique readable value such as user's email or an opaque identifier such as a customer's internal user ID.                                                                   | [jdoe@company.com](mailto:jdoe@company.com) |
| firstName          | yes          | user's first name                                                                                                                                                                                                                      | John                                        |
| lastName           | yes          | user's last name                                                                                                                                                                                                                       | Doe                                         |
| nameAlias          | yes          | user's display name. Allows an agent, based on their personal preference or company's privacy policy, to set an alias to show to the customers they are chatting with. If this is not sent then the agent firstName will be displayed. | John Doe                                    |
| roles              | yes          | the roles the user has within the ASAPP platform. Typically mapped to one or more AD Security Groups on the IDP.                                                                                                                       | representative\|manager                     |

The following fields are not **required** but **desired** to further automate the agent Desk configuration:

| **Attribute Name** | **Required** | **Description**                                                                                                                                                                   | **Example**           |
| :----------------- | :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------- |
| groups             | no           | group(s) the user belongs to. This attribute controls the queue(s) that a user is assigned to. Not to be confused with the AD Security Groups (see the **roles** attribute above) | residential\|business |
| concurrency        | no           | number of concurrent chats the user can handle                                                                                                                                    | 5                     |

In addition, any custom fields can be configured in the SAML assertion. See the section below for more details.

### Sending User Data via SAML

ASAPP uses the SAML attribute fields to keep the user data up-to-date in our system. It also allows us to register a new user automatically when a new user logs into the ASAPP application for the first time.

In addition to the required fields that ASAPP needs to identify the user, customers can send additional fields in the SAML assertion that can be used for other purposes such as Reporting. An example can be the Agent Location. These fields are specific per customers. The name and possible values of these fields need to be agreed upon and configured prior to the SAML implementation.

### SSO Testing

SSO testing between the customer and ASAPP must be a coordinated effort due to the nature of the IDP-initiated SSO flow. The customer must provide several user accounts to be used for testing. Generally, the test scenarios are as follows:

1. An agent logs in for the first time. ASAPP observes that a new user record is created and the agent lands on the correct ASAPP application for their role (Desk for a rep, Admin for supervisor/manager).
2. The same agent logs out and logs back in. The agent observes that the correct application still opens.
3. Repeat the same test for another user account, ideally with different roles.

Once testing is completed successfully, then the SSO flow is certified for that environment.

Setting up SSO in the Production environment should follow the same steps.
