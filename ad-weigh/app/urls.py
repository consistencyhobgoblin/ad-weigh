
from django.conf.urls import url
from app.models import metric_grouping, metric_category, metric_type, metric_value
import app.views

urlpatterns = [
    # Home page routing
    url(r'^$',
        app.views.TypeListView.as_view(
            queryset=metric_type.objects.order_by('-type_metric_category_id', '-type_name'),
            context_object_name='current_types_list',
            template_name='app/index.html',),
        name='home'),

    ## Routing for a metric_values_list page, which use URLs in the form <value_metric_type_id>/,
    ## where the id number is captured as a group named "value_metric_type_id".
    #url(r'^(?P<value_metric_type_id>\d+)/$',
    #    app.views.ValuesListView.as_view(
    #        context_object_name='current_values_list',
    #        template_name='app/values_list.html'),
    #    name='values_list'),

    # Routing for a metric_type detail page, which use URLs in the form <pk>/,
    # where the id number is captured as a group named "pk".
    #url(r'^(?P<pk>\d+)/$',
    #    app.views.TypeDetailView.as_view(
    #        template_name='app/type_details.html'),
    #    name='type_detail'),

    url(r'^(?P<pk>\d+)/$',
        app.views.ValueFormSetView.as_view(
            template_name='app/value_formset.html'),
        name='value_formset'),    

    ## Routing for a metric_value detail page, which use URLs in the form <metric_value_id>/,
    ## where the id number is captured as a group named "metric_value_id".
    #url(r'^(?P<metric_value_id>\d+)/$',
    #    app.views.ValueDetailView.as_view(
    #        template_name='app/value_detaisl.html'),
    #    name='value_detail'),

    ## Routing for <poll_id>/results pages, again using a capture group
    ## named pk.
    #url(r'^(?P<pk>\d+)/results/$',
    #    app.views.PollResultsView.as_view(
    #        template_name='app/results.html'),
    #    name='results'),

    ## Routing for <value_id>/save_value pages, with the capture group named
    ## value_id this time, which becomes an argument passed to the view.
    url(r'^(?P<value_id>\d+)/save_value/$', app.views.save_value, name='save_value'),
]
