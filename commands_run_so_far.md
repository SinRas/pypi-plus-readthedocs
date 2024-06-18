# Install Sphinx
pip install -U sphinx

# Install Setuptools
pip install setuptools

# Install build
pip install --upgrade build

# Install NumPy
pip install numpy

# Install Icecream
pip install icecream

# Building tutorial: https://earthly.dev/blog/create-python-package/
python -m build --wheel
