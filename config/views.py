from django.shortcuts import render

# 全ユーザー共通のページを表示
def index(request):
    return render(request, 'menu/index.html')