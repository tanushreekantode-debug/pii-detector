# PII Detector - AWS Ready

This package contains the React frontend and Flask backend. The final package is designed for a simple single-server AWS deployment: the React build is placed in `backend/static`, and Flask serves both the website and `/api/scan`.

## Local run

### Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m web.app
```

Open `http://localhost:5000`.

### Frontend development (optional)

```powershell
cd frontend
npm install
npm run dev
```

If the frontend is run separately, set `VITE_API_URL` to the backend URL in `frontend/.env.local`.

## AWS single-server deployment

The ZIP already contains the production React build in `backend/static`.

On an Ubuntu AWS EC2 server:

```bash
cd backend
sudo apt update
sudo apt install -y python3 python3-venv tesseract-ocr
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 --workers 2 --timeout 120 web.app:app
```

Open TCP port 5000 in the EC2 security group for testing, then visit:

`http://YOUR_EC2_PUBLIC_IP:5000`

The frontend calls `/api/scan` on the same server, so no Render URL or separate AWS service is required.

## Docker

```bash
cd backend
docker build -t pii-detector .
docker run --rm -p 5000:10000 -e PORT=10000 pii-detector
```

Then open `http://localhost:5000`.
