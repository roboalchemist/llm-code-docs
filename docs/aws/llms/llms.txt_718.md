# Source: https://docs.aws.amazon.com/routing-control/latest/APIReference/llms.txt

# Amazon Route 53 Application Recovery Controller Routing Control API Reference Guide

> Welcome to the Routing Control (Recovery Cluster) API Reference Guide for Amazon Route 53 Application Recovery Controller.

- [Welcome](https://docs.aws.amazon.com/routing-control/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/routing-control/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/routing-control/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_Operations.html)

- [GetRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_GetRoutingControlState.html): Get the state for a routing control.
- [ListRoutingControls](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_ListRoutingControls.html): List routing control names and Amazon Resource Names (ARNs), as well as the routing control state for each routing control, along with the control panel name and control panel ARN for the routing controls.
- [UpdateRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlState.html): Set the state of the routing control to reroute traffic.
- [UpdateRoutingControlStates](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStates.html): Set multiple routing control states.


## [Data Types](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_Types.html)

- [RoutingControl](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_RoutingControl.html): A routing control, which is a simple on/off switch that you can use to route traffic to cells.
- [UpdateRoutingControlStateEntry](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStateEntry.html): A routing control state entry.
- [ValidationExceptionField](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_ValidationExceptionField.html): There was a validation error on the request.
