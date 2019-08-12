# Chap 4: virtual environment
Mimics installing Python w no libraries

Show installed libraries

    pip3 freeze

Install virtualenv

    pip3 install virtualenv

Create an virtual environment

    virtualenv venv --python=python3.6      # python3.6.8 did not work

Activate the environment

    ./venv/Scripts/activate.bat     # Windows
    source venv/bin/activate        # Mac Linux
    
Deactivate environment

    deactivate

Install libraries

    pip freeze
    pip install Flask-RESTful
    pip freeze
