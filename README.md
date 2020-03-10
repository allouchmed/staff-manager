## Staff Manager

StaffManager is a Django demo application that shows the basic CRUD operations using the company's personnel 
management as an example.

#### Dependencies

* `Django==3.0.4`
* `django-environ==0.4.5`
* `django-filter==2.2.0`
* `django-debug-toolbar==2.2`
* `mysqlclient==1.4.6`
* `btc-dev-tools==0.5.3`
* `btc-template-tables==0.4.1`
* `btc-action-set==0.2.3`
* `btc-flex-forms==2.1`
* `btc-floating-windows==1.0`

#### Packages overview

* `btc-dev-tools` - contains some help-full functions for other packages.
* `btc-template-tables` - used for rendering tables.
* `btc-action-set` - used for rendering actions via buttons, links, breadcrumbs and increase code reuse.
* `btc-flex-forms` - used for fast form development - forms have autogenerated template.
* `btc-floating-windows` - used for displaying modals

#### Deprecated

* `django-autocomplete-light` is too old, so were used custom solution.

#### Note

* Before use, create necessary relations: Country, City and etc.

1. Remove employee from department

    To delete employee from department use filter `In the department` and select employees by `trash` button.

2. Add employee to the department:

    Uncheck filter `In the department` to show non free employees. Select employees by `+` button in the table.

You can search employees with table filters.

For save selection click `Save selection` button on the toolbar. To reset selection click `Reset selection` button.

#### Example
<img src="https://user-images.githubusercontent.com/33987296/76365006-547c3a00-6337-11ea-9fa5-7181d0c25e3e.png">


