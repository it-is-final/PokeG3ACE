import argparse
import sys
from pathlib import Path


def validate_input(payload_path: Path):
    payload: list[int] = []
    with payload_path.open(encoding="utf-8") as f:
        for line in f:
            try:
                if (raw_part_payload := line.split("#", 1)[0].strip()) == '':
                    continue
                part_payload = int(raw_part_payload, 16)
                if not 0 <= part_payload <= 0xFFFF:
                    raise ValueError(line.strip())
            except ValueError as e:
                print(f"{e.args} is not a valid hexadecimal 16-bit number")
                sys.exit(1)
            else:
                payload.append(part_payload)
    return payload


def convert_payload(payload: list[int]):
    i_payload = iter(payload)
    out: list[int] = []
    for short in i_payload:
        out.append(
            short | (next(i_payload, 0xFFFF) << 16)
        )
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "payload",
        type=Path,
        help="A .txt file containing the payload you are trying to convert",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(__file__).absolute().parent / "CodeGeneratorInput.txt",
        help="Where to save the result",
    )
    args = parser.parse_args()
    output_path: Path = args.output
    payload = validate_input(args.payload)
    converted_payload = convert_payload(payload)
    with output_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("@@\n")
        for part in converted_payload:
            f.write(f"0x{part:08X}\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
