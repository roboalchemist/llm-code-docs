# Source: https://uat.rive.app/docs/runtimes/web/web-js.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Web (JS)

> JavaScript/WASM runtime for Rive.

export const Demos = ({examples, runtime, columns = 2, children, childrenIndex = 0}) => {
  const examplesData = {
    cachingARiveFile: {
      title: 'Caching a Rive File',
      description: 'Load the .riv into memory once, use it multiple times.',
      riv: 'https://static.rive.app/rivs/rives_animated_emojis.riv',
      stateMachines: "State Machine 1",
      artboard: "Emoji_package",
      links: {
        web: "https://codesandbox.io/p/sandbox/rive-js-caching-a-rive-file-g675my?file=%2Fsrc%2Findex.ts%3A9%2C1",
        react: "https://codesandbox.io/p/sandbox/rive-react-caching-a-rive-file-53gmdf?file=%2Fsrc%2FApp.tsx"
      },
      source: ["https://rive.app/marketplace/24644-46045-caching-a-rive-file-at-runtime/"]
    },
    dataBindingArtboards: {
      title: 'Data Binding Artboards',
      description: 'Swap an artboard with another artboard from the same .riv or one loaded at runtime.',
      image: '/images/runtimes/rive-data-bind-components.webp',
      links: {
        web: 'https://codesandbox.io/p/sandbox/rive-js-data-binding-artboards-jx3pf9?file=%2Fsrc%2Findex.mjs%3A5%2C19',
        react: 'https://codesandbox.io/p/sandbox/rive-react-data-binding-artboards-kmvzh8?file=%2Fsrc%2FApp.tsx',
        flutter: 'https://github.com/rive-app/rive-flutter/blob/master/example/lib/examples/databinding_artboards.dart',
        reactNative: 'https://github.com/rive-app/rive-nitro-react-native/blob/main/example/src/demos/DataBindingArtboardsExample.tsx',
        android: "https://github.com/rive-app/rive-android/blob/master/app/src/main/java/app/rive/runtime/example/ComposeArtboardBindingActivity.kt"
      },
      source: ["https://rive.app/marketplace/24641-46042-data-binding-artboards/", "https://rive.app/marketplace/24642-47536-data-binding-artboards/"]
    },
    dataBindingImages: {
      title: 'Data Binding Images',
      description: 'Replace images at runtime using data binding images with javascript.',
      image: '/images/runtimes/rive-db-images.webp',
      links: {
        web: 'https://codesandbox.io/p/sandbox/objective-cohen-sqwh9q?file=%2Fsrc%2Findex.ts',
        flutter: 'https://github.com/rive-app/rive-flutter/blob/master/example/lib/examples/databinding_images.dart',
        android: "https://github.com/rive-app/rive-android/blob/master/app/src/main/java/app/rive/runtime/example/ComposeImageBindingActivity.kt"
      },
      source: ["https://rive.app/marketplace/25472-47537-data-binding-images/"]
    },
    dataBindingLists: {
      title: 'Data Binding Lists',
      description: 'Add, remove, edit, and swap items in your data binding list.',
      image: '/images/runtimes/rive-db-lists.webp',
      links: {
        web: 'https://codesandbox.io/p/sandbox/suspicious-hertz-2lg4m8?file=%2Fsrc%2Findex.ts',
        react: 'https://codesandbox.io/p/sandbox/rive-react-data-binding-lists-4msh9z?file=%2Fsrc%2FApp.tsx',
        flutter: 'https://github.com/rive-app/rive-flutter/blob/master/example/lib/examples/databinding_lists.dart',
        android: "https://github.com/rive-app/rive-android/blob/master/app/src/main/java/app/rive/runtime/example/ComposeListActivity.kt"
      },
      source: ["https://rive.app/marketplace/25474-47539-data-binding-lists/"]
    },
    dataBindingQuickStart: {
      title: "Data Binding Quick Start",
      description: "Get started with Data Binding at runtime.",
      image: "/images/runtimes/rewards.gif",
      links: {
        flutter: "https://github.com/rive-app/rive-flutter/blob/master/example/lib/examples/databinding.dart",
        reactNative: "https://github.com/rive-app/rive-react-native/blob/main/example/app/(examples)/DataBinding.tsx",
        unity: "https://github.com/rive-app/rive-unity-examples/blob/main/getting-started/Assets/RewardsController.cs",
        apple: "https://github.com/rive-app/rive-ios/blob/main/Example-iOS/Source/Examples/SwiftUI/RewardsView.swift",
        android: "https://github.com/rive-app/rive-android/blob/master/app/src/main/java/app/rive/runtime/example/ComposeDataBindingActivity.kt"
      },
      source: ["https://rive.app/marketplace/25475-47540-data-binding-demo/"]
    },
    dataBindingSolos: {
      title: "Data Binding Solos",
      description: "Control solos at runtime using strings, numbers, or enums.",
      image: '/images/runtimes/data-binding-solos.gif',
      links: {
        react: "https://codesandbox.io/p/sandbox/rive-react-controlling-solos-at-runtime-ctcnlx?file=%2Fsrc%2FApp.tsx"
      },
      source: ["https://rive.app/marketplace/24643-46044-data-binding-solos/"]
    },
    googleAppAds: {
      title: "Google App Ads",
      description: "How to make an interactive Google App with Rive.",
      image: "/images/runtimes/google-app-ads.png",
      links: {
        mobile: "https://github.com/rive-app/rive-use-cases/tree/main/rive-google-ads"
      }
    },
    layouts: {
      title: "Responsive Layouts",
      description: "Create responsive layouts that adapt to different screen sizes.",
      riv: "https://static.rive.app/rivs/layouts_demo.riv",
      stateMachines: "State Machine 1",
      artboard: "Demo",
      links: {
        web: "https://codesandbox.io/p/devbox/rive-responsive-layout-js-forked-m77nlw",
        react: "https://codesandbox.io/p/devbox/rive-responsive-layouts-react-forked-nmpv39?file=%2Fsrc%2FApp.tsx",
        flutter: "https://github.com/rive-app/rive-flutter/blob/master/example/lib/examples/responsive_layouts.dart",
        reactNative: "https://github.com/rive-app/rive-react-native/blob/main/example/app/(examples)/ResponsiveLayout.tsx",
        android: "https://github.com/rive-app/rive-android/blob/master/app/src/main/java/app/rive/runtime/example/ComposeLayoutActivity.kt"
      },
      source: ["https://rive.app/marketplace/24638-46038-layouts-demo/"]
    },
    fontsHostedCompressed: {
      title: 'Load a Compressed Font for Web',
      description: 'Dynamically load a font asset from a hosted location with compression.',
      image: '/images/runtimes/brotli-compressed-fonts.webp',
      links: {
        react: 'https://codesandbox.io/p/sandbox/prod-sound-6yc5xl?file=%2Fsrc%2FApp.tsx%3A19%2C1'
      },
      source: ["https://rive.app/marketplace/25473-47538-loading-compressed-fonts-web/"]
    },
    quickStart: {
      title: "Quick Start",
      image: '/images/runtimes/quick-start.gif',
      description: 'Load and control your Rive (.riv) file.',
      links: {
        web: 'https://codesandbox.io/p/sandbox/rive-quick-start-js-xmwcm6?file=%2Fsrc%2Findex.ts',
        react: 'https://codesandbox.io/p/sandbox/rive-react-quick-start-4xy76h?file=%2Fsrc%2FApp.tsx%3A77%2C14',
        reactJs: 'https://codesandbox.io/p/devbox/rive-react-vanilla-js-quick-start-kz66t4?file=%2Fsrc%2FApp.tsx%3A53%2C7',
        reactNative: 'https://github.com/rive-app/rive-nitro-react-native/blob/main/example/src/demos/QuickStart.tsx',
        unity: '/game-runtimes/unity/tutorials/health-bar'
      },
      source: ["https://rive.app/marketplace/24637-46037-health-bar-data-binding-quick-start/"]
    },
    quickStartReact: {
      title: "Quick Start",
      image: '/images/runtimes/quick-start.gif',
      description: 'Load and control your Rive (.riv) file.',
      links: {
        react: 'https://codesandbox.io/p/sandbox/rive-react-quick-start-4xy76h?file=%2Fsrc%2FApp.tsx%3A77%2C14',
        reactJs: 'https://codesandbox.io/p/devbox/rive-react-vanilla-js-quick-start-kz66t4?file=%2Fsrc%2FApp.tsx%3A53%2C7'
      },
      source: ["https://rive.app/marketplace/24637-46037-health-bar-data-binding-quick-start/"]
    },
    scriptingDrawingShapes: {
      title: "Drawing with Scripting",
      image: "https://static.rive.app/docs/drawing-demo.png",
      description: "Draw a squirkle, a star, and an animated wave with scripting.",
      links: {
        editor: "https://rive.app/community/files/25751-48087-drawing-shapes-with-scripting"
      }
    },
    scriptingMasonry: {
      title: "Masonry Layout",
      image: "https://static.rive.app/docs/masonry.png",
      description: "Create a masonry layout using a Layout script.",
      links: {
        editor: "https://rive.app/community/files/25826-masonry-layout/"
      }
    },
    scriptingTippingConverter: {
      title: "Custom Converter",
      image: "https://static.rive.app/docs/tipping-scripting-converter.gif",
      description: "Calculate the bill total using the converter's input value added to data binding values.",
      links: {
        editor: "https://uat.rive.app/community/files/610-1126-custom-converter-with-scripting"
      }
    },
    scriptingUnitTesting: {
      title: "Unit Testing",
      image: "https://static.rive.app/docs/scripting-default-thumb.png",
      description: "This hands-on example demonstrates unit testing rgbToHex and hexToRgb color utilities.",
      links: {
        editor: "https://rive.app/community/files/25752-48088-test-script"
      }
    },
    scriptingSnakeGame: {
      title: "Snake - Complete Game",
      image: "https://static.rive.app/docs/snake-game.png",
      description: "Check out this complete game built entirely with Rive using scripting.",
      links: {
        editor: "https://rive.app/community/files/25748-48110-snake-game/"
      }
    },
    scriptingMultiTouch: {
      title: "Tracking Multi-touch",
      image: "https://static.rive.app/docs/scripting-default-thumb.png",
      description: "Keep track of every finger.",
      links: {
        editor: "https://rive.app/community/files/25754-48090-multi-touch-with-scripting"
      }
    },
    scriptingNestedPointers: {
      title: "Nested Pointer Events",
      image: "https://static.rive.app/docs/scripting-default-thumb.png",
      description: "Pass pointer events from the parent component to the instantiated children.",
      links: {
        editor: "https://rive.app/community/files/25750-48086-scripting-nested-pointer-events/"
      }
    },
    scriptingBoilPathEffect: {
      title: "Boiling Path Effect",
      image: "https://static.rive.app/docs/boiling-effect.gif",
      description: "Apply a boiling effect to any path using scripting.",
      links: {
        editor: "https://rive.app/community/files/25767-48113-scripting-path-effect-boil"
      }
    },
    scriptingTextPathEffect: {
      title: "Text Path Effect",
      image: "https://static.rive.app/docs/text-path-effect.gif",
      description: "Control a text path using scripting.",
      links: {
        editor: "https://rive.app/community/files/25823-text-path-effects/"
      }
    },
    scriptingDrawImages: {
      title: "Render an Image with Scripting",
      image: "https://static.rive.app/docs/render-image-with-scripting.jpg",
      description: "Draw an image, give it transforms, and control its mesh all through scripting.",
      links: {
        editor: "https://rive.app/community/files/26406-49444-draw-an-image-with-scripting/"
      }
    },
    scriptingSlotMachine: {
      title: "Slot Machine - Complete Game",
      image: "https://static.rive.app/docs/slot-machine.png",
      description: "Build a complete casino game using scripting.",
      links: {
        editor: "https://rive.app/community/files/25759-slot-machine-game-with-scripting/"
      }
    },
    scriptingPlinko: {
      title: "Plinko - Complete Game",
      image: "https://static.rive.app/docs/scripting-plinko-game.png",
      description: "Build a complete Plinko game using Layout, Node, and Path Effect scripts.",
      links: {
        editor: "https://rive.app/marketplace/25772-blinko-scripted-game/"
      }
    }
  };
  const runtimesInOrder = ['web', 'react', 'reactJs', 'reactNative', 'flutter', 'apple', 'android', 'unity', 'unreal', 'mobile', 'editor'];
  const runtimeTitles = {
    web: 'Web',
    reactJs: 'React (Imperative)',
    react: 'React',
    reactNative: "React Native",
    flutter: 'Flutter',
    apple: 'Apple',
    android: 'Android',
    unity: 'Unity',
    unreal: 'Unreal',
    mobile: 'Mobile',
    editor: 'Try in Rive'
  };
  const riveInstances = useRef([]);
  const initRives = () => {
    const rive = window.rive;
    examples.forEach(example => {
      const {riv, stateMachines = "State Machine 1", artboard} = examplesData[example];
      if (riv) {
        const canvasId = `rive-canvas-${example}`;
        const canvas = document.getElementById(canvasId);
        if (canvas) {
          const r = new rive.Rive({
            src: riv,
            stateMachines,
            canvas,
            artboard,
            autoplay: true,
            Layout: new rive.Layout({
              fit: rive.Fit.Layout
            }),
            onLoad: () => {
              r.resizeDrawingSurfaceToCanvas();
              riveInstances.current.push(r);
            }
          });
        }
      }
    });
  };
  useEffect(() => {
    if (window.rive) {
      initRives();
      return;
    }
    const checkRive = () => {
      if (window.rive) {
        initRives();
        window.removeEventListener("rive-loaded", checkRive);
      }
    };
    const handleResize = () => {
      riveInstances.current.forEach(instance => {
        instance.resizeDrawingSurfaceToCanvas();
      });
    };
    window.addEventListener("rive-loaded", checkRive);
    window.addEventListener("resize", handleResize);
    return () => {
      window.removeEventListener("rive-loaded", checkRive);
      window.removeEventListener("resize", handleResize);
      riveInstances.current.forEach(instance => {
        instance.cleanup();
      });
    };
  }, []);
  const RuntimeLink = ({link, runtime}) => {
    if (!link) return null;
    if (runtime === 'editor') {
      link = `${link}?utm_source=docs&utm_medium=docs_demo_card&utm_campaign=docs_to_marketplace_links`;
    }
    return <a href={link} target="_blank" className="cursor-pointer border border-neutral-600 hover:border-white rounded-[4px] text-14 py-1 px-5 mr-[10px] mb-[10px]">
        {runtimeTitles[runtime]}
      </a>;
  };
  const CardContainer = ({children: content}) => {
    return <div className="flex flex-col card block font-normal group relative my-2 ring-2 ring-transparent rounded-2xl bg-white dark:bg-background-dark border border-gray-950/10 dark:border-white/10 overflow-hidden w-full">
        {content}
      </div>;
  };
  const getSrc = imageSrc => {
    if (location.hostname === "localhost" && imageSrc.startsWith("/images/")) {
      return imageSrc;
    } else if (imageSrc.startsWith('https:')) {
      return imageSrc;
    }
    return `https://rive.app/docs${imageSrc}`;
  };
  return <div className={`
card-group not-prose grid gap-x-4
        grid-cols-1
        ${columns >= 2 && "md:grid-cols-2"}
        ${columns >= 3 && "xl:grid-cols-3 xl:w-[67rem] xl:max-w-[calc(100vw-25rem)]"}
      `}>
      {examples.map((example, index) => {
    const {title, image, links, description, source, riv} = examplesData[example];
    const canvasId = `rive-canvas-${example}`;
    return <>
            {index === childrenIndex && children}
            <CardContainer key={canvasId}>
              <div className="w-full h-0 relative pb-[75%]">
                <div className="absolute inset-0">
                  {image && <img alt={title} className="w-full object-cover object-center" src={getSrc(image)} />}

                  {riv && !image && <canvas id={canvasId} style={{
      width: "100%",
      height: "100%"
    }} />}
                </div>
              </div>
              <div className="flex flex-grow flex-col px-6 py-5 relative" data-component-part="card-content-container">
                <div className="flex flex-col grow">
                  <h2 className="not-prose font-semibold text-base text-gray-800 dark:text-white" data-component-part="card-title">{title}</h2>

                  <div className="flex flex-col grow prose mt-1 font-normal text-sm leading-6 text-gray-600 dark:text-gray-400" data-component-part="card-content">
                    <div className="grow flex flex-col">
                        <p>{description}</p>
                        {source && source.length > 0 && <p className="mt-3">
                              {source.map((item, index) => {
      if (source.length == 1) {
        return <>Open the <a href={item}>Rive file</a>.</>;
      }
      if (index == 0) {
        return <>Open <a href={item}>Rive file 1</a></>;
      }
      return <>, <a href={item}>file {index + 1}</a></>;
    })}
                            </p>}
                    </div>
                    {<div className="mt-6 flex flex-wrap">
                        {runtimesInOrder.map(currentRuntime => {
      if (runtime && currentRuntime !== runtime) return;
      return <RuntimeLink key={currentRuntime} runtime={currentRuntime} link={links[currentRuntime]} />;
    })}
                      </div>}
                  </div>
                </div>
              </div>
            </CardContainer>
          </>;
  })}
    </div>;
};

