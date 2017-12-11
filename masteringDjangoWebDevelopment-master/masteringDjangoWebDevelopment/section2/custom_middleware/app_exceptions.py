from django.core.checks import messages
from django.http import HttpResponseRedirect
from section2.part3.migrations.views import AppError


class AppExceptionTrap:
    def process_exception(self, request, exception):
        if isinstance(exception, AppError):
            messages.error(request, str(exception))

            return HttpResponseRedirect('/')
        return None