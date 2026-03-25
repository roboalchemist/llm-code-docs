# Source: https://uat.rive.app/docs/feature-support.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Feature Support

export const FeatureSupportGroup = ({feature, runtime, children}) => {
  const defaultOpen = false;
  const runtimeTitles = {
    webCanvas: "Web - Canvas",
    webWebGL: "Web - WebGL (Legacy)",
    webWebGL2: "Web - WebGL2",
    webCanvasLite: "Web - Canvas Lite",
    reactCanvas: "React - Canvas",
    reactCanvasLite: "React - Canvas Lite",
    reactWebGL: "React - WebGL (Legacy)",
    reactWebGL2: "React - WebGL2",
    reactNative: "React Native",
    reactNativeLegacy: "React Native (Legacy)",
    flutter: "Flutter",
    apple: "Apple",
    android: "Android",
    cpp: "C++",
    unity: "Unity",
    unreal: "Unreal"
  };
  const runtimesInOrder = ["webWebGL2", "webCanvas", "webCanvasLite", "reactWebGL2", "reactCanvas", "reactCanvasLite", "reactNative", "flutter", "apple", "android", "cpp", "unity", "unreal", "webWebGL", "reactWebGL", "reactNativeLegacy"];
  const legacyRuntimes = ["webWebGL", "reactWebGL", "reactNativeLegacy"];
  const featuresInOrder = ["scripting", "dataBindingListsImagesArtboards", "rightToLeftLayoutsText", "textFollowPath", "dataBinding", "vectorFeathering", "nSlicing", "layouts", "fallbackFonts", "randomization", "audio", "outOfBandAssets", "text", "followPath", "interpolationOnStates", "joysticks", "solos", "speedOnStates", "graphEditor", "listeners", "meshDeformation", "cachingARiveFile", "rasterAssets", "events", "nestedText"];
  const features = {
    scripting: {
      title: "Scripting",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.34.0+"
        },
        webCanvasLite: {
          supported: true,
          version: "2.34.0+"
        },
        webWebGL: {
          supported: true,
          version: "2.34.0+"
        },
        webWebGL2: {
          supported: true,
          version: "2.34.0+"
        },
        reactCanvas: {
          supported: true,
          version: "4.26.0+"
        },
        reactCanvasLite: {
          supported: true,
          version: "4.26.0+"
        },
        reactWebGL: {
          supported: true,
          version: "4.26.0+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.26.0+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.5+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "v9.8.0+"
        },
        flutter: {
          supported: true,
          version: "0.14.1"
        },
        apple: {
          supported: true,
          version: "v6.13.0+"
        },
        android: {
          supported: true,
          version: "v11.1.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          version: "v0.4.1-canary.33+"
        },
        unreal: {
          supported: true,
          version: "v0.4.20+"
        }
      }
    },
    dataBindingListsImagesArtboards: {
      title: "Data Binding - Lists, Images, and Artboards",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.30.3+"
        },
        webCanvasLite: {
          supported: true,
          version: "2.30.3+"
        },
        webWebGL: {
          supported: true,
          version: "2.30.3+"
        },
        webWebGL2: {
          supported: true,
          version: "2.30.3+"
        },
        reactCanvas: {
          supported: true,
          version: "4.22.0+"
        },
        reactCanvasLite: {
          supported: true,
          version: "4.22.0+"
        },
        reactWebGL: {
          supported: true,
          version: "4.22.0+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.22.0+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: false,
          description: "Not supported"
        },
        flutter: {
          supported: true,
          version: "0.14.0-dev.1"
        },
        apple: {
          supported: true,
          version: "v6.11.0+"
        },
        android: {
          supported: true,
          version: "v10.4.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          version: "v0.3.7-canary.142"
        },
        unreal: {
          supported: false,
          description: "Not yet supported"
        }
      }
    },
    rightToLeftLayoutsText: {
      title: "Right to Left Layouts & Text",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.26.7+"
        },
        webCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        webWebGL: {
          supported: true,
          version: "2.26.7+"
        },
        webWebGL2: {
          supported: true,
          version: "2.26.7+"
        },
        reactCanvas: {
          supported: true,
          version: "4.18.6+"
        },
        reactCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        reactWebGL: {
          supported: true,
          version: "4.18.6+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.18.6+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "9.2.1+"
        },
        flutter: {
          supported: true,
          version: "0.14.0-dev.1"
        },
        apple: {
          supported: true,
          version: "6.7.4+"
        },
        android: {
          supported: true,
          version: "10.0.4"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          version: "0.3.5+"
        },
        unreal: {
          supported: true,
          version: "0.3.0a-gh"
        }
      }
    },
    textFollowPath: {
      title: "Text Follow Path",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.26.7+"
        },
        webCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        webWebGL: {
          supported: true,
          version: "2.26.7+"
        },
        webWebGL2: {
          supported: true,
          version: "2.26.7+"
        },
        reactCanvas: {
          supported: true,
          version: "4.18.6+"
        },
        reactCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        reactWebGL: {
          supported: true,
          version: "4.18.6+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.18.6+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "9.2.1+"
        },
        flutter: {
          supported: true,
          version: "0.14.0-dev.1"
        },
        apple: {
          supported: true,
          version: "6.7.4+"
        },
        android: {
          supported: true,
          version: "10.0.4"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          version: "0.3.5+"
        },
        unreal: {
          supported: true,
          version: "0.3.0a-gh"
        }
      }
    },
    dataBinding: {
      title: "Data Binding",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.26.6+"
        },
        webCanvasLite: {
          supported: true,
          version: "2.26.6+"
        },
        webWebGL: {
          supported: true,
          version: "2.26.6+"
        },
        webWebGL2: {
          supported: true,
          version: "2.26.6+"
        },
        reactCanvas: {
          supported: true,
          version: "4.20.0+"
        },
        reactCanvasLite: {
          supported: true,
          version: "4.20.0+"
        },
        reactWebGL: {
          supported: true,
          version: "4.20.0+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.20.0+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "9.3.0+"
        },
        flutter: {
          supported: true,
          version: "0.14.0-dev.1"
        },
        apple: {
          supported: true,
          version: "6.8.0+"
        },
        android: {
          supported: true,
          version: "10.1.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          version: "0.3.6-canary.27"
        },
        unreal: {
          supported: true,
          version: "0.3.0a-gh"
        }
      }
    },
    vectorFeathering: {
      title: "Vector Feathering",
      runtimes: {
        webWebGL2: {
          supported: true,
          version: "2.26.0+"
        },
        webCanvas: {
          supported: false,
          description: "Not supported"
        },
        webCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        webWebGL: {
          supported: false,
          description: "Not supported"
        },
        reactWebGL2: {
          supported: true,
          version: "4.18.0+"
        },
        reactCanvas: {
          supported: false,
          description: "Not supported"
        },
        reactCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        reactWebGL: {
          supported: false,
          description: "Not supported"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "9.0.0+"
        },
        flutter: {
          supported: true,
          version: "0.14.0-dev.1"
        },
        apple: {
          supported: true,
          version: "6.6.0+"
        },
        android: {
          supported: true,
          version: "10.0.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          version: "0.3.3-canary.72+"
        },
        unreal: {
          supported: true,
          version: "0.3.0a-gh"
        }
      }
    },
    nSlicing: {
      title: "N-Slicing",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.23.11+"
        },
        webCanvasLite: {
          supported: true,
          version: "2.23.11+"
        },
        webWebGL: {
          supported: true,
          version: "2.23.11+"
        },
        webWebGL2: {
          supported: true,
          version: "2.23.11+"
        },
        reactCanvas: {
          supported: true,
          version: "4.16.7+"
        },
        reactCanvasLite: {
          supported: true,
          version: "4.16.7+"
        },
        reactWebGL: {
          supported: true,
          version: "4.16.7+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.16.7+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "8.2.0+"
        },
        flutter: {
          supported: true,
          version: "0.14.0-dev.1"
        },
        apple: {
          supported: true,
          version: "6.4.0+"
        },
        android: {
          supported: true,
          version: "9.12.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          version: "0.2.2-canary.22+"
        },
        unreal: {
          supported: true,
          version: "0.2.2+"
        }
      }
    },
    layouts: {
      title: "Layouts",
      runtimes: {
        webWebGL2: {
          supported: true,
          version: "2.23.3+"
        },
        webCanvas: {
          supported: true,
          version: "2.23.3+"
        },
        webCanvasLite: {
          supported: true,
          version: "2.23.3+"
        },
        webWebGL: {
          supported: true,
          version: "2.23.3+"
        },
        reactCanvas: {
          supported: true,
          version: "4.16.0+"
        },
        reactCanvasLite: {
          supported: true,
          version: "4.16.0+"
        },
        reactWebGL: {
          supported: true,
          version: "4.16.0+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.16.0+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "8.1.0+"
        },
        flutter: {
          supported: true,
          version: "0.14.0-dev.1"
        },
        apple: {
          supported: true,
          version: "6.3.0+"
        },
        android: {
          supported: true,
          version: "9.10.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          version: "0.2.1+"
        },
        unreal: {
          supported: true,
          version: "0.2.1+"
        }
      }
    },
    fallbackFonts: {
      title: "Fallback Fonts",
      runtimes: {
        webCanvas: {
          supported: false,
          description: "Not yet supported"
        },
        webCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        webWebGL: {
          supported: false,
          description: "Not supported"
        },
        webWebGL2: {
          supported: false,
          description: "Not yet supported"
        },
        reactCanvas: {
          supported: false,
          description: "Not yet supported"
        },
        reactCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        reactWebGL: {
          supported: false,
          description: "Not supported"
        },
        reactWebGL2: {
          supported: false,
          description: "Not yet supported"
        },
        reactNative: {
          supported: true,
          version: "0.2.7+"
        },
        reactNativeLegacy: {
          supported: false,
          description: "Not supported"
        },
        flutter: {
          supported: false,
          description: "Not yet supported"
        },
        apple: {
          supported: true,
          version: "6.1.0+"
        },
        android: {
          supported: true,
          version: "9.7.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: false,
          description: "Not supported"
        },
        unreal: {
          supported: false,
          description: "Not Supported"
        }
      }
    },
    nestedText: {
      title: "Nested Text (deprecated)",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.21.0+"
        },
        webCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        webWebGL: {
          supported: true,
          version: "2.21.0+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "4.14.0+"
        },
        reactCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        reactWebGL: {
          supported: true,
          version: "4.14.0+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.14.0+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "5.8.2+"
        },
        flutter: {
          supported: true,
          version: "0.13.7+"
        },
        apple: {
          supported: true,
          version: "6.1.0+"
        },
        android: {
          supported: true,
          version: "9.8.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          version: "0.1.14+"
        }
      }
    },
    randomization: {
      title: "Randomization",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.15.6+"
        },
        webCanvasLite: {
          supported: true,
          version: "2.15.6+"
        },
        webWebGL: {
          supported: true,
          version: "2.15.6+"
        },
        webWebGL2: {
          supported: true,
          version: "2.15.6+"
        },
        reactCanvas: {
          supported: true,
          version: "4.9.5+"
        },
        reactCanvasLite: {
          supported: true,
          version: "4.9.5+"
        },
        reactWebGL: {
          supported: true,
          version: "4.9.5+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.9.5+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "7.0.3+"
        },
        flutter: {
          supported: true,
          version: "0.13.4+"
        },
        apple: {
          supported: true,
          version: "5.11.5+"
        },
        android: {
          supported: true,
          version: "9.3.5+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    audio: {
      title: "Audio",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.15.6+"
        },
        webCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        webWebGL: {
          supported: true,
          version: "2.15.6+"
        },
        webWebGL2: {
          supported: true,
          version: "2.15.6+"
        },
        reactCanvas: {
          supported: true,
          version: "4.9.5+"
        },
        reactCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        reactWebGL: {
          supported: true,
          version: "4.9.5+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.9.5+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "7.0.3+"
        },
        flutter: {
          supported: true,
          version: "0.13.4+"
        },
        apple: {
          supported: true,
          version: "5.11.5+"
        },
        android: {
          supported: true,
          version: "9.3.5+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    outOfBandAssets: {
      title: "Out-of-band Assets",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.7.0+"
        },
        webCanvasLite: {
          supported: true,
          version: "2.7.0+"
        },
        webWebGL: {
          supported: true,
          version: "2.7.0+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "4.5.0+"
        },
        reactCanvasLite: {
          supported: true,
          version: "4.5.0+"
        },
        reactWebGL: {
          supported: true,
          version: "4.5.0+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.5.0+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "8.4.0+"
        },
        flutter: {
          supported: true,
          version: "0.12.0+"
        },
        apple: {
          supported: true,
          version: "5.7.0+"
        },
        android: {
          supported: true,
          version: "8.6.1+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: false,
          description: "Not yet supported"
        }
      }
    },
    events: {
      title: "Events (deprecated)",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.4.3+"
        },
        webCanvasLite: {
          supported: true,
          version: "2.4.3+"
        },
        webWebGL: {
          supported: true,
          version: "2.4.3+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "4.3.3+"
        },
        reactCanvasLite: {
          supported: true,
          version: "4.3.3+"
        },
        reactWebGL: {
          supported: true,
          version: "4.3.3+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.3.3+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "6.1.0+"
        },
        flutter: {
          supported: true,
          version: "0.11.17+"
        },
        apple: {
          supported: true,
          version: "5.3.1+"
        },
        android: {
          supported: false,
          description: "Deprecated and will be removed in future versions"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    text: {
      title: "Text",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "2.1.3+"
        },
        webCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        webWebGL: {
          supported: true,
          version: "2.1.3+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "4.1.3+"
        },
        reactCanvasLite: {
          supported: false,
          description: "Not supported"
        },
        reactWebGL: {
          supported: true,
          version: "4.1.3+"
        },
        reactWebGL2: {
          supported: true,
          version: "4.1.3+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "6.0.3+"
        },
        flutter: {
          supported: true,
          version: "0.11.14+"
        },
        apple: {
          supported: true,
          version: "5.1.5+"
        },
        android: {
          supported: true,
          version: "8.1.3+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    followPath: {
      title: "Follow Path",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "1.2.4+"
        },
        webCanvasLite: {
          supported: true,
          version: "1.2.4+"
        },
        webWebGL: {
          supported: true,
          version: "1.2.4+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "3.0.55+"
        },
        reactCanvasLite: {
          supported: true,
          version: "3.0.55+"
        },
        reactWebGL: {
          supported: true,
          version: "3.0.55+"
        },
        reactWebGL2: {
          supported: true,
          version: "3.0.55+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "5.0.0+"
        },
        flutter: {
          supported: true,
          version: "0.11.6+"
        },
        apple: {
          supported: true,
          version: "4.0.5+"
        },
        android: {
          supported: true,
          version: "6.0.1+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    interpolationOnStates: {
      title: "Interpolation on States",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "1.2.1+"
        },
        webCanvasLite: {
          supported: true,
          version: "1.2.1+"
        },
        webWebGL: {
          supported: true,
          version: "1.2.1+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "3.0.54+"
        },
        reactCanvasLite: {
          supported: true,
          version: "3.0.54+"
        },
        reactWebGL: {
          supported: true,
          version: "3.0.54+"
        },
        reactWebGL2: {
          supported: true,
          version: "3.0.54+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "4.1.2+"
        },
        flutter: {
          supported: true,
          version: "0.11.4+"
        },
        apple: {
          supported: true,
          version: "4.0.4+"
        },
        android: {
          supported: true,
          version: "5.1.5+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    joysticks: {
      title: "Joysticks",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "1.1.9+"
        },
        webCanvasLite: {
          supported: true,
          version: "1.1.9+"
        },
        webWebGL: {
          supported: true,
          version: "1.1.9+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "3.0.49+"
        },
        reactCanvasLite: {
          supported: true,
          version: "3.0.49+"
        },
        reactWebGL: {
          supported: true,
          version: "3.0.49+"
        },
        reactWebGL2: {
          supported: true,
          version: "3.0.49+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "4.1.0+"
        },
        flutter: {
          supported: true,
          version: "0.11.1+"
        },
        apple: {
          supported: true,
          version: "4.0.1+"
        },
        android: {
          supported: true,
          version: "5.0.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    solos: {
      title: "Solos",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "1.1.2+"
        },
        webCanvasLite: {
          supported: true,
          version: "1.1.2+"
        },
        webWebGL: {
          supported: true,
          version: "1.1.2+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "3.0.42+"
        },
        reactCanvasLite: {
          supported: true,
          version: "3.0.42+"
        },
        reactWebGL: {
          supported: true,
          version: "3.0.42+"
        },
        reactWebGL2: {
          supported: true,
          version: "3.0.42+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "4.0.4+"
        },
        flutter: {
          supported: true,
          version: "0.10.4+"
        },
        apple: {
          supported: true,
          version: "3.1.9+"
        },
        android: {
          supported: true,
          version: "4.4.0+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    speedOnStates: {
      title: "Speed on States",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "1.0.102+"
        },
        webCanvasLite: {
          supported: true,
          version: "1.0.102+"
        },
        webWebGL: {
          supported: true,
          version: "1.0.98+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "3.0.38+"
        },
        reactCanvasLite: {
          supported: true,
          version: "3.0.38+"
        },
        reactWebGL: {
          supported: true,
          version: "3.0.38+"
        },
        reactWebGL2: {
          supported: true,
          version: "3.0.38+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "4.0.1+"
        },
        flutter: {
          supported: true,
          version: "0.10.3+"
        },
        apple: {
          supported: true,
          version: "3.1.7+"
        },
        android: {
          supported: true,
          version: "4.2.7+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    graphEditor: {
      title: "Graph Editor",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "1.0.97+"
        },
        webCanvasLite: {
          supported: true,
          version: "1.0.97+"
        },
        webWebGL: {
          supported: true,
          version: "1.0.93+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "3.0.34+"
        },
        reactCanvasLite: {
          supported: true,
          version: "3.0.34+"
        },
        reactWebGL: {
          supported: true,
          version: "3.0.34+"
        },
        reactWebGL2: {
          supported: true,
          version: "3.0.34+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "4.0.1+"
        },
        flutter: {
          supported: true,
          version: "0.10.0+"
        },
        apple: {
          supported: true,
          version: "3.1.3+"
        },
        android: {
          supported: true,
          version: "4.2.2+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    listeners: {
      title: "Listeners",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "1.0.65+"
        },
        webCanvasLite: {
          supported: true,
          version: "1.0.65+"
        },
        webWebGL: {
          supported: true,
          version: "1.0.62+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "3.0.6+"
        },
        reactCanvasLite: {
          supported: true,
          version: "3.0.6+"
        },
        reactWebGL: {
          supported: true,
          version: "3.0.6+"
        },
        reactWebGL2: {
          supported: true,
          version: "3.0.6+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "3.0.38+"
        },
        flutter: {
          supported: true,
          version: "0.9.0+"
        },
        apple: {
          supported: true,
          version: "2.0.21+"
        },
        android: {
          supported: true,
          version: "3.0.8+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    meshDeformation: {
      title: "Mesh Deformation",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "1.0.47+"
        },
        webCanvasLite: {
          supported: true,
          version: "1.0.47+"
        },
        webWebGL: {
          supported: true,
          version: "1.0.44+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "3.0.1+"
        },
        reactCanvasLite: {
          supported: true,
          version: "3.0.1+"
        },
        reactWebGL: {
          supported: true,
          version: "3.0.1+"
        },
        reactWebGL2: {
          supported: true,
          version: "3.0.1+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "2.1.37+"
        },
        flutter: {
          supported: true,
          version: "0.8.4+"
        },
        apple: {
          supported: true,
          version: "1.0.18+"
        },
        android: {
          supported: true,
          version: "2.0.24+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    },
    cachingARiveFile: {
      title: "Caching a Rive File",
      runtimes: {
        webCanvas: {
          supported: true,
          description: "Supported"
        },
        webCanvasLite: {
          supported: true,
          description: "Supported"
        },
        webWebGL: {
          supported: true,
          description: "Supported"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          description: "Supported"
        },
        reactCanvasLite: {
          supported: true,
          description: "Supported"
        },
        reactWebGL: {
          supported: true,
          description: "Supported"
        },
        reactWebGL2: {
          supported: true,
          description: "Supported"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: false,
          description: "Not supported"
        },
        flutter: {
          supported: true,
          description: "Supported"
        },
        apple: {
          supported: true,
          description: "Supported"
        },
        android: {
          supported: true,
          description: "Supported"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: false,
          description: "Not yet supported"
        }
      }
    },
    rasterAssets: {
      title: "Raster Assets",
      runtimes: {
        webCanvas: {
          supported: true,
          version: "1.0.2+"
        },
        webCanvasLite: {
          supported: true,
          version: "1.0.2+"
        },
        webWebGL: {
          supported: true,
          version: "1.0.2+"
        },
        webWebGL2: {
          supported: true,
          version: "2.11.0+"
        },
        reactCanvas: {
          supported: true,
          version: "0.0.28+"
        },
        reactCanvasLite: {
          supported: true,
          version: "0.0.28+"
        },
        reactWebGL: {
          supported: true,
          version: "0.0.28+"
        },
        reactWebGL2: {
          supported: true,
          version: "0.0.28+"
        },
        reactNative: {
          supported: true,
          version: "v0.1.4+"
        },
        reactNativeLegacy: {
          supported: true,
          version: "2.1.36+"
        },
        flutter: {
          supported: true,
          version: "0.8.1+"
        },
        apple: {
          supported: true,
          version: "1.0.1+"
        },
        android: {
          supported: true,
          version: "2.0.5+"
        },
        cpp: {
          supported: true,
          description: "Supported"
        },
        unity: {
          supported: true,
          description: "Supported"
        },
        unreal: {
          supported: true,
          description: "Supported"
        }
      }
    }
  };
  if (runtime) {
    return <Accordion title={runtimeTitles[runtime]} defaultOpen={defaultOpen}>
                 {children}
                <div data-table-wrapper="true" className="[--page-padding:20px] overflow-x-auto flex my-[1em] py-[1em] max-w-none [contain:inline-size]">
                    <div className="px-[var(--page-padding)] grow max-w-none table">
                        <table className="m-0 min-w-full w-full max-w-none [&_td]:min-w-[150px] [&_th]:text-left [&_td[data-numeric]]:tabular-nums">
                            <thead className="w-full">
                                <tr>
                                    <th className="w-2/3">
                                        <strong>Feature</strong>
                                    </th>
                                    <th className="w-1/3">
                                        <strong>Version</strong>
                                    </th>
                                </tr>
                            </thead>
                            <tbody>

                                {featuresInOrder.map(featureKey => {
      const currentFeature = features[featureKey];
      const runtimeFeatureSupport = currentFeature.runtimes[runtime];
      console.log(runtimeFeatureSupport);
      if (!runtimeFeatureSupport) {
        return <tr>
                                                    <td>{currentFeature.title}</td>
                                                    <td>Unknown</td>
                                                </tr>;
      }
      const {supported, version, description} = runtimeFeatureSupport;
      return <tr>
                                                <td>{currentFeature.title}</td>
                                                {version && !description && <td data-numeric="true">
                                                            {supported && '✅ '}
                                                            <code>{version}</code>
                                                        </td>}
                                                {description && !version && <td>
                                                            {supported && '✅ '}
                                                            {description}
                                                        </td>}
                                            </tr>;
    })}

                            </tbody>
                        </table>
                    </div>
                </div>
            </Accordion>;
  }
  const currentFeature = features[feature];
  const allSupported = Object.entries(currentFeature.runtimes).filter(([runtimeKey]) => !legacyRuntimes.includes(runtimeKey)).every(([, runtimeSupport]) => runtimeSupport.supported === true);
  const statusEmoji = allSupported ? '✅' : '🟡';
  const titleWithEmoji = `${statusEmoji} ${currentFeature.title}`;
  return <Accordion title={titleWithEmoji} defaultOpen={defaultOpen}>
            {children}
            <div data-table-wrapper="true" className="[--page-padding:20px] overflow-x-auto flex my-[1em] py-[1em] max-w-none [contain:inline-size]">
                <div className="px-[var(--page-padding)] grow max-w-none table">
                    <table className="m-0 min-w-full w-full max-w-none [&_td]:min-w-[150px] [&_th]:text-left [&_td[data-numeric]]:tabular-nums">
                        <thead className="w-full">
                            <tr>
                                <th className="w-2/3">
                                    <strong>Runtime</strong>
                                </th>
                                <th className="w-1/3">
                                    <strong>Version</strong>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            {runtimesInOrder.map(runtimeKey => {
    const currentRuntime = currentFeature.runtimes[runtimeKey];
    if (!currentRuntime) {
      return <tr>
                                                <td>{runtimeTitles[runtimeKey]}</td>
                                                <td>Unknown</td>
                                            </tr>;
    }
    const {supported, version, description} = currentFeature.runtimes[runtimeKey];
    return <tr>
                                            <td>{runtimeTitles[runtimeKey]}</td>
                                            {version && !description && <td data-numeric="true">
                                                        {supported && '✅ '}
                                                        <code>{version}</code>
                                                    </td>}
                                            {description && !version && <td>
                                                        {supported && '✅ '}
                                                        {description}
                                                    </td>}
                                        </tr>;
  })}

                        </tbody>
                    </table>
                </div>
            </div>
        </Accordion>;
};

