from rest_framework.serializers import ModelSerializer

from shortener.models import Urls


class UrlsSerializer(ModelSerializer):
    class Meta:
        model = Urls
        fields = [
            'id',
            'short_id',
            'http_url',
            'pub_date',
            'nums_of_visits',
            'want_edit'
        ]

    def update(self, instance, validated_data):
        url = Urls.objects.get(pk=instance.id)
        # Urls.objects.filter(pk=instance.id).update(**validated_data)
        if validated_data['want_edit'] is True:
            url.short_id = validated_data['short_id']
            url.save()
        return url
