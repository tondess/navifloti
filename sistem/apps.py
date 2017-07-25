from django.apps import AppConfig
 
 
class sistemConfig(AppConfig):
    name = 'sistem'
    verbose_name = 'sistem Application'
 
    def ready(self):
        import sistem.signals