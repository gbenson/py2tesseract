git clone https://github.com/madmaze/pytesseract
cd pytesseract
docker run --rm -it --mount type=bind,src=$(pwd),target=/work gbenson/python:2
virtualenv venv2
. venv2/bin/activate
pip config set global.no_python_version_warning True
pip install packaging
pip install -e .
pip wheel --no-cache-dir --no-deps .

or, build a wheel in one command:

docker run --rm -it --mount type=bind,src=$(pwd),target=/work gbenson/python:2 venv2/bin/pip wheel --no-cache-dir --no-deps .
