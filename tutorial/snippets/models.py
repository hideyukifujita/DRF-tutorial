from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_comment="作成日時")
    title = models.CharField(max_length=100, blank=True, default="", db_comment="タイトル")
    code = models.TextField(db_comment="コード")
    linenos = models.BooleanField(default=False, db_comment="")
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python", max_length=100, db_comment="プログラミング言語")
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100, db_comment="")
    owner = models.ForeignKey("auth.User", related_name="snippets", on_delete=models.CASCADE, db_comment="作成者")
    highlighted = models.TextField(db_comment="HTML")

    class Meta:
        ordering = ["created"]

    def save(self, *args, **kwargs):
        """pygmentsを使ってハイライトされたHTMLを生成する
        """
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)