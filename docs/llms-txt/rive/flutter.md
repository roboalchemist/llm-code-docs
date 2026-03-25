# Source: https://uat.rive.app/docs/runtimes/flutter/flutter.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flutter

> Flutter runtime for Rive.

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

## Overview

This guide documents how to use the Rive Flutter runtime to easily integrate Rive graphics in your Flutter apps.

<Note>
  The latest version of Rive Flutter is currently published as a dev release
  `0.14.0-dev.x`. This means that while the package is stable and ready for
  production use, we are still actively developing new features and
  improvements. We recommend using the latest dev version to take advantage of
  the newest features and fixes.
</Note>

<Info>
  Already using Rive Flutter? See our [Migration
  Guide](/runtimes/flutter/migration-guide) for information on adopting the
  latest `0.14.x` version.
</Info>

## Quick start

See our [example app](https://github.com/rive-app/rive-flutter/tree/master/example).

<Demos examples={["dataBindingQuickStart"]} runtime="flutter" />

## Getting started

Follow the steps below to integrate Rive into your Flutter apps.

<Steps>
  <Step title="Add the Rive package dependency">
    Check out Rive's [pub.dev](https://pub.dev/packages/rive) page to get the latest version.

    ```yaml  theme={null}
    # pubspec.yaml
    dependencies:
      rive: ^0.14.0-dev.6 # or latest dev version
    ```
  </Step>

  <Step title="Import the Rive package">
    Import the Rive runtime library in the file you're looking to integrate Rive animations into.

    ```dart  theme={null}
    import 'package:rive/rive.dart';
    ```

    Consider doing a named import to avoid conflicts with other libraries:

    ```dart  theme={null}
    import 'package:rive/rive.dart' as rive;
    ```
  </Step>

  <Step title="Initialize Rive">
    <Info>
      You're encouraged to call `await RiveNative.init()` at the start of your app, or before you use Rive. For example, in `main.dart`. This will automatically be called the first time you load a Rive file, but if you want to ensure Rive is loaded before showing your first graphic, call it manually.
    </Info>

    ```dart  theme={null}
    import 'package:rive/rive.dart';

    Future<void> main() async {
      WidgetsFlutterBinding.ensureInitialized();
      // Call init before using Rive.
      await RiveNative.init();
      runApp(const MyApp());
    }
    ```
  </Step>

  <Step title="Add a Rive widget">
    There are several ways to render Rive graphics in Flutter. We recommend using the `RiveWidget`, and optionally the `RiveWidgetBuilder`, or `RivePanel`.

    * `RiveWidget` is responsible for rendering the graphic and exposing common view configuration.
    * `RiveWidgetBuilder` handles file loading, error states, and resource management automatically.
    * `RivePanel` is a higher-level inherited widget that creates a shared texture to paint multiple `RiveWidget`s to. Only usable when using the Rive Renderer (`Factory.rive`). This can drastically improve performance when showing many Rive graphics at once by reducing the number of textures and avoiding WebGL context limitations on the web.

    <Tabs>
      <Tab title="Using RiveWidgetBuilder">
        ```dart  theme={null}
        class ExampleRiveBuilder extends StatefulWidget {
          const ExampleRiveBuilder({super.key});

          @override
          State<ExampleRiveBuilder> createState() => _ExampleRiveBuilderState();
        }

        class _ExampleRiveBuilderState extends State<ExampleRiveBuilder> {
          late final fileLoader = FileLoader.fromAsset("assets/vehicles.riv", riveFactory: Factory.rive);

          @override
          void dispose() {
            fileLoader.dispose();
            super.dispose();
          }

          @override
          Widget build(BuildContext context) {
            return RiveWidgetBuilder(
              fileLoader: fileLoader,
              builder: (context, state) => switch (state) {
                RiveLoading() => const Center(child: CircularProgressIndicator()),
                RiveFailed() => ErrorWidget.withDetails(
                    message: state.error.toString(),
                    error: FlutterError(state.error.toString()),
                  ),
                RiveLoaded() => RiveWidget(
                    controller: state.controller,
                    fit: Fit.cover,
                  )
              },
            );
          }
        }
        ```
      </Tab>

      <Tab title="Using RiveWidget directly">
        ```dart  theme={null}
        class ExampleBasic extends StatefulWidget {
          const ExampleBasic({super.key});

          @override
          State<ExampleBasic> createState() => _ExampleBasicState();
        }

        class _ExampleBasicState extends State<ExampleBasic> {
          late File file;
          late RiveWidgetController controller;
          bool isInitialized = false;

          @override
          void initState() {
            super.initState();
            initRive();
          }

          void initRive() async {
            file = (await File.asset("assets/vehicles.riv", riveFactory: Factory.rive))!;
            controller = RiveWidgetController(file);
            setState(() => isInitialized = true);
          }

          @override
          void dispose() {
            file.dispose();
            controller.dispose();
            super.dispose();
          }

          @override
          Widget build(BuildContext context) {
            if (!isInitialized) {
              return const Center(child: CircularProgressIndicator());
            }
            return RiveWidget(
              controller: controller,
              fit: Fit.cover,
            );
          }
        }
        ```
      </Tab>

      <Tab title="Using RivePanel">
        Steps:

        1. Wrap the `RiveWidget`s that should draw to the same texture with a single inherited `RivePanel`.
        2. Set `useSharedTexture: true` in each `RiveWidget` that should draw to the shared texture.
        3. (Optional) Set `drawOrder` in each `RiveWidget` to control the order they are drawn in. Lower numbers are drawn first.

        ```dart  theme={null}
         class ExampleRivePanel extends StatelessWidget {
           const ExampleRivePanel({super.key});

           @override
           Widget build(BuildContext context) {
             return const RivePanel(
               backgroundColor: Colors.red,
               child: ListViewExample(),
             );
           }
        }
        class ListViewExample extends StatefulWidget {
          const ListViewExample({super.key});

          @override
          State<ListViewExample> createState() => _ListViewExampleState();
        }

        class _ListViewExampleState extends State<ListViewExample> {
          late final fileLoader = FileLoader.fromAsset(
            'assets/rating.riv',
            riveFactory: Factory.rive,
          );

          @override
          void dispose() {
            fileLoader.dispose();
            super.dispose();
          }

          @override
          Widget build(BuildContext context) {
            return ListView.builder(
              itemCount: 10,
              itemBuilder: (context, index) {
                return MyRiveWidget(fileLoader: fileLoader);
              },
            );
          }
        }
        class MyRiveWidget extends StatelessWidget {
          const MyRiveWidget({super.key, required this.fileLoader});
          final FileLoader fileLoader;

          @override
          Widget build(BuildContext context) {
            return RiveWidgetBuilder(
              fileLoader: fileLoader,
              builder: (context, state) => switch (state) {
                RiveLoading() => const Center(
                    child: Center(child: CircularProgressIndicator()),
                  ),
                RiveFailed() => ErrorWidget.withDetails(
                    message: state.error.toString(),
                    error: FlutterError(state.error.toString()),
                  ),
                RiveLoaded() => RiveWidget(
                    controller: state.controller,
                    fit: Fit.contain,
                    // Set this to true to draw to the nearest RivePanel
                    useSharedTexture: true,
                  )
              },
            );
          }
        }
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Loading from different sources">
    **From Asset Bundle:**

    Make sure you add the Rive files to your asset bundle and reference them in `pubspec.yaml`:

    ```yaml  theme={null}
    # pubspec.yaml
    assets:
        - assets/vehicles.riv
    ```

    ```dart  theme={null}
    // Using FileLoader (with RiveWidgetBuilder)
    final fileLoader = FileLoader.fromAsset("assets/vehicles.riv", riveFactory: Factory.rive);

    // Using File directly
    final file = await File.asset("assets/vehicles.riv", riveFactory: Factory.rive);
    ```

    **From URL:**

    ```dart  theme={null}
    // Using FileLoader (with RiveWidgetBuilder)
    final fileLoader = FileLoader.fromUrl("https://cdn.rive.app/animations/vehicles.riv", riveFactory: Factory.rive);

    // Using File directly
    final file = await File.url("https://cdn.rive.app/animations/vehicles.riv", riveFactory: Factory.rive);
    ```

    **From Rive File:**

    ```dart  theme={null}
    // Using FileLoader (with RiveWidgetBuilder)
    final fileLoader = FileLoader.fromFile(existingFile, riveFactory: Factory.rive);
    ```
  </Step>
</Steps>

## Key components

### `RiveWidget`

`RiveWidget` is responsible for displaying Rive graphics.

**Properties:**

* `controller` \[**required**]: The `RiveWidgetController` that manages the Rive graphic
* `fit`: How the artboard should fit within the widget (default: `contain`)
* `alignment`: How the artboard should be aligned within the widget (default: `center`)
* `hitTestBehavior`: How pointer events should be handled (default: `opaque`)
* `cursor`: The cursor to display when hovering over the widget (default: `defer`)
* `layoutScaleFactor`: Scale factor when using `Fit.layout` (default: `1.0`)
* `useSharedTexture`: Whether to use a shared texture ([RivePanel](#rivepanel)) to draw the artboard to. Defaults to false. When set to true, it draws to nearest inherited widget of type [RivePanel](#rivepanel).
* `drawOrder`: The draw order of the artboard. This is only used when `useSharedTexture` is true when drawing to a [RivePanel](#rivepanel), and using `Factory.rive`. Defaults to 1.

### `RiveWidgetBuilder`

`RiveWidgetBuilder` is a higher-level widget that handles file loading, error states, and resource management automatically.

**Properties:**

* `fileLoader` \[**required**]: The `FileLoader` for loading the Rive file
* `builder` \[**required**]: Function that builds the widget based on state
* `artboardSelector`: Which artboard to use (default: `ArtboardDefault()`)
* `stateMachineSelector`: Which state machine to use (default: `StateMachineDefault()`)
* `dataBind`: How to bind view model data (optional)
* `controller`: Optional custom controller builder
* `onLoaded`: Callback when Rive state is loaded
* `onFailed`: Callback when Rive state fails to load

### `RivePanel`

`RivePanel` is a widget that creates a shared texture to paint multiple `RiveWidget` s to. This is useful when using `Factory.rive` and can significantly improve performance under certain conditions.

**When to use RivePanel:**

* When displaying multiple `RiveWidget`s in your app and they can be drawn to the same texture
* When you want to programatically composit a scene that includes multiple Rive graphics (from multiple Rive files/artboards)
* When using `Factory.rive` (will report errors with `Factory.flutter`) and want to improve performance
* When you want to reduce the number of textures being drawn to
* When targeting web platforms to avoid WebGL context limitations through `Factory.rive`

**Performance considerations:**

* **Benefits**: Drawing multiple `RiveWidget`s to the same texture can drastically improve performance by reducing texture allocation overhead
* **Memory cost**: There is a memory cost in allocating a larger texture, though this may be offset by the reduced number of individual textures
* **Rendering limitations**: Drawing to the same surface means you cannot interleave Rive drawing commands with Flutter's drawing commands
* **Benchmarking recommended**: Performance characteristics vary by use case - what works for one scenario may not work for another

**Usage:**

```dart  theme={null}
RivePanel(
  backgroundColor: Colors.red, // Optional background color
  child: YourWidgetWithMultipleRiveWidgets(),
)
```

**Important notes:**

* Only works with `Factory.rive` - has no effect with `Factory.flutter`
* Set `useSharedTexture: true` in your `RiveWidget`s to enable shared texture rendering
* If you need to interleave Rive content with Flutter content, consider using separate `RivePanel`s or `Factory.flutter`
* For complex scenarios, benchmark both approaches to determine the best performance strategy

### `RiveWidgetController`

`RiveWidgetController` manages the graphic.

**Creating a Controller:**

```dart  theme={null}
// Using default artboard and state machine
final controller = RiveWidgetController(file);

// Specifying artboard and state machine
final controller = RiveWidgetController(
  file,
  artboardSelector: ArtboardSelector.byName("MyArtboard"),
  stateMachineSelector: StateMachineSelector.byName("MyStateMachine"),
);
```

**Data Binding:**

```dart  theme={null}
// Auto-bind with default view model instance
final viewModelInstance = controller.dataBind(DataBind.auto());

// Bind by specific instance
final viewModelInstance = controller.dataBind(DataBind.byInstance(myInstance));

// Bind by name
final viewModelInstance = controller.dataBind(DataBind.byName("MyViewModel"));
```

### File loading

The `FileLoader` class provides a unified way to load Rive files from different sources.

**Loading from Assets:**

```dart  theme={null}
final fileLoader = FileLoader.fromAsset(
  "assets/vehicles.riv",
  riveFactory: Factory.rive,
);
```

**Loading from URL:**

```dart  theme={null}
final fileLoader = FileLoader.fromUrl(
  "https://example.com/animation.riv",
  riveFactory: Factory.rive,
);
```

**Loading from Existing File:**

```dart  theme={null}
final fileLoader = FileLoader.fromFile(
  existingFile,
  riveFactory: Factory.rive,
);
```

Or you can load files directly using the `File` class:

```dart  theme={null}
// Load from asset
final file = await File.asset("assets/vehicles.riv", riveFactory: Factory.rive);
// Load from URL
final file = await File.url("https://example.com/animation.riv", riveFactory:
Factory.rive);
// Load from path
final file = await File.path("/path/to/animation.riv", riveFactory: Factory.rive);
// Load from bytes
final file = await File.decode(bytes, riveFactory: Factory.rive);
```

## Error handling

The Rive Flutter package provides specific exception types for different error scenarios:

* `RiveFileLoaderException`: Thrown when file loading fails
* `RiveArtboardException`: Thrown when artboard selection fails
* `RiveStateMachineException`: Thrown when state machine selection fails
* `RiveDataBindException`: Thrown when data binding fails

## Resource management

### Manual resource management (`RiveWidget`)

When using `RiveWidget` directly, you are responsible for managing all resources:

```dart  theme={null}
@override
void dispose() {
  // Dispose resources in reverse order of creation
  viewModelInstance.dispose();
  controller.dispose();
  file.dispose();
  super.dispose();
}
```

### Automatic resource management (`RiveWidgetBuilder`)

When using `RiveWidgetBuilder`, the widget automatically manages most resources. You only need to dispose the file loader:

```dart  theme={null}
@override
void dispose() {
  fileLoader.dispose();
  super.dispose();
}
```

<Note>
  Because the resources are managed by the `RiveWidgetBuilder`, you will not be able to access the `RiveWidgetController` (and other state) after the widget is disposed. If you need to access the controller after the widget is disposed, consider creating the file and controller yourself.

  The exception to this is the `FileLoader`, which you control. This loader can be reused across multiple `RiveWidgetBuilder` instances. The underlying `File` will only be loaded once. The `File` will be disposed when the `FileLoader` is disposed.
</Note>

## Specifying a renderer

When creating a Rive `File` or `FileLoader`, you need to specify a factory to use:

* `Factory.rive` for the Rive renderer
* `Factory.flutter` for the Flutter renderer (Skia or Impeller)

You can use different renderers for different graphics in your app.

Some considerations when choosing a renderer:

* If you plan on showing many Rive graphics that are all drawing to different Rive widgets consider using a [RivePanel](#rivepanel) with `Factory.rive` to draw multiple graphics to the same texture to reduce the overhead of allocating native render targets and textures. Or make use of `Factory.flutter`.
* If you are showing a complex graphic, consider using `Factory.rive` to take advantage of the Rive renderer's optimizations.
* Vector Feathering is only available with `Factory.rive`, so if you need that feature, use the Rive renderer.

For more information see [Choosing a Renderer](/runtimes/choose-a-renderer/).

<Warning>
  The Rive Renderer is not yet supported on Linux through Flutter. On Linux, it
  automatically falls back to `Factory.flutter`.
</Warning>

### Note on Flutter Rendering

[Impeller](https://docs.flutter.dev/perf/impeller) is replacing [Skia](https://skia.org/) to become the default renderer for all platforms. As such, there is a possibility of rendering and [performance](https://github.com/flutter/flutter/issues/134432) discrepancies when using the Rive Flutter runtime with platforms that use the Impeller renderer that may not have surfaced before. If you encounter any visual or performance errors at runtime compared to expected behavior in the Rive editor, we recommend trying the following steps to triage:

1. Try running the Flutter app with the `--no-enable-impeller` flag to use the Skia renderer. If the visual discrepancy does not show when using Skia, it may be a rendering bug on Impeller. However, before raising a bug with the Flutter team, try the second point below👇

```bash  theme={null}
flutter run --no-enable-impeller
```

1. Try running the Flutter app on the latest `master` channel. It is possible that visual bugs may be resolved on the latest Flutter commits, but not yet released in the `beta` or `stable` channel.
2. If you are still seeing visual discrepancies with just the Impeller renderer on the latest master branch, we recommend raising a detailed issue to the [Flutter](https://github.com/flutter/flutter) Github repo with a reproducible example, and other relevant details that can help the team debug any possible issues that may be present.

## Troubleshooting

If you encounter issues with Rive in Flutter, consider the following:

* Ensure you have called `await RiveNative.init()` before using any Rive features.
* Check the console for any error messages related to Rive.
* Make sure your Rive files are correctly referenced in `pubspec.yaml` and exist in the specified paths.
* If using `RiveWidgetBuilder`, ensure you handle all possible states (loading, loaded, failed) in the builder function.

### Build errors

If you encounter build errors related to Rive, ensure that:

* You have the correct version of the Rive package in your `pubspec.yaml`.
* You have run `flutter pub get` to fetch the latest dependencies.
* You have reviewed the [Flutter FAQ](/runtimes/flutter/faq) for common issues and questions.

If you're still having issues, please see the [Troubleshooting section](/runtimes/flutter/rive-native#troubleshooting) in the Rive Native documentation.

## Manually building Rive native libraries

Rive automatically downloads the native libraries for you as part of the `rive_native` plugin.

However, if you need to manually build the native libraries, see the [build section](/runtimes/flutter/rive-native#building-rive-native) in the Rive Native documentation.

## Next steps

Now that you have Rive integrated into your Flutter app, you can explore more advanced features like:

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

## Resources

Rive Flutter:

* [GitHub](https://github.com/rive-app/rive-flutter)
* [pub.dev](https://pub.dev/packages/rive)
* [Example app](https://github.com/rive-app/rive-flutter/tree/master/example/)

Rive Native:

* [Rive Native overview](/runtimes/flutter/rive-native)
* [pub.dev](https://pub.dev/packages/rive_native)
