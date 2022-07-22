from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from rooms import models as room_models
from . import models


def toggle_room(request, room_pk):
    action = request.GET.get("action", None)
    room = room_models.Room.objects.get_or_none(pk=room_pk)
    if room is not None and action is not None:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name=models.List.FAVOURITE_LIST_NAME
        )
        if action == "add":
            the_list.rooms.add(room)
            messages.success(request, "This room is added in FavList")
        if action == "remove":
            the_list.rooms.remove(room)
            messages.success(request, "This room is removed from FavList")
    return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))


class SeeFavsView(TemplateView):

    template_name = "lists/list_detail.html"
