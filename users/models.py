from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom User placeholder."""

    shoe_number = models.FloatField()

    def __str__(self) -> str:
        return str(self.shoe_number)

    def get_canonical_url(self) -> str:
        """Generate canonical URL for Custom User.

        :returns: canonical URL
        :rtype: str
        """
        return f"/{self.shoe_number}/canonical/"
