from django.apps import AppConfig


class ActionsConfig(AppConfig):
    name = 'Actions'

    def ready(self):
        import Actions.signals
