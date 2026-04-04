# Source: https://libgdx.com/features/

Title: Features

URL Source: https://libgdx.com/features/

Markdown Content:
![Image 1](https://libgdx.com/assets/images/features/crossplatform.jpeg)

Cross-Platform
--------------

libGDX offers a single API to target: **Windows, Linux (including the Raspberry Pi), macOS, Android, iOS and Web**. Developers can use various backends to access the capabilities of the host platform, **without having to write platform-specific code**. Rendering is handled on all platforms through Open GL ES 2.0/3.0.

![Image 2](https://libgdx.com/assets/images/features/reliable.png)

Well proven
-----------

The libGDX project was started [over 10 years ago](https://libgdx.com/history/). Over the years, libGDX and its community matured: nowadays, libGDX is a **[well proven](https://libgdx.com/showcase/) and reliable framework** with a sound base and documentation. Furthermore, there are plenty of games built on top of libGDX, many of which are open source.

[See some projects](https://libgdx.com/showcase/)

![Image 3](https://libgdx.com/assets/images/features/ecosystem.png)

Extensive third-party ecosystem
-------------------------------

libGDX offers a very extensive third-party ecosystem. There are numerous [tools](https://libgdx.com/dev/tools/) and libraries that take a lot of work off the hands of developers. [Awesome-libGDX](https://github.com/rafaskb/awesome-libgdx#readme) is a curated list of libGDX-centered **libraries** and a good starting point for anyone new in the libGDX world.

[Check out Awesome-libGDX](https://github.com/rafaskb/awesome-libgdx)

Do whatever you want
--------------------

_Unlike many popular editor-based platforms, libGDX is entirely code-centric, offering developers fine-grained control over every aspect of their game._

*   **Freedom:** While libGDX gives you access to various different tools and abstractions, you can still access the underlying base. libGDX acknowledges that there is no one-size-fits-all solution, so it doesn’t force you to use certain tools or coding styles: you are free to do whatever you want!
*   **Open Source:** libGDX is licensed under Apache 2.0 and maintained by the community, so you can take a look [under the hood](https://github.com/libgdx/libgdx) and see how everything works.
*   **Java:** Since libGDX uses Java, you can profit from the wide Java ecosystem – Powerful IDEs, out-of-the-box support for Git, fined-tuned debuggers, performance profilers, and an abundance of well-tried libraries and frameworks, as well as many resources and extensive documentation.

Feature Packed
--------------

_libGDX comes with batteries included. Write 2D or 3D games and let libGDX worry about low-level details._

Audio
-----

*   [Streaming music](https://libgdx.com/wiki/audio/streaming-music) and [sound effect playback](https://libgdx.com/wiki/audio/sound-effects) for WAV, MP3 and OGG 
*   Direct access to audio device for [PCM sample playback](https://libgdx.com/wiki/audio/playing-pcm-audio) and [recording](https://libgdx.com/wiki/audio/recording-pcm-audio)

Input Handling
--------------

*   Abstractions for [mouse, keyboard, touchscreen](https://libgdx.com/wiki/input/mouse-touch-and-keyboard), [controllers](https://github.com/libgdx/gdx-controllers), [accelerometer](https://libgdx.com/wiki/input/accelerometer), [gyroscope](https://libgdx.com/wiki/input/gyroscope) and [compass](https://libgdx.com/wiki/input/compass)
*   [Gesture detection](https://libgdx.com/wiki/input/gesture-detection) (recognising taps, panning, flinging and pinch zooming) 

Math & Physics
--------------

*   [Matrix, vector and quaternion](https://libgdx.com/wiki/math-utils/vectors-matrices-quaternions) classes; accelerated via native C code where possible (if you are interested in that, also note our [gdx-jnigen](https://libgdx.com/wiki/utils/jnigen) project) 
*   [Bounding shapes and volumes as well as a Frustum class for picking and culling](https://libgdx.com/wiki/math-utils/circles-planes-rays-etc)
*   [Intersection and overlap testing](https://javadoc.io/doc/com.badlogicgames.gdx/gdx/latest/com/badlogic/gdx/math/Intersector.html)
*   [Steering Behaviours, Formation Motion, Pathfinding, Behaviour Trees and Finite State Machines](https://github.com/libgdx/gdx-ai)
*   Common [interpolators](https://libgdx.com/wiki/math-utils/interpolation), different [spline implementations](https://libgdx.com/wiki/math-utils/path-interface-and-splines), concave polygon triangulators and more 
*   2D physics: JNI wrapper for the popular [Box2D physics](https://libgdx.com/wiki/extensions/physics/box2d) (see also [Box2DLights](https://github.com/libgdx/box2dlights)). Alternatively, you can take a look at [jbump](https://github.com/implicit-invocation/jbump) for a simpler physics implementation. 
*   3D physics: JNI Wrapper for [Bullet physics](https://libgdx.com/wiki/extensions/physics/bullet/bullet-physics)

Integration of Services
-----------------------

*   Easy integration of [game services](https://github.com/MrStahlfelge/gdx-gamesvcs), such as Google Play Games, Apple Game Center, and more. 
*   Cross-platform API for [in-app purchases](https://github.com/libgdx/gdx-pay). 
*   Third-party support for Google’s [Firebase](https://github.com/mk-5/gdx-fireapp), the [Steamworks API](https://github.com/code-disaster/steamworks4j), [gameanalytics.com](https://github.com/MrStahlfelge/gdx-gameanalytics) and Facebook’s [Graph API](https://github.com/TomGrill/gdx-facebook). 
*   Easy integration of [AdMob](https://libgdx.com/wiki/third-party/admob-in-libgdx)

File I/O & Storage
------------------

*   [File system abstraction](https://libgdx.com/wiki/file-handling) for all platforms 
*   Straight-forward [asset management](https://libgdx.com/wiki/managing-your-assets)
*   [Preferences](https://libgdx.com/wiki/preferences) for lightweight settings storage 
*   [JSON](https://libgdx.com/wiki/utils/reading-and-writing-json) and [XML](https://libgdx.com/wiki/utils/reading-and-writing-xml) serialisation 
*   Custom, [optimised collections](https://libgdx.com/wiki/utils/collections), with primitive support 

Graphics
--------

*   Rendering through [OpenGL ES 2.0/3.0](https://libgdx.com/wiki/graphics/opengl-es-support) on all platforms 
*   **Low-Level OpenGL helpers:**
    *   Vertex arrays and vertex buffer objects 
    *   [Meshes](https://libgdx.com/wiki/graphics/opengl-utils/meshes)
    *   [Textures](https://libgdx.com/wiki/graphics/2d/spritebatch-textureregions-and-sprites)
    *   [Framebuffer objects](https://libgdx.com/wiki/graphics/opengl-utils/frame-buffer-objects)
    *   [Shaders](https://libgdx.com/wiki/graphics/opengl-utils/shaders), integrating easily with meshes 
    *   [Immediate mode rendering](https://javadoc.io/doc/com.badlogicgames.gdx/gdx/latest/com/badlogic/gdx/graphics/glutils/ImmediateModeRenderer.html) emulation 
    *   Simple [shape rendering](https://libgdx.com/wiki/graphics/opengl-utils/rendering-shapes)
    *   Automatic software or hardware mipmap generation 
    *   Automatic handling of OpenGL ES context loss 

*   **High-level 2D APIs:**
    *   [Orthographic camera](https://libgdx.com/wiki/graphics/2d/orthographic-camera)
    *   High-performance [sprite](https://libgdx.com/wiki/graphics/2d/spritebatch-textureregions-and-sprites) batching and caching 
    *   [Texture atlases](https://libgdx.com/wiki/graphics/2d/using-textureatlases), with whitespace stripping support. Either generated [offline](https://libgdx.com/wiki/graphics/2d/packing-atlases-offline) or [at runtime](https://libgdx.com/wiki/graphics/2d/packing-atlases-at-runtime)
    *   [Bitmap fonts](https://libgdx.com/wiki/graphics/2d/fonts/bitmap-fonts). Either generated offline or [loaded from TTF files](https://libgdx.com/wiki/extensions/gdx-freetype)
    *   [2D Particle system](https://libgdx.com/wiki/graphics/2d/2d-particleeffects)
    *   [TMX tile map support](https://libgdx.com/wiki/graphics/2d/tile-maps)
    *   [2D scene-graph API](https://libgdx.com/wiki/graphics/2d/scene2d/scene2d)

*   **A Powerful UI Solution:**
    *   [2D UI library](https://libgdx.com/wiki/graphics/2d/scene2d/scene2d-ui), based on scene-graph API 
    *   A plethora of [official](https://libgdx.com/wiki/graphics/2d/scene2d/scene2d-ui#widgets) and third-party widgets 
    *   Fully [skinnable](https://libgdx.com/wiki/graphics/2d/scene2d/skin); [Composer](https://github.com/raeleus/skin-composer) for creating UI skins 

*   **High-Level 3D APIs:**
    *   Decal batching, for 3D billboards or [particle systems](https://libgdx.com/wiki/graphics/3d/3d-particle-effects)
    *   Basic loaders for Wavefront OBJ and MD5 
    *   [3D rendering API](https://libgdx.com/wiki/graphics/3d/3d-graphics) with materials, animation and lighting system and support for loading FBX models via fbx-conv 
    *   Third-party support for [GLTF 2.0](https://github.com/mgsx-dev/gdx-gltf)
    *   Rudimentary [VR support](https://libgdx.com/wiki/graphics/3d/virtual-reality)

*   Third-party [post-processing](https://github.com/crashinvaders/gdx-vfx) shader effects 

Networking
----------

*   [Gdx.net](https://libgdx.com/wiki/networking) for simple networking (TCP sockets and HTTP requests) 
*   Cross-platform [WebSocket support](https://github.com/MrStahlfelge/gdx-websockets)
*   Common Java networking solutions: [KryoNet](https://github.com/EsotericSoftware/kryonet)&[Netty](https://github.com/netty/netty) (not supported on Web) 

And…
----

**…a Great Community!** Get support from a very friendly [community](https://libgdx.com/community/) of game and application developers or use any of the libraries and tools created by members of our community. Join us today and get started with your very first libGDX game!

[Get Started!](https://libgdx.com/dev/setup/)
