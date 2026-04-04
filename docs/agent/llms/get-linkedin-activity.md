# Source: https://docs.agent.ai/api-reference/get-data/get-linkedin-activity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get LinkedIn Activity

> Retrieve recent LinkedIn posts from specified profiles to analyze professional activity and engagement.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_linkedin_activity
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
  /action/get_linkedin_activity:
    post:
      tags:
        - Get Data
      summary: Get LinkedIn Activity
      description: >-
        Retrieve recent LinkedIn posts from specified profiles to analyze
        professional activity and engagement.
      operationId: getLinkedinActivity
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                profile_urls:
                  type: string
                  format: textarea
                  description: LinkedIn profile URLs, one per line.
                  example: https://linkedin.com/in/dharmesh
                num_posts:
                  type: integer
                  format: int64
                  enum:
                    - 1
                    - 5
                    - 10
                    - 25
                    - 50
                    - 100
                  default: 3
                  description: Number of recent posts to fetch from each profile.
              required:
                - profile_urls
                - num_posts
      responses:
        '200':
          description: LinkedIn activity data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  dharmesh:
                    post_count: 3
                    posts:
                      - activity_id: urn:li:activity:7295218047521349632
                        attachments: []
                        author:
                          background_image: null
                          entity_urn: ACoAAAAKDWUBlFAmXL1HBXFzTLscnoT1eYz66T8
                          first_name: Dharmesh
                          last_name: Shah
                          object_urn: 658789
                          profile_id: dharmesh
                          profile_picture: >-
                            https://media.licdn.com/dms/image/v2/C4E03AQGL2VlL9W53ww/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1516232442184?e=1744848000&v=beta&t=UfjG46VfFYolr_n5m5yzgiPO67Yydg6Q39NwmKqsV_E
                          profile_type: personal
                          sub_title: >-
                            Founder and CTO at HubSpot. Helping millions grow
                            better.
                        commentary: >-
                          "I self-identify as an engineer. Even when I was
                          co-CEO of Salesforce, I was still coding on the
                          weekends."


                          ~ Bret Taylor (Google Maps, FriendFeed, Meta,
                          Salesforce, and now Sierra AI)


                          ---

                          Bret is one of the people I most look up to and
                          admire.


                          He doesn't know me, but I feel like I know him. I have
                          watched hours and hours of his online appearances.
                          Some of them multiple times.


                          He's built great products, great teams and a great
                          legacy. 


                          I love both his values and his vibe. 


                          When I grow up, I want to be a wee bit more like Bret.


                          #goals
                        header_text: null
                        li_url: >-
                          https://www.linkedin.com/posts/dharmesh_goals-activity-7295218047521349632-pcYG?utm_source=combined_share_message&utm_medium=member_ios&rcm=ACoAAFewJzYBzxg3UoUGLhXJD4lGmMAqv_RQdpE
                        num_comments: 22
                        num_reactions: 362
                        num_shares: 3
                        reaction_breakdown:
                          appreciation: 2
                          empathy: 50
                          entertainment: 2
                          interest: 4
                          like: 280
                          praise: 24
                        reshared_activity_details: null
                        time_elapsed: 45 minutes ago
                      - activity_id: urn:li:activity:7295126465598181376
                        attachments: []
                        author:
                          background_image: null
                          entity_urn: ACoAAAAKDWUBlFAmXL1HBXFzTLscnoT1eYz66T8
                          first_name: Dharmesh
                          last_name: Shah
                          object_urn: 658789
                          profile_id: dharmesh
                          profile_picture: >-
                            https://media.licdn.com/dms/image/v2/C4E03AQGL2VlL9W53ww/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1516232442184?e=1744848000&v=beta&t=UfjG46VfFYolr_n5m5yzgiPO67Yydg6Q39NwmKqsV_E
                          profile_type: personal
                          sub_title: >-
                            Founder and CTO at HubSpot. Helping millions grow
                            better.
                        commentary: >-
                          Many seem to still be hung up on the debate of what is
                          or isn't an agent. Do they need to be autonomous? Do
                          they have to have full "agency"?


                          Here's my simple take:


                          This is not a binary thing, it's a spectrum. Software
                          (which is what agents are) can be less agentic or more
                          agentic. 


                          I find it helpful to classify the agents into
                          different types:


                          1) Conversational/Chat Agents: These are agents that
                          are interacted with in some type of conversational
                          interface (like chat).  @HubSpot's Customer Agent is
                          an example. It's an agent that handles queries from a
                          company's customers in a chat UX. 


                          2) Workflow Agents: These execute a set of steps to
                          accomplish a goal. AI is involved at one or more steps
                          (LLMs, image generation, data analysis etc.) For now,
                          the steps are commonly predefined, but they can also
                          be determined by an LLM-powered "orchestrator" (I
                          think of it as a manager that coordinates the work). 
                          They can be triggered manually, on a schedule or by a
                          trigger in response to some external event (like a new
                          prospect being added to the CRM).


                          Many of the 700+ agents on Agent.ai are workflow
                          agents.


                          3) Hybrid Agents: These are app-like agents and use a
                          mix of Chat UX and classic UI (like buttons, text
                          fields and dropdowns). They can run for a while, pause
                          for user input or approval. They can send a
                          notification when work is complete. 


                          Most of the 700+ agents on Agent.ai are these
                          Hybrid/app agents.


                          Things the different types of agents share in common:


                          1) They usually use one or more LLMs for some portion
                          of their work. 


                          2) The LLMs are given access to a library of "tools"
                          in order for them to access data (often via APIs) or
                          take action and do things.


                          3) They have some notion of "memory" -- at a minimum
                          during the time an agent is running, but increasingly,
                          across multiple agent interactions and ideally across
                          all the agents in a system. 


                          In the future, I'm hoping there will be an additional
                          feature:


                          4) Agents will be able to discover each other and
                          collaborate to accomplish higher-order goals. 


                          So, given all of that, I'd define agents today like
                          this:

                          AGENTS: Software that uses AI to accomplish a goal
                          requiring multiple predetermined or AI-generated
                          steps. 


                          No matter how you define them or classify them, the
                          result is the same: Agents should be useful to humans
                          and help us work better.


                          Now, back to building agents...and helping others
                          build theirs.
                        header_text: null
                        li_url: >-
                          https://www.linkedin.com/posts/dharmesh_many-seem-to-still-be-hung-up-on-the-debate-activity-7295126465598181376-IZ7i?utm_source=combined_share_message&utm_medium=member_ios&rcm=ACoAAFewJzYBzxg3UoUGLhXJD4lGmMAqv_RQdpE
                        num_comments: 72
                        num_reactions: 476
                        num_shares: 27
                        reaction_breakdown:
                          appreciation: 1
                          empathy: 19
                          interest: 53
                          like: 396
                          praise: 7
                        reshared_activity_details: null
                        time_elapsed: 6 hours ago
                      - activity_id: urn:li:activity:7294951434633052160
                        attachments: []
                        author:
                          background_image: null
                          entity_urn: ACoAAAAKDWUBlFAmXL1HBXFzTLscnoT1eYz66T8
                          first_name: Dharmesh
                          last_name: Shah
                          object_urn: 658789
                          profile_id: dharmesh
                          profile_picture: >-
                            https://media.licdn.com/dms/image/v2/C4E03AQGL2VlL9W53ww/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1516232442184?e=1744848000&v=beta&t=UfjG46VfFYolr_n5m5yzgiPO67Yydg6Q39NwmKqsV_E
                          profile_type: personal
                          sub_title: >-
                            Founder and CTO at HubSpot. Helping millions grow
                            better.
                        commentary: >-
                          A long time ago when starting HubSpot and figuring out
                          SEO (Search Engine Optimization), I learned that the
                          best way to rank in Google was to be rank-worthy.
                          Create the web page that *should* rank compared to the
                          alternatives.  


                          Over time what should rank does rank. 


                          Today, I came across this old Charlie Munger quote
                          that captured this idea brilliantly: 


                          "The best way to get what you want is to deserve what
                          you want."
                        header_text: null
                        li_url: >-
                          https://www.linkedin.com/posts/dharmesh_a-long-time-ago-when-starting-hubspot-and-activity-7294951434633052160-kr0N?utm_source=combined_share_message&utm_medium=member_ios&rcm=ACoAAFewJzYBzxg3UoUGLhXJD4lGmMAqv_RQdpE
                        num_comments: 70
                        num_reactions: 728
                        num_shares: 8
                        reaction_breakdown:
                          appreciation: 3
                          empathy: 77
                          entertainment: 1
                          interest: 14
                          like: 612
                          praise: 21
                        reshared_activity_details: null
                        time_elapsed: 18 hours ago
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