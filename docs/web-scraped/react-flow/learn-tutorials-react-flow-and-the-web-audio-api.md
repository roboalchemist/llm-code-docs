# Source: https://reactflow.dev/learn/tutorials/react-flow-and-the-web-audio-api

2023/04/14

## Integrating React Flow and the Web Audio API 

[![](https://github.com/hayleigh-dot-dev.png)](https://twitter.com/hayleighdotdev)

[Hayleigh Thompson](https://twitter.com/hayleighdotdev)

Software Engineer

Today we'll be looking at how to create an interactive audio playground using React Flow and the Web Audio API. We'll start from scratch, first learning about the Web Audio API before looking at how to handle many common scenarios in React Flow: state management, implementing custom nodes, and adding interactivity.

<figure class="my-8 mx-0 sm:-mx-[min(calc((100vw-768px)/2),12rem)]">
<img src="/_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fbleep-cafe.png&amp;w=3840&amp;q=75" class="w-full h-auto rounded-xl" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" sizes="100vw" srcset="/_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fbleep-cafe.png&amp;w=640&amp;q=75 640w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fbleep-cafe.png&amp;w=750&amp;q=75 750w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fbleep-cafe.png&amp;w=828&amp;q=75 828w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fbleep-cafe.png&amp;w=1080&amp;q=75 1080w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fbleep-cafe.png&amp;w=1200&amp;q=75 1200w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fbleep-cafe.png&amp;w=1920&amp;q=75 1920w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fbleep-cafe.png&amp;w=2048&amp;q=75 2048w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fbleep-cafe.png&amp;w=3840&amp;q=75 3840w" width="0" height="0" alt="A screenshot of bleep.cafe, a visual audio programming environment. In it, there are four nodes connected together: an xy pad, an oscillator node, a volume node, and a master output." />
<figcaption>This is bleep.cafe. We're going to learn everything we need to know to build something just like it!</figcaption>
</figure>

A while back I shared a project I was working on to the React Flow [discord server ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://discord.com/invite/RVmnytFmGW). It's called [bleep.cafe ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://bleep.cafe) and it's a little web app for learning digital synthesis all inside the browser. A lot of folks were interested to see how something like that was put together: most people don't even know **their browser has a whole synth engine built in!**

This tutorial will take us step-by-step to build something similar. We may skip over some bits here and there, but for the most part if you're new to React Flow *or* the Web Audio API you should be able to follow along and have something working by the end.

If you're already a React Flow wizard you might want to read the first section covering the Web Audio API and then jump to the third to see how things are tied together!

But first...

## A demo\![](#a-demo) 

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik02LjQ1NyAxLjA0N2MuNjU5LTEuMjM0IDIuNDI3LTEuMjM0IDMuMDg2IDBsNi4wODIgMTEuMzc4QTEuNzUgMS43NSAwIDAgMSAxNC4wODIgMTVIMS45MThhMS43NSAxLjc1IDAgMCAxLTEuNTQzLTIuNTc1Wm0xLjc2My43MDdhLjI1LjI1IDAgMCAwLS40NCAwTDEuNjk4IDEzLjEzMmEuMjUuMjUgMCAwIDAgLjIyLjM2OGgxMi4xNjRhLjI1LjI1IDAgMCAwIC4yMi0uMzY4Wm0uNTMgMy45OTZ2Mi41YS43NS43NSAwIDAgMS0xLjUgMHYtMi41YS43NS43NSAwIDAgMSAxLjUgMFpNOSAxMWExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDBaIiAvPjwvc3ZnPg==)

This and other examples in this tutorial *make sound*. To avoid creating an avant-garde masterpiece, remember to mute each example before moving on!

## The Web Audio API[](#the-web-audio-api) 

Before we get stuck in to React Flow and interactive node editor goodness, we need to take a crash course on the [Web Audio API ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API). Here are the highlights you need to know:

- The Web Audio API provides a variety of different audio nodes, including sources (e.g. [OscillatorNode ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://developer.mozilla.org/en-US/docs/Web/API/OscillatorNode), [MediaElementAudioSourceNode ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://developer.mozilla.org/en-US/docs/Web/API/MediaElementAudioSourceNode)), effects (e.g. [GainNode ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://developer.mozilla.org/en-US/docs/Web/API/GainNode), [DelayNode ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://developer.mozilla.org/en-US/docs/Web/API/DelayNode), [ConvolverNode ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://developer.mozilla.org/en-US/docs/Web/API/ConvolverNode)), and outputs (e.g. [AudioDestinationNode ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://developer.mozilla.org/en-US/docs/Web/API/AudioDestinationNode)).
- Audio nodes can be connected together to form a (potentially cyclic) graph. We tend to call this the audio-processing graph, signal graph, or signal chain.
- Audio processing is handled in a separate thread by native code. This means we can keep generating sounds even when the main UI thread is busy or blocked.
- An [AudioContext ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext) acts as the brain of an audio-processing graph. We can use it to create new audio nodes and suspend or resume audio processing entirely.

### Hello, sound\![](#hello-sound) 

Let's see some of this stuff in action and build our first Web Audio app! We won't be doing anything too wild: we'll make a simple mouse [theremin ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](http://www.thereminworld.com/Article/14232/what-s-a-theremin-). We'll use React for these examples and everything else moving forward (we're called React Flow after all!) and [`vite`](https://vitejs.dev) to handle bundling and hot reloading.

If you prefer another bundler like parcel or Create React App that's cool too, they all do largely the same thing. You could also choose to use TypeScript instead of JavaScript. To keep things simple we won't use it today, but React Flow is fully typed (and written entirely in TypeScript) so it's a breeze to use!

npm

pnpm

yarn

bun

``` 
npm create vite@latest -- --template react
```

``` 
npm create vite@latest -- --template react
# couldn't auto-convert command
```

``` 
npm create vite@latest -- --template react
# couldn't auto-convert command
```

``` 
bunx create-vite@latest --template react
```

Vite will scaffold out a simple React application for us, but can delete the assets and jump right into `App.jsx`. Remove the demo component generated for us and start by creating a new AudioContext and putting together the nodes we need. We want an OscillatorNode to generate some tones and a GainNode to control the volume.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/App.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
// Create the brain of our audio-processing graph
const context = new AudioContext();
 
// Create an oscillator node to generate tones
const osc = context.createOscillator();
 
// Create a gain node to control the volume
const amp = context.createGain();
 
// Pass the oscillator's output through the gain node and to our speakers
osc.connect(amp);
amp.connect(context.destination);
 
// Start generating those tones!
osc.start();
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Oscillator nodes need to be started.

Don't forget that call to `osc.start`. The oscillator won't start generating tones without it!

For our app, we'll track the mouse's position on the screen and use that to set the pitch of the oscillator node and the volume of the gain node.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/App.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import React from 'react';
 
const context = new AudioContext();
const osc = context.createOscillator();
const amp = context.createGain();
 
osc.connect(amp);
amp.connect(context.destination);
 
osc.start();
 
const updateValues = (e) => ;
 
export default function App() } onMouseMove= />;
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

`osc.frequency.value`, `amp.gain.value`...

The Web Audio API makes a distinction between simple object properties and audio node *parameters*. That distinction appears in the form of an `AudioParam`. You can read up on them in the [MDN docs ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://developer.mozilla.org/en-US/docs/Web/API/AudioParam) but for now it's enough to know that you need to use `.value` to set the value of an `AudioParam` rather than just assigning a value to the property directly.

If you try this example as it is, you'll probably find that nothing happens. An AudioContext often starts in a suspended state in an attempt to avoid ads hijacking our speakers. We can fix that easily by adding a click handler on the `<div />` to resume the context if it's suspended.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/App.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
const toggleAudio = () =>  else 
};
 
export default function App() 
    />
  );
};
```

And that's everything we need to start making some sounds with the Web Audio API! Here's what we put together, in case you weren't following along at home:

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

Now let's put this knowledge to one side and take a look at how to build a React Flow project from scratch.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Already a React Flow pro? If you're already familiar with React Flow, you can comfortably skip over the next section and head straight on over to [making some sounds](#do-sound-to-it). For everyone else, let's take a look at how to build a React Flow project from scratch.

## Scaffolding a React Flow project[](#scaffolding-a-react-flow-project) 

Later on we'll take what we've learned about the Web Audio API, oscillators, and gain nodes and use React Flow to interactively build audio-processing graphs. For now though, we need to put together an empty React Flow app.

We already have a React app set up with Vite, so we'll keep using that. If you skipped over the last section, we ran `npm create vite@latest -- --template react` to get started. You can use whatever bundler and/or dev server you like, though. Nothing here is vite specific.

We only need three additional dependencies for this project: `@xyflow/react` for our UI (obviously!), `zustand` as our simple state management library (that's what we use under the hood at React Flow) and `nanoid` as a lightweight id generator.

npm

pnpm

yarn

bun

``` 
npm install @xyflow/react zustand nanoid
```

``` 
pnpm add @xyflow/react zustand nanoid
```

``` 
yarn add @xyflow/react zustand nanoid
```

``` 
bun add @xyflow/react zustand nanoid
```

We're going to remove everything from our Web Audio crash course and start from scratch. Start by modifying `main.jsx` to match the following:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/main.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import App from './App';
import React from 'react';
import ReactDOM from 'react-dom/client';
import  from '@xyflow/react';
 
// 👇 Don't forget to import the styles!
import '@xyflow/react/dist/style.css';
import './index.css';
 
const root = document.querySelector('#root');
 
ReactDOM.createRoot(root).render(
  <React.StrictMode>
    
    <div style=}>
      <ReactFlowProvider>
        <App />
      </ReactFlowProvider>
    </div>
  </React.StrictMode>,
);
```

There are three important things to pay attention to here:

1.  You need to remember to **import the React Flow CSS styles** to make sure everything works correctly.
2.  The React Flow renderer needs to be inside an element with a known height and width, so we've set the containing `<div />` to take up the entire screen.
3.  To use some of the hooks React Flow provides, your components need to be inside a `<ReactFlowProvider />` or inside the `<ReactFlow />` component itself, so we've wrapped the entire app in the provider to be sure.

Next, hop into `App.jsx` and create an empty flow:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/App.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import React from 'react';
import  from '@xyflow/react';
 
export default function App() 
```

We'll expand and add on to this component over time. For now, we've added one of React Flow's built-in components - [`<Background />`](/api-reference/components/background) - to check if everything is setup correctly. Go ahead and run `npm run dev` (or whatever you need to do to spin up a dev server if you didn't choose vite) and check out your browser. You should see an empty flow:

<figure class="my-8 mx-0">
<img src="/_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fempty-flow.png&amp;w=3840&amp;q=75" class="w-full h-auto rounded-xl" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" sizes="100vw" srcset="/_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fempty-flow.png&amp;w=640&amp;q=75 640w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fempty-flow.png&amp;w=750&amp;q=75 750w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fempty-flow.png&amp;w=828&amp;q=75 828w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fempty-flow.png&amp;w=1080&amp;q=75 1080w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fempty-flow.png&amp;w=1200&amp;q=75 1200w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fempty-flow.png&amp;w=1920&amp;q=75 1920w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fempty-flow.png&amp;w=2048&amp;q=75 2048w, /_next/image?url=%2Fimg%2Ftutorials%2Fwebaudio%2Fempty-flow.png&amp;w=3840&amp;q=75 3840w" width="0" height="0" alt="Screenshot of an empty React Flow graph" />
</figure>

Leave the dev server running. We can keep checking back on our progress as we add new bits and bobs.

### 1. State management with Zustand[](#1-state-management-with-zustand) 

A Zustand store will hold all the UI state for our application. In practical terms that means it'll hold the nodes and edges of our React Flow graph, a few other pieces of state, and a handful of *actions* to update that state.

To get a basic interactive React Flow graph going we need three actions:

1.  `onNodesChange` to handle nodes being moved around or deleted.
2.  `onEdgesChange` to handle *edges* being moved around or deleted.
3.  `addEdge` to connect two nodes in the graph.

Go ahead and create a new file, `store.js`, and add the following:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/store.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from '@xyflow/react';
import  from 'nanoid';
import  from 'zustand/traditional';
 
export const useStore = createWithEqualityFn((set, get) => ();
  },
 
  onEdgesChange(changes) );
  },
 
  addEdge(data) ;
 
    set();
  },
}));
```

Zustand is dead simple to use. We create a function that receives both a `set` and a `get` function and returns an object with our initial state along with the actions we can use to update that state. Updates happen immutably and we can use the `set` function for that. The `get` function is how we read the current state. And... that's it for zustand.

The `changes` argument in both `onNodesChange` and `onEdgesChange` represents events like a node or edge being moved or deleted. Fortunately, React Flow provides some [helper](/api-reference/utils/apply-node-changes) [functions](/api-reference/utils/apply-edge-changes) to apply those changes for us. We just need to update the store with the new array of nodes.

`addEdge` will be called whenever two nodes get connected. The `data` argument is *almost* a valid edge, it's just missing an id. Here we're getting nanoid to generate a 6 character random id and then adding the edge to our graph, nothing exciting.

If we hop back over to our `<App />` component we can hook React Flow up to our actions and get something working.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/App.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import React from 'react';
import  from '@xyflow/react';
import  from 'zustand/shallow';
 
import  from './store';
 
const selector = (store) => ();
 
export default function App() 
      edges=
      onNodesChange=
      onEdgesChange=
      onConnect=
    >
      <Background />
    </ReactFlow>
  );
}
```

So what's this `selector` thing all about? Zustand let's us supply a selector function to pluck out the exact bits of state we need from the store. Combined with the `shallow` equality function, this means we typically don't have re-renders when state we don't care about changes.

Right now, our store is small and we actually want everything from it to help render our React Flow graph, but as we expand on it this selector will make sure we're not re-rendering *everything* all the time.

This is everything we need to have an interactive graph: we can move nodes around, connect them together, and remove them. To demonstrate, *temporarily* add some dummy nodes to your store:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./store.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
const useStore = createWithEqualityFn((set, get) => (, position:  },
    , position:  },
    , position:  }
  ],
  ...
}));
```

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

### 2. Custom nodes[](#2-custom-nodes) 

OK great, we have an interactive React Flow instance we can start playing with. We added some dummy nodes but they're just the default unstyled ones right now. In this step we'll add three custom nodes with interactive controls:

1.  An oscillator node and controls for the pitch and waveform type.
2.  A gain node and a control for the volume
3.  An output node and a button to toggle audio processing on and off.

Let's create a new folder, `nodes/`, and create a file for each custom node we want to create. Starting with the oscillator we need two controls and a source handle to connect the output of the oscillator to other nodes.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/nodes/Osc.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import React from 'react';
import  from '@xyflow/react';
 
import  from '../store';
 
export default function Osc()  />
          <span>Hz</span>
        </label>
 
        <label>
          <span>Waveform</span>
          <select className="nodrag" value=>
            <option value="sine">sine</option>
            <option value="triangle">triangle</option>
            <option value="sawtooth">sawtooth</option>
            <option value="square">square</option>
          </select>
      </div>
 
      <Handle type="source" position="bottom" />
    </div>
  );
};
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

