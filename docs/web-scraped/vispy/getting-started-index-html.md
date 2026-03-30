# Source: https://vispy.org/getting_started/index.html

Title: Getting Started — VisPy

URL Source: https://vispy.org/getting_started/index.html

Markdown Content:
VisPy strives to provide an easy path for users to make fast interactive visualizations. To serve as many users as possible VisPy provides different interfaces for differing levels of experience. While one interface may be enough to build a simple visualization, knowing all the interfaces can provide the most flexibility for fully customizing your visualization.

The below pages are meant to provide an introduction to these interfaces and help guide you into what interface might be best for your experience and the final visualization you are looking to achieve. Additionally, the [Gallery](https://vispy.org/gallery/index.html) can be used for inspiration. Further low-level details can be found in the [API documentation](https://vispy.org/api/modules.html) and existing examples.

VisPy targets two primary categories of users:

1.   **Users knowing OpenGL**, or willing to learn OpenGL, who want to create beautiful and fast interactive 2D/3D visualizations in Python as easily as possible. Users in this category can write their own visualizations with [`vispy.gloo`](https://vispy.org/api/vispy.gloo.html#module-vispy.gloo "vispy.gloo") (requires knowing OpenGL/GLSL). Another option with VisPy development is to encapsulate gloo-based visualizations into re-usable Visual classes. The below pages will provide an introduction of these interfaces.

*   [Modern OpenGL](https://vispy.org/getting_started/modern-gl.html)
*   [Gloo](https://vispy.org/getting_started/gloo.html)
*   [Visuals](https://vispy.org/getting_started/visuals.html)

1.   **Scientists without any knowledge of OpenGL**, who are seeking a high-level, high-performance plotting toolkit. Use the [`vispy.plot`](https://vispy.org/api/vispy.plot.html#module-vispy.plot "vispy.plot") and [`vispy.scene`](https://vispy.org/api/vispy.scene.html#module-vispy.scene "vispy.scene") interfaces for high-level work. The below pages provide an introduction into these interfaces.

*   [Scene](https://vispy.org/getting_started/scene.html)
*   [Plotting](https://vispy.org/getting_started/plot.html)
