# Source: https://uat.rive.app/docs/runtimes/react-native/react-native.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# React Native

> React Native runtime for Rive.

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

<Note>
  🚀 **The new Rive React Native runtime is now available!** Built with Nitro for improved performance and better React Native integration.

  **Get started:**

* [Migration guide](/runtimes/react-native/migration-guide)
* [GitHub](https://github.com/rive-app/rive-nitro-react-native)
* [NPM](https://www.npmjs.com/package/@rive-app/react-native)

  **Migration Timeline:**

* **Short term:** Complete the new runtime, see [Feature Support](https://github.com/rive-app/rive-nitro-react-native?tab=readme-ov-file#feature-support) and [Roadmap](https://github.com/rive-app/rive-nitro-react-native?tab=readme-ov-file#roadmap)
* **Medium term:** Address major concerns in the legacy package while supporting migration
* **Long term:** Full migration to the new package

  We're actively gathering feedback to improve the new runtime. Please share your thoughts and report any issues you encounter.
</Note>

## Overview

This guide documents how to get started using the Rive React Native runtime. The source for the new runtime is available in its [GitHub repository](https://github.com/rive-app/rive-nitro-react-native).

<Tabs>
  <Tab title="New Runtime (Recommended)">
    ## Requirements

    * **React Native**: 0.78 or later (0.79+ recommended for improved Android error messages)
    * **Expo SDK**: 53 or later (for Expo users)
    * **iOS**: 15.1 or later
    * **Android**: SDK 24 (Android 7.0) or later
    * **Xcode**: 16.4 or later
    * **JDK**: 17 or later
    * **Nitro Modules**: 0.25.2 or later

    ## Quick Start

    Follow these quick start steps to get familiar with the Rive React Native runtime.

    <CardGroup cols={2}>
      <Card title="Rive File" href="https://rive.app/marketplace/24637-46037-health-bar-data-binding-quick-start/">
        Remix/download the Rive file used in this quick start guide
      </Card>

      <Card title="Complete example" href="https://github.com/rive-app/rive-nitro-react-native/blob/main/example/src/demos/QuickStart.tsx">
        View the complete quick start example
      </Card>
    </CardGroup>

    <Steps>
      <Step title="Install the dependency">
        ```bash  theme={null}
        npm install @rive-app/react-native react-native-nitro-modules
        # or for Yarn
        yarn add @rive-app/react-native react-native-nitro-modules
        ```

        <Note>
          `react-native-nitro-modules` is required as this library relies on [Nitro Modules](https://nitro.margelo.com/).
        </Note>
      </Step>

      <Step title="Setup">
        Import the necessary components and define styles for the following steps.

        ```ts Imports theme={null}
        import {
          RiveView,
          useRive,
          useRiveFile,
          useRiveNumber,
          useRiveTrigger,
          useViewModelInstance,
          Fit,
        } from '@rive-app/react-native';
        ```

        ```ts Styles theme={null}
        const styles = StyleSheet.create({
          container: {
            flex: 1,
            alignItems: 'center',
            justifyContent: 'center',
          },
          rive: {
            width: '100%',
            height: 400,
          },
        });
        ```
      </Step>

      <Step title="Rive File and Component">
        The `RiveView` component displays Rive graphics. It requires a single prop: `file`, a `RiveFile` object.

        Use the `useRiveFile` hook to load a **riv** file and create a `RiveFile` object. This object can be cached and reused across multiple components.

        ```ts Loading a file theme={null}
        export default function QuickStart() {
          const { riveFile } = useRiveFile(
            require('path/to/quick_start.riv')
          );

          return (
            <View style={styles.container}>
              {riveFile && <RiveView file={riveFile} style={styles.rive} />}
            </View>
          );
        }
        ```

        Further reading:

        <CardGroup cols={3}>
          <Card title="Props" href="/runtimes/react-native/props">
            Available view props for `RiveView`
          </Card>

          <Card title="Loading Rive Files" href="/runtimes/react-native/loading-rive-files">
            How to load Rive files in your app
          </Card>

          <Card title="Caching Rive Files" href="/runtimes/caching-a-rive-file">
            Cache Rive files for better performance
          </Card>
        </CardGroup>
      </Step>

      <Step title="Layout">
        Configure how the graphic fits within its container.

        For this example, we'll set `fit` to `Layout`, which automatically resizes the artboard to match the view size. This is ideal for responsive Rive graphics built with [Layouts](/editor/layouts/layouts-overview).

        ```ts Layout focus={1, 4, 5} theme={null}
        <RiveView
          file={riveFile}
          style={styles.rive}
          fit={Fit.Layout}
        />
        ```

        Further reading:

        <CardGroup cols={1}>
          <Card title="Runtime layout" href="/runtimes/layout">
            Control how Rive graphics fit and align within their containers
          </Card>
        </CardGroup>
      </Step>

      <Step title="View Reference">
        Use the `useRive()` hook to access the Rive view reference for programmatic control.

        ```ts useRive hook focus={5, 11} theme={null}
        export default function QuickStart() {
          const { riveFile } = useRiveFile(
            require('path/to/quick_start.riv')
          );
          const { riveViewRef, setHybridRef } = useRive();

          return (
            <View style={styles.container}>
              {riveFile && (
                <RiveView
                  hybridRef={setHybridRef}
                  file={riveFile}
                  fit={Fit.Layout}
                  style={styles.rive}
                />
              )}
            </View>
          );
        }
        ```

        Further reading:

        <CardGroup cols={2}>
          <Card title="View methods" href="/runtimes/react-native/rive-ref-methods">
            See all the available view reference methods.
          </Card>

          <Card title="Hybrid Views" href="https://nitro.margelo.com/docs/hybrid-views">
            Read more on Nitro Hybrid Views.
          </Card>
        </CardGroup>
      </Step>

      <Step title="Data binding">
        Create the view model instance manually using the `useViewModelInstance` hook and pass it to the view.

        This approach lets you set initial property values in the `onInit` callback before the view loads and decouples the `ViewModelInstance` from the `RiveView`.

        ```ts Manually create view model instance focus={6-8, 12, 18} theme={null}
        export default function QuickStart() {
          const { riveFile } = useRiveFile(
            require('path/to/quick_start.riv')
          );
          const { riveViewRef, setHybridRef } = useRive();
          const viewModelInstance = useViewModelInstance(riveFile, {
            onInit: (vmi) => (vmi.numberProperty('health')!.value = 20),
          });

          return (
            <View style={styles.container}>
              {riveFile && viewModelInstance && (
                <RiveView
                  hybridRef={setHybridRef}
                  file={riveFile}
                  fit={Fit.Layout}
                  style={styles.rive}
                  dataBind={viewModelInstance}
                />
              )}
            </View>
          );
        }
        ```

        Use the view model property hooks to update and listen to property changes.

        ```ts Property hooks focus={10-37, 50-52} expandable theme={null}
        export default function QuickStart() {
          const { riveFile } = useRiveFile(
            require('path/to/quick_start.riv')
          );
          const { riveViewRef, setHybridRef } = useRive();
          const viewModelInstance = useViewModelInstance(riveFile, {
            onInit: (vmi) => (vmi.numberProperty('health')!.value = 20),
          });

          const { value: health, setValue: setHealth } = useRiveNumber(
            'health',
            viewModelInstance
          );

          console.log('health', health);

          const { trigger: gameOverTrigger } = useRiveTrigger(
            'gameOver',
            viewModelInstance,
            { onTrigger: () => console.log('Game Over Triggered') }
          );

          const handleTakeDamage = () => {
            setHealth((h) => (h ?? 0) - 7);
            riveViewRef!.playIfNeeded();
          };

          const handleMaxHealth = () => {
            setHealth(100);
            riveViewRef!.playIfNeeded();
          };

          const handleGameOver = () => {
            setHealth(0);
            gameOverTrigger();
            riveViewRef!.playIfNeeded();
          };

          return (
            <View style={styles.container}>
              {riveFile && viewModelInstance && (
                <RiveView
                  hybridRef={setHybridRef}
                  file={riveFile}
                  fit={Fit.Layout}
                  style={styles.rive}
                  dataBind={viewModelInstance}
                />
              )}
              <Button onPress={handleTakeDamage} title="Take Damage" />
              <Button onPress={handleMaxHealth} title="Max Health" />
              <Button onPress={handleGameOver} title="Game Over" />
            </View>
          );
        }
        ```

        <Warning>
          We call `playIfNeeded` to force the state machine to play. Under some circumstances, the state machine might be settled if there is no active timeline in the graphic.

          This is a temporary workaround. In the future, this will happen automatically.
        </Warning>

        Further reading:

        <CardGroup cols={1}>
          <Card title="Data binding" href="/runtimes/data-binding">
            See the runtime data binding documentation for more information.
          </Card>
        </CardGroup>
      </Step>
    </Steps>

    <Note>
      See our [example app](https://github.com/rive-app/rive-nitro-react-native/tree/main/example) for more usage examples.
    </Note>

    ## Key Components

    ### `RiveView`

    The component to render Rive content:

    ```ts  theme={null}
    <RiveView
      file={riveFile}
    />
    ```

    See the available [props](/runtimes/react-native/props) and [methods](/runtimes/react-native/rive-ref-methods).

    ### `useRiveFile`

    Hook for loading Rive files from a URL or local source:

    ```javascript  theme={null}
    const { riveFile } = useRiveFile(
      'https://cdn.rive.app/animations/vehicles.riv'
    );
    // or
    // const { riveFile } = useRiveFile(require('./assets/graphic.riv'));
    ```

    See [loading Rive files](/runtimes/react-native/loading-rive-files) and [caching Rive files](/runtimes/caching-a-rive-file) for more information.

    ### `useRive`

    Hook to access the Rive view reference for programmatic control:

    ```javascript  theme={null}
    const { riveViewRef, setHybridRef } = useRive();

    <RiveView
      hybridRef={setHybridRef}
      file={riveFile}
    />
    ```

    This is a [Nitro Hybrid View](https://nitro.margelo.com/docs/hybrid-views). See the avaiable [view reference methods](/runtimes/react-native/rive-ref-methods).

    ### `useViewModelInstance`

    Hook to create a view model instance from a `RiveFile`, `ViewModel`, or `RiveViewRef`:

    ```ts  theme={null}
    // From RiveFile — default artboard's ViewModel, default instance
    const instance = useViewModelInstance(riveFile);

    // From RiveFile — specify artboard or ViewModel name (mutually exclusive)
    const instance = useViewModelInstance(riveFile, { artboardName: 'MainArtboard' });
    const instance = useViewModelInstance(riveFile, { viewModelName: 'Settings' });

    // instanceName can be combined with any of the above to pick a specific instance
    const instance = useViewModelInstance(riveFile, { instanceName: 'PersonInstance' });
    const instance = useViewModelInstance(riveFile, { viewModelName: 'Settings', instanceName: 'UserSettings' });

    // From a ViewModel object
    const namedInstance = useViewModelInstance(viewModel, { name: 'My Instance' });
    const newInstance = useViewModelInstance(viewModel, { useNew: true });

    // With required: true (throws if null, use with Error Boundary)
    const instance = useViewModelInstance(riveFile, { required: true });

    // With onInit to set initial values synchronously
    const instance = useViewModelInstance(riveFile, {
      onInit: (vmi) => {
        vmi.numberProperty('health')!.value = 100;
      },
    });
    ```

    Pass the `dataBind` prop in `RiveView`.

    ```ts  theme={null}
    return (
      <RiveView
        file={riveFile}
        dataBind={instance}
      />
    );
    ```

    You can also get the auto-bound instance from a `RiveViewRef`:

    ```javascript  theme={null}
    import { useRive, useViewModelInstance } from '@rive-app/react-native';

    const { riveViewRef, setHybridRef } = useRive();
    const instance = useViewModelInstance(riveViewRef);
    ```

    See the [runtime data binding documentation](/runtimes/data-binding) for more information.

    ## Resources

    <CardGroup cols={3}>
      <Card title="GitHub" href="https://github.com/rive-app/rive-nitro-react-native" />

      <Card title="NPM" href="https://www.npmjs.com/package/@rive-app/react-native" />

      <Card title="Example App" href="https://github.com/rive-app/rive-nitro-react-native/tree/main/example" />
    </CardGroup>
  </Tab>

  <Tab title="Legacy Runtime">
    <Warning>
      The legacy runtime is still supported, but we recommend migrating to the new runtime for better performance and features.
    </Warning>

    This guide documents how to get started using the legacy React Native runtime library. The source is available in its [GitHub repository](https://github.com/rive-app/rive-react-native). This library contains an API for React Native apps to easily integrate Rive assets.

    The minimum iOS target is **14.0**

    <Note>
      See [our documentation](/runtimes/react-native/adding-rive-to-expo) to add
      Rive to an Expo app.
    </Note>

    ## Getting Started

    Follow the steps below for a quick start on integrating Rive into your React Native app.

    <Steps>
      <Step title="Install the dependency">
        ```bash  theme={null}
        npm install rive-react-native
        # or for Yarn
        yarn add rive-react-native
        ```
      </Step>

      <Step title="iOS - Pod Install">
        `cd` inside the `ios` folder and run `pod install` (if deploying to iOS)

        <Note>
          If you run into issues here, you may need to bump the `ios` deployment version target to at least `14.0`. You can find this version in the `Podfile` of the `ios/` folder.
        </Note>
      </Step>

      <Step title="Android - Set Kotlin Dependency Resolution">
        This step may be optional - however, if your Android setup in the React Native project does not have Kotlin `v1.8.0+` set up, you may run into duplicate class issues when building the project. To mitigate these issues, as suggested by [Kotlin docs](https://kotlinlang.org/docs/gradle-configure-project.html#versions-alignment-of-transitive-dependencies), add the following to your dependencies in your application's `build.gradle` file to deal with version alignment:

        ```javascript  theme={null}
        dependencies {
            implementation platform('org.jetbrains.kotlin:kotlin-bom:1.8.0')
            ...
        }
        ```
      </Step>

      <Step title="Add the Rive component">
        ```javascript  theme={null}
        import Rive from 'rive-react-native';

        function App() {
          return <Rive
              url="https://public.rive.app/community/runtime-files/2195-4346-avatar-pack-use-case.riv"
              artboardName="Avatar 1"
              stateMachineName="avatar"
              style={{width: 400, height: 400}}
          />;
        }
        ```
      </Step>
    </Steps>

    ## Resources

    <CardGroup cols={2}>
      <Card title="GitHub" href="https://github.com/rive-app/rive-react-native" />

      <Card title="Example App" href="https://github.com/rive-app/rive-react-native/tree/main/example" />
    </CardGroup>
  </Tab>
</Tabs>
