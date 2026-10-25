# אתר הדמיה – כניסה עם כרטיס דמיוני

## הרצה מקומית
    pip install -r requirements.txt
    python app.py
ואז לפתוח http://localhost:5000

## פרסום ב-Render.com
1. מעלים את התיקייה ל-GitHub (ריפו חדש).
2. ב-Render: New + → Web Service (או Blueprint, כי יש render.yaml) ← בוחרים את הריפו.
3. אם יוצרים ידנית:
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
   - Environment Variable: SECRET_KEY = מחרוזת אקראית כלשהי
4. Deploy – ותקבלו כתובת בסגנון https://card-demo.onrender.com
