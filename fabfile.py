import requests
from fabric import task


@task
def create_r2m(ctx, repo, branch, target, title):
    response = requests.post("https://deploy.heumtax.com/deployment/", json={
        "repo": repo, "branch": branch, "target": target, "title": title
    })
    print(repo, branch, target, title)
    print(response.ok)
    print(response.content)
