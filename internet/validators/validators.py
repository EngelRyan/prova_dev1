from django.utils import timezone

from django.core.exceptions import ValidationError

def validate_min_date_today(date):
    if date < timezone.datetime.date(timezone.now()):
        raise ValidationError(
            "Data menor que hoje não né",
            params={"date": date}
        )