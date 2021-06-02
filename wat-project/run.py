from Setting import OpenInit

openInit = OpenInit()
app = openInit.app()

if __name__ == "__main__":
    app.run(debug=True, threaded=True)