import random
from faker import Faker
from django.core.management.base import BaseCommand
from django_seed import Seed
from boards import models as board_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates boards"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many boards you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        fake = Faker(["ko_KR"])
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            board_models.Board,
            number,
            {
                "title": lambda x: fake.company(),
                "content": lambda x: fake.address(),
                "user": lambda x: random.choice(all_users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} boards created!"))
