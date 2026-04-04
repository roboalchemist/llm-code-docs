# Source: https://uat.rive.app/docs/runtimes/caching-a-rive-file.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Caching a Rive File

export const Apple = {
  currentRuntimeName: "New Runtime (Experimental)",
  legacyRuntimeName: "Legacy Runtime"
};

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

Under most circumstances a `.riv` file should load quickly and managing the `RiveFile` yourself is not necessary. But if you intend to use the same `.riv` file in multiple parts of your application, or even on the same screen, it might be advantageous to load the file once and keep it in memory.

## Example Usage

<Demos examples={["cachingARiveFile"]} />

<Tabs>
  <Tab title="Flutter">
    In Flutter, you are responsible for managing the lifecycle of a Rive file. You can create a `File` object directly, or use the `FileLoader` convenience class with `RiveWidgetBuilder`. In both cases, you must call `dispose()` on the object when it's no longer needed to free up memory.

    ```dart  theme={null}
    import 'package:flutter/material.dart';
    import 'package:rive/rive.dart';

    class CachedPage extends StatefulWidget {
        const CachedPage({super.key});

        @override
        State<CachedPage> createState() => _CachedPageState();
    }

    class _CachedPageState extends State<CachedPage> {
        var _isRivLoaded = false;

        // This is where our cached file will go.
        late File _riveFile;

        @override
        void initState() {
            super.initState();

            // Once initialized, build the layout by updating _isRivLoaded.
            _initRive().whenComplete(
                () => setState(() {
                    _isRivLoaded = true;
                }),
            );
        }

        Future<void> _initRive() async {
            // Retrieve the Rive file from assets.
            _riveFile = (await File.asset(
                "assets/rewards_demo.riv",
                riveFactory: Factory.rive,
            ))!;
        }

        @override
        void dispose() {
            _riveFile.dispose();
            super.dispose();
        }

        @override
        Widget build(BuildContext context) {
            if (_isRivLoaded) {
                // Both widgets can use the same Rive file because we cached it as state.
                final widget1 = RiveWidget(controller: RiveWidgetController(_riveFile));
                final widget2 = RiveWidget(controller: RiveWidgetController(_riveFile));

                return Scaffold(
                    body: Row(
                        children: [
                            Expanded(child: widget1),
                            Expanded(child: widget2),
                        ],
                    ),
                );
            } else {
                return CircularProgressIndicator();
            }
        }
    }
    ```

    <Tip>
      To optimize memory usage, reuse the same `File` object across multiple `RiveWidget` instances if they use the same `.riv` file. This ensures the file is loaded only once and shared in memory.
    </Tip>

    <Warning>
      After a `File` is disposed, it cannot be used again. To use the same `.riv` file, create a new `File` object.
    </Warning>

    #### Managing State

    How you keep the Rive `File` alive and share it with widgets depends on your state management approach. For global access, load the file in `main` or during app startup, and expose it using a package like [Provider](https://pub.dev/packages/provider). If the file is only needed in a specific part of your app, consider loading the file only when required.

    #### Memory

    Managing the file yourself gives you fine-grained control over memory usage, especially when the same Rive file is used in multiple places or simultaneously in several widgets. Use [Flutter DevTools memory tooling](https://docs.flutter.dev/tools/devtools/memory#memory-view-guide) to monitor and optimize memory if needed.

    #### Network Assets

    To load a Rive file from the Internet, use `File.url('YOUR:URL')`. For network assets, cache the file in memory to avoid repeated downloads and unnecessary decoding of the file.
  </Tab>

  <Tab title="React">
    Here’s a simplified example showing how to integrate the `useRiveFile` hook to reuse a `RiveFile` across components

    ```javascript  theme={null}
    import React, { useState } from 'react';
    import { useRiveFile } from '@rive-app/react-canvas';

    // Custom Wrapper component to display the Rive animation
    const RiveAnimation = ({ riveFile }) => {
        const { RiveComponent } = useRive({
            riveFile: riveFile,
            autoplay: true
        });

        return <RiveComponent/>;
    };

    function App() {
    const { riveFile, status } = useRiveFile({
        src: 'https://cdn.rive.app/animations/myrivefile.riv',
    });

    const [instanceCount] = useState(5); // Number of RiveAnimation components to render

    if (status === 'idle') {
        return <div>Idle...</div>;
    }

    if (status === 'loading') {
        return <div>Loading...</div>;
    }

    if (status === 'failed') {
        return <div>Failed to load Rive file.</div>;
    }

    // Each RiveAnimation component uses the RiveFile we loaded earlier, so it is only fetched and initialized once
    return (
        <div className="App">
            <header className="App-header">Rive Instances</header>
            <div className="rive-list">
            {Array.from({ length: instanceCount }, (_, index) => (
                <RiveAnimation key={`rive-instance-${index}`} riveFile={riveFile} />
            ))}
            </div>
        </div>
        );

    }

    export default App;
    ```
  </Tab>

  <Tab title="React Native">
    <Tabs>
      <Tab title="New Runtime (Recommended)">
        In the new React Native runtime, you always need to load and manage the lifetime of a `RiveFile` object that is passed to `RiveView`. The `useRiveFile` hook handles loading, and you can reuse the same `RiveFile` across multiple `RiveView` components to cache it in memory.

        Here's an example showing how to cache a Rive file and reuse it across multiple components:

        ```tsx Reuse RiveFile example expandable theme={null}
        import { useState } from 'react';
        import { View, ActivityIndicator, Text } from 'react-native';
        import {
          RiveView,
          useRiveFile,
          Fit,
          type RiveFile,
        } from '@rive-app/react-native';

        // Custom component to display a Rive animation
        const RiveExample = ({ riveFile }: { riveFile: RiveFile }) => {
          return (
            <RiveView
              file={riveFile}
              fit={Fit.Contain}
              autoPlay={true}
              style={{ width: 200, height: 200 }}
            />
          );
        };

        export default function CacheExample() {
          // Load the Rive file once using useRiveFile
          const { riveFile, isLoading, error } = useRiveFile(
            require('../../assets/rive/rating.riv')
          );

          const [instanceCount] = useState(5); // Number of RiveExample components to render

          if (isLoading) {
            return <ActivityIndicator size="large" />;
          }

          if (error || !riveFile) {
            return <Text>Failed to load Rive file: {error || 'Unknown error'}</Text>;
          }

          // Each RiveExample component uses the same RiveFile we loaded earlier,
          // so it is only fetched and initialized once
          return (
            <View style={{ flex: 1, flexDirection: 'row', flexWrap: 'wrap' }}>
              {Array.from({ length: instanceCount }, (_, index) => (
                <RiveExample key={`rive-instance-${index}`} riveFile={riveFile} />
              ))}
            </View>
          );
        }
        ```

        <Tip>
          To optimize memory usage, reuse the same `RiveFile` object across multiple `RiveView` instances if they use the same `.riv` file. This ensures the file is loaded only once and shared in memory.
        </Tip>

        #### Managing State

        How you keep the `RiveFile` alive and share it with components depends on your state management approach:

        * **Global access**: Load the file at the app level or in a context provider, and expose it using React Context or a state management library like Redux or Zustand.
        * **Component-level**: If the file is only needed in a specific part of your app, load it in a parent component and pass it down as props.
        * **Custom hook**: Create a custom hook that manages the `RiveFile` lifecycle and provides it to consuming components.

        #### Memory Management

        The `useRiveFile` hook automatically manages the lifecycle of the `RiveFile` object. When the component unmounts or the input changes, the hook will dispose of the previous file and load a new one if needed. This gives you automatic memory management without manual cleanup.

        #### Network Assets

        To load a Rive file from a remote URL, pass the URL string to `useRiveFile`:

        ```tsx  theme={null}
        const { riveFile, isLoading, error } = useRiveFile(
            'https://cdn.rive.app/animations/vehicles.riv'
        );
        ```

        For network assets, caching the file in memory avoids repeated downloads and unnecessary decoding. The `useRiveFile` hook handles this automatically as long as you reuse the same `riveFile` object.

        See [Loading Rive Files](/runtimes/react-native/loading-rive-files) for more information on different loading methods.
      </Tab>

      <Tab title="Legacy Runtime">
        Not supported
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Web">
    The following is a basic example to illustrate how to preload a Rive file, and pass the data to multiple Rive instances.

    ```javascript  theme={null}
    const rive = require("@rive-app/canvas");

    let riveInstances = [];

    function loadRiveFile(src, onSuccess, onError) {
    const file = new rive.RiveFile({
        src: src,
        onLoad: () => onSuccess(file),
        onLoadError: onError,
    });
    // Remember to call init() to trigger the load;
    file.init().catch(onError);
    }

    function setupRiveInstance(loadedRiveFile, canvasId) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;

    const riveInstance = new rive.Rive({
        riveFile: loadedRiveFile,
        // Be sure to specify the correct state machine (or animation) name
        stateMachines: "Motion", // Name of the State Machine to play
        canvas: canvas,
        layout: new rive.Layout({
        fit: rive.Fit.FitWidth,
        alignment: rive.Alignment.Center,
        }),
        autoplay: true,
        onLoad: () => {
        // Prevent a blurry canvas by using the device pixel ratio
        riveInstance.resizeDrawingSurfaceToCanvas();
        },
    });

    riveInstances.push(riveInstance);
    }

    // Loads the .riv file and initializes multiple Rive instances using the same loaded RiveFile in memory
    loadRiveFile(
    "clean_the_car.riv",
    (file) => {
        setupRiveInstance(file, "rive-canvas-1");
        setupRiveInstance(file, "rive-canvas-2");
        // You could also store a reference to the loaded RiveFile here so you're able to initialize other Rive instances later.
    },
    (error) => {
        console.error("Failed to load Rive file:", error);
    }
    );

    // Resize the drawing surface for all instances if the window resizes
    window.addEventListener(
    "resize",
    () => {
        riveInstances.forEach((instance) => {
        if (instance) {
            instance.resizeDrawingSurfaceToCanvas();
        }
        });
    },
    false
    );
    ```
  </Tab>

  <Tab title="Apple">
    <Tabs>
      <Tab title={Apple.currentRuntimeName}>
        To cache a Rive file, you can create a strong reference to a `File` object. This `File` can then be reused to create `Rive` objects.

        Artboards and state machines are unique when created using the `create` functions. This means that you can create a new `Rive` object with the same file, but with different (and unique) artboards and state machines.

        ```swift  theme={null}
        // An example builder class that creates a new Rive object with a cached file, creating new and unique artboards and state machines for each Rive object.
        class RiveBuilder {
            private let file: File
            
            init(file: File) {
                self.file = file
            }
            
            @MainActor
            func createRive(artboard: String? = nil, stateMachine: String? = nil) async throws -> Rive {
                let artboardInstance = try await file.createArtboard(artboard ?? .default)
                let stateMachineInstance = try await artboardInstance.createStateMachine(stateMachine ?? .default)
                return try await Rive(file: file, artboard: artboardInstance, stateMachine: stateMachineInstance)
            }
        }

        // Load and cache the file once
        let file = try await File(source: ..., worker: Worker())

        // Create a builder with the cached file
        let builder = RiveBuilder(file: file)

        // Create multiple Rive objects with different configurations
        // Each Rive object is unique, but they all share the same cached File
        let rive1 = try await builder.createRive() // Creates a unique artboard and state machine
        let rive2 = try await builder.createRive() // Creates a unique artboard and state machine, behaving separately from the first Rive object
        let rive4 = try await builder.createRive(artboard: "MainArtboard", stateMachine: "Walking") // Creates a unique artboard and state machine, behaving separately from the first three Rive objects
        let rive5 = try await builder.createRive(artboard: "MainArtboard", stateMachine: "Idle") // Creates a unique artboard and state machine, behaving separately from the first four Rive objects
        ```
      </Tab>

      <Tab title={Apple.legacyRuntimeName}>
        ```swift  theme={null}
        // Cache a RiveFile somewhere to cache for reuse
        let file = try! RiveFile(resource: "file", loadCdn: false)

        // For example purposes, a type that reuses a single RiveFile
        // when creating new view models for given state machines or artboards.
        class ViewModelGenerator {
            /// The RiveFile to reuse when generating new view models.
            private let file: RiveFile

            init(file: RiveFile) {
                self.file = file
            }

            // Returns a new view model using a cached RiveFile.
            // This means that the RiveFile will not have to be reparsed
            // each time a view model is generated.
            func viewModel(stateMachine: String?, artboard: String?) -> RiveViewModel {
                // While one RiveFile can be cached and reused, each view model
                // should have its own model as to not share state.
                let model = RiveModel(riveFile: file)
                return RiveViewModel(model, stateMachineName: stateMachine, artboardName: artboard)
            }
        }
        ```

        When using the `RiveViewModel(fileName:)` initializer, the Apple runtime does not cache file usage; that has to be handled manually. You may find that when reusing the same file, your memory usage increases (over time) as you create more view models. This is when you should consider caching the underlying file for reuse.

        Reusing a single `RiveFile` (when applicable) will reduce the overall memory usage of your application. If your `.riv` can be reused across multiple views, where each view requires the same file but uses different artboards or state machines, consider caching the `RiveFile` before creating your view models. While one `RiveFile` can be cached, to ensure that each view is in its own state, you must create a unique `RiveModel` per `RiveViewModel` instance.
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Android">
    To cache a rive file in Android, you can use the Rive `File` class to load and cache the file. That `RiveFile` can then be reused across multiple `RiveAnimationView` instances. Here's a basic example:

    ```kotlin  theme={null}
    import app.rive.runtime.kotlin.RiveAnimationView
    import app.rive.runtime.kotlin.RiveInitializer
    import app.rive.runtime.kotlin.core.File

    class MainActivity : ComponentActivity() {
        var riveFile: File? = null

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            enableEdgeToEdge()

            // Initialize Rive.
            AppInitializer.getInstance(applicationContext)
                .initializeComponent(RiveInitializer::class.java)

            // Load Rive file from assets and cache.
            application.assets.open("rewards_demo.riv").use { inputStream ->
                val fileBytes = inputStream.readBytes()
                riveFile = File(fileBytes)
            }

            setContent {
                Row {
                    // First cached file usage.
                    AndroidView(
                        modifier = Modifier.weight(1f),
                        factory = { context ->
                            RiveAnimationView(context).also {
                                it.setRiveFile(
                                    file = riveFile!!,
                                    stateMachineName = "State Machine 1",
                                    autoBind = true,
                                )
                            }
                        }
                    )

                    // Second cached file usage.
                    AndroidView(
                        modifier = Modifier.weight(1f),
                        factory = { context ->
                            RiveAnimationView(context).also {
                                it.setRiveFile(
                                    file = riveFile!!,
                                    stateMachineName = "State Machine 1",
                                    autoBind = true,
                                )
                            }
                        }
                    )
                }
            }
        }

        override fun onDestroy() {
            riveFile?.release()
            super.onDestroy()
        }
    }
    ```

    Please bear in mind that this is only one way to load the bytes, and your implementation may vary based on your app's architecture. The key point is to create a Rive `File` from the byte array and then set it on the `RiveAnimationView`.

    <Warning>
      A Rive `File` is reference counted and when created has a reference count of 1. Assigning it to a `RiveAnimationView` will keep an additional reference, but there is still the original reference from its creation. You are responsible for releasing that reference when you are done with the file by calling `File::release`. If you do not release the file, the native memory will remain until the app is closed, even if the Kotlin object is garbage collected.
    </Warning>
  </Tab>
</Tabs>
