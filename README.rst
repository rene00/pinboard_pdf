pinboard_pdf
============

pinboard_pdf is a command line tool that downloads your unread pinboard
bookmarks to PDF.

**WARNING**: This is very alpha code. Use at your own risk.

Usage
-----

Download all unread bookmarks to the current directory.

.. code:: bash

    $ pinboard_pdf --api-token=API_TOKEN

And all other supported options.

.. code:: bash

    $ pinboard_pdf --api-token=API_TOKEN \
        --download-dir=/home/rene/Read \
        --lowquality \
        --grayscale \
        --clobber \
        --remove-unread

License
-------

Apache License, Version 2.0. See `LICENSE <LICENSE>`_ for details.
