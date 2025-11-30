# Source: https://www.electronjs.org/docs/latest/tutorial/native-code-and-electron-swift-macos

On this page

# Native Code and Electron: Swift (macOS)

This tutorial builds on the [general introduction to Native Code and Electron](/docs/latest/tutorial/native-code-and-electron) and focuses on creating a native addon for macOS using Swift.

Swift is a modern, powerful language designed for safety and performance. While you can\'t use Swift directly with the Node.js N-API as used by Electron, you can create a bridge using Objective-C++ to connect Swift with JavaScript in your Electron application.

To illustrate how you can embed native macOS code in your Electron app, we\'ll be building a basic native macOS GUI (using SwiftUI) that communicates with Electron\'s JavaScript.

This tutorial will be most useful to those who already have some familiarity with Objective-C, Swift, and SwiftUI development. You should understand basic concepts like Swift syntax, optionals, closures, SwiftUI views, property wrappers, and the Objective-C/Swift interoperability mechanisms such as the `@objc` attribute and bridging headers.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

If you\'re not already familiar with these concepts, Apple\'s [Swift Programming Language Guide](https://docs.swift.org/swift-book/), [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui/), and [Swift and Objective-C Interoperability Guide](https://developer.apple.com/documentation/swift/importing-swift-into-objective-c) are excellent starting points.

## Requirements[â€‹](#requirements "Direct link to Requirements") 

Just like our [general introduction to Native Code and Electron](/docs/latest/tutorial/native-code-and-electron), this tutorial assumes you have Node.js and npm installed, as well as the basic tools necessary for compiling native code on macOS. You\'ll need:

- Xcode installed (available from the Mac App Store)
- Xcode Command Line Tools (can be installed by running `xcode-select --install` in Terminal)

## 1) Creating a package[â€‹](#1-creating-a-package "Direct link to 1) Creating a package") 

You can re-use the package we created in our [Native Code and Electron](/docs/latest/tutorial/native-code-and-electron) tutorial. This tutorial will not be repeating the steps described there. Let\'s first setup our basic addon folder structure:

``` 
swift-native-addon/
âââ binding.gyp            # Build configuration
âââ include/
â   âââ SwiftBridge.h      # Objective-C header for the bridge
âââ js/
â   âââ index.js           # JavaScript interface
âââ package.json           # Package configuration
âââ src/
    âââ SwiftCode.swift    # Swift implementation
    âââ SwiftBridge.m      # Objective-C bridge implementation
    âââ swift_addon.mm     # Node.js addon implementation
```

Our `package.json` should look like this:

package.json

``` 
,
  "license": "MIT",
  "dependencies": ,
  "devDependencies": 
}
```

## 2) Setting Up the Build Configuration[â€‹](#2-setting-up-the-build-configuration "Direct link to 2) Setting Up the Build Configuration") 

In our other tutorials focusing on other native languages, we could use `node-gyp` to build the entirety of our code. With Swift, things are a bit more tricky: We need to first build and then link our Swift code. This is because Swift has its own compilation model and runtime requirements that don\'t directly integrate with node-gyp\'s C/C++ focused build system.

The process involves:

1.  Compiling Swift code separately into a static library (.a file)
2.  Creating an Objective-C bridge that exposes Swift functionality
3.  Linking the compiled Swift library with our Node.js addon
4.  Managing Swift runtime dependencies

This two-step compilation process ensures that Swift\'s advanced language features and runtime are properly handled while still allowing us to expose the functionality to JavaScript through Node.js\'s native addon system.

Let\'s start by adding a basic structure:

binding.gyp

``` 
,
        "actions": []
      }]
    ]
  }]
}
```

We include our Objective-C++ files (`sources`), specify the necessary macOS frameworks, and set up C++ exceptions and ARC. We also set various Xcode flags:

