from django.db import models
from users import models as user_models


class Board(models.Model):

    """  Board Model Definition """

    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(
        user_models.User,
        on_delete=models.SET_NULL,
        null=True,
        default="1"
    )

    def __str__(self):
        return self.title