<Warning>
  Note that certain Rive features may not be supported yet for a particular runtime, or may require using the Rive Renderer.

  For more details, refer to the [feature support](/feature-support/) and [choosing a renderer](/runtimes/choose-a-renderer/) pages.
</Warning>

<Demos examples={['quickStart']} runtime="web" />

## Overview

This guide documents how to get started using the Rive web runtime library. The runtime is open source and available in this [GitHub repository](https://github.com/rive-app/rive-wasm). This library has a high-level JavaScript API (with TypeScript support) and a low-level API to load in Web Assembly (WASM) and control the rendering loop yourself. This runtime allows you to:

* Quickly integrate Rive into all web applications (Webflow, WordPress, etc.)
* Provides a base API to build other web-based Rive runtime wrappers (React, Svelte, etc.)
* Support advanced use cases by controlling the render loop (web-based game engines)

## Getting started

Follow the steps below to integrate Rive into your web app.

<Note>
  The following instructions describe using the `@rive-app/canvas` package. Rive provides web-based packages like WebGL, Canvas, and Lite versions.

  See [Canvas vs WebGL](/runtimes/web/canvas-vs-webgl) for guidance on which package is the correct choice for your use case.
</Note>

<Steps>
  <Step title="Install the dependency">
    <Warning>
      We recommend always using the [latest version](https://www.npmjs.com/package/@rive-app/canvas). The versions listed below and in the examples may differ from the latest.
    </Warning>

    <Tabs>
      <Tab title="Script Tag">
        ```html  theme={null}
        // Add the following script tag to your web page to get the latest version:


        <script src="https://unpkg.com/@rive-app/canvas"></script>

        // You can also pin to a specific version (See [here](https://www.npmjs.com/package/@rive-app/canvas) for the latest):


        <script src="https://unpkg.com/@rive-app/canvas@2.35.0"></script>

        // This will make a global `rive` object available, allowing you to access the Rive API via the `rive` entry point:

        new rive.Rive({});
        ```
      </Tab>

      <Tab title="Package Manager">
        ```bash npm theme={null}
        npm install @rive-app/canvas
        ```

        ```bash pnpm theme={null}
        pnpm add @rive-app/canvas
        ```

        ```bash yarn theme={null}
        yarn add @rive-app/canvas
        ```

        ```bash bun theme={null}
        bun add @rive-app/canvas
        ```

        ```javascript Importing theme={null}
        // Import the entire module under the global identifier `rive`
        import * as rive from "@rive-app/canvas";

        // Alternatively, import only the specific parts you need
        import { Rive } from "@rive-app/canvas";

        ```
      </Tab>
    </Tabs>

    <Note>
      Not using [Rive Text](/editor/text/) and [Rive Audio](/editor/events/audio-events)? Consider using [@rive-app/canvas-lite](/runtimes/web/canvas-vs-webgl#rive-app-canvas-lite) which is a smaller package variant.
    </Note>
  </Step>

  <Step title="Create a Canvas">
    Add a canvas element to your HTML where you want the Rive graphic to be displayed:

    ```json  theme={null}
    <canvas id="canvas" width="500" height="500"></canvas>
    ```
  </Step>

  <Step title="Create a Rive instance">
    To create a new instance of a Rive object, provide the following properties:

    * `src`: A string representing the URL of the hosted `.riv` file (as shown in the example below) or the path to the public asset `.riv` file. For more details, refer to [Rive Parameters](/runtimes/web/rive-parameters) on how to properly use this property.
    * `artboard` - (Optional) A string representing the artboard you want to display. If not supplied the default is selected.
    * `stateMachines` - A string representing the name of the state machine you wish to play.
    * `canvas` - The canvas element where the animation will be rendered.
    * `autoplay` - A boolean indicating whether the animation should play automatically.

    ```javascript  theme={null}
    <script>
        const r = new rive.Rive({
            src: "https://cdn.rive.app/animations/vehicles.riv",
            // OR the path to a discoverable and public Rive asset
            // src: '/public/example.riv',
            canvas: document.getElementById("canvas"),
            autoplay: true,
            // artboard: "Artboard", // Optional. If not supplied the default is selected
            stateMachines: "bumpy",
            onLoad: () => {
              r.resizeDrawingSurfaceToCanvas();
            },
        });
    </script>
    ```

    <Note>
      The `resizeDrawingSurfaceToCanvas` method ensures that the Rive animation is correctly scaled to fit the dimensions of the specified canvas element. By default, the canvas rendering surface might not match the exact size of the `<canvas>` element defined in your HTML, which can lead to blurry or incorrectly scaled graphics, especially on high-DPI or retina displays.

      Calling this method adjusts the internal drawing surface so that the animation is rendered with crisp detail, matching the pixel density of the canvas. This is particularly important when:

      * The size of the canvas changes dynamically (e.g., if it is resized due to responsive layouts).
      * You want to ensure the animation remains sharp, regardless of device or screen resolution.

      <br />

      **Best practices:**

      * **Call after load**: It's recommended to call `resizeDrawingSurfaceToCanvas` inside the `onLoad` callback to ensure that the Rive asset has been fully loaded before adjusting the drawing surface. This prevents any rendering issues.
      * **Handling window resize**: If your canvas size changes during the user's interaction (such as when resizing the browser window), you should also listen for window resize events and call `resizeDrawingSurfaceToCanvas` to re-adjust the rendering surface:

      ```javascript  theme={null}
      window.addEventListener("resize", () => {
          r.resizeDrawingSurfaceToCanvas();
      });
      ```

      This way, the Rive animation will continue to look sharp and correctly scaled as the canvas size changes.
    </Note>
  </Step>
</Steps>

### Complete example

Bringing it all together, here's how to load a Rive graphic in a single HTML file.

```html  theme={null}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Rive Hello World</title>
  </head>
  <body>
    <canvas id="canvas" width="500" height="500"></canvas>

    <script src="https://unpkg.com/@rive-app/canvas"></script>
    <script>
      const r = new rive.Rive({
        src: "https://cdn.rive.app/animations/vehicles.riv",
        canvas: document.getElementById("canvas"),
        autoplay: true,
        // artboard: "Arboard", // Optional. If not supplied the default is selected
        stateMachines: "bumpy",
        onLoad: () => {
          // Ensure the drawing surface matches the canvas size and device pixel ratio
          r.resizeDrawingSurfaceToCanvas();
        },
      });
    </script>
  </body>
</html>
```

### Loading Rive files

[See this example](https://codesandbox.io/p/sandbox/rive-quick-start-js-xmwcm6?file=%2Fsrc%2Findex.ts) for the different ways to load in a .riv file, the options are:

1. **Hosted URL**: Use a string representing the URL where the `.riv` file is hosted. Set this as the `src` attribute when creating a new Rive instance.
2. **Static Assets in the bundle**: Provide a string with the path to a publicly accessible `.riv` file within your web project. Handle `.riv` files just like any other static asset (e.g., images or fonts) in your project.
3. **Fetching a file**: Instead of using the `src` attribute, use the `buffer` attribute to load an `ArrayBuffer` when fetching a file. This is useful when reusing the same `.riv` file across multiple Rive instances, allowing you to load it only once.
4. **Reusing a Loaded File**: Use the `rivFile` parameter to reuse a previously loaded Rive runtime file object, avoiding the need to fetch it again via the `src` URL or reload it from the `buffer`. This can significantly improve performance by eliminating redundant network requests and loading times, especially when creating multiple Rive instances from the same source. Unlike the `src` and `buffer` parameters, which require parsing under the hood to create a runtime file object, the `riveFile` parameter uses an already parsed object, including any loaded assets. See [Caching a Rive File](/runtimes/caching-a-rive-file).

For more details, refer to the [Rive Parameters](/runtimes/web/rive-parameters) section on the `src` property.

## 4. Clean up Rive

When working with a Rive instance, it's important to properly clean it up when it's no longer needed. This is especially necessary in scenarios where:

* The UI containing Rive animations is no longer needed (e.g., when a modal with Rive graphics is closed).
* The animation or state machine has completed and will not be shown or run again.

Under the hood, Rive creates various low-level objects (such as artboard instances, animation instances, and state machine instances) in C++, which need to be manually deleted to prevent memory leaks. If not cleaned up, these objects can consume unnecessary resources, potentially impacting your application's performance.

Fortunately, the high-level JavaScript API simplifies this process. You don't need to track every object created during the Rive instance lifecycle. Instead, you can clean up all associated objects with a single method call.

To clean up a Rive instance and free up resources, simply call the following method on your Rive instance:

```javascript  theme={null}
const riveInstance = new Rive({...));
...
// When ready to cleanup
riveInstance.cleanup();
```

# Rive runtime concepts

Learn how to interact with your Rive graphics during runtime.

<CardGroup cols={2}>
  <Card
    title="Artboards"
    href="/runtimes/artboards"
    icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      height="100%"
      fill="none"
      viewBox="0 0 16 16"
      class="size-4 text-gray-500/80 dark:text-gray-400"
      aria-hidden="true"
    >
      <path
        fill="currentColor"
        fill-rule="evenodd"
        d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38"
        clip-rule="evenodd"
      ></path>
    </svg>
  }
  >
    Control which artboard is displayed at runtime.
  </Card>

  <Card
    title="Layout"
    href="/runtimes/layout"
    icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      height="100%"
      fill="none"
      viewBox="0 0 16 16"
      class="size-4 text-gray-500/80 dark:text-gray-400"
      aria-hidden="true"
    >
      <path
        fill="currentColor"
        fill-rule="evenodd"
        d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38"
        clip-rule="evenodd"
      ></path>
    </svg>
  }
  >
    Control the artboard's layout (fit and alignment) at runtime.
  </Card>

  <Card
    title="State Machine Playback"
    href="/runtimes/state-machines"
    icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      height="100%"
      fill="none"
      viewBox="0 0 16 16"
      class="size-4 text-gray-500/80 dark:text-gray-400"
      aria-hidden="true"
    >
      <path
        fill="currentColor"
        fill-rule="evenodd"
        d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38"
        clip-rule="evenodd"
      ></path>
    </svg>
  }
  >
    Control state machine playback at runtime and interact with state machine
    inputs.
  </Card>

  <Card
    title="Data Binding"
    href="/runtimes/data-binding"
    icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      height="100%"
      fill="none"
      viewBox="0 0 16 16"
      class="size-4 text-gray-500/80 dark:text-gray-400"
      aria-hidden="true"
    >
      <path
        fill="currentColor"
        fill-rule="evenodd"
        d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38"
        clip-rule="evenodd"
      ></path>
    </svg>
  }
  >
    Dynamically update content at runtime using two-way data binding for text,
    colors, images, lists, and more.
  </Card>

  <Card
    title="Loading Assets"
    href="/runtimes/loading-assets"
    icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      height="100%"
      fill="none"
      viewBox="0 0 16 16"
      class="size-4 text-gray-500/80 dark:text-gray-400"
      aria-hidden="true"
    >
      <path
        fill="currentColor"
        fill-rule="evenodd"
        d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38"
        clip-rule="evenodd"
      ></path>
    </svg>
  }
  >
    Load referenced assets (images, fonts, audio) at runtime. Also known as
    out-of-band assets.
  </Card>

  <Card
    title="Caching a Rive File"
    href="/runtimes/caching-a-rive-file"
    icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      height="100%"
      fill="none"
      viewBox="0 0 16 16"
      class="size-4 text-gray-500/80 dark:text-gray-400"
      aria-hidden="true"
    >
      <path
        fill="currentColor"
        fill-rule="evenodd"
        d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38"
        clip-rule="evenodd"
      ></path>
    </svg>
  }
  >
    Cache and reuse a Rive file object across multiple Rive instances to improve
    performance.
  </Card>
