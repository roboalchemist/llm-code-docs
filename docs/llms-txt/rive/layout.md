# Source: https://uat.rive.app/docs/scripting/api-reference/interfaces/layout.md

# Source: https://uat.rive.app/docs/runtimes/layout.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Layout

> Control how graphics are laid out within the canvas, view, widget, or texture.

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

<Demos examples={["layouts"]} />

## The Fit Mode

A Rive graphic authored in the editor will not necessarily match the size of the container (canvas, view, widget, or texture) it is rendered into at runtime. We need to determine the behavior for this scenario, as no one size fits all.

The solution is choosing the fit mode. This is specified on the container and controls how Rive is scaled.

* `Layout`: Use the Rive layout engine to apply responsive layout to the artboard, matching the container dimensions. For this to work, the artboard must be designed with layouts in mind. See [Responsive Layouts](#responsive-layouts) for more information on how to use this option.
* `Contain`: **(Default)** Preserve aspect ratio and scale the artboard so that its larger dimension matches the corresponding dimension of the container.

  If aspect ratios are not identical, this will leave space on the shorter dimension's axis.
* `ScaleDown`: Preserve aspect ratio and behave like `Contain` when the artboard is larger than the container. Otherwise, use the artboard's original dimensions.
* `Cover`: Preserve aspect ratio and scale the artboard so that its smaller dimension matches the corresponding dimension of the container.

  If aspect ratios are not identical, this will clip the artboard on the larger dimension's axis.
* `FitWidth`: Preserve aspect ratio and scale the artboard width to match the container's width.

  If the aspect ratios between the artboard and container do not match, this will result in either vertical clipping or space in the vertical axis.
* `FitHeight`: Preserve aspect ratio and scale the artboard height to match the container's height.

  If the aspect ratios between the artboard and container do not match, this will result in either horizontal clipping or space in the horizontal axis.
* `Fill`: Do not preserve aspect ratio and stretch to the container's dimensions.
* `None`: Do not scale. Use the artboard's original dimensions.

  For either dimension, if the artboard's dimension is larger, it will be clipped. If it is smaller, it will leave space.

### Alignment

In all options other than `Layout` and `Fill`, there is the possibility that the Rive graphic is clipped or leaves space within its container. Alignment determines how to align content aligns with within the container. The following options are available.

* `TopLeft`
* `TopCenter`
* `TopRight`
* `CenterLeft`
* `Center` **(Default)**
* `CenterRight`
* `BottomLeft`
* `BottomCenter`
* `BottomRight`

### Bounds

Some runtimes expose the option to set the bounding dimensions for the area in which the Rive content will render by providing the minimum and maximum x and y coordinates. These coordinates are relative to the container and all must be provided. These will override alignment settings.

* `minX`
* `minY`
* `maxX`
* `maxY`

### Applying the Fit Mode

<Tabs>
  <Tab title="Web">
    Use the `Layout` object to configure `Fit` and `Alignment`. See [Fit](#the-fit-mode) and [Alignment](#alignment) for all enum options.

    ```javascript  theme={null}
    <div>
        <canvas id="canvas" width="800" height="600"></canvas>
    </div>
    <script src="https://unpkg.com/@rive-app/canvas@latest"></script>
    <script>
        // Fill the canvas, cropping Rive if necessary
        let layout = new rive.Layout({
            fit: rive.Fit.Cover,
        });

        // Fit to the width and align to the top of the canvas
        layout = new rive.Layout({
            fit: rive.Fit.FitWidth,
            alignment: rive.Alignment.TopCenter,
        });

        // Constrain the Rive content to (minX, minY), (maxX, maxY) in the canvas
        layout = new rive.Layout({
            fit: rive.Fit.Contain,
            minX: 50,
            minY: 50,
            maxX: 100,
            maxY: 100,
        });

        const r = new rive.Rive({
            src: 'https://cdn.rive.app/animations/vehicles.riv',
            canvas: document.getElementById('canvas'),
            layout: layout,
            autoplay: true
        });

        // Update the layout
        r.layout = new rive.Layout({ fit: rive.Fit.Fill });
    </script>
    ```
  </Tab>

  <Tab title="React">
    Use the `Layout` object to configure `Fit` and `Alignment`. See [Fit](#the-fit-mode) and [Alignment](#alignment) for all enum options.

    ```javascript  theme={null}
    import Rive, { Layout, Fit, Alignment } from '@rive-app/react-canvas';

    export const Simple = () => (
      <Rive
        src="https://cdn.rive.app/animations/vehicles.riv"
        layout={new Layout({ fit: Fit.Contain, alignment: Alignment.TopCenter })}
      />
    );
    ```

    With the `useRive` hook:

    ```javascript  theme={null}
    import { useRive, Layout, Fit, Alignment } from '@rive-app/react-canvas';

    export default function Example() {
      const { RiveComponent } = useRive({
        src: 'my-file.riv',
        artboard: 'my-artboard',
        animations: 'my-animation',
        layout: new Layout({
          fit: Fit.Cover,
          alignment: Alignment.TopCenter,
        }),
        autoplay: true,
      });

      return <RiveComponent />;
    }
    ```
  </Tab>

  <Tab title="React Native">
    <Tabs>
      <Tab title="New Runtime (Recommended)">
        Set layout attributes for `Fit` and `Alignment` on the `RiveView` component directly. See [Fit](#the-fit-mode) and [Alignment](#alignment) for all enum options.

        ```ts  theme={null}
        import {
          Alignment,
          Fit,
          RiveView,
          useRiveFile,
        } from '@rive-app/react-native';

        export default function LayoutExample() {
          const { riveFile } = useRiveFile(
            require('path/to/file.riv')
          );

          return (
            <View style={styles.container}>
              {riveFile ? (
                <RiveView
                  file={riveFile}
                  style={styles.rive}
                  fit={Fit.Contain}
                  alignment={Alignment.Center}
                />
              ) : null}
            </View>
          );
        }
        ```
      </Tab>

      <Tab title="Legacy Runtime">
        Set layout attributes for `Fit` and `Alignment` on the `Rive` component directly. See [Fit](#the-fit-mode) and [Alignment](#alignment) for all enum options.

        ```javascript  theme={null}
        import Rive, { Alignment, Fit } from 'rive-react-native';

        export default function Simple() {
          return (
            <ScrollView>
              <Rive
                fit={Fit.Cover}
                alignment={Alignment.TopCenter}
                resourceName="truck_v7"
              />
            </ScrollView>
          );
        };
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Flutter">
    Pass the `Fit` and `Alignment` to the `RiveWidget` widget.

    ```dart  theme={null}
    return RiveWidget(
      controller: controller,
      fit: Fit.contain,
      alignment: Alignment.center,
    );
    ```

    Alternatively, you can also the set `fit` and `alignment` properties directly on any `RivePainter`, such as the `RiveWidgetController`:

    ```dart  theme={null}
    final controller = RiveWidgetController(riveFile);
    controller.fit = Fit.contain;
    controller.alignment = Alignment.center;
    ```
  </Tab>

  <Tab title="Apple">
    <Tabs>
      <Tab title={Apple.currentRuntimeName}>
        You can set the fit and layout options on a `Rive` object. The `.fit` can be updated at runtime without creating a new `Rive` object.

        For all possible options, see [Fit.swift](https://github.com/rive-app/rive-ios/blob/main/Source/Experimental/View/Fit.swift)

        ```swift  theme={null}
        // Set a fit and alignment for an artboard that does not use layouts
        let file = try await File(source: ..., worker: Worker())
        var rive = try await Rive(file: file, fit: .contain(alignment: .center))
        // Update the fit and alignment at runtime
        rive.fit = .fitWidth(alignment: .topCenter)
        ```
      </Tab>

      <Tab title={Apple.legacyRuntimeName}>
        The runtime provides the following enums to set on layout parameters:

        * **Fit**
          * `.fill`
          * `.contain`
          * `.cover`
          * `.fitWidth`
          * `.fitHeight`
          * `.scaleDown`
          * `.noFit`

        * **Alignment**
          * `.topLeft`
          * `.topCenter`
          * `.topRight`
          * `.centerLeft`
          * `.center`
          * `.centerRight`
          * `.bottomLeft`
          * `.bottomCenter`
          * `.bottomRight`

        ### SwiftUI

        The following example shows how to set layout parameters and switch them at runtime:

        ```swift  theme={null}
        struct SwiftLayout: View {
            @State private var fit: RiveFit = .contain
            @State private var alignment: RiveAlignment = .center

            var body: some View {
                VStack {
                    RiveViewModel(fileName: "fancy_rive_file", fit: fit, alignment: alignment).view()
                }
                HStack {
                    Text("Some Fit Examples")
                }
                HStack {
                    Button("Fill") { fit = .fill }
                    Button("Contain") { fit = .contain }
                    Button("Cover") { fit = .cover }
                }
                HStack {
                    Text("Some Alignment Examples")
                }
                HStack {
                    Button("Top Left") { alignment = .topLeft }
                    Button("Top Center") { alignment = .topCenter }
                    Button("Top Right") { alignment = .topRight }
                }
            }
        }
        ```

        ### UIKit

        The following example shows how to set layout parameters and switch them at runtime:

        ```swift  theme={null}
        class LayoutViewController: UIViewController {
            @IBOutlet weak var riveView: RiveView!
            var viewModel = RiveViewModel(fileName: "fancy_rive_file")

            override func viewDidLoad() {
                viewModel.setView(riveView)
            }

            @IBAction func fitButtonTriggered(_ sender: UIButton) {
                setFit(name: sender.currentTitle!)
            }

            @IBAction func alignmentButtonTriggered(_ sender: UIButton) {
                setAlignment(name: sender.currentTitle!)
            }

            func setFit(name: String) {
                var fit: RiveFit = .contain
                switch name {
                case "Fill": fit = .fill
                case "Contain": fit = .contain
                case "Cover": fit = .cover
                case "Fit Width": fit = .fitWidth
                case "Fit Height": fit = .fitHeight
                case "Scale Down": fit = .scaleDown
                case "None": fit = .noFit
                default: fit = .contain
                }
                viewModel.fit = fit
            }

            func setAlignment(name: String) {
                var alignment: RiveAlignment = .center
                switch name {
                case "Top Left": alignment = .topLeft
                case "Top Center": alignment = .topCenter
                case "Top Right": alignment = .topRight
                case "Center Left": alignment = .centerLeft
                case "Center": alignment = .center
                case "Center Right": alignment = .centerRight
                case "Bottom Left": alignment = .bottomLeft
                case "Bottom Center": alignment = .bottomCenter
                case "Bottom Right": alignment = .bottomRight
                default: alignment = .center
                }
                viewModel.alignment = alignment
            }
        }
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Android">
    <Tabs>
      <Tab title="Compose">
        The `Fit` sealed class is used to specify the fit mode. On all variants other than `Layout` and `Fill`, the `Alignment` enum can be supplied to specify the alignment. Note that because this is a class, it must be constructed. If an alignment is not provided, it defaults to `Alignment.Center`.

        ```kotlin  theme={null}
        Rive(
            myRiveFile,
            fit = Fit.Cover(Alignment.TopCenter)
        )
        ```
      </Tab>

      <Tab title="Legacy">
        The `Fit` enum specifies the fit mode with the follow options: `LAYOUT`, `CONTAIN`, `SCALE_DOWN`, `COVER`, `FIT_WIDTH`, `FIT_HEIGHT`, `FILL`, and `NONE`.

        The `Alignment` enum specifies the alignment with the following options: `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER`, `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, and `BOTTOM_RIGHT`.

        ### Using XML Layouts

        The fit and alignment enum values can be applied to the `riveFit` and `riveAlignment` attributes in your XML layout:

        ```xml  theme={null}
        <app.rive.runtime.kotlin.RiveAnimationView
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            app:riveResource="@raw/my_rive_file"
            app:riveAlignment="CENTER"
            app:riveFit="CONTAIN"
        />
        ```

        ### Using Kotlin

        The fit and alignment enum values can be applied to the `fit` and `alignment` properties on your `RiveAnimationView` instance:

        ```kotlin  theme={null}
        animationView.fit = Fit.FILL
        animationView.alignment = Alignment.CENTER
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>

## Responsive Layouts

Rive’s layout feature lets you design resizable artboards with built-in responsive behavior, configured from the editor. Ensure the fit mode is set to **Layout** at runtime and the artboard will resize to fill its container according to the constraints defined in the editor.

Optionally you may provide a **layout scale factor** to multiply the scale of the content. This allows fine tuning the visual size within your container. This property only applies when setting the **Fit** mode to **Layout**.

For more Editor information and how to configure your graphic, see [Layouts Overview](/editor/layouts/layouts-overview).

<Tabs>
  <Tab title="Web">
    **Steps**

    1. Set `fit` to `Fit.Layout` - this will automatically scale and resize the artboard to match the canvas size when calling `resizeDrawingSurfaceToCanvas()`.
    2. Optionally set `layoutScaleFactor` for manual control of the artboard size (scale factor).
    3. Subscribe to `window.onresize` and call `resizeDrawingSurfaceToCanvas()` to adjust the artboard size as the canvas and window changes.
    4. Subscribe to **device pixel ratio** changes and call `resizeDrawingSurfaceToCanvas()` to ensure the artboard updates correctly on various screen densities. For example, when dragging the window between multiple monitors with different device pixel ratios.

    ```javascript  theme={null}
    <style>
      body {
        background: #f0f0f0;
        margin: 0;
        overflow: hidden;
      }

      canvas {
        background-color: red;
        display: block;
        width: 100vw;
        height: 100vh;
      }
    </style>

    <canvas id="riveCanvas"></canvas>

    <script src="https://unpkg.com/@rive-app/canvas@latest"></script>

    <script>
      const rive = new Rive({
        src: "your-rive-file.riv",
        autoplay: true,
        canvas: riveCanvas,
        layout: new Layout({
          fit: Fit.Layout,
          // layoutScaleFactor: 2, // 2x scale of the layout, when using `Fit.Layout`. This allows you to resize the layout as needed.
        }),
        stateMachines: ["State Machine 1"],
        onLoad: () => {
          computeSize();
        },
      });

      function computeSize() {
        rive.resizeDrawingSurfaceToCanvas();
      }

      // Subscribe to window size changes and update call `resizeDrawingSurfaceToCanvas`
      window.onresize = computeSize;

      // Subscribe to devicePixelRatio changes and call `resizeDrawingSurfaceToCanvas`
      window
        .matchMedia(`(resolution: ${window.devicePixelRatio}dppx)`)
        .addEventListener("change", computeSize);
    </script>
    ```
  </Tab>

  <Tab title="React">
    **Steps**

    1. Set `fit` to `Fit.Layout` in the `Layout` object - this will automatically scale and resize the artboard to match the canvas size.
    2. Pass the `Layout` object to the `layout` prop in `useRive`.
    3. Optionally set `layoutScaleFactor` in the `Layout` object for manual control of the artboard's scale factor.
    4. The React runtime automatically handles window resizing and device pixel ratio changes.

    ```jsx  theme={null}
    import { useRive, Layout, Fit } from "@rive-app/react-canvas";

    export const RiveComponent = () => {
      const { RiveComponent } = useRive({
        src: "your-rive-file.riv",
        stateMachines: "State Machine 1",
        layout: new Layout({
          fit: Fit.Layout,
          // layoutScaleFactor: 2, // Optional: 2x scale of the layout
        }),
        autoplay: true,
      });

      return <RiveComponent />;
    };
    ```
  </Tab>

  <Tab title="React Native">
    <Tabs>
      <Tab title="New Runtime (Recommended)">
        **Steps**

        1. Set `fit` to `Fit.Layout` - this will automatically scale and resize the artboard to match the view size.
        2. Optionally set the `layoutScaleFactor` for manual control of the artboard size (scale factor). If not set, the graphic uses the DPI of the device for scaling.

        ```javascript  theme={null}
        export default function ResponsiveLayoutsExample() {
          const { riveFile, isLoading, error } = useRiveFile(
            require('path/to/file.riv')
          );
          const [scaleFactor, setScaleFactor] = useState(4.0);
          const riveRef = useRef<RiveViewRef>(null);
          const { width, height } = useWindowDimensions();

          useEffect(() => {
            riveRef.current?.playIfNeeded();
          }, [width, height]);

          const increaseScale = () => {
            setScaleFactor((prev) => prev + 0.5);
            riveRef.current?.playIfNeeded();
          };
          const decreaseScale = () => {
            setScaleFactor((prev) => Math.max(0.5, prev - 0.5));
            riveRef.current?.playIfNeeded();
          };

          return (
            <View style={styles.container}>
              {isLoading ? (
                <ActivityIndicator size="large" color="#0000ff" />
              ) : error ? (
                <Text style={styles.errorText}>{error}</Text>
              ) : riveFile ? (
                <RiveView
                  hybridRef={{ f: (ref) => (riveRef.current = ref) }}
                  file={riveFile}
                  fit={Fit.Layout}
                  layoutScaleFactor={scaleFactor}
                  style={styles.rive}
                  autoPlay={true}
                />
              ) : null}
              <View style={styles.controls}>
                <Text style={styles.label}>Layout Scale Factor</Text>
                <View style={styles.scaleControls}>
                  <Button title="-" onPress={decreaseScale} />
                  <View style={styles.scaleText}>
                    <Text>{scaleFactor.toFixed(1)}x</Text>
                  </View>
                  <Button title="+" onPress={increaseScale} />
                </View>
              </View>
            </View>
          );
        }
        ```

        <Note>The call to `playIfNeeded()` ensures that the graphic is visually updated after the change. In the future this will be handled automatically.</Note>
      </Tab>

      <Tab title="Legacy Runtime">
        **Examples**

        * [Layout React Native Example](https://github.com/rive-app/rive-react-native/blob/main/example/app/\(examples\)/ResponsiveLayout.tsx)

        **Steps**

        1. Set `fit` to `Fit.Layout` - this will automatically scale and resize the artboard to match the canvas size.
        2. Optionally set `layoutScaleFactor` in the `Layout` object for manual control of the artboard's scale factor.
        3. The React Native runtime automatically handles window resizing and device pixel ratio changes.

        ```javascript  theme={null}
        import Rive, { Fit } from 'rive-react-native';

        const resourceName = 'layout_test';

        export default function ResponsiveLayout() {
          return (
            <Rive
              autoplay={true}
              fit={Fit.Layout}
              layoutScaleFactor={0.5} // If you do not set this (or set equal to "-1.0"), Rive will automatically scale the layout to match the device pixel ratio
              resourceName={resourceName}
              artboardName={'Artboard'}
              stateMachineName={'State Machine 1'}
            />
          );
        }
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Flutter">
    Pass the `Fit.layout` to the `RiveWidget` widget. This will automatically scale and resize the artboard to match the widget size.
    You can also set the `layoutScaleFactor` to control the scale of the artboard. This is useful for adjusting the size of the artboard when using `Fit.layout`.

    ```dart  theme={null}
    return RiveWidget(
      controller: controller,
      fit: Fit.layout,
      layoutScaleFactor: 2.0, // Optional: 2x scale of the layout,
    );
    ```

    Alternatively, you can also set the `fit` and `layoutScaleFactor` properties directly on any `RivePainter`, such as the `RiveWidgetController`:

    ```dart  theme={null}
    final controller = RiveWidgetController(riveFile);
    controller.fit = Fit.layout;
    controller.layoutScaleFactor = 2.0; // Optional: 2x scale of the layout
    ```
  </Tab>

  <Tab title="Apple">
    <Tabs>
      <Tab title={Apple.currentRuntimeName}>
        When creating a new `Rive` object, you can set the fit to layout, with two options for the scale factor: automatic or explicit.

        ```swift  theme={null}
        let file = try await File(source: ..., worker: Worker())
        // Create a new Rive object with a layout fit that automatically determines the scale factor based on the screen the view is being displayed on
        var rive = try await Rive(file: file, fit: .layout(scaleFactor: .automatic))
        // Or, use an explicit scale factor
        rive.fit = .layout(scaleFactor: .explicit(2.0))
        ```
      </Tab>

      <Tab title={Apple.legacyRuntimeName} borderBottom>
        **Examples**

        * [SwiftUI](https://github.com/rive-app/rive-ios/blob/main/Example-iOS/Source/Examples/SwiftUI/SwiftLayout.swift)

        **Steps**

        1. Set `fit` on an instance of `RiveViewModel` to `layout`
        2. Optionally set `layoutScaleFactor` on `RiveViewModel` for manual control of an artboard's scale factor.

        <Info>
          To enable automatically determining the scale factor, set `.layoutScaleFactor` to `RiveViewModel.layoutScaleFactorAutomatic`. This is the default value; it is equivalent to `-1`. When set, Rive will listen for window and screen changes for the view model's view, and automatically apply the correct scale factor for the current view hierarchy.
        </Info>

        ```swift  theme={null}
        let viewModel = RiveViewModel(fileName: "...")
        viewModel.fit = .layout
        viewModel.layoutScaleFactor = RiveViewModel.layoutScaleFactorAutomatic // Allow Rive to determine the scale factor
        viewModel.layoutScaleFactor = 2.0 // Or, explicitly set the scale factor
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="Android">
    <Tabs>
      <Tab title="Compose">
        See also the [Compose Layout](https://github.com/rive-app/rive-android/blob/master/app/src/main/java/app/rive/runtime/example/ComposeLayoutActivity.kt) sample.

        Set the `fit` parameter to `Fit.Layout` in the `Rive` composable. This will resize the artboard to match the container size. The `Fit.Layout` constructor takes an optional `layoutScaleFactor` parameter to adjust the scale of the artboard. By default it is 1, i.e. no scaling.

        ```kotlin  theme={null}
        Rive(
            myRiveFile,
            fit = Fit.Layout(1.2f) // 1.2x scale
        )
        ```
      </Tab>

      <Tab title="Legacy">
        ### Sample

        See the [Layout](https://github.com/rive-app/rive-android/blob/master/app/src/main/java/app/rive/runtime/example/LayoutActivity.kt) sample.

        ### Using XML Layouts

        Set the `riveFit` attribute to `"LAYOUT"`.

        ```kotlin  theme={null}
        <app.rive.runtime.kotlin.RiveAnimationView
            ...
            app:riveFit="LAYOUT"
        />
        ```

        ### Using Kotlin

        Set the RiveAnimationView's `fit` property to `LAYOUT`.

        ```kotlin  theme={null}
        val animationView = findViewById<RiveAnimationView>(R.id.my_view)
        animationView.fit = Fit.LAYOUT
        ```

        ### Adjusting the Layout Scale Factor

        To adjust the scale factor of the contents, use the `layoutScaleFactor` property. This is nullable, so by default, it will use the density as reported by `resources.displayMetrics.density`. You can override this to any positive float value, or return control to the system by resetting to `null`:

        ```kotlin  theme={null}
        // Force a set scale factor
        animationView.layoutScaleFactor = 2.5f
        // Reset to system control
        animationView.layoutScaleFactor = null
        ```

        ### Resizing the Artboard

        The artboard size can be manually controlled by using the `width` and `height` properties. `resetArtboardSize()` can be used to return these values to their defaults.

        ```kotlin  theme={null}
        // Force a certain artboard size
        animationView.controller.activeArtboard?.width = 1000f
        animationView.controller.activeArtboard?.height = 1000f
        // Reset the artboard size to defaults
        animationView.controller.activeArtboard?.resetArtboardSize()
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
