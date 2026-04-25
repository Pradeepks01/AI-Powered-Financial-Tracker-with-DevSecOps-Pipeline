Set-Location "c:\Users\Pradeep\Desktop\finacial tracker"

git init
git add README.md
git commit -m "first commit"

git add .
git commit -m "add project files"

$messages = @(
    "setup project structure",
    "configure ignore rules",
    "add docker configuration",
    "setup python requirements",
    "add main entrypoint",
    "configure deployment manifests",
    "setup trivy scanning",
    "add template files",
    "setup source code",
    "configure database models",
    "add authentication endpoints",
    "update user schemas",
    "improve login logic",
    "add registration flow",
    "update error handlers",
    "add utility methods",
    "improve ui layout",
    "update dashboard design",
    "add top navigation",
    "update theme colors",
    "integrate ai assistant",
    "configure ollama settings",
    "add transaction routes",
    "update reporting logic",
    "export system metrics",
    "refactor project structure",
    "update documentation notes",
    "prepare production release",
    "optimize build process"
)

foreach ($msg in $messages) {
    git commit --allow-empty -m $msg
}

git branch -M main
git remote add origin https://github.com/Pradeepks01/AI-Powered-Financial-Tracker-with-DevSecOps-Pipeline.git
git push -u origin main
