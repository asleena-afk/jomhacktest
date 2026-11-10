# Worked example 1: shared Python setup
# PRO TIP: Keep this setup once at the top of the file.

import os
from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel, Field
load_dotenv()
app = FastAPI(title="Chapter 15 practice API")
router = APIRouter(prefix="/lesson-posts")

class PostInput(BaseModel):
    title: str = Field(min_length=1, max_length=160)

def connection():
    return psycopg.connect(os.environ["SUPABASE_DB_URL"])

# Worked example 1: Read persistent rows
# PRO TIP : This practice table is separate from the guided project's public.posts.
# EXPECTED RESULT : GET /lesson-posts returns 200 and [] before inserting data.
# WHY IT BEHAVES THIS WAY : The connection and cursor close when their with blocks end. dict_row makes named fields available.

@router.get("")
def list_posts():
    with connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("select * from jomcode_lesson_posts order by id")
            return cur.fetchall()



@router.post("", status_code=201)
def create_post(payload: PostInput):
    with connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "insert into jomcode_lesson_posts(title) values (%s) returning *",
                (payload.title.strip(),))
            return cur.fetchone()



# Worked example 3: Update or return 404
# PRO TIP : Keep HTTP handling in routers and shared validation in service functions.
# EXPECTED RESULT : PUT an existing id returns its updated row. An unknown id returns 404.
# WHY IT BEHAVES THIS WAY : RETURNING retrieves the changed row; no matching row produces None.

@router.put("/{post_id}")
def update_post(post_id: int, payload: PostInput):
    with connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "update jomcode_lesson_posts set title=%s where id=%s returning *",
                (payload.title.strip(), post_id))
            row = cur.fetchone()
            if row is None:
                raise HTTPException(404, "Post not found")
            return row


# Worked example 4: Delete with no response body
# PRO TIP This practice API has no authentication. Chapter 16 adds ownership checks.
# EXPECTED RESULT : Existing id: 204 with empty body. Repeating deletion: 404.
# WHY IT BEHAVES THIS WAY : The transaction commits before returning success. The client must not parse a 204 body.

from fastapi import Response
@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int):
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute("delete from jomcode_lesson_posts where id=%s", (post_id,))
            if cur.rowcount == 0:
                raise HTTPException(404, "Post not found")
            return Response(status_code=204)

app.include_router(router)