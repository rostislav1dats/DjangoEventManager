# Django Event Manager
Simple project on Django + Django Rest Framework for manage events with JWT user authentification

## Project opportunities
- Registration and authentification users by **JWT** (refresh and access tokens)
- CRUD operations with Events
- Searching and filtering events by:
  - names (`title`)
  - place (`location`)
  - date range (`date`)
- Send email to organizer when event is created (Celery + Redis)
- Swagger and Redoc API documentation
- containirization via Docker and Docker Compose
- WhiteNoise for staticfiles
____________________________
## Technologies
- Django 5.2.9
- Django Rest Framework
- Simple JWT (`djangorestframework_simpleJWT`)
- Celery + Redis
- Docker + Docker Compose
____________________________
## Fast start
### 1. Clone Repository
```bash
git clone <URL_REPO>
cd <PROJECT_ROOT>
```

### 2. Create .env file
# django stuff
SECRET_KEY = <YOUR_DJANGO_SECRET_KEY>

#email stuff  
EMAIL_HOST_USER = <YOUR_EMAIL_HOST_USER>  
EMAIL_HOST_PASSWORD = <YOUR_EMAIL_HOST_PASSWORD>  
DEFAULT_FROM_EMAIL = <YOUR_FROM_EMAIL>  

### 3. Build Docker
```bash
docker compose build --no-cache
```

### 4. Up redis (and Postgres if needed)
```bash
docker compose up -d redis
```
For Postgres
```bash
docker compose up -d db redis
```

### 5. Do migrations
```bash
docker compose run --rm web python manage.py migrate --noinput
```

### 6. Create Superuser
```bash
docker compose run --rm web python manage.py createsuperuser
```

### 7. Up all project
```bash
docker compose up -d
```
and check logs
```bash
docker compose logs -f web
docker compose logs -f celery
docker compose logs -f celery-beat
```
____________________________
## API Documentation 
Swagger UI:
http://localhost:8000/api/docs/swagger/  
Redoc UI:
http://localhost:8000/api/docs/redoc/

## Authentification by JWT
1. Get token (POST request)  
POST `apiuser/register/`  
Request body:  
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```  
Response:  
```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```  
2. Use Access token for authencificated requests  
header  
`Authorization: Bearer <access_token>`  
3. Refresh access token with refresh token  
POST `apiuser/token/refresh`  
Request body:  
```json
{
  "refresh": "<refresh_token>"
}
```  
Response:  
```json  
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```  
## Manage events via API
1. Get events list (only authentificated users)  
GET apievents/events/  
Authorization: Bearer <access_token>  

Searching and filtering:  
- by title `?search=conferation`
- by location `?search=Kyiv`
- filter by date `date_after=2025-12-01&date_before=2025-12-31`
- possibility to combine parameters `/apievents/events/?search=Kyiv&date_after=2025-12-01&date_before=2025-12-31`  
Searching and filtering work via DRF filter and SearchFilter  

2. Get detailed info about event
GET apievents/events/{id}/  
Authorization: Bearer <access_token>  

3. Create event  
POST apievents/events/  
Authorization: Bearer <access_token>  

Request Bogy:  
```json
{
  "title": "IT conferation",
  "description": "new IT technologies and AI",
  "date": "2025-12-20T18:00:00Z",
  "location": "Kyiv"
}
```  

4. Update event  
PUT /apievents/events/{id}/  
PATCH /apievents/events/{id}/  
Authorization: Bearer <access_token>  

5. Delete event  
DELETE /api/events/{id}/  
Authorization: Bearer <access_token>  

## Email notifications  
After creation event organizer receive email with title, date and location of created event  
Work via Celery + Redis  

## Useful links
- [Django](https://www.djangoproject.com)
- [Django Rest Framework](https://www.django-rest-framework.org)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
