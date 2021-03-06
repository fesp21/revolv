from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from revolv.base import views as base_views
from revolv.project import views as project_views
from revolv.base.views import solarathome, bring_solar_tou_your_community, select_chapter, intake_form, intake_form_submit

from revolv.project.views import ProjectView

urlpatterns = patterns(
    '',
    (r'^ckeditor/', include('ckeditor.urls')),  # for assets for the ckedit widget, etc
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', base_views.HomePageView.as_view(), name='home'),
    url(r'^project/', include('revolv.project.urls', namespace='project')),
    url(r'^my-portfolio/$', base_views.DashboardRedirect.as_view(), name='dashboard'),
    url(r'^my-portfolio/categories/$', base_views.CategoryPreferenceSetterView.as_view(), name='dashboard_category_setter'),
    url(r'^my-portfolio/admin/', include('revolv.administrator.urls', namespace='administrator')),
    url(r'^my-portfolio/ambassador/', include('revolv.ambassador.urls', namespace='ambassador')),
    url(r'^my-portfolio/donor/', include('revolv.donor.urls', namespace='donor')),
    url(r'^payment_ajax_url/$', 'revolv.base.views.payment_data_table', name='payment_ajax_url'),
    url(r'^ambassador_data_table/$', 'revolv.base.views.ambassador_data_table', name='ambassador_data_table'),
    url(r'^my-portfolio/donationreport/', base_views.DonationReportView.as_view(), name='donationreport'),
    url(r'^my-portfolio/financialreport/', base_views.DonationReportForProject.as_view(), name='financialreport'),
    url(r'^my-portfolio/matchingdonors/', base_views.MatchingDonorsView.as_view(), name='matchingdonors'),
    url(r'^my-portfolio/reinvest_list/', base_views.ReinvestmentRedirect.as_view(), name='reinvest_list'),

    url(r'^what-we-do/projects/', base_views.ProjectListView.as_view(), name='projects_list'),
    url(r'^signin/$', base_views.SignInView.as_view(), name='signin'),
    url(r'^login/$', base_views.LoginView.as_view(), name='login'),
    url(r'^signup/$', base_views.SignupView.as_view(), name='signup'),
    url(r'^logout/$', base_views.LogoutView.as_view(), name='logout'),
    url(r'^unsubscribe/(?P<action>\w+)/$', 'revolv.base.views.unsubscribe', name='unsubscribe'),
    url(r'^solar_at_home/$',solarathome, name='solar_at_home'),
    url(r'^bring_solar_to_your_community/$',bring_solar_tou_your_community, name='bring_solar_to_your_community'),
    url(r'^bring_solar_to_your_community/chapter/(?P<chapter>\d+)/$',select_chapter, name='chapter'),
    url(r'^bring_solar_to_your_community/intake_form/$',intake_form, name='intake_form'),
    url(r'^bring_solar_to_your_community/intake_form/submit/$',intake_form_submit, name='intake_form_submit'),
    url(r'^my_social_account/$', 'revolv.base.views.social_connection', name='social-connection'),
    url(r'^delete/$', 'revolv.base.views.delete', name='delete'),
    url(r'^edit/$', 'revolv.base.views.edit', name='edit'),
    url(r'^add_matching_donor/$', 'revolv.base.views.add_maching_donors', name='add_matching_donor'),
    url(r'^social_connect_failed/$', 'revolv.base.views.social_exception', name='social-exception'),

    url(r'^password_reset/$', base_views.password_reset_initial, name="password_reset"),
    url(r'^password_reset/done/$', base_views.password_reset_done, name="password_reset_done"),
    url(r'^password_reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$$', base_views.password_reset_confirm, name="password_reset_confirm"),
    url(r'^password_reset/complete/$', base_views.password_reset_complete, name="password_reset_complete"),
    url(r'^password_change/$', base_views.password_change, name="password_change"),

    # wagtail urls, see http://wagtail.readthedocs.org/en/v1.0b2/howto/settings.html
    # note: we're not including the search module for public users, so we don't define it here
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'social/', include('social.apps.django_app.urls', namespace='social')),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'^harborhouse/$','revolv.base.views.harborhouse', name="harborhouse"),
    url(r'^riverrevitalizationfoundation/$','revolv.base.views.riverrevitalizationfoundation', name="riverrevitalizationfoundation"),
    url(r'^campketcha/$','revolv.base.views.campketcha', name="campketcha"),
    url(r'', include(wagtail_urls)),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