- `GCC_ENABLE_CPP_EXCEPTIONS`: Enables C++ exception handling in the native code.
- `CLANG_ENABLE_OBJC_ARC`: Enables Automatic Reference Counting for Objective-C memory management.
- `SWIFT_OBJC_BRIDGING_HEADER`: Specifies the header file that bridges Swift and Objective-C code.
- `SWIFT_VERSION`: Sets the Swift language version to 5.0.
- `SWIFT_OBJC_INTERFACE_HEADER_NAME`: Names the automatically generated header that exposes Swift code to Objective-C.
- `MACOSX_DEPLOYMENT_TARGET`: Sets the minimum macOS version (11.0/Big Sur) required.
- `OTHER_CFLAGS`: Additional compiler flags: `-ObjC++` specifies Objective-C++ mode. `-fobjc-arc` enables ARC at the compiler level.

Then, with `OTHER_LDFLAGS`, we set Linker flags:

- `-Wl,-rpath,@loader_path`: Sets runtime search path for libraries
- `-Wl,-install_name,@rpath/libSwiftCode.a`: Configures library install name
- `HEADER_SEARCH_PATHS`: Directories to search for header files during compilation.

You might also notice that we added a currently empty `actions` array to the JSON. In the next step, we\'ll be compiling Swift.

### Setting up the Swift Build Configuration[â€‹](#setting-up-the-swift-build-configuration "Direct link to Setting up the Swift Build Configuration") 

We\'ll add two actions: One to compile our Swift code (so that it can be linked) and another one to copy it to a folder to use. Replace the `actions` array above with the following JSON:

binding.gyp

``` 
,
    
  ]
  // ...other code
}
```

These actions:

- Compile the Swift code to a static library using `swiftc`
- Generate an Objective-C header from the Swift code
- Copy the compiled Swift library to the output directory
- Fix the library path with `install_name_tool` to ensure the dynamic linker can find the library at runtime by setting the correct install name

## 3) Creating the Objective-C Bridge Header[â€‹](#3-creating-the-objective-c-bridge-header "Direct link to 3) Creating the Objective-C Bridge Header") 

We\'ll need to setup a bridge between the Swift code and the native Node.js C++ addon. Let\'s start by creating a header file for the bridge in `include/SwiftBridge.h`:

include/SwiftBridge.h

``` 
#ifndef SwiftBridge_h
#define SwiftBridge_h

#import <Foundation/Foundation.h>

@interface SwiftBridge : NSObject
+ (NSString*)helloWorld:(NSString*)input;
+ (void)helloGui;

+ (void)setTodoAddedCallback:(void(^)(NSString* todoJson))callback;
+ (void)setTodoUpdatedCallback:(void(^)(NSString* todoJson))callback;
+ (void)setTodoDeletedCallback:(void(^)(NSString* todoId))callback;
@end

#endif
```

This header defines the Objective-C interface that we\'ll use to bridge between our Swift code and the Node.js addon. It includes:

- A simple `helloWorld` method that takes a string input and returns a string
- A `helloGui` method that will display a native SwiftUI interface
- Methods to set callbacks for todo operations (add, update, delete)

## 4) Implementing the Objective-C Bridge[â€‹](#4-implementing-the-objective-c-bridge "Direct link to 4) Implementing the Objective-C Bridge") 

Now, let\'s create the Objective-C bridge itself in `src/SwiftBridge.m`:

src/SwiftBridge.m

``` 
#import "SwiftBridge.h"
#import "swift_addon-Swift.h"
#import <Foundation/Foundation.h>

@implementation SwiftBridge

static void (^todoAddedCallback)(NSString*);
static void (^todoUpdatedCallback)(NSString*);
static void (^todoDeletedCallback)(NSString*);

+ (NSString*)helloWorld:(NSString*)input 

+ (void)helloGui 

+ (void)setTodoAddedCallback:(void(^)(NSString*))callback 

+ (void)setTodoUpdatedCallback:(void(^)(NSString*))callback 

+ (void)setTodoDeletedCallback:(void(^)(NSString*))callback 

@end
```

This bridge:

- Imports the Swift-generated header (`swift_addon-Swift.h`)
- Implements the methods defined in our header
- Simply forwards calls to the Swift code
- Stores the callbacks for later use in static variables, allowing them to persist throughout the application\'s lifecycle. This ensures that the JavaScript callbacks can be invoked at any time when todo items are added, updated, or deleted.