"nodrag" is important.

Pay attention to the `"nodrag"` class being added to both the `<input />` and `<select />` elements. It's *super important* that you remember to add this class otherwise you'll find that React Flow intercepts the mouse events and you'll be stuck dragging the node around forever!

If we try rendering this custom node we'll find that the inputs don't do anything. That's because the input values are fixed by `data.frequency` and `data.type` but we have no event handlers listening to changes and no mechanism to update a node's data!

To fix the situation we need to jump back to our store and add an `updateNode` action:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/store.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
export const useStore = createWithEqualityFn((set, get) => ( }
          : node
      )
    });
  },
 
  ...
}));
```

This action will handle partial data updates, such that if we only want to update a node's `frequency`, for example, we could just call `updateNode(id, `. Now we just need to bring the action into our `<Osc />` component and call it whenever an input changes.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/nodes/Osc.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import React from 'react';
import  from '@xyflow/react';
import  from 'zustand/shallow';
 
import  from '../store';
 
const selector = (id) => (store) => (),
  setType: (e) => store.updateNode(id, ),
});
 
export default function Osc()  = useStore(selector(id), shallow);
 
  return (
    <div>
      <div>
        <p>Oscillator Node</p>
 
        <label>
          <span>Frequency:</span>
          <input
            className="nodrag"
            type="range"
            min="10"
            max="1000"
            value=
            onChange=
          />
          <span>Hz</span>
        </label>
 
        <label>
          <span>Waveform:</span>
          <select className="nodrag" value= onChange=>
            <option value="sine">sine</option>
            <option value="triangle">triangle</option>
            <option value="sawtooth">sawtooth</option>
            <option value="square">square</option>
          </select>
        </label>
      </div>
 
      <Handle type="source" position="bottom" />
    </div>
  );
}
```

Hey, that `selector` is back! Notice how this time we're using it to derive two event handlers, `setFrequency` and `setType`, from the general `updateNode` action.

The last piece of the puzzle is to tell React Flow how to render our custom node. For that we need to create a `nodeTypes` object: the keys should correspond to a node's `type` and the value will be the React component to render.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/App.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import React from 'react';
import  from '@xyflow/react';
import  from 'zustand/shallow';
 
import  from './store';
import Osc from './nodes/Osc';
 
const selector = (store) => ();
 
const nodeTypes = ;
 
export default function App() 
      nodeTypes=
      edges=
      onNodesChange=
      onEdgesChange=
      onConnect=
    >
      <Background />
    </ReactFlow>
  );
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Avoid unnecessary renders.

