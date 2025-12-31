# Source: https://lynxjs.org/rspeedy/start/tutorial-gallery.md

# Source: https://lynxjs.org/react/start/tutorial-gallery.md

# Source: https://lynxjs.org/guide/start/tutorial-gallery.md

# Tutorial: Product Gallery


We will build a product gallery page together during this tutorial. This tutorial does not assume any existing Lynx knowledge. The techniques you'll learn in the tutorial are fundamental to building any Lynx pages and applications.

:::note

This tutorial is designed for people who prefer to learn by doing and want to quickly try making something tangible. If you prefer learning each concept step by step, start with [Describing the UI](/guide/ui/elements-components.md).

:::

## What are we building?

Let's first have a look at the result! To see the page live, download and install [LynxExplorer](/guide/start/quick-start.md#ios-simulator-platform=macos-arm64,explorer-platform=ios-simulator) on your device, then scan the generated QR code below.

**This is an example below:  gallery**

**Entry:** `src/GalleryComplete.tsx`
**Bundle:** `dist/GalleryComplete.lynx.bundle` | Web: `dist/GalleryComplete.web.bundle`

```tsx {6}
import { root } from "@lynx-js/react";
import { furnituresPictures } from "../Pictures/furnitures/furnituresPictures.jsx";
import Gallery from "./Gallery.jsx";

function GalleryComplete() {
  return <Gallery pictureData={furnituresPictures} />;
}

root.render(<GalleryComplete />);

```



## Setup for the tutorial

Check out our detailed [quick start](/guide/start/quick-start.md) doc that will guide you through creating a new Lynx project.

You may notice that the project is using TypeScript. Although Lynx and ReactLynx support both TypeScript and plain JavaScript, we recommend TypeScript for a better development experience, provided by static type checking and better editor IntelliSense.

