python -m venv .venv
. .venv/bin/activate
pip -V
pip install celery[redis]


brew update
brew install redis
brew services start redis
redis-cli ping

