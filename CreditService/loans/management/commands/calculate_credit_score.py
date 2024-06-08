from django.core.management.base import BaseCommand
from loans.models import User
from loans.tasks import calculate_credit_score

class Command(BaseCommand):
    help = 'Calculate credit score for all users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            calculate_credit_score.delay(user.id)
        self.stdout.write(self.style.SUCCESS('Successfully started credit score calculations for all users'))
