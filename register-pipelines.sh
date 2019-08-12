#!/bin/bash

fly -t azureci set-pipeline -p hello-world -c pipeline.yml -l .config.yml
fly -t azureci set-pipeline -p scimmia-images -c ci/pipeline.yml -l .config.yml