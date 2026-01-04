# iostpa's api shenanigans

How to run:
Install the necessary packages (with uv its `uv sync` while for pip its `pip install -r requirements.txt` i think) and then run `gunicorn -w 4 -b 0.0.0.0:8000 api:app`, for development run `python3 api`
