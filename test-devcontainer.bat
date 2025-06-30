@echo off
echo Testing Dev Container Configuration...
echo.

echo 1. Checking Docker status...
docker --version
if %ERRORLEVEL% neq 0 (
    echo ERROR: Docker is not working properly
    pause
    exit /b 1
)

echo.
echo 2. Checking if python-dev image exists...
docker images python-dev
echo.

echo 3. Testing container creation...
docker run --rm -v "%CD%:/workspace" python-dev:latest python /workspace/hello_world.py
if %ERRORLEVEL% neq 0 (
    echo ERROR: Container test failed
    pause
    exit /b 1
)

echo.
echo SUCCESS: Dev Container configuration appears to be working!
echo You can now try opening the folder in VS Code Dev Containers.
echo.
pause
