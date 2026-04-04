# Source: https://docs.flux.ai/reference/what-s-supported.md

# What's supported?

The Flux API gives you access to Flux documents and the electronics simulation engine. It already contains close to a hundred methods and properties, but it is still very new and there is still more to add.

Some APIs are harder to create than others. There are technical difficulties and security concerns that are not always obvious. Ironing them out will take time. Our #1 priority is to keep Flux stable, when user code is in use, so that it stays the design tool you want to use both now and in the future.

This page is to let you know we're keeping track of requests, and to answer the most common questions of the form "do you have this API?" and "when will you have this API?"

You can help us by sending detailed descriptions of plugins you want to build and how these plugins would use these APIs. This may allow us to design partial solutions that satisfy the needs of most plugin developers.

## Known Limitations

A list of know issues and limitations of the release.

Please report any other issues you come across via the chat in the bottom right or send a email to [team@defygravityinc.com](mailto:team@defygravityinc.com).

### 🏗 Documentation

In some cases there is either documentation missing or the feature the documentation is describing is missing 🤷‍♂️

### 🏗 Limited set of simulator primitives

We are working on expanding to a full set.

### 🏗 Simulator load times

Initialization of the simulator takes a few seconds longer than we'd like it to.

## Planned

### 🕐 No easy way to get node uid's

It a little tricky to get the node uid's right now. Here are some of the ways:

1. Copy the node you want the uid of to the clipboard and paste it to any text editor to get the object in json format. then look for the uid field on the root.
2. Use the flux.print method to print out the nodes from flux.nodes

### 🕐 No easy way to see if parts have simulation model

There is no easy way in the part browser right now to see if a part has a working simulation model.

## Supported

### ✅ Linear DC Analysis

Ability to evaluate the DC currents and DC voltages for a lumped, linear time-invariant circuit.

### ✅ Nonlinear DC Analysis

Ability to obtain the quiescent operating point of a circuit which contains nonlinear elements such as a transistor.

### ✅ Linear transient analysis

Ability to determine the time domain response of a circuit to various input waveforms starting with the initial conditions obtained from the linear dc analysis.

### ✅ Large signal transient analysis

Ability to obtain the time domain response of a circuit which contains nonlinear elements, such as transistors. The time domain responses are determined by considering the various input waveforms starting with the initial conditions obtained from the nonlinear dc analysis.

### ✅ Reading the documents diagram

The API gives you access to all nodes of the diagram and their fields and child nodes.

### ✅ Set and update the atomic simulator models

The API lets you configure and automate a documents underlying atomic simulation model.

### ✅ Reading simulator outputs

The API lets you read voltage and current of any point in the circuit and use it to define a parts behavior or display data to the user.

### ✅ Listen to UI inputs

The API lets you register events to listen to UI input event such as buttons, sliders and other control types to let users interact with your part models.

### ✅ Write Metrics to UI

The API lets write data such as simulator metrics outputs to the Flux UI.

### ✅ Change parts diagram symbol

The API lets you dynamically load different symbols for a part to for example show a switches open/closed states.

### ✅ Display notifications to users

The API lets popup notifications to the user in the UI.

### ✅ Write debug messages to stdout

The API lets write debugging information to the in-app console.

### ✅ Interactivity

Interactive controls for your parts such as push buttons, sliders, etc as I am writing this. 

### ✅ In-app debugging tools

Debugging code without having to resort to your browsers debugging tools.

### ✅ Simulated Circuits can be nested infinite levels deep

Yep, you heard right: documents can be nested infinitely deep....good luck out there ;)

## Coming soon

If there is demand, we are likely to add these in the timespan of a few weeks to a few months.

### 🕐 Plots

Any type of time based circuit requires the ability to visualize data in a time based fashion. We are therefore working on adding powerful Oscilloscope like features.

### 🕐 Linear AC Analysis

Ability to obtain the frequency response of a lumped, linear, time invariant circuit.

### 🕐 Small signal AC analysis

Ability to obtain the frequency domain response of a circuit by replacing nonlinear elements with their linearized equivalents computed from the quiescent operating point.

## Future extensions

_Note: not a roadmap_

These are projects we'd like to do because many people ask for them, but have a lot to consider before they can be done. They could turn to be easy for us to add, but they could also turn out to be big projects. We don't have a timeline on these yet.

### 🗄️ Write changes to the diagram

The current API is simple, you can read the document, you can alter the UI state but you cannot persist changes to the document. We would love to hear about your use cases for being able to persist document changes.

### 🗄️ Import libraries via webpack

Currently the sandbox only gives access to the Flux API as well most of the ES6 globals. We think it could be interesting to allow users to import external libraries and would love to hear from you about use cases.

### 🗄️ Write native micro controller code

The current API enables users to mock microcontrollers but the mock code wouldn't run on the real hardware. We would love to hear about your use-cases for implementing support for native MCU development within Flux.

### 🗄️ Virtual circuits

We realize that the current constraint of only being able to configure one simulator privative per document is limiting and would love to hear from you what use cases its hindering/blocking.