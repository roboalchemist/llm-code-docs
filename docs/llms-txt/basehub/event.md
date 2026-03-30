# Event

> A unique block that enables type-safe data submissions

## Introduction

The Event block is a unique primitive in BaseHub. Playing with its layout and schema, you can go from a simple page view counter to a complex form submissions table.

The events are tracked in real time, so you will see the incoming events no matter the block’s layout.

## Features

*   ✅ Ideal for tracking analytics events or form submissions
    
*   ✅ It can have a type-safe schema, used to render forms or send events through the SDK
    
*   ✅ It can be tracked by [Workflow](https://docs.basehub.com/blocks/primitives/workflow) blocks
    
*   ✅ Events can be exported as CSV
    

## Constraints

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Contraint

Description

Layout

Events can be displayed in either a **Table** view, similar to the [Collection](https://docs.basehub.com/blocks/layout/collection) block, or as a **Time-series** visualization that that draws an area chart showing daily (or hourly) event frequency up to today.

Schema

Defines which columns will be displayed on the Table view, and it’s used to create the type that will be exposed on the BaseHub SDK.  
Useful to correctly ingest events through the SDK. Can also be fetched from the API to render custom [forms](https://docs.basehub.com/extras/forms).

## Examples

*   [Feedback Form](https://docs.basehub.com/templates-and-examples/examples-and-guides/create-a-feedback-form)
    
*   [Newsletter](https://docs.basehub.com/templates-and-examples/examples-and-guides/create-a-newsletter)
    
*   [View Counter](https://docs.basehub.com/templates-and-examples/examples-and-guides/create-a-view-counter)
    
*   [Form Builder](https://docs.basehub.com/templates-and-examples/examples-and-guides/create-a-form-builder)