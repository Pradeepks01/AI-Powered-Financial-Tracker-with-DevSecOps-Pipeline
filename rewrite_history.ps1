Set-Location "c:\Users\Pradeep\Desktop\finacial tracker"

git reset --soft 560301d
git reset

Remove-Item -Recurse -Force AI-BankApp-DevOps -ErrorAction SilentlyContinue

git add .gitignore
git commit -m "configure git ignore"

git add requirements.txt
git commit -m "define python dependencies"

git add Dockerfile
git commit -m "initialize docker container"

git add docker-compose.yml app-tier.yml
git commit -m "configure deployment manifests"

git add trivy.yaml
git commit -m "setup security scanning"

git add main.py
git commit -m "initialize application entrypoint"

git add .github/workflows/ci.yml
git commit -m "setup continuous integration"

git add .github/workflows/cd.yml
git commit -m "configure deployment pipeline"

git add .github/workflows/build.yml
git commit -m "setup build automation"

git add .github/workflows/devsecops-main.yml .github/workflows/devsecops-pipeline.yml
git commit -m "configure devsecops workflows"

git add src/core/config.py
git commit -m "implement core configuration"

git add src/core/security.py
git commit -m "setup security utilities"

git add src/db/session.py
git commit -m "configure database session"

git add src/db/models.py
git commit -m "define database models"

git add src/schemas/auth.py
git commit -m "implement authentication schemas"

git add src/schemas/accounts.py
git commit -m "define account schemas"

git add src/schemas/budgets.py
git commit -m "implement budget schemas"

git add src/schemas/entries.py
git commit -m "define entry schemas"

git add src/schemas/chat.py
git commit -m "implement chat schemas"

git add src/api/api.py
git commit -m "initialize api router"

git add src/api/endpoints/auth.py
git commit -m "implement authentication endpoints"

git add src/api/endpoints/accounts.py
git commit -m "setup account routing"

git add src/api/endpoints/budgets.py
git commit -m "implement budget endpoints"

git add src/api/endpoints/entries.py
git commit -m "setup entry routing"

git add src/api/endpoints/chat.py
git commit -m "implement chat endpoints"

git add src/api/endpoints/reports.py
git commit -m "setup report routing"

git add templates/index.html
git commit -m "design dashboard layout"

git add templates/login.html
git commit -m "implement login interface"

git add templates/register.html
git commit -m "design registration page"

git add scripts/ollama-setup.sh
git commit -m "setup external services"

git add src/
git commit -m "finalize core architecture"

git add .
git commit -m "polish system integration"

git push -f origin main
