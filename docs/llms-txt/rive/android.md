# Source: https://uat.rive.app/docs/runtimes/android/android.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Android

> The Android runtime for Rive.

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

<Demos examples={['dataBindingQuickStart']} runtime="android" />

# Overview

Welcome to using Rive on Android. Rive runtime libraries are open-source, with Android available in the [rive-android](https://github.com/rive-app/rive-android) GitHub repository.

## The Two Android APIs

Rive for Android provides two main APIs for integrating Rive into your application.

**The New Compose API (Beta)**

This API is designed for Jetpack Compose, allowing for a more modern and declarative approach to building UIs. It is currently in beta and undergoing additional testing, and some issues may be uncovered during development. We will work to address these quickly as they come up. It is feature complete, production ready, and recommended for any new projects using Compose, while existing projects should migrate when feasible.

The entry point for this API is the `Rive` composable function, which can be used directly within your Compose UI code.

In addition to providing a more idiomatic Compose experience, this API is also powered by a stronger threading model with higher stability and flexibility to spread Rive work across multiple threads.

In the future this threading model will also include a View-based API for projects that cannot use Compose.

**The Legacy View-based API**

This API is based on Android Views and XML layouts. It has been widely deployed in production applications. It also supports [Compose by using AndroidView](https://github.com/rive-app/rive-android/blob/master/app/src/main/java/app/rive/runtime/example/LegacyComposeActivity.kt), though it does require some boilerplate to set up.

The entry point for this API is the `RiveAnimationView`, which can be added to your XML layouts or instantiated programmatically.

We refer to this as the "legacy" API as we are focusing our development efforts on the new Compose API going forward, though this API will continue to be supported and maintained for some time. For all new development projects, we recommend using the new Compose API. Additionally, we recommend migrating existing projects to the new API when feasible, as this version will be deprecated in the future and will have limited to no new feature development.

# Sample App

To explore the Android API, you can run our Android sample app. Each activity demonstrates a particular feature of the Rive Android runtime.

```bash  theme={null}
git clone https://github.com/rive-app/rive-android
```

Open the cloned folder in Android Studio and select the `app` configuration and target device. Ensure that the build variant is set to `preview (default)` by opening the menu `Build - Select Build Variant...` and selecting the `preview (default)` variant for `app`.

The other build variants are for development purposes and require additional configuration. See [CONTRIBUTING.MD](https://github.com/rive-app/rive-android/blob/master/CONTRIBUTING.md).

# Getting Started

If you are looking for getting started instructions for the Legacy API, see [Getting Started (Legacy API)](./legacy-getting-started).

## Adding Rive to Your Project

<Steps>
  <Step title="Add the Rive dependency">
    Add the following dependencies to your `build.gradle` file in your project. We recommend using the latest version of the Rive Android runtime, which can be found on [Maven Central](https://central.sonatype.com/artifact/app.rive/rive-android).

    ```groovy  theme={null}
    dependencies {
        ...
        implementation 'app.rive:rive-android:<Latest Version>'
        // For initialization, you may want to add a dependency on Jetpack Startup
        implementation "androidx.startup:startup-runtime:1.1.1"
    }
    ```
  </Step>

  <Step title="Initializing Rive">
    Rive needs to link and initialize its C++ runtime for its Kotlin bindings to work.

    This can be done via an [initializer](https://developer.android.com/topic/libraries/app-startup) which does this automatically at app startup time. The initialization provider can be set up directly in your app's manifest file.

    ```xml  theme={null}
    <manifest ...>
      <application ...>
        <provider
          android:name="androidx.startup.InitializationProvider"
          android:authorities="${applicationId}.androidx-startup"
          android:exported="false"
          tools:node="merge">
            <meta-data android:name="app.rive.runtime.kotlin.RiveInitializer"
              android:value="androidx.startup" />
        </provider>
      </application>
    </manifest>
    ```

    Otherwise this can be achieved by calling the initializer in your code.

    ```kotlin  theme={null}
    AppInitializer.getInstance(applicationContext)
      .initializeComponent(RiveInitializer::class.java)
    ```

    If you want to initialize Rive yourself, this can be done in code using the following. This is the most flexible option, as you can lazily load the native library, but be sure to call it before any Rive functionality is used.

    ```kotlin  theme={null}
    Rive.init(context)
    ```
  </Step>

  <Step title="Add Rive to your layout">
    You can now add `Rive` composables to your Compose layouts. See the following sections for details. If you are using the legacy API, see [Getting Started (Legacy API)](./legacy-getting-started.mdx) instead.
  </Step>
</Steps>

## Enabling Logging

The Compose API uses extensive logging, especially at the debug level, to help diagnose issues. By default there is no logger enabled. Most commonly you will want to set the global logger to pipe to Android's Logcat, which has a convenience function as follows. This could be done in your activity's `onCreate` method or in your `Application` subclass, for instance, before any Rive functionality is used.

```kotlin  theme={null}
RiveLog.logger = RiveLog.LogcatLogger()
```

## Adding Rive to Your Composition

<Steps>
  <Step title="Creating a Worker">
    The Compose API uses an explicit Rive worker which owns a thread for Rive operations, including file and asset decoding, advancing, and drawing. Before you can use any of the API surface, you must create a worker to host these operations. Be aware that the worker must live for the duration of all Rive resources made from it.

    The simplest API within a Compose context is `rememberRiveWorker`, which will create and remember a worker for the lifetime of the composition. However, if you want to handle any unexpected errors during worker creation, you can use `rememberRiveWorkerOrNull`, which will return `null` if the worker could not be created and forward the error to an error state you provide.

    ```kotlin  theme={null}
    setContent {
        // Simple
        val riveWorker = rememberRiveWorker()

        // Safe
        val errorState = remember { mutableStateOf<Throwable?>(null) }
        val riveWorker = rememberRiveWorkerOrNull(errorState)
        if (riveWorker == null) {
            // Handle the error and early return
            return@setContent
        }
    }
    ```
  </Step>

  <Step title="Loading a Rive File">
    Before you can display a Rive element, you must load a Rive file, i.e. an exported .riv file. Rive files are specified by a `RiveFileSource`, which can be either a `RawRes` (for local raw resources) or a `Bytes` (for raw byte data, from any source including the network). In this case, we'll use a raw resource for simplicity. That source, along with the above worker, are passed to `rememberRiveFile`, which internally will load and cache the file for use in the composition.

    ```kotlin  theme={null}
    setContent {
      ... // riveWorker from above

      val riveFile = rememberRiveFile(
          RiveFileSource.RawRes.from(R.raw.my_rive_file),
          riveWorker
      )
    }
    ```

    The returned value is a `Result<RiveFile>`, which can be either `Loading`, `Success`, or `Error`. This pattern requires you to handle the loading and error states appropriately in your UI. Typically this is done with a `when` statement.

    ```kotlin  theme={null}
    when (riveFile) {
        is Result.Loading -> LoadingIndicator()
        is Result.Error -> /* Handle error */
        is Result.Success -> {
            // The `RiveFile` is held in the `value` property
            val file = riveFile.value
            // Use the file - see next step
        }
    }
    ```
  </Step>

  <Step title="Using the Rive Composable">
    With the loaded `RiveFile` you can now display it using the `Rive` composable. The worker is captured in the Rive file, so those two components are all that are needed. Without specifying further, this will choose the default artboard and state machine, as specified in the Rive editor. Further options are explored in the other documentation sections, such as [Artboards](../artboards), [State Machines](../state-machines), and [Data Binding](../data-binding).

    ```kotlin  theme={null}
    when (riveFile) {
        ...
        is Result.Success -> {
            Rive(riveFile.value)
        }
    }
    ```
  </Step>
</Steps>

# Resources

[GitHub](https://github.com/rive-app/rive-android)

[Examples](https://github.com/rive-app/rive-android/tree/master/app/src/main/java/app/rive/runtime/example)
