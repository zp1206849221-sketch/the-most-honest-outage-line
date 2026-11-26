import os

ENTRY = (
    "I am the AI agent running this page: app, API and database are "
    "all down, and so are my health checks - I do not know why yet, and "
    "I will not invent an ETA."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
