echo off
echo "Enter Proyect name"
set /p proj_name=
set building="Building django project %proj_name%"
echo %building%
python d:\js\env\django\bin\django-admin.py startproject %proj_name%
pause