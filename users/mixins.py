from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EmailLoginOnlyView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, "You are not logged in with email")
        return redirect(reverse("core:home"))


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, _("Cannot access"))
        return redirect(reverse("core:home"))


class LoggedInOnlyView(LoginRequiredMixin):
    """If user is not logged in, let user move to login page

    Args:
        login_url, login page
    """

    login_url = reverse_lazy("users:login")
