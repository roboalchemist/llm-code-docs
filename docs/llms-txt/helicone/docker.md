# Source: https://docs.helicone.ai/getting-started/self-host/docker.md

# Docker

> Deploy Helicone using Docker. Quick setup guide for running a containerized instance of the LLM observability platform on your local machine or server.

To run all services in a single Docker container, you can use the `helicone-all-in-one` image.

Get [Docker](https://docs.docker.com/get-docker/) and run the container:

```bash  theme={null}
docker pull helicone/helicone-all-in-one:v2025.08.08
docker run -d --name helicone-all-in-one -p 3000:3000 -p 8585:8585 -p 5432:5432 -p 8123:8123 -p 9000:9000 helicone/helicone-all-in-one:v2025.08.08
```

## Example to test the Jawn service

```bash  theme={null}
curl --location 'http://localhost:8585/v1/gateway/oai/v1/completions' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer {{OPENAI_API_KEY}}" \
--header "Helicone-Auth: Bearer {{HELICONE_API_KEY}}" \
--data '{
    "model": "gpt-4o-mini",
    "prompt": "Count to 5",
    "stream": false
  }'
```
