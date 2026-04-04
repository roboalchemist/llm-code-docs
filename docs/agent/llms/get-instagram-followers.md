# Source: https://docs.agent.ai/api-reference/get-data/get-instagram-followers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Instagram Followers

> Retrieve a list of top followers from a specified Instagram account for social media analysis.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_instagram_followers
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
  /action/get_instagram_followers:
    post:
      tags:
        - Get Data
      summary: Get Instagram Followers
      description: >-
        Retrieve a list of top followers from a specified Instagram account for
        social media analysis.
      operationId: getInstagramFollowers
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                  description: Instagram username (without @).
                  example: taylorswift
                limit:
                  type: string
                  enum:
                    - '10'
                    - '20'
                    - '50'
                    - '100'
                  default: '20'
                  description: Number of top followers to retrieve.
              required:
                - username
                - limit
      responses:
        '200':
          description: Instagram followers data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  - follower_count: 849
                    full_name: >-
                      ??????????????king Luis h Quezada?????????          Kerlyn
                      Emmanuel ????
                    is_private: false
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/439638964_2316363465224145_7358702140012716031_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=I4q0O90PTfQQ7kNvgEXPteP&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYCvr_ULM1ZFZZ4Q5xBBx39JAA5tZ2NCa6f4VJmv69K4GQ&oe=67B1D67B&_nc_sid=17ea04
                    username: luis_h_quezada
                  - follower_count: 804
                    full_name: Taylor Dundon
                    is_private: false
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/427190453_785616990267306_5959964410039103353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=GH81ZTDpIVsQ7kNvgG0imQT&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYCehOpsDwZJ7CuC09zzBJb-Lcx9aNz4H_kQaRvxFnvAyQ&oe=67B1A5F6&_nc_sid=17ea04
                    username: taydundon
                  - follower_count: 624
                    full_name: Sarah Wise Flanigan
                    is_private: true
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/467394312_534253766174114_4795981361332911272_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=qQ9ce92Gp90Q7kNvgHw3KiX&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYAG1oR0ncYccE-95AkbzJp9X83ruhkP3D5cVagpv5-6ZA&oe=67B1BB93&_nc_sid=17ea04
                    username: blondiewcu22
                  - follower_count: 623
                    full_name: >-
                      ????????????????????????????????
                      ???????????????????????????????????? ????
                    is_private: false
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/465696697_484777051241652_3949279683053664580_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=H_C-dShFchYQ7kNvgHgWcVq&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYAhZGE5UWMlA2wFgXvGzsG-6oXF7yO5aH_fDomP3G8mkw&oe=67B1C377&_nc_sid=17ea04
                    username: gabrielatrewartha
                  - follower_count: 469
                    full_name: '????????'
                    is_private: true
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/472285380_863925555819825_1532714645016929042_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=J1F87DlLjHMQ7kNvgEos1hn&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYCfNwTKMePpPBb6hky6UjqG_x-p1yYM3i_2hz10-iUX_g&oe=67B1D3DF&_nc_sid=17ea04
                    username: jpqdrey
                  - follower_count: 338
                    full_name: eli
                    is_private: false
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/476778299_968818688125317_8971166944851277215_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=MoEFI_rsuroQ7kNvgF4WtDK&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYDT8HW3e-VeOrWsaqki3K9TIc05vxWJCKaMrh450ZuS-g&oe=67B1A9BF&_nc_sid=17ea04
                    username: ems6sx
                  - follower_count: 226
                    full_name: Fairyy
                    is_private: false
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/471821087_9318977181459945_4974290925321805937_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=BbOCPsjJuU8Q7kNvgGV8hZl&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYC0p2duax-SaPyxc32pz8UUy8kTsdAwsZ8B19aL3XT_uQ&oe=67B1B779&_nc_sid=17ea04
                    username: itsfairyy0714
                  - follower_count: 136
                    full_name: Jazmín E.F.
                    is_private: true
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/342547709_1252954485311567_899797009132530988_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=G0lmi9OlG3cQ7kNvgE0XBMv&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYDuNMkT08u4Pm5ixtMl9YOmOpCjei-o4IjgvKIt1ua5Nw&oe=67B1CFE3&_nc_sid=17ea04
                    username: the_dazzler
                  - follower_count: 129
                    full_name: ''
                    is_private: true
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/475458167_1135262874484140_3009195711518212800_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=t_MbLY_aaUsQ7kNvgFfVLMP&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYB5M5sU1jW3lNDmWgpfjyQsCtYP71LuLg75a-nXeSNM0w&oe=67B1C594&_nc_sid=17ea04
                    username: maii.guc
                  - follower_count: 108
                    full_name: Isabela fronza linardi
                    is_private: true
                    is_verified: false
                    profile_pic_url: >-
                      https://scontent-ham3-1.cdninstagram.com/v/t51.2885-19/472214443_512555881165128_5807458048529882114_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-ham3-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2AEdlD42_0XyXTQHQNt24eBgfnByjoniy6CKZGrNS7JRw4XmYjuHuPymQlQH8RnoTG4&_nc_ohc=kGoWsbTQrFwQ7kNvgHEN8FJ&_nc_gid=46de04c42cd84b1095fd5920feb94249&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_AYAlonkyiE4FQGJv1Tc-jYdHCHbScSxAu8NW5IThplwMjg&oe=67B1CC1F&_nc_sid=17ea04
                    username: isa_linardi
        '400':
          description: Instagram followers data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                error: 'Failed to fetch profile: Not found'
                response: null
                status: 400
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