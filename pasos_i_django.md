# EjerciciosPy-MOD6-1

## Crear entorno virtual
mkdir nombre_proyecto
cd nombre_proyecto

python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install django
pip freeze > requirements.txt
django-admin startproject config .
python manage.py runserver

(pip install -r requirements.txt)

python manage.py startapp nombre
python manage.py migrate

## Volver a trabajar en entorno virtual 
cd nombre_proyecto
venv\Scripts\activate
python manage.py runserver


## Crear archivo .gitignore y luego escribir en él:

# Entorno virtual
venv/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Base de datos
db.sqlite3

# Archivos de entorno
.env

# VSCode
.vscode/

# Mac (por si acaso)
.DS_Store

## Subir el Repo
echo "# Nuevo proyecto" >> README.md
git init
git add .
git commit -m "Initial Django project setup"
git branch -M main
git remote add origin https://github.com/tu_usuario/nombre_repo.git
git push -u origin main
