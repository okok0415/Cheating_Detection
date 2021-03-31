from faker import Faker
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "this command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many users do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        fake = Faker(["ko_KR"])
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
                "cellphoneNum": lambda x: fake.phone_number(),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created"))