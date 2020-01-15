
"""
Customizations for the Django administration interface.
"""

from django.contrib import admin
from app.models import metric_grouping, metric_category, metric_type, metric_value

#class MetricGroupingInline(admin.TabularInline):
#    """Grouping objects can be edited inline in the ad-weigh editor."""
#    model = metric_grouping
#    extra = 3

#class MetricCategoryInline(admin.TabularInline):
#    """Grouping objects can be edited inline in the ad-weigh editor."""
#    model = metric_category
#    extra = 3

class MetricTypeInline(admin.TabularInline):
    """Grouping objects can be edited inline in the ad-weigh editor."""
    model = metric_type
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    """Definition of the metric_category editor."""
    fieldsets = [
        (None, {'fields': ['category_name', 'normalized_table_name']}),
    ]
    inlines = [MetricTypeInline]
    list_display = ('category_name', 'normalized_table_name')
    list_filter = ['category_name']
    search_fields = ['category_name']
    #date_hierarchy = 'when_metric_occurred'

admin.site.register(metric_grouping)
admin.site.register(metric_category, CategoryAdmin)