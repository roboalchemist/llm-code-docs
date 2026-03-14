# Source: https://docs.edgeimpulse.com/apis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# APIs

Edge Impulse provides several APIs to interact with the platform programmatically. These APIs allow you to automate tasks, integrate with other systems, and build custom applications on top of Edge Impulse's capabilities. Collectively, these APIs are referred to as the Edge Impulse API and you may see the term used interchangeably, specifically when referencing the Studio API.

<Columns cols={4}>
  <Card title="Studio API" img="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/fa-icon-16x9-gears-solid-full.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=162cff40c8c839ea8144b9b49aa41a45" href="/apis/studio" width="1600" height="900" data-path=".assets/images/fa-icon-16x9-gears-solid-full.png" />

  <Card title="Ingestion API" img="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/fa-icon-16x9-gears-solid-full.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=162cff40c8c839ea8144b9b49aa41a45" href="/apis/ingestion" width="1600" height="900" data-path=".assets/images/fa-icon-16x9-gears-solid-full.png" />

  <Card title="Remote Mgmt. API" img="https://mintcdn.com/edgeimpulse/mqaETyKntJOjsP_8/.assets/images/fa-icon-16x9-gears-solid-full.png?fit=max&auto=format&n=mqaETyKntJOjsP_8&q=85&s=162cff40c8c839ea8144b9b49aa41a45" href="/apis/remote-management" width="1600" height="900" data-path=".assets/images/fa-icon-16x9-gears-solid-full.png" />
</Columns>

***

## Studio API

The Studio API exposes most of the Studio functionality, enabling you to manage your projects, datasets, and models programmatically. With the Studio API, you can automate tasks such as uploading data, training models, and deploying your applications.

## Ingestion API

The Ingestion API allows you to send new device data to Edge Impulse. It provides endpoints for uploading training and testing samples for different types of data, including sensor data, images, and audio files.

## Remote Management API

The Remote Management API is a part of the remote management service that Edge Impulse provides. It allows you to control your remote edge devices from Studio, for example to acquire new data.


Built with [Mintlify](https://mintlify.com).