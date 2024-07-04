FastAPI using Postgres and Ormar as an ORM (in Docker)

TODO:
"on_event" is deprecated, use lifespan event handlers instead.

Reference:

Ormar:
https://github.com/collerek/ormar

Prod builds:
use dockerfile - tiangolo/uvicorn-gunicorn:python3.11-slim for prod builds, and Traefik for reverse proxy
check here- https://testdriven.io/blog/fastapi-docker-traefik/