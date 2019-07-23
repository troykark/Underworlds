REM https://kivy.org/doc/stable/installation/installation-windows.html
REM C:\Python37\share\kivy-examples example location 

python -m pip install --upgrade pip wheel setuptools virtualenv
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.22 kivy_deps.glew==0.1.12
python -m pip install kivy_deps.gstreamer==0.1.17
python -m pip install kivy==1.11.1
python -m pip install kivy_examples==1.11.1

