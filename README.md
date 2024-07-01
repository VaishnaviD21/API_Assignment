Requirements-
- Docker(https://www.docker.com/products/docker-desktop/)
- Docker Compose

Setup and Run-

docker-compose up --build

Endpoints
- Register: `POST /api/register/`
- Login: `POST /api/login/`
- Refresh Token: `POST /api/token/refresh/`
- Logout: `POST /api/logout/`

CURL Commands
- Register:
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"password", "email":"testuser@example.com"}' http://127.0.0.1:8000/api/register/

- Obtain Token:
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"password"}' http://127.0.0.1:8000/api/login/

- Refresh Token:
curl -X POST -H "Content-Type: application/json" -d '{"refresh":"<refresh_token>"}' http://127.0.0.1:8000/api/token/refresh/

- Logout:
curl -X POST -H "Content-Type: application/json" -d '{"refresh":"<refresh_token>"}' http://127.0.0.1:8000/api/logout/
