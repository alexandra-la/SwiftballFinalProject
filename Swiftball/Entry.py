from django import forms
Bodysuit_ops = ((1,'Pink and blue'), (2,'Blue and gold'), (3,'Purple with Tassels'), (4,"New Bodysuit"))
ManJacket_ops = ((1, "Black"), (2, "Silver"), (3, "New jacket"))
Album_ops = ((1, "Taylor Swift"), (2, "Fearless (Taylor's Version)"), (3, "Speak Now"), (4, "Red (Taylor's Version)"), (5, "1989"), (6,"Reputation"), (7, "Lover"), (8, "Folklore"), (9, "Evermore"), (10, "Midnights"))
class SwiftEntry(forms.Form):
    Name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;'}))
    Handle = forms.CharField(max_length= 200, widget=forms.TextInput(attrs={'placeholder': 'Handle', 'style': 'width: 293px;'}))
    Lover_Bodysuit = forms.MultipleChoiceField(choices = Bodysuit_ops)
    The_Man_Jacket = forms.MultipleChoiceField(choices = ManJacket_ops)
    Surprise_Guitar_Song_Album = forms.MultipleChoiceField(choices =Album_ops)
    Surprise_Guitar_Song = forms.CharField(max_length=200)
    Surprise_Piano_Song_Album = forms.MultipleChoiceField(choices =Album_ops)
    Surprise_Piano_Song = forms.CharField(max_length= 200)