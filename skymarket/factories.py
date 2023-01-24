import factory

from ads.models import Ad
from users.models import User

from ads.models import Comment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'test_name'
    last_name = 'test_last_name'
    phone = "+79995553311"
    email = factory.Faker('email')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    title = 'test_title'
    price = 1000
    description = "test_description"
    author = factory.SubFactory(UserFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = 'test_text'
    author = factory.SubFactory(UserFactory)
    ad = factory.SubFactory(AdFactory)
