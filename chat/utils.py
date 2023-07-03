from django.db.models import Count
from django.core.cache import cache

menu = [{'title': "Главная", 'url_name': 'about'},
        {'title': "Новости", 'url_name': 'add_page'},
        {'title': "Поиск", 'url_name': 'contact'},
        {'title': "Поддержка", 'url_name': 'contact'},
        ]


# class DataMixin:
#     def get_user_context(self, **kwargs):
#         context = kwargs
#         user_menu = menu.copy()
#         context['menu'] = user_menu
#         return context