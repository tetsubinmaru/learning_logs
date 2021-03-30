from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name="topic"),
    path('new_topic/', views.new_topic, name='new_topic'),
    # 新規記事の追加ページ
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 記事の編集ページ
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry"),
]