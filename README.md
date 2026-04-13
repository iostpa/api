# iostpa's api shenanigans

A random API that I made for a friend, now open source.

## How to run

### Manual
Install the necessary packages (with uv its `uv sync` while for pip its `pip install -r requirements.txt` i think) and then run `gunicorn -w 4 -b 0.0.0.0:8000 api:app`, for development run `python3 api`
Note: might be inaccurate since the API uses uv instead of pip now

### Docker
Use the docker-compose.yml file and run it, though I wouldn't recommend since some parts of the API use my domain

## Contribute
Easiest would be to send a list of links in a GitHub issue and I'll add them from there. If you want to also fix my bad code then go ahead.
