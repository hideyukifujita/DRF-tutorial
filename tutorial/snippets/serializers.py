from rest_framework import serializers
from django.contrib.auth.models import User

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]

    def create(self, validated_data):
        """validated_dataを受け取って、Snippetオブジェクトを返す

        Args:
            validated_data (dict): バリデーションデータ

        Returns:
            Snippet: Snippetオブジェクト
        """
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """instance, validatedを受け取って、既存のSnippetインスタンスを更新して返す

        Args:
            instance (Snippet): 既存のSnippetインスタンス
            validated_data (dict): バリデーションデータ

        Returns:
            Snippet: Snippetインスタンス
        """
        instance.title = validated_data.get("title", instance.title)
        instance.code = validated_data.get("code", instance.code)
        instance.linenos = validated_data.get("linenos", instance.linenos)
        instance.language = validated_data.get("language", instance.language)
        instance.style = validated_data.get("style", instance.style)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]