from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

# Create your models here.

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    RABBIT = "Rabbit", _("Rabbit")
    FRIDGE = "Fridge", _("Fridge")
    OTHER = "Other", _("Other")


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    about_me = models.TextField(verbose_name =_("About me"), default="say something about yourself")
    colour = models.CharField(_("Colour"), max_length=150, default="What is your favourite color?")
    animal = models.CharField(_("Animal"), max_length=150, default="If you were an animal what animal would you like to be?")
    profile_photo = models.ImageField( verbose_name=_("Profile Photo"), default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_("Country"), default="PT", blank=False, null=False)
    city= models.CharField(verbose_name="City", max_length=80, default="Lagos", blank=False, null=False)
    num_reviews = models.IntegerField(_("Number of Reviews"), default=0, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"



class Review(models.Model):
    reviewed_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_reviews')
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='given_reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.reviewed_user} by {self.reviewer}"
    

# # Example usage in views.py
# from your_app.models import CustomUser, Review

# def create_review(request, reviewed_user_id, reviewer_id):
#     reviewed_user = CustomUser.objects.get(pk=reviewed_user_id)
#     reviewer = CustomUser.objects.get(pk=reviewer_id)
#     content = "This is a great user!"
#     rating = 5

#     review = Review.objects.create(reviewed_user=reviewed_user, reviewer=reviewer, content=content, rating=rating)
#     review.save()
#     # Handle the rest of the view logic