</CardGroup>

# Additional Rive web resources

More in-depth Rive web documentation and advanced use cases.

<CardGroup cols={2}>
  <Card title="Rive Parameters" icon={<svg xmlns="http://www.w3.org/2000/svg" height="100%" fill="none" viewBox="0 0 16 16" class="size-4 text-gray-500/80 dark:text-gray-400" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38" clip-rule="evenodd"></path></svg>} href="/runtimes/web/rive-parameters">
    API docs for the Rive instance.
  </Card>

  <Card title="Canvas vs WebGL" icon={<svg xmlns="http://www.w3.org/2000/svg" height="100%" fill="none" viewBox="0 0 16 16" class="size-4 text-gray-500/80 dark:text-gray-400" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38" clip-rule="evenodd"></path></svg>} href="/runtimes/web/canvas-vs-webgl">
    A guide to the different Rive web packages
  </Card>

  <Card title="FAQ" icon={<svg xmlns="http://www.w3.org/2000/svg" height="100%" fill="none" viewBox="0 0 16 16" class="size-4 text-gray-500/80 dark:text-gray-400" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38" clip-rule="evenodd"></path></svg>} href="/runtimes/web/faq">
    Frequently asked questions
  </Card>

  <Card title="Preloading WASM" icon={<svg xmlns="http://www.w3.org/2000/svg" height="100%" fill="none" viewBox="0 0 16 16" class="size-4 text-gray-500/80 dark:text-gray-400" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38" clip-rule="evenodd"></path></svg>} href="/runtimes/web/preloading-wasm">
    Instructions on how to preload and self-host the rive WASM library.
  </Card>

  <Card title="Low-level API Usage" icon={<svg xmlns="http://www.w3.org/2000/svg" height="100%" fill="none" viewBox="0 0 16 16" class="size-4 text-gray-500/80 dark:text-gray-400" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="M8.036 1v4.178c0 1.034.839 1.873 1.873 1.873h4.003v6.178a1.77 1.77 0 0 1-1.77 1.77H3.858a1.77 1.77 0 0 1-1.771-1.77V2.771A1.77 1.77 0 0 1 3.857 1zm1.25.145v4.033c0 .345.279.624.623.624h3.889a1.8 1.8 0 0 0-.377-.597L11.618 3.32 9.842 1.525a1.8 1.8 0 0 0-.557-.38" clip-rule="evenodd"></path></svg>} href="/runtimes/web/low-level-api-usage">
    Control the Rive render loop and layout, and draw multiple artboards to the same canvas.
  </Card>
</CardGroup>

# Examples

* [Basic gallery app](https://github.com/rive-app/rive-wasm/tree/master/js/examples/_frameworks/parcel_example_canvas)
* [Tracking mouse cursor](https://codesandbox.io/p/sandbox/tracking-mouse-cursor-n38gdd?file=%2Fsrc%2Findex.ts)
* [Connecting to page scroll](https://codesandbox.io/p/sandbox/rive-page-scroll-h4msqw?file=%2Fsrc%2Findex.ts%3A27%2C45)
* [Playing state machine only when scrolled into the user's viewport](https://codesandbox.io/p/sandbox/rive-wait-for-scroll-into-view-y9wg8d?file=%2Fsrc%2Findex.ts)
