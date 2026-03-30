# Source: https://developer.apple.com/documentation/spritekit/skview

Title: SKView | Apple Developer Documentation

URL Source: https://developer.apple.com/documentation/spritekit/skview

Markdown Content:
[Mentioned in](https://developer.apple.com/documentation/spritekit/skview#mentions)
-----------------------------------------------------------------------------------

[Choosing a SpriteKit Scene Renderer](https://developer.apple.com/documentation/spritekit/choosing-a-spritekit-scene-renderer)

[Creating a New Node By Rendering To a Texture](https://developer.apple.com/documentation/spritekit/creating-a-new-node-by-rendering-to-a-texture)

[Overview](https://developer.apple.com/documentation/spritekit/skview#overview)
-------------------------------------------------------------------------------

You present a scene by calling the view’s [`presentScene(_:)`](https://developer.apple.com/documentation/spritekit/skview/presentscene(_:)) method. When a scene is presented by the view, it alternates between running its simulation (which animates the content) and rendering the content for display. You can pause the scene by setting the view’s [`isPaused`](https://developer.apple.com/documentation/spritekit/skview/ispaused) property to [`true`](https://developer.apple.com/documentation/Swift/true).

[Topics](https://developer.apple.com/documentation/spritekit/skview#topics)
---------------------------------------------------------------------------

### [Displaying a Scene](https://developer.apple.com/documentation/spritekit/skview#Displaying-a-Scene)

Present a scene to display content on the screen.

[`var scene: SKScene?`](https://developer.apple.com/documentation/spritekit/skview/scene)

The scene currently presented by this view.

[`func presentScene(SKScene?)`](https://developer.apple.com/documentation/spritekit/skview/presentscene(_:))

Presents a scene.

[`func presentScene(SKScene, transition: SKTransition)`](https://developer.apple.com/documentation/spritekit/skview/presentscene(_:transition:))

Transitions from the current scene to a new scene.

[`class SKTransition`](https://developer.apple.com/documentation/spritekit/sktransition)

An object used to perform an animated transition to a new scene.

### [Controlling the Timing of a Scene’s Rendering](https://developer.apple.com/documentation/spritekit/skview#Controlling-the-Timing-of-a-Scenes-Rendering)

Control the timing of the view’s screen updates.

[`var isPaused: Bool`](https://developer.apple.com/documentation/spritekit/skview/ispaused)

A Boolean value that indicates whether the view’s scene animations are paused.

[`var preferredFramesPerSecond: Int`](https://developer.apple.com/documentation/spritekit/skview/preferredframespersecond)

The animation frame rate that the view uses to render its scene.

[`var delegate: (any SKViewDelegate)?`](https://developer.apple.com/documentation/spritekit/skview/delegate)

A delegate that allows dynamic control of the view’s render rate.

[`protocol SKViewDelegate`](https://developer.apple.com/documentation/spritekit/skviewdelegate)

Methods to take custom control over the view’s render rate.

[`var frameInterval: Int`](https://developer.apple.com/documentation/spritekit/skview/frameinterval)

The number of frames that must pass before the scene is called to update its contents.

Deprecated

[`var preferredFrameRate: Float`](https://developer.apple.com/documentation/spritekit/skview/preferredframerate)
Deprecated

### [Configuring Performance Related Toggles](https://developer.apple.com/documentation/spritekit/skview#Configuring-Performance-Related-Toggles)

Control hints that have performance implications which are unique to your app.

[`var ignoresSiblingOrder: Bool`](https://developer.apple.com/documentation/spritekit/skview/ignoressiblingorder)

A Boolean value that indicates whether parent-child and sibling relationships affect the rendering order of nodes in the scene.

[`var shouldCullNonVisibleNodes: Bool`](https://developer.apple.com/documentation/spritekit/skview/shouldcullnonvisiblenodes)

A Boolean value that indicates whether the view automatically culls non-visible nodes from the rendering tree.

[`var allowsTransparency: Bool`](https://developer.apple.com/documentation/spritekit/skview/allowstransparency)

A Boolean property that indicates whether the view is rendered using transparency.

[`var isAsynchronous: Bool`](https://developer.apple.com/documentation/spritekit/skview/isasynchronous)

A Boolean value that indicates whether the content is rendered asynchronously.

### [Enabling Visual Statistics for Debugging](https://developer.apple.com/documentation/spritekit/skview#Enabling-Visual-Statistics-for-Debugging)

Display metrics in the bottom corner of the view for debugging purposes.

[`var showsFPS: Bool`](https://developer.apple.com/documentation/spritekit/skview/showsfps)

A Boolean value that indicates whether the view displays a frame rate indicator.

[`var showsNodeCount: Bool`](https://developer.apple.com/documentation/spritekit/skview/showsnodecount)

A Boolean value that indicates whether the view displays an overlay that shows physics bodies that are visible in the scene.

[`var showsDrawCount: Bool`](https://developer.apple.com/documentation/spritekit/skview/showsdrawcount)

A Boolean value that indicates whether the view displays the number of drawing passes it needed to render the view.

[`var showsQuadCount: Bool`](https://developer.apple.com/documentation/spritekit/skview/showsquadcount)

A Boolean value that indicates whether the view displays the number of rectangles used to render the scene.

[`var showsPhysics: Bool`](https://developer.apple.com/documentation/spritekit/skview/showsphysics)

A Boolean value that indicates whether the view displays physics-related debugging information.

[`var showsFields: Bool`](https://developer.apple.com/documentation/spritekit/skview/showsfields)

A Boolean value that indicates whether the view displays information about physics fields in the scene.

### [Converting Between View and Scene Coordinates](https://developer.apple.com/documentation/spritekit/skview#Converting-Between-View-and-Scene-Coordinates)

Convert to or from scene and view coordinates which is a common task for touch or mouse input.

[`func convert(CGPoint, from: SKScene) -> CGPoint`](https://developer.apple.com/documentation/spritekit/skview/convert(_:from:))

Converts a point from scene coordinates to view coordinates.

[`func convert(CGPoint, to: SKScene) -> CGPoint`](https://developer.apple.com/documentation/spritekit/skview/convert(_:to:))

Converts a point from view coordinates to scene coordinates.

### [Snapshotting Nodes to a Texture](https://developer.apple.com/documentation/spritekit/skview#Snapshotting-Nodes-to-a-Texture)

Create a texture that is a flattened or cropped portion of the node heirarchy.

[`func texture(from: SKNode, crop: CGRect) -> SKTexture?`](https://developer.apple.com/documentation/spritekit/skview/texture(from:crop:))

Renders a portion of a node’s contents and returns the rendered image as a texture.

[`func texture(from: SKNode) -> SKTexture?`](https://developer.apple.com/documentation/spritekit/skview/texture(from:))

Renders the contents of a node tree and returns the rendered image as a texture.

[Creating a New Node By Rendering To a Texture](https://developer.apple.com/documentation/spritekit/creating-a-new-node-by-rendering-to-a-texture)

Render a portion of the node tree into a new texture.

### [Switching Renderers](https://developer.apple.com/documentation/spritekit/skview#Switching-Renderers)

[Requesting the Open GL Renderer](https://developer.apple.com/documentation/spritekit/requesting-the-opengl-renderer)

Switch to the legacy renderer temporarily for debugging purposes.

### [Instance Properties](https://developer.apple.com/documentation/spritekit/skview#Instance-Properties)

[`var disableDepthStencilBuffer: Bool`](https://developer.apple.com/documentation/spritekit/skview/disabledepthstencilbuffer)

[Relationships](https://developer.apple.com/documentation/spritekit/skview#relationships)
-----------------------------------------------------------------------------------------

### [Inherits From](https://developer.apple.com/documentation/spritekit/skview#inherits-from)

*   [`NSView`](https://developer.apple.com/documentation/AppKit/NSView)
*   [`UIView`](https://developer.apple.com/documentation/UIKit/UIView)

### [Conforms To](https://developer.apple.com/documentation/spritekit/skview#conforms-to)

*   [`CALayerDelegate`](https://developer.apple.com/documentation/QuartzCore/CALayerDelegate)
*   [`CVarArg`](https://developer.apple.com/documentation/Swift/CVarArg)
*   [`CustomDebugStringConvertible`](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
*   [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
*   [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable)
*   [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable)
*   [`NSAccessibilityElementProtocol`](https://developer.apple.com/documentation/AppKit/NSAccessibilityElementProtocol)
*   [`NSAccessibilityProtocol`](https://developer.apple.com/documentation/AppKit/NSAccessibilityProtocol)
*   [`NSAnimatablePropertyContainer`](https://developer.apple.com/documentation/AppKit/NSAnimatablePropertyContainer)
*   [`NSAppearanceCustomization`](https://developer.apple.com/documentation/AppKit/NSAppearanceCustomization)
*   [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding)
*   [`NSDraggingDestination`](https://developer.apple.com/documentation/AppKit/NSDraggingDestination)
*   [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
*   [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding)
*   [`NSStandardKeyBindingResponding`](https://developer.apple.com/documentation/AppKit/NSStandardKeyBindingResponding)
*   [`NSTouchBarProvider`](https://developer.apple.com/documentation/AppKit/NSTouchBarProvider)
*   [`NSUserActivityRestoring`](https://developer.apple.com/documentation/AppKit/NSUserActivityRestoring)
*   [`NSUserInterfaceItemIdentification`](https://developer.apple.com/documentation/AppKit/NSUserInterfaceItemIdentification)
*   [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable)
*   [`SendableMetatype`](https://developer.apple.com/documentation/Swift/SendableMetatype)
*   [`UIAccessibilityIdentification`](https://developer.apple.com/documentation/UIKit/UIAccessibilityIdentification)
*   [`UIActivityItemsConfigurationProviding`](https://developer.apple.com/documentation/UIKit/UIActivityItemsConfigurationProviding)
*   [`UIAppearance`](https://developer.apple.com/documentation/UIKit/UIAppearance)
*   [`UIAppearanceContainer`](https://developer.apple.com/documentation/UIKit/UIAppearanceContainer)
*   [`UICoordinateSpace`](https://developer.apple.com/documentation/UIKit/UICoordinateSpace)
*   [`UIDynamicItem`](https://developer.apple.com/documentation/UIKit/UIDynamicItem)
*   [`UIFocusEnvironment`](https://developer.apple.com/documentation/UIKit/UIFocusEnvironment)
*   [`UIFocusItem`](https://developer.apple.com/documentation/UIKit/UIFocusItem)
*   [`UIFocusItemContainer`](https://developer.apple.com/documentation/UIKit/UIFocusItemContainer)
*   [`UILargeContentViewerItem`](https://developer.apple.com/documentation/UIKit/UILargeContentViewerItem)
*   [`UIPasteConfigurationSupporting`](https://developer.apple.com/documentation/UIKit/UIPasteConfigurationSupporting)
*   [`UIPopoverPresentationControllerSourceItem`](https://developer.apple.com/documentation/UIKit/UIPopoverPresentationControllerSourceItem)
*   [`UIResponderStandardEditActions`](https://developer.apple.com/documentation/UIKit/UIResponderStandardEditActions)
*   [`UITraitChangeObservable`](https://developer.apple.com/documentation/UIKit/UITraitChangeObservable-67e94)
*   [`UITraitEnvironment`](https://developer.apple.com/documentation/UIKit/UITraitEnvironment)
*   [`UIUserActivityRestoring`](https://developer.apple.com/documentation/UIKit/UIUserActivityRestoring)

[See Also](https://developer.apple.com/documentation/spritekit/skview#see-also)
-------------------------------------------------------------------------------

### [Scene Renderers](https://developer.apple.com/documentation/spritekit/skview#Scene-Renderers)

[Choosing a Sprite Kit Scene Renderer](https://developer.apple.com/documentation/spritekit/choosing-a-spritekit-scene-renderer)

Compare the different ways to display a SpriteKit scene.

[`class SKRenderer`](https://developer.apple.com/documentation/spritekit/skrenderer)

An object that renders a scene into a custom Metal rendering pipeline and drives the scene update cycle.

[`class WKInterfaceSKScene`](https://developer.apple.com/documentation/WatchKit/WKInterfaceSKScene)

A visual WatchKit element that displays a SpriteKit scene.
