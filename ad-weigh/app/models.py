"""
Definition of models.
"""
from django.db import models
from django.db.models import Sum

class metric_grouping(models.Model):
    """an object to store 'dashboard', 'report' or other grouping of metrics"""
    grouping_name = models.CharField(max_length=200)
    grouping_description = models.CharField(max_length=1200, null=True, blank=True)
    enum_grouping_type = models.CharField(max_length=50)

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.grouping_name

    def __str__(self):
        return self.grouping_name

class metric_category(models.Model):
    """an object to store 'CRM', 'Display', 'Paid Search' et al."""
    category_name = models.CharField('category', max_length=50)
    normalized_table_name = models.CharField('datamart table', max_length=100, null=True, blank=True)

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.category_name

    def __str__(self):
        return self.category_name

class metric_type(models.Model):
    """a classification of a metric such as 'impression' or 'click'"""
    type_metric_category = models.ForeignKey(metric_category)
    type_metric_grouping = models.ManyToManyField(metric_grouping, blank=True)
    type_name = models.CharField('metric type', max_length=50)
    enum_datatype = models.CharField('datatype', max_length=50, null=True, blank=True)

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.type_name

    def __str__(self):
        return self.type_name

class metric_value(models.Model):
    """an object to store the value of the metric"""
    value_metric_type = models.ForeignKey(metric_type)
    when_metric_occurred = models.DateTimeField('metric date', null=True, blank=True)
    numeric_value = models.FloatField('number value', default=0.0)
    string_value = models.CharField('text value', max_length=1000, null=True, blank=True)
    boolean_value = models.NullBooleanField('true-false value')
    is_rate = models.BooleanField(default=False)
    notes = models.TextField('notes', null=True, blank=True)
  