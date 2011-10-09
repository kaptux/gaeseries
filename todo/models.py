from google.appengine.ext import db

class Todo(db.Model):
    content = db.StringProperty()
    done = db.BooleanProperty()

    def to_dict(self):
        return dict(id=self.key().id(),
                    content=self.content,
                    done=self.done,
                   )
