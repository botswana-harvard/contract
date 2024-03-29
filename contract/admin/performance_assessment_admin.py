from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)
from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import PerformanceAssessmentForm
from ..models import PerformanceAssessment


@admin.register(PerformanceAssessment, site=contract_admin)
class PerformanceAssessmentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = PerformanceAssessmentForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 5,
                   'cols': 50,
                   'style': 'height: 3em;'})},
    }

    fieldsets = (
        (None, {
            'fields': (
                'emp_identifier',
                'contract',
                'overall_perf_score',
            )}),
        audit_fieldset_tuple)
