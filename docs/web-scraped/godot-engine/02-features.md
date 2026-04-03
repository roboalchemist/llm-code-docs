# Source: https://docs.godotengine.org/en/stable/about/list_of_features.html

## Godot Engine - Complete Feature List

### Core Engine Features

#### Platforms

Godot supports exporting to:

- **Desktop**: Windows, macOS, Linux
- **Mobile**: iOS (via iOS SDK), Android (via Android SDK)
- **Web**: HTML5/WebGL via Emscripten
- **Consoles**: Nintendo Switch, PlayStation, Xbox (with platform-specific setup)
- **VR/XR**: OpenXR-compatible platforms

#### Architecture

- Scene and node-based architecture
- Extremely lightweight core
- Modular design allows customization
- Plugin system for extensions
- GDExtension for C++ modules
- Multi-threaded rendering

#### Scripting Languages

- **GDScript**: Built-in dynamically-typed language optimized for games
- **C#**: Full .NET/Mono support
- **C++**: Via GDExtension for performance-critical code
- **VisualScript**: Node-based visual programming (legacy)
- Hot-reload during development

#### Editor

- Fully integrated development environment
- Visual scene and node editor
- Integrated code editor with syntax highlighting
- Animation editor with timeline
- Particle effect editor
- Shader editor
- Tilemap editor
- Debugger with breakpoints and watches
- Profiler for performance analysis
- Dockable panels and customizable layout
- Community-driven plugin system

#### Asset Pipeline

- Import system for various formats
- Built-in texture compression
- Model import with automatic processing
- Audio import and streaming
- Font importing and rendering
- Automatic asset caching
- Re-import on source file changes

### 2D Graphics

#### 2D Rendering

- Sprite rendering with modulation
- Texture atlasing support
- Particle system for effects
- Canvas layers for depth organization
- Dynamic lighting and shadows
- Parallax scrolling
- Normal mapping support
- Animation blend trees
- Skeletal animation for 2D

#### 2D Graphics Tools

- Sprite editor with slicing
- Tile set and tilemap editor
- Particle effect editor
- Animation player with timeline
- Frame-by-frame animation support

#### 2D Geometry

- Polygon2D for custom shapes
- Line2D for paths and trails
- Shape casting (circle, rectangle, line)
- Collision shape definitions

### 3D Graphics

#### 3D Rendering

- OpenGL ES 3.0 and Vulkan support
- Real-time shadows (including soft shadows)
- Dynamic global illumination with GIProbes
- Light baking with LightmapProbes
- Environment mapping and reflections
- Post-processing effects
- Deferred and forward rendering
- High Dynamic Range (HDR) rendering
- Tone mapping

#### 3D Graphics Features

- Normal, parallax, and detail mapping
- Ambient occlusion
- Subsurface scattering
- Anisotropic filtering
- Triplanar mapping
- Object and screen-space shaders
- Multi-sample antialiasing (MSAA)
- Temporal antialiasing (TAA)
- Depth of field
- Motion blur

#### 3D Tools

- Model importer for FBX, glTF, OBJ
- Mesh instancing
- LOD (Level of Detail) support
- Decals for surface details
- Volumetric fog
- Particle effects for 3D

#### 3D Scene Components

- Multiple light types (directional, point, spot)
- Reflection probes
- Occluders for visibility culling
- Viewport rendering to texture
- Lightmap baking
- Environmental lighting

### Physics

#### 2D Physics

- Rigid bodies with linear and angular velocity
- Kinematic bodies for character controllers
- Static bodies for immovable objects
- Multiple collision shapes (circle, rectangle, polygon, capsule)
- Physics materials with friction and bounce
- Joints and constraints (pin, groove, spring)
- Area detection zones
- Raycasting and shape queries
- Continuous collision detection
- Physics-based damping and gravity

#### 3D Physics

- Full 3D rigid body physics
- Kinematic bodies for player characters
- Particles physics (optional GPU simulation)
- Convex and concave mesh colliders
- Trimesh collision shapes
- Physics joints (fixed, ball, hinge, groove, 6DOF)
- Constraints and motors
- Area triggers
- Raycasting with multiple results
- CCD (Continuous Collision Detection)
- Simulated gravity and air resistance

#### Physics Engines

- **Built-in Physics Engine**: Default Godot physics system
- **Bullet Physics**: Alternative 3D physics option
- Selectable per-project

### Audio

#### Audio Playback

- Multi-channel audio output
- Spatial audio for 3D positioning
- Audio streaming from files
- Audio bus system for mixing
- Real-time audio processing
- Audio effects and filters
- Volume and pitch control
- Audio ducking

#### Audio Effects

- Reverb (room, hall, cathedral presets)
- Delay and echo effects
- Chorus and flanger effects
- Distortion
- Equalizer
- Compressor
- Limiter
- Stereo panning
- Doppler effect for moving sources

#### Audio Formats Supported

