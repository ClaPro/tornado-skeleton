from invoke import run, task


@task
def devserver(port=8888, logging='error'):
    """Start the server in development mode."""
    run('python run.py --port=%s --logging=%s' % (port, logging))

@task
def build():
    run("python setup.py build")

@task
def clean(bytecode=False, extra=''):
    patterns = ['build']
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        run("rm -rf %s" % pattern)

@task
def test():
    run("py.test")

@task
def quality():
    run("pylama app handlers -l pylint,pep8,pep257 -i D203")

@task
def check():
    test()
    quality()
