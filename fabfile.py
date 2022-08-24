import requests
from fabric import task


@task
def create_r2m(ctx, repo, branch, title):
    requests.post("https://deploy.heumtax.com/deploy/", json={
        "repo": repo, "branch": branch, "title": title
    })
