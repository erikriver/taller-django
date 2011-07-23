from django.http import HttpResponse
from plus.models import *
from plus.forms import *
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import ProcessFormView
import json

class StatusCreate(CreateView):
    template_name = 'index.html'
    form_class = StatusForm

    def form_valid(self, form):
        object = form.save(commit = False)
        object.author = self.request.user
        object.save()
        self.success_url = "/index"
        return super(StatusCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        statuses = Status.objects.all()
        for status in statuses:
            status.plus = Plus.objects.filter(content_type = ContentType.objects.get_for_model(status), content_id = status.id).count()
        kwargs.update({
            'statuses'  : statuses
        })
        return super(StatusCreate, self).get_context_data(*args, **kwargs)


class PlusOne(ProcessFormView):
    def get(self, request, *args, **kwargs):
        status = Status.objects.get(id = self.request.GET.get('vote'))
        vote = Plus(user = self.request.user, content = status)
        vote.save()
        count = Plus.objects.filter(content_type = ContentType.objects.get_for_model(status), content_id = status.id).count()
        return HttpResponse(json.dumps({'count': count, 'id': status.id }), content_type='application/json')