- WAV (uncompressed and compressed)
- OGG Vorbis (streaming)
- MP3 (with patent concerns)
- MIDI files (playback)
- Custom audio plugins

### Input System

#### Input Devices

- Keyboard input
- Mouse input and cursor control
- Gamepad/joystick support
- Touch input for mobile
- Multitouch gestures
- Accelerometer (mobile)
- Gyroscope (mobile)
- Camera input
- Haptic feedback/vibration

#### Input Features

- Customizable input maps
- Input action system for game controls
- Gesture recognition
- Event queue system
- Keyboard focus management
- Virtual keyboard support

### Scripting Features

#### GDScript

- Python-like syntax
- Dynamically-typed
- First-class functions
- Lambdas and closures
- Type hints for optimization
- Annotations and metadata
- Hot-reload support
- Coroutines and yielding
- Signal system for events
- Built-in documentation strings

#### C #

- Full .NET language support
- Access to .NET libraries
- Visual Studio integration
- Static typing
- LINQ support
- Async/await
- Multiple inheritance patterns
- Full Godot API access

### Networking

#### Network Features

- Low-level TCP/UDP networking
- High-level multiplayer system
- Peer-to-peer (P2P) architecture
- Client/server architecture
- Remote Procedure Calls (RPC)
- Network state synchronization
- Lag compensation
- Network testing in editor

#### Protocol Support

- Custom protocol via raw sockets
- WebSocket support for web games
- SSL/TLS encryption
- UPNP port mapping
- NAT punchthrough (basic)

### UI/GUI System

#### UI Controls

- Buttons with various states
- Text input (single and multi-line)
- Labels and rich text
- Checkboxes and radio buttons
- Sliders and spin boxes
- Dropdown/option menus
- Tabs and tabbed interfaces
- Tree view (hierarchical lists)
- Item lists
- Progress bars
- Color pickers
- File dialogs
- Directory dialogs
- Popup menus
- Tooltips
- Modal dialogs

#### UI Layout

- Container-based layout system
- Anchors for responsive positioning
- Margins for sizing
- Size flags for flexible sizing
- HBox, VBox for linear layouts
- Grid containers
- Center containers
- Tab containers
- Aspect ratio containers
- Dynamic layout recalculation

#### Theming

- Theme system for consistent styling
- Custom font support
- Customizable control appearance
- Style inheritance
- Runtime theme switching
- Per-control style overrides

### Animation

#### Animation System

- Timeline-based animation editor
- Keyframe animation
- Tweening/easing functions
- Multiple animation tracks
- Animation blending
- Animation states and transitions
- Root motion animation
- Skeletal animation
- Vertex animation

#### Animation Tools

- Visual timeline editor
- Keyframe management
- Bezier curve editing for easing
- Animation preview in editor
- Real-time animation playback
- Pose library (animation presets)

### File Formats

#### Import Support

- **3D Models**: FBX, glTF 2.0, OBJ, Collada (DAE), Blend (Blender)
- **Images**: PNG, JPG, WebP, TGA, BMP, EXR (HDR)
- **Audio**: WAV, OGG Vorbis, MP3
- **Fonts**: TrueType (TTF), OpenType (OTF)
- **Text**: JSON, YAML, CSV, XML
- **Vector**: SVG (basic support)

#### Godot Native Formats

- .tscn: Text-based scene format
- .tres: Resource format
- .gdshader: Shader files
- .gd: GDScript source files
- .cs: C# source files

### Miscellaneous Features

#### Performance

- Multi-threaded rendering
- Spatial hashing for fast queries
- Frustum culling for hidden object skipping
- Occlusion culling
- LOD (Level of Detail) support
- Instancing for batch rendering
- Profiling tools (frame time, memory, etc.)
- Performance monitoring

#### Debugging

- Built-in debugger
- Breakpoints and watch variables
- Stack trace inspection
- Memory profiler
- Frame profiler
- Network debugging
- Remote debugging (over network)
- Print debugging support
- Error messages with file/line information

#### Compatibility

- 32-bit and 64-bit builds
- GLES 2 and GLES 3 rendering backends
- Vulkan support (newer platforms)
- DirectX 12 (via Angle layer on Windows)
- Metal support on macOS/iOS
- OpenGL ES 2/3 on mobile

#### Extensibility

- Plugin system in editor
- GDExtension for C++ modules
- Custom importers
- Custom exporters
- Scene template system
- Autoload scripts (singletons)
- Custom nodes from scripts
- Node inheritance and composition

#### Internationalization

- Multi-language support
- Translation system with Gettext compatibility
- Right-to-left (RTL) language support
- Unicode support
- Font fallback for missing characters
- Text direction handling

#### Development Tools

- Version control friendly (text-based formats)
- Command-line export
- Build automation support
- Headless rendering for automation
- Editor scripting (EditorScript)
- Build customization hooks
- Custom build tools

---

Godot continues to evolve with regular updates adding new features and improvements. Check the official blog at https://godotengine.org/blog for the latest developments.
