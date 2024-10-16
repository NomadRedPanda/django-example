import logging
logger = logging.getLogger(__name__)

try:
    from decouple import config
except ImportError:
    logger.info('python-decouple is not installed, using os.environ')
    import os
    config = os.environ.get

CLOUDFLARE_R2_CONFIG_OPTIONS = {}

CLOUDFLARE_R2_BUCKET=config('CLOUDFLARE_R2_BUCKET', cast=str)
CLOUDFLARE_R2_ACCESS_KEY=config('CLOUDFLARE_R2_ACCESS_KEY', cast=str)
CLOUDFLARE_R2_SECRET_KEY=config('CLOUDFLARE_R2_SECRET_KEY', cast=str)
CLOUDFLARE_R2_BUCKET_ENDPOINT=config('CLOUDFLARE_R2_BUCKET_ENDPOINT', cast=str)


if all([CLOUDFLARE_R2_BUCKET, CLOUDFLARE_R2_ACCESS_KEY, CLOUDFLARE_R2_SECRET_KEY, CLOUDFLARE_R2_BUCKET_ENDPOINT]):
    CLOUDFLARE_R2_CONFIG_OPTIONS = {
        "bucket_name": CLOUDFLARE_R2_BUCKET,
        'access_key': CLOUDFLARE_R2_ACCESS_KEY,
        'secret_key': CLOUDFLARE_R2_SECRET_KEY,
        'endpoint_url': CLOUDFLARE_R2_BUCKET_ENDPOINT,
        'default_acl': "public-read", # private
        "signature_version": "s3v4",
    }