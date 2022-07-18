from django.db import models

# Customize objects method.


class CustomModelManager(models.Manager):
    """
    Query with kwargs from reservation database
    and return specific datum,
    but return None if not exists in database.
    """

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None
