from controllers.base import Controllers
from views.base import View


def main():
    vue = View()

    test = Controllers(vue)

    test.launch_app()


if __name__ == "__main__":
    main()
