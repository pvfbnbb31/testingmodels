from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from memoraid.models import Choice, Memoraid

from django.forms import ModelForm

from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

# You can find an example class diagram for the View (M-T-V pattern) at
# http://yuml.me/edit/c1965e70
# You'll notice that the View classes provided by Django are
# elided (they do not have the attributes or methods listed).

class IndexView(generic.ListView):
    template_name = 'memoraid/index.html'
    context_object_name = 'latest_memoraid_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Memoraid.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Memoraid
    template_name = 'memoraid/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yetself.
        """
        return Memoraid.objects.filter(pub_date__lte=timezone.now())


class ResultsView(LoginRequiredMixin, generic.DetailView):
    model = Memoraid
    template_name = 'memoraid/results.html'

class MasterView(LoginRequiredMixin, generic.ListView):
    template_name = 'memoraid/master.html'
    def get_queryset(self):
        return Memoraid.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

	
def vote(request, memoraid_id):
    p = get_object_or_404(Memoraid, pk=memoraid_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'memoraid/detail.html', {
            'memoraid': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('memoraid:results', args=(p.id,)))

class MemoraidModelForm(ModelForm):
    class Meta:
        model = Memoraid
        fields = ['memoraid_text', 'pub_date']




