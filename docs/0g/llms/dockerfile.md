# Dockerfile
FROM rust:alpine3.20 as builder

WORKDIR /0g-da-retriever
COPY . .

RUN apk update && apk add --no-cache make protobuf-dev musl-dev
RUN cargo build --release

FROM alpine:3.20

WORKDIR /0g-da-retriever

COPY --from=builder /0g-da-retriever/target/release/retriever /usr/local/bin/retriever