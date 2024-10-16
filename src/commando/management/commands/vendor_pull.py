import helpers
from typing import Any

from django.core.management.base import BaseCommand
from django.conf import settings

STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

VENDOR_STATICFILES = {
    "saas-theme.min.css":"https://raw.githubusercontent.com/codingforentrepreneurs/SaaS-Foundations/refs/heads/main/src/staticfiles/theme/saas-theme.min.css",
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js",
    "flowbite.min.js.map":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.5.1/flowbite.js.map"
}


class Command(BaseCommand):
    
    def handle(self, *args:Any, **options:Any):
        self.stdout.write("Downloading vendor static files")
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {url}")
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("Successfully updated all vendor static files.")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Some files were not updated.")
            )