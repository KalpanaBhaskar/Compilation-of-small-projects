from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Query,
    Path,
    Header,
    Cookie,
    Response,
)

from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
    PlainTextResponse,
    RedirectResponse,
)

from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="FastAPI Learning",
    description="Learning every REST API feature",
    version="1.0.0"
)

############################################################
# Fake Database
############################################################

posts = [
    {
        "id": 1,
        "author": "Corey",
        "title": "FastAPI",
        "content": "Awesome",
        "date_posted": "April 20"
    },
    {
        "id": 2,
        "author": "Jane",
        "title": "Python",
        "content": "Great",
        "date_posted": "April 21"
    }
]

############################################################
# Models
############################################################

class Student(BaseModel):

    id: int

    name: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="Student Name"
    )

    subjects: List[str] = []

class Post(BaseModel):

    id: int

    author: str

    title: str

    content: str

    date_posted: str

############################################################
# HOME
############################################################

@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <h1>Welcome to FastAPI</h1>

    <ul>
        <li><a href="/docs">Swagger UI</a></li>
        <li><a href="/redoc">ReDoc</a></li>
        <li><a href="/api/posts">Posts</a></li>
    </ul>
    """

############################################################
# GET ALL POSTS
############################################################

@app.get("/api/posts", response_model=List[Post])
def get_posts():

    return posts

############################################################
# GET SINGLE POST
############################################################

@app.get("/api/posts/{post_id}")
def get_post(

    post_id: int = Path(..., gt=0)

):

    for post in posts:

        if post["id"] == post_id:
            return post

    raise HTTPException(
        status_code=404,
        detail="Post Not Found"
    )

############################################################
# SEARCH
############################################################

@app.get("/search")
def search(

    keyword: Optional[str] = Query(None),
    author: Optional[str] = Query(None)

):

    result = posts

    if keyword:

        result = [

            p for p in result

            if keyword.lower() in p["title"].lower()

        ]

    if author:

        result = [

            p for p in result

            if author.lower() == p["author"].lower()

        ]

    return result

############################################################
# CREATE POST
############################################################

@app.post(
    "/api/posts",
    status_code=status.HTTP_201_CREATED
)
def create_post(post: Post):

    posts.append(post.model_dump())

    return {
        "message": "Created",
        "post": post
    }

############################################################
# PUT (Replace Entire Object)
############################################################

@app.put("/api/posts/{post_id}")
def update_post(

    post_id: int,

    updated_post: Post

):

    for index, post in enumerate(posts):

        if post["id"] == post_id:

            posts[index] = updated_post.model_dump()

            return updated_post

    raise HTTPException(404, "Post not found")

############################################################
# PATCH (Partial Update)
############################################################

class UpdatePost(BaseModel):

    author: Optional[str] = None

    title: Optional[str] = None

    content: Optional[str] = None

    date_posted: Optional[str] = None


@app.patch("/api/posts/{post_id}")
def patch_post(

    post_id: int,

    patch: UpdatePost

):

    for post in posts:

        if post["id"] == post_id:

            update_data = patch.model_dump(exclude_unset=True)

            post.update(update_data)

            return post

    raise HTTPException(404, "Not Found")

############################################################
# DELETE
############################################################

@app.delete("/api/posts/{post_id}")
def delete_post(post_id: int):

    for index, post in enumerate(posts):

        if post["id"] == post_id:

            deleted = posts.pop(index)

            return {
                "Deleted": deleted
            }

    raise HTTPException(404, "Not Found")

############################################################
# STUDENT
############################################################

@app.post("/students")
async def create_student(student: Student):

    return student

############################################################
# TEXT RESPONSE
############################################################

@app.get(
    "/text",
    response_class=PlainTextResponse
)
def text():

    return "Hello FastAPI"

############################################################
# JSON RESPONSE
############################################################

@app.get("/json")
def json_response():

    return JSONResponse(

        content={
            "message": "Hello",
            "success": True
        }

    )

############################################################
# HTML RESPONSE
############################################################

@app.get(
    "/html",
    response_class=HTMLResponse
)
def html():

    return """
    <h1>Hello HTML</h1>
    <p>This came from FastAPI</p>
    """

############################################################
# Redirect
############################################################

@app.get("/google")
def google():

    return RedirectResponse(
        "https://www.google.com"
    )

############################################################
# Cookies
############################################################

@app.get("/cookie")
def cookie(response: Response):

    response.set_cookie(

        key="username",

        value="Akash"

    )

    return {

        "message": "Cookie Set"

    }

############################################################
# Read Cookie
############################################################

@app.get("/read-cookie")
def read_cookie(

    username: str = Cookie(None)

):

    return {

        "cookie": username

    }

############################################################
# Headers
############################################################

@app.get("/headers")
def headers(

    user_agent: str = Header(None)

):

    return {

        "Browser": user_agent

    }