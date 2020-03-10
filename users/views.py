from action_set.action_set import ActionSetType
from action_set.views import BreadcrumbsMixinView, ActionSetMixinView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from users.action_set import DashboardBreadcrumbs, DashboardActionSet
from users.filters import EmployeesTemplateTableFilter, CountriesTemplateTableFilter, CitiesTemplateTableFilter, \
    OrganizationsTemplateTableFilter, DepartmentsTemplateTableFilter, DepartmentEmployeesTemplateTableFilter
from users.forms import EmployeeCreateUpdateForm, CountryCreateUpdateForm, CityCreateUpdateForm, \
    OrganizationCreateUpdateForm, DepartmentCreateUpdateForm, DepartmentStaticFieldset
from users.models import User, Country, City, Organization, Department
from users.tables import EmployeesTemplateTable, CountriesTemplateTable, CitiesTemplateTable, \
    OrganizationsTemplateTable, DepartmentTemplateTable, DepartmentEmployeesTemplateTable
from utils.mixins import CustomFilterTableView, TitleViewMixin, POSTMessagesMixin


class DashboardEmployees(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, CustomFilterTableView):
    """
    View for rendering employees dashboard registry page.
    """

    model = User
    template_name = 'components/generic_template.html'
    filterset_class = EmployeesTemplateTableFilter
    table_class = EmployeesTemplateTable
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_crumbs = ['dashboard', '*employees']
    filtered_actions = ['create']
    sidebar_active_items = ['employees']
    title = 'Employee registry'

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['create'].html_params.update({'href': reverse('dashboard:employee_create')})
        return action_set_object


class DashboardCountries(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, CustomFilterTableView):
    """
    View for rendering filter table with Countries.
    """

    model = Country
    template_name = 'components/generic_template.html'
    filterset_class = CountriesTemplateTableFilter
    table_class = CountriesTemplateTable
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_crumbs = ['dashboard', '*countries']
    filtered_actions = ['create']
    sidebar_active_items = ['countries']
    title = 'Country registry'

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['create'].html_params.update({'href': reverse('dashboard:country_create')})
        return action_set_object


class DashboardCities(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, CustomFilterTableView):
    """
    View for rendering filter table with Cities.
    """

    model = City
    template_name = 'components/generic_template.html'
    filterset_class = CitiesTemplateTableFilter
    table_class = CitiesTemplateTable
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_crumbs = ['dashboard', '*cities']
    filtered_actions = ['create']
    sidebar_active_items = ['cities']
    title = 'Cities registry'

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['create'].html_params.update({'href': reverse('dashboard:city_create')})
        return action_set_object


class DashboardOrganizations(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, CustomFilterTableView):
    """
    View for rendering filter table with Organizations.
    """

    model = Organization
    template_name = 'components/generic_template.html'
    filterset_class = OrganizationsTemplateTableFilter
    table_class = OrganizationsTemplateTable
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_crumbs = ['dashboard', '*organizations']
    filtered_actions = ['create']
    sidebar_active_items = ['organizations']
    title = 'Organizations registry'

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['create'].html_params.update({'href': reverse('dashboard:organization_create')})
        return action_set_object


class DashboardDepartments(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, CustomFilterTableView):
    """
    View for rendering filter table with Departments.
    """

    model = Department
    template_name = 'components/generic_template.html'
    filterset_class = DepartmentsTemplateTableFilter
    table_class = DepartmentTemplateTable
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_crumbs = ['dashboard', '*departments']
    filtered_actions = ['create']
    sidebar_active_items = ['departments']
    title = 'Departments registry'

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['create'].html_params.update({'href': reverse('dashboard:department_create')})
        return action_set_object


class EmployeeCreateUpdateMixinView(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, POSTMessagesMixin):
    """
    Mixin for creating or updating Employee instances.
    """

    model = User
    form_class = EmployeeCreateUpdateForm
    template_name = 'components/generic_template.html'
    action_set_class = DashboardActionSet
    filtered_actions = ['save_form']
    breadcrumbs_set_class = DashboardBreadcrumbs
    sidebar_active_items = ['employees']
    success_url = reverse_lazy('dashboard:employees')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        department = form.cleaned_data.get('department')
        if department:
            self.object.organization = department.organization
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EmployeeCreateView(EmployeeCreateUpdateMixinView, CreateView):
    """
    View for creating Employee instances.
    """

    filtered_crumbs = ['dashboard', 'employees', '*employee_create']
    title = 'Employee create'


