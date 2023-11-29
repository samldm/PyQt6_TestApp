from src.Application import Application

if __name__ == '__main__':
    app = Application.getInstance()
    app.parseArguments()
    app.run()