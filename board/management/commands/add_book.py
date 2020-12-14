from django.core.management.base import BaseCommand
from datetime import *
from board.models import BookStore


class Command(BaseCommand):
    help = 'Create Book Data'

    def handle(self, *args, **options):
        today = datetime.now().date()
        for i in range(1, 2000001):
            title = f"judul buku wisata book {i} untuk test {i}"
            short = f"ini merupakan short summary buku {i}, jadi ini sebagai contoh saja. cerita di buku {i} cuma fiksi. terima kasih"
            BookStore.objects.create(title=title, short_summary=short, published_date=today)
