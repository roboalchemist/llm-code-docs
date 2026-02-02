# versioncontrol

Source: https://developer.ui.com/site-manager/v1.0.0/versioncontrol

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

Available Endpoints

There are two versions of the Site Manager API:

Official (v1): Fully-stable and backward compatible APIs with long-term support.
Endpoint: https://api.ui.com/v1/...
Early Access (EA): APIs that have undergone extensive testing but are still in the evaluation and feedback phase. These may be enhanced based on user input.
Endpoint: https://api.ui.com/ea/...
Backward Compatibility

When an EA endpoint is promoted to Official (e.g., api.ui.com/ea/ → api.ui.com/v1/), your existing integration using the EA endpoint will continue to function as expected — no immediate changes required.

Optional fields during EA

In the Early Access version of our APIs, all fields within response.data are considered optional. This flexible design facilitates ongoing iteration and improvement of our API. We strongly recommend building your integrations with this optionality in mind to ensure compatibility with future updates.

Backward-Compatible Changes

The following modifications are considered backward-compatible and may be applied to the API without advance notice:

Adding new API resources or endpoints
Adding new optional request parameters to existing API methods
Adding new properties to existing API responses
Changing the order of properties in existing API responses
Changing the length or format of opaque strings (such as object IDs, error messages, and other human-readable strings)

Best Practice: Design your integration to handle unexpected response structures gracefully, including unfamiliar properties, null values, and missing attributes. Please report any suspected breaking changes via our feedback form.