from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.core.exceptions import ValidationError
from ..utils.validators import (validate_ses,
                                     validate_generic_number,
                                     validate_names, validate_sus)
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .model_user import User
from .model_responsible import Responsible


class Patient(models.Model):
    user = models.OneToOneField(
        User,
        related_name='patient',
        on_delete=models.CASCADE,
        limit_choices_to=Q(has_specialization=False),
        verbose_name=_('User')
    )
    ses = models.CharField(
        help_text=_("Please, enter the valid SES number"),
        unique=True,
        max_length=9,
        validators=[validate_ses],
    )

    responsible = models.ForeignKey(
        Responsible,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Responsible')
    )

    PRIORITIES = (
        (5, _('Not urgent')),
        (4, _('Not very urgent')),
        (3, _('Urgent')),
        (2, _('Very urgent')),
        (1, _('Emerging')),
      )
    priority = models.IntegerField(
        _('Priority'),
        choices=PRIORITIES,
        help_text=_("Please, insert the degree of priority of the patient"),
    )

    mother_name = models.CharField(
        _('Name of mother'),
        help_text=_("Please, insert your mother name"),
        max_length=80,
        validators=[validate_names],
    )

    father_name = models.CharField(
        _('Name of father'),
        help_text=_("Please, insert your father name"),
        max_length=80,
        validators=[validate_names],
    )

    COLOR = (
        (5, _('White')),
        (4, _('Black')),
        (3, _('Yellow')),
        (2, _('Brown')),
        (1, _('Indigenous')),
    )
    ethnicity = models.IntegerField(
        _('Ethnicity'),
        choices=COLOR,
        help_text=_("Please insert the ethnicity of the patient"),
    )
    sus_number = models.CharField(
        _('SUS number'),
        help_text=_("Please, enter valid SUS in format: XXXXXXXXXXXXXXX"),
        unique=True,
        max_length=15,
        validators=[validate_sus],
    )
    civil_registry_of_birth = models.CharField(
        _('Civil register of birth'),
        help_text=_("Please, enter the civil registry of birth number"),
        unique=True,
        default='',
        max_length=11,
        validators=[validate_generic_number],
    )
    declaration_of_live_birth = models.CharField(
        _('Declaration of live birth'),
        help_text=_("Please, enter the declaration of live birth number"),
        unique=True,
        default='',
        max_length=11,
        validators=[validate_generic_number],
    )

    def __str__(self):
        return self.user.get_username()

    def clean(self, *args, **kwargs):

        try:
            user_db = Patient.objects.get(id=self.id).user

            if self.user != user_db:
                raise ValidationError(
                    _("Don't change users"))
            else:
                pass
        except Patient.DoesNotExist:
            pass

        self.user.clean()

    def save(self, *args, **kwargs):
        self.user.clean()
        self.user.save()
        self.clean()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.user.has_specialization = False
        self.user.save()
        super().delete(*args, **kwargs)