## 5) Implementing the Swift Code[â€‹](#5-implementing-the-swift-code "Direct link to 5) Implementing the Swift Code") 

Now, let\'s implement our Objective-C code in `src/SwiftCode.swift`. This is where we\'ll create our native macOS GUI using SwiftUI.

To make this tutorial easier to follow, we\'ll start with the basic structure and add features incrementally - step by step.

### Setting Up the Basic Structure[â€‹](#setting-up-the-basic-structure "Direct link to Setting Up the Basic Structure") 

Let\'s start with the basic structure. Here, we\'re just setting up variables, some basic callback methods, and a simple helper method we\'ll use later to convert data into formats ready for the JavaScript world.

src/SwiftCode.swift

``` 
import Foundation
import SwiftUI

@objc
public class SwiftCode: NSObject 

    @objc
    public static func setTodoAddedCallback(_ callback: @escaping (String) -> Void) 

    @objc
    public static func setTodoUpdatedCallback(_ callback: @escaping (String) -> Void) 

    @objc
    public static func setTodoDeletedCallback(_ callback: @escaping (String) -> Void) 

    private static func encodeToJson<T: Encodable>(_ item: T) -> String? 

        guard let jsonData = try? encoder.encode(item),
              let jsonString = String(data: jsonData, encoding: .utf8) else 
        return jsonString
    }

    // More code to follow...
}
```

This first part of our Swift code:

1.  Declares a class with the `@objc` attribute, making it accessible from Objective-C
2.  Implements the `helloWorld` method
3.  Adds callback setters for todo operations
4.  Includes a helper method to encode Swift objects to JSON strings

### Implementing `helloGui()`[â€‹](#implementing-hellogui "Direct link to implementing-hellogui") 

Let\'s continue with the `helloGui` method and the SwiftUI implementation. This is where we start adding user interface elements to the screen.

src/SwiftCode.swift

``` 
// Other code...

@objc
public class SwiftCode: NSObject 
            },
            onTodoUpdated: 
            },
            onTodoDeleted: 
        ))
        let window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 500, height: 500),
            styleMask: [.titled, .closable, .miniaturizable, .resizable],
            backing: .buffered,
            defer: false
        )

        window.title = "Todo List"
        window.contentView = contentView
        window.center()

        windowController = NSWindowController(window: window)
        windowController?.showWindow(nil)

        NSApp.activate(ignoringOtherApps: true)
    }
}
```

This helloGui method:

1.  Creates a SwiftUI view hosted in an `NSHostingView`. This is a crucial bridging component that allows SwiftUI views to be used in AppKit applications. The `NSHostingView` acts as a container that wraps our SwiftUI `ContentView` and handles the translation between SwiftUI\'s declarative UI system and AppKit\'s imperative UI system. This enables us to leverage SwiftUI\'s modern UI framework while still integrating with the traditional macOS window management system.
2.  Sets up callbacks to notify JavaScript when todo items change. We\'ll setup the actual callbacks later, for now we\'ll just call them if one is available.
3.  Creates and displays a native macOS window.
4.  Activates the app to bring the window to the front.

### Implementing the Todo Item[â€‹](#implementing-the-todo-item "Direct link to Implementing the Todo Item") 

Next, we\'ll define a `TodoItem` model with an ID, text, and date.

src/SwiftCode.swift

``` 
// Other code...

@objc
public class SwiftCode: NSObject 
    }
}
```

### Implementing the View[â€‹](#implementing-the-view "Direct link to Implementing the View") 

Next, we can implement the actual view. Swift is fairly verbose here, so the code below might look scary if you\'re new to Swift. The many lines of code obfuscate the simplicity in it - we\'re just setting up some UI elements. Nothing here is specific to Electron.

src/SwiftCode.swift

``` 
// Other code...

@objc
public class SwiftCode: NSObject 

        private func todoDatePicker(_ date: Binding<Date>) -> some View 

        var body: some View 
                    }) 
                }
                .padding(.horizontal, 12)
                .padding(.vertical, 8)

                List ) 
                                }) 
                            }
                            .padding(.vertical, 4)
                        } else ) 
                                .buttonStyle(BorderlessButtonStyle())
                                Button(action: )
                                    onTodoDeleted(todo.id)
                                }) 
                                .buttonStyle(BorderlessButtonStyle())
                            }
                            .padding(.vertical, 4)
                        }
                    }
                }
            }
        }
    }
}
```

