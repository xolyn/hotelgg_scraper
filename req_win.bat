@echo off

python -c "import requests" 2>NUL
if %ERRORLEVEL% neq 0 (
    echo requests is not installed. Installing...
    pip install requests
) else (
    echo requests is already installed.
)

python -c "import bs4" 2>NUL
if %ERRORLEVEL% neq 0 (
    echo beautifulsoup4 is not installed. Installing...
    pip install beautifulsoup4
) else (
    echo beautifulsoup4 is already installed.
)

pause
