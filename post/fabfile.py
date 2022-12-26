import requests
from fabric import task


@task
def post_deploy(ctx, repo, sha):
    response = requests.post("https://deploy.heumtax.com/deployment/post", json={
        "repo": repo, "sha": sha
    })
    print(repo, sha)
    print(response.ok)
    print(response.content)
