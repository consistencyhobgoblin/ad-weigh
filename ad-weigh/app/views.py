"""
Definition of views.
"""
from app.models import metric_grouping, metric_category, metric_type, metric_value
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import ListView, DetailView
from datetime import datetime
from os import path
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#def home(request):
#    """Renders the home page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/index.html',
#        {
#            'title':'Ad-Weigh',
#            'year':datetime.now().year,
#        }
#    )

class TypeListView(ListView):
    """Renders the home page, with a list of all types."""
    model = metric_type

    #@method_decorator(login_required) # this barfs - figure out later
    def get_context_data(self, **kwargs):
        context = super(TypeListView, self).get_context_data(**kwargs)
        context['title'] = 'Metric Categories and Types'
        context['year'] = datetime.now().year
        return context

class TypeDetailView(DetailView):
    model = metric_type    
    #context_object_name = metric_type

    def get_context_data(self, **kwargs):
        context = super(TypeDetailView, self).get_context_data(**kwargs)
        #context['title'] = 'Values'
        #context['year'] = datetime.now().year
        return context

class ValuesListView(ListView):
    """Renders the values_list page, with a list of all types."""
    model = metric_value
    template_name = 'values_list.html'
    context_object_name = 'current_values_list'

    def get_queryset(self):
        return metric_value.objects.filter(value_metric_type_id=self.kwargs[value_metric_type_id])

    #def get_context_data(self, **kwargs):
    #    context = super(ValuesListView, self).get_context_data(**kwargs)
    #    context['title'] = 'Metric Values'
    #    context['year'] = datetime.now().year
    #    return context

class ValueDetailView(DetailView):
    """Renders the metric_value detail page."""
    model = metric_value

    def get_context_data(self, **kwargs):
        context = super(ValueDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Value Detail'
        context['year'] = datetime.now().year
        return context

def save_value(request, value_id):
    context_object_name = metric_value
    """Handles value persistence. Validates input and updates the repository."""

    oMetricValue = get_object_or_404(metric_value, pk=value_id)
    try:
        oSelectedValue = oMetricType.metric_value_set.get(ProcessLookupError=request.Post['metric_value'])
    except (KeyError, metric_value.DoesNotExist):
        return render(request, 'app/type_details.html', {
            'title': 'Type Detail',
            'year': datetime.now().year,
            'metric_type': oMetricType,
            'error_message': "Value not found",
    })
    else:
        oSelectedValue.numeric_value = 1
        oSelectedValue.save()

    return HttpResponseRedirect(reverse('app:type_details', args=(type.id,)))

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Ad-Weigh Contact Page',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Ad-Weigh is a generic digital ad metric entry tool and an ad taxonomy maintenance tool.',
            'year':datetime.now().year,
        }
    )
