from rest_framework import mixins
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        """requestを受け取って、Snippetのリストを取得する

        Args:
            request (HttpRequest): HttpRequestオブジェクト

        Returns:
            Response: JSON
        """
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """requestを受け取って、Snippetを作成する

        Args:
            request (HttpRequest): HttpRequestオブジェクト

        Returns:
            Response: JSON
        """
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        """requestを受け取って、Snippetを取得する

        Args:
            request (HttpRequest): HttpRequestオブジェクト

        Returns:
            Response: JSON
        """
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        """requestを受け取って、Snippetを更新する

        Args:
            request (HttpRequest): HttpRequestオブジェクト

        Returns:
            Response: JSON
        """
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        """requestを受け取って、Snippetを削除する

        Args:
            request (HttpRequest): HttpRequestオブジェクト

        Returns:
            Response: ステータスコード
        """
        return self.destroy(request, *args, **kwargs)