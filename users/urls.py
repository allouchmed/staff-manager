from django.urls import path

from users.views import DashboardEmployees, EmployeeCreateView, DashboardCountries, CountryCreateView, \
    CountryUpdateView, CountryDeleteView, EmployeeUpdateView, EmployeeDeleteView, DashboardCities, CityCreateView, \
    CityUpdateView, CityDeleteView, DashboardOrganizations, OrganizationCreateView, OrganizationUpdateView, \
    OrganizationDeleteView, DashboardDepartments, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView, \
    DepartmentDetailsView, DepartmentTableSaveSelection, DepartmentFlushTemplateTableSelection

app_name = 'dashboard'

urlpatterns = [
    # Employees
    path('employees/', DashboardEmployees.as_view(), name='employees'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),

    # Countries
    path('countries/', DashboardCountries.as_view(), name='countries'),
    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/update/<int:pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<int:pk>/', CountryDeleteView.as_view(), name='country_delete'),

    # Cities
    path('cities/', DashboardCities.as_view(), name='cities'),
    path('city/create/', CityCreateView.as_view(), name='city_create'),
    path('city/update/<int:pk>/', CityUpdateView.as_view(), name='city_update'),
    path('city/delete/<int:pk>/', CityDeleteView.as_view(), name='city_delete'),

    # Organizations
    path('organizations/', DashboardOrganizations.as_view(), name='organizations'),
    path('organization/create/', OrganizationCreateView.as_view(), name='organization_create'),
    path('organization/update/<int:pk>/', OrganizationUpdateView.as_view(), name='organization_update'),
    path('organization/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='organization_delete'),

    # Departments
    path('departments/', DashboardDepartments.as_view(), name='departments'),
    path('department/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('department/update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'),
    path('department/delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department_delete'),
    path('department/details/<int:pk>/', DepartmentDetailsView.as_view(), name='department_details'),
    path('department/<int:pk>/save-employee-selection/',
         DepartmentTableSaveSelection.as_view(), name='department_save_employee_selection'),
    path('department/<int:pk>/flush-employee-selection/',
         DepartmentFlushTemplateTableSelection.as_view(), name='department_flush_employee_selection'),
]
