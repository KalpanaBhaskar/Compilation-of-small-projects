from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# uv init foldername creates the basic main.py ptoj toml setup etc 
app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2026",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2026",
    },
]

#decorators and routes
@app.get("/")          #, response_class=HTMLResponse, include_in_schema=False)
def home():  #supports sync def - default def , async def
    # return {"message":"Hello World!"}
    return f"<h1>{posts[0]['title']}</h1>"

#commands to run : uv fastapi dev main.py  - includes auto reload ,   uv fastapi run main.py   - in production  ; remove the uv word alone if using pip

@app.get("/api/posts")
def get_posts():
    return posts 