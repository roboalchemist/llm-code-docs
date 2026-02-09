# Source: https://docs.agent.ai/api-reference/get-data/get-domain-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Domain Information

> Retrieve detailed information about a domain, including its registration details, DNS records, and more.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/domain_info
openapi: 3.0.0
info:
  version: 1.0.0
  title: AI Actions - Get Data
  description: API specifications for 'Get Data' category AI actions.
  license:
    name: MIT
servers:
  - url: https://api-lr.agent.ai/v1
security:
  - bearerAuth: []
paths:
  /action/domain_info:
    post:
      tags:
        - Get Data
      summary: Get Domain Information
      description: >-
        Retrieve detailed information about a domain, including its registration
        details, DNS records, and more.
      operationId: domainInfo
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                domain:
                  type: string
                  description: Domain name to retrieve information for.
                  example: agent.ai
              required:
                - domain
      responses:
        '200':
          description: >-
            Retrieve detailed information about a domain, including its
            registration details, DNS records, and more.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  administrative_contact:
                    city: Belmont
                    country_code: US
                    country_name: United States
                    email_address: dshah@hubspot.com
                    name: Dharmesh Shah
                    phone: '+16178559195'
                    state: Massachusetts
                    street: 9 Sumner lane,
                    zip_code: '02478'
                  create_date: '2017-12-16'
                  domain_name: agent.ai
                  domain_registered: 'yes'
                  domain_registrar:
                    email_address: abuse@1api.net
                    iana_id: '1387'
                    phone_number: '+4968949396850'
                    registrar_name: 1API GmbH
                    website_url: http://www.1api.net
                    whois_server: whois.1api.net
                  domain_status:
                    - clienttransferprohibited
                  expiry_date: '2026-06-01'
                  name_servers:
                    - garret.ns.cloudflare.com
                    - kate.ns.cloudflare.com
                  query_time: '2025-02-21 01:28:18'
                  registrant_contact:
                    city: Belmont
                    country_code: US
                    country_name: United States
                    email_address: dshah@hubspot.com
                    name: Dharmesh Shah
                    phone: '+16178559195'
                    state: Massachusetts
                    street: 9 Sumner lane,
                    zip_code: '02478'
                  status: true
                  technical_contact:
                    city: Belmont
                    country_code: US
                    country_name: United States
                    email_address: dshah@hubspot.com
                    name: Dharmesh Shah
                    phone: '+16178559195'
                    state: Massachusetts
                    street: 9 Sumner lane,
                    zip_code: '02478'
                  update_date: '2025-01-18'
                  whois_raw_domain: >-

                    Domain Name: agent.ai

                    Registry Domain ID: 7d34491dec624bf292b0c8a501b0d7dc-DONUTS

                    Registrar WHOIS Server: whois.1api.net

                    Registrar URL: http://www.1api.net

                    Updated Date: 2025-01-18T21:06:24Z

                    Creation Date: 2017-12-16T03:43:49Z

                    Registry Expiry Date: 2026-06-01T03:43:49Z

                    Registrar: 1API GmbH

                    Registrar IANA ID: 1387

                    Registrar Abuse Contact Email: abuse@1api.net

                    Registrar Abuse Contact Phone: +49.68949396850

                    Domain Status: clientTransferProhibited
                    https://icann.org/epp#clientTransferProhibited

                    Registry Registrant ID:
                    03be967cfdf84f39a51f6bf3c4c40951-DONUTS

                    Registrant Name: Dharmesh Shah

                    Registrant Organization: 

                    Registrant Street: 9 Sumner lane,

                    Registrant City: Belmont

                    Registrant State/Province: Massachusetts

                    Registrant Postal Code: 02478

                    Registrant Country: US

                    Registrant Phone: +1.6178559195

                    Registrant Phone Ext: 

                    Registrant Fax: 

                    Registrant Fax Ext: 

                    Registrant Email: dshah@hubspot.com

                    Registry Admin ID: 03be967cfdf84f39a51f6bf3c4c40951-DONUTS

                    Admin Name: Dharmesh Shah

                    Admin Organization: 

                    Admin Street: 9 Sumner lane,

                    Admin City: Belmont

                    Admin State/Province: Massachusetts

                    Admin Postal Code: 02478

                    Admin Country: US

                    Admin Phone: +1.6178559195

                    Admin Phone Ext: 

                    Admin Fax: 

                    Admin Fax Ext: 

                    Admin Email: dshah@hubspot.com

                    Registry Tech ID: 03be967cfdf84f39a51f6bf3c4c40951-DONUTS

                    Tech Name: Dharmesh Shah

                    Tech Organization: 

                    Tech Street: 9 Sumner lane,

                    Tech City: Belmont

                    Tech State/Province: Massachusetts

                    Tech Postal Code: 02478

                    Tech Country: US

                    Tech Phone: +1.6178559195

                    Tech Phone Ext: 

                    Tech Fax: 

                    Tech Fax Ext: 

                    Tech Email: dshah@hubspot.com

                    Name Server: kate.ns.cloudflare.com

                    Name Server: garret.ns.cloudflare.com

                    DNSSEC: unsigned

                    URL of the ICANN Whois Inaccuracy Complaint Form:
                    https://www.icann.org/wicf/

                    >>> Last update of WHOIS database: 2025-02-21T01:28:17Z <<<


                    For more information on Whois status codes, please visit
                    https://icann.org/epp


                    Terms of Use: Access to WHOIS information is provided to
                    assist persons in determining the contents of a domain name
                    registration record in the registry database. The data in
                    this record is provided by Identity Digital or the Registry
                    Operator for informational purposes only, and accuracy is
                    not guaranteed. This service is intended only for
                    query-based access. You agree that you will use this data
                    only for lawful purposes and that, under no circumstances
                    will you use this data to (a) allow, enable, or otherwise
                    support the transmission by e-mail, telephone, or facsimile
                    of mass unsolicited, commercial advertising or solicitations
                    to entities other than the data recipient's own existing
                    customers; or (b) enable high volume, automated, electronic
                    processes that send queries or data to the systems of
                    Registry Operator, a Registrar, or Identity Digital except
                    as reasonably necessary to register domain names or modify
                    existing registrations. When using the Whois service, please
                    consider the following: The Whois service is not a
                    replacement for standard EPP commands to the SRS service.
                    Whois is not considered authoritative for registered domain
                    objects. The Whois service may be scheduled for downtime
                    during production or OT&E maintenance periods. Queries to
                    the Whois services are throttled. If too many queries are
                    received from a single IP address within a specified time,
                    the service will begin to reject further queries for a
                    period of time to prevent disruption of Whois service
                    access. Abuse of the Whois system through data mining is
                    mitigated by detecting and limiting bulk query access from
                    single sources. Where applicable, the presence of a
                    [Non-Public Data] tag indicates that such data is not made
                    publicly available due to applicable data privacy laws or
                    requirements. Should you wish to contact the registrant,
                    please refer to the Whois records available through the
                    registrar URL listed above. Access to non-public data may be
                    provided, upon request, where it can be reasonably confirmed
                    that the requester holds a specific legitimate interest and
                    a proper legal basis for accessing the withheld data. Access
                    to this data provided by Identity Digital can be requested
                    by submitting a request via the form found at
                    https://www.identity.digital/about/policies/whois-layered-access/.
                    The Registrar of Record identified in this output may have
                    an RDDS service that can be queried for additional
                    information on how to contact the Registrant, Admin, or Tech
                    contact of the queried domain name. Identity Digital Inc.
                    and Registry Operator reserve the right to modify these
                    terms at any time. By submitting this query, you agree to
                    abide by this policy.
                  whois_server: whois.nic.ai
components:
  schemas:
    ActionResponse:
      type: object
      properties:
        status:
          type: integer
          format: int32
          description: HTTP status code of the action response
        response:
          type: object
          description: Response data from the action
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer token from your account
        ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))

````