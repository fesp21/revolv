from django.conf.urls import patterns, url

from revolv.administrator.views import (admin_csv_download,
                                        AdministratorDashboardView,
                                        AdministratorEmailView)
from revolv.base.users import is_administrator

urlpatterns = patterns(
    '',
    url(r'^$', is_administrator(AdministratorDashboardView.as_view()), name='dashboard'),
    url(r'^email$', is_administrator(AdministratorEmailView.as_view()), name='email'),
    url(r'^csv$', admin_csv_download, name='csv'),
)
