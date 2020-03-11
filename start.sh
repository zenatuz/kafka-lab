#!/bin/bash

docker run -d \
	-e ALLOW_ANONYMOUS_LOGIN=yes \
	bitnami/zookeeper:latest

docker run -d \
	-e ALLOW_PLAINTEXT_LISTENER=yes \
	-e KAFKA_CFG_ZOOKEEPER_CONNECT=10.10.2.113:2181 \
	bitnami/kafka:latest

docker run -it --rm \
	-e KAFKA_CFG_ZOOKEEPER_CONNECT=10.10.2.113:2181 \
	bitnami/kafka:latest kafka-topics.sh --list --zookeeper 10.10.2.113:2181
