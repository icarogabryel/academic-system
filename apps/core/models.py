from django.db import models


class Subject(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        default='',
    )
    description = models.TextField()
    wrokload = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ['name']


class Section(models.Model):
    code = models.CharField(primary_key=True, max_length=10, unique=True)
    schedule = models.CharField(max_length=10)
    subject = models.ForeignKey(
        Subject,
        # When a subject is deleted, all sections related to it will also be
        # deleted.
        on_delete=models.CASCADE,
        related_name='sections',
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"
        ordering = ['code']
