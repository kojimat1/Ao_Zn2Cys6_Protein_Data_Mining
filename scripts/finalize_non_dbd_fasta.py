#!/usr/bin/env python3
"""Create the final non-DBD FASTA, including the C-terminal-DBD exception."""
from pathlib import Path
import argparse

FOCAL_EXCEPTION = "AO090012000182-P"


def read_fasta(path):
    records = []
    name = None
    seq = []
    with Path(path).open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if name is not None:
                    records.append((name, "".join(seq)))
                name = line[1:].split()[0]
                seq = []
            else:
                seq.append(line)
    if name is not None:
        records.append((name, "".join(seq)))
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-non-dbd", default="aor0-5_non_SM00066_domains.faa")
    parser.add_argument("--full-length", default="aor0-5.faa")
    parser.add_argument("--sm00066-tsv", default="aor0-5_SM00066.tsv")
    parser.add_argument("--output", default="aor0-5_non_SM00066_domains_AO090012000182_fixed.faa")
    args = parser.parse_args()

    raw = read_fasta(args.raw_non_dbd)
    full = dict(read_fasta(args.full_length))

    dbd_start = None
    with Path(args.sm00066_tsv).open(encoding="utf-8") as handle:
        for line in handle:
            cols = line.rstrip("\n").split("\t")
            if cols and cols[0] == FOCAL_EXCEPTION:
                start = int(cols[6])
                dbd_start = start if dbd_start is None else min(dbd_start, start)
    if dbd_start is None:
        raise ValueError(f"No SM00066 annotation found for {FOCAL_EXCEPTION}")
    if FOCAL_EXCEPTION not in full:
        raise ValueError(f"No full-length sequence found for {FOCAL_EXCEPTION}")

    exception_sequence = full[FOCAL_EXCEPTION][: dbd_start - 1]
    output_records = [(header.split("|", 1)[0], seq) for header, seq in raw]
    output_records.append((FOCAL_EXCEPTION, exception_sequence))

    text = "\n".join(f">{header}\n{seq}" for header, seq in output_records)
    Path(args.output).write_text(text, encoding="utf-8")

    print(f"Wrote {len(output_records)} sequences to {args.output}")
    print(f"{FOCAL_EXCEPTION}: residues 1-{dbd_start - 1} ({len(exception_sequence)} aa)")


if __name__ == "__main__":
    main()
