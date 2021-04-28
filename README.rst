Pelican Podcast
########################################################################

This plugins adds a feed generator and feed writer for your podcast.

**Alert:** Still in early development stage.

Installation from Source
========================================================================
You can install this as a source package in the following way:

::

   python setup.py install

   or

   python setup.py develop

You can read more about how to install and use Pelican plugins in the
official Pelican documentation:
http://docs.getpelican.com/en/stable/plugins.html .


Available Settings
========================================================================

These are implemented as variables in the pelicanconf file.

::

  PODCAST_PATH = u''
  PODCAST_TITLE = u''
  PODCAST_EXPLICIT = u''
  PODCAST_LANGUAGE = u''
  PODCAST_COPYRIGHT = u''
  PODCAST_SUBTITLE = u''
  PODCAST_AUTHOR = u''
  PODCAST_SUMMARY = u''
  PODCAST_IMAGE = u''
  PODCAST_OWNER_NAME = u''
  PODCAST_OWNER_EMAIL = u''
  PODCAST_CATEGORY = ['iTunes Category','iTunes Subcategory']
  PODCAST_LOCKED = u''

In order to verify that your RSS feed for your podcast is being
correctly generated, you can visit `example.com/` +
`PODCAST_FEED_PATH` to download a copy of the feed. So, for example,
if you had set your `PODCAST_FEED_PATH` to "podcast" in your
pelicanconf file, and your website was example.com, you would visit
`example.com/PODCAST_FEED_PATH` to download a copy of the RSS Feed.

You can then take this RSS feed, and use a validator meant for RSS
feeds. This validator can help you fix any other issues you have with
the configuration of your podcast feed.

Multiple Podcast Feeds
========================================================================

You can optionally have a separate podcast feed for different content
categories. To use this feature, you'll need to create a nested
dictionary, called PODCASTS, with one sub dictionary for each category
slug that you want to put into a separate podcast feed. (All of the
episodes will continue to appear in the main feed as well, making it a
master feed of all episodes.)

You can override specific configuration settings from the master
feed. Everything that's not explicitly specified will be inherited
from the master feed settings.

::

  PODCASTS = {
  	'category-slug-1': {
  		'PODCAST_PATH': u'',
  		'PODCAST_TITLE': u'',
  		'PODCAST_SUBTITLE': u'',
  		'PODCAST_SUMMARY': u'',
  		'PODCAST_IMAGE': u'',
  	},
  	'category-slug-2': {
  		'PODCAST_PATH': u'',
  		'PODCAST_TITLE': u'',
  		'PODCAST_SUBTITLE': u'',
  		'PODCAST_SUMMARY': u'',
  		'PODCAST_IMAGE': u'',
  	},
  }

Publishing a Podcast
========================================================================
You'll have to upload your MP4 somewhere into your Pelican static site
separately, this plugin only creates the RSS feed necessary for
distributing your podcast.  After uploading your MP4 you'll have to
supply the following configuration at the top of your post (each post
represents a podcast episode, when configured with :podcast:):

::

   :status: published
   :podcast: http://www.example.com/url/to/mp4
   :length: 4645384
   :duration: 4:51
   :description: Some description for your podcast episode


Please note that the length is in bytes, whereas the duration is how
long (timewise) the MP4 file is.

Podcasting 2.0
========================================================================

::
    PODCAST_LOCKED = False
    
    PODCAST_LOCKED = True
    PODCAST_OWNER_EMAIL = ''


    PODCAST_FUNDING = [
        ['Paypal', 'https://paypal.me/davekeeshan'],
        ['Patreon', 'https://patreon.com/davekeeshan'],
    ]
