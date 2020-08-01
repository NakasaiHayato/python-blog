from django.db import models

# Create your models here.
class Post(models.Model):
  # 文字型定義, 最大100文字
  title = models.CharField(max_length=100)
  # 日付型
  published = models.DateTimeField()
  # 画像アップするための型
  image = models.ImageField(upload_to='media/')
  # テキスト型
  body = models.TextField()

  # 投稿タイトルをページに表示
  def __str__(self):
    return self.title

  def summary(self):
    # 先頭から３０文字だけ表示する
    return self.body[:30]