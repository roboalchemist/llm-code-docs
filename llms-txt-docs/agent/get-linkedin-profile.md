# Source: https://docs.agent.ai/api-reference/get-data/get-linkedin-profile.md

# Get LinkedIn Profile

> Retrieve detailed information from a specified LinkedIn profile for professional insights.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_linkedin_profile
paths:
  path: /action/get_linkedin_profile
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              profile_handle:
                allOf:
                  - type: string
                    description: LinkedIn profile handle to retrieve details.
                    example: dharmesh
            required: true
            requiredProperties:
              - profile_handle
        examples:
          example:
            value:
              profile_handle: dharmesh
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response:
                awards: []
                background_image: >-
                  https://media.licdn.com/dms/image/v2/C4E16AQHTt9ikcff1ug/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1610553040149?e=1744848000&v=beta&t=G4AZnkKvbXyhH5QrXyLnT6rH-C8GvCareuLlaaEYAMc
                birth_date: null
                certifications:
                  - authority: HubSpot
                    company:
                      id: null
                      logo: >-
                        https://media.licdn.com/dms/image/v2/C4D0BAQF8H-SLmMDZlA/company-logo_400_400/company-logo_400_400/0/1646683330132/hubspot_logo?e=1747267200&v=beta&t=J096eUo6RubrWAbpGw4f0LX4wqW09zioGtdDCnMLfts
                      name: HubSpot
                      url: null
                    date:
                      end:
                        day: null
                        month: 1
                        year: 2016
                      start:
                        day: null
                        month: 12
                        year: 2014
                    display_source: hubspot.com
                    license_number: null
                    name: Inbound Certification
                    url: http://academy.hubspot.com/certification
                contact_info: null
                courses: []
                education:
                  - date:
                      end:
                        day: null
                        month: 6
                        year: 2006
                      start:
                        day: null
                        month: null
                        year: 2004
                    degree_name: M.S.
                    description: null
                    field_of_study: Management of Technology
                    grade: null
                    school:
                      logo: >-
                        https://media.licdn.com/dms/image/v2/D560BAQH-UXRfIDIKug/company-logo_400_400/company-logo_400_400/0/1689799729035/mit_logo?e=1747267200&v=beta&t=KL3x2aO3w2ZaFnIj2cHddYIaShUHPJjMVtb3quAVF1w
                      name: Massachusetts Institute of Technology
                      url: https://www.linkedin.com/school/mit/
                  - date:
                      end:
                        day: null
                        month: null
                        year: null
                      start:
                        day: null
                        month: null
                        year: null
                    degree_name: B.S.
                    description: null
                    field_of_study: Computer Science
                    grade: null
                    school:
                      logo: >-
                        https://media.licdn.com/dms/image/v2/D560BAQG26bKMbN1kmA/company-logo_400_400/company-logo_400_400/0/1667495412134/uab_logo?e=1747267200&v=beta&t=Xs7Xru1b7O3-BYyHOAq0kV77PtLl0v2RVjj3yWmJ-qo
                      name: University of Alabama at Birmingham
                      url: https://www.linkedin.com/school/uab/
                entity_urn: ACoAAAAKDWUBlFAmXL1HBXFzTLscnoT1eYz66T8
                first_name: Dharmesh
                industry: Computer Software
                influencer: true
                languages:
                  primary_locale:
                    country: US
                    language: en
                  profile_languages:
                    - name: English
                      proficiency: NATIVE_OR_BILINGUAL
                    - name: Gujarati
                      proficiency: NATIVE_OR_BILINGUAL
                  supported_locales:
                    - country: US
                      language: en
                last_name: Shah
                location:
                  city: null
                  country: United States
                  default: Greater Boston
                  short: Greater Boston
                  state: null
                network_info:
                  connections_count: 500
                  followable: true
                  followers_count: 1095314
                object_urn: 658789
                open_to_work: false
                organizations: []
                patents: []
                position_groups:
                  - company:
                      employees:
                        end: 10000
                        start: 5001
                      id: 68529
                      logo: >-
                        https://media.licdn.com/dms/image/v2/C4D0BAQF8H-SLmMDZlA/company-logo_400_400/company-logo_400_400/0/1646683330132/hubspot_logo?e=1747267200&v=beta&t=J096eUo6RubrWAbpGw4f0LX4wqW09zioGtdDCnMLfts
                      name: HubSpot
                      url: https://www.linkedin.com/company/hubspot/
                    date:
                      end:
                        day: null
                        month: null
                        year: null
                      start:
                        day: null
                        month: 6
                        year: 2006
                    profile_positions:
                      - company: HubSpot
                        date:
                          end:
                            day: null
                            month: null
                            year: null
                          start:
                            day: null
                            month: 6
                            year: 2006
                        description: >-
                          Founder of HubSpot, a venture-backed software
                          startup.  HubSpot offers the industry's first inbound
                          marketing system for small businesses.  The software
                          is available as a hosted service (SaaS).
                        employment_type: Full-time
                        location: Cambridge, Massachusetts, United States
                        title: Founder and CTO
                  - company:
                      employees:
                        end: 10
                        start: 2
                      id: 8919615
                      logo: >-
                        https://media.licdn.com/dms/image/v2/C4E0BAQHn3i5C7ghcAg/company-logo_400_400/company-logo_400_400/0/1672773495239/onstartups_com_logo?e=1747267200&v=beta&t=v-TlKplGvP4uJgk1qeQp3LWFNv34YbinML5aO3DF1xc
                      name: OnStartups.com
                      url: https://www.linkedin.com/company/onstartups/
                    date:
                      end:
                        day: null
                        month: null
                        year: null
                      start:
                        day: null
                        month: 11
                        year: 2005
                    profile_positions:
                      - company: OnStartups.com
                        date:
                          end:
                            day: null
                            month: null
                            year: null
                          start:
                            day: null
                            month: 11
                            year: 2005
                        description: >-
                          Popular blog and community for startups with over
                          900,000 subscribers.
                        employment_type: Self-employed
                        location: Boston, Massachusetts, United States
                        title: Founder
                  - company:
                      employees:
                        end: null
                        start: null
                      id: null
                      logo: null
                      name: Pyramid Digital Solutions
                      url: null
                    date:
                      end:
                        day: null
                        month: 8
                        year: 2005
                      start:
                        day: null
                        month: 4
                        year: 1994
                    profile_positions:
                      - company: Pyramid Digital Solutions
                        date:
                          end:
                            day: null
                            month: 8
                            year: 2005
                          start:
                            day: null
                            month: 4
                            year: 1994
                        description: >-
                          Founder and CEO of Pyramid Digital Solutions, an
                          enterprise software startup in the financial services
                          sector.


                          Pyramid was acquired by SunGard Business Systems, an
                          $11 billion technology company, in August, 2005.
                        employment_type: null
                        location: null
                        title: Founder and CEO
                  - company:
                      employees:
                        end: null
                        start: 10001
                      id: 1872
                      logo: >-
                        https://media.licdn.com/dms/image/v2/C4E0BAQFfHmbAR9W5Vg/company-logo_400_400/company-logo_400_400/0/1631327213077?e=1747267200&v=beta&t=ckvcLF4F0lFkuvOQcr0mkz1O7DxdgJljRh0EkLy_tjQ
                      name: SunGard Employee Benefit Systems
                      url: https://www.linkedin.com/company/sungard/
                    date:
                      end:
                        day: null
                        month: 4
                        year: 1994
                      start:
                        day: null
                        month: 4
                        year: 1992
                    profile_positions:
                      - company: SunGard Employee Benefit Systems
                        date:
                          end:
                            day: null
                            month: 4
                            year: 1994
                          start:
                            day: null
                            month: 4
                            year: 1992
                        description: null
                        employment_type: null
                        location: null
                        title: Software Developer
                premium: true
                profile_id: dharmesh
                profile_picture: >-
                  https://media.licdn.com/dms/image/v2/C4E03AQGL2VlL9W53ww/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1516232442184?e=1744848000&v=beta&t=UfjG46VfFYolr_n5m5yzgiPO67Yydg6Q39NwmKqsV_E
                profile_type: personal
                projects: []
                publications:
                  - authors:
                      - first_name: Dharmesh
                        headline: >-
                          Founder and CTO at HubSpot. Helping millions grow
                          better.
                        last_name: Shah
                        name: null
                        type: standardizedContributor
                      - first_name: Brian
                        headline: HubSpot | Sequoia | Propeller Ventures
                        last_name: Halligan
                        name: null
                        type: standardizedContributor
                    date:
                      day: null
                      month: null
                      year: 2009
                    name: Inbound Marketing
                    publisher: United States
                    url: >-
                      http://www.amazon.com/Inbound-Marketing-Found-Google-Social/dp/0470499311/ref=sr_1_1?s=books&ie=UTF8&qid=1399245534&sr=1-1&keywords=inbound+marketing
                related_profiles: []
                skills:
                  - Inbound Marketing
                  - HubSpot Marketing Software
                  - Entrepreneurship
                  - Online Marketing
                  - Start-ups
                  - SaaS
                  - Online Advertising
                  - HubSpot
                  - Marketing
                  - Software Development
                  - SEO
                  - Strategy
                  - Blogging
                  - Business Strategy
                  - Leadership
                  - Web Development
                  - Thought Leadership
                  - Marketing Strategy
                  - Web Analytics
                  - Public Speaking
                sub_title: Founder and CTO at HubSpot. Helping millions grow better.
                summary: >-
                  Career startup guy.


                  Author of the book &quot;Inbound Marketing&quot;
                  (http://InboundBook.com)


                  Specialties: Entrepreneurship, Software Development, internet
                  marketing,SEO
                test_scores: []
                treasury_media: []
                verifications_info: null
                volunteer_experiences: []
        description: LinkedIn profile data
  deprecated: false
  type: path
components:
  schemas: {}

````