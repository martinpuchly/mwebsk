from django.db import models

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(verbose_name="predmet", max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name="email")
    message = models.TextField(verbose_name="správa")
    read_over = models.BooleanField(verbose_name="prečítané", default=False)

    def __str__(self):
        if self.subject is not None:
            return self.subject
        else:
            return f"{self.message[0:100]}..."

    class Meta:
        verbose_name = "Správa"
        verbose_name_plural = "Správy"