This part of the code:

- Creates a SwiftUI view with a form to add new todos, featuring a text field for the todo description, a date picker for setting due dates, and an Add button that validates input, creates a new TodoItem, adds it to the local array, triggers the `onTodoAdded` callback to notify JavaScript, and then resets the input fields for the next entry.
- Implements a list to display todos with edit and delete capabilities
- Calls the appropriate callbacks when todos are added, updated, or deleted

The final file should look as follows:

src/SwiftCode.swift

``` 
import Foundation
import SwiftUI

@objc
public class SwiftCode: NSObject 

    @objc
    public static func setTodoAddedCallback(_ callback: @escaping (String) -> Void) 

    @objc
    public static func setTodoUpdatedCallback(_ callback: @escaping (String) -> Void) 

    @objc
    public static func setTodoDeletedCallback(_ callback: @escaping (String) -> Void) 

    private static func encodeToJson<T: Encodable>(_ item: T) -> String? 

        guard let jsonData = try? encoder.encode(item),
              let jsonString = String(data: jsonData, encoding: .utf8) else 
        return jsonString
    }

    @objc
    public static func helloGui() -> Void 
            },
            onTodoUpdated: 
            },
            onTodoDeleted: 
        ))
        let window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 500, height: 500),
            styleMask: [.titled, .closable, .miniaturizable, .resizable],
            backing: .buffered,
            defer: false
        )

        window.title = "Todo List"
        window.contentView = contentView
        window.center()

        windowController = NSWindowController(window: window)
        windowController?.showWindow(nil)

        NSApp.activate(ignoringOtherApps: true)
    }

    private struct TodoItem: Identifiable, Codable 
    }

    private struct ContentView: View 

        private func todoDatePicker(_ date: Binding<Date>) -> some View 

        var body: some View 
                    }) 
                }
                .padding(.horizontal, 12)
                .padding(.vertical, 8)

                List ) 
                                }) 
                            }
                            .padding(.vertical, 4)
                        } else ) 
                                .buttonStyle(BorderlessButtonStyle())
                                Button(action: )
                                    onTodoDeleted(todo.id)
                                }) 
                                .buttonStyle(BorderlessButtonStyle())
                            }
                            .padding(.vertical, 4)
                        }
                    }
                }
            }
        }
    }
}
```

## 6) Creating the Node.js Addon Bridge[â€‹](#6-creating-the-nodejs-addon-bridge "Direct link to 6) Creating the Node.js Addon Bridge") 

We now have working Objective-C code, which in turn is able to call working Swift code. To make sure it can be safely and properly called from the JavaScript world, we need to build a bridge between Objective-C and C++, which we can do with Objective-C++. We\'ll do that in `src/swift_addon.mm`.

src/swift_addon.mm

``` 
#import <Foundation/Foundation.h>
#import "SwiftBridge.h"
#include <napi.h>

class SwiftAddon : public Napi::ObjectWrap<SwiftAddon> );

        Napi::FunctionReference* constructor = new Napi::FunctionReference();
        *constructor = Napi::Persistent(func);
        env.SetInstanceData(constructor);

        exports.Set("SwiftAddon", func);
        return exports;
    }

    // More code to follow...
```

This first part:

1.  Defines a C++ class that inherits from `Napi::ObjectWrap`
2.  Creates a static `Init` method to register our class with Node.js
3.  Defines three methods: `helloWorld`, `helloGui`, and `on`

### Callback Mechanism[â€‹](#callback-mechanism "Direct link to Callback Mechanism") 

Next, let\'s implement the callback mechanism:

src/swift_addon.mm