It's important to define `nodeTypes` outside of the `<App />` component (or use React's [`useMemo`](https://react.dev/reference/react/useMemo)) to avoid recomputing it every render.

If you've got the dev server running, don't panic if things haven't changed yet! None of our temporary nodes have been given the right type yet, so React Flow just falls back to rendering the default node. If we change one of those nodes to be an `osc` with some initial values for `frequency` and `type` we should see our custom node being rendered.

``` 
const useStore = createWithEqualityFn((set, get) => (,
      position: 
    },
    ...
  ],
  ...
}));
```

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Stuck on styling?

If you're just implementing the code from this post as you go along, you'll see that your custom node doesn't look like the one in the preview above. To keep things easy to digest, we've left out styling in the code snippets.

To learn how to style your custom nodes, check out our docs on [theming](/learn/customization/theming) or our example using [Tailwind](/examples/styling/tailwind).

Implementing a gain node is pretty much the same process, so we'll leave that one to you. Instead, we'll turn our attention to the output node. This node will have no parameters control, but we do want to toggle signal processing on and off. That's a bit difficult right now when we haven't implemented any audio code yet, so in the meantime we'll add just a flag to our store and an action to toggle it.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/store.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
const useStore = createWithEqualityFn((set, get) => ();
  },
 
  ...
}));
```

The custom node itself is then pretty simple:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/nodes/Out.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import React from 'react';
import  from '@xyflow/react';
import  from 'zustand/shallow';
import  from '../store';
 
const selector = (store) => ();
 
export default function Out()  = useStore(selector, shallow);
 
  return (
    <div>
      <Handle type="target" position="top" />
 
      <div>
        <p>Output Node</p>
 
        <button onClick=>
          
        </button>
      </div>
    </div>
  );
}
```