class EmployeeUpdateView(EmployeeCreateUpdateMixinView, UpdateView):
    """
    View for updating Employee instances.
    """

    filtered_crumbs = ['dashboard', 'employees', '*employee_update']
    title = 'Employee update'
    filtered_actions = ['delete', 'save_form']

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['delete'].html_params.update({
            'data-url': reverse('dashboard:employee_delete', kwargs=dict(pk=self.kwargs['pk'])),
            'data-confirmation-id': 'employee'
        })
        return action_set_object


class EmployeeDeleteView(POSTMessagesMixin, DeleteView):
    """
    View for Employee deletion.
    """

    model = User
    success_url = reverse_lazy('dashboard:employees')


class CountryCreateUpdateMixin(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, POSTMessagesMixin):
    """
    Mixin for creating or updating Country instances.
    """

    model = Country
    form_class = CountryCreateUpdateForm
    template_name = 'components/generic_template.html'
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_actions = ['save_form']
    sidebar_active_items = ['countries']
    success_url = reverse_lazy('dashboard:countries')


class CountryCreateView(CountryCreateUpdateMixin, CreateView):
    """
    View for creating Country instances.
    """

    filtered_crumbs = ['dashboard', 'countries', '*country_create']
    title = 'Country create'


class CountryUpdateView(CountryCreateUpdateMixin, UpdateView):
    """
    View for updating Country instances.
    """

    filtered_crumbs = ['dashboard', 'countries', '*country_update']
    title = 'Country update'
    filtered_actions = ['delete', 'save_form']

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['delete'].html_params.update({
            'data-url': reverse('dashboard:country_delete', kwargs=dict(pk=self.kwargs['pk'])),
            'data-confirmation-id': 'country'
        })
        return action_set_object


class CountryDeleteView(POSTMessagesMixin, DeleteView):
    """
    View for Country deletion.
    """

    model = Country
    success_url = reverse_lazy('dashboard:countries')


class CityCreateUpdateMixin(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, POSTMessagesMixin):
    """
    Mixin for creating or updating City instances.
    """

    model = City
    form_class = CityCreateUpdateForm
    template_name = 'components/generic_template.html'
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_actions = ['save_form']
    sidebar_active_items = ['cities']
    success_url = reverse_lazy('dashboard:cities')


class CityCreateView(CityCreateUpdateMixin, CreateView):
    """
    View for creating City instances.
    """

    filtered_crumbs = ['dashboard', 'cities', '*city_create']
    title = 'City create'


class CityUpdateView(CityCreateUpdateMixin, UpdateView):
    """
    View for updating City instances.
    """

    filtered_crumbs = ['dashboard', 'cities', '*city_update']
    title = 'City update'
    filtered_actions = ['delete', 'save_form']

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['delete'].html_params.update({
            'data-url': reverse('dashboard:city_delete', kwargs=dict(pk=self.kwargs['pk'])),
            'data-confirmation-id': 'city'
        })
        return action_set_object


class CityDeleteView(POSTMessagesMixin, DeleteView):
    """
    View for City deletion.
    """

    model = City
    success_url = reverse_lazy('dashboard:cities')


class OrganizationCreateUpdateMixin(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, POSTMessagesMixin):
    """
    Mixin for creating or updating Organization instances.
    """

    model = Organization
    form_class = OrganizationCreateUpdateForm
    template_name = 'components/generic_template.html'
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_actions = ['save_form']
    sidebar_active_items = ['organizations']
    success_url = reverse_lazy('dashboard:organizations')


class OrganizationCreateView(OrganizationCreateUpdateMixin, CreateView):
    """
    View for creating Organization instances.
    """

    filtered_crumbs = ['dashboard', 'organizations', '*organization_create']
    title = 'Organization create'


class OrganizationUpdateView(OrganizationCreateUpdateMixin, UpdateView):
    """
    View for updating Organization instances.
    """

    filtered_crumbs = ['dashboard', 'organizations', '*organization_update']
    title = 'Organization update'
    filtered_actions = ['delete', 'save_form']

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['delete'].html_params.update({
            'data-url': reverse('dashboard:organization_delete', kwargs=dict(pk=self.kwargs['pk'])),
            'data-confirmation-id': 'organization'
        })
        return action_set_object


class OrganizationDeleteView(POSTMessagesMixin, DeleteView):
    """
    View for Organization deletion.
    """

    model = Organization
    success_url = reverse_lazy('dashboard:organizations')


