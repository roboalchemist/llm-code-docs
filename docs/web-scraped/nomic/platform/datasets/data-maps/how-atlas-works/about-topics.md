# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/how-atlas-works/about-topics

The annotation layer of Atlas generates topics for your data.

- Atlas automatically builds clusters over uploaded data by applying a hierarchical clustering model over data vectors in the (high-dimensional) latent space.
- Atlas auto-labels each cluster with a custom-trained large language model that synthesizes a short topical description for each topic/cluster.
The topic labeling system in Atlas will generate topics at either two or three depth levels depending on the granularity of your dataset.

- Topic Depth 1: Most general
- Topic Depth 2: Between general and specific
- Topic Depth 3: Most specific (only generated for highly granular datasets)
## Example: News Topic Modeling​

For example, we can see a conceptual example of how Atlas auto-labeling works on a toy dataset of news articles. From the raw data, Atlas will generate clusters and names for those clusters.

Toy Dataset of News Articles:

- Sen. Hawley calls on Biden to suspend support for Ukraine NATO membership
- The Fed Is Poised to Cut Rates Again. Here's What to Watch.
- House Poised to Approve $13.6 Billion in Emergency Aid for Ukraine
- Five Ways the United States Can Still Fight Climate Change
- Biden approves more anti-aircraft systems, drones for Ukraine, warns of long and difficult battle
- UK prime minister says no immediate plans to send British troops to Ukraine
- Binance Faces Mounting Pressure as U. S. Crypto Crackdown Intensifies
- Moody Buys Climate Data Firm, Signaling New Scrutiny of Climate Risks
- Opinion | Glasgow Delegates Should Focus on More Than Methane
Atlas takes each headline and embeds it into vectors using a language model. Based on the embeddings of these articles, statistical clustering algorithms on these (news articles as) vectors results in 3 categories. In order of relative size, these clusters are:

Cluster A:

- Biden approves more anti-aircraft systems, drones for Ukraine, warns of long and difficult battle
- Sen. Hawley calls on Biden to suspend support for Ukraine NATO membership
- House Poised to Approve $13.6 Billion in Emergency Aid for Ukraine
- UK prime minister says no immediate plans to send British troops to Ukraine
Cluster B:

- The Fed Is Poised to Cut Rates Again. Here's What to Watch.
- Binance Faces Mounting Pressure as U. S. Crypto Crackdown Intensifies
- Pier 1 Imports to Close Up to 450 Stores and Cut Jobs
Cluster C:

- Five Ways the United States Can Still Fight Climate Change
- Opinion | Glasgow Delegates Should Focus on More Than Methane
Next, Atlas auto-labels each cluster. Atlas uses a combination of computational linguistics and a large language model to synthesize a short topical description for each cluster.

These labels will thematically describe the content of each cluster as a whole, which creates more human-readable label names than just listing the most frequent keywords or picking the most demonstrative title of the cluster. It's possible that the topic labeling algorithm may even generate topic labels which do not contain any of the words from text but succinctly describe the content as a whole.

So, Atlas topic labels for our data clusters could look like:

Aid to Ukraine:

- Biden approves more anti-aircraft systems, drones for Ukraine, warns of long and difficult battle
- Sen. Hawley calls on Biden to suspend support for Ukraine NATO membership
- House Poised to Approve $13.6 Billion in Emergency Aid for Ukraine
- UK prime minister says no immediate plans to send British troops to Ukraine
Economy and Jobs:

- The Fed Is Poised to Cut Rates Again. Here's What to Watch.
- Binance Faces Mounting Pressure as U. S. Crypto Crackdown Intensifies
- Pier 1 Imports to Close Up to 450 Stores and Cut Jobs
Climate Change:

- Five Ways the United States Can Still Fight Climate Change
- Opinion | Glasgow Delegates Should Focus on More Than Methane
For thousands or millions of news articles, Atlas would have many more clusters at different levels of hierarchy. For example, the articles in the Economy and Jobs cluster could be further clustered into more specific sub-topics, like “Unemployment”, “International trade relations”, “Personal finance”, and “Startups,” and these would be reflected on the map.

## Further Examples of Hierarchical Topic Models​

Here are some other examples of unstructured data that gets structured in real life in a hierarchical topic model:

- The grocery store: A grocery store organizes thousands of individual products into sections like produce, dairy, frozen goods, and baked goods based on the temperature, taste, type, culinary use, and origin of food and drink products. Often, there is an order within each section: the baked goods section may keep sweet and savory items separate.
The grocery store: A grocery store organizes thousands of individual products into sections like produce, dairy, frozen goods, and baked goods based on the temperature, taste, type, culinary use, and origin of food and drink products. Often, there is an order within each section: the baked goods section may keep sweet and savory items separate.

- The library: A library is organized by different attributes of its many books. The Dewey Decimal System divides books up into ten main classes of content like history, science, and the arts, and these get arranged around the library's stacks. Libraries could also be organized by last name of author, genre, reading-level, and more.
The library: A library is organized by different attributes of its many books. The Dewey Decimal System divides books up into ten main classes of content like history, science, and the arts, and these get arranged around the library's stacks. Libraries could also be organized by last name of author, genre, reading-level, and more.

- Example: News Topic Modeling
- Further Examples of Hierarchical Topic Models