Things are starting to shape up quite nicely!

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

The next step, then, is to...

## Do sound to it[](#do-sound-to-it) 

We have an interactive graph and we're able to update node data, now let's add in what we know about the Web Audio API. Start by creating a new file, `audio.js`, and create a new audio context and an empty `Map`.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/audio.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
const context = new AudioContext();
const nodes = new Map();
```

The way we'll manage our audio graph is by hooking into the different actions in our store. So we might connect two audio nodes when the `addEdge` action is called, or update an audio node's properties when `updateNode` is called, and so on.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik02LjQ1NyAxLjA0N2MuNjU5LTEuMjM0IDIuNDI3LTEuMjM0IDMuMDg2IDBsNi4wODIgMTEuMzc4QTEuNzUgMS43NSAwIDAgMSAxNC4wODIgMTVIMS45MThhMS43NSAxLjc1IDAgMCAxLTEuNTQzLTIuNTc1Wm0xLjc2My43MDdhLjI1LjI1IDAgMCAwLS40NCAwTDEuNjk4IDEzLjEzMmEuMjUuMjUgMCAwIDAgLjIyLjM2OGgxMi4xNjRhLjI1LjI1IDAgMCAwIC4yMi0uMzY4Wm0uNTMgMy45OTZ2Mi41YS43NS43NSAwIDAgMS0xLjUgMHYtMi41YS43NS43NSAwIDAgMSAxLjUgMFpNOSAxMWExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDBaIiAvPjwvc3ZnPg==)

Hardcoded nodes

We hardcoded a couple of nodes in our store earlier on in this post but our audio graph doesn't know anything about them! For the finished project we can do away with all these hardcoded bits, but for now it's **really important** that we also hardcode some audio nodes.

Here's how we did it:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/audio.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
const context = new AudioContext();
const nodes = new Map();
 
const osc = context.createOscillator();
osc.frequency.value = 220;
osc.type = 'square';
osc.start();
 
const amp = context.createGain();
amp.gain.value = 0.5;
 
const out = context.destination;
 
nodes.set('a', osc);
nodes.set('b', amp);
nodes.set('c', out);
```