``` 
// Previous code...

    struct CallbackData ;

    SwiftAddon(const Napi::CallbackInfo& info)
        : Napi::ObjectWrap<SwiftAddon>(info)
        , env_(info.Env())
        , emitter(Napi::Persistent(Napi::Object::New(info.Env())))
        , callbacks(Napi::Persistent(Napi::Object::New(info.Env())))
        , tsfn_(nullptr) 

                try );
                    }
                } catch (...) 

                delete callbackData;
            },
            &tsfn_
        );

        if (status != napi_ok) 
```

This part:

1.  Defines a struct to pass data between threads
2.  Sets up a constructor for our addon
3.  Creates a threadsafe function to handle callbacks from Swift

Let\'s continue with setting up the Swift callbacks:

src/swift_addon.mm

``` 
// Previous code...

        auto makeCallback = [this](const char* eventType) ;
                    napi_call_threadsafe_function(tsfn_, data, napi_tsfn_blocking);
                }
            };
        };

        [SwiftBridge setTodoAddedCallback:makeCallback("todoAdded")];
        [SwiftBridge setTodoUpdatedCallback:makeCallback("todoUpdated")];
        [SwiftBridge setTodoDeletedCallback:makeCallback("todoDeleted")];
    }

    ~SwiftAddon() 
    }
```

This part:

1.  Creates a helper function to generate Objective-C blocks that will be used as callbacks for Swift events. This lambda function `makeCallback` takes an event type string and returns an Objective-C block that captures the event type and payload. When Swift calls this block, it creates a CallbackData structure with the event information and passes it to the threadsafe function, which safely bridges between Swift\'s thread and Node.js\'s event loop.
2.  Sets up the carefully constructed callbacks for todo operations
3.  Implements a destructor to clean up resources

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

Finally, let\'s implement the instance methods:

src/swift_addon.mm

``` 
// Previous code...

private:
    Napi::Env env_;
    Napi::ObjectReference emitter;
    Napi::ObjectReference callbacks;
    napi_threadsafe_function tsfn_;

    Napi::Value HelloWorld(const Napi::CallbackInfo& info) 

        std::string input = info[0].As<Napi::String>();
        NSString* nsInput = [NSString stringWithUTF8String:input.c_str()];
        NSString* result = [SwiftBridge helloWorld:nsInput];

        return Napi::String::New(env, [result UTF8String]);
    }

    void HelloGui(const Napi::CallbackInfo& info) 

    Napi::Value On(const Napi::CallbackInfo& info) 

        callbacks.Value().Set(info[0].As<Napi::String>(), info[1].As<Napi::Function>());
        return env.Undefined();
    }
};

Napi::Object Init(Napi::Env env, Napi::Object exports) 

NODE_API_MODULE(swift_addon, Init)
```

This final part does multiple things:

1.  The code defines private member variables for the environment, event emitter, callback storage, and thread-safe function that are essential for the addon\'s operation.
2.  The HelloWorld method implementation takes a string input from JavaScript, passes it to the Swift code, and returns the processed result back to the JavaScript environment.
3.  The `HelloGui` method implementation provides a simple wrapper that calls the Swift UI creation function to display the native macOS window.
4.  The `On` method implementation allows JavaScript code to register callback functions that will be invoked when specific events occur in the native Swift code.
5.  The code sets up the module initialization process that registers the addon with Node.js and makes its functionality available to JavaScript.

The final and full `src/swift_addon.mm` should look like:

src/swift_addon.mm

