# intelligence-task-manager

## Database (Docker)

```bash
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=intelligence_db -p 3306:3306 mysql:8.0
```

## Run

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
