from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# 投稿一覧画面のメソッド
def index(request):
  # return HttpResponse("Hello World")
  # -published: 降順でデータを並び替え
  posts = Post.objects.order_by('-published')
  # index.htmlをrenderする
  return render(request, 'posts/index.html', {'posts': posts})

# 投稿詳細画面のメソッド
def post_detail(request, post_id):
  # 投稿データが帰ってこない時404エラーを返す
  post = get_object_or_404(Post, pk=post_id)
  return render(request, 'posts/post_detail.html', {'post': post})

# アバウト画面のメソッド
def about(request):
  return render(request, 'posts/about.html')

# Create your views here.
