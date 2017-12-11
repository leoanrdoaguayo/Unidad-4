from linecache import cache

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from section4.part1.migrations.managers import SongManager
from section5.part1.templates.models import Favorite, Album, Artist


class Song(models.Model):
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    fovorite_set = GenericRelation(Favorite)
    object = SongManager()

    def __unicode__(self):
        return u'%s -%s' % (self.artist, self.title)

    def save(self, *args, **kwargs):
        super(Song, self).save(*args, **kwargs)
        cache.delete('song-%s' % self.pk)