As the Rive Editor evolves, some new features require updates to the Rive runtimes. In certain cases, this may introduce new or modified APIs. We recommend staying on the latest runtime version to ensure compatibility, bug fixes, and performance improvements.

Use the table below to verify whether a feature used in your `.riv` file is supported by your target runtime.

<Warning>
  Certain features require the use of the Rive Renderer at runtime. See our
  documentation on [choosing a renderer](/runtimes/choose-a-renderer/).

  Currently, the only feature that requires the Rive Renderer is **[Vector
  Feathering](https://rive.app/blog/introducing-vector-feathering)**.
</Warning>

When a feature requires API changes, migration notes will be included below.

## Feature Support by Runtime

### Runtimes

<FeatureSupportGroup runtime="webWebGL2">
  Choose between @rive-app/webgl2 and @rive-app/canvas, with guidance on performance, package size, and when to use canvas-lite.
</FeatureSupportGroup>

<FeatureSupportGroup runtime="webCanvas">
  For better performance and the latest features, like vector feathering, we recommend using the WebGL2 runtime, which uses the Rive Renderer.
</FeatureSupportGroup>

<FeatureSupportGroup runtime="reactWebGL2" />

<FeatureSupportGroup runtime="reactCanvas" />

<FeatureSupportGroup runtime="reactNative" />

<FeatureSupportGroup runtime="flutter" />

<FeatureSupportGroup runtime="apple" />

<FeatureSupportGroup runtime="android" />

<FeatureSupportGroup runtime="cpp" />

<FeatureSupportGroup runtime="unity" />

<FeatureSupportGroup runtime="unreal" />

### Lite Runtimes

<FeatureSupportGroup runtime="webCanvasLite">
  This lightweight version uses the same API as `@rive-app/canvas`, but excludes certain features to reduce bundle size.
</FeatureSupportGroup>

<FeatureSupportGroup runtime="reactCanvasLite">
  This lightweight version uses the same API as `@rive-app/react-canvas`, but excludes certain features to reduce bundle size.
</FeatureSupportGroup>

### Legacy Runtimes

<FeatureSupportGroup runtime="webWebGL">
  <Warning>
    The `@rive-app/webgl` runtime is deprecated. For better performance and the latest features, use `@rive-app/webgl2`.
  </Warning>
</FeatureSupportGroup>

<FeatureSupportGroup runtime="reactWebGL">
  <Warning>
    The `@rive-app/react-webgl` runtime is deprecated. For better performance and the latest features, use `@rive-app/react-webgl2`.
  </Warning>
</FeatureSupportGroup>

<FeatureSupportGroup runtime="reactNativeLegacy">
  <Warning>
    The `rive-react-native` runtime is deprecated. For better performance and the latest features, use `rive-nitro-react-native`.

    [Migration guide](/feature-support#react-native-legacy)
  </Warning>
</FeatureSupportGroup>

## Runtime Support by Feature

A green checkmark (✅) indicates that a feature is supported in all current runtimes.
A yellow circle (🟡) indicates that support varies by runtime or renderer.

Differences may reflect:

* Platform or SDK limitations where a feature cannot be supported
* Staggered releases as features roll out across runtimes, or
* Lightweight (“lite”) builds that intentionally omit some features to reduce package size.

<Note>
  A feature may still be considered fully supported even if it is unavailable in legacy runtimes.
</Note>

### Features

<FeatureSupportGroup feature="scripting">
  Support for Rive files with [Scripting](/scripting).
</FeatureSupportGroup>

<FeatureSupportGroup feature="dataBindingListsImagesArtboards">
  Data binding lists, images, and artboards were added after initial data binding support.

  See [Data Binding Overview](/editor/data-binding/overview) and [Data Binding for Runtimes](/runtimes/data-binding).
</FeatureSupportGroup>

<FeatureSupportGroup feature="rightToLeftLayoutsText" />

<FeatureSupportGroup feature="textFollowPath" />

<FeatureSupportGroup feature="dataBinding">
  See [Data Binding Overview](/editor/data-binding/overview) and [Data Binding for Runtimes](/runtimes/data-binding).
</FeatureSupportGroup>

<FeatureSupportGroup feature="vectorFeathering" />

<FeatureSupportGroup feature="nSlicing">
  See [N-Slicing](/editor/layouts/n-slicing).
</FeatureSupportGroup>

<FeatureSupportGroup feature="layouts">
  Allows Rive to automatically update the artboard size as the underlying view/canvas/widget/texture size changes. See [Layouts](/editor/layouts/layouts-overview).
</FeatureSupportGroup>

<FeatureSupportGroup feature="fallbackFonts">
  Allows Rive to use a fallback font if a glyph is not available. A default font is automatically chosen, or you can optionally configure the desired fallback font based on various options. See [Fallback Fonts](/runtimes/text#fallback-fonts).
</FeatureSupportGroup>

<FeatureSupportGroup feature="randomization">
  Enables randomizing transitions between animations and customizing the probability.
</FeatureSupportGroup>

<FeatureSupportGroup feature="audio">
  See [Rive Events](/runtimes/rive-events) and [Audio Events](/editor/events/audio-events).
</FeatureSupportGroup>

<FeatureSupportGroup feature="outOfBandAssets">
  See [Loading Assets](/runtimes/loading-assets).
</FeatureSupportGroup>

<FeatureSupportGroup feature="text">
  See [Text](/runtimes/text).
</FeatureSupportGroup>

<FeatureSupportGroup feature="followPath" />

<FeatureSupportGroup feature="interpolationOnStates" />

<FeatureSupportGroup feature="joysticks" />

<FeatureSupportGroup feature="solos" />

<FeatureSupportGroup feature="speedOnStates" />

<FeatureSupportGroup feature="graphEditor" />

<FeatureSupportGroup feature="listeners" />

<FeatureSupportGroup feature="meshDeformation" />

<FeatureSupportGroup feature="cachingARiveFile" />

<FeatureSupportGroup feature="rasterAssets" />

### Legacy Features

<FeatureSupportGroup feature="events">
  <Warning>
    Listening to [Rive Events](/runtimes/rive-events) at runtime is deprecated and will be removed in future versions.

    Use [Data Binding](/runtimes/data-binding) to listen for triggers or changes to properties instead.
  </Warning>
</FeatureSupportGroup>

<FeatureSupportGroup feature="nestedText">
  <Warning>
    Setting text, including [nested text](/runtimes/text#read-update-nested-text-runs-at-runtime), at runtime is deprecated and will be removed in a future version.

    Instead, use [Data Binding](/runtimes/data-binding) to update a string, which is bound to a text run.
  </Warning>
</FeatureSupportGroup>
