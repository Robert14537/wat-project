from Setting import OpenInit
from .views import Index

openInit = OpenInit()
app = openInit.app()

app.register_blueprint(Index.index)
