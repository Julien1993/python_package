from setuptools import setup, find_packages
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='nom_de_votre_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={
        'dev': [
            'pytest',
        ]
    },
    entry_points={
        'console_scripts': [
            'votre_script = nom_de_votre_package.script:fonction_principale',
        ]
    },
    python_requires='>=3.6',
)
