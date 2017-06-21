#!/usr/bin/env python

import click
import pinboard
import pdfkit
import os
import logging
from urlparse import urlparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def sanitize_filename(url, download_dir):
    """Generate a clean filename."""
    filename = urlparse(url).path
    filename = filename.replace('/', '')
    filename = filename.split('.')[0]
    return os.path.join(download_dir, '{0}.pdf'.format(filename))


def wkhtmlpdf_opts(lowquality, quiet, grayscale):
    options = dict()
    if grayscale:
        options['grayscale'] = ''
    if lowquality:
        options['lowquality'] = ''
    if quiet:
        options['quiet'] = ''
    return options


def download_url(url, filename, options=None, clobber=False):
    if not os.path.exists(filename) or clobber:
        r = pdfkit.PDFKit(url, 'url', options=options)
        r.to_pdf(filename)
        logger.info('Saved {0} to {1}.'.format(url, filename))
    else:
        logger.info('{0} already exists, not clobbering.'.format(filename))


@click.command()
@click.option('--api-token', required=True)
@click.option('--download-dir', required=False, default=os.getcwd())
@click.option('--remove-unread', is_flag=True, default=False)
@click.option('--lowquality', is_flag=True, default=False)
@click.option('--quiet', is_flag=True, default=True)
@click.option('--grayscale', is_flag=True, default=False)
@click.option('--clobber', is_flag=True, default=False)
@click.option('--pinboard-pdf-tag', is_flag=True, default=True)
@click.option('--pinboard-pdf-tag-name', required=False,
              default='pinboard_pdf')
def pinboard_pdf(api_token, download_dir, remove_unread, lowquality, quiet,
                 grayscale, pinboard_pdf_tag_name, pinboard_pdf_tag, clobber):
    pb = pinboard.Pinboard(api_token)
    options = wkhtmlpdf_opts(lowquality, quiet, grayscale)
    for bm in pb.posts.all(toread=True):
        filename = sanitize_filename(bm.url, download_dir)
        success = True
        try:
            download_url(bm.url, filename, options=options, clobber=clobber)
        except IOError:
            pass
        else:
            success = False
        finally:
            if remove_unread:
                bm.toread = False
                logger.info('Removing {0} from unread.'.format(bm.url))
                if pinboard_pdf_tag:
                    bm.tags.append(pinboard_pdf_tag_name)
                    logger.info('Tagging {0} with {1}'.
                                format(bm.url, pinboard_pdf_tag_name))
                bm.save()


if __name__ == '__main__':
    pinboard_pdf()
