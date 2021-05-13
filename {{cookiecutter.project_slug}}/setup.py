from setuptools import setup
from setuptools.command.install import install
import importlib
import src.{{cookiecutter.sku}}.version as ver


class CustomInstallCommand(install):
    """
    Custom installation for grading
    """

    def run(self):
        install.run(self)
        try:
            module = importlib.import_module("labs.labconfig")
            module.gencfg(sku='{{cookiecutter.sku}}', version=ver.__version__, force=True)
        except ModuleNotFoundError:
            exit(1)


setup(
    include_package_data=True,
    version=ver.__version__,
    cmdclass={
        'install': CustomInstallCommand
    }
)
