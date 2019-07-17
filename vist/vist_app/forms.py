from django import forms
from vist_app.models import TracksChoice

chs = TracksChoice.objects.all()

# track_models_tuple = (
#     ('ВСЕ', 'ВСЕ',),
#     ('Белаз', 'Белаз',),
#     ('Komatsu', 'Komatsu',),
# )

track_models_tuple = (
    (chs[0].trk_model, chs[0].trk_model,),
    (chs[1].trk_model, chs[1].trk_model,),
    (chs[2].trk_model, chs[2].trk_model,),
)


class Tracksmodelform(forms.Form):

    model = TracksChoice
    trk_model = forms.ChoiceField(choices=track_models_tuple)

