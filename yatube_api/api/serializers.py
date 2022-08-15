from rest_framework import serializers
from posts.models import Group, Post, Comment, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        fields = ('id', 'author',
                  'pub_date', 'text', 'group')
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate_following(self, value):
        user = self.context['request'].user
        if Follow.objects.filter(user=user,
                                 following__username=value).exists():
            raise serializers.ValidationError("Подписка уже оформлена")
        return value

    def validate(self, value):
        if self.context['request'].user == value['following']:
            raise serializers.ValidationError(
                'Подписка на себя запрещена')
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title')
        model = Group
