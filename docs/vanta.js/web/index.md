# Vanta.js - Animated 3D Backgrounds For Your Website

## Overview

Vanta.js is a lightweight JavaScript library that adds animated 3D digital art backgrounds to any webpage with just a few lines of code. It's perfect for creating stunning, interactive visual effects that respond to mouse/touch input.

**Website:** https://www.vantajs.com/  
**GitHub:** https://github.com/tengbao/vanta  
**npm:** `npm install vanta`

### Key Features

- **Easy integration** - Works with vanilla JavaScript, React, Angular, Vue, and other frameworks
- **Multiple effects** - Choose from birds, fog, waves, clouds, globe, net, cells, trunk, topology, dots, rings, halo, and more
- **Interactive** - Effects respond to mouse/touch inputs and device gyroscope
- **Performance** - Runs at 60fps on most laptops/desktops; renders with three.js (WebGL) or p5.js
- **Small filesize** - ~120kb minified and gzipped (mostly three.js), smaller than background images/videos
- **Customizable** - Easily modify colors, parameters, and styling to match your brand
- **No pixelation** - Canvas runs at full resolution

## What is Vanta?

Vanta inserts an animated effect as a background into any HTML element. The library:
- Uses [three.js](https://github.com/mrdoob/three.js/) (WebGL) for 3D effects like birds, waves, clouds, globe
- Uses [p5.js](https://github.com/processing/p5.js) for procedural effects like trunk and topology
- Appends a canvas as a child of your container element
- Allows other children to appear as foreground content in front of the canvas

## Basic Usage

### With Script Tags

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta/dist/vanta.waves.min.js"></script>
<script>
  VANTA.WAVES('#my-background')
</script>
```

**View fiddle:** https://jsfiddle.net/usdzfbLt/1/

### With Options

```js
VANTA.WAVES({
  el: '#my-background',        // element selector or DOM reference
  color: 0x000000,
  waveHeight: 20,
  shininess: 50,
  waveSpeed: 1.5,
  zoom: 0.75
})
```

## Common Options

- **el** (required): The container element (selector string or DOM object)
  - Vanta appends a canvas as a child of this element
  - Canvas inherits the width/height of this container
  - For fullscreen canvas, make sure the container is fullscreen
  - Other children appear as foreground content in front of the canvas

- **mouseControls**: (default: `true`) Enable/disable mouse interaction
- **touchControls**: (default: `true`) Enable/disable touch interaction  
- **gyroControls**: (default: `false`) Enable device gyroscope control

**Note:** Each effect has its own specific parameters. Explore them all at https://www.vantajs.com/

## Available Effects

- **birds** - Flying birds effect (three.js, GPGPU-based)
- **fog** - Foggy atmosphere effect
- **waves** - Ocean waves effect
- **clouds** - Procedural cloud generation
- **clouds2** - Alternative cloud effect
- **globe** - Rotating globe with terrain
- **net** - Interconnected network nodes
- **cells** - Cellular/organic pattern
- **trunk** - Tree-like branching structure (p5.js)
- **topology** - Topographical mesh surface (p5.js)
- **dots** - Spherical dot pattern with lines
- **rings** - Concentric ring pattern
- **halo** - Glowing halo effect

## Updating Options After Initialization

```js
const effect = VANTA.WAVES({
  el: '#my-background',
  color: 0x000000
})

// Update options on running effect
effect.setOptions({
  color: 0xff88cc
})

// Force redraw at new container size
effect.resize()
```

## Cleanup

```js
const effect = VANTA.WAVES('#my-background')
effect.destroy() // Call in React componentWillUnmount, Vue beforeDestroy, etc.
```

## Framework Integration

### React with Hooks

```js
import React, { useState, useEffect, useRef } from 'react'
import BIRDS from 'vanta/dist/vanta.birds.min'
// Make sure window.THREE is defined via <script> tag

const MyComponent = (props) => {
  const [vantaEffect, setVantaEffect] = useState(null)
  const myRef = useRef(null)
  
  useEffect(() => {
    if (!vantaEffect) {
      setVantaEffect(BIRDS({
        el: myRef.current
      }))
    }
    return () => {
      if (vantaEffect) vantaEffect.destroy()
    }
  }, [vantaEffect])
  
  return <div ref={myRef}>
    Foreground content goes here
  </div>
}
```

**View fiddle:** https://jsfiddle.net/1mcr7x50/2/

### React with Classes

```js
import React from 'react'
import BIRDS from 'vanta/dist/vanta.birds.min'
// Make sure window.THREE is defined via <script> tag

class MyComponent extends React.Component {
  constructor() {
    super()
    this.vantaRef = React.createRef()
  }
  
  componentDidMount() {
    this.vantaEffect = BIRDS({
      el: this.vantaRef.current
    })
  }
  
  componentWillUnmount() {
    if (this.vantaEffect) this.vantaEffect.destroy()
  }
  
  render() {
    return <div ref={this.vantaRef}>
      Foreground content goes here
    </div>
  }
}
```

**View fiddle:** https://jsfiddle.net/4fzxhv1w/2/

### Vue 2 (Single File Component)

```vue
<template>
  <div ref='vantaRef'>
    Foreground content here
  </div>
</template>

<script>
import BIRDS from 'vanta/dist/vanta.birds.min'
// Make sure window.THREE is defined via <script> tag

export default {
  mounted() {
    this.vantaEffect = BIRDS({
      el: this.$refs.vantaRef
    })
  },
  beforeDestroy() {
    if (this.vantaEffect) {
      this.vantaEffect.destroy()
    }
  }
}
</script>
```

## Using THREE or p5 from npm

### With Custom three.js

```js
import React from 'react'
import * as THREE from 'three'
import BIRDS from 'vanta/dist/vanta.birds.min'

class MyComponent extends React.Component {
  componentDidMount() {
    this.vantaEffect = BIRDS({
      el: this.vantaRef.current,
      THREE: THREE  // Pass custom THREE
    })
  }
}
```

### With Custom p5.js

```js
import React from 'react'
import p5 from 'p5'
import TRUNK from 'vanta/dist/vanta.trunk.min'

class MyComponent extends React.Component {
  componentDidMount() {
    this.vantaEffect = TRUNK({
      el: this.vantaRef.current,
      p5: p5  // Pass custom p5
    })
  }
}
```

## Performance Considerations

### Advantages
- **No pixelation** - Canvas renders at full resolution
- **Efficient** - Smaller filesize than background images/videos
- **Smooth performance** - Runs at 60fps on most modern devices
- **Responsive** - Effects automatically adapt to container size

### Limitations
- Some WebGL effects may be slow on older computers
- Avoid using multiple Vanta effects on a single page
- Not all effects work well on mobile devices (use background image/color fallback)
- Effects that use THREE must have `window.THREE` defined
- Effects that use p5 must have `window.p5` defined

## Installation and Distribution

### Via npm

```bash
npm install vanta
```

Then import the effect you want:

```js
import BIRDS from 'vanta/dist/vanta.birds.min'
```

### Via CDN (jsdelivr)

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta/dist/vanta.birds.min.js"></script>
```

Available at: https://cdn.jsdelivr.net/npm/vanta@latest/dist/

### For Strikingly.com Sites

Paste the following into Strikingly Editor → Settings → Custom Code → Footer Code:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r121/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.birds.min.js"></script>
<script>
  var setVanta = () => {
    if (window.VANTA) {
      window.VANTA.BIRDS({
        el: '.s-page-1 .s-section-1 .s-section',
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 200,
        minWidth: 200,
        scale: 1,
        scaleMobile: 1
      })
    }
  }
  _strk.push(function() {
    setVanta()
    window.edit_page.Event.subscribe('Page.beforeNewOneFadeIn', setVanta)
  })
</script>
```

## Browser Compatibility

- Modern browsers with WebGL support (Chrome, Firefox, Safari, Edge)
- Falls back gracefully on older browsers (show background image instead)
- Mobile support varies by effect (test each effect on your target devices)

## API Reference

### Methods

#### `VANTA.EFFECT_NAME(options)`

Initialize an effect. Returns effect object with methods:

```js
const effect = VANTA.WAVES({
  el: '#background'
})
```

#### `effect.setOptions(newOptions)`

Update effect options while animation is running:

```js
effect.setOptions({
  color: 0xff0000,
  waveHeight: 25
})
```

#### `effect.resize()`

Force canvas to redraw at current container dimensions:

```js
window.addEventListener('resize', () => {
  effect.resize()
})
```

#### `effect.destroy()`

Clean up effect and remove canvas:

```js
effect.destroy()
```

## Troubleshooting

### THREE is undefined
- Make sure `<script src="three.min.js"></script>` is included before Vanta effect script
- Or pass custom THREE via `THREE: THREE` option when importing from npm

### p5 is undefined
- Include `<script src="p5.min.js"></script>` for p5-based effects
- Or pass custom p5 via `p5: p5` option

### Effect not visible
- Check that container element (`el`) has non-zero width/height
- Verify canvas is being appended to the container
- Check browser console for errors
- Try simpler effect (e.g., waves) to test

### Performance issues
- Reduce quality settings if available for effect
- Use only one Vanta effect per page
- Try alternative effects to find best performance
- Consider using static background on older devices

### Mobile not working
- Not all effects support mobile well
- Set a background image/color as fallback
- Test effect on mobile device before deployment

## Credits

Vanta.js was created by [Teng Bao](https://www.tengbao.me/).

**Attribution:**
- Birds effect from [three.js examples](https://threejs.org/examples/?q=birds#webgl_gpgpu_birds) by @zz85
- Fog effect from [The Book of Shaders](https://thebookofshaders.com/13/) by @patriciogonzalezvivo
- Clouds effect from [ShaderToy](https://www.shadertoy.com/view/XslGRr) by Inigo Quilez
- Clouds2 effect from [ShaderToy](https://www.shadertoy.com/view/lsBfDz) by Rune Stubbe
- Trunk and Topology effects from [generated.space](http://generated.space/) by Kjetil Midtgarden Golid @kgolid

**Inspiration:** shadertoy.com, #generative, /r/generative, /r/creativecoding

## License

MIT License - Copyright 2020 Teng Bao

See https://github.com/tengbao/vanta/blob/master/LICENSE.md for full license text.

## Version History

**0.5.24** - Update readme examples, remove gallery images from main branch

**0.5.23** - Update waves, dots, globe for latest three.js; update birds to r134; fix animation speed; fix custom three in halo

**0.5.22** - Fix hash function in clouds; update dependencies

**0.5.21** - Fix readme on npmjs.com; fix fog on retina screens

**0.5.20** - Add Vue.js example; add resize example; remove current reference on destroy

**0.5.19** - Fix globe color updating via setOptions; update fiddle three.js version

**0.5.18** - Upgrade three.js to r119; update effects for newest three.js

**0.5.17** - Fix custom THREE in birds; call triggerMouseMove on setOptions

**0.5.16** - Add gyroControls option; add default params for triggerMouseMove

**0.5.15** - Add offset options for halo

**0.5.14** - Fix readme encoding; add halo options

**0.5.13** - Fix missing camera for some effects

**0.5.12** - Fix missing THREE for dots; add initial halo effect

**0.5.11** - Fix resize issue for React

**0.5.10** - Update readme for npm; add showLines option for dots

**0.5.8** - Initial publish on npm; fix method name in readme

**0.5.7** - Remove gallery code from master, add to gallery branch; fix compilation issue

**0.5.6** - Add ability to disable mouse/touch controls; add custom scale option

**0.5.5** - Fix container height/width issue; fix text node handling

**0.5.4** - Add custom THREE support; add create-react-app example; fix p5 renderer error

**0.5.3** - Fix VANTA undefined in waves; add setOptions method; add speed option for clouds

**0.5.2** - Add forceAnimate option; add globe effect

**0.5.1** - Allow touchscreen controls; fix Gatsby build window error

**0.5.0** - Update module for static import; update React example to use refs; fix sibling overlay; add THREE missing warning

**0.4.0** - Add mobile support for birds (alternative to GPGPU); add bird size option

**0.3.0** - Remove backgroundColor "transparent" option, use backgroundAlpha instead

**0.2.0** - Add p5 effects (trunk, topology); update dots with spherical effect

**0.1.0** - First release

## Resources

- **Demo Gallery:** https://www.vantajs.com/
- **GitHub Repository:** https://github.com/tengbao/vanta
- **npm Package:** https://www.npmjs.com/package/vanta
- **CDN:** https://cdn.jsdelivr.net/npm/vanta@latest/dist/
- **JSFiddle Examples:** https://jsfiddle.net/usdzfbLt/1/ (basic), https://jsfiddle.net/1mcr7x50/2/ (React)

---

**Source:** GitHub repository (https://github.com/tengbao/vanta)  
**Last Updated:** 2026-04-03
