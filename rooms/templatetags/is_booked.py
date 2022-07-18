import datetime
from django import template
from reservations import models as reservation_models

register = template.Library()


@register.simple_tag
def is_booked(room, cal_date):
    """make tag to validate this day is booked or not

    Args:
        room (RoomObject): the room of page
        cal_day (DateTime): the date of calendar

    Returns:
        Boolean: this date is booked or
    """
    if cal_date.number == 0:
        return
    try:
        date = datetime.date(cal_date.year, cal_date.month, cal_date.number)
        reservation_models.BookedDay.objects.get(day=date, reservation__room=room)
        return True
    except reservation_models.BookedDay.DoesNotExist:
        return False
