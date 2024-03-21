from rest_framework import serializers
from configuration.models import Configuration, SocialLinks, Navbar
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data.get("email"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            username=validated_data.get("username"),
            password=validated_data.get("password")
        )
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = '__all__'


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = ['id', 'title', 'nav_link', 'is_active', 'priority',
                  'created_at', 'updated_at']


class ConfigurationSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True, read_only=True)
    navbar = NavbarSerializer(many=True, read_only=True)

    class Meta:
        model = Configuration
        fields = ['title', 'meta_title', 'post_count', 'social_links',
                  'navbar', 'is_search', 'created_at', 'updated_at']
