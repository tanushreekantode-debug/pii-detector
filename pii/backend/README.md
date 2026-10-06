# PII Detector Backend

Flask API plus the built React frontend.

## Endpoints

- `GET /` - serves the React frontend when `static/index.html` exists.
- `GET /health` - health check.
- `POST /api/scan` - upload one supported file using form field `file`.

Maximum upload size is 10 MB.
