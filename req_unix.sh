#!/bin/bash

check_and_install() {
    package_name=$1
    module_import_name=$2
    python -c "import $module_import_name" 2> /dev/null
    if [ $? -eq 0 ]; then
        echo "$package_name is already installed."
    else
        echo "$package_name is not installed. Installing..."
        pip install $package_name
    fi
}

check_and_install "requests" "requests"

check_and_install "beautifulsoup4" "bs4"

