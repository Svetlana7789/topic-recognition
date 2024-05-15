import json
import csv


def get_report(top_words, destination: str = "stdout"):
    base_path = "reports"

    match destination.rsplit(".", maxsplit=1):
        case ["stdout"]:
            print(top_words)
        case [_, "json"]:
            with open(f"{base_path}\{destination}", "w", encoding="utf-8") as fp:
                json.dump(dict(top_words), fp, ensure_ascii=False, indent=2)
        case [filename, "xls" | "xlsx" | "csv" | "tsv"]:
            with open(f"{base_path}\{filename}.csv", "w", newline="") as fp:
                writer = csv.writer(fp)
                writer.writerows(top_words)


# TODO: сортировать репорты по директориям с датой
