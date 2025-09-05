# Flap Server

The server for Flap. Contains basic API for retrieving peer information and static website for https://flap.it.com. In the future, we will host our own p2p relay as well.

## Installation

Installing Docker and running `docker compose up` should set up the server. The current HTTP/1 server is bound to `http://localhost:8000`, and the HTTP/3 server is bound to `http://localhost:4433`.
