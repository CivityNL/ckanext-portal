.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/CivityNL/ckanext-portal.svg?branch=master
    :target: https://travis-ci.org/CivityNL/ckanext-portal

.. image:: https://coveralls.io/repos/CivityNL/ckanext-portal/badge.svg
  :target: https://coveralls.io/r/CivityNL/ckanext-portal

.. image:: https://img.shields.io/pypi/v/ckanext-portal.svg
    :target: https://pypi.org/project/ckanext-portal/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/ckanext-portal.svg
    :target: https://pypi.org/project/ckanext-portal/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/status/ckanext-portal.svg
    :target: https://pypi.org/project/ckanext-portal/
    :alt: Development Status

.. image:: https://img.shields.io/pypi/l/ckanext-portal.svg
    :target: https://pypi.org/project/ckanext-portal/
    :alt: License

=============
ckanext-portal
=============

With this plugin, you extend the organization, and dataset entities to comply with the portal metadata structure.


------------
Requirements
------------

This plugin includes schemas and thus the ckanext-scheming is a requirement for it to function properly.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-portal:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-portal Python package into your virtual environment::

     pip install ckanext-portal

3. Add ``portal`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/ckan.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config settings
---------------
Adding and enabling the portal schema will modify the forms used to update and create each entity, indicated by the respective type property at the root level. Such as organization_type and dataset_type.

Enable the plugin by including it in the configuration options::

   ckan.plugins = ... portal ...

Set the schemas you want to use in the configuration options::

   #   For dataset portal schema:
   scheming.dataset_schemas = ckanext.portal:scheming/schemas/portal.json

   #   For organization portal schema:
   scheming.organization_schemas = ckanext.portal:scheming/schemas/organization/portal_organization.json

Portal dataset schema keys
--------------------------
::

   'carousel_active': choose to display a dataset in the portal's carousel widget
   'carousel_order':  set the order in which you want the dataset to be displayed in the carousel widget
   'carousel_image':  set an image URL to be displayed as a background image in your carousel activated dataset
   'carousel_text':   set a description to be displayed in your carousel activated dataset

Portal organization schema keys
-------------------------------
::

   'portal_intro_text': set an intro text to be displayed in your portal's homepage screen

-------------
API Endpoints
-------------
scheming_package_show
---------------------
An extended version of package_show, returning information in a format that is fitted to what the Dataplatform Portal needs
Example endpoint::

   `http://localhost:5000/api/3/action/scheming_package_show`

----------------------
Developer installation
----------------------

To install ckanext-portal for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/CivityNL/ckanext-portal.git
    cd ckanext-portal
    python setup.py develop
    pip install -r dev-requirements.txt


-----
Tests
-----

To run the tests, do::

    pytest --ckan-ini=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    pytest --ckan-ini=test.ini --cov=ckanext.portal
