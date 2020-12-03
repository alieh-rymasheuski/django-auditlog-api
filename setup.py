from setuptools import setup

import auditlog_api

setup(
    name="django-auditlog-api",
    version=auditlog_api.__version__,
    url="https://github.com/alieh-rymasheuski/django-auditlog-api/",
    license="MIT",
    author="Alieh Rymašeŭski",
    description="Minimal API for django-auditlog",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
