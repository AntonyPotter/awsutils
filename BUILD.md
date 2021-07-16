# awsutils

This package was built following the instructions [here](https://packaging.python.org/tutorials/packaging-projects/)

    $ python3 -m build

Having created a user in pypi authentication tokens are stored in.

    ~/.pypirc

To upload to the test pypi

    $ python3 -m twine upload --repository testpypi dist/*

To install from test pypi

    $ python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps potteringabout-awsutils




