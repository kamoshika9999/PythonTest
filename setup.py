from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="GUItest",
    version="0.1.0",
    license="ライセンス",
    description="パッケージの説明",
    author="sureisu",
    url="https://github.com/kamoshika9999/PythonTest.git",
    packages=find_packages("GUItest/src"),
    package_dir={"": "GUItest/src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('GUItest/requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    entry_points={'console_scripts':['guitest = pk1.main:main' ]}
)

