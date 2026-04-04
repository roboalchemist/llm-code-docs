# Source: https://lynxjs.org/guide/styling/animation.md

# Motion

Lynx offers extensive motion capabilities, allowing developers to create more modern, smooth, and intuitive user interfaces. Utilizing these features, developers can produce stunning transition effects and natural motion feedback, thereby enhancing user experience.

## Add transitions for layout and style changes.

If you need to smoothly apply new property values when the layout or style changes, you can use transitions.

Transitions provide a way to control the speed of animation changes when altering CSS properties. Instead of having changes take effect immediately, you can have the changes happen gradually over a period of time. For example, when you change an element's color from white to black, normally the change happens instantaneously. With transitions enabled, the change takes place over an interval that follows an easing curve, all of which can be customized.

Transitions are automatically triggered, non-repetitive, and easy to use. They can be defined using the shorthand [`transition`](/api/css/properties/transition.md) to set animation properties and duration, or you can specify them individually with [`transition-property`](/api/css/properties/transition-property.md) and [`transition-duration`](/api/css/properties/transition-duration.md), among others.

### Implement Collapse and Expand Effect for List Items

You can use transitions to add an animation effect for expanding and collapsing a list item in a list:

**This is an example below:  animation**

**Entry:** `src/transition_toggle`
**Bundle:** `dist/toggle_transition_demo.lynx.bundle` | Web: `dist/toggle_transition_demo.web.bundle`

```tsx
import { root, useState } from "@lynx-js/react";
import type { ReactNode } from "@lynx-js/react";
import "./index.scss";

const AccordionItem = ({ title, content }: { title: ReactNode; content: ReactNode }) => {
  const [isActive, setIsActive] = useState(false);

  const toggleItem = () => {
    setIsActive(!isActive);
  };
  return (
    <view className={`accordion-item ${isActive ? "active" : ""}`}>
      <view className="accordion-header" bindtap={toggleItem} style={{ transition: "background-color 0.5s" }}>
        <text>{title}</text>
        <text className={`icon ${isActive ? "rotate" : ""}`} style={{ transition: "transform 0.5s" }}>▼</text>
      </view>
      <view
        className="accordion-content"
        // use 200px to estimate the height
        style={{ maxHeight: isActive ? "200px" : "14px", transition: "max-height 2s linear" }}
      >
        <text className="content">{content}</text>
      </view>
    </view>
  );
};

const Accordion = () => {
  const items = [
    {
      title: "Item 1",
      content: "This is the content of item 1. ".repeat(10),
    },
    {
      title: "Item 2",
      content: "This is the content of item 2. ".repeat(10),
    },
    {
      title: "Item 3",
      content: "This is the content of item 3. ".repeat(10),
    },
  ];

  return (
    <view className="accordion">
      {items.map((item, index) => <AccordionItem key={index} title={item.title} content={item.content} />)}
    </view>
  );
};
root.render(<Accordion />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



## Achieve stunning effects with keyframes.

If you need multiple sets of styles to transition in sequence, you can use keyframe animations.

Keyframe animations are defined in CSS using the [`@keyframes`](/api/css/at-rule/keyframes.md) rule, which specifies the style changes at various stages of the animation. The [`animation`](/api/css/properties/animation.md) property is then used to apply the defined animation to elements, allowing you to set parameters such as animation name, duration, delay, and number of iterations.

Keyframe animations are more flexible and controllable compared to transitions, as they allow you to specify the process and provide finer control over timing curves. You can define them in CSS with [`@keyframes`](/api/css/at-rule/keyframes.md) and specify them using the shorthand [`animation`](/api/css/properties/animation.md) property, or define them with individual properties such as [`animation-name`](/api/css/properties/animation-name.md), [`animation-duration`](/api/css/properties/animation-duration.md), and others.

### To achieve a rotation effect

Keyframe animations can be used to achieve the effect of a bounding box rotation.

**This is an example below:  animation**

**Entry:** `src/keyframe_rotate`
**Bundle:** `dist/keyframe_rotate.lynx.bundle` | Web: `dist/keyframe_rotate.web.bundle`

```scss
page {
  background-color: #f7f7f7;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  border: 1px solid red;
}

