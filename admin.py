from django.contrib import admin
from.models import BoardGame, Entry
from.models import Gamer
from.models import Loan

admin.site.register(BoardGame)
admin.site.register(Gamer)
admin.site.register(Loan)
admin.site.register(Entry)

# Register your models here.
