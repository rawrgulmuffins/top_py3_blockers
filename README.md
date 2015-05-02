# top_python3_blockers
Create a list of the of the python projects stored in pypi which are blocking the most python projects from being ported to Python3.

# Running instructions
##NOTE

These instructions were written on a ubuntu 14.10 machine.

##Instructions
you'll need a copy of python3, which comes by default in ubuntu 14.10

I personally suggest using a virtual environment
    sudo apt-get install pip
    sudo pip install virtualenvwrapper
    source /usr/local/bin/virtualenvwrapper.sh
    mkvirtualenv --python=/usr/bin/python3 top_py3_blockers
    workon top_py3_blockers

You'll need a copy of the dev version of caniusepython3
    cd ~/git # cd to where ever you organize projects
    git clone git@github.com:brettcannon/caniusepython3.git
    cd caniusepython3
    python setup.py build
    python setup.py install
    cd ~/git # cd to where ever you organize projects
    git clone git@github.com:rawrgulmuffins/top_py3_blockers.git
    cd top_py3_blockers
    python top_py3_blockers.
