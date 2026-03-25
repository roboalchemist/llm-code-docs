# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listenwebsocket.md

# ListenWebSocket 2025.10.9.21

## Bundle

org.apache.nifi | nifi-websocket-processors-nar

## Description

Acts as a WebSocket server endpoint to accept client connections. FlowFiles are transferred to downstream relationships according to received message types as the WebSocket server configured with this processor receives client requests

## Tags

WebSocket, consume, listen, subscribe

## Input Requirement

FORBIDDEN

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| server-url-path | The WetSocket URL Path on which this processor listens to. Must starts with ‘/’, e.g. ‘/example’. |
| websocket-server-controller-service | A WebSocket SERVER Controller Service which can accept WebSocket requests. |

## Relationships

| Name | Description |
| --- | --- |
| binary message | The WebSocket binary message output |
| connected | The WebSocket session is established |
| disconnected | The WebSocket session is disconnected |
| text message | The WebSocket text message output |

## Writes attributes

| Name | Description |
| --- | --- |
| websocket.controller.service.id | WebSocket Controller Service id. |
| websocket.session.id | Established WebSocket session id. |
| websocket.endpoint.id | WebSocket endpoint id. |
| websocket.local.address | WebSocket server address. |
| websocket.remote.address | WebSocket client address. |
| websocket.message.type | TEXT or BINARY. |
