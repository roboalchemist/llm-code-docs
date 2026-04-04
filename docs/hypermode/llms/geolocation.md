# Source: https://docs.hypermode.com/dgraph/guides/get-started-with-dgraph/geolocation.md

# Get Started with Dgraph - Geolocation

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

**Welcome to the eight tutorial of getting started with Dgraph.**

In the [previous tutorial](./fuzzy-search), we learned about building a
twitter-like user-search feature using
[Dgraph's fuzzy search](dgraph/dql/functions#fuzzy-matching).

In this tutorial, we'll build a graph of tourist locations around San Francisco
and help our Zoologist friend, Mary, and her team in their mission to conserve
birds using Dgraph's geolocation capabilities.

You might have used Google to find the restaurants near you or to find the
shopping centers within a mile of your current location. Apps like these make
use of your geolocation data.

Geolocation has become an integral part of mobile apps, especially with the
advent of smartphones in the last decade, the list of apps which revolves around
users location to power app features has grown beyond imagination.

Let's take Uber, for instance, the location data of the driver and passenger is
pivotal for the app. We're gathering more GPS data than ever before, being able
to store and query the location data efficiently can give you an edge over your
competitors.

Real-world data is interconnected and they are not sparse. This is even more
relevant when it comes to location data. The natural representation of railway
networks, maps, routes are graphs.

The good news is that Dgraph, the world's most advanced graph database, comes
with functionalities to efficiently store and perform useful queries on graphs
containing location data. If you want to run queries like
`find hotels near Golden Gate Bridge`, or
`find all the tourist location around Golden Gate Park`, Dgraph has your back.

First, let's learn how to represent Geolocation data in Dgraph.

## Representing geolocation data

You can represent location data in Dgraph using two ways:

* **Point location**

Point location contains the geo-coordinate tuple (latitude, longitude) of your
location of interest.

The following image has the point location with the latitude and longitude for
the Eiffel Tower in Paris. Point locations are useful for representing a precise
location. For instance, your location when booking a cab or your delivery
address.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-paris.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=39cec24306a35799527a0db29b6fd153" alt="model" width="610" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/b-paris.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-paris.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d2a6c5db00a4f07511e91b520344ba6e 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-paris.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=8b49a0dd5d77e34a5d7b2012a9adc545 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-paris.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=9e6482664682c18dc01be5605cc0b6f9 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-paris.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=48bd3a0154f2d68d870866527585e85d 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-paris.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d66d835fb887b42be0d427c29bfa8c0b 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-paris.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3940eb4f1c3fbd149bb0c04b051c40f3 2500w" data-optimize="true" data-opv="2" />

* **Polygonal location**

It isn't possible to represent geographical entities which are spread across
multiple geo-coordinates just using a point location. To represent geo entities
like a city, a lake, or a national park, you should use a polygonal location.

Here is an example:

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-delhi.jpg?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d0787fef68189f6aa579473df2f333e9" alt="model" width="741" height="440" data-path="images/dgraph/guides/get-started-with-dgraph/c-delhi.jpg" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-delhi.jpg?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f48c6639591028ebae13ac094324a144 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-delhi.jpg?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=67b0ead5a37b83e9772fda04c05e1cae 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-delhi.jpg?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=bfd86a92c2ac512b8785e24c17691904 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-delhi.jpg?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f2c66e0a73755b941a5ad9a603524ae2 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-delhi.jpg?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e06876d1e8923c9e69ceb33e8ba7222f 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-delhi.jpg?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f4d59c638d35ea01f6d12eb99fea68cd 2500w" data-optimize="true" data-opv="2" />

The polygonal fence above represents the city of Delhi, India. This polygonal
fence or the geo-fence is formed by connecting multiple straight-line
boundaries, and they're collectively represented using an array of location
tuples of format `[(latitude, longitude), (latitude, longitude), ...]`. Each
tuple pair `(2 tuples and 4 coordinates)` represents a straight line boundary of
the geo-fence, and a polygonal fence can contain any number of lines.

Let's start with building a simple San Francisco tourist graph, here's the graph
model.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph.jpg?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7338acc4d9005003212ea8d6b0354b7b" alt="model" width="681" height="471" data-path="images/dgraph/guides/get-started-with-dgraph/a-graph.jpg" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph.jpg?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=02cc5141a04873a1755c5c7f84167331 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph.jpg?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=46dbfdfab7661ad4a9e91b69c2efa285 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph.jpg?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=de067bcaa2ccccd07355125d9d49e4d5 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph.jpg?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3fc36eaeaaf1ab982a4995b88a82555c 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph.jpg?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=bba21a6e71d2d47433b4a465566f0c90 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph.jpg?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6f9e7a5096e82ec048978126df0aa341 2500w" data-optimize="true" data-opv="2" />

The above graph has three entities represented by the nodes:

* **City**

A `city node` represents the tourist city. Our dataset only contains the city of
`San Francisco`, and a node in the graph represents it.

* **Location**

A location node, along with the name of the location, it contains the point or
polygonal location of the place of interest.

* **Location Type**

A location type consists of the type of location. There are four types of
location in our dataset: `zoo`, `museum`, `hotel` or a `tourist attraction`.

The `location nodes` with geo-coordinates of a `hotel` also contains their
pricing information.

There are different ways to model the same graph. For instance, the
`location type` could just be a property or a predicate of the `location node`,
rather than being a node of its own.

The queries you want to perform or the relationships you like to explore mostly
influence the modeling decisions. The goal of the tutorial isn't to arrive at
the ideal graph model, but to use a simple dataset to demonstrate the
geolocation capabilities of Dgraph.

For the rest of the tutorial, let's call the node representing a `City` as a
`city` node, and the node representing a `Location` as a `location` node, and
the node representing the `Location Type` as a `location type` node.

Here's the relationship between these nodes:

* Every `city node` is connected to a `location node` via the `has_location`
  edge.
* Every `location node` is connected to its node representing a `location type`
  via the `has_type` edge.

<Note>
  Dgraph allows you to associate one or more types for the nodes using its type
  system feature, for now, we're using nodes without types, we'll learn about
  type system for nodes in a future tutorial. Read more on the [DQL
  schema](/dgraph/dql/schema) to explore type system feature for nodes
</Note>

Here is our sample dataset. Open Ratel, go to the mutate tab, paste the
mutation, and click Run.

```json
{
  "set": [
    {
      "city": "San Francisco",
      "uid": "_:SFO",
      "has_location": [
        {
          "name": "USS Pampanito",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.4160088, 37.8096674],
                [-122.4161147, 37.8097628],
                [-122.4162064, 37.8098357],
                [-122.4163467, 37.8099312],
                [-122.416527, 37.8100471],
                [-122.4167504, 37.8101792],
                [-122.4168272, 37.8102137],
                [-122.4167719, 37.8101612],
                [-122.4165683, 37.8100108],
                [-122.4163888, 37.8098923],
                [-122.4162492, 37.8097986],
                [-122.4161469, 37.8097352],
                [-122.4160088, 37.8096674]
              ]
            ]
          },
          "has_type": [
            {
              "uid": "_:museum",
              "loc_type": "Museum"
            }
          ]
        },
        {
          "name": "Alameda Naval Air Museum",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.2995054, 37.7813924],
                [-122.2988538, 37.7813582],
                [-122.2988421, 37.7814972],
                [-122.2994937, 37.7815314],
                [-122.2995054, 37.7813924]
              ]
            ]
          },
          "street": "Ferry Point Road",
          "has_type": [
            {
              "uid": "_:museum"
            }
          ]
        },
        {
          "name": "Burlingame Museum of PEZ Memorabilia",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.3441509, 37.5792003],
                [-122.3438207, 37.5794257],
                [-122.3438987, 37.5794587],
                [-122.3442289, 37.5792333],
                [-122.3441509, 37.5792003]
              ]
            ]
          },
          "street": "California Drive",
          "has_type": [
            {
              "uid": "_:museum"
            }
          ]
        },
        {
          "name": "Carriage Inn",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.3441509, 37.5792003],
                [-122.3438207, 37.5794257],
                [-122.3438987, 37.5794587],
                [-122.3442289, 37.5792333],
                [-122.3441509, 37.5792003]
              ]
            ]
          },
          "street": "7th street",
          "price_per_night": 350.0,
          "has_type": [
            {
              "uid": "_:hotel",
              "loc_type": "Hotel"
            }
          ]
        },
        {
          "name": "Lombard Motor In",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.4260484, 37.8009811],
                [-122.4260137, 37.8007969],
                [-122.4259083, 37.80081],
                [-122.4258724, 37.8008144],
                [-122.4257962, 37.8008239],
                [-122.4256354, 37.8008438],
                [-122.4256729, 37.8010277],
                [-122.4260484, 37.8009811]
              ]
            ]
          },
          "street": "Lombard Street",
          "price_per_night": 400.0,
          "has_type": [
            {
              "uid": "_:hotel"
            }
          ]
        },
        {
          "name": "Holiday Inn San Francisco Golden Gateway",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.4214895, 37.7896108],
                [-122.4215628, 37.7899798],
                [-122.4215712, 37.790022],
                [-122.4215987, 37.7901606],
                [-122.4221004, 37.7900985],
                [-122.4221044, 37.790098],
                [-122.4219952, 37.7895481],
                [-122.4218207, 37.78957],
                [-122.4216158, 37.7895961],
                [-122.4214895, 37.7896108]
              ]
            ]
          },
          "street": "Van Ness Avenue",
          "price_per_night": 250.0,
          "has_type": [
            {
              "uid": "_:hotel"
            }
          ]
        },
        {
          "name": "Golden Gate Bridge",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.479784, 37.8288329],
                [-122.4775646, 37.8096291],
                [-122.4775538, 37.8095165],
                [-122.4775465, 37.8093304],
                [-122.4775823, 37.8093296],
                [-122.4775387, 37.8089749],
                [-122.4773545, 37.8089887],
                [-122.4773402, 37.8089575],
                [-122.4772752, 37.8088285],
                [-122.4772084, 37.8087099],
                [-122.4771322, 37.8085903],
                [-122.4770518, 37.8084793],
                [-122.4769647, 37.8083687],
                [-122.4766802, 37.8080091],
                [-122.4766629, 37.8080195],
                [-122.4765701, 37.8080751],
                [-122.476475, 37.8081322],
                [-122.4764106, 37.8081708],
                [-122.476396, 37.8081795],
                [-122.4764936, 37.8082814],
                [-122.476591, 37.8083823],
                [-122.4766888, 37.8084949],
                [-122.47677, 37.808598],
                [-122.4768444, 37.8087008],
                [-122.4769144, 37.8088105],
                [-122.4769763, 37.8089206],
                [-122.4770373, 37.8090416],
                [-122.477086, 37.809151],
                [-122.4771219, 37.8092501],
                [-122.4771529, 37.809347],
                [-122.477179, 37.8094517],
                [-122.4772003, 37.809556],
                [-122.4772159, 37.8096583],
                [-122.4794624, 37.8288561],
                [-122.4794098, 37.82886],
                [-122.4794817, 37.8294742],
                [-122.4794505, 37.8294765],
                [-122.4794585, 37.8295453],
                [-122.4795423, 37.8295391],
                [-122.4796312, 37.8302987],
                [-122.4796495, 37.8304478],
                [-122.4796698, 37.8306078],
                [-122.4796903, 37.830746],
                [-122.4797182, 37.8308784],
                [-122.4797544, 37.83102],
                [-122.479799, 37.8311522],
                [-122.4798502, 37.8312845],
                [-122.4799025, 37.8314139],
                [-122.4799654, 37.8315458],
                [-122.4800346, 37.8316718],
                [-122.4801231, 37.8318137],
                [-122.4802112, 37.8319368],
                [-122.4803028, 37.8320547],
                [-122.4804046, 37.8321657],
                [-122.4805121, 37.8322792],
                [-122.4805883, 37.8323459],
                [-122.4805934, 37.8323502],
                [-122.4807146, 37.8323294],
                [-122.4808917, 37.832299],
                [-122.4809526, 37.8322548],
                [-122.4809672, 37.8322442],
                [-122.4808396, 37.8321298],
                [-122.4807166, 37.8320077],
                [-122.4806215, 37.8319052],
                [-122.4805254, 37.8317908],
                [-122.4804447, 37.8316857],
                [-122.4803548, 37.8315539],
                [-122.4802858, 37.8314395],
                [-122.4802227, 37.8313237],
                [-122.4801667, 37.8312051],
                [-122.4801133, 37.8310812],
                [-122.4800723, 37.8309602],
                [-122.4800376, 37.8308265],
                [-122.4800087, 37.8307005],
                [-122.4799884, 37.8305759],
                [-122.4799682, 37.8304181],
                [-122.4799501, 37.8302699],
                [-122.4798628, 37.8295146],
                [-122.4799157, 37.8295107],
                [-122.4798451, 37.8289002],
                [-122.4798369, 37.828829],
                [-122.479784, 37.8288329]
              ]
            ]
          },
          "street": "Golden Gate Bridge",
          "has_type": [
            {
              "uid": "_:attraction",
              "loc_type": "Tourist Attraction"
            }
          ]
        },
        {
          "name": "Carriage Inn",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.3441509, 37.5792003],
                [-122.3438207, 37.5794257],
                [-122.3438987, 37.5794587],
                [-122.3442289, 37.5792333],
                [-122.3441509, 37.5792003]
              ]
            ]
          },
          "street": "7th street",
          "has_type": [
            {
              "uid": "_:attraction"
            }
          ]
        },
        {
          "name": "San Francisco Zoo",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.5036126, 37.7308562],
                [-122.5028991, 37.7305879],
                [-122.5028274, 37.7305622],
                [-122.5027812, 37.7305477],
                [-122.5026992, 37.7305269],
                [-122.5026211, 37.7305141],
                [-122.5025342, 37.7305081],
                [-122.5024478, 37.7305103],
                [-122.5023667, 37.7305221],
                [-122.5022769, 37.7305423],
                [-122.5017546, 37.7307008],
                [-122.5006917, 37.7311277],
                [-122.4992484, 37.7317075],
                [-122.4991414, 37.7317614],
                [-122.4990379, 37.7318177],
                [-122.4989369, 37.7318762],
                [-122.4988408, 37.731938],
                [-122.4987386, 37.7320142],
                [-122.4986377, 37.732092],
                [-122.4978359, 37.7328712],
                [-122.4979122, 37.7333232],
                [-122.4979485, 37.7333909],
                [-122.4980162, 37.7334494],
                [-122.4980945, 37.7334801],
                [-122.4989553, 37.7337384],
                [-122.4990551, 37.7337743],
                [-122.4991479, 37.7338184],
                [-122.4992482, 37.7338769],
                [-122.4993518, 37.7339426],
                [-122.4997605, 37.7342142],
                [-122.4997578, 37.7343433],
                [-122.5001258, 37.7345486],
                [-122.5003425, 37.7346621],
                [-122.5005576, 37.7347566],
                [-122.5007622, 37.7348353],
                [-122.500956, 37.7349063],
                [-122.5011438, 37.7349706],
                [-122.5011677, 37.7349215],
                [-122.5013556, 37.7349785],
                [-122.5013329, 37.7350294],
                [-122.5015181, 37.7350801],
                [-122.5017265, 37.7351269],
                [-122.5019229, 37.735164],
                [-122.5021252, 37.7351953],
                [-122.5023116, 37.7352187],
                [-122.50246, 37.7352327],
                [-122.5026074, 37.7352433],
                [-122.5027534, 37.7352501],
                [-122.5029253, 37.7352536],
                [-122.5029246, 37.735286],
                [-122.5033453, 37.7352858],
                [-122.5038376, 37.7352855],
                [-122.5038374, 37.7352516],
                [-122.5054006, 37.7352553],
                [-122.5056182, 37.7352867],
                [-122.5061792, 37.7352946],
                [-122.5061848, 37.7352696],
                [-122.5063093, 37.7352671],
                [-122.5063297, 37.7352886],
                [-122.5064719, 37.7352881],
                [-122.5064722, 37.735256],
                [-122.506505, 37.7352268],
                [-122.5065452, 37.7352287],
                [-122.5065508, 37.7351214],
                [-122.5065135, 37.7350885],
                [-122.5065011, 37.7351479],
                [-122.5062471, 37.7351127],
                [-122.5059669, 37.7349341],
                [-122.5060092, 37.7348205],
                [-122.5060405, 37.7347219],
                [-122.5060611, 37.734624],
                [-122.5060726, 37.7345101],
                [-122.5060758, 37.73439],
                [-122.5060658, 37.73427],
                [-122.5065549, 37.7342676],
                [-122.5067262, 37.7340364],
                [-122.506795, 37.7340317],
                [-122.5068355, 37.733827],
                [-122.5068791, 37.7335407],
                [-122.5068869, 37.7334106],
                [-122.5068877, 37.733281],
                [-122.5068713, 37.7329795],
                [-122.5068598, 37.7328652],
                [-122.506808, 37.7325954],
                [-122.5067837, 37.732482],
                [-122.5067561, 37.7323727],
                [-122.5066387, 37.7319688],
                [-122.5066273, 37.731939],
                [-122.5066106, 37.7319109],
                [-122.506581, 37.7318869],
                [-122.5065404, 37.731872],
                [-122.5064982, 37.7318679],
                [-122.5064615, 37.731878],
                [-122.5064297, 37.7318936],
                [-122.5063553, 37.7317985],
                [-122.5063872, 37.7317679],
                [-122.5064106, 37.7317374],
                [-122.5064136, 37.7317109],
                [-122.5063998, 37.7316828],
                [-122.5063753, 37.7316581],
                [-122.5061296, 37.7314636],
                [-122.5061417, 37.731453],
                [-122.5060145, 37.7313791],
                [-122.5057839, 37.7312678],
                [-122.5054352, 37.7311479],
                [-122.5043701, 37.7310447],
                [-122.5042805, 37.7310343],
                [-122.5041861, 37.7310189],
                [-122.5041155, 37.7310037],
                [-122.5036126, 37.7308562]
              ]
            ]
          },
          "street": "San Francisco Zoo",
          "has_type": [
            {
              "uid": "_:zoo",
              "loc_type": "Zoo"
            }
          ]
        },
        {
          "name": "Flamingo Park",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.5033039, 37.7334601],
                [-122.5032811, 37.7334601],
                [-122.503261, 37.7334601],
                [-122.5032208, 37.7334495],
                [-122.5031846, 37.7334357],
                [-122.5031806, 37.7334718],
                [-122.5031685, 37.7334962],
                [-122.5031336, 37.7335078],
                [-122.503128, 37.7335189],
                [-122.5031222, 37.7335205],
                [-122.5030954, 37.7335269],
                [-122.5030692, 37.7335444],
                [-122.5030699, 37.7335677],
                [-122.5030813, 37.7335868],
                [-122.5031034, 37.7335948],
                [-122.5031511, 37.73359],
                [-122.5031933, 37.7335916],
                [-122.5032228, 37.7336022],
                [-122.5032697, 37.7335937],
                [-122.5033194, 37.7335874],
                [-122.5033515, 37.7335693],
                [-122.5033723, 37.7335518],
                [-122.503369, 37.7335068],
                [-122.5033603, 37.7334702],
                [-122.5033462, 37.7334474],
                [-122.5033073, 37.733449],
                [-122.5033039, 37.7334601]
              ]
            ]
          },
          "street": "San Francisco Zoo",
          "has_type": [
            {
              "uid": "_:zoo"
            }
          ]
        },
        {
          "name": "Peace Lantern",
          "location": {
            "type": "Point",
            "coordinates": [-122.4705776, 37.7701084]
          },
          "street": "Golden Gate Park",
          "has_type": [
            {
              "uid": "_:attraction"
            }
          ]
        },
        {
          "name": "Buddha",
          "location": {
            "type": "Point",
            "coordinates": [-122.469942, 37.7703183]
          },
          "street": "Golden Gate Park",
          "has_type": [
            {
              "uid": "_:attraction"
            }
          ]
        },
        {
          "name": "Japanese Tea Garden",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [-122.4692131, 37.7705116],
                [-122.4698998, 37.7710069],
                [-122.4702431, 37.7710137],
                [-122.4707248, 37.7708919],
                [-122.4708911, 37.7701541],
                [-122.4708428, 37.7700354],
                [-122.4703492, 37.7695011],
                [-122.4699255, 37.7693989],
                [-122.4692131, 37.7705116]
              ]
            ]
          },
          "street": "Golden Gate Park",
          "has_type": [
            {
              "uid": "_:attraction"
            }
          ]
        }
      ]
    }
  ]
}
```

*Note: If this mutation syntax is new to you, refer to the
[first tutorial](/introduction) to learn the basics of mutations in Dgraph.*

Run the query below to fetch the entire graph:

```graphql
{
  entire_graph(func: has(city)) {
    city
    has_location {
    name
    has_type {
      loc_type
      }
    }
  }
}
```

*Note: Check the [second tutorial](./basic-operations) if you want to learn more
about traversal queries like the above one.*

Here's our graph!

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-full-graph.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=0033be49c937941416a6baa51be189b2" alt="full graph" width="854" height="382" data-path="images/dgraph/guides/get-started-with-dgraph/d-full-graph.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-full-graph.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=0f74ba4e59bb1d213be2ffb1e8eddd50 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-full-graph.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=66c0f9727bef16b46ec8e80e5bb6f3be 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-full-graph.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=fbd7556f4e8e24494d2350d217b049f0 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-full-graph.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=d0a83cd0e98df1f939a37b1df421612e 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-full-graph.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=0be086a7ec6d0f948ce0fb1ebc9ecd78 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-full-graph.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=8d6659a530c200ac16b68b0d50ac96ee 2500w" data-optimize="true" data-opv="2" />

Our graph has:

* One blue `city node`. We just have one node which represents the city of
  `San Francisco`.
* The green ones are the `location` nodes. We have a total of 13 locations.
* The pink nodes represent the `location types`. We have four kinds of locations
  in our dataset: `museum`, `zoo`, `hotel`, and `tourist attractions`.

You can also see that Dgraph has auto-detected the data types of the predicates
from the schema tab, and the location predicate has been auto-assigned `geo`
type.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-schema.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=2246e69e7b65c24c02ba59d404a4bdcd" alt="type detection" width="854" height="411" data-path="images/dgraph/guides/get-started-with-dgraph/e-schema.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-schema.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=07ce3fde3054514324dd75037f67d778 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-schema.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=a5a792b37aee60b51c80b56584e44e2c 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-schema.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c5447aadace879a545ff851c5d39873f 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-schema.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=855d318afeb52a09d0acf76b76b76dce 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-schema.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=a64132188581832c938ec12690e8bb7e 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-schema.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3c5109665cab152311764eb598fc1041 2500w" data-optimize="true" data-opv="2" />

*Note: Check out the [previous tutorial](./types-and-operations) to know more
about data types in Dgraph.*

Before we start, please say Hello to `Mary`, a zoologist who has dedicated her
research for the cause of conserving various bird species.

For the rest of the tutorial, let's help Mary and her team of zoologists in
their mission to conserving birds.

## Enter San Francisco: Hotel booking

Several research projects done by Mary suggested that Flamingos thrive better
when there are abundant water bodies for their habitat.

Her team got approval for expanding the water source for the Flamingos in the
San Francisco Zoo, and her team is ready for a trip to San Francisco with Mary
remotely monitoring the progress of the team.

Her teammates wish to stay close to the `Golden Gate Bridge` so that they could
cycle around the Golden gate, enjoy the breeze, and the sunrise every morning.

Let's help them find a hotel which is within a reasonable distance from the
`Golden Gate Bridge`, and we'll do so using Dgraph's geolocation functions.

Dgraph provides a variety of functions to query geolocation data. To use them,
you have to set the `geo` index first.

Go to the Schema tab and set the index on the `location` predicate.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-index.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3f11d7dff0f0f4c3d8524a5a30b977fa" alt="geo-index" width="854" height="417" data-path="images/dgraph/guides/get-started-with-dgraph/f-index.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-index.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=0d079f967915ffce600ffc9967500e00 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-index.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=340d04396e2e1cdd61e2a003b5098f3e 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-index.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=620fdd2960fdd9f67468f7d023dd6885 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-index.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=06c079000dc513ab080061c3d70e38bd 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-index.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=238ece1087ea6425fc92d6572b562009 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-index.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=b3969500456a584e55522d559110cbdf 2500w" data-optimize="true" data-opv="2" />

After setting the `geo` index on the `location` predicate, you can use Dgraph's
built-in function `near` to find the hotels near the Golden gate bridge.

Here is the syntax of the `near` function:
`near(geo-predicate, [long, lat], distance)`.

The [`near` function](/dgraph/graphql/schema/directives/search#near) matches and
returns all the geo-predicates stored in the database which are within
`distance meters` of geojson coordinate `[long, lat]` provided by the user.

Let's search for hotels within 7KM of from a point on the Golden Gate bridge.

Go to the query tab, paste the query below and click Run.

```graphql
{
  find_hotel(func: near(location, [-122.479784,37.82883295],7000) )  {
    name
    has_type {
      loc_type
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-near-1.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=8fafb87ff3574c4ab7fdc82b6ccb0efe" alt="geo-index" width="854" height="407" data-path="images/dgraph/guides/get-started-with-dgraph/g-near-1.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-near-1.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=4c6a89a08d095a993e82e6e04876879a 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-near-1.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ab154b7d9b231ada08e8e1b24736954f 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-near-1.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=df70a8ef342ef151f90f18fa3e6f0559 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-near-1.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ce6b45bfb26f9a4c3607a293b212ed76 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-near-1.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=97e2d19a8dc04e56d985d298bbc17837 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-near-1.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=96550e8d41f58a7d5182eb6b0e5d0def 2500w" data-optimize="true" data-opv="2" />

Wait! The search returns not just the hotels, but also all other locations
within 7 Km from the point coordinate on the `Golden Gate Bridge`.

Let's use the `@filter` function to filter for search results containing only
the hotels. You can visit our [third tutorial](./types-and-operations) of the
series to refresh our previous discussions around using the `@filter` directive.

```graphql
{
  find_hotel(func: near(location, [-122.479784,37.82883295],7000)) {
    name
    has_type @filter(eq(loc_type, "Hotel")){
      loc_type
    }
  }
}
```

Oops, we forgot to add an index while using the `eq` comparator in the filter.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-near-2.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f94317e4b76afdf33a21185ce9102902" alt="geo-index" width="854" height="408" data-path="images/dgraph/guides/get-started-with-dgraph/h-near-2.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-near-2.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=80215d1e57be00201d4913b8b88f1eba 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-near-2.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c2230ec13bc260be72d42b4de6319daf 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-near-2.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=1e246421c5db4e88f9270eb79264d8a6 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-near-2.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=d0ab391dbeeb2888234dbb28e12e80e6 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-near-2.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=559f1dff77a8de88ae2b3908690dd45c 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-near-2.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=865ab782b1a76acd5d9f50ef5c5e5549 2500w" data-optimize="true" data-opv="2" />

Let's add a `hash` index to the `loc_type` and re-run the query.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-near-3.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=75e6b73cd6b415bdaa1aff22de80a2b9" alt="geo-index" width="854" height="410" data-path="images/dgraph/guides/get-started-with-dgraph/i-near-3.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-near-3.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ee96956a912cd7f2bb988e18167a251e 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-near-3.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=91da027bf1665d719440944facf3232d 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-near-3.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=4314835657c434e541cf32f53c8fff43 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-near-3.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3569587151871cfd9319d300c60a304e 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-near-3.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3e8d2363f1abe89d7b7793bd11bac3a3 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-near-3.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ac3de4e582712030de44e9d07c85e1dc 2500w" data-optimize="true" data-opv="2" />

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-near-4.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=acbaeb687b099c2da76b997d0e2003ab" alt="geo-index" width="854" height="385" data-path="images/dgraph/guides/get-started-with-dgraph/j-near-4.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-near-4.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=9bcaf59486d625f041100696d7fd9b3b 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-near-4.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=b6e2d2a97b762a174f6b6bdb72e1c85d 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-near-4.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=848123f4a95fbf1f5e02b2306090a398 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-near-4.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=7d1f80a443d8ecb1ae15f9be33016577 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-near-4.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f8300e08f9bffb69d2e278f47d322f7a 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-near-4.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=64c61f89c5bfcef9902f91e08c895ca3 2500w" data-optimize="true" data-opv="2" />

*Note: Refer to the [third tutorial](./types-and-operations) of the series to
learn more about hash index and comparator functions in Dgraph.*

The search result still contains nodes representing locations which are not
hotels. That's because the root query first finds all the location nodes which
are within 7KM from the specified point location, and then it applies the filter
while selectively traversing to the `location type nodes`.

Only the predicates in the location nodes can be filtered at the root level, and
you cannot filter the `location types` without traversing to the
`location type nodes`.

We have the filter to select only the `hotels` while we traverse the
`location type nodes`. Can we cascade or bubble up the filter to the root level,
so that, we only have `hotels` in the final result?

Yes you can! You can do by using the `@cascade` directive.

The `@cascade` directive helps you `cascade` or `bubble up` the filters applied
to your inner query traversals to the root level nodes, by doing so, we get only
the locations of `hotels` in our result.

```graphql
{
  find_hotel(func: near(location, [-122.479784,37.82883295],7000)) @cascade {
   name
   price_per_night
   has_type @filter(eq(loc_type,"Hotel")){
     loc_type
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-near-5.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4ee37102df450628a9b89a19eb49bbee" alt="geo-index" width="854" height="389" data-path="images/dgraph/guides/get-started-with-dgraph/k-near-5.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-near-5.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=97e11a2a55fcaeb25a866acd4346b260 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-near-5.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=9f40b2e2ead8a908dee6e221febca343 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-near-5.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b4d07cbb2cbe99e42f5ac51244c7e53c 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-near-5.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d62a552812ed403a7096a49a4a20c756 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-near-5.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b4546575a3b470588221661c57368fa3 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-near-5.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=935d0b977466aaae5b56f94ee1b517cc 2500w" data-optimize="true" data-opv="2" />

Voila! You can see in the result that, after adding the `@cascade` directive in
the query, only the locations with type `hotel` appear in the result.

We have two hotels in the result, and one of them is over their budget of 300$per night. Let's add another filter to search for Hotels priced below$300 per
night.

The price information of every hotel is stored in the `location nodes` along
with their coordinates, hence the filter on the pricing should be at the root
level of the query, not at the level we traverse the location type nodes.

Before you jump onto run the query, don't forget to add an index on the
`price_per_night` predicate.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-float-index.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=1f8e5decea31bf4ff69e74b43c04233e" alt="geo-index" width="854" height="410" data-path="images/dgraph/guides/get-started-with-dgraph/l-float-index.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-float-index.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=cc526a2553d966d45b3db397ab9e6345 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-float-index.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2b4679cef84c6d34dbca82d2c9a02bc8 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-float-index.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=195564061f97ab03e56f8527e5d1e3b8 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-float-index.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8adc81c1124419a4bfd12d801950fd51 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-float-index.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=cadcecbe00bde470f0e0e427a6839014 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-float-index.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=25d07925acd045a1d945ce225cc277d7 2500w" data-optimize="true" data-opv="2" />

```graphql
{
  find_hotel(func: near(location, [-122.479784,37.82883295],7000)) @cascade @filter(le(price_per_night, 300)){
    name
    price_per_night
    has_type @filter(eq(loc_type,"Hotel")){
      loc_type
    }
  }
}

```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-final-result.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=24c94b177a1e2df4e64d27f4f1baf38e" alt="geo-index" width="854" height="388" data-path="images/dgraph/guides/get-started-with-dgraph/m-final-result.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-final-result.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=f5a64f11d2c73d6279b67746b38b2eb5 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-final-result.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c185d105c150505d458a7ca21251ca36 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-final-result.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=eb605f79f1fad125691a3dfe63bd6248 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-final-result.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=32079ea5ecdf0788d80fd985a0687d2b 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-final-result.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=45e7546dc67f897be48c3469af90cda6 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-final-result.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=34b0262f7086684047f23c89d30d6a18 2500w" data-optimize="true" data-opv="2" />

Now we have a hotel well within the budget, and also close to the Golden Gate
Bridge!

## Summary

In this tutorial, we learned about geolocation capabilities in Dgraph, and
helped Mary's team book a hotel near Golden bridge.

In the next tutorial, we'll showcase more geolocation functionalities in Dgraph
and assist Mary's team in their quest for conserving Flamingo's.

See you all in the next tutorial. Till then, happy Graphing!

Remember to click the "Join our community" button below and subscribe to our
newsletter to get the latest tutorial right into your inbox.

## What's next?

* Go to [Clients](/dgraph/sdks/overview) to see how to communicate with Dgraph
  from your app.
* A wider range of queries can also be found in the
  [Query Language](/dgraph/dql/query) reference.
* See [Deploy](/dgraph/self-managed/overview) if you wish to run Dgraph in a
  cluster.

## Need help

* Please use [discuss.hypermode.com](https://discuss.hypermode.com) for
  questions, feature requests, bugs, and discussions.
