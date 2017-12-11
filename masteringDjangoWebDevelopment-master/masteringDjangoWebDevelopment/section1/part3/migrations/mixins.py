from Tools.Scripts.findnocoding import args
from django.core.checks import messages
from django.http import request, HttpResponseRedirect


class OnlyStaffMixin(object):
    def dispatch(self. request, *args, **kwargs):

        if not request.user.is_staff:
            messages.error(request, "Only Staff members can do this.")

            try:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            except keyError:
                return HttpResponseRedirect('/')
        return super(OnlyStaffMixin, self).dispatch(request, *args, **kwargs)