import nox


@session(python=False)
def tests(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report")


@nox.session(python=False)
def lint(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("black", "--check", ".")
    session.run("flake8", ".")


@nox.session(python=False)
def typing(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("mypy", ".")
