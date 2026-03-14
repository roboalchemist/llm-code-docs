# Source: https://docs.flux.ai/tutorials/components-procurement.md

# PCB Component Procurement in Flux: Real-time Sourcing and Availability

Explore how Flux transforms your PCB component procurement process, giving you the power of an entire procurement team.



## Overview

Failing to secure even a single component can make or break a product launch. The key to reducing risks and ensuring your project can be manufactured is having up-to-date information at every stage:

- **Part Selection:** Include real-time pricing and availability information when choosing your components. [Learn more](#part-selection-finding-the-right-components).
- **During Schematic and PCB Design:** Keep a real-time pulse on your BoM's price and availability to avoid manufacturing roadblocks when the design is done. [Learn more](#during-design-keep-procurement-information-top-of-mind).
- **After Your Design is Ready:** Stay in the loop even after the project is complete to ensure it remains manufacturable at all times. [Learn more](#after-design-is-ready-keeping-your-project-manufacturable).

## Part Selection: Finding the Right Components

When selecting parts for your design, sourcing information might not be the first thing that comes to mind. However, it can be the deciding factor between a manufacturable design and one that's stuck on the drawing board.

Flux provides real-time pricing and availability information right when you're searching for parts in the Library. This means you can make informed decisions about your components on the spot without switching between different tools or websites.

Need more detailed information about pricing and suppliers? Simply drag the edge to expand the library panel to the side to get more information about the parts you're considering.

![](https://uploads.developerhub.io/prod/86Yw/1bnxdowao0wgk8js43sgljmttpetcvttp9h3lnoa2wimq8arqz9r8546w1dkyttw.png)

## During Design: Keep Procurement Information Top-of-Mind

Imagine finishing a design only to discover that some of your parts are no longer in stock. With Flux, you can avoid such surprises by staying proactive about procurement throughout the design process.

### Project-Level Information

Flux provides real-time price information of your total Bill of Materials (BoM) right in the top panel, next to the share menu. This means you can monitor your project's overall procurement status and pricing without leaving your workspace.

You'll find more comprehensive procurement information about your project's BoM in the inspector menu's 'Availability and Pricing' section. This includes everything you need to know to ensure your project stays on track.

![](https://uploads.developerhub.io/prod/86Yw/bvkqnzi0rt1ot4j54fx680qk2h0jjnklqjn2bu8fwz0ykgskhpcn2rhbnw9faslt.png)

#### Set your project's target quantity

If you have decided how many units you plan to manufacture, you can add that information to your project and have Flux calculate your project cost based on volume pricing:

1. Make sure nothing is selected by clicking on an empty section of the schematic editor
2. Click on the "Inspector Menu" in the right and scroll down to find the "Properties" section
3. Click on "Edit" and then "Add"
4. Find the "Manufacturing Quantity Target Property"
5. Click on "Add" and type the number of units you're targeting

All project-level calculations will automatically readjust using the new volume pricing for each component.

### Component-Level Information

Procurement information about individual components is available in the 'Availability and Pricing' when a component is selected. Here you can narrow down your MPN results to a specific DPN, giving you a clear picture of component prices and the overall cost of your components in the different packaging options and across different distributors.

![](https://uploads.developerhub.io/prod/86Yw/vwxyneg1epgt97z9s6whhwo5ljsvj88gnq348l2323kozj5r07nhos89mxf40b3r.png)

## After Design is Ready: Keeping Your Project Manufacturable

Even after your design is complete, the manufacturing process often continues for a long time. It's impossible to predict exactly how many units you'll need to manufacture, and the last thing you want is to be caught off guard by a sudden shortage of components.

Flux sends you periodic email notifications about your project costs and availability. This means you're always in the loop about the status of your components, even long after the design phase is over.

![](https://uploads.developerhub.io/prod/86Yw/q7rmgkx89up9wqkmqjtkvsy75hunhz46y7p8lsedgfjrqs75fn34hjnbjvsd8fee.png)

### Configuring Email Notifications

You can configure email notifications for your projects by adding a few properties to your project. To add a property:

1. Make sure nothing is selected by clicking on an empty section of the schematic editor
2. Click on the "Inspector Menu" in the right and scroll down to find the "Properties" section
3. Click on "Edit" and then "Add"
4. Add any of the properties below

![](https://uploads.developerhub.io/prod/86Yw/2t36jbd68z83j6t3dwb6svi794b0r5klzu520uhjm0gii8t6mkhqqa6g4oh7e3z8.png)

#### Price Change Threshold

Sets the minimum price % change for pricing alerts. For example, setting this property to 1 means you will receive an email notification if your project's total price changes by 1% or more since the last notification.

#### Lead Time Change Threshold

Sets the minimum lead time % change for lead time alerts. For example, setting this property to 5 means you will receive an email notification if any of your project's parts' lead time changes by 5% or more since the last notification.

## Troubleshooting Common Issues

If you're not seeing pricing information for components:

- Verify that the component has a valid Manufacturer Part Number (MPN)
- Check your internet connection, as pricing data requires online access
- Try refreshing the page or reopening the project
- Ensure the component is from a recognized manufacturer