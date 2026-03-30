# Execute main function
asyncio.run(main())
```

```json  theme={null}
Enter the city you want to travel to: Paris
Enter the start date of your travel: 01, April 2025
Enter the number of days for your trip: 5

ORIGINAL PROMPT: Generate a 5-day travel itinerary for Paris, tailored to the real-time weather forecast for the selected date: 01, April 2025. Follow these steps:

Determine Current Date and Travel Period:
Use Dappier's real-time search to identify the current date and calculate the trip duration based on user input.

Fetch LifeStyle News:
Retrieve LifeStyle news using Dappier AI Recommendations API for the given date and provide insight to the user.

Fetch Weather Data:
Retrieve the weather forecast for Paris during the selected dates to understand the conditions for each day.

Fetch Live Events Data:
Use Dappier's real-time search to find live events happening in Paris during the trip dates.

Fetch Hotel Deals Data:
Use Dappier's real-time search to find the best hotel deals with booking links in Paris during the trip dates.

Design the Itinerary:
Use the weather insights, live events, hotel deals to plan activities and destinations that suit the expected conditions. For each suggested location:

Output:
Present latest life style news at first then. Present a detailed 5-day itinerary, including timing, activities, booking links, weather information for each day and travel considerations. Ensure the plan is optimized for convenience and enjoyment.



=== Streaming Start ===


CALLING TOOL - dappier_real_time_search: am_01j0rzq4tvfscrgzwac7jv1p4c

Query: current date

CALLING TOOL: dappier_ai_recommendations: dm_01j0q82s4bfjmsqkhs3ywm3x6y

Query: Paris lifestyle news

CALLING TOOL - dappier_real_time_search: am_01j0rzq4tvfscrgzwac7jv1p4c

Query: Paris weather April 1-5, 2025

CALLING TOOL - dappier_real_time_search: am_01j0rzq4tvfscrgzwac7jv1p4c

Query: Paris live events April 1-5, 2025

CALLING TOOL - dappier_real_time_search: am_01j0rzq4tvfscrgzwac7jv1p4c

Query: Paris hotel deals April 1-5, 2025

### Latest Lifestyle News Highlights

#### Justin Bieber's Heartfelt Message
- **Title:** Christian Singer Justin Bieber, 31, Issues Heartbreaking Message To Fans Amidst Concerns For His Wellbeing
- **Summary:** Justin Bieber addresses mental health struggles in a candid message to fans, sharing feelings of inadequacy despite his fame.
- **Link:** [Read more](https://www.themix.net/celebrity/celebrity-news/christian-singer-justin-bieber-31-issues-heartbreaking-message-to-fans-amidst-concerns-for-his-wellbeing/)

#### Controversies in Disney's Live-Action Snow White
- **Title:** Live-Action Snow White Continues to Have Issues as Disney Scales Back Premiere
- **Summary:** Disney's adaptation faces hurdles and mixed reactions due to casting choices and character portrayal.
- **Link:** [Read more](https://www.themix.net/movies/movie-news/live-action-snow-white-continues-to-have-issues-as-disney-scales-back-premiere/)

#### Family-Favorite Baked Ziti Recipe
- **Title:** Family-Favorite Baked Ziti: Simple, Satisfying, and Oh-So-Good
- **Summary:** Discover a delicious and easy-to-make baked ziti recipe that's perfect for family gatherings.
- **Link:** [Read more](https://www.familyproof.com/lifestyle/food-drink/baked-ziti/)

### 5-Day Paris Travel Itinerary (April 1-5, 2025)

#### Weather Overview
- **April 1-5:** Mild temperatures (12-14°C / 54-57°F), partly cloudy. Ideal for outdoor activities and exploration.

#### Day 1: Explore Paris and Join the Marathon
- **Morning:** Breakfast at Café de Flore. Explore Saint-Germain-des-Prés.
- **Afternoon:** Participate or watch the Paris Marathon. Visit Eiffel Tower post-event.
- **Evening:** Dinner at Le Jules Verne with Eiffel Tower views.

#### Day 2: Art and Design Immersion
- **Morning:** Visit Pad Paris - Art + Design Fair.
- **Afternoon:** Explore the Art Paris Art Fair at Grand Palais.
- **Evening:** Candlelight concert at Sainte-Chapelle. Book [here](https://linkparis.com).

#### Day 3: Cultural Experiences
- **Morning:** Tour the Louvre Museum. Don’t miss the Mona Lisa and other major works.
- **Afternoon:** Lunch at Angelina’s. Discover Musée d'Orsay's art.
- **Evening:** Dinner at a local bistro in Montmartre.

#### Day 4: Scenic Views and Relaxation
- **Morning:** Visit Palais Garnier and take a guided tour.
- **Afternoon:** Enjoy a Seine River Cruise with lunch.
- **Evening:** Explore Le Marais district. Dinner at Chez Janou.

#### Day 5: Quirky Fun and Departure
- **Morning:** Participate in International Pillow Fight Day.
- **Afternoon:** Last-minute shopping at Galeries Lafayette.
- **Evening:** Departure preparation. Stay at Mercari Hotel ([Booking Link](https://www.mercari.com/us/item/m11634459421/)).

### Hotel Deals
- **Stay Option:** 5-Day, 4-Night Package at $1,750 from [LinkParis](https://linkparis.com/5-day-trip-to-paris/).
- **Alternative Stay:** Hotel rooms starting at $120 through [Mercari](https://www.mercari.com/us/item/m11634459421/).

Experience a mix of culture, relaxation, and excitement in Paris. Enjoy your trip! 🇫🇷✨

=== Streaming Complete ===
```

***

## Conclusion

This notebook provides a structured guide to building an AI-powered **travel itinerary assistant** using **OpenAI Agents SDK** and **Dappier**.

It covers:

* **Secure API key storage** using `getpass`
* **Real-time data retrieval** for weather, events, and hotels
* **AI-powered recommendations** for lifestyle insights
* **An agent-driven workflow** to generate structured travel plans

This AI assistant can be extended further by integrating **flight search APIs, restaurant recommendations**, and **personalized travel preferences**.