### 1. Node changes[](#1-node-changes) 

Right now, there are two types of node changes that can happen in our graph and that we need to respond to: updating a node's `data`, and removing a node from the graph. We already have an action for the former, so let's handle that first.

In `audio.js` we'll define a function, `updateAudioNode`, that we'll call with a node's id and a partial `data` object and use it to update an existing node in the `Map`:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/audio.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
export function updateAudioNode(id, data)  else 
  }
}
```

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIuOGVtIiBjbGFzcz0ieDptdC1bLjNlbV0iPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMSAxIDE2IDBBOCA4IDAgMCAxIDAgOFptOC02LjVhNi41IDYuNSAwIDEgMCAwIDEzIDYuNSA2LjUgMCAwIDAgMC0xM1pNNi41IDcuNzVBLjc1Ljc1IDAgMCAxIDcuMjUgN2gxYS43NS43NSAwIDAgMSAuNzUuNzV2Mi43NWguMjVhLjc1Ljc1IDAgMCAxIDAgMS41aC0yYS43NS43NSAwIDAgMSAwLTEuNWguMjV2LTJoLS4yNWEuNzUuNzUgMCAwIDEtLjc1LS43NVpNOCA2YTEgMSAwIDEgMSAwLTIgMSAxIDAgMCAxIDAgMloiIC8+PC9zdmc+)

Remember that properties on an audio node may be special `AudioParams` that must be updated differently to regular object properties.

Now we'll want to update our `updateNode` action in the store to call this function as part of the update:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/store.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from './audio';
 
export const useStore = createWithEqualityFn((set, get) => ();
  },
 
  ...
}));
 
```

The next change we need to handle is removing a node from the graph. If you select a node in the graph and hit backspace, React Flow will remove it. This is implicitly handled for us by the `onNodesChange` action we hooked up, but now we want some additional handling we'll need to wire up a new action to React Flow's `onNodesDelete` event.

This is actually pretty simple, so I'll save you some reading and present the next three snippets of code without comment.

./src/audio.js

./src/store.js

./src/App.jsx

### ./src/audio.js 

``` 
export function removeAudioNode(id) 
```

### ./src/store.js 

``` 
import  from './audio';
 
export const useStore = createWithEqualityFn((set, get) => ( of nodes) 
  },
 
  ...
}));
```

### ./src/App.jsx 

``` 
const selector = store => ();
 
export default function App() 
      ...
    >
      <Background />
    </ReactFlow>
  )
};
```

The only thing to note is that `onNodesDelete` calls the provided callback with an *array* of deleted nodes, because it is possible to delete more than one node at once!

