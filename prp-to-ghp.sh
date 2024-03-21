git commit -am 'update'
git checkout pd-output
git merge main
source mkdc.sh
git commit -am 'update'
git checkout gh-pages
git merge pd-output
git push gh-origin
git checkout main
