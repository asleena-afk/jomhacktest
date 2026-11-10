# CHAPTER 14
# FastAPI, Uvicorn and Swagger fundamentals learn

# Shared setup
# PRO TIP : Keep this setup once at the top of the file.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app = FastAPI(title="JomCode Chapter 14")

# Worked example 1: Health endpoint
# PRO TIP : Start Uvicorn from the folder containing Chapter14.py
# EXPECTED RESULT : Swagger: GET /health returns 200 and {"ok": true}.
# WHY IT BEHAVES THIS WAY :The decorator registers this function for the method and path. FastAPI serializes the dictionary to JSON.

@app.get("/health")
def health():
     return {"ok": True}


# Worked example 2: Path and query parameters
# PRO TIP : In Swagger, expand the operation, select Try it out, enter values, then Execute.
# EXPECTED RESULT : GET /posts/7?preview=true returns 200 with id=7 and preview=true. /posts/abc returns 422.
# WHY IT BEHAVES THIS WAY : Annotations convert and validate HTTP text before the function runs.

@app.get("/posts/{post_id}")
def read_post(post_id: int, preview: bool = False):
     return {"id": post_id, "preview": preview}

# Worked example 3: Validated request body
# PRO TIP : Length validation alone allows whitespace. Add strip() rules in the service layer.
# EXPECTED RESULT : POST /posts with {"title":"Hi","body":"Welcome"} returns 201. An empty title returns 422.
# WHY IT BEHAVES THIS WAY : Pydantic checks the body before the handler receives it. This example returns data without persisting it.

class PostInput(BaseModel):
     title: str = Field(min_length=1, max_length=160)
     body: str = Field(min_length=1, max_length=20000)

@app.post("/posts", status_code=201)
def create_post(payload: PostInput):
     return {"id": 1, **payload.model_dump()}

# Worked example 4: Explicit HTTP error
# PRO TIP : A traceback and status 500 usually indicate an unexpected server failure.
# EXPECTED RESULT : GET /missing returns 404 and {"detail":"Post not found"}.
# WHY IT BEHAVES THIS WAY :HTTPException turns an expected application failure into a documented HTTP response.

@app.get("/missing")
def missing():
     raise HTTPException(404, "Post not found")

# Exercise 1: Greeting endpoint
# YOUR TASK : Add GET /greeting with a name query parameter defaulting to Reader.
# CHECK THESE CASES : No name gives Hello, Reader. name=Ada gives Hello, Ada.
# HINT AFTER A TRY : Use a typed function argument with a default.

# Exercise 2: Whitespace validation
# YOUR TASK : Add POST /checked-posts and reject a title containing only whitespace.
# CHECK THESE CASES : Blank title returns 422. " Hi " returns cleaned title Hi.
# HINT AFTER A TRY : Strip the title and raise HTTPException when empty
