# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/guides/create-your-own-atlas-data-story

This guide will walk you through how to turn your Atlas Data Map into an interactive scrollable story.

Prerequisites:

• An Atlas account, which you can create for free here

• An Atlas Data Map you want to create a story from

## Instructions​

### 1. Install​

Install the Atlas Stories React package and import the required components in your React file:

```
npm install @nomic-ai/atlas-stories-react
```

```
import { Scrollyteller, Folio } from '@nomic-ai/atlas-stories-react';import '@nomic-ai/atlas-stories-react/dist/style.css';
```

### 2. Explore​

You'll likely iterate back and forth between the step 2. Explore and the step 3. Write as you develop your story.

```
2. Explore
```

```
3. Write
```

Explore your data in Atlas and generate share links for each different view of your data that you want to include in your story.

To get a share link:

• Click "Share" in the top-right corner of the Atlas interface

• Copy the generated link, which will be in this format:
https://atlas.nomic.ai/data/ORG_NAME/MAP_NAME/map/MAP_ID#XXXX

```
https://atlas.nomic.ai/data/ORG_NAME/MAP_NAME/map/MAP_ID#XXXX
```

• Note the four-character code at the end (e.g., #vYoe or #r6H8) - you'll need this for your folios

```
#vYoe
```

```
#r6H8
```

Your browser does not support the video tag.

### 3. Write​

Write your story using the Scrollyteller and Folio components.

```
Scrollyteller
```

```
Folio
```

Scrollyteller

The Scrollyteller component will wrap your entire story.

```
Scrollyteller
```

Each Scrollyteller requires a map parameter containing a URL to your Atlas map in the format YOUR_ORGANIZATION/MAP_NAME/map/MAP_ID (this is the bulk of the generated share link, so you can copy a share link here and delete the https://atlas.nomic.ai/data prefix and the four-item #XXXX code suffix).

```
Scrollyteller
```

```
map
```

```
YOUR_ORGANIZATION/MAP_NAME/map/MAP_ID
```

```
https://atlas.nomic.ai/data
```

```
#XXXX
```

```
<Scrollyteller map='YOUR_ORG/MAP_NAME/map/MAP_ID'>...the folios will go in here...</Scrollyteller>
```

Folio

The Folio components you create will represent each state in your story.

```
Folio
```

Each Folio requires a hash: the four-digit code from the Share links you generate.

```
Folio
```

```
hash
```

Here is how to create a basic Folio:

```
<Folio hash="XXXX">Your folio content...</Folio>
```

Additionally, here are optional parameters for a Folio:

```
Folio
```

- duration: Number - Transition time in milliseconds between folios (default: 1000)
```
duration
```

- zoom: Object - Specify custom view coordinates (default: whatever the current zoom state was in the Atlas data map interface when you generated your Atlas share link)
```
zoom
```

Here is how to make a Folio with these optional parameters:

```
<Folio hash="XXXX" duration={2000} zoom={{ x: [-55, 55], y: [-55, 55] }}>Your folio content...</Folio>
```

Here's what your React file should look like with your components:

```
import { Scrollyteller, Folio } from '@nomic-ai/atlas-stories-react';import '@nomic-ai/atlas-stories-react/dist/style.css';<Scrollyteller map='YOUR_ORG/MAP_NAME/map/MAP_ID'><Folio hash="vYoe">Your first folio content...</Folio><Folio hash="oZyE">Your second folio content...</Folio>...<Folio hash="r6H8">Your last folio content...</Folio></Scrollyteller>
```

### 4. View​

Run your React app using npm run or your equivalent.

```
npm run
```

On page load you will then see each Atlas map state to the side of your Folio text:

Your browser does not support the video tag.

## Example GitHub Repository​

We've set up this public GitHub repository that you can use as an example for how to set up your Data Story in React. The most relevant file is app/page.tsx.

```
app/page.tsx
```

## Additional Features​

### Topic Labels (beta)​

To get topic labels to appear over the map in your story, include this baseURL parameter value when initializing your Scrollyteller component:

```
baseURL
```

```
Scrollyteller
```

```
<Scrollyteller map='YOUR_ORG/MAP_NAME/map/MAP_ID' baseURL="https://atlas-next-test-prod.vercel.app">...the folios will go in here...</Scrollyteller>
```

- Instructions1. Install2. Explore3. Write4. View
- 1. Install
- 2. Explore
- 3. Write
- 4. View
- Example GitHub Repository
- Additional FeaturesTopic Labels (beta)
- Topic Labels (beta)
