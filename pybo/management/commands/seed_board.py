from django_seed import Seed
from django.core.management.base import BaseCommand
from pybo.models import Question


class Command(BaseCommand):

    help = "This command creates board"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many users do you want to create?",
        )

        return super().add_arguments(parser)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(Question, number)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} board created!"))

