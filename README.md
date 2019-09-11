# chaos-scimmia
 Chaos Engineering for Redis

## What is where

There's a ci folder: the contents get build into a docker image for use in concourse pipelines. 
There's a concourse pipeline for building that docker image.
There's another concourse pipeline for running it, on a time resource so it runs every 2 minutes. It's a sanity check for now.

The new approach is an app called "continuous redis" in the test-apps folder; it makes an AJAX call to ping a redis backend, saving a timestamp every two seconds. Then it adds DIVs with the diff of the latest two timestamps. (It also adds a bunch with ERROR divs).
