# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python application

on:
  workflow_dispatch:

permissions:
  contents: read
env:
  PYTHONPATH: '/usr/local/lib'

jobs:
  build:
    env:
      PYTHONPATH: "/usr/local/lib/python${{matrix.pyv}}/site-packages"

    runs-on: ubuntu-22.04
    strategy:
      matrix:
        pyv: ["3.8","3.9","3.10"]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{matrix.pyv}}
      uses: actions/setup-python@v3
      with:
        python-version: ${{matrix.pyv}}

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get -y install gcc cmake make build-essential cython3 libeigen3-dev libnetcdf-dev libnetcdf19 libnetcdf-mpi-dev libnetcdf-mpi-19 python3-netcdf4 libhdf5-103 libhdf5-cpp-103 libhdf5-dev python3-setuptools python3-build python3-pip libglu1-mesa
        pip install pytest

    -name Build and install openmc
        git clone --depth 1 https://github.com/openmsr/openmc_install_scripts
        cd openmc_install_scripts/Ubuntu_22.04
        ./install-all.sh

    - name: Run Tests
      run: |
        pytest openmc_tests
