import os

# forked from https://github.com/sayyid5416/pyinstaller/blob/main/src/actions.py

def env(name: str, _def=''):
    """ Returns environment variable """
    return os.environ.get(
        name,
        _def
    )

def set_output(key: str, value: str):
    """ Sets the output to `$GITHUB_OUTPUT` file
    - Using `key=value`
    """
    with open(env('GITHUB_OUTPUT'), 'a') as f:
        f.write(
            f'{key}={value}\n'
        )