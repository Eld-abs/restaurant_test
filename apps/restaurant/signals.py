from django.contrib.auth.models import Group


def create_groups(sender, **kwargs):
    for name in ["owner", "manager"]:
        Group.objects.get_or_create(name=name)