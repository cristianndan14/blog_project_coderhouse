import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_create():
    user = User.objects.create_user(
        username='auhdiasASDAD134141daauhd',
        email='oiasdoas.doasda.sdASDAhaosd@gmail.com',
        first_name='aubahsdASDFASosahd asndo12',
        last_name='asodahSADGGosdno 123123-}..',
        password='123123oihad.ONDSANDknlasd',
    )
    assert user.username == 'auhdiasASDAD134141daauhd'


@pytest.mark.django_db
def test_superuser_create():
    user = User.objects.create_superuser(
        username='auhdiasASDAD134141daauhd',
        email='oiasdoas.doasda.sdASDAhaosd@gmail.com',
        first_name='aubahsdASDFASosahd asndo12',
        last_name='asodahSADGGosdno 123123-}..',
        password='123123oihad.ONDSANDknlasd',
    )
    assert user.is_superuser