# Source: https://docs.agent.ai/api-reference/get-data/get-instagram-profile.md

# Get Instagram Profile

> Fetch detailed profile information for a specified Instagram username.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_instagram_profile
paths:
  path: /action/get_instagram_profile
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
              username:
                allOf:
                  - type: string
                    description: Instagram username (without @).
                    example: taylorswift
            required: true
            requiredProperties:
              - username
        examples:
          example:
            value:
              username: taylorswift
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
                response:
                  about: null
                  account_badges: []
                  account_category: ''
                  account_type: 3
                  active_standalone_fundraisers:
                    fundraisers: []
                    total_count: 0
                  additional_business_addresses: []
                  adjusted_banners_order: []
                  ads_incentive_expiration_date: null
                  ads_page_id: null
                  ads_page_name: null
                  auto_expand_chaining: false
                  avatar_status:
                    has_avatar: false
                  bio_links:
                    - icon_url: ''
                      image_url: ''
                      is_pinned: false
                      is_verified: false
                      link_id: 17899966490651260
                      link_type: external
                      lynx_url: >-
                        https://l.instagram.com/?u=http%3A%2F%2Ftaylorswift.com%2F%3Ffbclid%3DPAZXh0bgNhZW0CMTEAAabw-h_L5suFAr1hiBsgDl2LFupiJnBnoDtatI5yTU6T1GdDyOcOuu9XiBE_aem_d69Mu7ZzZTJ9ouOOJ_dWlQ&e=AT3wf1TQkZVOLRSp-2bAxic1A7Y682Kvw_F2UqD7VXuMMFrg_FFytEMqHgZPjVu6KvfTtXa6RT2t9bDXXQN-QjMSX-19DL-RdoubM8o
                      media_type: none
                      open_external_url_with_in_app_browser: true
                      title: ''
                      url: http://taylorswift.com
                    - icon_url: ''
                      image_url: ''
                      is_pinned: false
                      is_verified: false
                      link_id: 18001077971004600
                      link_type: external
                      lynx_url: >-
                        https://l.instagram.com/?u=https%3A%2F%2Ftaylor.lnk.to%2Fthetorturedpoetsdepartment%3Ffbclid%3DPAZXh0bgNhZW0CMTEAAaYv0nKSrW78bzyQZRPbSKqDg85gv3BF3UBOey9O7tHnAJtZxVeKYkXlfz0_aem_k3TNam9fjNOb4KN4pfhyrQ&e=AT3hfA3XDZllKZVAdlX8VQ1lFcmZ50pN6j1TdvAEN4a3ZMatnEvK4zlxEnatuqvoFJ_F_JZYZB4RVypnSC-nGDJpcQLLs_KmCGaBFP8
                      media_type: none
                      open_external_url_with_in_app_browser: true
                      title: THE TORTURED POETS DEPARTMENT 🤍
                      url: https://taylor.lnk.to/thetorturedpoetsdepartment
                    - icon_url: ''
                      image_url: ''
                      is_pinned: false
                      is_verified: false
                      link_id: 17870840868003034
                      link_type: external
                      lynx_url: >-
                        https://l.instagram.com/?u=https%3A%2F%2Ftaylor.lnk.to%2FTSTheErasTourFilm%3Ffbclid%3DPAZXh0bgNhZW0CMTEAAaYX9G0l3dT87NlnGcsITeOeae11enahaKKXec9plaXzzFN6w698pp3tobU_aem_E__ozWUeuNtmg5WuWJOHhg&e=AT03gyzLPmdLY9powVMNR77tQe8E0m5aHwN5CD32P-3zGNzxuuUHBa2vuRGq_yogOP4UyM0qd4ubz9P5q-u7wDW_pQLWyXCNlBM_-AQ
                      media_type: none
                      open_external_url_with_in_app_browser: true
                      title: Taylor Swift | The Eras Tour concert film
                      url: https://taylor.lnk.to/TSTheErasTourFilm
                  biography: >-
                    All’s fair in love and poetry... New album THE TORTURED
                    POETS DEPARTMENT. Out now 🤍
                  biography_email: null
                  biography_with_entities:
                    entities: []
                    raw_text: >-
                      All’s fair in love and poetry... New album THE TORTURED
                      POETS DEPARTMENT. Out now 🤍
                  birthday_today_visibility_for_viewer: NOT_VISIBLE
                  broadcast_chat_preference_status:
                    json_response: >-
                      {"status":"ok","status_code":"200","is_broadcast_chat_creator":true,"notification_setting_type":2}
                  business_contact_method: UNKNOWN
                  can_add_fb_group_link_on_profile: false
                  can_hide_category: true
                  can_hide_public_contacts: true
                  can_use_affiliate_partnership_messaging_as_brand: false
                  can_use_affiliate_partnership_messaging_as_creator: false
                  can_use_branded_content_discovery_as_brand: false
                  can_use_branded_content_discovery_as_creator: false
                  can_use_paid_partnership_messaging_as_creator: false
                  category: Musician
                  category_id: 1335670856447673
                  chaining_upsell_cards: []
                  contact_phone_number: ''
                  creator_shopping_info:
                    linked_merchant_accounts: []
                  current_catalog_id: null
                  direct_messaging: ''
                  enable_add_school_in_edit_profile: false
                  existing_user_age_collection_enabled: true
                  external_lynx_url: >-
                    https://l.instagram.com/?u=http%3A%2F%2Ftaylorswift.com%2F%3Ffbclid%3DPAZXh0bgNhZW0CMTEAAabw-h_L5suFAr1hiBsgDl2LFupiJnBnoDtatI5yTU6T1GdDyOcOuu9XiBE_aem_d69Mu7ZzZTJ9ouOOJ_dWlQ&e=AT3wf1TQkZVOLRSp-2bAxic1A7Y682Kvw_F2UqD7VXuMMFrg_FFytEMqHgZPjVu6KvfTtXa6RT2t9bDXXQN-QjMSX-19DL-RdoubM8o
                  external_url: http://taylorswift.com
                  fan_club_info:
                    autosave_to_exclusive_highlight: null
                    connected_member_count: null
                    fan_club_id: null
                    fan_club_name: null
                    fan_consideration_page_revamp_eligiblity: null
                    has_created_ssc: null
                    has_enough_subscribers_for_ssc: null
                    is_fan_club_gifting_eligible: null
                    is_fan_club_referral_eligible: null
                    is_free_trial_eligible: null
                    largest_public_bc_id: null
                    subscriber_count: null
                  fbid_v2: '17841401648650184'
                  feed_post_reshare_disabled: false
                  follow_friction_type: 0
                  follower_count: 282510661
                  following_count: 0
                  full_name: Taylor Swift
                  has_anonymous_profile_picture: false
                  has_chaining: false
                  has_chains: false
                  has_collab_collections: false
                  has_ever_selected_topics: false
                  has_exclusive_feed_content: false
                  has_fan_club_subscriptions: false
                  has_gen_ai_personas_for_profile_banner: false
                  has_guides: false
                  has_highlight_reels: true
                  has_ig_profile: true
                  has_igtv_series: false
                  has_legacy_bb_pending_profile_picture_update: false
                  has_music_on_profile: true
                  has_mv4b_pending_profile_picture_update: false
                  has_nme_badge: false
                  has_private_collections: false
                  has_public_tab_threads: true
                  has_videos: true
                  has_views_fetching: true
                  hd_profile_pic_url_info:
                    height: 1000
                    url: >-
                      https://scontent-atl3-2.cdninstagram.com/v/t51.2885-19/432597291_3681183002154789_5473029370098280466_n.jpg?_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_cat=1&_nc_ohc=hQCGPLcccToQ7kNvgE40yj1&_nc_gid=638a927549d341858014179930ccce04&edm=AO4kU9EBAAAA&ccb=7-5&oh=00_AYD00YUrPPERMT4IHe-pkpnuTeB7o_2E4xm87WLkp57dSQ&oe=67B1B8DF&_nc_sid=164c1d
                    width: 1000
                  hd_profile_pic_versions:
                    - height: 320
                      url: >-
                        https://scontent-atl3-2.cdninstagram.com/v/t51.2885-19/432597291_3681183002154789_5473029370098280466_n.jpg?stp=dst-jpg_s320x320_tt6&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_cat=1&_nc_ohc=hQCGPLcccToQ7kNvgE40yj1&_nc_gid=638a927549d341858014179930ccce04&edm=AO4kU9EBAAAA&ccb=7-5&oh=00_AYA7A4gMCiWlNspXWsNHW6a5NWGICSd-s_k5gDIWa27hIA&oe=67B1B8DF&_nc_sid=164c1d
                      width: 320
                    - height: 640
                      url: >-
                        https://scontent-atl3-2.cdninstagram.com/v/t51.2885-19/432597291_3681183002154789_5473029370098280466_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_cat=1&_nc_ohc=hQCGPLcccToQ7kNvgE40yj1&_nc_gid=638a927549d341858014179930ccce04&edm=AO4kU9EBAAAA&ccb=7-5&oh=00_AYBWSIWDh8rbh5DKpK9-PoLOnQbmsOVtLKmA_myGUiH9qA&oe=67B1B8DF&_nc_sid=164c1d
                      width: 640
                  highlight_reshare_disabled: false
                  highlights_tray_type: DEFAULT
                  id: '11830955'
                  include_direct_blacklist_status: true
                  instagram_pk: '11830955'
                  interop_messaging_user_fbid: 115431063179813
                  is_active_on_text_post_app: true
                  is_auto_confirm_enabled_for_all_reciprocal_follow_requests: false
                  is_bestie: false
                  is_business: false
                  is_call_to_action_enabled: false
                  is_category_tappable: false
                  is_creator_agent_enabled: false
                  is_direct_roll_call_enabled: true
                  is_eligible_for_diverse_owned_business_info: false
                  is_eligible_for_meta_verified_enhanced_link_sheet: false
                  is_eligible_for_meta_verified_enhanced_link_sheet_consumption: false
                  is_eligible_for_meta_verified_label: true
                  is_eligible_for_meta_verified_links_in_reels: false
                  is_eligible_for_meta_verified_multiple_addresses_consumption: false
                  is_eligible_for_meta_verified_multiple_addresses_creation: false
                  is_eligible_for_meta_verified_related_accounts: false
                  is_eligible_for_post_boost_mv_upsell: false
                  is_eligible_for_request_message: false
                  is_eligible_to_display_diverse_owned_business_info: false
                  is_favorite: false
                  is_favorite_for_clips: false
                  is_favorite_for_highlights: false
                  is_favorite_for_igtv: false
                  is_favorite_for_stories: false
                  is_in_canada: false
                  is_interest_account: true
                  is_legacy_verified_max_profile_pic_edit_reached: false
                  is_memorialized: false
                  is_meta_verified_related_accounts_display_enabled: false
                  is_mv4b_application_matured_for_profile_edit: true
                  is_mv4b_biz_asset_profile_locked: false
                  is_mv4b_max_profile_edit_reached: false
                  is_new_to_instagram: false
                  is_opal_enabled: false
                  is_open_to_collab: false
                  is_oregon_custom_gender_consented: false
                  is_parenting_account: false
                  is_potential_business: false
                  is_private: false
                  is_profile_audio_call_enabled: false
                  is_profile_broadcast_sharing_enabled: true
                  is_profile_picture_expansion_enabled: true
                  is_recon_ad_cta_on_profile_eligible_with_viewer: true
                  is_regulated_c18: false
                  is_regulated_news_in_viewer_location: false
                  is_remix_setting_enabled_for_posts: true
                  is_remix_setting_enabled_for_reels: true
                  is_secondary_account_creation: false
                  is_stories_teaser_muted: false
                  is_supervision_features_enabled: false
                  is_verified: true
                  is_whatsapp_linked: false
                  latest_besties_reel_media: 0
                  latest_reel_media: 0
                  live_subscription_status: default
                  location_data:
                    address_street: ''
                    city_id: 0
                    city_name: ''
                    instagram_location_id: ''
                    latitude: 0
                    longitude: 0
                    zip: ''
                  media_count: 676
                  merchant_checkout_style: none
                  meta_verified_benefits_info:
                    is_eligible_for_meta_verified_content_protection: false
                  meta_verified_related_accounts_count: 0
                  nametag:
                    available_theme_colors:
                      - -1
                      - 7747834
                      - 13828293
                      - 16712041
                      - 16742912
                      - 0
                    background_image_url: ''
                    emoji: 😀
                    emoji_color: 0
                    gradient: 0
                    is_background_image_blurred: false
                    mode: 1
                    selected_theme_color: -1
                    selfie_sticker: 0
                    selfie_url: ''
                    theme_color:
                      available_theme_colors:
                        - display_label: Default
                          int_value: -1
                        - display_label: Purple
                          int_value: 7747834
                        - display_label: Lavender
                          int_value: 13828293
                        - display_label: Pink
                          int_value: 16712041
                        - display_label: Orange
                          int_value: 16742912
                        - display_label: Black
                          int_value: 0
                      selected_theme_color:
                        display_label: Default
                        int_value: -1
                  nonpro_can_maybe_see_profile_hypercard: false
                  not_meta_verified_friction_info:
                    is_eligible_for_label_friction: false
                    label_friction_content: Not Meta Verified
                  open_external_url_with_in_app_browser: true
                  page_id: 19614945368
                  page_name: Taylor Swift
                  pinned_channels_info:
                    has_public_channels: false
                    pinned_channels_list: []
                  primary_profile_link_type: 0
                  professional_conversion_suggested_account_type: 3
                  profile_context: Followed by melrobbins and reesewitherspoon
                  profile_context_facepile_users:
                    - full_name: Mel Robbins
                      id: '50722961'
                      is_private: false
                      is_verified: true
                      profile_pic_id: '3354341036162976480_50722961'
                      profile_pic_url: >-
                        https://scontent-atl3-2.cdninstagram.com/v/t51.2885-19/440074143_789167112847793_2497590725115182376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_cat=1&_nc_ohc=doZShPquwu8Q7kNvgEKgUDw&_nc_gid=638a927549d341858014179930ccce04&edm=AO4kU9EBAAAA&ccb=7-5&oh=00_AYCysONxAfhs4_oZKs-Z7H8kgJWqmPHj5oxzVLdaQe-DDg&oe=67B1BC31&_nc_sid=164c1d
                      username: melrobbins
                    - full_name: Reese Witherspoon
                      id: '367315644'
                      is_private: false
                      is_verified: true
                      profile_pic_id: '2689488593938037730_367315644'
                      profile_pic_url: >-
                        https://scontent-atl3-2.cdninstagram.com/v/t51.2885-19/246775225_4412432445539714_307618120921833826_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_cat=1&_nc_ohc=ehxmbWPBc30Q7kNvgFcUe3i&_nc_gid=638a927549d341858014179930ccce04&edm=AO4kU9EBAAAA&ccb=7-5&oh=00_AYBCnhtxaKziyesNqbA_AIV4DqEIoxQ4cJQ77XVO0w-abQ&oe=67B1B3BF&_nc_sid=164c1d
                      username: reesewitherspoon
                  profile_context_links_with_user_ids:
                    - end: 22
                      start: 12
                      username: melrobbins
                    - end: 43
                      start: 27
                      username: reesewitherspoon
                  profile_context_mutual_follow_ids:
                    - 50722961
                    - 367315644
                  profile_pic_genai_tool_info: []
                  profile_pic_id: '3320725335023712969_11830955'
                  profile_pic_url: >-
                    https://scontent-atl3-2.cdninstagram.com/v/t51.2885-19/432597291_3681183002154789_5473029370098280466_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_cat=1&_nc_ohc=hQCGPLcccToQ7kNvgE40yj1&_nc_gid=638a927549d341858014179930ccce04&edm=AO4kU9EBAAAA&ccb=7-5&oh=00_AYBxLw8tuJ60vqQCZKXn56p7HHRxINqwNd4bknLcSEOLVg&oe=67B1B8DF&_nc_sid=164c1d
                  profile_pic_url_hd: >-
                    https://scontent-atl3-2.cdninstagram.com/v/t51.2885-19/432597291_3681183002154789_5473029370098280466_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_cat=1&_nc_ohc=hQCGPLcccToQ7kNvgE40yj1&_nc_gid=638a927549d341858014179930ccce04&edm=AO4kU9EBAAAA&ccb=7-5&oh=00_AYBWSIWDh8rbh5DKpK9-PoLOnQbmsOVtLKmA_myGUiH9qA&oe=67B1B8DF&_nc_sid=164c1d
                  profile_reels_sorting_eligibility: CHECK_VIEWER_QE
                  profile_type: 0
                  pronouns: []
                  public_email: ''
                  public_phone_country_code: ''
                  public_phone_number: ''
                  recon_features:
                    enable_recon_cta: true
                  recs_from_friends:
                    enable_recs_from_friends: false
                    recs_from_friends_entry_point_type: banner
                  relevant_news_regulation_locations: []
                  remove_message_entrypoint: false
                  seller_shoppable_feed_type: none
                  show_account_transparency_details: true
                  show_blue_badge_on_main_profile: true
                  show_post_insights_entry_point: true
                  show_schools_badge: null
                  show_shoppable_feed: false
                  spam_follower_setting_enabled: true
                  text_app_last_visited_time: null
                  text_post_app_badge_label: taylorswift
                  text_post_new_post_count: 0
                  third_party_downloads_enabled: 1
                  threads_profile_glyph_url: >-
                    https://www.threads.net/@taylorswift?modal=true&xmt=AQGzvDqI3TkMt0-x1f_bRCaaVH4QRpRaebh7OxbMs3qp27I
                  total_ar_effects: 0
                  total_igtv_videos: 17
                  transparency_product_enabled: false
                  upcoming_events: []
                  username: taylorswift
                  views_on_grid_status: SHOW_VIEWS_ON_GRID
        description: Instagram profile data
  deprecated: false
  type: path
components:
  schemas: {}

````