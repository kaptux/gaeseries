from flask import Flask
import settings

app = Flask('todo')
app.config.from_object('todo.settings')

import views
