from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True,)
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        'Group',
        related_name='posts',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Введите название тематической группы',
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Номер группы',
        help_text='Укажите порядковый номер группы',
    )
    description = models.TextField(
        max_length=200,
        verbose_name='Описание группы',
        help_text='Добавьте текст описания группы',
    )


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField(max_length=300,)
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
    )
    following = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                name='unique_follow',
                fields=('user', 'following')
            ),
        )
