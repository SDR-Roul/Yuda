@echo off
title python pip install
cls

echo upgrading pip
echo.

python -m pip install --upgrade pip

echo installing

python -m pip install --upgrade -r requirements.txt

echo.
echo install finished
echo now you can run "python app.py"
echo or to run with ssl, "python app_ssl.py"