from django.db import models
from django.contrib.auth.models import User


class BoardGame(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Entry(models.Model):
    boardgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    text =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='entries'

        def __str__(self):
            return f"{self.text[:50]}..."



class Gamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Loan(models.Model):
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.board_game.title} - {self.borrower.user.username}"