### 2. Edge changes[](#2-edge-changes) 

We're getting super close to actually making some sounds! All that's left is to handle changes to our graph's edges. Like with node changes, we already have an action to handle creating new edges and we're also implicitly handling removed edges in `onEdgesChange`.

To handle new connections, we just need the `source` and `target` ids from the edge created in our `addEdge` action. Then we can just look up the two nodes in our `Map` and connect them up.

./src/audio.js

./src/store.js

### ./src/audio.js 

``` 
export function connect(sourceId, targetId) 
```

### ./src/store.js 

``` 
import  from './audio';
 
export const useStore = createWithEqualityFn((set, get) => (,
 
  ...
}));
```

We saw React Flow accepted an `onNodesDelete` handler and wouldn't you know it, there's an `onEdgesDelete` handler too! The approach we'd take to implement `disconnect` and hook it up to our store and React Flow instance is pretty much the same as before, so we'll leave that one down to you as well!

### 3. Switching the speakers on[](#3-switching-the-speakers-on) 

You'll remember that our `AudioContext` probably begins in a suspended state to prevent potentially annoying autoplay issues. We already faked the data and actions we need for our `<Out />` component in the store, now we just need to replace them with the real context's state and resume/suspend methods.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/audio.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
export function isRunning() 
 
export function toggleAudio() 
```

Although we haven't been returning anything from our audio functions up until now, we need to return from `toggleAudio` because those methods are asynchronous and we don't want to update the store prematurely!

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/store.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from './audio'
 
export const useStore = createWithEqualityFn((set, get) => ();
    });
  }
}));
```

Et voilà, we did it! We've now put enough together to actually *make sounds*! Let's see what we have in action.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

### 4. Creating new nodes[](#4-creating-new-nodes) 

Up until now we have been dealing with a hard-coded set of nodes in our graph. This has been fine for prototyping but for it to actually be useful we'll want a way to add new nodes to the graph dynamically. Our final task will be adding this functionality: we'll work backwards starting with the audio code and ending by creating a basic toolbar.

Implementing a `createAudioNode` function will be simple enough. All we need is an id for the new node, the type of node to create, and its initial data:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/audio.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
export function createAudioNode(id, type, data) 
 
    case 'amp': 
  }
}
```

Next we'll need a `createNode` function in our store. The node id will be generated by nanoid and we'll hardcode some initial data for each of the node types, so the only thing we need to pass in is the type of node to create:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgaGVpZ2h0PSIxZW0iIGNsYXNzPSJ4Om1heC13LTYgeDpzaHJpbmstMCI+PHBhdGggZD0iTTIxLjgxODIgMEgyLjE4MTgyQzAuOTc2MzY0IDAgMCAwLjk3NjM2NCAwIDIuMTgxODJWMjEuODE4MkMwIDIzLjAyMzYgMC45NzYzNjQgMjQgMi4xODE4MiAyNEgyMS44MTgyQzIzLjAyMzYgMjQgMjQgMjMuMDIzNiAyNCAyMS44MTgyVjIuMTgxODJDMjQgMC45NzYzNjQgMjMuMDIzNiAwIDIxLjgxODIgMFpNMTIgMTcuODY5MUMxMiAxOS44MDc2IDEwLjgxMDkgMjAuODk0MiA4LjgzNjM2IDIwLjg5NDJDNi44ODU4MiAyMC44OTQyIDUuNjQzMjcgMTkuNzU0MiA1LjY0MzI3IDE3LjkxMDVINy43NTYzNkM3Ljc2MTgyIDE4LjU5NDUgOC4xNjk4MiAxOS4wMjY1IDguODAwMzYgMTkuMDI2NUM5LjQ0ODM2IDE5LjAyNjUgOS43OTYzNiAxOC42MTg1IDkuNzk2MzYgMTcuODUwNVYxMS45OTc4SDEyVjE3Ljg2OTFaTTE3Ljk3OTMgMjAuODk0MkMxNS43ODc2IDIwLjg5NDIgMTQuNDA4NyAxOS44NjIyIDE0LjM3MTYgMTguMTkzMUgxNi40NzI3QzE2LjUyNjIgMTguODIzNiAxNy4xNTU2IDE5LjIyNTEgMTguMDY4NyAxOS4yMjUxQzE4Ljg5MTMgMTkuMjI1MSAxOS40NTY0IDE4LjgyOTEgMTkuNDU2NCAxOC4yNTg1QzE5LjQ1NjQgMTcuNzc4NSAxOS4wNzc4IDE3LjUyIDE4LjA4NzMgMTcuMzIyNUwxNi45NDczIDE3LjA5NDVDMTUuMzYyMiAxNi43OTQ1IDE0LjU0NjIgMTUuOTMwNSAxNC41NDYyIDE0LjU2OEMxNC41NDYyIDEyLjg3NDkgMTUuOTAzMyAxMS43NjQ0IDE3Ljk5MTMgMTEuNzY0NEMyMC4wMjA0IDExLjc2NDQgMjEuNDI0NCAxMi44NjI5IDIxLjQ2MDQgMTQuNDY1NUgxOS40MjU4QzE5LjM3NzggMTMuODUzNSAxOC43OTUzIDEzLjQyNjkgMTguMDE5NiAxMy40MjY5QzE3LjI0NjIgMTMuNDI2OSAxNi43MzY3IDEzLjc5MzUgMTYuNzM2NyAxNC4zNjk1QzE2LjczNjcgMTQuODQ0IDE3LjEyMDcgMTUuMTIgMTguMDMyNyAxNS4zTDE5LjE0NzYgMTUuNTE2QzIwLjg1OTMgMTUuODQ2NSAyMS42MjczIDE2LjYyIDIxLjYyNzMgMTcuOTk0NUMyMS42Mjg0IDE5LjgwMjIgMjAuMjQ4NCAyMC44OTQyIDE3Ljk3OTMgMjAuODk0MloiIC8+PC9zdmc+)[./src/store.js]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
import  from './audio';
 
export const useStore = createWithEqualityFn((set, get) => (;
        const position = ;
 
        createAudioNode(id, type, data);
        set(] });
 
        break;
      }
 
      case 'amp': ;
        const position = ;
 
        createAudioNode(id, type, data);
        set(] });
 
        break;
      }
    }
  }
}));
```

