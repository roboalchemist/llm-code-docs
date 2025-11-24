# Source: https://docs.agent.ai/api-reference/agent-discovery/search.md

# Search

> Search and discover agents based on various criteria including status, tags, and search terms.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/search
paths:
  path: /action/search
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
              query:
                allOf:
                  - type: string
                    description: Text to search for in agent names and descriptions.
                    example: content generation
              status:
                allOf:
                  - type: string
                    description: Filter agents by their visibility status.
                    enum:
                      - public
                      - private
                      - team
                      - all
                    default: public
                    example: public
              limit:
                allOf:
                  - type: integer
                    description: Maximum number of agents to return (capped at 100).
                    default: 10
                    minimum: 1
                    maximum: 100
                    example: 20
              page:
                allOf:
                  - type: integer
                    description: Page number for pagination (0-indexed).
                    default: 0
                    minimum: 0
                    example: 0
            required: true
        examples:
          example:
            value:
              query: content generation
              status: public
              limit: 20
              page: 0
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
              response:
                - type: function
                  function:
                    name: invoke_agent_6bf8p9clio50t5cy
                    description: >-
                      Invoke agent "Social Media Post Generator": Creates
                      engaging social media posts tailored to specific platforms
                      and target audiences to boost engagement and brand
                      awareness.
                    metadata:
                      id: 6bf8p9clio50t5cy
                      slug: null
                      icon: /icons/copywriting.svg
                      name: Social Media Post Generator
                      description: >-
                        Creates engaging social media posts tailored to specific
                        platforms and target audiences to boost engagement and
                        brand awareness.
                      status: public
                      type: studio
                      executions: 12203
                      reviews_count: 346
                      reviews_score: 4.23
                      created_at: Fri, 13 Sep 2024 14:23:19 GMT
                      updated_at: Wed, 24 Sep 2025 15:09:47 GMT
                      score: 0.6715
                    parameters:
                      type: object
                      properties:
                        message_content:
                          type: string
                          description: 'Enter the main message or content you want to share:'
                        platform:
                          type: string
                          description: 'Select the social media platform:'
                          enum:
                            - Facebook
                            - Twitter
                            - LinkedIn
                            - Instagram
                      required:
                        - message_content
                        - platform
                      additionalProperties: false
                    strict: true
                - type: function
                  function:
                    name: invoke_agent_lt8gzzc4s59qym06
                    description: >-
                      Invoke agent "Video Script Generator": Creates engaging
                      scripts for various types of video content, such as
                      explainer videos, product demos, and promotional videos.
                      Assists content creators, marketers, and educators by
                      automating the scriptwriting process, saving time and
                      ensuring consistently high-quality output.
                    metadata:
                      id: lt8gzzc4s59qym06
                      slug: lt8gzzc4s59qym06
                      icon: /icons/youtube2.svg
                      name: Video Script Generator
                      description: >-
                        Creates engaging scripts for various types of video
                        content, such as explainer videos, product demos, and
                        promotional videos. Assists content creators, marketers,
                        and educators by automating the scriptwriting process,
                        saving time and ensuring consistently high-quality
                        output.
                      status: public
                      type: studio
                      executions: 110052
                      reviews_count: 2282
                      reviews_score: 4.21
                      created_at: Fri, 04 Oct 2024 16:31:07 GMT
                      updated_at: Wed, 24 Sep 2025 21:42:38 GMT
                      score: 0.6599
                    parameters:
                      type: object
                      properties:
                        input_video_content_type:
                          type: string
                          description: Video Content Type *
                          enum:
                            - Explainer Video
                            - Product Demo
                            - Tutorial/How-To
                            - Promotional/Advertisement
                            - Educational/Lecture
                            - Trailer (for movies, games, events)
                            - Podcast-style discussion
                        input_video_topic:
                          type: string
                          description: Video Topic *
                        input_audience_information:
                          type: string
                          description: Audience Information *
                        input_key_messages:
                          type: string
                          description: Key Messages * (one per line)
                        input_desired_video_length:
                          type: string
                          description: Desired Video Length*
                          default: 30 seconds
                          enum:
                            - 10 seconds
                            - 30 seconds
                            - 60 seconds
                            - 3 minutes
                            - 5+ minutes
                        input_tone:
                          type: string
                          description: Tone
                          enum:
                            - Casual
                            - Funny
                            - Professional
                        input_competitor_content:
                          type: string
                          description: Competitor/Reference Content URL (YouTube)
                        input_visual_theme_suggestions:
                          type: string
                          description: Visual Theme Suggestions (Keywords to guide visuals)
                      required:
                        - input_video_content_type
                        - input_video_topic
                        - input_audience_information
                        - input_key_messages
                        - input_desired_video_length
                      additionalProperties: false
                    strict: true
                - type: function
                  function:
                    name: invoke_agent_zy06i5o3s2ygay29
                    description: >-
                      Invoke agent "Trending Content Idea Generator": Provides
                      content topic ideas based on target keywords and current
                      trends to boost engagement and SEO performance.
                    metadata:
                      id: zy06i5o3s2ygay29
                      slug: null
                      icon: /icons/copywriting.svg
                      name: Trending Content Idea Generator
                      description: >-
                        Provides content topic ideas based on target keywords
                        and current trends to boost engagement and SEO
                        performance.
                      status: public
                      type: studio
                      executions: 5130
                      reviews_count: 156
                      reviews_score: 4.38
                      created_at: Fri, 13 Sep 2024 14:12:01 GMT
                      updated_at: Wed, 24 Sep 2025 21:35:55 GMT
                      score: 0.652
                    parameters:
                      type: object
                      properties:
                        primary_keyword:
                          type: string
                          description: 'Enter your primary keyword or topic:'
                      required:
                        - primary_keyword
                      additionalProperties: false
                    strict: true
                - type: function
                  function:
                    name: invoke_agent_0frbzoamzb733wh2
                    description: >-
                      Invoke agent "Fit to purpose image generator": This
                      specialized Image Generation agent guides users through a
                      series of targeted prompts to capture all essential image
                      parameters: theme, text content, featured objects, color
                      palette, and visual style. By methodically gathering these
                      creative specifications through an intuitive interface,
                      the agent eliminates the complexity typically associated
                      with image creation. Once all parameters are collected,
                      the agent seamlessly processes these inputs through
                      advanced generative AI models to produce images that
                      precisely match user intent.
                    metadata:
                      id: 0frbzoamzb733wh2
                      slug: fit_to_purpose_image_generator
                      icon: /icons/generative-image.svg
                      name: Fit to purpose image generator
                      description: >-
                        This specialized Image Generation agent guides users
                        through a series of targeted prompts to capture all
                        essential image parameters: theme, text content,
                        featured objects, color palette, and visual style. By
                        methodically gathering these creative specifications
                        through an intuitive interface, the agent eliminates the
                        complexity typically associated with image creation.
                        Once all parameters are collected, the agent seamlessly
                        processes these inputs through advanced generative AI
                        models to produce images that precisely match user
                        intent.
                      status: public
                      type: studio
                      executions: 94448
                      reviews_count: 2316
                      reviews_score: 4.2
                      created_at: Wed, 04 Dec 2024 22:59:27 GMT
                      updated_at: Wed, 24 Sep 2025 18:05:25 GMT
                      score: 0.6445
                    parameters:
                      type: object
                      properties:
                        out_theme:
                          type: string
                          description: Enter the theme of the image
                        out_text:
                          type: string
                          description: 'Enter text you want to be in the image '
                        out_objects:
                          type: string
                          description: Enter a list of objects you want in the image
                        out_color:
                          type: string
                          description: Enter the colors you want in the image
                        out_style:
                          type: string
                          description: Enter the style of the image
                      required:
                        - out_theme
                        - out_text
                        - out_objects
                        - out_color
                        - out_style
                      additionalProperties: false
                    strict: true
                - type: function
                  function:
                    name: invoke_agent_0lbxuj5hbhz5iy0e
                    description: >-
                      Invoke agent "Video to blog generator": Generate highly
                      engaging articles and blog posts using our Video to blog
                      AI agent. This intelligent agent seamlessly converts
                      videos such as YouTube videos into high-quality,
                      well-structured blogs, articles, and summaries.


                      Key Features:


                      Effortless Content Creation: Extract the essence of any
                      video and turn it into polished written content in
                      seconds.


                      SEO-Optimized Output: Boost your online presence with
                      articles crafted to rank higher in search engines. You can
                      provide it the keywords you are targeting and it will do
                      it's magic.


                      Customizable Tone and Style: Whether you prefer
                      professional, conversational, or creative writing, tailor
                      the output to match your unique voice.


                      Enhanced Accessibility: Make your video insights
                      accessible to a broader audience, including readers who
                      prefer written content.


                      Time-Saving Automation: Streamline your workflow and focus
                      on strategy while the AI handles the heavy lifting.


                      Perfect for bloggers, marketers, and content creators,
                      this AI agent bridges the gap between video and text,
                      helping you expand your reach and engage with your
                      audience like never before.
                    metadata:
                      id: 0lbxuj5hbhz5iy0e
                      slug: video-to-blog
                      icon: /icons/video-marketing.svg
                      name: Video to blog generator
                      description: >-
                        Generate highly engaging articles and blog posts using
                        our Video to blog AI agent. This intelligent agent
                        seamlessly converts videos such as YouTube videos into
                        high-quality, well-structured blogs, articles, and
                        summaries.


                        Key Features:


                        Effortless Content Creation: Extract the essence of any
                        video and turn it into polished written content in
                        seconds.


                        SEO-Optimized Output: Boost your online presence with
                        articles crafted to rank higher in search engines. You
                        can provide it the keywords you are targeting and it
                        will do it's magic.


                        Customizable Tone and Style: Whether you prefer
                        professional, conversational, or creative writing,
                        tailor the output to match your unique voice.


                        Enhanced Accessibility: Make your video insights
                        accessible to a broader audience, including readers who
                        prefer written content.


                        Time-Saving Automation: Streamline your workflow and
                        focus on strategy while the AI handles the heavy
                        lifting.


                        Perfect for bloggers, marketers, and content creators,
                        this AI agent bridges the gap between video and text,
                        helping you expand your reach and engage with your
                        audience like never before.
                      status: public
                      type: studio
                      executions: 555
                      reviews_count: 41
                      reviews_score: 4.27
                      created_at: Tue, 14 Jan 2025 18:48:02 GMT
                      updated_at: Wed, 24 Sep 2025 22:32:35 GMT
                      score: 0.6229
                    parameters:
                      type: object
                      properties:
                        youtube_url:
                          type: string
                          description: Please enter a YouTube url
                          default: https://www.youtube.com/watch?v=IKy-oKy0Sns
                        seo_target_keyword:
                          type: string
                          description: Are you targeting a specific keyword or phrase?
                      required:
                        - youtube_url
                        - seo_target_keyword
                      additionalProperties: false
                    strict: true
                - type: function
                  function:
                    name: invoke_agent_nviyovw4ww4i7bsj
                    description: >-
                      Invoke agent "Website Generator": Launch a professional
                      site fast with B12.io’s AI Website Builder – no code, no
                      design skills needed.


                      Need to build a website, create your first business site,
                      or launch a startup online?

                      This tool helps you generate an entire website using AI —
                      from structure and branding to content and forms.


                      What You Can Create:

                          Full business websites

                          AI-powered multi-page sites

                          No-code websites for startups and SMBs

                          Online presence for services, portfolios, and consultants

                          Contact forms and built-in scheduling tools

                          Conversion-ready homepage and service pages

                      What This Tool Can Help You Do:

                          Build website in minutes using AI

                          Create your site from a simple prompt

                          Generate homepage sections, navigation, and content

                          Design a site that matches your brand

                          Publish quickly without developers or designers

                      Why It Works:

                          Trusted by over 2 million users

                          Combines AI design, AI copywriting, and web publishing

                          Perfect for non-technical founders, marketers, freelancers, and business owners

                      Want to build and launch a polished website today?

                      Try B12.io — and let AI do the heavy lifting.
                    metadata:
                      id: nviyovw4ww4i7bsj
                      slug: website-generator
                      icon: /icons/website.svg
                      name: Website Generator
                      description: >-
                        Launch a professional site fast with B12.io’s AI Website
                        Builder – no code, no design skills needed.


                        Need to build a website, create your first business
                        site, or launch a startup online?

                        This tool helps you generate an entire website using AI
                        — from structure and branding to content and forms.


                        What You Can Create:

                            Full business websites

                            AI-powered multi-page sites

                            No-code websites for startups and SMBs

                            Online presence for services, portfolios, and consultants

                            Contact forms and built-in scheduling tools

                            Conversion-ready homepage and service pages

                        What This Tool Can Help You Do:

                            Build website in minutes using AI

                            Create your site from a simple prompt

                            Generate homepage sections, navigation, and content

                            Design a site that matches your brand

                            Publish quickly without developers or designers

                        Why It Works:

                            Trusted by over 2 million users

                            Combines AI design, AI copywriting, and web publishing

                            Perfect for non-technical founders, marketers, freelancers, and business owners

                        Want to build and launch a polished website today?

                        Try B12.io — and let AI do the heavy lifting.
                      status: public
                      type: studio
                      executions: 7273
                      reviews_count: 397
                      reviews_score: 4.27
                      created_at: Wed, 15 Jan 2025 18:46:35 GMT
                      updated_at: Wed, 24 Sep 2025 20:57:41 GMT
                      score: 0.5872
                    parameters:
                      type: object
                      properties:
                        business_name:
                          type: string
                          description: What is your business name?
                        business_description:
                          type: string
                          description: Describe your business and desired website
                      required:
                        - business_name
                        - business_description
                      additionalProperties: false
                    strict: true
                - type: function
                  function:
                    name: invoke_agent_nhwrqdx5nvqt899a
                    description: >-
                      Invoke agent "Loading Message Generator": This agent
                      creates engaging, on-brand loading messages that enhance
                      user experience while pages or processes load on websites
                      and apps. 


                      Just provide your app's name,  website, and preferred
                      brand voice to generate a customized set of witty,
                      professional, or informative loading messages. Perfect for
                      UX designers, content creators, and developers who want to
                      transform wait times into brand-building moments that
                      reduce perceived loading time and maintain user
                      engagement.
                    metadata:
                      id: nhwrqdx5nvqt899a
                      slug: null
                      icon: /icons/copywriting.svg
                      name: Loading Message Generator
                      description: >-
                        This agent creates engaging, on-brand loading messages
                        that enhance user experience while pages or processes
                        load on websites and apps. 


                        Just provide your app's name,  website, and preferred
                        brand voice to generate a customized set of witty,
                        professional, or informative loading messages. Perfect
                        for UX designers, content creators, and developers who
                        want to transform wait times into brand-building moments
                        that reduce perceived loading time and maintain user
                        engagement.
                      status: public
                      type: studio
                      executions: 4439
                      reviews_count: 309
                      reviews_score: 4.31
                      created_at: Fri, 06 Sep 2024 05:36:53 GMT
                      updated_at: Wed, 24 Sep 2025 07:51:22 GMT
                      score: 0.5863
                    parameters:
                      type: object
                      properties:
                        user_input_name:
                          type: string
                          description: >-
                            What's the name of your company, website, project,
                            or app?
                        user_input_URL:
                          type: string
                          description: >-
                            If you have a website associated with it, enter that
                            URL.
                        brand_voice:
                          type: string
                          description: What brand voice do you want to convey?
                        target_audience:
                          type: string
                          description: Who is your target audience?
                      required: []
                      additionalProperties: false
                    strict: true
                - type: function
                  function:
                    name: invoke_agent_6keobi838j5pkod1
                    description: >-
                      Invoke agent "Viral LinkedIn Post Writer":  This Agent
                      converts your raw thoughts into a viral LinkedIn post.
                      Only provide a less than 100-word context in case you are
                      sharing your raw thoughts. If you are sharing a topic as a
                      prompt then the topic alone would suffice.
                    metadata:
                      id: 6keobi838j5pkod1
                      slug: viral-linkedin-post-writer
                      icon: /icons/linkedin3.svg
                      name: Viral LinkedIn Post Writer
                      description: ' This Agent converts your raw thoughts into a viral LinkedIn post. Only provide a less than 100-word context in case you are sharing your raw thoughts. If you are sharing a topic as a prompt then the topic alone would suffice.'
                      status: public
                      type: studio
                      executions: 1182
                      reviews_count: 79
                      reviews_score: 4.46
                      created_at: Mon, 20 Jan 2025 10:40:46 GMT
                      updated_at: Wed, 24 Sep 2025 20:55:53 GMT
                      score: 0.5839
                    parameters:
                      type: object
                      properties:
                        user_input:
                          type: string
                          description: >-
                            Write raw thought or a topic on which you want to
                            write a LinkedIn post.
                      required:
                        - user_input
                      additionalProperties: false
                    strict: true
                - type: function
                  function:
                    name: invoke_agent_qfwjaebz3s069pmw
                    description: >-
                      Invoke agent "Ad Copy Creator": Generates persuasive ad
                      copy for different advertising platforms (e.g., Google
                      Ads, Facebook Ads) to improve click-through rates and
                      conversions.
                    metadata:
                      id: qfwjaebz3s069pmw
                      slug: null
                      icon: /icons/copywriting.svg
                      name: Ad Copy Creator
                      description: >-
                        Generates persuasive ad copy for different advertising
                        platforms (e.g., Google Ads, Facebook Ads) to improve
                        click-through rates and conversions.
                      status: public
                      type: studio
                      executions: 2764
                      reviews_count: 85
                      reviews_score: 4.06
                      created_at: Fri, 13 Sep 2024 14:26:13 GMT
                      updated_at: Wed, 24 Sep 2025 09:24:33 GMT
                      score: 0.5754
                    parameters:
                      type: object
                      properties:
                        product_description:
                          type: string
                          description: 'Describe your product or service:'
                        ad_platform:
                          type: string
                          description: 'Select the advertising platform:'
                          enum:
                            - Google Ads
                            - Facebook Ads
                            - Instagram Ads
                            - LinkedIn Ads
                      required:
                        - product_description
                        - ad_platform
                      additionalProperties: false
                    strict: true
                - type: function
                  function:
                    name: invoke_agent_tx3oam6fo51b7pw7
                    description: >-
                      Invoke agent "Writing Idea Generator": This Ai will
                      generate fun writing prompts for you to write essays or
                      stories to so you can share it with others.
                    metadata:
                      id: tx3oam6fo51b7pw7
                      slug: writing-prompt
                      icon: /icons/writing.svg
                      name: Writing Idea Generator
                      description: >-
                        This Ai will generate fun writing prompts for you to
                        write essays or stories to so you can share it with
                        others.
                      status: public
                      type: studio
                      executions: 756
                      reviews_count: 73
                      reviews_score: 3.67
                      created_at: Thu, 07 Nov 2024 23:16:03 GMT
                      updated_at: Fri, 22 Aug 2025 01:11:41 GMT
                      score: 0.5658
                    parameters:
                      type: object
                      properties:
                        Style:
                          type: string
                          description: Style of writing
                      required:
                        - Style
                      additionalProperties: false
                    strict: true
              status: 200
        description: Agents found successfully
    '400':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Bad request
  deprecated: false
  type: path
components:
  schemas: {}

````