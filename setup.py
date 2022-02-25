from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='qtpylet',
    version='0.6.1',
    description='Bringing leaflet maps to PyQt or PySide',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Leon Friedmann',
    author_email='leon.friedmann@tum.de',
    url='https://github.com/EasyIsrael/qtpylet',
    keywords='leaflet, pyqt, pyside, maps, python, python3',
    classifiers=[],
    packages=[
        'qtpylet',
        'qtpylet.leaflet',
        'qtpylet.leaflet.control',
        'qtpylet.leaflet.core',
        'qtpylet.leaflet.layer',
        'qtpylet.leaflet.layer.marker',
        'qtpylet.leaflet.layer.tile',
        'qtpylet.leaflet.layer.vector',
        'qtpylet.leaflet.layer.icon',
        'qtpylet.leaflet.map',
    ],
    package_data={
        'qtpylet': [
            'web/map.html',
            'web/custom.js',
            'web/modules/*/*',
            'web/modules/*/images/*',
        ],
    },
    install_requires=[
        #'QtPy==2.0.1',
    ],
    extras_require = {
        'PyQt5' : ['PyQt5==5.15.5','PyQtWebEngine==5.15.5'],
        'PySide2': ['PySide2==5.15.2.1']
    }
)