We could be a bit smarter about calculating the position of the new node, but to keep things simple we'll just hardcode it to `` for now.

The final piece of the puzzle is to create a toolbar component that can trigger the new `createNode` action. To do that we'll jump back to `App.jsx` and make use of the [`<Panel />`](/docs/api-reference/components/panel) built-in component.

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/App.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
...
import  from '@xyflow/react';
...
 
const selector = (store) => ();
 
export default function App() ;
```

We don't need anything fancy here, just a couple of buttons that trigger the `createNode` action with the appropriate type:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSItMTAuNSAtOS40NSAyMSAxOC45IiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZT0iY3VycmVudENvbG9yIiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6bWF4LXctNiB4OnNocmluay0wIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iMiIgc3Ryb2tlPSJub25lIj48L2NpcmNsZT48ZyBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSI+PC9lbGxpcHNlPjxlbGxpcHNlIHJ4PSIxMCIgcnk9IjQuNSIgdHJhbnNmb3JtPSJyb3RhdGUoNjApIj48L2VsbGlwc2U+PGVsbGlwc2Ugcng9IjEwIiByeT0iNC41IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIj48L2VsbGlwc2U+PC9nPjwvc3ZnPg==)[./src/App.jsx]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjIiIGhlaWdodD0iMWVtIiBjbGFzcz0ibmV4dHJhLWNvcHktaWNvbiI+PHJlY3QgeD0iOSIgeT0iOSIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiByeD0iMiIgLz48cGF0aCBkPSJNNSAxNUg0QzIuODk1NDMgMTUgMiAxNC4xMDQ2IDIgMTNWNEMyIDIuODk1NDMgMi44OTU0MyAyIDQgMkgxM0MxNC4xMDQ2IDIgMTUgMi44OTU0MyAxNSA0VjUiIC8+PC9zdmc+)

``` 
<Panel position="top-right">
  <button onClick=>osc</button>
  <button onClick=>amp</button>
