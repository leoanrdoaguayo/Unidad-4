from django.db import models
from part1.managers import AlbumManager, SongManager


class Artist(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return u'%s' % self.name


class Album(models.Model):
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist)
    release_date = models.DateField()
    object = AlbumManager()

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def year(self):
        return self.release_date.year


class Song(models.Model):
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    object = SongManager()
