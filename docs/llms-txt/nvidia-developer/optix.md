# Source: https://developer.nvidia.com/rtx/ray-tracing/optix.md

 Join this fireside chat with NVIDIA CEO Jensen Huang at SIGGRAPH on July 29.   [Register Now](https://www.nvidia.com/en-us/events/siggraph/)

# NVIDIA OptiX™ Ray Tracing Engine

An application framework for achieving optimal ray tracing performance on the GPU. It provides a simple, recursive, and flexible pipeline for accelerating ray tracing algorithms. Bring the power of NVIDIA GPUs to your ray tracing applications with programmable intersection, ray generation, and shading.

[Get Started](https://developer.nvidia.com/designworks/optix/download)

![](https://developer.download.nvidia.com/assets/optix/optix_main.jpg)
_Image courtesy of Chaos - RTX Mode_

## Ray Tracing

Programmable GPU-accelerated Ray-Tracing Pipeline, single-ray shader programming model using C++, and ray Tracing acceleration using RT Cores.

## Scalability

Optimized for current and future generations of NVIDIA GPU architectures. Transparently scales across multiple GPUs, and can combine GPU memory over NVLink for large scenes.

## Ease of Integration

Free for commercial use. Nsight Compute 2019.4 &amp; NsightVSE 2019.3, debugger OptiX application profiling support.

## Shader Execution Reordering (SER)

SER is a performance optimization that unlocks the potential for better ray and memory coherency in ray tracing shaders.

[Learn more about SER](https://developer.nvidia.com/blog/improve-shader-performance-and-in-game-frame-rates-with-shader-execution-reordering/)

## AI-Accelerated Denoiser

Included with OptiX, the AI-Accelerated Denoiser is a new post-processing feature to denoise images reducing the need for rendering iterations. This denoiser is based on a paper published by NVIDIA research [“Interactive Reconstruction of Monte Carlo Image Sequences using a Recurrent Denoising Autoencoder”](https://research.nvidia.com/publication/2017-07_interactive-reconstruction-monte-carlo-image-sequences-using-recurrent) It uses GPU-accelerated artificial intelligence to dramatically reduce the time to render a high fidelity image that is visually noiseless.

[Learn More](https://developer.nvidia.com/optix-denoiser)

[![Optimized AI models for Domain Specific Tasks](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/optix-isotropix-1280x620.png)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/optix-isotropix-1280x620.png)

## Partners

From film and games to design and scientific visualization, OptiX has been successfully deployed in a broad range of commercial applications. These applications range from rendering software to scientific visualization (including Gordon Bell Award finalists), defense applications, audio synthesis, and computing lightmaps for games.

[![altair Render](https://developer.download.nvidia.com/assets/optix/altair_done.png)](https://www.thearender.com)

##### Thea Render
×

[![](https://developer.download.nvidia.com/assets/optix/altair_done.png)](https://www.thearender.com)

**Thea Render** is a physically-based global illumination renderer of high quality. It is a unique renderer that is able to render using state-of-the-art techniques in biased photorealistic, unbiased and GPU modes. Thea Render comes with its own standalone application (Studio) with various tools, material editor and advanced staging operations along with integration (plugins) on various popular modeling solutions.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/thea_with.png)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/thea_without1.png)

&gt; Altair® Thea Render® v2.0 integrates NVIDIA® OptiX™ denoiser, dramatically accelerating production of final renders. Users can take advantage of this optimized workflow, creating out-of-the-box, stunning photorealistic images in a fraction of previous render times.
&gt; 
&gt; Dr. Ing. Ioannis Pantazopoulos, VP Rendering Technology, **Altair**

[Learn more about Thea Render](https://www.thearender.com/features/)

[![Autodesk Arnold](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-autodesk.png)](https://www.autodesk.com/)

##### Autodesk Arnold
×

[![Autodesk Arnold](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-arnold_001.png)](https://www.autodesk.com/)

Arnold is an advanced Monte Carlo ray tracing renderer. It is designed for artists and built for the demands of modern animation and visual effects production. It is available as a standalone renderer on Linux, Windows and Mac OS X, with plug-ins for Maya, 3ds Max, Houdini, Cinema 4D, and Katana. With an integrated OptiX denoiser, Arnold takes advantage of NVIDIA AI tech for accelerated interactive rendering.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/optiX-denoiser_Arnold-kitchen.PNG)

&gt; The OptiX Denoiser is an invaluable option for interactive workflows in Arnold. The artist can create and move around geometry and lights and get immediate noise-free visual feedback, even for challenging rendering scenarios.
&gt; 
&gt; Frederic Servant, Arnold Development Manager, **Autodesk**

[Learn more about Arnold](https://www.autodesk.com/products/arnold/overview)

[![Cebas finalRender](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/logo-cebas.png)](https://www.cebas.com/)

##### cebas finalRender
×

[![Cebas finalRender](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/logo-cebas.png)](https://www.cebas.com/)

Cebas Visual Technology, founded in Heidelberg, Germany and headquartered in Victoria, BC Canada, has been developing 3dsMax plugins for visual technology since 1988. Following the launch of our latest finalRender trueHybrid™, cebas&#39; mission as always, is dedicated to getting the most sophisticated renderer into the hands of the artists affordably by incorporating latest NVIDIA GPU technology combined with cebas CPU enhancements, to achieve a powerful as well as an unique mix of processing power. Our new finalRender&#39;s latest addition is the NVIDIA&#39;s OptiX 5.0 AI Denoiser feature. Users can expect ongoing innovative updates as finalRender progresses.

![Cebas finalRender](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/Before_after_Ai-denoiser.png)
_This image shows the OptiX AI-Denoiser running in finalRender at 100 samples after only 45 seconds
                          of rendering._

&gt; Our very first integration tests revealed right from the start that NVIDIA has created an exceptional piece of software engineering by combining the power of AI and their powerful GPU hardware to surmount what has bothered every single GPU software developer for years - Noise in the image. The use of AI Neuronal Network technology in OptiX 5.0 to enhance the process of denoising and cebas&#39; engineering work on finalRender&#39;s trueHybrid™ technology offers a bright future towards higher quality photo-realistic images in much lesser time.
&gt; 
&gt; Edwin Braun, CEO &amp; Co-founder, **Cebas Visual Technology**

[Learn more about finalRender](https://www.cebas.com/)

[![Chaos Group Vray](https://developer.download.nvidia.com/assets/optix/chaos_new.png)](https://www.chaosgroup.com/)

##### Chaos Group Vray
×

[![Chaos Group Vray](https://developer.download.nvidia.com/assets/optix/chaos_new.png)](https://www.chaosgroup.com/)

Chaos Group is a worldwide leader in computer graphics. They create the technology that helps artists and designers create photoreal imagery and animation for design, television, and feature films. Their physically-based rendering and simulation software is used daily by top design studios, architectural firms, advertising agencies, and visual effects companies around the globe. Their research and development in cloud rendering, material scanning, and virtual reality is shaping the future of creative storytelling and digital design.

![Chaos Group Vray](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/CGvrayblog.png)

&gt; We’re finding the NVIDIA denoising results to be very impressive on interactive scenes, giving artists a much quicker estimate of what their final result will look like. We believe this will speed the creative process while using our upcoming V-Ray GPU.
&gt; 
&gt; Vlado Koylazov, founder, **Chaos Group**

[Learn more about Vray](https://www.chaosgroup.com/)

[![SOLIDWORKS Visualize](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-solidworks.png)](https://www.solidworks.com/category/visualization)

##### SOLIDWORKS Visualize
×

[![SOLIDWORKS Visualize](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-solidworks.png)](https://www.solidworks.com/category/visualization)

**SOLIDWORKS® Visualization products** (formerly known as Bunkspeed) provide a suite of standalone software tools that combine industry-leading rendering capabilities with design-oriented features and workflows that enable easy and fast creation of visual content for designers, engineers, marketing, and other content creators. Import SOLIDWORKS, Autodesk Alias®, Rhino®, SketchUp® and many other CAD formats to create compelling scenes and ultimately the most realistic content possible.

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/denoiser_cover-image.png)](http://blogs.solidworks.com/solidworksblog/2018/02/introducing-new-artificial-intelligence-denoiser.html)[Learn more SOLIDWORKS Visulaize](https://www.solidworks.com/category/visualization)  
  
 News:  
 Blog: [Introducing the New Artificial Intelligence Denoiser](http://blogs.solidworks.com/solidworksblog/2018/02/introducing-new-artificial-intelligence-denoiser.html)  
 Blog: [From Great Idea to Amazing Product: SOLIDWORKS and NVIDIA Power AI, VR and Virtualized Workflows](https://blogs.nvidia.com/blog/2018/02/05/solidworks-world-2018/)

[![ESI IC.IDO](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-icido.png)](https://www.esi-group.com/)

##### ESI IC.IDO
×

[![ESI IC.IDO](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-icido.png)](https://www.esi-group.com/)

**ESI Group** is a leading innovator in Virtual Prototyping software and services. ESI | IC.IDO provides a Human Centric digital mock-up environment that enables individual engineers as well as teams to explore, experience, validate, and collaborate to resolve complex integration scenarios at the intersection between product function, human interaction and assembly/service requirements.

&gt; “We adopted OptiX for ray tracing in IC.IDO. It was incredibly easy to integrate and offers amazing speed and performance with NVIDIA GPUs, this frees our engineering team to focus their time and talents on developing new features for our Virtual Engineering enterprise customers. Offering a unified visualization and physical simulation experience in VR gives users the ability to interact with their products and processes in ways previously only possible with full scale physical prototypes.”
&gt; 
&gt; Dr. Christian Odaker, Director of R&amp;D, Immersive Experience at ESI Group

[Learn more about IC.IDO](https://virtualreality.esi-group.com)

[![Foundry Modo](https://developer.download.nvidia.com/assets/optix/foundry_done.png)](https://www.foundry.com/products/modo)

##### Foundry Modo
×

[![Foundry Modo](https://developer.download.nvidia.com/assets/optix/foundry_done.png)](https://www.foundry.com/products/modo)

Modo’s powerful and flexible 3D modeling, texturing and rendering toolset empowers artists to explore and develop ideas without jumping through technical hoops. Modo® is your starting point for creative exploration.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/Modo122_Optix_ArchViz_001.jpg) **Without Denoiser        |            With Denoiser**  
  
 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/Modo122_Optix_RimDeNoise_002.jpg) **Without Denoiser        |            With Denoiser**

&gt; Modo artists can now expect to see GPU Accelerated Rendering with OptiX™ from NVIDIA®. The integrated enhancement provides incredible speed and quality for their product and arch-viz creations. Developed and integrated in collaboration with NVIDIA®’s award-winning engineering team, OptiX™ has been optimized specifically for Modo 12.2 and future releases.
&gt; 
&gt; Shane Griffith, Senior Product Manager, **Foundry**

[Learn more about Modo](https://www.foundry.com/products/modo)

[![NVIDIA Iray](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-iray.png)](https://www.nvidia.com/en-us/design-visualization/iray)

##### NVIDIA Iray
×

[![NVIDIA Iray](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-iray.png)](https://www.nvidia.com/en-us/design-visualization/iray)

**NVIDIA Iray** employs OptiX technology for optimal performance in both its path tracing and ray tracing render modes. Iray is a state of the art, yet easy to use, photorealistic rendering solution provided as an SDK for seamless integration into custom tools and within industry-leading products from the likes of Dassault Systemes and Siemens PLM.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/image07.png)[Learn more about Iray](https://www.nvidia.com/en-us/design-visualization/iray)

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-optis1.png)](http://www.optis-world.com/)

##### OPTIS
×

[![OPTIS](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-optis1.png)](http://www.optis-world.com/)

**OPTIS** , the virtual prototyping company, brings life and emotion to all industrial projects. Its world-leading solutions pave the way for a revolutionary design process: towards zero physical prototypes. Since 1989, OPTIS offers its know-how in light and human vision simulation into leading CAD/CAM software and dedicated immersive virtual solutions. This synergy creates true-to-life virtual mockups which are used as real decision-making tools. Today, more than 2,500 clients in over 50 countries already trust OPTIS and innovate day after day with its solutions to ensure the look and safety of their designs, reduce their ecological footprint and bring their future products faster on the market.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Optis003.png)

&gt; “We use powerful NVIDIA GPU technologies, like the new Quadro GV100 to accelerate our simulation applications and algorithms, and NVIDIA OptiX for fast AI-based rendering. Looking ahead, we’re excited about the potential NVIDIA RTX ray-tracing technology holds to deliver more lifelike images faster than ever,” said Jacques Delacour, CEO and founder of OPTIS.

[Learn more about SPEOS (Bright Light and Appearance Simulation)](https://www.optis-world.com/product-offering-light-simulation-virtual-reality-software/SPEOS)[Learn more about Theia RT (Real-time Color and Material Evaluation)](https://www.optis-world.com/product-offering-light-simulation-virtual-reality-software/theia-rt-software-evaluation-vizualization-real-time)[Learn more about Optis](http://www.optis-world.com/)

[![Pixar’s Flow Material Editing Tool](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-pixar1.png)](https://example.com)

##### Pixar’s Flow Material Editing Tool
×

 ![Pixar’s Flow Material Editing Tool](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-pixar1.png)

**Pixar Animation Studio&#39;s** new material editing tool &quot;Flow&quot; enables their artists to interactively edit rich, complex shading networks. Flow provides live real-time feedback with full, multi-bounce progressive ray tracing using OptiX.

![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/image02.png)
_Pixar Flow material editing tool. Image courtesy of Pixar Animation Studios_
[Watch SIGGRAPH talk on OptiX integration in Flow](http://on-demand.gputechconf.com/siggraph/2015/video/SIG515-Danny-Nahmias.html)

[![Redshift](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/logo-redshift.png)](https://www.redshift3d.com/)

##### Redshift
×

[![Redshift](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/logo-redshift.png)](https://www.redshift3d.com/)

Redshift Rendering Technologies Inc was founded in early 2012 in Newport Beach, California with the goal of developing a production-quality, GPU-accelerated renderer with support for the biased global illumination techniques that until now have remained squarely in the CPU-only domain.

https://www.youtube-nocookie.com/embed/2vJ_5nPVU0s?&amp;loop=1&amp;playlist=2vJ_5nPVU0s

&gt; With OptiX 5.0, NVIDIA continues to lead the way for the use of AI in rendering for design, character generation and the creation of virtual worlds. Integration of OptiX 5.0 was a no-brainer for us — being both easy and free, it turbocharges the creative process and improves productivity for our users.
&gt; 
&gt; Panos Zompolas, chief technology officer and co-founder, **Redshift**

[Learn more about Redshift](https://www.redshift3d.com/product)

[![SideFX Houdini](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/logo-sidefx_001.png)](https://www.sidefx.com/products/houdini/)

##### SideFX Houdini
×

[![SideFX Houdini](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/logo-sidefx_001.png)](https://www.sidefx.com/products/houdini/)

Houdini is a 3D animation software application developed by SideFX, based in Toronto. SideFX adapted Houdini from the PRISMS suite of procedural generation software tools. Its exclusive attention to procedural generation distinguishes it from other 3D computer graphics software.

![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/houdini_denoiser.png)
_result of denoiser shown on the left half of image above_
[Learn more about the Houdini denoiser integration](http://www.sidefx.com/docs/houdini/render/optixdenoiser.html)

[![Unity](https://developer.download.nvidia.com/assets/optix/unity_done.png)](https://unity.com/srp/High-Definition-Render-Pipeline)

##### Unity
×

[![Unity](https://developer.download.nvidia.com/assets/optix/unity_done.png)](https://unity.com/srp/High-Definition-Render-Pipeline)

Unity is the creator of the world’s leading real-time 3D development platform, giving users the most powerful and accessible tools to quickly create, easily operate, and fully monetize amazing immersive and interactive experiences. Unity empowers anyone, regardless of skill level and industry, to maximize their success.

![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/Denoiser/UnityOptixDenoise.png)
_By using AI denoising, artists can spend more time creating beautiful renderings than battling noise. Robust denoising means that creators can focus on iterating the artwork, thereby optimizing workflow efficiency and output quality._
[Learn more about Unity](https://unity.com/srp/High-Definition-Render-Pipeline)

[![Visual Molecular Dynamics (VMD)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-vmd.png)](http://www.ks.uiuc.edu/Research/vmd/)

##### Visual Molecular Dynamics (VMD)
×

[![Visual Molecular Dynamics (VMD)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/optix/logo-action-vmd.png)](http://www.ks.uiuc.edu/Research/vmd/)

**Visual Molecular Dynamics (VMD)** is a molecular visualization program for displaying, animating, and analyzing large biomolecular systems using 3-D graphics and built-in scripting. VMD’s preferred rendering mode for both viewport and final render is OptiX, with full VCA support available. The OptiX path renders the highest visual quality and even has a frame rate five times higher than OpenGL on massive datasets.

https://www.youtube-nocookie.com/embed/6hKq5A __yrY?&amp;loop=1&amp;playlist=6hKq5A__ yrY
[Learn more about VMD](http://www.ks.uiuc.edu/Research/vmd/)

[  
 ![Maverick](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/maverickrender-logo-1800x512-black.png)](https://maverickrender.com/)

##### Maverick Studio
×

[![Maverick](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/maverickrender-logo-1800x512-black.png)](https://maverickrender.com/)

Maverick Render consists of 3 GPU-accelerated applications that will help designers efficiently render photo-realistic 3D models and analyze how performant their GPUs are.

**Maverick Studio** is a very easy-to-use product rendering application that harnesses Maverick’s proprietary light simulation technology with interactive and intuitive drag-and-drop tools.

**Maverick Indie** , the baby brother of Maverick Studio, is an ideal tool to import 3D models or materials and render highly photo-real presentations and turntables.

**Maverick Benchmark** is a very consistent and reliable free-to-use tool that stress-tests Nvidia GPUs to tell how performant they are.

 ![maverick.jpg](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/maverick.jpg)[Learn more about Maverick](https://maverickrender.com/)

[  
 ![OTOY](https://developer.download.nvidia.com/images/otoy_logo_vector_horizontal.png)](https://home.otoy.com/render/octane-render/)

##### Otoy
×

[![OTOY](https://developer.download.nvidia.com/images/otoy-logo-vector.svg)](https://home.otoy.com/render/octane-render/)

Octane by OTOY is the first and fastest GPU accelerated unbiased path-traced render engine and features OptiX™ 7 ray-tracing hardware acceleration powered by NVIDIA RTX. OptiX RTX GPU hardware acceleration enables users to see 2-3x speed increases in many scenes using RTX and up to 15-30x accelerations in fully RTX optimized scenes.

 ![otoy.jpg](https://developer.download.nvidia.com/images/otoy-octane-cornerstore.png)[Learn more about Octane](https://home.otoy.com/render/octane-render/)

## OptiX in the News

 ![OptiX 8 Release](https://developer.download.nvidia.com/assets/optix/optix_news.png)

### NVIDIA releases OptiX 8

A flexible and powerful ray tracing solution for the Media and Entertainment Industry.

[Learn More](https://developer.nvidia.com/blog/flexible-and-powerful-ray-tracing-with-optix-8/)

 ![What’s New in Optix](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/optix/new_in_optix.png)

### What’s New in OptiX

Catch up with the latest additions to the OptiX SDK and learn tips and tricks on how best to implement them into your products.

[Learn More](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s31736/)

 ![OptiX Advanced Topics](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/optix/optix_news_thumbnail_2.jpg)

### OptiX Advanced Topics

GTC 2021 Session

Join Senior Software Engineer, David Hart for a deep dive into the OptiX Curves API and learn best practices for how to best optimize your applications.

[Learn More](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s31752/)

## Resources

https://www.youtube-nocookie.com/embed/Z7QsPb7YWjc

- [**How to get started with OptiX 7**](https://devblogs.nvidia.com/how-to-get-started-with-optix-7/)
- [Documentation](https://raytracing-docs.nvidia.com/)
- [Learn more about the AI-accelerated denoiser](/optix-denoiser)
- [Developer Forum](https://devtalk.nvidia.com/default/board/90/)
- [GTC on Demand](http://on-demand-gtc.gputechconf.com/gtcnew/on-demand-gtc.php?searchByKeyword=optix&amp;searchItems=&amp;sessionTopic=&amp;sessionEvent=&amp;sessionFormat=&amp;submit=&amp;select=+)
- [OptiX GPU Ray Tracing ACM paper](http://cacm.acm.org/magazines/2013/5/163758-gpu-ray-tracing/fulltext)

Ready to get started developing with OptiX?

[Get Started](https://developer.nvidia.com/designworks/optix/download)  


