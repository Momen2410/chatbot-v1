## How Run App 

1. Install Requirements.txt

```bash
pip install -r requirements.txt
```

2. Get Gemini-Pro-1.0 API an put it in `.env`

3. run app

```bash
uvicorm main:app
```

4. get response from server `API`

```bash
http://localhost:8000/api/chatbot/v1/chat?question=what is Apple Plant?
```