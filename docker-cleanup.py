# -*- coding: utf-8 -*
# remove old images and stopped containers

import docker

client = docker.DockerClient(version='1.24')  # macth the API version with commad ( docker version)

print(client)

container_list = client.containers.list()