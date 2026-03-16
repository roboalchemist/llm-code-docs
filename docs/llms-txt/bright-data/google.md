# Source: https://docs.brightdata.com/scraping-automation/serp-api/query-parameters/google.md

# Source: https://docs.brightdata.com/scraping-automation/serp-api/header-parameters/google.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API Google Header Parameters

> Configure BrightData parameters for parsing and more.

<AccordionGroup>
  <Accordion title="Parsing" icon="brackets-curly">
    <AccordionGroup>
      <Accordion title="Raw HTML" icon="brackets-curly" />

      <Accordion title="Full JSON" icon="brackets-curly">
        ## Expected Parsed Output when using `brd_json=1`

        The following is the exact JSON response received when sending the request above:

        <Accordion title="JSON Response">
          ```JSON  theme={null}
          {
            "general": {
              "search_engine": "google",
              "results_cnt": 1980000000,
              "search_time": 0.57,
              "language": "en",
              "mobile": false,
              "basic_view": false,
              "search_type": "text",
              "page_title": "pizza - Google Search",
              "code_version": "1.90",
              "timestamp": "2023-06-30T08:58:41.786Z"
            },
            "input": {
              "original_url": "https://www.google.com/search?q=pizza&brd_json=1",
              "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/608.2.11 (KHTML, like Gecko) Version/13.0.3 Safari/608.2.11",
              "request_id": "hl_1a1be908_i00lwqqxt1"
            },
            "organic": [
              {
                "link": "https://www.pizzahut.com/",
                "display_link": "https://www.pizzahut.com",
                "title": "Pizza Hut | Delivery & Carryout - No One OutPizzas The Hut!",
                "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                "image_alt": "pizza from www.pizzahut.com",
                "image_base64": "data:image/jpeg;base64,/9j/4AAQSk...",
                "rank": 1,
                "global_rank": 1
              },
              {
                "link": "https://www.dominos.com/en/",
                "display_link": "https://www.dominos.com › ...",
                "title": "Domino's: Pizza Delivery & Carryout, Pasta, Chicken & More",
                "description": "Order pizza, pasta, sandwiches & more online for carryout or delivery from Domino's. View menu, find locations, track orders. Sign up for Domino's email ...",
                "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                "image_alt": "pizza from www.dominos.com",
                "image_base64": "data:image/jpeg;base64,/9j/4AAQSk...",
                "rank": 2,
                "global_rank": 3
              },
              {
                "link": "https://en.wikipedia.org/wiki/Pizza",
                "display_link": "https://en.wikipedia.org › wiki › Pizza",
                "title": "Pizza - Wikipedia",
                "description": "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various ...",
                "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                "image_alt": "pizza from en.wikipedia.org",
                "image_base64": "data:image/jpeg;base64,/9j/4AAQSk...",
                "rank": 3,
                "global_rank": 4
              },
              {
                "link": "https://www.papajohns.com/",
                "display_link": "https://www.papajohns.com",
                "title": "Papa Johns Pizza Delivery & Carryout - Best Deals on Pizza ...",
                "description": "Enjoy the ease of ordering delicious pizza for delivery or carryout from a Papa Johns near you. Start tracking the speed of your delivery and earn rewards ...",
                "rank": 4,
                "global_rank": 5
              },
              {
                "link": "https://littlecaesars.com/",
                "display_link": "https://littlecaesars.com",
                "title": "Little Caesars® Pizza: Best Value Delivery and Carryout",
                "description": "Your home for HOT-N-READY® pizzas, EXTRAMOSTBESTEST® pizzas, DEEP!DEEP!™ Dish pizzas, Crazy Bread® and MORE! Order online for no-contact delivery or ...",
                "rank": 5,
                "global_rank": 6
              },
              {
                "link": "https://www.blazepizza.com/",
                "display_link": "https://www.blazepizza.com",
                "title": "Blaze Pizza - Fast-Fire'd Pizzas - Order Online | Blaze Pizza",
                "description": "Get fired up with Fast-Fire'd Pizzas from Blaze! Made just the way you want. Order online for delivery or pickup.",
                "rank": 6,
                "global_rank": 7
              },
              {
                "link": "https://www.theguardian.com/food/2023/jun/28/rightwingers-say-pink-haired-liberals-are-killing-new-york-pizza-heres-whats-really-happening",
                "display_link": "https://www.theguardian.com › food › jun › rightwing...",
                "title": "Rightwingers say 'pink-haired liberals' are killing New York ...",
                "description": "The pizza pile-on was sparked by a inaccuracy-riddled report ... 'This is not legislation that will corrode the New York pizza scene,' says ...",
                "extensions": [
                  {
                    "inline": true,
                    "type": "text",
                    "text": "20 hours ago",
                    "rank": 1
                  }
                ],
                "rank": 7,
                "global_rank": 8
              },
              {
                "link": "https://www.youtube.com/watch?v=oxLzRjYBxQQ",
                "display_link": "https://www.youtube.com › watch",
                "title": "Barstool Pizza Review - YouTube",
                "description": "YouTube",
                "extensions": [
                  {
                    "type": "text",
                    "text": "One Bite Pizza Reviews",
                    "rank": 1
                  },
                  {
                    "type": "text",
                    "text": "1 day ago",
                    "rank": 2
                  }
                ],
                "image": "https://i.ytimg.com/vi/oxLzRjYBxQQ/mqdefault.jpg?sqp=-oaymwEFCJQBEFM&rs=AMzJL3lRRTbw1I91F1168NO_w1YftuPlgA",
                "image_url": "https://i.ytimg.com/vi/oxLzRjYBxQQ/mqdefault.jpg?sqp=-oaymwEFCJQBEFM&rs=AMzJL3lRRTbw1I91F1168NO_w1YftuPlgA",
                "duration": "11:14",
                "duration_sec": 674,
                "rank": 8,
                "global_rank": 12
              },
              {
                "link": "https://www.youtube.com/watch?v=9X56jc_68EU",
                "display_link": "https://www.youtube.com › watch",
                "title": "Barstool Pizza Review - NYC Pizza Kitchen (New York, NY)",
                "description": "YouTube",
                "extensions": [
                  {
                    "type": "text",
                    "text": "One Bite Pizza Reviews",
                    "rank": 1
                  },
                  {
                    "type": "text",
                    "text": "3 days ago",
                    "rank": 2
                  }
                ],
                "image": "https://i.ytimg.com/vi/9X56jc_68EU/mqdefault.jpg?sqp=-oaymwEFCJQBEFM&rs=AMzJL3lO46CkRjZWL3FEQeeQkBJgCxZzeQ",
                "image_url": "https://i.ytimg.com/vi/9X56jc_68EU/mqdefault.jpg?sqp=-oaymwEFCJQBEFM&rs=AMzJL3lO46CkRjZWL3FEQeeQkBJgCxZzeQ",
                "duration": "4:10",
                "duration_sec": 250,
                "rank": 9,
                "global_rank": 13
              }
            ],
            "recipes": {
              "title": "Recipes",
              "items": [
                {
                  "title": "Homemade Pizza & Pizza Dough",
                  "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS47CWfkHqjbfUIaFrK8RjTm_KngqQxsXQ2OTmW7q1lrTebxVxzzYG3mmpj4g&s",
                  "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS47CWfkHqjbfUIaFrK8RjTm_KngqQxsXQ2OTmW7q1lrTebxVxzzYG3mmpj4g&s",
                  "link": "https://www.simplyrecipes.com/recipes/homemade_pizza/",
                  "rating": 4.8,
                  "reviews_cnt": 90,
                  "source": "Simply Recipes",
                  "cook_time": "2 hr 30 min",
                  "ingredients": [
                    "Italian sausage",
                    "pizza dough",
                    "pesto",
                    "feta cheese",
                    "bell peppers"
                  ],
                  "rank": 1,
                  "global_rank": 9
                },
                {
                  "title": "Pizza Dough",
                  "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHSV3fiR1QKeO5Gu7eVRg66v32XW049i_F8_sAYXxXHxS1oRwZ3IS0mTPY&s",
                  "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHSV3fiR1QKeO5Gu7eVRg66v32XW049i_F8_sAYXxXHxS1oRwZ3IS0mTPY&s",
                  "link": "https://www.foodnetwork.com/recipes/bobby-flay/pizza-dough-recipe-1921714",
                  "rating": 4.5,
                  "reviews_cnt": 1600,
                  "source": "Food Network",
                  "cook_time": "1 hr 30 min",
                  "ingredients": [
                    "Bread flour",
                    "olive oil",
                    "sugar",
                    "dry yeast"
                  ],
                  "rank": 2,
                  "global_rank": 10
                },
                {
                  "title": "Easy Homemade Pizza Dough",
                  "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzzGNfXoRqbKBti55KO34rb_SW-xePkIvSMgef0AsbRArRcu9nMLpyr8-Iyw&s",
                  "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzzGNfXoRqbKBti55KO34rb_SW-xePkIvSMgef0AsbRArRcu9nMLpyr8-Iyw&s",
                  "link": "https://www.allrecipes.com/recipe/20171/quick-and-easy-pizza-crust/",
                  "rating": 4.7,
                  "reviews_cnt": 3900,
                  "source": "Allrecipes",
                  "cook_time": "45 min",
                  "ingredients": [
                    "Bread flour",
                    "olive oil",
                    "active dry yeast",
                    "white sugar"
                  ],
                  "rank": 3,
                  "global_rank": 11
                }
              ]
            },
            "knowledge": {
              "name": "Pizza",
              "subtitle": "Dish",
              "description": "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients, which is then baked at a high temperature, traditionally in a wood-fired oven.",
              "description_source": "Wikipedia",
              "description_link": "https://en.wikipedia.org/wiki/Pizza",
              "images": [
                {
                  "link": "https://www.google.com/search?q=pizza&hl=en&tbm=isch&source=iu&ictx=1&vet=1&fir=vwyNmrlxb87lKM%252C5xpz_Vm2ema2NM%252C%252Fm%252F0663v%253BefJ23c2_JH_n7M%252CbBq_NwtYzsoXvM%252C_%253B4T1KqgPBvr4X6M%252CJGW8XVFocJC4wM%252C_%253B7mn1Wr2V2et-TM%252CCk5z3mFwtc-sLM%252C_%253BHAxRWExZGt4a0M%252CTQkQ0B0M4aWgcM%252C_%253BAOp1u9WxhkknqM%252CDnbYrezaqAeTBM%252C_%253BZiJze8NWYgm1BM%252CmUmiEmWVfPIjPM%252C_&usg=AI4_-kQ40qSc7MuZBzNVnuLne9fo9Vl5gA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ_B16BAhUEAE#imgrc=vwyNmrlxb87lKM",
                  "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                  "image_base64": "data:image/jpeg;base64,/9j/4AAQSk..."
                },
                {
                  "link": "https://www.google.com/search?q=pizza&hl=en&tbm=isch&source=iu&ictx=1&vet=1&fir=efJ23c2_JH_n7M%252CbBq_NwtYzsoXvM%252C_%253B4T1KqgPBvr4X6M%252CJGW8XVFocJC4wM%252C_%253B7mn1Wr2V2et-TM%252CCk5z3mFwtc-sLM%252C_%253BHAxRWExZGt4a0M%252CTQkQ0B0M4aWgcM%252C_%253BAOp1u9WxhkknqM%252CDnbYrezaqAeTBM%252C_%253BZiJze8NWYgm1BM%252CmUmiEmWVfPIjPM%252C_&usg=AI4_-kRwEYdg29oH_CmkbTMQheFOmeF4NA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ_h16BAhWEAE#imgrc=efJ23c2_JH_n7M",
                  "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                  "image_alt": "Classic Cheese Pizza",
                  "image_base64": "data:image/jpeg;base64,/9j/4AAQSk..."
                },
                {
                  "link": "https://www.google.com/search?q=pizza&hl=en&tbm=isch&source=iu&ictx=1&vet=1&fir=efJ23c2_JH_n7M%252CbBq_NwtYzsoXvM%252C_%253B4T1KqgPBvr4X6M%252CJGW8XVFocJC4wM%252C_%253B7mn1Wr2V2et-TM%252CCk5z3mFwtc-sLM%252C_%253BHAxRWExZGt4a0M%252CTQkQ0B0M4aWgcM%252C_%253BAOp1u9WxhkknqM%252CDnbYrezaqAeTBM%252C_%253BZiJze8NWYgm1BM%252CmUmiEmWVfPIjPM%252C_&usg=AI4_-kRwEYdg29oH_CmkbTMQheFOmeF4NA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ_h16BAhYEAE#imgrc=4T1KqgPBvr4X6M",
                  "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                  "image_alt": "Homemade Pepperoni Pizza",
                  "image_base64": "data:image/jpeg;base64,/9j/4AAQSk..."
                },
                {
                  "link": "https://www.google.com/search?q=pizza&hl=en&tbm=isch&source=iu&ictx=1&vet=1&fir=efJ23c2_JH_n7M%252CbBq_NwtYzsoXvM%252C_%253B4T1KqgPBvr4X6M%252CJGW8XVFocJC4wM%252C_%253B7mn1Wr2V2et-TM%252CCk5z3mFwtc-sLM%252C_%253BHAxRWExZGt4a0M%252CTQkQ0B0M4aWgcM%252C_%253BAOp1u9WxhkknqM%252CDnbYrezaqAeTBM%252C_%253BZiJze8NWYgm1BM%252CmUmiEmWVfPIjPM%252C_&usg=AI4_-kRwEYdg29oH_CmkbTMQheFOmeF4NA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ_h16BAhaEAE#imgrc=7mn1Wr2V2et-TM",
                  "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                  "image_alt": "Homemade Pepperoni Pizza",
                  "image_base64": "data:image/jpeg;base64,/9j/4AAQSk..."
                },
                {
                  "link": "https://www.google.com/search?q=pizza&hl=en&tbm=isch&source=iu&ictx=1&vet=1&fir=efJ23c2_JH_n7M%252CbBq_NwtYzsoXvM%252C_%253B4T1KqgPBvr4X6M%252CJGW8XVFocJC4wM%252C_%253B7mn1Wr2V2et-TM%252CCk5z3mFwtc-sLM%252C_%253BHAxRWExZGt4a0M%252CTQkQ0B0M4aWgcM%252C_%253BAOp1u9WxhkknqM%252CDnbYrezaqAeTBM%252C_%253BZiJze8NWYgm1BM%252CmUmiEmWVfPIjPM%252C_&usg=AI4_-kRwEYdg29oH_CmkbTMQheFOmeF4NA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ_h16BAhZEAE#imgrc=HAxRWExZGt4a0M",
                  "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                  "image_alt": "Pizza Dough recipe",
                  "image_base64": "data:image/jpeg;base64,/9j/4AAQSk..."
                },
                {
                  "link": "https://www.google.com/search?q=pizza&hl=en&tbm=isch&source=iu&ictx=1&vet=1&fir=efJ23c2_JH_n7M%252CbBq_NwtYzsoXvM%252C_%253B4T1KqgPBvr4X6M%252CJGW8XVFocJC4wM%252C_%253B7mn1Wr2V2et-TM%252CCk5z3mFwtc-sLM%252C_%253BHAxRWExZGt4a0M%252CTQkQ0B0M4aWgcM%252C_%253BAOp1u9WxhkknqM%252CDnbYrezaqAeTBM%252C_%253BZiJze8NWYgm1BM%252CmUmiEmWVfPIjPM%252C_&usg=AI4_-kRwEYdg29oH_CmkbTMQheFOmeF4NA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ_h16BAhXEAE#imgrc=AOp1u9WxhkknqM",
                  "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBTiGlL3eQeQk_UYQGpoyg3OE6RQsOhx60YyUbNvPFng&s",
                  "image_alt": "Chicken Alfredo Pizza",
                  "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBTiGlL3eQeQk_UYQGpoyg3OE6RQsOhx60YyUbNvPFng&s"
                },
                {
                  "link": "https://www.google.com/search?q=pizza&hl=en&tbm=isch&source=iu&ictx=1&vet=1&fir=efJ23c2_JH_n7M%252CbBq_NwtYzsoXvM%252C_%253B4T1KqgPBvr4X6M%252CJGW8XVFocJC4wM%252C_%253B7mn1Wr2V2et-TM%252CCk5z3mFwtc-sLM%252C_%253BHAxRWExZGt4a0M%252CTQkQ0B0M4aWgcM%252C_%253BAOp1u9WxhkknqM%252CDnbYrezaqAeTBM%252C_%253BZiJze8NWYgm1BM%252CmUmiEmWVfPIjPM%252C_&usg=AI4_-kRwEYdg29oH_CmkbTMQheFOmeF4NA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ_h16BAhQEAE#imgrc=ZiJze8NWYgm1BM",
                  "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShqNOrnCWng5zaBj2reNeU2QHAMaeyj1EJJhqbunN9kg&s",
                  "image_alt": "Classic Cheese Pizza",
                  "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShqNOrnCWng5zaBj2reNeU2QHAMaeyj1EJJhqbunN9kg&s"
                }
              ],
              "facts": [
                {
                  "key": "Origin",
                  "key_link": "https://www.google.com/search?hl=en&q=pizza+origin&stick=H4sIAAAAAAAAAOPgE-LQz9U3MDMzLtOSySi30k_Oz8lJTS7JzM_TT8kszkgttsovykzPzFvEylOQWVWVqADhAgAjO0XtOQAAAA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ6BMoAHoECEcQAg",
                  "predicate": "hw:/collection/dishes:origin",
                  "value": [
                    {
                      "text": "Italy",
                      "link": "https://www.google.com/search?hl=en&q=Italy&si=AMnBZoFk_ppfOKgdccwTD_PVhdkg37dbl-p8zEtOPijkCaIHMj99cmEC8YmqzIntfXVZNtU5L5s_BYkw6CsmIn-L56QSbpr6PIZUjdVkuKrffw6c1CKZ_9pKBFW4qlnB9Bhm0MDfT6vScNQrXeycat32kzuoKi0SbwH1ZOSp7Rw9H4b-NlpUU9DyezwS3Hx3MvdZtCWf0TlV&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQmxMoAXoECEcQAw"
                    }
                  ]
                }
              ],
              "widgets": [
                {
                  "type": "carousel",
                  "key": "downwards",
                  "predicate": "kc:/common:downwards",
                  "key_link": "https://www.google.com/search?hl=en&q=where+to+buy+neapolitan+pizza+dough&stick=H4sIAAAAAAAAAD3IMQrCMBQAUIoUOosHCHVziSJ06GVCmnySkJ_Q5Ma7HEcPYHH08nt8YbDcZBJXqfp_hj_upyimaXhlJhmy42aXm15d7ffIYKpgUlG4oZgHaisCbDI4jnnQE7FrACDCwvCqz83DyuIymLZnoJAZ8ZQNYkc9l0Ly5vzn777AncBsYyJAAAA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQMSgAegQIQxAB",
                  "title": "where to buy neapolitan pizza dough",
                  "items": [
                    {
                      "title": "Delallo Pizza Dough Kit",
                      "link": "https://www.google.com/search?hl=en&q=Delallo+Pizza+Dough+Kit&stick=H4sIAAAAAAAAAONgFmJQ4tVP1zc0zDArSa-KL7TUYljEKu6SmpOYk5OvEJBZVZWo4JJfmp6h4J1ZsoOVEQCmdWPwMgAAAA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQxA16BAhDEAQ",
                      "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                      "image_alt": "Delallo Pizza Dough Kit",
                      "image_base64": "data:image/jpeg;base64,/9j/4AAQSk...",
                      "rank": 1
                    },
                    {
                      "title": "King Arthur Flour Piz...",
                      "link": "https://www.google.com/search?hl=en&q=King+Arthur+Flour+Pizza&stick=H4sIAAAAAAAAAONgFmJQ4tVP1zc0zM4wNjQsiS_WYljEKu6dmZeu4FhUklFapOCWkw8kAzKrqhJ3sDICAJ9B7QQyAAAA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQxA16BAhDEAY",
                      "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                      "image_alt": "King Arthur Flour Pizza",
                      "image_base64": "data:image/jpeg;base64,/9j/4AAQSk...",
                      "rank": 2
                    },
                    {
                      "title": "Pizza Buddy Pizza Do...",
                      "link": "https://www.google.com/search?hl=en&q=Pizza+Buddy+Pizza+Dough&stick=H4sIAAAAAAAAAONgFmJQ4tVP1zc0TM9IKkwqsjTQYljEKh6QWVWVqOBUmpJSqQBhu-SXpmfsYGUEAHLKv6oyAAAA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQxA16BAhDEAg",
                      "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                      "image_alt": "Pizza Buddy Pizza Dough",
                      "image_base64": "data:image/jpeg;base64,/9j/4AAQSk...",
                      "rank": 3
                    },
                    {
                      "title": "Pillsbury Classic Pizza Cr...",
                      "link": "https://www.google.com/search?hl=en&q=Pillsbury+Classic+Pizza+Crust&stick=H4sIAAAAAAAAAONgFmJQ4tVP1zc0LDExNjTNqsjTYljEKhuQmZNTnFRaVKngnJNYXJyZrBCQWVWVqOBcVFpcsoOVEQCR9ToAOAAAAA&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQxA16BAhDEAo",
                      "image": "data:image/jpeg;base64,/9j/4AAQSk...",
                      "image_alt": "Pillsbury Classic Pizza Crust",
                      "image_base64": "data:image/jpeg;base64,/9j/4AAQSk...",
                      "rank": 4
                    }
                  ],
                  "rank": 1,
                  "global_rank": 2
                }
              ]
            },
            "snack_pack_map": {
              "image": "data:image/png;base64,iVBOR...",
              "image_alt": "Map of pizza",
              "image_base64": "data:image/png;base64,iVBOR...",
              "link": "https://www.google.com/search?hl=en&q=pizza&npsic=0&rflfq=1&rldoc=1&rllag=40711584,-74006968,203&tbm=lcl&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQtgN6BAgWEAI",
              "latitude": 40.711584,
              "longitude": -74.006968,
              "altitude": 203
            },
            "pagination": {
              "current_page": 1,
              "next_page_link": "https://www.google.com/search?q=pizza&hl=en&ei=P5meZMuIMLyiptQP89muyA0&start=10&sa=N",
              "next_page_start": 10,
              "next_page": 2
            },
            "related": [
              {
                "text": "Family-friendly dinner near New York",
                "list_group": true,
                "image": "https://lh5.googleusercontent.com/p/AF1QipN9vMB3YUcI2E2RBZYuhQcpa9q3yCLDClsVS20_=w40-h40-n-k-no",
                "image_url": "https://lh5.googleusercontent.com/p/AF1QipN9vMB3YUcI2E2RBZYuhQcpa9q3yCLDClsVS20_=w40-h40-n-k-no",
                "rank": 1,
                "global_rank": 14
              },
              {
                "text": "Quick bites near New York",
                "list_group": true,
                "image": "https://lh5.googleusercontent.com/p/AF1QipM0BsBfNtUBmGyzowDeE9Zkp30pYTdtbTJCpqai=w40-h40-n-k-no",
                "image_url": "https://lh5.googleusercontent.com/p/AF1QipM0BsBfNtUBmGyzowDeE9Zkp30pYTdtbTJCpqai=w40-h40-n-k-no",
                "rank": 2,
                "global_rank": 15
              },
              {
                "text": "Pizza takeaway near New York",
                "list_group": true,
                "image": "https://lh5.googleusercontent.com/p/AF1QipO_5JRLn_XOBC5luGuOcIG_JCdfGoeBOggO69Ly=w40-h40-n-k-no",
                "image_url": "https://lh5.googleusercontent.com/p/AF1QipO_5JRLn_XOBC5luGuOcIG_JCdfGoeBOggO69Ly=w40-h40-n-k-no",
                "rank": 3,
                "global_rank": 16
              },
              {
                "text": "Best restaurants near New York",
                "list_group": true,
                "image": "https://lh5.googleusercontent.com/p/AF1QipNgm_8G1gbEVoaG2CvygurS-TZpEIohi2zrx6tz=w40-h40-n-k-no",
                "image_url": "https://lh5.googleusercontent.com/p/AF1QipNgm_8G1gbEVoaG2CvygurS-TZpEIohi2zrx6tz=w40-h40-n-k-no",
                "rank": 4,
                "global_rank": 17
              },
              {
                "list_group": false,
                "link": "https://www.google.com/search?hl=en&q=Domino%27s+Pizza+Pakistan&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ1QJ6BAg4EAE",
                "text": "domino's pizza pakistan",
                "rank": 5,
                "global_rank": 18
              },
              {
                "list_group": false,
                "link": "https://www.google.com/search?hl=en&q=Domino%27s+pizza+near+me&sa=X&ved=2ahUKEwiLpJav0Or_AhU8kYkEHfOsC9kQ1QJ6BAg3EAE",
                "text": "domino's pizza near me",
                "rank": 6,
                "global_rank": 19
              }
            ]
          }
          ```
        </Accordion>

        Next, we will examine a number of the important fields within the parsed JSON data to understand the type of structured data we have to offer.

        ***

        ## A Comprehensive Guide to Parsed Google SERP JSON Data

        At the top of the JSON response, you can find the `general` field, which contains details about the search you ran and also includes the "results count" from the response.

        <Frame>
                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/general-field.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=e7c874fe9363531e7d622e4df682503a" alt="General-Field" width="686" height="475" data-path="images/scraping-automation/serp-api/parsing-search-results/general-field.png" />
        </Frame>

        The following fields can be found in the `general` field

        |                         |                                                                                                                                                                                       |
        | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | `general.search_engine` | the search engine used for the search                                                                                                                                                 |
        | `general.query`         | the keywords used for the search                                                                                                                                                      |
        | `general.results_cnt`   | the results count<br /><Info>                           Google doesn't display results count for Mobile, so this field is supported only with desktop search results.         </Info> |
        | `general.search_time`   | the response time to get the results page                                                                                                                                             |
        | `general.language`      | the language that was set for the search, <br /><br />**Default**: `hl=en`                                                                                                            |
        | `general.location`      | the location that was targeted with the search,(based on the `localization` and `geo-location` parameters)                                                                            |
        | `general.mobile`        | the device the search was performed with (desktop/mobile)                                                                                                                             |
        | `general.basic_view`    | deprecated                                                                                                                                                                            |
        | `general.search _type`  | the type of search that was set to the request                                                                                                                                        |
        | `general.Page_title`    | results page title                                                                                                                                                                    |
        | general.Code\_version   | Bright data parser version                                                                                                                                                            |
        | `general.Timestamp`     | the time when the search executed                                                                                                                                                     |
        | Input.original\_url     | the url used for the search, this url includes all parameters applied for the search.applied for the search.                                                                          |

        ## Starter fields to know

        |                 |                                                                 |
        | --------------- | --------------------------------------------------------------- |
        | **JSON field**  | **Description**                                                 |
        | `type`          | The field type (site\_link, text, rating, etc.)                 |
        | `title`         | The text header, mostly the link text.                          |
        | `description`   | The description under the link                                  |
        | `referral_link` | Redirection link                                                |
        | `image`         | This field can contain the image base64 string or the Image url |
        | `image_alt`     | Image alternative name                                          |

        ## Explanation of other `fields`

        <AccordionGroup>
          <Accordion title="rank">
            |               |                                                                                                       |
            | ------------- | ----------------------------------------------------------------------------------------------------- |
            | `rank`        | indicates the position of the element in accordance with the other elements **within** that component |
            | `global_rank` | indicates the position of the element in accordance with **all** the elements in the SERP             |

            <Frame>
                            <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/rank-field.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=6f599a200e6d5868d289cd2658e230aa" alt="Rank-Field" width="429" height="628" data-path="images/scraping-automation/serp-api/parsing-search-results/rank-field.png" />
            </Frame>
          </Accordion>

          <Accordion title="spelling">
            When your search terms are inaccurate, Google suggests other search terms, which will show under the `spelling` field.

            **Subfields:**

            |                       |                                         |
            | --------------------- | --------------------------------------- |
            | `Original_text`       | the text that was searched              |
            | `Original_empty`      | true, means that no results were found. |
            | `Auto_corrected_link` | link to suggested result                |
            | `auto_corrected_text` | the suggested link text                 |

            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/spelling-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=f265a3380940c5f53a1ca89f456525d4" alt="Spelling-HTML" width="496" height="254" data-path="images/scraping-automation/serp-api/parsing-search-results/spelling-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/spelling-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=9bb5d4083727467fc8af5254abfda774" alt="Spelling-JSON" width="781" height="135" data-path="images/scraping-automation/serp-api/parsing-search-results/spelling-json.png" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="rating & reviews">
            Some of the components within a SERPs can include the `reviews` and `rating` fields

            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/rating-reviews-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=c425e51cb816fa4ff8021735fbd68371" alt="Rating-Reviews-HTML" width="366" height="28" data-path="images/scraping-automation/serp-api/parsing-search-results/rating-reviews-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/ratings-reviews-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=e56e492dafa8d899aa7339b5ae5a65db" alt="Rating-Reviews-JSON" width="429" height="628" data-path="images/scraping-automation/serp-api/parsing-search-results/ratings-reviews-json.png" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="extensions">
            Some SERP results could include site sub-links (AKA site links) that are displayed as a vertical or horizontal list

            <Tab title="Vertical - marked with extended:true">
              <Tabs>
                <Tab title="HTML">
                  <Frame>
                                        <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/ext-vertical-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=94e3ba444cc381fc0c1b3486a6c39a36" alt="Extensions-Vertical-HTML" width="610" height="375" data-path="images/scraping-automation/serp-api/parsing-search-results/ext-vertical-html.png" />
                  </Frame>
                </Tab>

                <Tab title="JSON">
                  <Frame>
                                        <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/ext-vertical-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=dbc6d2ebc92a83a17bfbd6ed7641c5e3" alt="Extensions-Vertical-JSON" width="715" height="621" data-path="images/scraping-automation/serp-api/parsing-search-results/ext-vertical-json.png" />
                  </Frame>
                </Tab>
              </Tabs>
            </Tab>

            <Tab title="Horizontal - not marked with `extended:true`">
              <Tabs>
                <Tab title="HTML">
                  <Frame>
                                        <img src="https://mintcdn.com/brightdata/YUhP5HZ1PAScLcu8/images/scraping-automation/serp-api/parsing-search-results/ext-horizontal-html.png?fit=max&auto=format&n=YUhP5HZ1PAScLcu8&q=85&s=16f222a54a2b965338a3fd5b73e9b61b" alt="Extensions-Horizontal-HTML" width="557" height="139" data-path="images/scraping-automation/serp-api/parsing-search-results/ext-horizontal-html.png" />
                  </Frame>
                </Tab>

                <Tab title="JSON">
                  <Frame>
                                        <img src="https://mintcdn.com/brightdata/YUhP5HZ1PAScLcu8/images/scraping-automation/serp-api/parsing-search-results/ext-horizontal-json.png?fit=max&auto=format&n=YUhP5HZ1PAScLcu8&q=85&s=0a4d332aca0cc1f9b6a4a5a16a0a583f" alt="Extensions-Horizontal-JSON" width="752" height="584" data-path="images/scraping-automation/serp-api/parsing-search-results/ext-horizontal-json.png" />
                  </Frame>
                </Tab>
              </Tabs>
            </Tab>
          </Accordion>

          <Accordion title="display_link">
            These are breadcrumbs from the URL in the result:

            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/YUhP5HZ1PAScLcu8/images/scraping-automation/serp-api/parsing-search-results/display-link-html.png?fit=max&auto=format&n=YUhP5HZ1PAScLcu8&q=85&s=05777421fc7f278377393481b1ff9998" alt="Display-Link-HTML" width="965" height="572" data-path="images/scraping-automation/serp-api/parsing-search-results/display-link-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/YUhP5HZ1PAScLcu8/images/scraping-automation/serp-api/parsing-search-results/display-link-json.png?fit=max&auto=format&n=YUhP5HZ1PAScLcu8&q=85&s=59f365cabcc46d93e9863cfbe93a7d8a" alt="Display-Link-JSON" width="783" height="439" data-path="images/scraping-automation/serp-api/parsing-search-results/display-link-json.png" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="organic">
            Main search results are called organic results and are located in the organic json node.

            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/organic-html.jpg?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=2359f841993d8323dd82ba5e42ce93ec" alt="Orgranic-HTML" width="758" height="734" data-path="images/scraping-automation/serp-api/parsing-search-results/organic-html.jpg" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/organic-json.jpg?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=43a153838b82c410864e4ccbf6f86403" alt="Orgranic-JSON" width="761" height="663" data-path="images/scraping-automation/serp-api/parsing-search-results/organic-json.jpg" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="ads">
            There are four different locations for ads within a SERP and each are parsed separately:

            |               |                                                                                                                                                   |
            | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
            | `top_ads`     | Ads that are located at the top of the SERP                                                                                                       |
            | `top_pla`     | Ads that are located within a special carousel at the top of a SERP                                                                               |
            | `jackpot_pla` | Ads that are located within the right side panel in **shopping** ads. It usually appears when a particular product matches your search perfectly. |
            | `bottom_ads`  | Ads that are located at the bottom of the SERP                                                                                                    |

            <Note>
              By default, SERP API displays "organic" adds (based on IP location and cookies, etc). If you wish SERP API to display ads in different ways (incognito, adtest) you can change this in your SERP API zone on the control panel.
            </Note>

            <AccordionGroup>
              <Accordion title="top_ads">
                <Tabs>
                  <Tab title="HTML">
                    <Frame>
                                            <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/top-ads-html.jpg?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=233e484a58def8f5540d1cef69064100" alt="Top-Ads-HTML" width="751" height="590" data-path="images/scraping-automation/serp-api/parsing-search-results/top-ads-html.jpg" />
                    </Frame>
                  </Tab>

                  <Tab title="JSON">
                    <Frame>
                                            <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/top-ads-json.jpg?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=e40d71257ba83b73f7e5cac677d39a22" alt="Top-Ads-JSON" width="774" height="601" data-path="images/scraping-automation/serp-api/parsing-search-results/top-ads-json.jpg" />
                    </Frame>
                  </Tab>
                </Tabs>
              </Accordion>

              <Accordion title="top_pla">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/top-pla.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=23f1e58cdf782259221774bbab431495" alt="Top-PLA" width="1600" height="471" data-path="images/scraping-automation/serp-api/parsing-search-results/top-pla.png" />
                </Frame>
              </Accordion>

              <Accordion title="jackpot_pla">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/jackpot-pla.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=11b2079beea868e256f90f9ef8f0d17b" alt="Jackpot-PLA" width="1600" height="663" data-path="images/scraping-automation/serp-api/parsing-search-results/jackpot-pla.png" />
                </Frame>
              </Accordion>

              <Accordion title="bottom_ads">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/YUhP5HZ1PAScLcu8/images/scraping-automation/serp-api/parsing-search-results/bottom-ads.png?fit=max&auto=format&n=YUhP5HZ1PAScLcu8&q=85&s=f99a787a808567b9906b40afc0447aa2" alt="Bottom-Ads" width="1600" height="599" data-path="images/scraping-automation/serp-api/parsing-search-results/bottom-ads.png" />
                </Frame>
              </Accordion>
            </AccordionGroup>
          </Accordion>

          <Accordion title="people_also_ask">
            The `people_also_ask` section includes questions Google automatically generates based on queries it believes are related to your question.

            ### `answers`

            In a SERP,  the PAA box questions are connected to answers that users can click to read. This can help people better understand their initial question without clicking on other results. Each question here has its answer under the “answers” element.

            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/people-also-ask-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=ace18d68322b13bde48cb09e7fd0547a" alt="People-Also-Ask-HTML" width="624" height="502" data-path="images/scraping-automation/serp-api/parsing-search-results/people-also-ask-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/people-also-ask-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=89a34b2a8699d78d6758b68d01b213b7" alt="People-Also-Ask-JSON" width="676" height="634" data-path="images/scraping-automation/serp-api/parsing-search-results/people-also-ask-json.png" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="videos">
            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/videos-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=2fdf9bec9ab4e29ea7c7b3d638d8849a" alt="Videos-HTML" width="724" height="639" data-path="images/scraping-automation/serp-api/parsing-search-results/videos-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/videos-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=cacdf6d1e13eb6285cc622f7078414c9" alt="Videos-JSON" width="703" height="648" data-path="images/scraping-automation/serp-api/parsing-search-results/videos-json.png" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="twitter">
            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/twitter-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=97d1b197cd11b74a924a0d730cc27097" alt="Twitter-HTML" width="647" height="301" data-path="images/scraping-automation/serp-api/parsing-search-results/twitter-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/twitter-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=f0b4638bf6d974d42a3c5b18e2531bc0" alt="Twitter-JSON" width="783" height="559" data-path="images/scraping-automation/serp-api/parsing-search-results/twitter-json.png" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="top_stories">
            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/top-stories-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=19a6ab84113fff278bf34a9223946073" alt="Top-Stories-HTML" width="511" height="567" data-path="images/scraping-automation/serp-api/parsing-search-results/top-stories-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/top-stories-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=e41989aeb09f148e297ead20f036c4dc" alt="Top-Stories-JSON" width="786" height="536" data-path="images/scraping-automation/serp-api/parsing-search-results/top-stories-json.png" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="knowledge">
            Provides a brief overview of the searched topic in a knowledge panel (desktop- on the right side, mobile - at the top)

            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/knowledge-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=7426666032fdb9c8f2232317747fea28" alt="Knowledge-HTML" width="479" height="520" data-path="images/scraping-automation/serp-api/parsing-search-results/knowledge-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/knowledge-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=eaeff77b8b048052acb8fd67cc8f535f" alt="Knowledge-JSON" width="305" height="548" data-path="images/scraping-automation/serp-api/parsing-search-results/knowledge-json.png" />
                </Frame>
              </Tab>
            </Tabs>

            ### `widgets`

            |                                           |                   |
            | ----------------------------------------- | ----------------- |
            | `knowledge.widgets.social_media_presence` | includes profiles |
            | `knowledge.widgets.sideways_refinements`  | people also ask   |
          </Accordion>

          <Accordion title="recipes">
            When searching for food items the SERP might contain also recipes

            <Frame>
                            <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/recipes.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=ad406e91a951ced69a49ce5a797a5683" alt="Recipes" width="1600" height="491" data-path="images/scraping-automation/serp-api/parsing-search-results/recipes.png" />
            </Frame>
          </Accordion>

          <Accordion title="snack_pack_map & snack_pack">
            Relates to the Google maps displayed in a SERP.

            ### `snack_pack_map`

            This map part is displayed in the JSON and includes the coordinates of the map location.

            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/snack-pack-map-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=9cb0c409ea92ec8ba867a4657bf53075" alt="Snackpack-Map-HTML" width="687" height="718" data-path="images/scraping-automation/serp-api/parsing-search-results/snack-pack-map-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/snack-pack-map-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=f0b8e5eae6d66ef33e8fbe9182f93e35" alt="Snackpack-Map-JSON" width="798" height="504" data-path="images/scraping-automation/serp-api/parsing-search-results/snack-pack-map-json.png" />
                </Frame>
              </Tab>
            </Tabs>

            ### `snack_pack`

            If the map includes **pins** of specific locations, the JSON will include a `snack_pack` field for each location with additional details like open hours, contact details, tags etc.

            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/snack-pack-map-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=9cb0c409ea92ec8ba867a4657bf53075" alt="Snackpack-HTML" width="687" height="718" data-path="images/scraping-automation/serp-api/parsing-search-results/snack-pack-map-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/snack-pack-map-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=f0b8e5eae6d66ef33e8fbe9182f93e35" alt="Snackpack-JSON" width="798" height="504" data-path="images/scraping-automation/serp-api/parsing-search-results/snack-pack-map-json.png" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="related">
            At the bottom of SERPs, Google also provides users with a “related searches” portion, prompting other search queries related to the initial search.

            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/related-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=fed48c8a4c50b01510227747338b85b5" alt="Related-HTML" width="691" height="301" data-path="images/scraping-automation/serp-api/parsing-search-results/related-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/related-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=36ba5f314c5e502177f30e9739764a45" alt="Related-JSON" width="680" height="688" data-path="images/scraping-automation/serp-api/parsing-search-results/related-json.png" />
                </Frame>
              </Tab>
            </Tabs>

            <Note>
              | `List_group` | Description                                                                   |
              | ------------ | ----------------------------------------------------------------------------- |
              | `true`       | when the elements are grouped as at the top of the following screenshot       |
              | `false`      | when the elements aren't grouped as at the bottom of the following screenshot |

              <Frame>
                                <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/list-group.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=11b9f2e3ee57c61911634a4106283596" alt="List-Group" width="1600" height="520" data-path="images/scraping-automation/serp-api/parsing-search-results/list-group.png" />
              </Frame>
            </Note>
          </Accordion>

          <Accordion title="flights">
            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/flights-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=3a3a985ef667b38907d6b5492b2b87f0" alt="Flights-HTML" width="517" height="379" data-path="images/scraping-automation/serp-api/parsing-search-results/flights-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/flights-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=ea877a51ddf92bfa9f333e9b7549ddab" alt="Flights-JSON" width="771" height="560" data-path="images/scraping-automation/serp-api/parsing-search-results/flights-json.png" />
                </Frame>
              </Tab>
            </Tabs>
          </Accordion>

          <Accordion title="hotels">
            Bright Data's SERP API makes it easy to collect hotel data, like prices, availability, reviews, and more.

            Here's how to collect the data from the hotel knowledge graph using Google Search and how to get even more details from the hotel page on Google Travel.

            When you search for a hotel using Google Search, its details and reviews appear in the resulting knowledge graph on the right.

            <Frame>
                            <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/hotels-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=d0b52cd39528c56a595cdf0f63a756b5" alt="Hotels-HTML" width="1485" height="825" data-path="images/scraping-automation/serp-api/parsing-search-results/hotels-html.png" />
            </Frame>

            Setting arrival and departure dates along with the number of guests lets you see and compare some of the hotel's prices.

            With SERP API, you can set these fields to collect different price combinations using dedicated parameters.

            <Frame>
                            <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/hotels-availability.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=79bbfeba7ebc8b34d76e61c3f4b665e3" alt="Hotels-Availability" width="548" height="666" data-path="images/scraping-automation/serp-api/parsing-search-results/hotels-availability.png" />
            </Frame>

            The SERP API also lets you target the hotel page in Google Travel, where you can find more prices and search by more parameters (including arrival and departure dates, the number of adults and children, the children's ages, and whether or not it has free cancellation) to collect more price combinations. Go to the [API Guide](https://brightdata.com/cp/serp_api/api/google/hotels) to learn more.
          </Accordion>

          <Accordion title="pagination">
            <Tabs>
              <Tab title="HTML">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/pagination-html.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=dbc55cfaedb55f263724fb7822054d77" alt="Pagination-HTML" width="533" height="138" data-path="images/scraping-automation/serp-api/parsing-search-results/pagination-html.png" />
                </Frame>
              </Tab>

              <Tab title="JSON">
                <Frame>
                                    <img src="https://mintcdn.com/brightdata/_dGTsheeDiM8MlIC/images/scraping-automation/serp-api/parsing-search-results/pagination-json.png?fit=max&auto=format&n=_dGTsheeDiM8MlIC&q=85&s=5c01533b27d7d8eecb2347778d2b4852" alt="Pagination-JSON" width="566" height="508" data-path="images/scraping-automation/serp-api/parsing-search-results/pagination-json.png" />
                </Frame>
              </Tab>
            </Tabs>

            Pagination indexes can be found in the bottom JSON section:

            |                                          |                                                          |
            | ---------------------------------------- | -------------------------------------------------------- |
            | `current_page`                           | the requested page location within the search            |
            | `first_page_link`                        | Link of the first page                                   |
            | `prev_page_link`<br />`next_page_link`   | referring to requested page                              |
            | `prev_page_start`<br />`next_page_start` | first searched results number in previous and next pages |
            | `prev_page`<br />`next_page`             | number of pages for previous and next pages              |
            | `page`                                   | page number                                              |
            | `link`                                   | link to page                                             |
            | `start`                                  | first result in the page                                 |
          </Accordion>

          <Accordion title="AI Overview">
            ### `ai_overview`

            Google's Generative [AI Overviews](/scraping-automation/serp-api/query-parameters/google#ai-overview) are shown on various SERPs when the query aligns with topics Google considers suitable for generative answers.

            <Frame>
                            <img src="https://mintcdn.com/brightdata/cdJVb3cg7Aggy8az/images/scraping-automation/serp-api/parsing-search-results/serp-ai-overview.png?fit=max&auto=format&n=cdJVb3cg7Aggy8az&q=85&s=1af3af8a6e4feb3daab1e9f6ccfcadf4" alt="SERP-AI-Overview" width="1299" height="552" data-path="images/scraping-automation/serp-api/parsing-search-results/serp-ai-overview.png" />
            </Frame>

            ## AI Overviews Response Example Schema

            <CodeGroup>
              ```sh Exists theme={null}
              {
                "ai_overview": {
                  "texts": [
                    {
                      "type": "paragraph",
                      "snippet": "To make the best pizza, focus on a good pizza dough, high heat baking, and fresh, high-quality toppings. Start with a slow fermentation for the dough, bake on a hot surface like a pizza stone or baking steel, and use fresh, quality toppings.",
                      "snippet_highlighted_words": "focus on a good pizza dough, high heat baking, and fresh, high-quality toppings",
                      "reference_indexes": [4, 5, 7, 9, 11, 12, 16]
                    },
                    {
                      "type": "paragraph",
                      "snippet": "Here's a more detailed breakdown:"
                    },
                    {
                      "type": "list",
                      "list": [
                        {
                          "type": "paragraph",
                          "snippet": "Slow Fermentation: . Opens in new tabAllow the dough to ferment for a longer period, ideally overnight in the refrigerator. This develops the flavor and makes the crust more chewy and crispy according to Serious Eats and Food & Wine.",
                          "reference_indexes": [2, 3, 6, 22]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Flour Selection: . Opens in new tabUse a combination of bread flour for strength and all-purpose flour for a nice rise.",
                          "reference_indexes": [14]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Dough Preparation: . Opens in new tabStretch the dough carefully to avoid overworking it, which can make it tough.",
                          "reference_indexes": [13]
                        }
                      ],
                      "title": "1. Dough:"
                    },
                    {
                      "type": "list",
                      "list": [
                        {
                          "type": "paragraph",
                          "snippet": "High Heat: Preheat your oven to the highest temperature it can reach, ideally between 450°F and 500°F (232°C and 260°C).",
                          "reference_indexes": [9, 12]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Hot Baking Surface: Use a pizza stone or baking steel to distribute heat evenly and create a crispy crust.",
                          "reference_indexes": [9, 11]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Baking Time: Monitor the pizza closely and bake for 6-15 minutes, depending on the crust thickness and toppings.",
                          "reference_indexes": [9, 12, 17, 21, 23]
                        }
                      ],
                      "title": "2. Baking:"
                    },
                    {
                      "type": "list",
                      "list": [
                        {
                          "type": "paragraph",
                          "snippet": "Layering: Start with the sauce, followed by a layer of cheese, then meats, and finally vegetables.",
                          "reference_indexes": [15]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Fresh Ingredients: Use fresh, high-quality ingredients for the sauce, cheese, and toppings.",
                          "reference_indexes": [0, 4, 18, 20]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Pre-Cooked Toppings: Pre-cook toppings like sausage and vegetables that may not cook completely in the short baking time.",
                          "reference_indexes": [10]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Sauce: Consider using a simple sauce made with fresh crushed tomatoes, garlic, basil, olive oil, and spices.",
                          "reference_indexes": [0, 4]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Cheese: Consider using a combination of low-moisture mozzarella for melting and fresh mozzarella for flavor.",
                          "reference_indexes": [4]
                        }
                      ],
                      "title": "3. Toppings:"
                    },
                    {
                      "type": "list",
                      "list": [
                        {
                          "type": "paragraph",
                          "snippet": "Dough Storage: Store the dough in a bowl, oiled to prevent sticking, and covered tightly with plastic wrap.",
                          "reference_indexes": [2]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Crust: Consider using a baking stone, cast-iron griddle, or perforated pizza pan for a crispier crust.",
                          "reference_indexes": [8, 11]
                        },
                        {
                          "type": "paragraph",
                          "snippet": "Tossing Dough: For a more professional look, consider using the dough tossing technique.",
                          "reference_indexes": [1, 19, 24]
                        }
                      ],
                      "title": "4. Optional but Recommended:"
                    },
                    {
                      "type": "paragraph",
                      "snippet": "This video demonstrates 5 pro chef secrets to the perfect pizza: 57sBigger Bolder Baking with Gemma StaffordYouTube · Jul 18, 2019",
                      "image": {
                        "image": "https://i.ytimg.com/vi/0hqLSZPaThU/mqdefault.jpg?sqp=-oaymwEGCPgEEOQC&rs=AMzJL3ldq2W1-OGaL6qxskwJT0GAYMe_4w",
                        "image_url": "https://i.ytimg.com/vi/0hqLSZPaThU/mqdefault.jpg?sqp=-oaymwEGCPgEEOQC&rs=AMzJL3ldq2W1-OGaL6qxskwJT0GAYMe_4w"
                      }
                    }
                  ],
                  "references": [
                    {
                      "href": "https://www.youtube.com/watch?v=mRx_odAj-XQ&t=147",
                      "title": "The Best Pizza You'll Ever Make | Epicurious 101 - YouTube",
                      "subtitle": "Apr 18, 2023 — and they have a ton of flavor as well i'm using crushed peeled tomatoes. you can use whole peeled or diced tomatoes. w...",
                      "source": "YouTube · Epicurious",
                      "index": 0
                    }
                    // ... more references follow
                  ]
                }
              }
              ```

              ```js Doesn't exist: Warning theme={null}
              {
              //Returned within response headers, displayed when adding `-i` OR `-v` to your request

              `x-brd-warning: AI Overview did not appear on original SERP. Please ensure that you are using the brd_ai_overview=2 query parameter (https://docs.brightdata.com/scraping-automation/serp-api/query-parameters/google#ai-overview), and that your query is relevant for triggering an AI Overview.`
              }
              ```
            </CodeGroup>
          </Accordion>
        </AccordionGroup>
      </Accordion>

      <Accordion title="JSON+HTML" icon="brackets-curly" />

      <Accordion title="Light JSON" icon="brackets-curly">
        ## Light Parser

        Add the `x-unblock-data-format: parsed_light` header to your HTTP requests.

        * Focus on Top 10 results: Extracts only the top 10 organic search results from Google.
        * Optimized speed: Approximately 50% faster latency compared to standard parsing.

        <CodeGroup>
          ```sh Direct API theme={null}
          # Returns a single parsed JSON 
          curl -k --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>:<zone_password> -H "x-unblock-data-format: parsed_light" "https://www.google.com/search?q=pizza"
          ```

          ```sh Native Proxy Interface theme={null}
          # Returns a single parsed JSON 

          curl -X POST https://api.brightdata.com/request \
          --header "Content-Type: application/json" \
          --header "Authorization: Bearer API_KEY" \
          --data '{
            "zone": "serp_api1",
            "url": "https://www.google.com/search?q=pizza",
            "format": "raw",
            "headers": {
              "x-unblock-data-format": "light_json"
            }
          }'
          ```

          ```sh JSON Response theme={null}
          {
          "organic": [
              {
                  "link": "https://en.wikipedia.org/wiki/Pizza",
                  "title": "Pizza",
                  "description": "an Italian, specifically Neapolitan, dish typically consisting of a flat base of leavened wheat-based dough topped with tomato, cheese, and other ingredients",
                  "extensions": [
                      {
                          "type": "site_link",
                          "link": "https://en.wikipedia.org/wiki/Pizzeria",
                          "text": "Pizzeria"
                      },
                      {
                          "type": "site_link",
                          "link": "https://en.wikipedia.org/wiki/Neapolitan_pizza",
                          "text": "Neapolitan pizza"
                      },
                      {
                          "type": "site_link",
                          "link": "https://en.wikipedia.org/wiki/Pizza_Margherita",
                          "text": "Pizza Margherita"
                      },
                      {
                          "type": "site_link",
                          "link": "https://en.wikipedia.org/wiki/Pizza_marinara",
                          "text": "Pizza marinara"
                      }
                  ],
                  "global_rank": 1
              },
              {
                  "link": "https://www.tripadvisor.com/Restaurants-g293763-c31-Luanda_Luanda_Province.html",
                  "title": "THE 10 BEST Pizza Places in Luanda (Updated 2025)",
                  "description": "Pizza il Forno serves delicious pizza, with a thin crust and fresh ingredients... Good pizza in loud surroundings ┬╖ 2. O Toscano. 3.8. (24 ...",
                  "global_rank": 2
              },
              {
                  "link": "https://debonairspizza.co.ao/",
                  "title": "Debonairs Pizza Angola ΓÇô Pizza Sit Down & Delivery Eatery",
                  "description": "A Nossa Hist├│ria ┬╖ Nossas Lojas ┬╖ Promessa de Qualidade. Vamos Conversar. Atendimento ao Cliente ┬╖ Encontre um restaurante.",
                  "global_rank": 6
              },
              {
                  "link": "https://www.foodandwine.com/cooking-techniques/pizza-guide",
                  "title": "The F&W Guide to Making Pizza at Home",
                  "description": "Apr 29, 2025 ΓÇö A super-flavorful and forgiving pizza dough is the key to pro-level pies. Food & Wine Test Kitchen pros share each step for making and ...",
                  "global_rank": 7
              },
              {
                  "link": "https://www.youtube.com/watch?v=4mA54Uy3YGY&pp=0gcJCfwAo7VqN5tD",
                  "title": "Classic New York Pizza At Home",
                  "description": "This is everything you want in New York-style pizza: a crispy crust, a light, foldable center, and bubbling cheese ΓÇö all made right at home.",
                  "global_rank": 8
              },
              {
                  "link": "https://www.pizzahut.com/",
                  "title": "Pizza Hut | Delivery & Carryout - No One OutPizzas The Hut!",
                  "description": "Large Hut Lover's Pizzas. $12.99 each. Limited time only. Additional charge for extra toppings, Pan crust, Stuffed crust, and extra cheese.",
                  "global_rank": 9
              },
              {
                  "link": "https://www.bbcgoodfood.com/recipes/pizza-margherita-4-easy-steps",
                  "title": "Pizza Margherita in 4 easy steps recipe",
                  "description": "Even a novice cook can master the art of perfect pizza with our step-by-step guide. This homemade pizza recipe features a simple pizza dough and toppings.",
                  "global_rank": 10
              },
              {
                  "link": "https://www.facebook.com/PizzaHutAngola/",
                  "title": "Pizza Hut Angola | Luanda",
                  "description": "ROD├ìZIO PIZZA HUT: Γ£ôPizzas Ilimitadas Γ£ôEntrada Γ£ôSobremesa Tudo isso por apenas 15.900Kz por pessoa! Junta os teus, senta, relaxa e deixa a pizza vir at├⌐ ti.",
                  "global_rank": 11
              },
              {
                  "link": "https://www.instagram.com/debonairspizza_ao/?hl=en",
                  "title": "Debonairs Pizza Angola ≡ƒçª≡ƒç┤ (@debonairspizza_ao)",
                  "description": "Refei├º├úo de Valor Uma Pizza pequena de frango ou carne com uma bebida por apenas 3450Kz! Visite-nos no centro shoprite mais perto de ti, aberto todos os dias ...",
                  "global_rank": 12
              }
          ],
          "videos": [
              {
                  "link": "https://www.youtube.com/watch?v=HLfRhp4EGlo",
                  "title": "SECRET TO CRISPY PIZZA AT HOME | ONLY PIZZA RECIPE ...",
                  "global_rank": 3
              },
              {
                  "link": "https://www.youtube.com/watch?v=4mA54Uy3YGY",
                  "title": "Classic New York Pizza At Home",
                  "global_rank": 4
              },
              {
                  "link": "https://www.youtube.com/watch?v=ICHxQHsf7E4",
                  "title": "Creative Pizza Making (Neapolitan Pizzette)",
                  "global_rank": 5
              }
          ]
          }
          ```
        </CodeGroup>
      </Accordion>
    </AccordionGroup>
  </Accordion>
</AccordionGroup>