``` 
#import <Foundation/Foundation.h>
#import "SwiftBridge.h"
#include <napi.h>

class SwiftAddon : public Napi::ObjectWrap<SwiftAddon> );

        Napi::FunctionReference* constructor = new Napi::FunctionReference();
        *constructor = Napi::Persistent(func);
        env.SetInstanceData(constructor);

        exports.Set("SwiftAddon", func);
        return exports;
    }

    struct CallbackData ;

    SwiftAddon(const Napi::CallbackInfo& info)
        : Napi::ObjectWrap<SwiftAddon>(info)
        , env_(info.Env())
        , emitter(Napi::Persistent(Napi::Object::New(info.Env())))
        , callbacks(Napi::Persistent(Napi::Object::New(info.Env())))
        , tsfn_(nullptr) 

                try );
                    }
                } catch (...) 

                delete callbackData;
            },
            &tsfn_
        );

        if (status != napi_ok) 

        auto makeCallback = [this](const char* eventType) ;
                    napi_call_threadsafe_function(tsfn_, data, napi_tsfn_blocking);
                }
            };
        };

        [SwiftBridge setTodoAddedCallback:makeCallback("todoAdded")];
        [SwiftBridge setTodoUpdatedCallback:makeCallback("todoUpdated")];
        [SwiftBridge setTodoDeletedCallback:makeCallback("todoDeleted")];
    }

    ~SwiftAddon() 
    }

private:
    Napi::Env env_;
    Napi::ObjectReference emitter;
    Napi::ObjectReference callbacks;
    napi_threadsafe_function tsfn_;

    Napi::Value HelloWorld(const Napi::CallbackInfo& info) 

        std::string input = info[0].As<Napi::String>();
        NSString* nsInput = [NSString stringWithUTF8String:input.c_str()];
        NSString* result = [SwiftBridge helloWorld:nsInput];

        return Napi::String::New(env, [result UTF8String]);
    }

    void HelloGui(const Napi::CallbackInfo& info) 

    Napi::Value On(const Napi::CallbackInfo& info) 

        callbacks.Value().Set(info[0].As<Napi::String>(), info[1].As<Napi::Function>());
        return env.Undefined();
    }
};

Napi::Object Init(Napi::Env env, Napi::Object exports) 

NODE_API_MODULE(swift_addon, Init)
```

## 6) Creating a JavaScript Wrapper[â€‹](#6-creating-a-javascript-wrapper "Direct link to 6) Creating a JavaScript Wrapper") 

You\'re so close! We now have working Objective-C, Swift, and thread-safe ways to expose methods and events to JavaScript. In this final step, let\'s create a JavaScript wrapper in `js/index.js` to provide a more friendly API:

js/index.js

``` 
const EventEmitter = require('node:events')

class SwiftAddon extends EventEmitter 

    const native = require('bindings')('swift_addon')
    this.addon = new native.SwiftAddon()

    this.addon.on('todoAdded', (payload) => )

    this.addon.on('todoUpdated', (payload) => )

    this.addon.on('todoDeleted', (payload) => )
  }

  helloWorld (input = '') 

  helloGui () 

  parse (payload) 
  }
}

if (process.platform === 'darwin')  else 
}
```

This wrapper:

1.  Extends EventEmitter to provide event support
2.  Checks if we\'re running on macOS
3.  Loads the native addon
4.  Sets up event listeners and forwards them
5.  Provides a clean API for our functions
6.  Parses JSON payloads and converts timestamps to JavaScript Date objects

## 7) Building and Testing the Addon[â€‹](#7-building-and-testing-the-addon "Direct link to 7) Building and Testing the Addon") 

With all files in place, you can build the addon:

``` 
npm run build
```

Please note that you *cannot* call this script from Node.js directly, since Node.js doesn\'t set up an \"app\" in the eyes of macOS. Electron does though, so you can test your code by requiring and calling it from Electron.

## Conclusion[â€‹](#conclusion "Direct link to Conclusion") 

You\'ve now built a complete native Node.js addon for macOS using Swift and SwiftUI. This provides a foundation for building more complex macOS-specific features in your Electron apps, giving you the best of both worlds: the ease of web technologies with the power of native macOS code.

The approach demonstrated here allows you to:

- Setting up a project structure that bridges Swift, Objective-C, and JavaScript
- Implementing Swift code with SwiftUI for native UI
- Creating an Objective-C bridge to connect Swift with Node.js
- Setting up bidirectional communication using callbacks and events
- Configuring a custom build process to compile Swift code

For more information on developing with Swift and Swift, refer to Apple\'s developer documentation:

- [Swift Programming Language](https://developer.apple.com/swift/)
- [SwiftUI Framework](https://developer.apple.com/documentation/swiftui)
- [macOS Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/macos)
- [Swift and Objective-C Interoperability Guide](https://developer.apple.com/documentation/swift/importing-swift-into-objective-c)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/native-code-and-electron-swift-macos.md)