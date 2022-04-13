from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, ReviewViewSet, CategoryViewSet, GenreViewSet, TitleViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'^titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet,
                basename='review')
router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