You'll see lots of beautiful images throughout this guide. We've put together a package of sample images you can download [here](https://lf-lynx.tiktok-cdns.com/obj/lynx-artifacts-oss-sg/lynx-website/download/Pictures.tar.gz) to use in your projects.

## Adding Styles

Since the focus of this tutorial is not on how to style your UI, you may just save some time and directly copy the below `index.css` file:

<CodeFold toggle>
  ```css title="index.css"
  .gallery-wrapper {
    height: 100vh;
    background-color: black;
  }

  .single-card {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .scrollbar {
    position: absolute;
    right: 7px;
    z-index: 1000;
    width: 4px;
    background: linear-gradient(to bottom, #ff6448, #ccddff, #3deae7);
    border-radius: 5px;
    overflow: hidden;
    box-shadow:
      0px 0px 4px 1px rgba(12, 205, 223, 0.4),
      0px 0px 16px 5px rgba(12, 205, 223, 0.5);
  }

  .scrollbar-effect {
    width: 100%;
    height: 80%;
  }

  .glow {
    background-color: #333;
    border-radius: 4px;
    background: linear-gradient(
      45deg,
      rgba(255, 255, 255, 0) 20%,
      rgba(255, 255, 255, 0.8) 50%,
      rgba(255, 255, 255, 0) 80%
    );
    animation: flow 3s linear infinite;
  }

  @keyframes flow {
    0% {
      transform: translateY(-100%);
    }
    100% {
      transform: translateY(100%);
    }
  }

  .list {
    width: 100vw;
    padding-bottom: 20px;
    padding-left: 20px;
    padding-right: 20px;
    height: calc(100% - 48px);
    list-main-axis-gap: 10px;
    list-cross-axis-gap: 10px;
  }

  .picture-wrapper {
    border-radius: 10px;
    overflow: hidden;
    width: 100%;
  }

  .like-icon {
    position: absolute;
    display: grid;
    justify-items: center;
    align-items: center;
    top: 0px;
    right: 0px;
    width: 48px;
    height: 48px;
  }

  .heart-love {
    width: 16px;
    height: 16px;
  }

  .circle {
    position: absolute;
    top: calc(50% - 8px);
    left: calc(50% - 8px);
    height: 16px;
    width: 16px;
    border: 2px solid red;
    border-radius: 50%;
    transform: scale(0);
    opacity: 1;
    animation: ripple 1s 1 ease-out;
  }

  .circleAfter {
    animation-delay: 0.5s;
  }

  @keyframes ripple {
    0% {
      transform: scale(1);
      opacity: 1;
    }
    100% {
      transform: scale(2);
      opacity: 0;
    }
  }
  ```
</CodeFold>

and import it as a global styles:

```js
import '../index.scss';
```

This make sure your UI look great when you are following this tutorial.

:::info Styling variations in Lynx
Lynx supports a wide variaties of styling features, including global styles, CSS Modules, inline styles, Sass, CSS variables, and more! Please refer to [Rspeedy - Styling](/rspeedy/styling.md) page for how to pick your best styling configurations.
:::

## Your First Component: An Image Card

Now, let's start by creating the first image card, which will be the main part of this page.

**This is an example below:  gallery**

**Entry:** `src/FirstImageCard`
**Bundle:** `dist/FirstImageCard.lynx.bundle` | Web: `dist/FirstImageCard.web.bundle`

```tsx {11}
import { furnituresPictures } from "../Pictures/furnitures/furnituresPictures.jsx";
import ImageCard from "./ImageCard.jsx";
import "../index.scss";

import { root } from "@lynx-js/react";

function FirstImageCard() {
  const MyFirstPicture = furnituresPictures[0];
  return (
    <view className="gallery-wrapper single-card">
      <ImageCard picture={MyFirstPicture} />
    </view>
  );
}

root.render(<FirstImageCard />);

```



Great, you can now see the image card displayed. Here, we use the [`<image>`](/api/elements/built-in/image.md) element to display your image. You only need to give it a width and height (or specify the aspectRatio property as shown here), and it will automatically resize to fit the specified dimensions.
This component can receive a picture property, allowing you to change the image it displays. In fact, all components can receive external inputs like this, giving you control over them.

:::details The src Attribute of Images
The Lynx `<image>` element can accept a local relative path as the `src` attribute to render an image, which is the most important attribute of the `<image>` element. All images in this page are sourced locally, and these paths need to be imported before use.

However, if your images are stored online, you can easily replace them with web image addresses by changing the value of the src attribute to the corresponding web image link.
:::

## Adding interactivity: Like an Image Card

We can add a small white heart in the upper right corner and make it the like button for the image card. Here, we implement a small component called `LikeIcon`:

**This is an example below:  gallery**

**Entry:** `src/Components`
**Bundle:** `dist/LikeImageCard.lynx.bundle` | Web: `dist/LikeImageCard.web.bundle`

```tsx {7-10,13-15}
import { useState } from "@lynx-js/react";
import redHeart from "../Pictures/redHeart.png";
import whiteHeart from "../Pictures/whiteHeart.png";
import "../index.scss";

export default function LikeIcon() {
  const [isLiked, setIsLiked] = useState(false);
  const onTap = () => {
    setIsLiked(true);
  };
  return (
    <view className="like-icon" bindtap={onTap}>
      {isLiked && <view className="circle" />}
      {isLiked && <view className="circle circleAfter" />}
      <image src={isLiked ? redHeart : whiteHeart} className="heart-love" />
    </view>
  );
}

```



We want each card to know whether it has been liked, so we added isLiked, which is its internal data. It can use this internal data to save your changes.

```tsx title="LikeIcon.tsx" {2}
...
  const [isLiked, setIsLiked] = useState(false);
...
```

Then we add the bindtap event to `<image>`, so that when the user clicks the heart, it triggers this event and changes the state of `isLiked`:

```tsx title="LikeIcon.tsx" {3,7}
...
  const onTap = () => {
    setIsLiked(true);
  }
  return (
      ...
      <image bindtap={onTap}/>
  )
...
```

:::details What is "bindtap"?
If you come from a web development background, you might be more familiar with naming conventions like onclick (HTML attribute) or onClick (in the React community). Lynx follows a different convention: due to the static nature of its architecture, it uses `bind*` and `catch*`. Learn more on the [Event Handling](/guide/interaction/event-handling.md) page.
:::

Finally, we use `isLiked` to control the like effect. Because isLiked is a state, `LikeIcon` will respond to its changes, turning into a red like icon, and the `<view>` used to render the animation effect will be conditionally rendered:

```tsx title="LikeIcon.tsx"
...
  return
    ...
      {isLiked && <view className="circle" />}
      {isLiked && <view className="circle circleAfter" />}
      <image src={isLiked ? redHeart : whiteHeart} />
...
```

To give this like a better visual interaction effect, we added animations, which are all in index.css. You can also learn more about animations in the [Animation](/guide/styling/animation.md) section. Then replace it with your preferred style!

## Displaying More Images with `<list>`

To show all your beautiful images, you may need help from `<list>`. This way, you will get a scrollable page that displays a large number of similar images:

**This is an example below:  gallery**

**Entry:** `src/CreateGallery`
**Bundle:** `dist/CreateGallery.lynx.bundle` | Web: `dist/CreateGallery.web.bundle`

```tsx {11,19,24}
import type { Picture } from "../Pictures/furnitures/furnituresPictures.jsx";
import "../index.scss";
import LikeImageCard from "../Components/LikeImageCard.jsx";
import { calculateEstimatedSize } from "../utils.jsx";

export const Gallery = (props: { pictureData: Picture[] }) => {
  const { pictureData } = props;

  return (
    <view className="gallery-wrapper">
      <list
        className="list"
        list-type="waterfall"
        column-count={2}
        scroll-orientation="vertical"
        custom-list-name="list-container"
      >
        {pictureData.map((picture: Picture, index: number) => (
          <list-item
            estimated-main-axis-size-px={calculateEstimatedSize(picture.width, picture.height)}
            item-key={"" + index}
            key={"" + index}
          >
            <LikeImageCard picture={picture} />
          </list-item>
        ))}
      </list>
    </view>
  );
};

export default Gallery;

```



:::details Special child elements of list
Each child component of `<list>` needs to be `<list-item>`, and you must specify a unique and non-repeating key and item-key attribute, otherwise it may not render correctly.
:::

Of course, we also provide other scrolling elements, such as `<scroll-view>`, to achieve similar effects. Here, we use a waterfall layout as the child node layout option. `<list>` also accepts other layout types, which you can refer to in [list](/api/elements/built-in/list.md).

:::info
You can refer to this [Scrolling](/guide/ui/scrolling.md) documentation to learn more about scrolling and scrolling elements.
:::

## Auto-Scrolling via Element Methods

If you want to create a desktop photo wall, you need to add an auto-scroll feature to this page. Your images will be slowly and automatically scrolled, allowing you to easily see more images:

**This is an example below:  gallery**

**Entry:** `src/AddAutoScroll`
**Bundle:** `dist/AddAutoScroll.lynx.bundle` | Web: `dist/AddAutoScroll.web.bundle`

```tsx {10,12-22,27}
import "../index.scss";
import { useEffect, useRef } from "@lynx-js/react";
import type { NodesRef } from "@lynx-js/types";
import LikeImageCard from "../Components/LikeImageCard.jsx";
import type { Picture } from "../Pictures/furnitures/furnituresPictures.jsx";
import { calculateEstimatedSize } from "../utils.jsx";

export const Gallery = (props: { pictureData: Picture[] }) => {
  const { pictureData } = props;
  const galleryRef = useRef<NodesRef>(null);

  useEffect(() => {
    galleryRef.current
      ?.invoke({
        method: "autoScroll",
        params: {
          rate: "60",
          start: true,
        },
      })
      .exec();
  }, []);

  return (
    <view className="gallery-wrapper">
      <list
        ref={galleryRef}
        className="list"
        list-type="waterfall"
        column-count={2}
        scroll-orientation="vertical"
        custom-list-name="list-container"
      >
        {pictureData.map((picture: Picture, index: number) => (
          <list-item
            estimated-main-axis-size-px={calculateEstimatedSize(picture.width, picture.height)}
            item-key={"" + index}
            key={"" + index}
          >
            <LikeImageCard picture={picture} />
          </list-item>
        ))}
      </list>
    </view>
  );
};

export default Gallery;

```



We use the `useEffect` hook to call the [`autoScroll`](/api/elements/built-in/list.md#autoscroll) method.

```tsx title="Gallery.tsx"
useEffect(() => {
  listRef.current
    ?.invoke({
      method: 'autoScroll',
      params: {
        rate: '60',
        start: true,
      },
    })
    .exec();
}, []);
```

:::details What is "invoke"?
In Lynx, all native elements have a set of "methods" that can be called via their ref. Unlike on the web, this call is asynchronous, similar to message passing. You need to use invoke with the method name method and parameters param to call them.
:::

## How about a Custom Scrollbar?

Like most apps, we can add a scrollbar to this page to indicate how many images are left to be displayed. But we can do more! For example, we can replace the default progress bar of `<list>` with our preferred style:

**This is an example below:  gallery**

**Entry:** `src/AddNiceScrollbar`
**Bundle:** `dist/AddNiceScrollbar.lynx.bundle` | Web: `dist/AddNiceScrollbar.web.bundle`

```tsx {14-19,37,45-46,50}
import "../index.scss";
import { useEffect, useRef } from "@lynx-js/react";
import type { ScrollEvent } from "@lynx-js/types";
import type { NodesRef } from "@lynx-js/types";
import LikeImageCard from "../Components/LikeImageCard.jsx";
import type { Picture } from "../Pictures/furnitures/furnituresPictures.jsx";
import { calculateEstimatedSize } from "../utils.jsx";
import { NiceScrollbar, type NiceScrollbarRef } from "./NiceScrollbar.jsx";

export const Gallery = (props: { pictureData: Picture[] }) => {
  const { pictureData } = props;
  const scrollbarRef = useRef<NiceScrollbarRef>(null);

  const onScroll = (event: ScrollEvent) => {
    scrollbarRef.current?.adjustScrollbar(
      event.detail.scrollTop,
      event.detail.scrollHeight,
    );
  };

  const galleryRef = useRef<NodesRef>(null);

  useEffect(() => {
    galleryRef.current
      ?.invoke({
        method: "autoScroll",
        params: {
          rate: "60",
          start: true,
        },
      })
      .exec();
  }, []);

  return (
    <view className="gallery-wrapper">
      <NiceScrollbar ref={scrollbarRef} />
      <list
        ref={galleryRef}
        className="list"
        list-type="waterfall"
        column-count={2}
        scroll-orientation="vertical"
        custom-list-name="list-container"
        bindscroll={onScroll}
        scroll-event-throttle={0}
      >
        {pictureData.map((picture: Picture, index: number) => (
          <list-item
            estimated-main-axis-size-px={calculateEstimatedSize(
              picture.width,
              picture.height,
            )}
            item-key={"" + index}
            key={"" + index}
          >
            <LikeImageCard picture={picture} />
          </list-item>
        ))}
      </list>
    </view>
  );
};

export default Gallery;

```



Similar to the `bindtap` event used to add the like functionality, we add the [`scroll`](/api/elements/built-in/list.md#scroll) event to `<list>`, which will be triggered when the `<list>` element scrolls. To make the scrollbar respond faster to scroll events, we need to set [`scroll-event-throttle`](/api/elements/built-in/list.md#scroll-event-throttle) to 0.

```tsx title="Gallery.tsx" {16}
...
const onScroll = (event: ScrollEvent) => {
  scrollbarRef.current?.adjustScrollbar(
    event.detail.scrollTop,
    event.detail.scrollHeight
  );
};
...
<list
  ref={galleryRef}
  className="list"
  list-type="waterfall"
  column-count={2}
  scroll-orientation="vertical"
  custom-list-name="list-container"
  bindscroll={onScroll}
  scroll-event-throttle={0}
>
...
```

The NiceScrollbar component provides an internal method adjustScrollbar, which we call to adjust the scrollbar's position whenever the bindscroll event is triggered.

:::info
We use many React techniques in this component, such as `forwardRef` and `useImperativeHandle` for calling the `adjustScrollbar` method. If you are not familiar with them, you can refer to the React official documentation to better understand them.
:::

```tsx title="NiceScrollbar.tsx" {14-19}
...
const adjustScrollbar = (scrollTop: number, scrollHeight: number) => {
  const listHeight = lynx.__globalProps.screenHeight - 48;
  const scrollbarHeight = listHeight * (listHeight / scrollHeight);
  const scrollbarTop = listHeight * (scrollTop / scrollHeight);
  setScrollbarHeight(scrollbarHeight);
  setScrollbarTop(scrollbarTop);
};
...
```

:::details \_\_globalProps
We use [globalProps](/api/lynx-api/lynx/lynx-global-props.md) in this method, where you can use `screenHeight` and `screenWidth` to get the screen height and width.
:::

:::details list-item's estimated-main-axis-size-px
You may have noticed this attribute [estimated-main-axis-size-px](/api/elements/built-in/list.md#estimated-main-axis-size-px). This attribute can estimate the size of elements on the main axis when they are not yet rendered in `<list>`. This is very useful when we add a scrollbar, as we need to know how long the scrollbar needs to be to cover all elements.

Of course, `<list>` also supports automatic layout. You can remove this attribute and see the effect—your scrollbar will automatically adjust its length as the elements change from preset height to actual height.

```tsx title="src/AddNiceScrollbar/Gallery.tsx" {5}
...
  <list>
    {pictureData.map((picture: Picture, index: number) => (
      <list-item
        estimated-main-axis-size-px={calculateEstimatedSize(
          picture.width,
          picture.height
        )}
        item-key={"" + index}
        key={"" + index}
      >
        <LikeImageCard picture={picture} />
      </list-item>
    ))}
  </list>
...
```

We provide a utility method to estimate the size of the image on the main axis based on the current `<list>` layout information and the image dimensions:

```tsx title="src/utils.tsx"
export const calculateEstimatedSize = (
  pictureWidth: number,
  pictureHeight: number,
) => {
  // Fixed styles of the gallery
  const galleryPadding = 20;
  const galleryMainAxisGap = 10;
  const gallerySpanCount = 2;
  const galleryWidth = lynx.__globalProps.screenWidth;
  // Calculate the width of each ImageCard and return the relative height of the it.
  const itemWidth =
    (galleryWidth - galleryPadding * 2 - galleryMainAxisGap) / gallerySpanCount;
  return (itemWidth / pictureWidth) * pictureHeight;
};
```

:::

At this point, we have a complete page! But you may have noticed that the scrollbar we added still lags a bit during scrolling, not as responsive as it could be. This is because our adjustments are still happening on the background thread, not the main thread that responds to touch scrolling.

:::details What are the background thread and main thread?
The biggest feature of Lynx is its dual-thread architecture. You can find a more detailed introduction in [JavaScript Runtime](/guide/scripting-runtime/index.md#javascript).
:::

## A More Responsive Scrollbar

To optimize the performance of the scrollbar, we need to introduce [Main Thread Script (MTS)](/react/main-thread-script.md) to [handle events on the main thread](/guide/interaction/event-handling.md#main-thread-event-processing), migrating the adjustments we made in the previous step for the scrollbar's height and position from the background thread to the main thread.

To let you see the comparison more clearly, we keep both scrollbars:

**This is an example below:  gallery**

**Entry:** `src/ScrollbarCompare`
**Bundle:** `dist/ScrollbarCompare.lynx.bundle` | Web: `dist/ScrollbarCompare.web.bundle`

```tsx {2,3,9,14,17-23,47,48}
import "../index.scss";
import { useEffect, useMainThreadRef, useRef } from "@lynx-js/react";
import { MainThread, type ScrollEvent } from "@lynx-js/types";
import type { NodesRef } from "@lynx-js/types";
import LikeImageCard from "../Components/LikeImageCard.jsx";
import type { Picture } from "../Pictures/furnitures/furnituresPictures.jsx";
import { calculateEstimatedSize } from "../utils.jsx";
import { NiceScrollbar, type NiceScrollbarRef } from "./NiceScrollbar.jsx";
import { adjustScrollbarMTS, NiceScrollbarMTS } from "./NiceScrollbarMTS.jsx";

export const Gallery = (props: { pictureData: Picture[] }) => {
  const { pictureData } = props;
  const scrollbarRef = useRef<NiceScrollbarRef>(null);
  const scrollbarMTSRef = useMainThreadRef<MainThread.Element>(null);
  const galleryRef = useRef<NodesRef>(null);

  const onScrollMTS = (event: ScrollEvent) => {
    "main thread";
    adjustScrollbarMTS(
      event.detail.scrollTop,
      event.detail.scrollHeight,
      scrollbarMTSRef,
    );
  };

  const onScroll = (event: ScrollEvent) => {
    scrollbarRef.current?.adjustScrollbar(
      event.detail.scrollTop,
      event.detail.scrollHeight,
    );
  };

  useEffect(() => {
    galleryRef.current
      ?.invoke({
        method: "autoScroll",
        params: {
          rate: "60",
          start: true,
        },
      })
      .exec();
  }, []);

  return (
    <view className="gallery-wrapper">
      <NiceScrollbar ref={scrollbarRef} />
      <NiceScrollbarMTS main-thread:ref={scrollbarMTSRef} />
      <list
        ref={galleryRef}
        className="list"
        list-type="waterfall"
        column-count={2}
        scroll-orientation="vertical"
        custom-list-name="list-container"
        bindscroll={onScroll}
        main-thread:bindscroll={onScrollMTS}
        scroll-event-throttle={0}
      >
        {pictureData.map((picture: Picture, index: number) => (
          <list-item
            estimated-main-axis-size-px={calculateEstimatedSize(picture.width, picture.height)}
            item-key={"" + index}
            key={"" + index}
          >
            <LikeImageCard picture={picture} />
          </list-item>
        ))}
      </list>
    </view>
  );
};

export default Gallery;

```



Now you should be able to see that the scrollbar on the left, controlled with main thread scripting, is smoother and more responsive compared to the scrollbar on the right that we implemented earlier. If you encounter issues in other UIs where updates need to happen immediately, try this method.

We also provide another tutorial, guiding you through a deep dive into implementing a highly responsive swiper in [Tutorial:Product Detail](/guide/start/tutorial-product-detail.md).

## Wrapping Up

We remove the redundant scrollbar used for comparison, and our Gallery is now complete! Let's take a look at the final result:

**This is an example below:  gallery**

**Bundle:** `dist/GalleryComplete.lynx.bundle` | Web: `dist/GalleryComplete.web.bundle`

```tsx
import { root } from "@lynx-js/react";
import { furnituresPictures } from "../Pictures/furnitures/furnituresPictures.jsx";
import Gallery from "./Gallery.jsx";

function GalleryComplete() {
  return <Gallery pictureData={furnituresPictures} />;
}

root.render(<GalleryComplete />);

```



Configurations! You have successfully created a product gallery page! 🎉 Throughout this tutorial, you’ve covered the basics of writing interactive UIs on the Lynx platform and some of the differences between using it on the Web.
