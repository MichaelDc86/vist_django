from django.forms import inlineformset_factory
from django.views.generic.list import ListView
# from django.db.models import F
from django.db.models.functions import Cast
from django.db.models import FloatField

from vist_app.models import Tracks, TracksChoice
from vist_app.forms import Tracksmodelform

# Create your views here.


class TrackListView(ListView):

    def get_queryset(self):
        if self.request.GET:
            track_model_choice = self.request.GET['trk_model']

            if track_model_choice == TracksChoice.objects.all()[0].trk_model:
                self.queryset = Tracks.objects.annotate(
                    overld=
                    (
                            (Cast('current_weight', FloatField()) / Cast('max_load_capacity', FloatField()) - 1) * 100
                    )
                )
            else:
                self.queryset = Tracks.objects.annotate(
                    overld=
                    (
                            (Cast('current_weight', FloatField()) / Cast('max_load_capacity', FloatField()) - 1) * 100
                    )
                ).filter(track_model=track_model_choice)
            print(track_model_choice)

        else:
            self.queryset = Tracks.objects.annotate(
                overld=
                (
                        (Cast('current_weight', FloatField()) / Cast('max_load_capacity', FloatField()) - 1) * 100
                )
            )

        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'tracks'
        if self.request.GET:
            context['form'] = Tracksmodelform(initial={'trk_model': self.request.GET['trk_model']})
        else:
            context['form'] = Tracksmodelform()

        return context
