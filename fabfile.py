import requests
from fabric import task


@task
def create_r2m(ctx, repo, branch, title):
    response = requests.post("https://deploy.heumtax.com/deployment/", json={
        "repo": repo, "branch": branch, "title": title
    })
    print(repo, branch, title)
    print(response.ok)
    print(response.json())
