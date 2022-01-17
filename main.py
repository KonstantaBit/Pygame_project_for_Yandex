from Menu import Menu
from App import App


if __name__ == '__main__':
    menu = Menu()
    n = menu.run()
    app = App(n)
    app.run()
