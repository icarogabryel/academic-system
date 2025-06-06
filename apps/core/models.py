from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import Student, Employee


class Subject(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField()
    wrokload = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        ordering = ['name']


class Section(models.Model):
    # todo Do regex validation
    schedule = models.CharField(max_length=5, null=True, blank=True)
    beginning_date = models.DateField(null=True, blank=True)
    ending_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    subject = models.ForeignKey(
        Subject,
        # When a subject is deleted, all sections related to it will also be
        # deleted.
        on_delete=models.CASCADE,
        related_name='sections',
    )

    def __str__(self):
        return str(self.subject) + f' - {self.pk}'

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ['beginning_date', 'ending_date']


def get_grade_field():
    """Returns a field definition for a grade."""
    return models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0),
        ]
    )


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    grade_1 = get_grade_field()
    grade_2 = get_grade_field()
    grade_3 = get_grade_field()

    class Meta:
        unique_together = ('student', 'section')
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        ordering = ['section', 'student']


class Assignment(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='assignments',
    )
    teacher = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='assignments',
    )

    def clean(self):  # ! Improve this method
        if self.teacher.role != 'teacher':
            raise ValueError("Only teachers can be assigned to sections.")

    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'
        ordering = ['section', 'teacher']
