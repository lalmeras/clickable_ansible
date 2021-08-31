`clickable\_ansible` provides ansible helpers for `clickable`.

# Release

Stable branch is `master`; development branch is `dev`. Usual release steps are :

```
# install dev tools and switch in pipenv
pipenv install --dev
pipenv shell

# update setup.py to target clickable release
# (use a git branch)

# prepare dev branch for release...
# update version
# increase version; may be launch multiple time to cycle dev, rc, ...
bump2version --verbose prerel

# merge on main
git checkout main
git pull
git merge dev

# prepare next development version (+1dev0)
git checkout dev
bump2version --verbose minor

# push all (launch with --dry-run to check before actual update)
# delete (git tag -d <tag> unneeded tags - dev, rc)
git push --all
git push --tag
```
