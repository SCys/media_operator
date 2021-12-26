from core import Application

import media.handlers


def main():
    app = Application(
        [
            (r"/api/media/convert", media.handlers.APIConvert),
            (r"/api/media/probe", media.handlers.APIProbe),
        ],
        client_max_size=2 << 32,  # 8G
    )

    app.start()


if __name__ == "__main__":
    main()
