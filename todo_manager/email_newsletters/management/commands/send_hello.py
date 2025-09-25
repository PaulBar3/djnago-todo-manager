from django.core.management import BaseCommand
from django.core.mail import send_mail


class Command(BaseCommand):
    help = "Send example hello email"

    def handle(self, *args, **options):
        self.stdout.write("Send email")

        send_mail(
            "Subject here",
            "Here is the welcoming message.",
            "admin@example.com",
            ["user@example.com"],
            fail_silently=False,
        )

        self.stdout.write(self.style.SUCCESS("Email sent"))