class DepartmentCreateUpdateMixin(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, POSTMessagesMixin):
    """
    Mixin for creating or updating Department instances.
    """

    model = Department
    form_class = DepartmentCreateUpdateForm
    template_name = 'components/generic_template.html'
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_actions = ['save_form']
    sidebar_active_items = ['departments']
    success_url = reverse_lazy('dashboard:departments')


class DepartmentCreateView(DepartmentCreateUpdateMixin, CreateView):
    """
    View for creating Department instances.
    """

    filtered_crumbs = ['dashboard', 'departments', '*department_create']
    title = 'Department create'


class DepartmentUpdateView(DepartmentCreateUpdateMixin, UpdateView):
    """
    View for updating Department instances.
    """

    filtered_crumbs = ['dashboard', 'departments', '*department_update']
    title = 'Department update'
    filtered_actions = ['delete', 'save_form']

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['delete'].html_params.update({
            'data-url': reverse('dashboard:department_delete', kwargs=dict(pk=self.kwargs['pk'])),
            'data-confirmation-id': 'department'
        })
        return action_set_object


class DepartmentDeleteView(POSTMessagesMixin, DeleteView):
    """
    View for Department deletion.
    """

    model = Department
    success_url = reverse_lazy('dashboard:departments')


class DepartmentDetailsView(BreadcrumbsMixinView, TitleViewMixin, ActionSetMixinView, CustomFilterTableView):
    """
    View for displaying Department's Employees.
    """

    model = User
    template_name = 'components/generic_template.html'
    filterset_class = DepartmentEmployeesTemplateTableFilter
    table_class = DepartmentEmployeesTemplateTable
    action_set_class = DashboardActionSet
    breadcrumbs_set_class = DashboardBreadcrumbs
    filtered_crumbs = ['dashboard', 'departments', '*department_details']
    filtered_actions = ['reset_table_selection', 'save_table_selection']
    sidebar_active_items = ['departments']
    title = 'Department employees'

    def get_filterset_kwargs(self, filterset_class):
        filter_kwargs = super().get_filterset_kwargs(filterset_class)
        filter_kwargs.update({
            'department': self.get_object()
        })
        return filter_kwargs

    def get_table_kwargs(self, context: dict, **kwargs):
        return super().get_table_kwargs(context, department_pk=self.kwargs['pk'], **kwargs)

    def get_object(self) -> Department:
        return get_object_or_404(Department, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        department_static_fieldset = DepartmentStaticFieldset(instance=self.get_object())
        return super().get_context_data(static_fieldset=department_static_fieldset, **kwargs)

    def get_action_set_object(self) -> ActionSetType:
        action_set_object = super().get_action_set_object()
        action_set_object.actions['save_table_selection'].html_params.update({
            'data-url': reverse('dashboard:department_save_employee_selection', kwargs=dict(pk=self.kwargs['pk'])),
            'data-confirmation-id': 'employees_selection'
        })
        action_set_object.actions['reset_table_selection'].html_params.update({
            'data-url': reverse('dashboard:department_flush_employee_selection', kwargs=dict(pk=self.kwargs['pk'])),
            'data-confirmation-id': 'employees_selection_flush'
        })
        return action_set_object


class DepartmentTableSaveSelection(View):
    """
    View for simple saving Department Employees selection.
    """

    def post(self, request, *args, **kwargs):
        employees_ids_to_add = self.request.session.pop('employee_add', None)
        employees_ids_to_remove = self.request.session.pop('employee_remove', None)
        if employees_ids_to_add:
            employees_ids_to_add = employees_ids_to_add.split(',')
            User.objects.filter(id__in=employees_ids_to_add).update(department=self.kwargs['pk'])
        if employees_ids_to_remove:
            employees_ids_to_remove = employees_ids_to_remove.split(',')
            User.objects.filter(id__in=employees_ids_to_remove).update(department=None)

        if employees_ids_to_add or employees_ids_to_remove:
            message = f'+ {len(employees_ids_to_add or [])} / - {len(employees_ids_to_remove or [])} ' \
                      f'Employees successfully processed!'
            messages.success(self.request, message)
        else:
            messages.warning(self.request, 'No Employees was added / removed!')
        return redirect('dashboard:department_details', pk=self.kwargs['pk'])


class DepartmentFlushTemplateTableSelection(View):
    """
    View for flushing cached table item choices.
    """

    def post(self, request, *args, **kwargs):
        self.request.session.pop('employee_add', None)
        self.request.session.pop('employee_remove', None)

        messages.success(self.request, 'Selection successfully removed!')
        return redirect('dashboard:department_details', pk=self.kwargs['pk'])
