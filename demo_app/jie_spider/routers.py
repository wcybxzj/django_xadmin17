class JieSpiderRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'jie_spider':
            return 'jie_data'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'jie_spider':
            return 'jie_data'
        return None

    def allow_syncdb(self, db, model):
        if db == 'jie_data':
            return model._meta.app_label == 'jie_spider'
        elif model._meta.app_label == 'jie_spider':
            return False
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        if obj1._meta.app_label == 'jie_spider' and obj2._meta.app_label == 'jie_spider':
            return True
        # Allow if neither is chinook app
        elif 'jie_spider' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False
