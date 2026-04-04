# Source: https://docs.agent.ai/api-reference/get-data/enrich-company-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Enrich Company Data

> Gather enriched company data using Breeze Intelligence for deeper analysis and insights.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_company_object
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
  /action/get_company_object:
    post:
      tags:
        - Get Data
      summary: Enrich Company Data
      description: >-
        Gather enriched company data using Breeze Intelligence for deeper
        analysis and insights.
      operationId: getCompanyObject
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                domain:
                  type: string
                  description: Domain of the company to retrieve enriched data.
                  example: hubspot.com
              required:
                - domain
      responses:
        '200':
          description: Enriched company data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  category:
                    gicsCode: '50201010'
                    industry: Media
                    industryGroup: Media
                    naics6Codes:
                      - '541810'
                    naics6Codes2022:
                      - '541810'
                    naicsCode: '54'
                    sector: Consumer Discretionary
                    sic4Codes:
                      - '7311'
                    sicCode: '73'
                    subIndustry: Advertising
                  crunchbase:
                    handle: organization/hubspot
                  description: >-
                    HubSpot provides a comprehensive cloud-based CRM platform
                    that integrates marketing, sales, service, and operations
                    tools to help businesses attract, engage, and delight
                    customers effectively.
                  domain: hubspot.com
                  domainAliases:
                    - hubspot.org.cn
                    - inboundstack.co
                    - hubspot.com.my
                    - hubspot.hk
                    - growthqa.org
                    - hubspot.com.hk
                    - meetme.cc
                    - hubspot.sg
                    - hubspot.com.tw
                    - hsappstatic.net
                    - hubspotcms.com
                    - hubspot.co.in
                    - hubspot.ie
                    - hubspot.nz
                    - smallbusinesshub.com
                    - inboundrank.co.uk
                    - thegrowthshow.com
                    - oneforty.com
                    - performable.com
                    - socialinbox.com
                    - stateofinbound.com
                    - wwwhubspot.com
                    - growth.org
                    - inboundstack.io
                    - culturecode.com
                    - hubspot.my
                    - chatspot.ai
                    - hubspot.app
                    - hubspot.net
                    - chatspot.com
                    - performable.net
                    - twittergrader.com
                    - hubspot.me
                    - makemypersona.com
                    - hubspot.ae
                    - hubspot.ee
                    - hubspot.tw
                    - hubspot.com.au
                    - hubspot.co.uk
                    - hscrmemail.com
                    - hubspot.org
                    - hubspot.kr
                    - hubspot.co
                    - hubspot.au
                    - hubspot.com.sg
                    - hubspot.ai
                    - hubspot.co.kr
                    - hubspot.gr
                    - sidekickforbusiness.com
                    - hubspot.net.cn
                    - customercode.com
                    - per.fm
                    - hubspot.io
                    - hubspot.pl
                    - hubspot.nl
                    - flubspot.com
                    - hubspot.co.nz
                    - stateofinboundmarketing.com
                    - cms.dev
                    - hubspots.com
                    - hubspot.store
                    - hubspot.si
                    - hubspot.ca
                    - hubspot.us
                    - inboundhub.com
                    - hubspot.co.id
                    - hs-sites.com
                  emailProvider: false
                  facebook:
                    handle: hubspot
                    likes: 1486705
                  foundedYear: 2006
                  geo:
                    city: Cambridge
                    country: United States
                    countryCode: US
                    lat: 42.3697647
                    lng: -71.0773545
                    postalCode: '02141'
                    state: Massachusetts
                    stateCode: MA
                    streetAddress: '25 First Street #2nd Floor'
                    streetName: First Street
                    streetNumber: '25'
                    subPremise: 2nd Floor
                  id: 54eddb27-988d-42a4-8688-59386edfc5bf
                  identifiers:
                    usCIK: '0001404655'
                    usEIN: null
                  indexedAt: '2025-02-07T23:06:26.171Z'
                  legalName: HubSpot, Inc.
                  linkedin:
                    handle: company/hubspot
                  location: 25 First St 2nd Floor, Cambridge, MA 02141, USA
                  logo: https://logo.clearbit.com/hubspot.com
                  metrics:
                    alexaGlobalRank: 230
                    alexaUsRank: 133
                    annualRevenue: 1730000000
                    employees: 7433
                    employeesRange: 5K-10K
                    estimatedAnnualRevenue: $1B-$10B
                    fiscalYearEnd: 12
                    marketCap: 3200000000
                    raised: null
                    trafficRank: very_high
                  name: HubSpot
                  parent:
                    domain: null
                  phone: +1 888-482-7768
                  site:
                    emailAddresses:
                      - media@hubspot.com
                      - memunroe@hubspot.com
                    phoneNumbers:
                      - +1 888-482-7768
                      - +1 857-829-5064
                      - +49 30 208486000
                      - +49 30 217998000
                      - +353 1 518 7500
                      - +32 9 320 03 70
                      - +32 9 320 03 50
                      - +31 20 200 3299
                      - +33 1 72 73 05 00
                      - +33 1 72 73 06 44
                  tags:
                    - Information Technology & Services
                    - Advertising
                    - Advertising Management
                    - Media
                    - Professional Services
                    - Agency
                    - Technology
                    - SAAS
                    - B2B
                  tech:
                    - cloud_flare
                    - hubspot
                    - facebook_connect
                    - twitter_button
                    - vidyard
                    - db2
                    - smartsheet
                    - sybase
                    - apache_kafka
                    - sage_50cloud
                    - splunk
                    - stripe
                    - appnexus
                    - wrike
                    - couchbase
                    - dropbox
                    - workamajig
                    - workday
                    - qliktech
                    - thomson_reuters_eikon
                    - tibco_spotfire
                    - oracle_data_integrator
                    - trello
                    - ibm_websphere
                    - sap_concur
                    - xero
                    - rabbitmq
                    - cision
                    - apache_hadoop
                    - couchdb
                    - dstillery
                    - oracle_business_intelligence
                    - aws_dynamodb
                    - oracle_weblogic
                    - netsuite
                    - atlassian_confluence
                    - kentico
                    - microsoft_dynamics
                    - hootsuite
                    - quickbooks
                    - sap_crystal_reports
                    - oracle_peoplesoft
                    - apache_tomcat
                    - hbase
                    - basecamp
                    - informatica
                    - okta
                    - mongodb
                    - microsoft_project
                    - ibm_cognos
                    - alteryx
                    - pentaho
                    - sap_sales_order_management
                    - jaspersoft
                    - apache_spark
                    - rubicon_project
                    - sprinklr
                    - qlikview
                    - meltwater
                    - aws_redshift
                    - teradata
                    - aws_lambda
                    - sage_intacct
                    - github
                    - rsa_securid
                    - sap_business_objects
                    - microstrategy
                    - oracle_fusion
                    - sap_hana
                    - oracle_essbase
                    - unbounce
                    - liferay
                    - talend
                    - twilio
                    - microsoft_sql_server
                    - postgresql
                    - gotomeeting
                    - mysql
                    - windows_server
                    - snowflake
                    - bamboohr
                    - adobe_marketing_cloud
                    - invoca
                    - paychex
                    - microsoft_power_bi
                    - aws_iam
                    - factset
                    - atlassian_jira
                    - oracle_hyperion
                    - neo4j
                    - hive
                    - filemaker_pro
                    - apache_cassandra
                  techCategories:
                    - dns
                    - marketing_automation
                    - authentication_services
                    - social_sharing
                    - image_video_services
                    - database
                    - crm
                    - productivity
                    - data_processing
                    - accounting_and_finance
                    - payment
                    - advertising
                    - project_management_software
                    - human_capital_management
                    - analytics
                    - data_management
                    - web_servers
                    - business_management
                    - content_management_system
                    - security
                    - data_visualization
                    - cloud_computing_services
                  ticker: HUBS
                  timeZone: America/New_York
                  twitter:
                    avatar: >-
                      https://pbs.twimg.com/profile_images/1500923494665797632/VytKgxOP_normal.jpg
                    bio: >-
                      HubSpot CRM 🤠 Helping you win the wild west of business
                      🏜
                    followers: 829213
                    following: 41922
                    handle: HubSpot
                    id: '14458280'
                    location: Cambridge, MA
                    site: https://t.co/HsUDbNAh5W
                  type: public
                  ultimateParent:
                    domain: null
                  utcOffset: -5
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