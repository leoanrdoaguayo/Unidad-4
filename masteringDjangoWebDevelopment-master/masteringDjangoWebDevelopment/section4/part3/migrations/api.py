from tastypie.resources import ModelResource
from part1.models import Artist, Album, Song
from tastypie import fields
from tastypie.api import Api
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authentication import DjangoAuthorization
from tastypie.exceptions import InvalidFilterError
import datetime


class AuthenticationMixim(object):
    def __init__(self):
        self._meta.authentication = ApiKeyAuthentication()
        self._meta.authorization = DjangoAuthorization()
        super(AuthenticationMixim, self).__init__()


class ArtistResource(AuthenticationMixim, ModelResource):
    class Meta:
        queryset = Artist.objects.all()
        resource_name = 'artist'


class AlbumResource(AuthenticationMixim, ModelResource):
    artist = fields.ForeignKey(ArtistResource, 'artist')

    class Meta:
        queryset = Album.objects.all()
        resource_name = 'album'

    def dehydrate(self, bundle):
        bundle.date['year'] = bundle.obj.year
        return bundle
    def build_filters(self, filters=None):
        res = super(AlbumResource, self).build_filters(filters)

        if 'year' in filters:
            try:
                res.update({'year': int(filters['year'])})

            except:
                raise  InvalidFilterError('year must be an integer!')
        return  res
    def appy_filters(self, request, applicable_filters):
        year = applicable_filters.pop('year', None)
        qs = super(AlbumResource, self).appy_filters(request, applicable_filters)

        if year is not None:
            return qs.filter(
                release_date__gte = datetime.date(year,1,1),
                release_date__lte = datetime.date(year,12,31))
        return qs


class SongResource(AuthenticationMixim, ModelResource):
    artist = fields.ForeignKey(ArtistResource, 'artist')
    album = fields.ForeignKey(AlbumResource, 'album')

    class Meta:
        queryset = Song.objects.all()
        resource_name = 'song'

