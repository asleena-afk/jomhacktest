-- Chapter 15: run once in Supabase SQL Editor, in a practice project.

create table if not exists public.jomcode_lesson_posts (
  id bigint generated always as identity primary key,
  title text not null check (length(trim(title)) between 1 and 160)
);
alter table public.jomcode_lesson_posts enable row level security;

-- No browser policies. The lab server uses a privileged database connection.