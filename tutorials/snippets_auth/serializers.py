from django.contrib.auth.models import User

from rest_framework import serializers

# from tutorials.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance: Snippet, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

from tutorials.snippets_auth.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    """
    It's important to remember that ModelSerializer classes don't do anything particularly magical, 
    they are simply a shortcut for creating serializer classes:

    An automatically determined set of fields.
    Simple default implementations for the create() and update() methods.
    """

    # This field is doing something quite interesting.
    # The source argument controls which attribute is used to populate a field,
    # and can point at any attribute on the serialized instance.
    # It can also take the dotted notation shown above,
    # in which case it will traverse the given attributes,
    # in a similar way as it is used with Django's template language.
    #
    # The field we've added is the untyped ReadOnlyField class,
    # in contrast to the other typed fields, such as CharField,
    # BooleanField etc... The untyped ReadOnlyField is always read-only,
    # and will be used for serialized representations, 
    # but will not be used for updating model instances when they are deserialized. 
    # We could have also used CharField(read_only=True) here.
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'owner', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):
        # Because 'snippets' is a reverse relationship on the User model, 
        # it will not be included by default when using the ModelSerializer class, 
        # so we needed to add an explicit field for it.
        snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

        class Meta:
            model = User
            fields = ['id', 'username', 'snippets']
        