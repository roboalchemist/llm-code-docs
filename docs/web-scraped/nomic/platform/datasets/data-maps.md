# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/

### Data Map Guides

Learn how to use Atlas for data mapping

### Atlas Data Map Controls

Learn about the controls at your fingertips in the Atlas Data Map

## What are Data Maps?​

The Atlas Data Map plots your entire dataset on one screen and organizes it by meaning into clusters. Clusters on your
Atlas Map contain datapoints that are semantically similar. An Atlas Map can search, filter and export data at
scale.

All operations on the Atlas Map browser interface can be executed with the API.

## Use Cases for Data Maps​

- See and explore your text, image, audio and video datasets.
- Cluster and auto-categorize your datasets.
- Discover outlier and anomolous regions in your data.
- Rapidly and collaboratively iterate on your dataset by removing undesired datapoints, applying tags and sharing insights.
An Atlas Map has the following properties:

- Points close to each other on the map are semantically similar/related.
The map clusters your data based on embeddings of your data.
Points close to each other on the map are semantically similar/related.

The map clusters your data based on embeddings of your data.

- Numerical distances between 2D point positions do not have concrete meaning.
Distinct clusters might be close together; related clusters might be far apart. The point of the map is neighborhoods of points and which points are in the same cluster as which other points; the X-Y axes of the map do not have meaning, and the exact distance between points is not meaningful.
Numerical distances between 2D point positions do not have concrete meaning.

Distinct clusters might be close together; related clusters might be far apart. The point of the map is neighborhoods of points and which points are in the same cluster as which other points; the X-Y axes of the map do not have meaning, and the exact distance between points is not meaningful.

- Floating labels correspond to distinct topics in your data.
For example, the Baseball cluster has the label 'Astros win Game 1 of World'. Labels are automatically determined from the textual contents of your data and are crucial for navigating the map. Learn more about how topics labels are generated.
Floating labels correspond to distinct topics in your data.

For example, the Baseball cluster has the label 'Astros win Game 1 of World'. Labels are automatically determined from the textual contents of your data and are crucial for navigating the map. Learn more about how topics labels are generated.

- Topics have a hierarchy.
Topics group your dataset into homogenous regions. As you zoom around the map, more granular versions of your datasets topics will appear.
Topics have a hierarchy.

Topics group your dataset into homogenous regions. As you zoom around the map, more granular versions of your datasets topics will appear.

- Maps update as your data updates.
When new data enters your dataset, Atlas can rebuild the map to reflect how the new data relates to existing data.
Maps update as your data updates.

When new data enters your dataset, Atlas can rebuild the map to reflect how the new data relates to existing data.

- Built for collaboration across technical and non-technical teams.
All information and operations that are visually presented on an Atlas Map have a programmatic analog. For example, engineers can access cluster ids, topic information, duplicate clusters and run vector search through the Python client.
Built for collaboration across technical and non-technical teams.

All information and operations that are visually presented on an Atlas Map have a programmatic analog. For example, engineers can access cluster ids, topic information, duplicate clusters and run vector search through the Python client.

- What are Data Maps?
- Use Cases for Data Maps