.title-name-wrapper-border {
  position: relative;
  z-index: 0;
  width: 100%;
  height: 100%;
  border-radius: 10px;
  overflow: hidden;
  padding: 2rem;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(1turn);
  }
}

@keyframes opacityChange {
  50% {
    opacity: 1;
  }

  100% {
    opacity: 0.5;
  }
}

.container {
  position: relative;
  z-index: 0;
  width: 80%;
  height: 300px;
  border-radius: 10px;
  overflow: hidden;
}

.title-name-wrapper-border-before {
  position: absolute;
  z-index: -2;
  left: -50%;
  top: -50%;
  width: 200%;
  height: 200%;
  background-color: red;
  background-repeat: no-repeat, no-repeat, no-repeat, no-repeat;
  background-size: 50% 50%, 50% 50%;
  background-position: 0px 0px, 100% 0px, 100% 100%, 0px 100%;
  background-image:
    linear-gradient(#399953, #399953),
    linear-gradient(#fbb300, #fbb300),
    linear-gradient(#d53e33, #d53e33),
    linear-gradient(#377af5, #377af5);
  animation: rotate 4s linear infinite;
}

.title-name-wrapper-border-after {
  position: absolute;
  z-index: -1;
  left: 6px;
  top: 6px;
  width: calc(100% - 12px);
  height: calc(100% - 12px);
  background: white;
  border-radius: 5px;
  animation: opacityChange 3s infinite alternate;
}

```



### To achieve a spring effect

Keyframe animations can add spring-like physics to element motion.

**This is an example below:  animation**

**Entry:** `src/keyframe_spring`
**Bundle:** `dist/keyframe_spring.lynx.bundle` | Web: `dist/keyframe_spring.web.bundle`

```scss
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.spring-box {
  width: 200px;
  height: 200px;
  background-color: #4a90e2;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.box-text {
  color: white;
  font-size: 24px;
}

.animate {
  animation: kf-anim-spring 4s linear forwards;
}

@keyframes kf-anim-spring {
  0% {
    transform: scale(0, 0);
  }

  0.999% {
    transform: scale(0.306, 0.306);
  }

  1.998% {
    transform: scale(0.967, 0.967);
  }

  2.997% {
    transform: scale(1.586, 1.586);
  }

  3.996% {
    transform: scale(1.825, 1.825);
  }

  4.995% {
    transform: scale(1.586, 1.586);
  }

  5.994% {
    transform: scale(1.046, 1.046);
  }

  6.993% {
    transform: scale(0.529, 0.529);
  }

  7.992% {
    transform: scale(0.319, 0.319);
  }

  9.09% {
    transform: scale(0.54, 0.54);
  }

  10.089% {
    transform: scale(0.993, 0.993);
  }

  11.088% {
    transform: scale(1.409, 1.409);
  }

  12.087% {
    transform: scale(1.561, 1.561);
  }

  13.086% {
    transform: scale(1.389, 1.389);
  }

  14.085% {
    transform: scale(1.018, 1.018);
  }

  15.084% {
    transform: scale(0.671, 0.671);
  }

  16.083% {
    transform: scale(0.537, 0.537);
  }

  17.082% {
    transform: scale(0.67, 0.67);
  }

  18.081% {
    transform: scale(0.973, 0.973);
  }

  19.08% {
    transform: scale(1.263, 1.263);
  }

  20.079% {
    transform: scale(1.381, 1.381);
  }

  21.178% {
    transform: scale(1.258, 1.258);
  }

  22.177% {
    transform: scale(1.003, 1.003);
  }

  23.176% {
    transform: scale(0.77, 0.77);
  }

  24.175% {
    transform: scale(0.685, 0.685);
  }

  25.174% {
    transform: scale(0.781, 0.781);
  }

  26.173% {
    transform: scale(0.989, 0.989);
  }

  27.172% {
    transform: scale(1.184, 1.184);
  }

  28.171% {
    transform: scale(1.259, 1.259);
  }

  29.17% {
    transform: scale(1.185, 1.185);
  }

  30.169% {
    transform: scale(1.015, 1.015);
  }

  31.168% {
    transform: scale(0.852, 0.852);
  }

  32.167% {
    transform: scale(0.785, 0.785);
  }

  33.266% {
    transform: scale(0.855, 0.855);
  }

  34.265% {
    transform: scale(0.997, 0.997);
  }

  35.264% {
    transform: scale(1.128, 1.128);
  }

  36.263% {
    transform: scale(1.176, 1.176);
  }

  38.261% {
    transform: scale(1.006, 1.006);
  }

  40.259% {
    transform: scale(0.854, 0.854);
  }

  42.257% {
    transform: scale(0.991, 0.991);
  }

  44.255% {
    transform: scale(1.12, 1.12);
  }

  46.353% {
    transform: scale(1.001, 1.001);
  }

  48.351% {
    transform: scale(0.9, 0.9);
  }

  52.347% {
    transform: scale(1.081, 1.081);
  }

  56.343% {
    transform: scale(0.932, 0.932);
  }

  60.439% {
    transform: scale(1.055, 1.055);
  }

  64.435% {
    transform: scale(0.954, 0.954);
  }

  68.431% {
    transform: scale(1.037, 1.037);
  }

  72.527% {
    transform: scale(0.968, 0.968);
  }

  76.523% {
    transform: scale(1.025, 1.025);
  }

  80.519% {
    transform: scale(0.978, 0.978);
  }

  84.615% {
    transform: scale(1.017, 1.017);
  }

  88.611% {
    transform: scale(0.985, 0.985);
  }

  92.607% {
    transform: scale(1.011, 1.011);
  }

  96.703% {
    transform: scale(0.99, 0.99);
  }

  100% {
    transform: scale(1.006, 1.006);
  }
}

```



## Create flexible keyframe animations in JS.

Additionally, our [animate api](/api/lynx-api/lynx/lynx-animate-api.md) extends CSS keyframe animations, allowing for more flexible and dynamic creation and control of animations in JavaScript. Developers can dynamically generate and modify animations at runtime based on interactions or logic, offering users a more vibrant and interactive experience.

### To achieve a variable speed transform motions

By using the animate api, we can add a motion to the original that changes its rate in real time.

**This is an example below:  animation**

**Entry:** `src/animate`
**Bundle:** `dist/animate.lynx.bundle`

```tsx
import { root } from "@lynx-js/react";

import "./index.scss";

const AnimateAnimationExample = () => {
  return (
    <view style={{ width: "100%", height: "100%" }}>
      <view
        id="view1"
        className="box"
        bindtap={() => {
          const ani = lynx.getElementById("view1").animate(
            [
              {
                transform: "translate(0%, 0%) rotate(0deg)",
                "animation-timing-function": "linear",
              },
              {
                transform: "translate(200px, 0%) rotate(90deg)",
                "animation-timing-function": "cubic-bezier(.91,.03,.94,.11)",
              },
              {
                transform: "translate(200px, 100%) rotate(180deg)",
                "animation-timing-function": "linear",
              },
              {
                transform: "translate(0%, 100%) rotate(270deg)",
                "animation-timing-function": "cubic-bezier(.91,.03,.94,.11)",
              },
              {
                transform: "translate(0%, 0%) rotate(360deg)",
              },
            ],
            {
              name: "js-animation-1",
              duration: 5000,
              iterations: Infinity,
              easing: "linear",
            },
          );
        }}
      >
      </view>
    </view>
  );
};
root.render(<AnimateAnimationExample />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```


