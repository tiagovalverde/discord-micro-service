
### Setup
```
virtualenv venv --python=python3
source `venv/bin/activate`
```

### Run

```
export FLASK_APP=app.py
flask run
```

## Docker

`docker build -t tiagovalverde/discord-micro-service:v1 .`
`docker run -p 5050:5000 <id>`


### TODO

- [x] Setup Discord connection
- [x] Add Flask endpoint to receive http requests to send messages from external sources
- [x] Add API_KEY authentication so only other services with a valid API_KEY can send messages
- [ ] Dockerize it
- [ ] Use `DiscordClient` to allow channel user to server interaction (fetch data, update, etc...)