</Panel>
```

And that's... everything! We've now got a fully functional audio graph editor that can:

- Create new audio nodes
- Update node data with some UI controls
- Connect nodes together
- Delete nodes and connections
- Start and stop audio processing

Here's the demo from the beginning, but this time you can see the source code to make sure you haven't missed anything.

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNy4yNSA2Ljc1IDIyLjUgMTJsLTUuMjUgNS4yNW0tMTAuNSAwTDEuNSAxMmw1LjI1LTUuMjVtNy41LTMtNC41IDE2LjUiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0ic2l6ZS01IHN0cm9rZS0yIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDAgMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMCAwIDEzLjgwMy0zLjdNNC4wMzEgOS44NjVhOC4yNSA4LjI1IDAgMCAxIDEzLjgwMy0zLjdsMy4xODEgMy4xODJtMC00Ljk5MXY0Ljk5IiAvPjwvc3ZnPg==)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ic2l6ZS00IGZpbGwtc2xhdGUtNzAwIHN0cm9rZS1zbGF0ZS03MDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDU2IDc4Ij48cGF0aCBkPSJNMjMuNDI3MyA0OC4yODUzQzIzLjc5MzEgNDcuNTg0NSAyMy4wNjE0IDQ2Ljg4MzcgMjIuMzI5OCA0Ni44ODM3SDEuMTEyMjhDMC4wMTQ4MjI0IDQ2Ljg4MzcgLTAuMzUwOTk3IDQ1LjgzMjYgMC4zODA2NDIgNDUuMTMxOEw0MC45ODY2IDAuMjgyMDg0QzQxLjcxODIgLTAuNDE4NjkzIDQzLjE4MTUgMC4yODIwODQgNDIuODE1NyAxLjMzMzI1TDMyLjkzODYgMzAuMDY1MUMzMi41NzI3IDMwLjc2NTkgMzIuOTM4NiAzMS40NjY2IDMzLjY3MDIgMzEuNDY2Nkg1NC44ODc3QzU1Ljk4NTIgMzEuNDY2NiA1Ni4zNTEgMzIuNTE3OCA1NS42MTk0IDMzLjIxODZMMTUuMDEzNCA3Ny43MTc5QzE0LjI4MTggNzguNDE4NyAxMi44MTg1IDc3LjcxNzkgMTMuMTg0MyA3Ni42NjY3TDIzLjQyNzMgNDguMjg1M1oiIC8+PC9zdmc+)

## Final thoughts[](#final-thoughts) 

Whew that was a long one, but we made it! For our efforts we've come out the other side with a fun little interactive audio playground, learned a little bit about the Web Audio API along the way, and have a better idea of one approach to "running" a React Flow graph.

If you've made it this far and are thinking "Hayleigh, I'm never going to write a Web Audio app. Did I learn *anything* useful?" Then you're in luck, because you did! You could take our approach to connecting to the Web Audio API and apply it to some other graph-based computation engine like [behave-graph ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/bhouston/behave-graph). In fact, some has done just that and created [behave-flow ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/beeglebug/behave-flow)!

There are still plenty of ways to expand on this project. If you'd like to keep working on it, here are some ideas:

- Add more node types.
- Allow nodes to connect to `AudioParams` on other nodes.
- Use the [`AnalyserNode`](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode) to visualize the output of a node or signal.
- Anything else you can think of!

And if you're looking for inspiration, there are quite a few projects out in the wild that are using node-based UIs for audio things. Some of my favorites are [Max/MSP ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://cycling74.com/products/max/), [Reaktor ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://www.native-instruments.com/en/products/komplete/synths/reaktor-6/), and [Pure Data ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://puredata.info/). Max and Reaktor are closed-source commercial software, but you can still steal some ideas from them [🕵️].

You can use the completed [source code ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/react-flow-web-audio) as a starting point, or you can just keep building on top of what we've made today. We'd love to see what you build so please share it with us over on our [Discord server ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://discord.com/invite/RVmnytFmGW) or [Twitter ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://twitter.com/xyflowdev).

React Flow is an independent company financed by its users. If you want to support us you can [sponsor us on Github ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/sponsors/xyflow) or [subscribe to one of our Pro plans](/pro).

### Get Pro examples, prioritized bug reports, 1:1 support from the maintainers, and more with React Flow Pro 

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0idy01IGgtNSBtci0xIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik05LjgxMyAxNS45MDQgOSAxOC43NWwtLjgxMy0yLjg0NmE0LjUgNC41IDAgMCAwLTMuMDktMy4wOUwyLjI1IDEybDIuODQ2LS44MTNhNC41IDQuNSAwIDAgMCAzLjA5LTMuMDlMOSA1LjI1bC44MTMgMi44NDZhNC41IDQuNSAwIDAgMCAzLjA5IDMuMDlMMTUuNzUgMTJsLTIuODQ2LjgxM2E0LjUgNC41IDAgMCAwLTMuMDkgMy4wOVpNMTguMjU5IDguNzE1IDE4IDkuNzVsLS4yNTktMS4wMzVhMy4zNzUgMy4zNzUgMCAwIDAtMi40NTUtMi40NTZMMTQuMjUgNmwxLjAzNi0uMjU5YTMuMzc1IDMuMzc1IDAgMCAwIDIuNDU1LTIuNDU2TDE4IDIuMjVsLjI1OSAxLjAzNWEzLjM3NSAzLjM3NSAwIDAgMCAyLjQ1NiAyLjQ1NkwyMS43NSA2bC0xLjAzNS4yNTlhMy4zNzUgMy4zNzUgMCAwIDAtMi40NTYgMi40NTZaTTE2Ljg5NCAyMC41NjcgMTYuNSAyMS43NWwtLjM5NC0xLjE4M2EyLjI1IDIuMjUgMCAwIDAtMS40MjMtMS40MjNMMTMuNSAxOC43NWwxLjE4My0uMzk0YTIuMjUgMi4yNSAwIDAgMCAxLjQyMy0xLjQyM2wuMzk0LTEuMTgzLjM5NCAxLjE4M2EyLjI1IDIuMjUgMCAwIDAgMS40MjMgMS40MjNsMS4xODMuMzk0LTEuMTgzLjM5NGEyLjI1IDIuMjUgMCAwIDAtMS40MjMgMS40MjNaIiAvPjwvc3ZnPg==)React Flow Pro](https://reactflow.dev/pro)